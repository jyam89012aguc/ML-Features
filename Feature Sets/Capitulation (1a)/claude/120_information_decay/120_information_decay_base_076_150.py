"""
120_information_decay — Base Features 076-150
Domain: information decay — mutual information proxies, GARCH-style variance decay,
        cross-lag correlation structure, signal-to-noise decay, entropy of return series,
        volume-weighted decay, range-based persistence, additional half-life variants
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _returns(close: pd.Series) -> pd.Series:
    """Simple log returns; NaN-safe."""
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation at given lag over window w. NaN-safe."""
    def _ac(x):
        x = x[~np.isnan(x)]
        if len(x) < lag + 3:
            return np.nan
        x0 = x[:-lag]
        x1 = x[lag:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    return s.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _decay_rate_from_two_lags(ac_lag1: pd.Series, ac_lag2: pd.Series) -> pd.Series:
    """Exponential decay rate from two autocorrelations: lambda = -log(|ac2|/|ac1|)."""
    ratio = _safe_div(ac_lag2.abs(), ac_lag1.abs().clip(lower=_EPS))
    ratio_clipped = ratio.clip(lower=_EPS, upper=1.0 - _EPS)
    return -np.log(ratio_clipped)


def _halflife_from_decay(decay_rate: pd.Series) -> pd.Series:
    """Half-life = log(2)/lambda."""
    return np.log(2.0) / decay_rate.clip(lower=_EPS)


def _mi_proxy_two_series(x: np.ndarray, y: np.ndarray, bins: int = 5) -> float:
    """
    Proxy for mutual information using histogram discretization.
    Returns normalized MI in [0, 1]. NaN-safe.
    """
    valid = np.isfinite(x) & np.isfinite(y)
    x, y = x[valid], y[valid]
    if len(x) < bins * 2:
        return np.nan
    try:
        hist_xy, _, _ = np.histogram2d(x, y, bins=bins)
        hist_x = hist_xy.sum(axis=1)
        hist_y = hist_xy.sum(axis=0)
        n = hist_xy.sum()
        if n == 0:
            return np.nan
        px = hist_x / n
        py = hist_y / n
        pxy = hist_xy / n
        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if pxy[i, j] > 0 and px[i] > 0 and py[j] > 0:
                    mi += pxy[i, j] * np.log(pxy[i, j] / (px[i] * py[j]))
        hx = -np.sum(px[px > 0] * np.log(px[px > 0]))
        hy = -np.sum(py[py > 0] * np.log(py[py > 0]))
        denom = max(hx, hy, _EPS)
        return float(mi / denom)
    except Exception:
        return np.nan


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Mutual information decay across lags ---

def idc_076_mi_lag1_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-1] over trailing 63-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
    return pd.Series(result, index=close.index)


def idc_077_mi_lag3_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-3] over trailing 63-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    lag = 3
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_078_mi_lag5_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-5] over trailing 63-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    lag = 5
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_079_mi_lag10_returns_126d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-10] over trailing 126-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    lag = 10
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_080_mi_decay_lag1_to_lag3_63d(close: pd.Series) -> pd.Series:
    """MI decay: MI(lag=1) minus MI(lag=3) over 63-day window (drop-off rate)."""
    r = _returns(close).values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi3 = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
        mi3[i] = _mi_proxy_two_series(seg[3:], seg[:-3])
    s1 = pd.Series(mi1, index=close.index)
    s3 = pd.Series(mi3, index=close.index)
    return s1 - s3


def idc_081_mi_decay_lag1_to_lag5_63d(close: pd.Series) -> pd.Series:
    """MI decay: MI(lag=1) minus MI(lag=5) over 63-day window."""
    r = _returns(close).values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi5 = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
        mi5[i] = _mi_proxy_two_series(seg[5:], seg[:-5])
    s1 = pd.Series(mi1, index=close.index)
    s5 = pd.Series(mi5, index=close.index)
    return s1 - s5


def idc_082_mi_decay_ratio_lag3_to_lag1_63d(close: pd.Series) -> pd.Series:
    """MI ratio MI(lag=3)/MI(lag=1) over 63-day window: near 0 = fast decay."""
    r = _returns(close).values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi3 = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
        mi3[i] = _mi_proxy_two_series(seg[3:], seg[:-3])
    s1 = pd.Series(mi1, index=close.index).clip(lower=_EPS)
    s3 = pd.Series(mi3, index=close.index)
    return _safe_div(s3, s1)


def idc_083_mi_lag1_abs_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between |return[t]| and |return[t-1]| over 63-day window (vol MI)."""
    r = _returns(close).abs().values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
    return pd.Series(result, index=close.index)


def idc_084_mi_lag5_abs_returns_126d(close: pd.Series) -> pd.Series:
    """MI proxy between |return[t]| and |return[t-5]| over 126-day window."""
    r = _returns(close).abs().values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    lag = 5
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_085_mi_vol_decay_ratio_lag5_to_lag1_126d(close: pd.Series) -> pd.Series:
    """Ratio of MI at lag=5 to lag=1 for |returns| over 126-day window (vol decay rate)."""
    r = _returns(close).abs().values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi5 = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
        mi5[i] = _mi_proxy_two_series(seg[5:], seg[:-5])
    s1 = pd.Series(mi1, index=close.index).clip(lower=_EPS)
    s5 = pd.Series(mi5, index=close.index)
    return _safe_div(s5, s1)


def idc_086_mi_pct_rank_lag1_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day MI(lag=1) in trailing 252-day distribution."""
    mi = idc_076_mi_lag1_returns_63d(close)
    return mi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_087_mi_decay_zscore_lag1_to_lag5_63d(close: pd.Series) -> pd.Series:
    """Z-score of MI decay (lag1-lag5) relative to its 252-day distribution."""
    decay = idc_081_mi_decay_lag1_to_lag5_63d(close)
    m = _rolling_mean(decay, _TD_YEAR)
    s = _rolling_std(decay, _TD_YEAR)
    return _safe_div(decay - m, s)


