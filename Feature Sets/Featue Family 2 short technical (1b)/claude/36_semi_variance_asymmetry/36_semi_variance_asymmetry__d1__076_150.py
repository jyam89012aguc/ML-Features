"""semi_variance_asymmetry d1 features 076-150 — Pipeline 1b-technical.

Continuation of family 36 — 75 more distinct asymmetry hypotheses, all
answering "are the up moves different from the down moves?" Buckets here:
single-day extremes, sign-streak asymmetry, tail asymmetry (VaR/ES),
quantile asymmetry, time-in-regime asymmetry, drawdown-vs-runup asymmetry,
volume-conditioned asymmetry, sign-aware autocorrelation, extreme-day
clip-rate asymmetry, coefficient-of-variation asymmetry, bar-shape
(upper-wick vs lower-wick) asymmetry, multi-bucket composite indices.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit
min_periods. Self-contained helpers — no cross-family imports.
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


def _log_returns(close: pd.Series) -> pd.Series:
    return _safe_log(close).diff()


def _neg_part(r: pd.Series) -> pd.Series:
    return r.where(r < 0, 0.0)


def _pos_part(r: pd.Series) -> pd.Series:
    return r.where(r > 0, 0.0)


def _when_neg(r: pd.Series) -> pd.Series:
    return r.where(r < 0)


def _when_pos(r: pd.Series) -> pd.Series:
    return r.where(r > 0)


# ============================================================
# Bucket L — Single-day extreme asymmetry (076-081)
# Max gain vs max loss over rolling window.
# ============================================================

def f36_svas_076_max_single_day_gain_21d(close: pd.Series) -> pd.Series:
    """Largest single-day positive log return in trailing 21d — short-horizon max gain."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).max()


def f36_svas_077_max_single_day_loss_21d(close: pd.Series) -> pd.Series:
    """Largest single-day loss in trailing 21d (positive magnitude) — short-horizon max loss."""
    r = _log_returns(close)
    return (-r).rolling(MDAYS, min_periods=WDAYS).max()


def f36_svas_078_max_gain_minus_max_loss_252d(close: pd.Series) -> pd.Series:
    """max(r)_252d - max(-r)_252d — additive extreme asymmetry over annual horizon."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).max() - (-r).rolling(YDAYS, min_periods=QDAYS).max()


def f36_svas_079_max_gain_over_max_loss_252d(close: pd.Series) -> pd.Series:
    """max(r) / max(-r) over 252d — ratio of best single day to worst single day."""
    r = _log_returns(close)
    return _safe_div(r.rolling(YDAYS, min_periods=QDAYS).max(),
                     (-r).rolling(YDAYS, min_periods=QDAYS).max())


def f36_svas_080_max_gain_minus_max_loss_504d(close: pd.Series) -> pd.Series:
    """max(r)_504d - max(-r)_504d — additive extreme asymmetry over biennial horizon."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).max() - (-r).rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f36_svas_081_normalized_extreme_asymmetry_252d(close: pd.Series) -> pd.Series:
    """(max_gain - max_loss) / (max_gain + max_loss) at 252d — bounded extreme asymmetry index in [-1,1]."""
    r = _log_returns(close)
    g = r.rolling(YDAYS, min_periods=QDAYS).max()
    l = (-r).rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(g - l, g + l)


# ============================================================
# Bucket M — Up-streak vs down-streak asymmetry (082-089)
# Run-length statistics conditioned on sign.
# ============================================================

def _longest_run_window(w: np.ndarray, sign: int) -> float:
    """Longest consecutive run of (sign>0)/(sign<0) markers within a rolling window."""
    if w.size == 0 or np.isnan(w).all():
        return np.nan
    best = 0
    cur = 0
    for v in w:
        if np.isnan(v):
            cur = 0
            continue
        if (sign > 0 and v > 0) or (sign < 0 and v < 0):
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return float(best)


def _mean_run_length_window(w: np.ndarray, sign: int) -> float:
    """Mean length of consecutive runs matching sign within a rolling window."""
    if w.size == 0 or np.isnan(w).all():
        return np.nan
    runs = []
    cur = 0
    for v in w:
        if np.isnan(v):
            if cur > 0:
                runs.append(cur); cur = 0
            continue
        match = (sign > 0 and v > 0) or (sign < 0 and v < 0)
        if match:
            cur += 1
        else:
            if cur > 0:
                runs.append(cur); cur = 0
    if cur > 0:
        runs.append(cur)
    return float(np.mean(runs)) if runs else np.nan


def f36_svas_082_longest_up_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive up-day streak in trailing 252d."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, +1), raw=True)


def f36_svas_083_longest_down_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive down-day streak in trailing 252d."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, -1), raw=True)


def f36_svas_084_streak_length_asymmetry_252d(close: pd.Series) -> pd.Series:
    """longest up streak - longest down streak over 252d — additive streak asymmetry."""
    r = _log_returns(close)
    up = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, +1), raw=True)
    dn = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, -1), raw=True)
    return up - dn


def f36_svas_085_streak_length_ratio_up_over_down_252d(close: pd.Series) -> pd.Series:
    """longest up streak / longest down streak over 252d — ratio form."""
    r = _log_returns(close)
    up = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, +1), raw=True)
    dn = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _longest_run_window(w, -1), raw=True)
    return _safe_div(up, dn)


def f36_svas_086_mean_up_run_length_252d(close: pd.Series) -> pd.Series:
    """Average length of up-day runs in trailing 252d — typical winning streak."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _mean_run_length_window(w, +1), raw=True)


def f36_svas_087_mean_down_run_length_252d(close: pd.Series) -> pd.Series:
    """Average length of down-day runs in trailing 252d — typical losing streak."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _mean_run_length_window(w, -1), raw=True)


def f36_svas_088_mean_run_length_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Mean up-run length - mean down-run length over 252d — typical-streak asymmetry."""
    r = _log_returns(close)
    u = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _mean_run_length_window(w, +1), raw=True)
    d = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _mean_run_length_window(w, -1), raw=True)
    return u - d


def f36_svas_089_current_signed_streak_length(close: pd.Series) -> pd.Series:
    """Current consecutive same-sign return streak: positive if up streak, negative if down streak."""
    r = _log_returns(close).values
    n = r.size
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    sign = 0
    for i in range(n):
        v = r[i]
        if np.isnan(v):
            streak = 0; sign = 0
            out[i] = np.nan; continue
        s = 1 if v > 0 else (-1 if v < 0 else 0)
        if s == 0:
            streak = 0; sign = 0
            out[i] = 0.0; continue
        if s == sign:
            streak += 1
        else:
            streak = 1; sign = s
        out[i] = float(sign * streak)
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket N — Tail asymmetry (VaR / ES style) (090-097)
# Compares left-tail to right-tail magnitudes.
# ============================================================

def f36_svas_090_var_5pct_lower_tail_252d(close: pd.Series) -> pd.Series:
    """5th percentile of returns over 252d (a negative VaR-style quantile)."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)


def f36_svas_091_var_95pct_upper_tail_252d(close: pd.Series) -> pd.Series:
    """95th percentile of returns over 252d — upper-tail counterpart to VaR."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f36_svas_092_tail_magnitude_asymmetry_5_95_252d(close: pd.Series) -> pd.Series:
    """|q05| - q95 over 252d — additive tail-magnitude asymmetry (positive = left tail dominates)."""
    r = _log_returns(close)
    ql = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    qh = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return ql.abs() - qh


def f36_svas_093_tail_magnitude_ratio_lower_over_upper_252d(close: pd.Series) -> pd.Series:
    """|q05| / q95 over 252d — left-tail magnitude as a multiple of right-tail magnitude."""
    r = _log_returns(close)
    ql = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    qh = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return _safe_div(ql.abs(), qh)


def _es_lower_window(w: np.ndarray, p: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 10:
        return np.nan
    thr = np.quantile(v, p)
    tail = v[v <= thr]
    return float(tail.mean()) if tail.size else np.nan


def _es_upper_window(w: np.ndarray, p: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 10:
        return np.nan
    thr = np.quantile(v, p)
    tail = v[v >= thr]
    return float(tail.mean()) if tail.size else np.nan


def f36_svas_094_expected_shortfall_lower_5pct_252d(close: pd.Series) -> pd.Series:
    """Lower-tail expected shortfall (mean of returns <= q05) over 252d."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_lower_window(w, 0.05), raw=True)


def f36_svas_095_expected_shortfall_upper_95pct_252d(close: pd.Series) -> pd.Series:
    """Upper-tail expected gain (mean of returns >= q95) over 252d."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_upper_window(w, 0.95), raw=True)


def f36_svas_096_es_magnitude_asymmetry_252d(close: pd.Series) -> pd.Series:
    """|lower-ES| - upper-ES over 252d — additive tail-expectation asymmetry."""
    r = _log_returns(close)
    el = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_lower_window(w, 0.05), raw=True)
    eu = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_upper_window(w, 0.95), raw=True)
    return el.abs() - eu


def f36_svas_097_es_ratio_lower_over_upper_252d(close: pd.Series) -> pd.Series:
    """|lower-ES| / upper-ES over 252d — ratio form of tail-expectation asymmetry."""
    r = _log_returns(close)
    el = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_lower_window(w, 0.05), raw=True)
    eu = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _es_upper_window(w, 0.95), raw=True)
    return _safe_div(el.abs(), eu)


# ============================================================
# Bucket O — Quantile-distance asymmetry (098-103)
# Distance from median to upper quantile vs median to lower quantile.
# ============================================================

def f36_svas_098_quantile_asymmetry_25_75_252d(close: pd.Series) -> pd.Series:
    """(q75 - q50) - (q50 - q25) at 252d — IQR-balance asymmetry."""
    r = _log_returns(close)
    q25 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q75 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (q75 - q50) - (q50 - q25)


def f36_svas_099_quantile_asymmetry_10_90_252d(close: pd.Series) -> pd.Series:
    """(q90 - q50) - (q50 - q10) at 252d — wider-quantile balance asymmetry."""
    r = _log_returns(close)
    q10 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q90 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (q90 - q50) - (q50 - q10)


def f36_svas_100_iqr_balance_ratio_252d(close: pd.Series) -> pd.Series:
    """(q75 - q50) / (q50 - q25) at 252d — ratio form of IQR-half balance."""
    r = _log_returns(close)
    q25 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q75 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return _safe_div(q75 - q50, q50 - q25)


def f36_svas_101_outer_decile_balance_ratio_252d(close: pd.Series) -> pd.Series:
    """(q90 - q50) / (q50 - q10) at 252d — ratio form of decile-half balance."""
    r = _log_returns(close)
    q10 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q90 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return _safe_div(q90 - q50, q50 - q10)


def f36_svas_102_extreme_decile_balance_ratio_252d(close: pd.Series) -> pd.Series:
    """(q95 - q50) / (q50 - q05) at 252d — extreme-tail half-balance ratio."""
    r = _log_returns(close)
    q05 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return _safe_div(q95 - q50, q50 - q05)


def f36_svas_103_median_position_in_range_252d(close: pd.Series) -> pd.Series:
    """(q50 - q_min) / (q_max - q_min) over 252d — median position within full return range; 0.5 = symmetric."""
    r = _log_returns(close)
    qm = r.rolling(YDAYS, min_periods=QDAYS).min()
    qx = r.rolling(YDAYS, min_periods=QDAYS).max()
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    return _safe_div(q50 - qm, qx - qm)


# ============================================================
# Bucket P — Time-in-regime asymmetry (104-108)
# Fraction of bars spent in different signed states.
# ============================================================

def f36_svas_104_fraction_time_below_zero_cum_return_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where cumulative-log-return (since start of window) is below 0."""
    r = _log_returns(close)
    # Within-window cum return measured from window start: use a rolling apply
    def _frac_below(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v)
        return float((c < 0).sum() / v.size)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_frac_below, raw=True)


def f36_svas_105_fraction_time_above_zero_cum_return_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where window-cumulative return is above 0."""
    r = _log_returns(close)
    def _frac_above(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v)
        return float((c > 0).sum() / v.size)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_frac_above, raw=True)


def f36_svas_106_time_in_regime_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Fraction above 0 - fraction below 0 (window-cum) at 252d — additive time-in-regime asymmetry."""
    r = _log_returns(close)
    def _delta(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v)
        return float(((c > 0).sum() - (c < 0).sum()) / v.size)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_delta, raw=True)


def f36_svas_107_fraction_above_below_zero_ratio_252d(close: pd.Series) -> pd.Series:
    """Fraction above 0 / fraction below 0 (window-cum) at 252d — ratio form."""
    r = _log_returns(close)
    def _ratio(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v)
        a = (c > 0).sum(); b = (c < 0).sum()
        return float(a / b) if b > 0 else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ratio, raw=True)


def f36_svas_108_fraction_consec_negative_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d that lies within a >=3-day consecutive-down streak — clustered-loss time share."""
    r = _log_returns(close).values
    n = r.size
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        lo = max(0, i - win + 1)
        w = r[lo:i + 1]
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            continue
        in_neg = np.zeros(v.size, dtype=bool)
        cur = 0
        for k, x in enumerate(v):
            if x < 0:
                cur += 1
                if cur >= 3:
                    in_neg[k - cur + 1:k + 1] = True
            else:
                cur = 0
        out[i] = float(in_neg.sum() / v.size)
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket Q — Drawdown vs run-up asymmetry (109-116)
# Worst peak-to-trough vs best trough-to-peak excursions.
# ============================================================

def _max_drawdown_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 5:
        return np.nan
    c = np.cumsum(v)
    peak = np.maximum.accumulate(c)
    dd = c - peak
    return float(dd.min())


def _max_runup_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 5:
        return np.nan
    c = np.cumsum(v)
    trough = np.minimum.accumulate(c)
    ru = c - trough
    return float(ru.max())


def f36_svas_109_max_drawdown_log_252d(close: pd.Series) -> pd.Series:
    """Max drawdown (in log-return units) over trailing 252d — peak-to-trough excursion."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_max_drawdown_window, raw=True)