def idc_088_mi_lag1_sq_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between squared return[t] and squared return[t-1] (variance MI)."""
    r = (_returns(close) ** 2).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
    return pd.Series(result, index=close.index)


def idc_089_mi_lag3_sq_returns_126d(close: pd.Series) -> pd.Series:
    """MI proxy between squared return[t] and squared return[t-3] over 126-day window."""
    r = (_returns(close) ** 2).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    lag = 3
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy_two_series(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_090_mi_vol_halflife_63d(close: pd.Series) -> pd.Series:
    """
    MI-based volatility half-life: ratio MI(lag=3)/MI(lag=1) for |returns|.
    Used to derive half-life = -3*log(2)/log(ratio+EPS).
    """
    r = _returns(close).abs().values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi3 = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy_two_series(seg[1:], seg[:-1])
        mi3[i] = _mi_proxy_two_series(seg[3:], seg[:-3])
    s1 = pd.Series(mi1, index=close.index).clip(lower=_EPS)
    s3 = pd.Series(mi3, index=close.index).clip(lower=_EPS)
    ratio = _safe_div(s3, s1)
    ratio_c = ratio.clip(lower=_EPS, upper=1.0 - _EPS)
    return -3.0 * np.log(2.0) / np.log(ratio_c + _EPS)


# --- Group G (091-110): GARCH-style variance decay and volatility persistence ---

def idc_091_garch_alpha_proxy_63d(close: pd.Series) -> pd.Series:
    """
    GARCH(1,1) alpha proxy: correlation of squared return[t] with squared return[t-1]
    over 63-day window. Higher = more ARCH effect (slower variance decay).
    """
    r2 = (_returns(close) ** 2)
    return _rolling_autocorr(r2, _TD_QTR, 1)


def idc_092_garch_alpha_proxy_126d(close: pd.Series) -> pd.Series:
    """GARCH alpha proxy over 126-day window."""
    r2 = (_returns(close) ** 2)
    return _rolling_autocorr(r2, _TD_HALF, 1)


def idc_093_garch_alpha_proxy_252d(close: pd.Series) -> pd.Series:
    """GARCH alpha proxy over 252-day window."""
    r2 = (_returns(close) ** 2)
    return _rolling_autocorr(r2, _TD_YEAR, 1)


def idc_094_variance_persistence_lag2_63d(close: pd.Series) -> pd.Series:
    """AC(2) of squared returns over 63-day window (2nd-order variance persistence)."""
    r2 = (_returns(close) ** 2)
    return _rolling_autocorr(r2, _TD_QTR, 2)


def idc_095_variance_persistence_lag5_126d(close: pd.Series) -> pd.Series:
    """AC(5) of squared returns over 126-day window (weekly variance persistence)."""
    r2 = (_returns(close) ** 2)
    return _rolling_autocorr(r2, _TD_HALF, 5)


def idc_096_garch_beta_proxy_63d(close: pd.Series) -> pd.Series:
    """
    GARCH beta proxy (long-run variance persistence):
    ratio AC(5)/AC(1) of squared returns over 63-day window.
    """
    r2 = (_returns(close) ** 2)
    ac1 = _rolling_autocorr(r2, _TD_QTR, 1).clip(lower=_EPS)
    ac5 = _rolling_autocorr(r2, _TD_QTR, 5)
    return _safe_div(ac5, ac1)


def idc_097_garch_halflife_variance_63d(close: pd.Series) -> pd.Series:
    """Half-life of variance from AC(1)/AC(2) of squared returns, 63-day window."""
    r2 = (_returns(close) ** 2)
    ac1 = _rolling_autocorr(r2, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r2, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_098_garch_halflife_variance_126d(close: pd.Series) -> pd.Series:
    """Half-life of variance from AC(1)/AC(2) of squared returns, 126-day window."""
    r2 = (_returns(close) ** 2)
    ac1 = _rolling_autocorr(r2, _TD_HALF, 1)
    ac2 = _rolling_autocorr(r2, _TD_HALF, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_099_vol_shock_decay_5d_ewm21(close: pd.Series) -> pd.Series:
    """
    Ratio of 5-day EWM variance to 21-day EWM variance.
    High ratio = recent shock not yet absorbed (slow decay).
    """
    r2 = _returns(close) ** 2
    ev5 = r2.ewm(span=_TD_WEEK, min_periods=2).mean()
    ev21 = r2.ewm(span=_TD_MON, min_periods=5).mean()
    return _safe_div(ev5, ev21.clip(lower=_EPS))


def idc_100_vol_shock_decay_21d_ewm63(close: pd.Series) -> pd.Series:
    """Ratio of 21-day EWM variance to 63-day EWM variance."""
    r2 = _returns(close) ** 2
    ev21 = r2.ewm(span=_TD_MON, min_periods=5).mean()
    ev63 = r2.ewm(span=_TD_QTR, min_periods=15).mean()
    return _safe_div(ev21, ev63.clip(lower=_EPS))


def idc_101_vol_shock_decay_63d_ewm252(close: pd.Series) -> pd.Series:
    """Ratio of 63-day EWM variance to 252-day EWM variance."""
    r2 = _returns(close) ** 2
    ev63 = r2.ewm(span=_TD_QTR, min_periods=15).mean()
    ev252 = r2.ewm(span=_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(ev63, ev252.clip(lower=_EPS))


def idc_102_vol_halflife_ewm_fit_21d(close: pd.Series) -> pd.Series:
    """
    EWM half-life fitted from AC(1) of squared returns over 21-day window
    (GARCH-style short-window variance half-life).
    """
    r2 = _returns(close) ** 2
    ac1 = _rolling_autocorr(r2, _TD_MON, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


def idc_103_vol_halflife_ewm_fit_63d(close: pd.Series) -> pd.Series:
    """EWM half-life of squared returns fitted from AC(1) over 63-day window."""
    r2 = _returns(close) ** 2
    ac1 = _rolling_autocorr(r2, _TD_QTR, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


def idc_104_vol_halflife_ewm_fit_252d(close: pd.Series) -> pd.Series:
    """EWM half-life of squared returns fitted from AC(1) over 252-day window."""
    r2 = _returns(close) ** 2
    ac1 = _rolling_autocorr(r2, _TD_YEAR, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


def idc_105_garch_alpha_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day GARCH alpha proxy in trailing 252-day distribution."""
    a = idc_091_garch_alpha_proxy_63d(close)
    return a.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_106_variance_halflife_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day variance half-life in trailing 252-day distribution."""
    hl = idc_097_garch_halflife_variance_63d(close)
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_107_vol_shock_decay_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5d/21d EWM variance ratio vs its 252-day distribution."""
    ratio = idc_099_vol_shock_decay_5d_ewm21(close)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def idc_108_vol_decay_slope_lags_1_to_5_63d(close: pd.Series) -> pd.Series:
    """
    OLS slope of AC(k) of squared returns for k=1..5 over 63-day window.
    Steeper negative slope = faster variance decay.
    """
    def _slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 15:
            return np.nan
        lags = [1, 2, 3, 4, 5]
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs)
        if valid.sum() < 2:
            return np.nan
        lags_v = np.array(lags, dtype=float)[valid]
        if lags_v.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags_v, acs[valid], 1)[0])
    r2 = (_returns(close) ** 2).values
    n = len(r2)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _slope(r2[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_109_ewm_vol_halflife_ratio_short_to_long(close: pd.Series) -> pd.Series:
    """Ratio of 21-day vol EWM half-life to 252-day vol EWM half-life."""
    hl21 = idc_102_vol_halflife_ewm_fit_21d(close)
    hl252 = idc_104_vol_halflife_ewm_fit_252d(close)
    return _safe_div(hl21, hl252.clip(lower=_EPS))


def idc_110_vol_decay_divergence_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Difference: 63-day variance half-life minus 252-day variance half-life (regime shift)."""
    hl63 = idc_097_garch_halflife_variance_63d(close)
    hl252 = idc_098_garch_halflife_variance_126d(close)
    return hl63 - hl252


# --- Group H (111-125): Volume-weighted and range-based decay ---

def idc_111_vol_weighted_ac1_returns_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Volume-weighted autocorrelation at lag=1 for returns over 63-day window.
    Weights each return-pair product by normalized volume.
    """
    def _vwac(x, v):
        valid = np.isfinite(x) & np.isfinite(v)
        x, v = x[valid], v[valid]
        if len(x) < 5:
            return np.nan
        vn = v / (v.sum() + _EPS)
        x_mean = (x * vn).sum()
        y = x - x_mean
        if len(y) < 2:
            return np.nan
        num = (vn[1:] * y[:-1] * y[1:]).sum()
        denom = (vn * y ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(num / denom)
    r = _returns(close).values
    v = volume.values.astype(float)
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _vwac(r[max(0, i - w + 1):i + 1], v[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_112_vol_weighted_ac1_returns_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted autocorrelation at lag=1 over 126-day window."""
    def _vwac(x, v):
        valid = np.isfinite(x) & np.isfinite(v)
        x, v = x[valid], v[valid]
        if len(x) < 5:
            return np.nan
        vn = v / (v.sum() + _EPS)
        x_mean = (x * vn).sum()
        y = x - x_mean
        if len(y) < 2:
            return np.nan
        num = (vn[1:] * y[:-1] * y[1:]).sum()
        denom = (vn * y ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(num / denom)
    r = _returns(close).values
    v = volume.values.astype(float)
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _vwac(r[max(0, i - w + 1):i + 1], v[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_113_vol_weighted_halflife_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Half-life derived from volume-weighted AC(1) of returns over 63-day window."""
    ac1 = idc_111_vol_weighted_ac1_returns_63d(close, volume)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


def idc_114_range_persistence_ac1_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC(1) of daily (high-low)/close range series over 63-day window (range persistence)."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_autocorr(rng, _TD_QTR, 1)


def idc_115_range_persistence_ac1_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC(1) of daily range series over 126-day window."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_autocorr(rng, _TD_HALF, 1)


def idc_116_range_halflife_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Half-life of range from AC(1)/AC(2) of normalized daily range over 63-day window."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    ac1 = _rolling_autocorr(rng, _TD_QTR, 1)
    ac2 = _rolling_autocorr(rng, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_117_range_shock_decay_5d_to_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of mean 5-day range to 21-day range (range shock absorption rate)."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    m5 = _rolling_mean(rng, _TD_WEEK)
    m21 = _rolling_mean(rng, _TD_MON)
    return _safe_div(m5, m21.clip(lower=_EPS))


def idc_118_range_shock_decay_21d_to_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of mean 21-day range to 63-day range."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    m21 = _rolling_mean(rng, _TD_MON)
    m63 = _rolling_mean(rng, _TD_QTR)
    return _safe_div(m21, m63.clip(lower=_EPS))


def idc_119_intraday_vol_decay_63d(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC(1) of (high-low)/open series over 63-day window (intraday vol persistence)."""
    rng = _safe_div(high - low, open_.clip(lower=_EPS))
    return _rolling_autocorr(rng, _TD_QTR, 1)


def idc_120_close_to_open_ac1_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """AC(1) of close-to-open gap returns over 63-day window (overnight shock decay)."""
    gap = np.log(open_ / close.shift(1))
    return _rolling_autocorr(gap, _TD_QTR, 1)


def idc_121_close_to_open_halflife_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Half-life of overnight gap from AC(1)/AC(2) over 63-day window."""
    gap = np.log(open_ / close.shift(1))
    ac1 = _rolling_autocorr(gap, _TD_QTR, 1)
    ac2 = _rolling_autocorr(gap, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_122_volume_ac1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """AC(1) of log volume over 63-day window (volume activity persistence)."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_autocorr(lv, _TD_QTR, 1)


def idc_123_volume_halflife_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Half-life of log-volume from AC(1)/AC(2) over 63-day window."""
    lv = np.log(volume.clip(lower=1.0))
    ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    ac2 = _rolling_autocorr(lv, _TD_QTR, 2)
    rate = _decay_rate_from_two_lags(ac1, ac2)
    return _halflife_from_decay(rate)


def idc_124_volume_shock_decay_5d_to_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean volume 5d to mean volume 21d (volume shock absorption)."""
    m5 = _rolling_mean(volume.astype(float), _TD_WEEK)
    m21 = _rolling_mean(volume.astype(float), _TD_MON)
    return _safe_div(m5, m21.clip(lower=_EPS))


def idc_125_vwap_return_ac1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """AC(1) of VWAP-close ratio returns over 63-day window (VWAP signal decay)."""
    vwap = _safe_div(_rolling_sum(close * volume.astype(float), _TD_WEEK),
                     _rolling_sum(volume.astype(float), _TD_WEEK).clip(lower=_EPS))
    vwap_ret = np.log(vwap / vwap.shift(1))
    return _rolling_autocorr(vwap_ret, _TD_QTR, 1)


# --- Group I (126-140): Signal-to-noise decay and entropy ---

def idc_126_signal_noise_ratio_5d_21d(close: pd.Series) -> pd.Series:
    """
    Signal-to-noise: |5-day return| / std of daily returns over 21 days.
    Captures how much directional information survives vs noise.
    """
    r = _returns(close)
    signal = close.pct_change(_TD_WEEK).abs()
    noise = _rolling_std(r, _TD_MON)
    return _safe_div(signal, noise.clip(lower=_EPS))


def idc_127_signal_noise_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Signal-to-noise: |21-day return| / std over 63 days."""
    r = _returns(close)
    signal = close.pct_change(_TD_MON).abs()
    noise = _rolling_std(r, _TD_QTR)
    return _safe_div(signal, noise.clip(lower=_EPS))


def idc_128_return_entropy_63d(close: pd.Series) -> pd.Series:
    """
    Shannon entropy of return sign distribution over 63-day window.
    Max entropy (H=1) = fast decay/unpredictable; low = persistent direction.
    """
    def _ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _ent(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_129_return_entropy_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of return signs over 21-day window."""
    def _ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 4:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_MON
    for i in range(w - 1, n):
        result[i] = _ent(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_130_return_entropy_126d(close: pd.Series) -> pd.Series:
    """Shannon entropy of return signs over 126-day window."""
    def _ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _ent(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_131_approx_entropy_63d(close: pd.Series) -> pd.Series:
    """
    Approximate entropy (ApEn) proxy of log returns over 63-day window.
    Uses m=2, r=0.2*std. Higher ApEn = more random (faster info decay).
    """
    def _apen(x, m=2, r_frac=0.2):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < m + 2:
            return np.nan
        r = r_frac * (x.std() + _EPS)
        def _phi(m_):
            count = 0
            total = 0
            for i in range(n - m_):
                template = x[i:i + m_]
                for j in range(n - m_):
                    if np.max(np.abs(x[j:j + m_] - template)) <= r:
                        count += 1
                total += 1
            if total == 0 or count == 0:
                return np.nan
            return np.log(count / total)
        p1 = _phi(m)
        p2 = _phi(m + 1)
        if p1 is None or p2 is None or np.isnan(p1) or np.isnan(p2):
            return np.nan
        return float(p1 - p2)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        if len(seg) >= 10:
            # limit to last 20 for speed
            result[i] = _apen(seg[-20:])
    return pd.Series(result, index=close.index)


def idc_132_snr_decay_ratio_5d_to_63d(close: pd.Series) -> pd.Series:
    """Ratio of SNR(5d,21d) to SNR(21d,63d): how quickly signal decays across horizons."""
    snr5 = idc_126_signal_noise_ratio_5d_21d(close)
    snr21 = idc_127_signal_noise_ratio_21d_63d(close)
    return _safe_div(snr5, snr21.clip(lower=_EPS))


def idc_133_entropy_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day return entropy in trailing 252-day distribution."""
    ent = idc_128_return_entropy_63d(close)
    return ent.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_134_snr_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d/21d SNR in trailing 252-day distribution."""
    snr = idc_126_signal_noise_ratio_5d_21d(close)
    return snr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_135_ac_decay_entropy_interaction_63d(close: pd.Series) -> pd.Series:
    """Product of AC decay rate and return entropy (both high = chaotic fast-decay regime)."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    ent = idc_128_return_entropy_63d(close)
    return rate * ent


def idc_136_spectral_flatness_proxy_63d(close: pd.Series) -> pd.Series:
    """
    Spectral flatness proxy: geometric mean / arithmetic mean of squared returns
    over 63-day window. Near 1 = white noise (fast decay); near 0 = tonal/persistent.
    """
    def _sf(x):
        x = x[~np.isnan(x)]
        x = x ** 2
        if len(x) < 5 or x.mean() < _EPS:
            return np.nan
        log_mean = np.log(x + _EPS).mean()
        arith = x.mean()
        if arith < _EPS:
            return np.nan
        return float(np.exp(log_mean) / arith)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _sf(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_137_spectral_flatness_proxy_126d(close: pd.Series) -> pd.Series:
    """Spectral flatness proxy over 126-day window."""
    def _sf(x):
        x = x[~np.isnan(x)]
        x = x ** 2
        if len(x) < 5 or x.mean() < _EPS:
            return np.nan
        log_mean = np.log(x + _EPS).mean()
        arith = x.mean()
        if arith < _EPS:
            return np.nan
        return float(np.exp(log_mean) / arith)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _sf(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_138_lz_complexity_proxy_63d(close: pd.Series) -> pd.Series:
    """
    Lempel-Ziv complexity proxy of binary return sequence (1=up, 0=down) over 63-day window.
    Higher = more complex / faster information decay.
    """
    def _lz(seq):
        if len(seq) < 4:
            return np.nan
        n = len(seq)
        s = ''.join('1' if v >= 0 else '0' for v in seq)
        i, k, l = 0, 1, 1
        c = 1
        k_max = 1
        while True:
            if s[i + k - 1] == s[l + k - 1]:
                k += 1
                if l + k > n:
                    c += 1
                    break
            else:
                if k > k_max:
                    k_max = k
                i += 1
                if i == l:
                    c += 1
                    l += k_max
                    if l + 1 > n:
                        break
                    i = 0
                    k = 1
                    k_max = 1
                else:
                    k = 1
        b = n / np.log2(n + 1 + _EPS)
        return float(c / b)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) >= 4:
            result[i] = _lz(seg)
    return pd.Series(result, index=close.index)


def idc_139_lz_complexity_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day LZ complexity in trailing 252-day distribution."""
    lz = idc_138_lz_complexity_proxy_63d(close)
    return lz.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_140_info_decay_composite_63d(close: pd.Series) -> pd.Series:
    """
    Composite information decay score (normalized average of decay rate,
    Hurst deviation from 0.5, and entropy) over 63-day horizon.
    Higher = faster information decay.
    """
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    rate_n = _safe_div(rate - _rolling_mean(rate, _TD_YEAR),
                       _rolling_std(rate, _TD_YEAR).clip(lower=_EPS))
    ent = idc_128_return_entropy_63d(close)
    ent_n = _safe_div(ent - _rolling_mean(ent, _TD_YEAR),
                      _rolling_std(ent, _TD_YEAR).clip(lower=_EPS))
    return (rate_n.fillna(0.0) + ent_n.fillna(0.0)) / 2.0


# --- Group J (141-150): Cross-series decay and additional regime features ---

def idc_141_close_vol_decay_interaction(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Interaction: product of price AC decay rate and volume AC decay rate (63-day).
    Both high = simultaneous information collapse in price and volume.
    """
    r = _returns(close)
    ac1_r = _rolling_autocorr(r, _TD_QTR, 1)
    ac2_r = _rolling_autocorr(r, _TD_QTR, 2)
    price_decay = _decay_rate_from_two_lags(ac1_r, ac2_r)
    lv = np.log(volume.clip(lower=1.0))
    ac1_v = _rolling_autocorr(lv, _TD_QTR, 1)
    ac2_v = _rolling_autocorr(lv, _TD_QTR, 2)
    vol_decay = _decay_rate_from_two_lags(ac1_v, ac2_v)
    return price_decay * vol_decay


def idc_142_hurst_deviation_from_random(close: pd.Series) -> pd.Series:
    """
    Hurst exponent deviation from 0.5 (random walk): H - 0.5.
    Negative = anti-persistent (faster decay); positive = persistent (slower decay).
    """
    def _hurst(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 10:
            return np.nan
        lags = []
        rs_vals = []
        for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
            if w > n:
                continue
            seg = x[:w]
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r_val = dev.max() - dev.min()
            s_val = seg.std()
            if s_val < _EPS:
                continue
            lags.append(np.log(w))
            rs_vals.append(np.log(r_val / s_val))
        if len(lags) < 2:
            return np.nan
        lags, rs_vals = np.array(lags), np.array(rs_vals)
        if lags.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags, rs_vals, 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        h = _hurst(r[max(0, i - w + 1):i + 1])
        result[i] = np.nan if h is None or np.isnan(h) else h - 0.5
    return pd.Series(result, index=close.index)


def idc_143_decay_regime_flag_fast(close: pd.Series) -> pd.Series:
    """Binary: decay rate > 75th percentile of 252-day distribution (fast decay regime)."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    q75 = rate.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    return (rate > q75).astype(float)


def idc_144_decay_regime_flag_slow(close: pd.Series) -> pd.Series:
    """Binary: decay rate < 25th percentile of 252-day distribution (slow decay regime)."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    q25 = rate.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return (rate < q25).astype(float)


def idc_145_halflife_vs_21d_ma(close: pd.Series) -> pd.Series:
    """63-day half-life minus its 21-day moving average (deviation from recent norm)."""
    hl = idc_006_halflife_ac_decay_63d(close)
    return hl - _rolling_mean(hl, _TD_MON)


def idc_146_halflife_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day half-life vs its 252-day distribution."""
    hl = idc_006_halflife_ac_decay_63d(close)
    m = _rolling_mean(hl, _TD_YEAR)
    s = _rolling_std(hl, _TD_YEAR)
    return _safe_div(hl - m, s)


def idc_147_ac_decay_rate_vs_hurst_interaction(close: pd.Series) -> pd.Series:
    """Product of AC decay rate (63d) and Hurst deviation from 0.5 (63d)."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    hdev = idc_142_hurst_deviation_from_random(close)
    return rate * (-hdev)


def idc_148_vol_and_price_decay_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference in half-life: price half-life minus volume half-life (63-day)."""
    r = _returns(close)
    p_ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    p_ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    p_hl = _halflife_from_decay(_decay_rate_from_two_lags(p_ac1, p_ac2))
    lv = np.log(volume.clip(lower=1.0))
    v_ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    v_ac2 = _rolling_autocorr(lv, _TD_QTR, 2)
    v_hl = _halflife_from_decay(_decay_rate_from_two_lags(v_ac1, v_ac2))
    return p_hl - v_hl


def idc_149_ac_decay_accel_21d(close: pd.Series) -> pd.Series:
    """21-day rate of change of the 63-day AC decay rate (acceleration of decay)."""
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    return rate.diff(_TD_MON)


def idc_150_decay_regime_zscore_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Composite z-scored decay regime score:
    z(price decay) + z(vol decay) + z(entropy). Higher = more decayed/random regime.
    """
    rate = idc_001_ac_decay_lag1_lag2_63d(close)
    rate_z = _safe_div(rate - _rolling_mean(rate, _TD_YEAR),
                       _rolling_std(rate, _TD_YEAR).clip(lower=_EPS))
    lv = np.log(volume.clip(lower=1.0))
    v_ac1 = _rolling_autocorr(lv, _TD_QTR, 1)
    v_ac2 = _rolling_autocorr(lv, _TD_QTR, 2)
    vdecay = _halflife_from_decay(_decay_rate_from_two_lags(v_ac1, v_ac2))
    vdecay_z = _safe_div(vdecay - _rolling_mean(vdecay, _TD_YEAR),
                         _rolling_std(vdecay, _TD_YEAR).clip(lower=_EPS))
    ent = idc_128_return_entropy_63d(close)
    ent_z = _safe_div(ent - _rolling_mean(ent, _TD_YEAR),
                      _rolling_std(ent, _TD_YEAR).clip(lower=_EPS))
    return rate_z.fillna(0.0) + vdecay_z.fillna(0.0) + ent_z.fillna(0.0)


# keep idc_001 and idc_006 and idc_128 available for cross-file calls at module level
def idc_001_ac_decay_lag1_lag2_63d(close: pd.Series) -> pd.Series:  # noqa: F811
    """Decay rate from AC(1)/AC(2) of returns, 63-day window (local copy)."""
    def _ac(x):
        x = x[~np.isnan(x)]
        if len(x) < 4:
            return np.nan
        x0, x1 = x[:-1], x[1:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    def _ac2(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        x0, x1 = x[:-2], x[2:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_006_halflife_ac_decay_63d(close: pd.Series) -> pd.Series:  # noqa: F811
    """Half-life from AC(1)/AC(2) decay rate, 63-day window (local copy)."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    return _halflife_from_decay(_decay_rate_from_two_lags(ac1, ac2))


def idc_128_return_entropy_63d(close: pd.Series) -> pd.Series:  # noqa: F811
    """Shannon entropy of return sign distribution, 63-day window (local copy)."""
    def _ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _ent(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


# ── Registry ──────────────────────────────────────────────────────────────────

INFORMATION_DECAY_REGISTRY_076_150 = {
    "idc_076_mi_lag1_returns_63d": {"inputs": ["close"], "func": idc_076_mi_lag1_returns_63d},
    "idc_077_mi_lag3_returns_63d": {"inputs": ["close"], "func": idc_077_mi_lag3_returns_63d},
    "idc_078_mi_lag5_returns_63d": {"inputs": ["close"], "func": idc_078_mi_lag5_returns_63d},
    "idc_079_mi_lag10_returns_126d": {"inputs": ["close"], "func": idc_079_mi_lag10_returns_126d},
    "idc_080_mi_decay_lag1_to_lag3_63d": {"inputs": ["close"], "func": idc_080_mi_decay_lag1_to_lag3_63d},
    "idc_081_mi_decay_lag1_to_lag5_63d": {"inputs": ["close"], "func": idc_081_mi_decay_lag1_to_lag5_63d},
    "idc_082_mi_decay_ratio_lag3_to_lag1_63d": {"inputs": ["close"], "func": idc_082_mi_decay_ratio_lag3_to_lag1_63d},
    "idc_083_mi_lag1_abs_returns_63d": {"inputs": ["close"], "func": idc_083_mi_lag1_abs_returns_63d},
    "idc_084_mi_lag5_abs_returns_126d": {"inputs": ["close"], "func": idc_084_mi_lag5_abs_returns_126d},
    "idc_085_mi_vol_decay_ratio_lag5_to_lag1_126d": {"inputs": ["close"], "func": idc_085_mi_vol_decay_ratio_lag5_to_lag1_126d},
    "idc_086_mi_pct_rank_lag1_252d": {"inputs": ["close"], "func": idc_086_mi_pct_rank_lag1_252d},
    "idc_087_mi_decay_zscore_lag1_to_lag5_63d": {"inputs": ["close"], "func": idc_087_mi_decay_zscore_lag1_to_lag5_63d},
    "idc_088_mi_lag1_sq_returns_63d": {"inputs": ["close"], "func": idc_088_mi_lag1_sq_returns_63d},
    "idc_089_mi_lag3_sq_returns_126d": {"inputs": ["close"], "func": idc_089_mi_lag3_sq_returns_126d},
    "idc_090_mi_vol_halflife_63d": {"inputs": ["close"], "func": idc_090_mi_vol_halflife_63d},
    "idc_091_garch_alpha_proxy_63d": {"inputs": ["close"], "func": idc_091_garch_alpha_proxy_63d},
    "idc_092_garch_alpha_proxy_126d": {"inputs": ["close"], "func": idc_092_garch_alpha_proxy_126d},
    "idc_093_garch_alpha_proxy_252d": {"inputs": ["close"], "func": idc_093_garch_alpha_proxy_252d},
    "idc_094_variance_persistence_lag2_63d": {"inputs": ["close"], "func": idc_094_variance_persistence_lag2_63d},
    "idc_095_variance_persistence_lag5_126d": {"inputs": ["close"], "func": idc_095_variance_persistence_lag5_126d},
    "idc_096_garch_beta_proxy_63d": {"inputs": ["close"], "func": idc_096_garch_beta_proxy_63d},
    "idc_097_garch_halflife_variance_63d": {"inputs": ["close"], "func": idc_097_garch_halflife_variance_63d},
    "idc_098_garch_halflife_variance_126d": {"inputs": ["close"], "func": idc_098_garch_halflife_variance_126d},
    "idc_099_vol_shock_decay_5d_ewm21": {"inputs": ["close"], "func": idc_099_vol_shock_decay_5d_ewm21},
    "idc_100_vol_shock_decay_21d_ewm63": {"inputs": ["close"], "func": idc_100_vol_shock_decay_21d_ewm63},
    "idc_101_vol_shock_decay_63d_ewm252": {"inputs": ["close"], "func": idc_101_vol_shock_decay_63d_ewm252},
    "idc_102_vol_halflife_ewm_fit_21d": {"inputs": ["close"], "func": idc_102_vol_halflife_ewm_fit_21d},
    "idc_103_vol_halflife_ewm_fit_63d": {"inputs": ["close"], "func": idc_103_vol_halflife_ewm_fit_63d},
    "idc_104_vol_halflife_ewm_fit_252d": {"inputs": ["close"], "func": idc_104_vol_halflife_ewm_fit_252d},
    "idc_105_garch_alpha_pct_rank_252d": {"inputs": ["close"], "func": idc_105_garch_alpha_pct_rank_252d},
    "idc_106_variance_halflife_pct_rank_252d": {"inputs": ["close"], "func": idc_106_variance_halflife_pct_rank_252d},
    "idc_107_vol_shock_decay_zscore_252d": {"inputs": ["close"], "func": idc_107_vol_shock_decay_zscore_252d},
    "idc_108_vol_decay_slope_lags_1_to_5_63d": {"inputs": ["close"], "func": idc_108_vol_decay_slope_lags_1_to_5_63d},
    "idc_109_ewm_vol_halflife_ratio_short_to_long": {"inputs": ["close"], "func": idc_109_ewm_vol_halflife_ratio_short_to_long},
    "idc_110_vol_decay_divergence_63d_vs_252d": {"inputs": ["close"], "func": idc_110_vol_decay_divergence_63d_vs_252d},
    "idc_111_vol_weighted_ac1_returns_63d": {"inputs": ["close", "volume"], "func": idc_111_vol_weighted_ac1_returns_63d},
    "idc_112_vol_weighted_ac1_returns_126d": {"inputs": ["close", "volume"], "func": idc_112_vol_weighted_ac1_returns_126d},
    "idc_113_vol_weighted_halflife_63d": {"inputs": ["close", "volume"], "func": idc_113_vol_weighted_halflife_63d},
    "idc_114_range_persistence_ac1_63d": {"inputs": ["close", "high", "low"], "func": idc_114_range_persistence_ac1_63d},
    "idc_115_range_persistence_ac1_126d": {"inputs": ["close", "high", "low"], "func": idc_115_range_persistence_ac1_126d},
    "idc_116_range_halflife_63d": {"inputs": ["close", "high", "low"], "func": idc_116_range_halflife_63d},
    "idc_117_range_shock_decay_5d_to_21d": {"inputs": ["close", "high", "low"], "func": idc_117_range_shock_decay_5d_to_21d},
    "idc_118_range_shock_decay_21d_to_63d": {"inputs": ["close", "high", "low"], "func": idc_118_range_shock_decay_21d_to_63d},
    "idc_119_intraday_vol_decay_63d": {"inputs": ["close", "open", "high", "low"], "func": idc_119_intraday_vol_decay_63d},
    "idc_120_close_to_open_ac1_63d": {"inputs": ["close", "open"], "func": idc_120_close_to_open_ac1_63d},
    "idc_121_close_to_open_halflife_63d": {"inputs": ["close", "open"], "func": idc_121_close_to_open_halflife_63d},
    "idc_122_volume_ac1_63d": {"inputs": ["close", "volume"], "func": idc_122_volume_ac1_63d},
    "idc_123_volume_halflife_63d": {"inputs": ["close", "volume"], "func": idc_123_volume_halflife_63d},
    "idc_124_volume_shock_decay_5d_to_21d": {"inputs": ["close", "volume"], "func": idc_124_volume_shock_decay_5d_to_21d},
    "idc_125_vwap_return_ac1_63d": {"inputs": ["close", "volume"], "func": idc_125_vwap_return_ac1_63d},
    "idc_126_signal_noise_ratio_5d_21d": {"inputs": ["close"], "func": idc_126_signal_noise_ratio_5d_21d},
    "idc_127_signal_noise_ratio_21d_63d": {"inputs": ["close"], "func": idc_127_signal_noise_ratio_21d_63d},
    "idc_128_return_entropy_63d": {"inputs": ["close"], "func": idc_128_return_entropy_63d},
    "idc_129_return_entropy_21d": {"inputs": ["close"], "func": idc_129_return_entropy_21d},
    "idc_130_return_entropy_126d": {"inputs": ["close"], "func": idc_130_return_entropy_126d},
    "idc_131_approx_entropy_63d": {"inputs": ["close"], "func": idc_131_approx_entropy_63d},
    "idc_132_snr_decay_ratio_5d_to_63d": {"inputs": ["close"], "func": idc_132_snr_decay_ratio_5d_to_63d},
    "idc_133_entropy_pct_rank_252d": {"inputs": ["close"], "func": idc_133_entropy_pct_rank_252d},
    "idc_134_snr_pct_rank_252d": {"inputs": ["close"], "func": idc_134_snr_pct_rank_252d},
    "idc_135_ac_decay_entropy_interaction_63d": {"inputs": ["close"], "func": idc_135_ac_decay_entropy_interaction_63d},
    "idc_136_spectral_flatness_proxy_63d": {"inputs": ["close"], "func": idc_136_spectral_flatness_proxy_63d},
    "idc_137_spectral_flatness_proxy_126d": {"inputs": ["close"], "func": idc_137_spectral_flatness_proxy_126d},
    "idc_138_lz_complexity_proxy_63d": {"inputs": ["close"], "func": idc_138_lz_complexity_proxy_63d},
    "idc_139_lz_complexity_pct_rank_252d": {"inputs": ["close"], "func": idc_139_lz_complexity_pct_rank_252d},
    "idc_140_info_decay_composite_63d": {"inputs": ["close"], "func": idc_140_info_decay_composite_63d},
    "idc_141_close_vol_decay_interaction": {"inputs": ["close", "volume"], "func": idc_141_close_vol_decay_interaction},
    "idc_142_hurst_deviation_from_random": {"inputs": ["close"], "func": idc_142_hurst_deviation_from_random},
    "idc_143_decay_regime_flag_fast": {"inputs": ["close"], "func": idc_143_decay_regime_flag_fast},
    "idc_144_decay_regime_flag_slow": {"inputs": ["close"], "func": idc_144_decay_regime_flag_slow},
    "idc_145_halflife_vs_21d_ma": {"inputs": ["close"], "func": idc_145_halflife_vs_21d_ma},
    "idc_146_halflife_zscore_252d": {"inputs": ["close"], "func": idc_146_halflife_zscore_252d},
    "idc_147_ac_decay_rate_vs_hurst_interaction": {"inputs": ["close"], "func": idc_147_ac_decay_rate_vs_hurst_interaction},
    "idc_148_vol_and_price_decay_divergence": {"inputs": ["close", "volume"], "func": idc_148_vol_and_price_decay_divergence},
    "idc_149_ac_decay_accel_21d": {"inputs": ["close"], "func": idc_149_ac_decay_accel_21d},
    "idc_150_decay_regime_zscore_composite": {"inputs": ["close", "volume"], "func": idc_150_decay_regime_zscore_composite},
}