def f36_svas_110_max_runup_log_252d(close: pd.Series) -> pd.Series:
    """Max run-up (in log-return units) over trailing 252d — trough-to-peak excursion."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_max_runup_window, raw=True)


def f36_svas_111_drawdown_runup_asymmetry_252d(close: pd.Series) -> pd.Series:
    """|max drawdown| - max runup over 252d — additive excursion asymmetry."""
    r = _log_returns(close)
    dd = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_drawdown_window, raw=True)
    ru = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_runup_window, raw=True)
    return dd.abs() - ru


def f36_svas_112_drawdown_runup_ratio_252d(close: pd.Series) -> pd.Series:
    """|max drawdown| / max runup over 252d — ratio form of excursion asymmetry."""
    r = _log_returns(close)
    dd = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_drawdown_window, raw=True)
    ru = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_runup_window, raw=True)
    return _safe_div(dd.abs(), ru)


def f36_svas_113_max_drawdown_log_504d(close: pd.Series) -> pd.Series:
    """Max drawdown (log-units) over trailing 504d — biennial peak-to-trough."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_max_drawdown_window, raw=True)


def f36_svas_114_max_runup_log_504d(close: pd.Series) -> pd.Series:
    """Max run-up (log-units) over trailing 504d — biennial trough-to-peak."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_max_runup_window, raw=True)


def f36_svas_115_drawdown_runup_asymmetry_504d(close: pd.Series) -> pd.Series:
    """|max drawdown|_504 - max runup_504 — biennial excursion asymmetry."""
    r = _log_returns(close)
    dd = r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_max_drawdown_window, raw=True)
    ru = r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_max_runup_window, raw=True)
    return dd.abs() - ru


def f36_svas_116_normalized_excursion_asymmetry_252d(close: pd.Series) -> pd.Series:
    """(|dd| - ru) / (|dd| + ru) over 252d — bounded excursion asymmetry index in [-1,1]."""
    r = _log_returns(close)
    dd = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_drawdown_window, raw=True)
    ru = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_runup_window, raw=True)
    return _safe_div(dd.abs() - ru, dd.abs() + ru)


# ============================================================
# Bucket R — Volume-conditioned sign asymmetry (117-124)
# How does volume scale with up days vs down days?
# ============================================================

def f36_svas_117_volume_on_up_days_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up days over 252d — typical up-day participation."""
    r = _log_returns(close)
    vu = volume.where(r > 0)
    return vu.rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_118_volume_on_down_days_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down days over 252d — typical down-day participation."""
    r = _log_returns(close)
    vd = volume.where(r < 0)
    return vd.rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_119_volume_asymmetry_ratio_up_over_down_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean up-day volume / mean down-day volume over 252d — accumulation/distribution flavor."""
    r = _log_returns(close)
    vu = volume.where(r > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    vd = volume.where(r < 0).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(vu, vd)


def f36_svas_120_log_volume_asymmetry_up_down_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(up-day vol / down-day vol) at 252d — symmetric scale of volume asymmetry."""
    r = _log_returns(close)
    vu = volume.where(r > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    vd = volume.where(r < 0).rolling(YDAYS, min_periods=QDAYS).mean()
    return np.log(_safe_div(vu, vd))


def f36_svas_121_avg_gain_on_high_vol_up_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean return on up days where volume is in top tertile of 252d vol distribution — premium-volume gain."""
    r = _log_returns(close)
    vt = volume.rolling(YDAYS, min_periods=QDAYS).quantile(2.0 / 3.0)
    mask = (r > 0) & (volume >= vt)
    return r.where(mask).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_122_avg_loss_on_high_vol_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean |return| on down days where volume in top tertile of 252d — premium-volume loss magnitude."""
    r = _log_returns(close)
    vt = volume.rolling(YDAYS, min_periods=QDAYS).quantile(2.0 / 3.0)
    mask = (r < 0) & (volume >= vt)
    return (-r).where(mask).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_123_high_vol_gain_minus_loss_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """High-vol up-day gain - high-vol down-day |loss| over 252d — premium-volume asymmetry."""
    r = _log_returns(close)
    vt = volume.rolling(YDAYS, min_periods=QDAYS).quantile(2.0 / 3.0)
    g = r.where((r > 0) & (volume >= vt)).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-r).where((r < 0) & (volume >= vt)).rolling(YDAYS, min_periods=QDAYS).mean()
    return g - l


def f36_svas_124_dollar_volume_asymmetry_up_down_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-volume (close*vol) on up days / mean $-volume on down days over 252d."""
    r = _log_returns(close)
    dv = close * volume
    du = dv.where(r > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    dd = dv.where(r < 0).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(du, dd)


# ============================================================
# Bucket S — Sign-asymmetric autocorrelation (125-130)
# Conditional return autocorrelation: does today's sign predict
# tomorrow's magnitude differently for + vs -?
# ============================================================

def _conditional_corr_window(w: np.ndarray, sign: int) -> float:
    """Pearson corr between r_{t-1} and r_t restricted to r_{t-1} matching sign."""
    v = w[~np.isnan(w)]
    if v.size < 30:
        return np.nan
    a = v[:-1]
    b = v[1:]
    if sign > 0:
        m = a > 0
    else:
        m = a < 0
    if m.sum() < 10:
        return np.nan
    aa = a[m]; bb = b[m]
    if aa.std() == 0 or bb.std() == 0:
        return np.nan
    return float(np.corrcoef(aa, bb)[0, 1])


def f36_svas_125_autocorr_after_up_day_252d(close: pd.Series) -> pd.Series:
    """corr(r_{t-1}, r_t | r_{t-1} > 0) over 252d — momentum/reversal conditional on up days."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _conditional_corr_window(w, +1), raw=True)


def f36_svas_126_autocorr_after_down_day_252d(close: pd.Series) -> pd.Series:
    """corr(r_{t-1}, r_t | r_{t-1} < 0) over 252d — momentum/reversal conditional on down days."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _conditional_corr_window(w, -1), raw=True)


def f36_svas_127_autocorr_asymmetry_up_minus_down_252d(close: pd.Series) -> pd.Series:
    """autocorr-after-up - autocorr-after-down over 252d — sign-asymmetric autocorrelation index."""
    r = _log_returns(close)
    au = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _conditional_corr_window(w, +1), raw=True)
    ad = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _conditional_corr_window(w, -1), raw=True)
    return au - ad


def f36_svas_128_p_up_after_up_252d(close: pd.Series) -> pd.Series:
    """P(r_t > 0 | r_{t-1} > 0) over 252d — conditional probability of up after up."""
    r = _log_returns(close)
    prev = r.shift(1)
    mask = (prev > 0)
    inc = (r > 0).astype(float).where(mask)
    num = inc.rolling(YDAYS, min_periods=QDAYS).sum()
    den = mask.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f36_svas_129_p_down_after_down_252d(close: pd.Series) -> pd.Series:
    """P(r_t < 0 | r_{t-1} < 0) over 252d — conditional probability of down after down."""
    r = _log_returns(close)
    prev = r.shift(1)
    mask = (prev < 0)
    inc = (r < 0).astype(float).where(mask)
    num = inc.rolling(YDAYS, min_periods=QDAYS).sum()
    den = mask.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f36_svas_130_sign_persistence_asymmetry_252d(close: pd.Series) -> pd.Series:
    """P(up|up) - P(down|down) over 252d — persistence asymmetry between sign regimes."""
    r = _log_returns(close)
    prev = r.shift(1)
    mu = (prev > 0); md = (prev < 0)
    pu = _safe_div((r > 0).astype(float).where(mu).rolling(YDAYS, min_periods=QDAYS).sum(),
                   mu.astype(float).rolling(YDAYS, min_periods=QDAYS).sum())
    pd_ = _safe_div((r < 0).astype(float).where(md).rolling(YDAYS, min_periods=QDAYS).sum(),
                    md.astype(float).rolling(YDAYS, min_periods=QDAYS).sum())
    return pu - pd_


# ============================================================
# Bucket T — Extreme-day (clip / pin) asymmetry (131-135)
# Counts of bars exceeding ± threshold (e.g. ±3σ).
# ============================================================

def f36_svas_131_count_extreme_up_3sigma_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where r > 3 * 252d std — extreme-up day count."""
    r = _log_returns(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (r > 3.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_132_count_extreme_down_3sigma_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where r < -3 * 252d std — extreme-down day count."""
    r = _log_returns(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (r < -3.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_133_extreme_day_count_asymmetry_252d(close: pd.Series) -> pd.Series:
    """count(extreme up) - count(extreme down) over 252d at the ±3σ threshold — extreme-day asymmetry."""
    r = _log_returns(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    nu = (r > 3.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    nd = (r < -3.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return nu - nd


def f36_svas_134_count_extreme_up_2sigma_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where r > 2σ — looser extreme-up count."""
    r = _log_returns(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (r > 2.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f36_svas_135_count_extreme_down_2sigma_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where r < -2σ — looser extreme-down count."""
    r = _log_returns(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (r < -2.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket U — Coefficient-of-variation asymmetry (136-140)
# CV = std / |mean| computed separately on up and down subsets.
# ============================================================

def f36_svas_136_cv_up_returns_252d(close: pd.Series) -> pd.Series:
    """std(r|up) / mean(r|up) over 252d — coefficient of variation of up-day returns."""
    r = _log_returns(close)
    ru = _when_pos(r)
    return _safe_div(ru.rolling(YDAYS, min_periods=QDAYS).std(),
                     ru.rolling(YDAYS, min_periods=QDAYS).mean())


def f36_svas_137_cv_down_returns_252d(close: pd.Series) -> pd.Series:
    """std(|r||down) / mean(|r||down) over 252d — coefficient of variation of down-day |returns|."""
    r = _log_returns(close)
    rd = -_when_neg(r)
    return _safe_div(rd.rolling(YDAYS, min_periods=QDAYS).std(),
                     rd.rolling(YDAYS, min_periods=QDAYS).mean())


def f36_svas_138_cv_asymmetry_up_minus_down_252d(close: pd.Series) -> pd.Series:
    """CV(up) - CV(down) over 252d — additive coefficient-of-variation asymmetry."""
    r = _log_returns(close)
    ru = _when_pos(r); rd = -_when_neg(r)
    cu = _safe_div(ru.rolling(YDAYS, min_periods=QDAYS).std(), ru.rolling(YDAYS, min_periods=QDAYS).mean())
    cd = _safe_div(rd.rolling(YDAYS, min_periods=QDAYS).std(), rd.rolling(YDAYS, min_periods=QDAYS).mean())
    return cu - cd


def f36_svas_139_cv_ratio_up_over_down_252d(close: pd.Series) -> pd.Series:
    """CV(up) / CV(down) over 252d — ratio form of CV asymmetry."""
    r = _log_returns(close)
    ru = _when_pos(r); rd = -_when_neg(r)
    cu = _safe_div(ru.rolling(YDAYS, min_periods=QDAYS).std(), ru.rolling(YDAYS, min_periods=QDAYS).mean())
    cd = _safe_div(rd.rolling(YDAYS, min_periods=QDAYS).std(), rd.rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(cu, cd)


def f36_svas_140_robust_cv_asymmetry_mad_over_median_252d(close: pd.Series) -> pd.Series:
    """(MAD/median)(up) - (MAD/median)(|down|) over 252d — robust CV asymmetry."""
    r = _log_returns(close)
    ru = _when_pos(r); rd = -_when_neg(r)
    mu_med = ru.rolling(YDAYS, min_periods=QDAYS).median()
    mu_mad = (ru - mu_med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    md_med = rd.rolling(YDAYS, min_periods=QDAYS).median()
    md_mad = (rd - md_med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(mu_mad, mu_med) - _safe_div(md_mad, md_med)


# ============================================================
# Bucket V — Bar-shape asymmetry (upper wick vs lower wick) (141-146)
# Daily (high-close) vs (close-low) magnitudes — intraday asymmetry
# OWNED here (NOT range-estimator territory).
# ============================================================

def f36_svas_141_upper_wick_minus_lower_wick_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high-close)-(close-low) over 252d — upper-wick vs lower-wick magnitude asymmetry."""
    asym = (high - close) - (close - low)
    return asym.rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_142_upper_over_lower_wick_ratio_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high-close) / (close-low) over 252d — ratio form of wick asymmetry."""
    return _safe_div(high - close, close - low).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_143_normalized_wick_asymmetry_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean [(upper - lower) / (upper + lower)] over 252d — bounded wick asymmetry index."""
    up_w = high - close
    lo_w = close - low
    asym = _safe_div(up_w - lo_w, up_w + lo_w)
    return asym.rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_144_fraction_close_in_lower_third_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d bars where close lies in lower third of daily range — sustained closing weakness."""
    pos = _safe_div(close - low, high - low)
    return (pos < 1.0 / 3.0).astype(float).where(pos.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_145_fraction_close_in_upper_third_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d bars where close lies in upper third of daily range — sustained closing strength."""
    pos = _safe_div(close - low, high - low)
    return (pos > 2.0 / 3.0).astype(float).where(pos.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_146_close_pos_in_range_asymmetry_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction(upper third) - Fraction(lower third) over 252d — closing-strength asymmetry."""
    pos = _safe_div(close - low, high - low)
    up = (pos > 2.0 / 3.0).astype(float).where(pos.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    lo = (pos < 1.0 / 3.0).astype(float).where(pos.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up - lo


# ============================================================
# Bucket W — Multi-bucket composite asymmetry indices (147-150)
# Combine moment / quantile / extreme / streak signals into a few
# composite z-scores. Each composite blends a different *flavor*
# of asymmetry so they don't duplicate.
# ============================================================

def f36_svas_147_composite_moment_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Z-blend of: skew_252 + (-)kurt_252 + Kelly_skew_252 — moment-flavored composite."""
    r = _log_returns(close)
    sk = r.rolling(YDAYS, min_periods=QDAYS).skew()
    kr = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    med = r.rolling(YDAYS, min_periods=QDAYS).median()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    kelly = _safe_div(m - med, sd)
    # Standardise each piece across the broader 504d window so they're commensurate
    z_sk = _rolling_zscore(sk, DDAYS_2Y, min_periods=YDAYS)
    z_kr = _rolling_zscore(kr, DDAYS_2Y, min_periods=YDAYS)
    z_k = _rolling_zscore(kelly, DDAYS_2Y, min_periods=YDAYS)
    return (z_sk - z_kr + z_k) / 3.0


def f36_svas_148_composite_quantile_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Z-blend of: Bowley_skew_252 + outer-quantile-skew_252 + IQR-balance-ratio_252 — quantile-flavored composite."""
    r = _log_returns(close)
    bw = r.rolling(YDAYS, min_periods=QDAYS).apply(_bowley_window, raw=True)
    oq = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _quantile_skew_window(w, 0.10, 0.90), raw=True)
    q25 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q75 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    iqr_r = _safe_div(q75 - q50, q50 - q25)
    z_b = _rolling_zscore(bw, DDAYS_2Y, min_periods=YDAYS)
    z_o = _rolling_zscore(oq, DDAYS_2Y, min_periods=YDAYS)
    z_i = _rolling_zscore(iqr_r, DDAYS_2Y, min_periods=YDAYS)
    return (z_b + z_o + z_i) / 3.0


def f36_svas_149_composite_extreme_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Z-blend of: (-)tail-magnitude-asym_252 + (-)excursion-asym_252 + (-)max-gain-minus-loss_252.
    Wired so MORE-negative output = downside dominates (which is the short-side signal)."""
    r = _log_returns(close)
    ql = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    qh = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    tail_asym = ql.abs() - qh   # >0 = left tail bigger
    dd = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_drawdown_window, raw=True)
    ru = r.rolling(YDAYS, min_periods=QDAYS).apply(_max_runup_window, raw=True)
    exc_asym = dd.abs() - ru
    gain_loss = r.rolling(YDAYS, min_periods=QDAYS).max() - (-r).rolling(YDAYS, min_periods=QDAYS).max()
    z_t = _rolling_zscore(tail_asym, DDAYS_2Y, min_periods=YDAYS)
    z_e = _rolling_zscore(exc_asym, DDAYS_2Y, min_periods=YDAYS)
    z_g = _rolling_zscore(gain_loss, DDAYS_2Y, min_periods=YDAYS)
    return (z_t + z_e - z_g) / 3.0


def f36_svas_150_composite_frequency_streak_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Z-blend of: up_fraction_252 + (-)mean-down-run_252 + (-)P(down|down)_252 —
    frequency-and-persistence-flavored composite asymmetry."""
    r = _log_returns(close)
    uf = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    mdn = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _mean_run_length_window(w, -1), raw=True)
    prev = r.shift(1); md = (prev < 0)
    pdd = _safe_div((r < 0).astype(float).where(md).rolling(YDAYS, min_periods=QDAYS).sum(),
                    md.astype(float).rolling(YDAYS, min_periods=QDAYS).sum())
    z_u = _rolling_zscore(uf, DDAYS_2Y, min_periods=YDAYS)
    z_m = _rolling_zscore(mdn, DDAYS_2Y, min_periods=YDAYS)
    z_p = _rolling_zscore(pdd, DDAYS_2Y, min_periods=YDAYS)
    return (z_u - z_m - z_p) / 3.0


# Bowley / outer-quantile helper functions used by composites (kept local — no cross-family imports).
def _bowley_window(w: np.ndarray) -> float:
    v = w[~np.isnan(w)]
    if v.size < 5:
        return np.nan
    q1, q2, q3 = np.quantile(v, [0.25, 0.5, 0.75])
    den = q3 - q1
    if den == 0:
        return np.nan
    return float((q1 + q3 - 2.0 * q2) / den)


def _quantile_skew_window(w: np.ndarray, ql: float, qh: float) -> float:
    v = w[~np.isnan(w)]
    if v.size < 5:
        return np.nan
    ql_v, q2, qh_v = np.quantile(v, [ql, 0.5, qh])
    den = qh_v - ql_v
    if den == 0:
        return np.nan
    return float((ql_v + qh_v - 2.0 * q2) / den)


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f36_svas_076_max_single_day_gain_21d_d1(close):
    return f36_svas_076_max_single_day_gain_21d(close).diff()


def f36_svas_077_max_single_day_loss_21d_d1(close):
    return f36_svas_077_max_single_day_loss_21d(close).diff()


def f36_svas_078_max_gain_minus_max_loss_252d_d1(close):
    return f36_svas_078_max_gain_minus_max_loss_252d(close).diff()


def f36_svas_079_max_gain_over_max_loss_252d_d1(close):
    return f36_svas_079_max_gain_over_max_loss_252d(close).diff()


def f36_svas_080_max_gain_minus_max_loss_504d_d1(close):
    return f36_svas_080_max_gain_minus_max_loss_504d(close).diff()


def f36_svas_081_normalized_extreme_asymmetry_252d_d1(close):
    return f36_svas_081_normalized_extreme_asymmetry_252d(close).diff()


def f36_svas_082_longest_up_streak_252d_d1(close):
    return f36_svas_082_longest_up_streak_252d(close).diff()


def f36_svas_083_longest_down_streak_252d_d1(close):
    return f36_svas_083_longest_down_streak_252d(close).diff()


def f36_svas_084_streak_length_asymmetry_252d_d1(close):
    return f36_svas_084_streak_length_asymmetry_252d(close).diff()


def f36_svas_085_streak_length_ratio_up_over_down_252d_d1(close):
    return f36_svas_085_streak_length_ratio_up_over_down_252d(close).diff()


def f36_svas_086_mean_up_run_length_252d_d1(close):
    return f36_svas_086_mean_up_run_length_252d(close).diff()


def f36_svas_087_mean_down_run_length_252d_d1(close):
    return f36_svas_087_mean_down_run_length_252d(close).diff()


def f36_svas_088_mean_run_length_asymmetry_252d_d1(close):
    return f36_svas_088_mean_run_length_asymmetry_252d(close).diff()


def f36_svas_089_current_signed_streak_length_d1(close):
    return f36_svas_089_current_signed_streak_length(close).diff()


def f36_svas_090_var_5pct_lower_tail_252d_d1(close):
    return f36_svas_090_var_5pct_lower_tail_252d(close).diff()


def f36_svas_091_var_95pct_upper_tail_252d_d1(close):
    return f36_svas_091_var_95pct_upper_tail_252d(close).diff()


def f36_svas_092_tail_magnitude_asymmetry_5_95_252d_d1(close):
    return f36_svas_092_tail_magnitude_asymmetry_5_95_252d(close).diff()


def f36_svas_093_tail_magnitude_ratio_lower_over_upper_252d_d1(close):
    return f36_svas_093_tail_magnitude_ratio_lower_over_upper_252d(close).diff()


def f36_svas_094_expected_shortfall_lower_5pct_252d_d1(close):
    return f36_svas_094_expected_shortfall_lower_5pct_252d(close).diff()


def f36_svas_095_expected_shortfall_upper_95pct_252d_d1(close):
    return f36_svas_095_expected_shortfall_upper_95pct_252d(close).diff()


def f36_svas_096_es_magnitude_asymmetry_252d_d1(close):
    return f36_svas_096_es_magnitude_asymmetry_252d(close).diff()


def f36_svas_097_es_ratio_lower_over_upper_252d_d1(close):
    return f36_svas_097_es_ratio_lower_over_upper_252d(close).diff()


def f36_svas_098_quantile_asymmetry_25_75_252d_d1(close):
    return f36_svas_098_quantile_asymmetry_25_75_252d(close).diff()


def f36_svas_099_quantile_asymmetry_10_90_252d_d1(close):
    return f36_svas_099_quantile_asymmetry_10_90_252d(close).diff()


def f36_svas_100_iqr_balance_ratio_252d_d1(close):
    return f36_svas_100_iqr_balance_ratio_252d(close).diff()


def f36_svas_101_outer_decile_balance_ratio_252d_d1(close):
    return f36_svas_101_outer_decile_balance_ratio_252d(close).diff()


def f36_svas_102_extreme_decile_balance_ratio_252d_d1(close):
    return f36_svas_102_extreme_decile_balance_ratio_252d(close).diff()


def f36_svas_103_median_position_in_range_252d_d1(close):
    return f36_svas_103_median_position_in_range_252d(close).diff()


def f36_svas_104_fraction_time_below_zero_cum_return_252d_d1(close):
    return f36_svas_104_fraction_time_below_zero_cum_return_252d(close).diff()


def f36_svas_105_fraction_time_above_zero_cum_return_252d_d1(close):
    return f36_svas_105_fraction_time_above_zero_cum_return_252d(close).diff()


def f36_svas_106_time_in_regime_asymmetry_252d_d1(close):
    return f36_svas_106_time_in_regime_asymmetry_252d(close).diff()


def f36_svas_107_fraction_above_below_zero_ratio_252d_d1(close):
    return f36_svas_107_fraction_above_below_zero_ratio_252d(close).diff()


def f36_svas_108_fraction_consec_negative_252d_d1(close):
    return f36_svas_108_fraction_consec_negative_252d(close).diff()


def f36_svas_109_max_drawdown_log_252d_d1(close):
    return f36_svas_109_max_drawdown_log_252d(close).diff()


def f36_svas_110_max_runup_log_252d_d1(close):
    return f36_svas_110_max_runup_log_252d(close).diff()


def f36_svas_111_drawdown_runup_asymmetry_252d_d1(close):
    return f36_svas_111_drawdown_runup_asymmetry_252d(close).diff()


def f36_svas_112_drawdown_runup_ratio_252d_d1(close):
    return f36_svas_112_drawdown_runup_ratio_252d(close).diff()


def f36_svas_113_max_drawdown_log_504d_d1(close):
    return f36_svas_113_max_drawdown_log_504d(close).diff()


def f36_svas_114_max_runup_log_504d_d1(close):
    return f36_svas_114_max_runup_log_504d(close).diff()


def f36_svas_115_drawdown_runup_asymmetry_504d_d1(close):
    return f36_svas_115_drawdown_runup_asymmetry_504d(close).diff()


def f36_svas_116_normalized_excursion_asymmetry_252d_d1(close):
    return f36_svas_116_normalized_excursion_asymmetry_252d(close).diff()


def f36_svas_117_volume_on_up_days_mean_252d_d1(close, volume):
    return f36_svas_117_volume_on_up_days_mean_252d(close, volume).diff()


def f36_svas_118_volume_on_down_days_mean_252d_d1(close, volume):
    return f36_svas_118_volume_on_down_days_mean_252d(close, volume).diff()


def f36_svas_119_volume_asymmetry_ratio_up_over_down_252d_d1(close, volume):
    return f36_svas_119_volume_asymmetry_ratio_up_over_down_252d(close, volume).diff()


def f36_svas_120_log_volume_asymmetry_up_down_252d_d1(close, volume):
    return f36_svas_120_log_volume_asymmetry_up_down_252d(close, volume).diff()


def f36_svas_121_avg_gain_on_high_vol_up_days_252d_d1(close, volume):
    return f36_svas_121_avg_gain_on_high_vol_up_days_252d(close, volume).diff()


def f36_svas_122_avg_loss_on_high_vol_down_days_252d_d1(close, volume):
    return f36_svas_122_avg_loss_on_high_vol_down_days_252d(close, volume).diff()


def f36_svas_123_high_vol_gain_minus_loss_252d_d1(close, volume):
    return f36_svas_123_high_vol_gain_minus_loss_252d(close, volume).diff()


def f36_svas_124_dollar_volume_asymmetry_up_down_252d_d1(close, volume):
    return f36_svas_124_dollar_volume_asymmetry_up_down_252d(close, volume).diff()


def f36_svas_125_autocorr_after_up_day_252d_d1(close):
    return f36_svas_125_autocorr_after_up_day_252d(close).diff()


def f36_svas_126_autocorr_after_down_day_252d_d1(close):
    return f36_svas_126_autocorr_after_down_day_252d(close).diff()


def f36_svas_127_autocorr_asymmetry_up_minus_down_252d_d1(close):
    return f36_svas_127_autocorr_asymmetry_up_minus_down_252d(close).diff()


def f36_svas_128_p_up_after_up_252d_d1(close):
    return f36_svas_128_p_up_after_up_252d(close).diff()


def f36_svas_129_p_down_after_down_252d_d1(close):
    return f36_svas_129_p_down_after_down_252d(close).diff()


def f36_svas_130_sign_persistence_asymmetry_252d_d1(close):
    return f36_svas_130_sign_persistence_asymmetry_252d(close).diff()


def f36_svas_131_count_extreme_up_3sigma_252d_d1(close):
    return f36_svas_131_count_extreme_up_3sigma_252d(close).diff()


def f36_svas_132_count_extreme_down_3sigma_252d_d1(close):
    return f36_svas_132_count_extreme_down_3sigma_252d(close).diff()


def f36_svas_133_extreme_day_count_asymmetry_252d_d1(close):
    return f36_svas_133_extreme_day_count_asymmetry_252d(close).diff()


def f36_svas_134_count_extreme_up_2sigma_252d_d1(close):
    return f36_svas_134_count_extreme_up_2sigma_252d(close).diff()


def f36_svas_135_count_extreme_down_2sigma_252d_d1(close):
    return f36_svas_135_count_extreme_down_2sigma_252d(close).diff()


def f36_svas_136_cv_up_returns_252d_d1(close):
    return f36_svas_136_cv_up_returns_252d(close).diff()


def f36_svas_137_cv_down_returns_252d_d1(close):
    return f36_svas_137_cv_down_returns_252d(close).diff()


def f36_svas_138_cv_asymmetry_up_minus_down_252d_d1(close):
    return f36_svas_138_cv_asymmetry_up_minus_down_252d(close).diff()


def f36_svas_139_cv_ratio_up_over_down_252d_d1(close):
    return f36_svas_139_cv_ratio_up_over_down_252d(close).diff()


def f36_svas_140_robust_cv_asymmetry_mad_over_median_252d_d1(close):
    return f36_svas_140_robust_cv_asymmetry_mad_over_median_252d(close).diff()


def f36_svas_141_upper_wick_minus_lower_wick_mean_252d_d1(high, low, close):
    return f36_svas_141_upper_wick_minus_lower_wick_mean_252d(high, low, close).diff()


def f36_svas_142_upper_over_lower_wick_ratio_mean_252d_d1(high, low, close):
    return f36_svas_142_upper_over_lower_wick_ratio_mean_252d(high, low, close).diff()


def f36_svas_143_normalized_wick_asymmetry_mean_252d_d1(high, low, close):
    return f36_svas_143_normalized_wick_asymmetry_mean_252d(high, low, close).diff()


def f36_svas_144_fraction_close_in_lower_third_252d_d1(high, low, close):
    return f36_svas_144_fraction_close_in_lower_third_252d(high, low, close).diff()


def f36_svas_145_fraction_close_in_upper_third_252d_d1(high, low, close):
    return f36_svas_145_fraction_close_in_upper_third_252d(high, low, close).diff()


def f36_svas_146_close_pos_in_range_asymmetry_252d_d1(high, low, close):
    return f36_svas_146_close_pos_in_range_asymmetry_252d(high, low, close).diff()


def f36_svas_147_composite_moment_asymmetry_252d_d1(close):
    return f36_svas_147_composite_moment_asymmetry_252d(close).diff()


def f36_svas_148_composite_quantile_asymmetry_252d_d1(close):
    return f36_svas_148_composite_quantile_asymmetry_252d(close).diff()


def f36_svas_149_composite_extreme_asymmetry_252d_d1(close):
    return f36_svas_149_composite_extreme_asymmetry_252d(close).diff()


def f36_svas_150_composite_frequency_streak_asymmetry_252d_d1(close):
    return f36_svas_150_composite_frequency_streak_asymmetry_252d(close).diff()


SEMI_VARIANCE_ASYMMETRY_D1_REGISTRY_076_150 = {
    "f36_svas_076_max_single_day_gain_21d_d1": {"inputs": ["close"], "func": f36_svas_076_max_single_day_gain_21d_d1},
    "f36_svas_077_max_single_day_loss_21d_d1": {"inputs": ["close"], "func": f36_svas_077_max_single_day_loss_21d_d1},
    "f36_svas_078_max_gain_minus_max_loss_252d_d1": {"inputs": ["close"], "func": f36_svas_078_max_gain_minus_max_loss_252d_d1},
    "f36_svas_079_max_gain_over_max_loss_252d_d1": {"inputs": ["close"], "func": f36_svas_079_max_gain_over_max_loss_252d_d1},
    "f36_svas_080_max_gain_minus_max_loss_504d_d1": {"inputs": ["close"], "func": f36_svas_080_max_gain_minus_max_loss_504d_d1},
    "f36_svas_081_normalized_extreme_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_081_normalized_extreme_asymmetry_252d_d1},
    "f36_svas_082_longest_up_streak_252d_d1": {"inputs": ["close"], "func": f36_svas_082_longest_up_streak_252d_d1},
    "f36_svas_083_longest_down_streak_252d_d1": {"inputs": ["close"], "func": f36_svas_083_longest_down_streak_252d_d1},
    "f36_svas_084_streak_length_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_084_streak_length_asymmetry_252d_d1},
    "f36_svas_085_streak_length_ratio_up_over_down_252d_d1": {"inputs": ["close"], "func": f36_svas_085_streak_length_ratio_up_over_down_252d_d1},
    "f36_svas_086_mean_up_run_length_252d_d1": {"inputs": ["close"], "func": f36_svas_086_mean_up_run_length_252d_d1},
    "f36_svas_087_mean_down_run_length_252d_d1": {"inputs": ["close"], "func": f36_svas_087_mean_down_run_length_252d_d1},
    "f36_svas_088_mean_run_length_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_088_mean_run_length_asymmetry_252d_d1},
    "f36_svas_089_current_signed_streak_length_d1": {"inputs": ["close"], "func": f36_svas_089_current_signed_streak_length_d1},
    "f36_svas_090_var_5pct_lower_tail_252d_d1": {"inputs": ["close"], "func": f36_svas_090_var_5pct_lower_tail_252d_d1},
    "f36_svas_091_var_95pct_upper_tail_252d_d1": {"inputs": ["close"], "func": f36_svas_091_var_95pct_upper_tail_252d_d1},
    "f36_svas_092_tail_magnitude_asymmetry_5_95_252d_d1": {"inputs": ["close"], "func": f36_svas_092_tail_magnitude_asymmetry_5_95_252d_d1},
    "f36_svas_093_tail_magnitude_ratio_lower_over_upper_252d_d1": {"inputs": ["close"], "func": f36_svas_093_tail_magnitude_ratio_lower_over_upper_252d_d1},
    "f36_svas_094_expected_shortfall_lower_5pct_252d_d1": {"inputs": ["close"], "func": f36_svas_094_expected_shortfall_lower_5pct_252d_d1},
    "f36_svas_095_expected_shortfall_upper_95pct_252d_d1": {"inputs": ["close"], "func": f36_svas_095_expected_shortfall_upper_95pct_252d_d1},
    "f36_svas_096_es_magnitude_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_096_es_magnitude_asymmetry_252d_d1},
    "f36_svas_097_es_ratio_lower_over_upper_252d_d1": {"inputs": ["close"], "func": f36_svas_097_es_ratio_lower_over_upper_252d_d1},
    "f36_svas_098_quantile_asymmetry_25_75_252d_d1": {"inputs": ["close"], "func": f36_svas_098_quantile_asymmetry_25_75_252d_d1},
    "f36_svas_099_quantile_asymmetry_10_90_252d_d1": {"inputs": ["close"], "func": f36_svas_099_quantile_asymmetry_10_90_252d_d1},
    "f36_svas_100_iqr_balance_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_100_iqr_balance_ratio_252d_d1},
    "f36_svas_101_outer_decile_balance_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_101_outer_decile_balance_ratio_252d_d1},
    "f36_svas_102_extreme_decile_balance_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_102_extreme_decile_balance_ratio_252d_d1},
    "f36_svas_103_median_position_in_range_252d_d1": {"inputs": ["close"], "func": f36_svas_103_median_position_in_range_252d_d1},
    "f36_svas_104_fraction_time_below_zero_cum_return_252d_d1": {"inputs": ["close"], "func": f36_svas_104_fraction_time_below_zero_cum_return_252d_d1},
    "f36_svas_105_fraction_time_above_zero_cum_return_252d_d1": {"inputs": ["close"], "func": f36_svas_105_fraction_time_above_zero_cum_return_252d_d1},
    "f36_svas_106_time_in_regime_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_106_time_in_regime_asymmetry_252d_d1},
    "f36_svas_107_fraction_above_below_zero_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_107_fraction_above_below_zero_ratio_252d_d1},
    "f36_svas_108_fraction_consec_negative_252d_d1": {"inputs": ["close"], "func": f36_svas_108_fraction_consec_negative_252d_d1},
    "f36_svas_109_max_drawdown_log_252d_d1": {"inputs": ["close"], "func": f36_svas_109_max_drawdown_log_252d_d1},
    "f36_svas_110_max_runup_log_252d_d1": {"inputs": ["close"], "func": f36_svas_110_max_runup_log_252d_d1},
    "f36_svas_111_drawdown_runup_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_111_drawdown_runup_asymmetry_252d_d1},
    "f36_svas_112_drawdown_runup_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_112_drawdown_runup_ratio_252d_d1},
    "f36_svas_113_max_drawdown_log_504d_d1": {"inputs": ["close"], "func": f36_svas_113_max_drawdown_log_504d_d1},
    "f36_svas_114_max_runup_log_504d_d1": {"inputs": ["close"], "func": f36_svas_114_max_runup_log_504d_d1},
    "f36_svas_115_drawdown_runup_asymmetry_504d_d1": {"inputs": ["close"], "func": f36_svas_115_drawdown_runup_asymmetry_504d_d1},
    "f36_svas_116_normalized_excursion_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_116_normalized_excursion_asymmetry_252d_d1},
    "f36_svas_117_volume_on_up_days_mean_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_117_volume_on_up_days_mean_252d_d1},
    "f36_svas_118_volume_on_down_days_mean_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_118_volume_on_down_days_mean_252d_d1},
    "f36_svas_119_volume_asymmetry_ratio_up_over_down_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_119_volume_asymmetry_ratio_up_over_down_252d_d1},
    "f36_svas_120_log_volume_asymmetry_up_down_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_120_log_volume_asymmetry_up_down_252d_d1},
    "f36_svas_121_avg_gain_on_high_vol_up_days_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_121_avg_gain_on_high_vol_up_days_252d_d1},
    "f36_svas_122_avg_loss_on_high_vol_down_days_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_122_avg_loss_on_high_vol_down_days_252d_d1},
    "f36_svas_123_high_vol_gain_minus_loss_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_123_high_vol_gain_minus_loss_252d_d1},
    "f36_svas_124_dollar_volume_asymmetry_up_down_252d_d1": {"inputs": ["close", "volume"], "func": f36_svas_124_dollar_volume_asymmetry_up_down_252d_d1},
    "f36_svas_125_autocorr_after_up_day_252d_d1": {"inputs": ["close"], "func": f36_svas_125_autocorr_after_up_day_252d_d1},
    "f36_svas_126_autocorr_after_down_day_252d_d1": {"inputs": ["close"], "func": f36_svas_126_autocorr_after_down_day_252d_d1},
    "f36_svas_127_autocorr_asymmetry_up_minus_down_252d_d1": {"inputs": ["close"], "func": f36_svas_127_autocorr_asymmetry_up_minus_down_252d_d1},
    "f36_svas_128_p_up_after_up_252d_d1": {"inputs": ["close"], "func": f36_svas_128_p_up_after_up_252d_d1},
    "f36_svas_129_p_down_after_down_252d_d1": {"inputs": ["close"], "func": f36_svas_129_p_down_after_down_252d_d1},
    "f36_svas_130_sign_persistence_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_130_sign_persistence_asymmetry_252d_d1},
    "f36_svas_131_count_extreme_up_3sigma_252d_d1": {"inputs": ["close"], "func": f36_svas_131_count_extreme_up_3sigma_252d_d1},
    "f36_svas_132_count_extreme_down_3sigma_252d_d1": {"inputs": ["close"], "func": f36_svas_132_count_extreme_down_3sigma_252d_d1},
    "f36_svas_133_extreme_day_count_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_133_extreme_day_count_asymmetry_252d_d1},
    "f36_svas_134_count_extreme_up_2sigma_252d_d1": {"inputs": ["close"], "func": f36_svas_134_count_extreme_up_2sigma_252d_d1},
    "f36_svas_135_count_extreme_down_2sigma_252d_d1": {"inputs": ["close"], "func": f36_svas_135_count_extreme_down_2sigma_252d_d1},
    "f36_svas_136_cv_up_returns_252d_d1": {"inputs": ["close"], "func": f36_svas_136_cv_up_returns_252d_d1},
    "f36_svas_137_cv_down_returns_252d_d1": {"inputs": ["close"], "func": f36_svas_137_cv_down_returns_252d_d1},
    "f36_svas_138_cv_asymmetry_up_minus_down_252d_d1": {"inputs": ["close"], "func": f36_svas_138_cv_asymmetry_up_minus_down_252d_d1},
    "f36_svas_139_cv_ratio_up_over_down_252d_d1": {"inputs": ["close"], "func": f36_svas_139_cv_ratio_up_over_down_252d_d1},
    "f36_svas_140_robust_cv_asymmetry_mad_over_median_252d_d1": {"inputs": ["close"], "func": f36_svas_140_robust_cv_asymmetry_mad_over_median_252d_d1},
    "f36_svas_141_upper_wick_minus_lower_wick_mean_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_141_upper_wick_minus_lower_wick_mean_252d_d1},
    "f36_svas_142_upper_over_lower_wick_ratio_mean_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_142_upper_over_lower_wick_ratio_mean_252d_d1},
    "f36_svas_143_normalized_wick_asymmetry_mean_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_143_normalized_wick_asymmetry_mean_252d_d1},
    "f36_svas_144_fraction_close_in_lower_third_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_144_fraction_close_in_lower_third_252d_d1},
    "f36_svas_145_fraction_close_in_upper_third_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_145_fraction_close_in_upper_third_252d_d1},
    "f36_svas_146_close_pos_in_range_asymmetry_252d_d1": {"inputs": ["high", "low", "close"], "func": f36_svas_146_close_pos_in_range_asymmetry_252d_d1},
    "f36_svas_147_composite_moment_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_147_composite_moment_asymmetry_252d_d1},
    "f36_svas_148_composite_quantile_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_148_composite_quantile_asymmetry_252d_d1},
    "f36_svas_149_composite_extreme_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_149_composite_extreme_asymmetry_252d_d1},
    "f36_svas_150_composite_frequency_streak_asymmetry_252d_d1": {"inputs": ["close"], "func": f36_svas_150_composite_frequency_streak_asymmetry_252d_d1},
}
