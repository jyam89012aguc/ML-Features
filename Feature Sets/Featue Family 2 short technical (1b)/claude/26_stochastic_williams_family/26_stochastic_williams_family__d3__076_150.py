"""stochastic_williams_family base features 076-150 — Pipeline 1b-technical.

Continues 001-075 with new buckets:
J: Ultimate Oscillator variants.
K: SMI (Stochastic Momentum Index) variants.
L: K-D hook patterns / failed crosses.
M: Vol-of-stoch / stoch-range / dispersion.
N: Multi-horizon stoch alignment.
O: Time-since events (different reference points than 001-075).
P: Composite blow-off / topping signals.
Q: Smoothing / regime / fast-vs-slow ratios.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers (no cross-file imports).
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


def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k


def _stoch_d(k, n_d):
    return k.rolling(n_d, min_periods=max(n_d // 2, 1)).mean()


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


def _stoch_rsi_kd(close, n_rsi=14, n_k=14, smooth_k=3, smooth_d=3):
    r = _rsi(close, n_rsi)
    ll = r.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = r.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    k = raw_k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    d = k.rolling(smooth_d, min_periods=max(smooth_d // 2, 1)).mean()
    return k, d


def _ultimate_osc(high, low, close, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    s1 = bp.rolling(n1, min_periods=max(n1 // 3, 2)).sum() / tr.rolling(n1, min_periods=max(n1 // 3, 2)).sum()
    s2 = bp.rolling(n2, min_periods=max(n2 // 3, 2)).sum() / tr.rolling(n2, min_periods=max(n2 // 3, 2)).sum()
    s3 = bp.rolling(n3, min_periods=max(n3 // 3, 2)).sum() / tr.rolling(n3, min_periods=max(n3 // 3, 2)).sum()
    return 100.0 * (4.0 * s1 + 2.0 * s2 + s3) / 7.0


def _smi(high, low, close, n1=25, n2=13):
    ll = low.rolling(n1, min_periods=max(n1 // 3, 2)).min()
    hh = high.rolling(n1, min_periods=max(n1 // 3, 2)).max()
    midpt = (hh + ll) / 2.0
    cm = close - midpt
    rng = hh - ll
    e1 = cm.ewm(span=n2, adjust=False, min_periods=max(n2 // 2, 2)).mean()
    e2 = e1.ewm(span=n2, adjust=False, min_periods=max(n2 // 2, 2)).mean()
    r1 = rng.ewm(span=n2, adjust=False, min_periods=max(n2 // 2, 2)).mean()
    r2 = r1.ewm(span=n2, adjust=False, min_periods=max(n2 // 2, 2)).mean()
    return 100.0 * _safe_div(e2, r2 / 2.0)


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


# ============================================================
# Bucket J — Ultimate Oscillator variants (076-085)
# ============================================================

def f26_stwf_076_ult_osc_7_14_28(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams' Ultimate Oscillator classical (7/14/28) — level."""
    return _ultimate_osc(high, low, close)


def f26_stwf_077_ult_osc_above_70_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if UO > 70 — Williams' classical OB threshold."""
    uo = _ultimate_osc(high, low, close)
    return (uo > 70.0).astype(float).where(uo.notna(), np.nan)


def f26_stwf_078_ult_osc_just_exited_above_70(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if UO crossed back below 70 this bar — Williams' OB-exit trigger."""
    uo = _ultimate_osc(high, low, close)
    return ((uo.shift(1) > 70.0) & (uo <= 70.0)).astype(float).where(uo.notna(), np.nan)


def f26_stwf_079_ult_osc_dwell_above_70_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with UO > 70 — Williams OB dwell."""
    uo = _ultimate_osc(high, low, close)
    return (uo > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(uo.notna(), np.nan)


def f26_stwf_080_ult_osc_bars_since_topped_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since UO hit its trailing 252d max — recency of UO peak."""
    uo = _ultimate_osc(high, low, close)
    at_max = uo == uo.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f26_stwf_081_ult_osc_peak_decay_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO 63d-max minus its value 63 bars ago — quarterly UO peak decay."""
    uo = _ultimate_osc(high, low, close)
    pmax = uo.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f26_stwf_082_ult_osc_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of UO over trailing 252d — distribution-relative momentum extreme."""
    uo = _ultimate_osc(high, low, close)
    return _rolling_zscore(uo, YDAYS, min_periods=QDAYS)


def f26_stwf_083_ult_osc_pct_rank_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of UO — distribution-based OB position."""
    uo = _ultimate_osc(high, low, close)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return uo.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f26_stwf_084_ult_osc_area_above_70_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of (UO - 70) over OB bars in 252 — UO saturation intensity."""
    uo = _ultimate_osc(high, low, close)
    area = (uo - 70.0).clip(lower=0).where(uo.notna(), np.nan)
    return area.rolling(YDAYS, min_periods=QDAYS).sum()


def f26_stwf_085_ult_osc_count_above_70_exits_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of UO OB-exits in 252 bars — annual UO turnover frequency."""
    uo = _ultimate_osc(high, low, close)
    ev = ((uo.shift(1) > 70.0) & (uo <= 70.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(uo.notna(), np.nan)


# ============================================================
# Bucket K — SMI variants (086-093)
# ============================================================

def f26_stwf_086_smi_25_13(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic Momentum Index (25,13) — double-smoothed centered momentum."""
    return _smi(high, low, close)


def f26_stwf_087_smi_above_40_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SMI > 40 — SMI OB threshold."""
    s = _smi(high, low, close)
    return (s > 40.0).astype(float).where(s.notna(), np.nan)


def f26_stwf_088_smi_just_exited_above_40(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SMI crossed back below 40 this bar — SMI OB-exit."""
    s = _smi(high, low, close)
    return ((s.shift(1) > 40.0) & (s <= 40.0)).astype(float).where(s.notna(), np.nan)


def f26_stwf_089_smi_dwell_above_40_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with SMI > 40 — SMI OB dwell."""
    s = _smi(high, low, close)
    return (s > 40.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)


def f26_stwf_090_smi_bars_since_topped_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since SMI hit its trailing 252d max."""
    s = _smi(high, low, close)
    at_max = s == s.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f26_stwf_091_smi_peak_decay_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMI 63d-max minus its value 63 bars ago — SMI peak decay."""
    s = _smi(high, low, close)
    pmax = s.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f26_stwf_092_smi_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of SMI over trailing 252d."""
    return _rolling_zscore(_smi(high, low, close), YDAYS, min_periods=QDAYS)


def f26_stwf_093_smi_signal_cross_down(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SMI crossed below its EMA(7) signal line this bar — SMI bearish cross trigger."""
    s = _smi(high, low, close)
    sig = s.ewm(span=7, adjust=False, min_periods=3).mean()
    diff = s - sig
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)


# ============================================================
# Bucket L — K-D hook patterns / failed crosses (094-101)
# ============================================================

def f26_stwf_094_kd_hook_at_top_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K crosses below D while both K and D > 80 — top hook (highest-quality stoch bearish trigger)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    ev = (diff.shift(1) > 0) & (diff <= 0) & (k > 80.0) & (d > 80.0)
    return ev.astype(float).where(diff.notna(), np.nan)


def f26_stwf_095_bullish_then_bearish_cross_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if a bearish K/D cross occurred within 21 bars of a prior bullish K/D cross — fake-out signal."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    bu = (diff.shift(1) <= 0) & (diff > 0)
    be = (diff.shift(1) > 0) & (diff <= 0)
    bu_in_21 = bu.rolling(MDAYS, min_periods=1).sum() > 0
    return (be & bu_in_21).astype(float).where(diff.notna(), np.nan)


def f26_stwf_096_kd_compression_at_ob_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """In OB zone, K-D compression = -|K-D| (smaller spread => tighter top consolidation)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    in_ob = (k > 80.0) & (d > 80.0)
    return (-(k - d).abs()).where(in_ob, np.nan)


def f26_stwf_097_bearish_cross_at_or_above_90_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K crossed below D while K >= 90 — premium bearish trigger (deep-OB exit)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    ev = (diff.shift(1) > 0) & (diff <= 0) & (k.shift(1) >= 90.0)
    return ev.astype(float).where(diff.notna(), np.nan)


def f26_stwf_098_cross_density_in_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of K/D crosses (either direction) while K > 80, in past 63 bars — OB-zone churn."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    cross = ((diff.shift(1) * diff) < 0) & (k > 80.0)
    return cross.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)


def f26_stwf_099_cross_failures_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bullish K/D crosses that reverted to bearish within 21 bars, past 252 — bullish-failure rate."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    bu = ((diff.shift(1) <= 0) & (diff > 0)).astype(float)
    be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    be_next_21 = be.rolling(MDAYS, min_periods=1).sum().shift(MDAYS).fillna(0)
    # Replace the .shift(21) with backward look: bullish cross 21 bars ago that was followed by bearish in next 21
    bu_21_ago = bu.shift(MDAYS)
    be_in_window = be.rolling(MDAYS, min_periods=1).sum()
    fail = (bu_21_ago > 0) & (be_in_window > 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(diff.notna(), np.nan)


def f26_stwf_100_recurring_bearish_cross_pattern_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if >=3 distinct bearish K/D crosses in past 63 bars — recurring failure pattern."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    cnt = be.rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt >= 3.0).astype(float).where(diff.notna(), np.nan)


def f26_stwf_101_multi_horizon_kd_bearish_cross_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {14, 63, 252} where K/D bearish cross fired in the past 5 bars."""
    out = pd.Series(0.0, index=close.index)
    cnt = pd.Series(0.0, index=close.index)
    for n in (14, QDAYS, YDAYS):
        k = _stoch_k(high, low, close, n)
        d = _stoch_d(k, max(3, n // 14))
        diff = k - d
        ev = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
        in_window = ev.rolling(WDAYS, min_periods=1).sum() > 0
        cnt = cnt + in_window.astype(float)
    return cnt.where(close.notna(), np.nan)


# ============================================================
# Bucket M — vol-of-stoch / range / dispersion (102-110)
# ============================================================

def f26_stwf_102_stoch_range_high_minus_low_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K(14) 63d max - 63d min — quarterly oscillator amplitude (narrow = squeeze)."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(QDAYS, min_periods=MDAYS).max() - k.rolling(QDAYS, min_periods=MDAYS).min()


def f26_stwf_103_stoch_vol_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard deviation of %K(14) over 21 bars — monthly stoch volatility."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(MDAYS, min_periods=WDAYS).std()


def f26_stwf_104_stoch_vol_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Standard deviation of %K(14) over 63 bars — quarterly stoch volatility."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(QDAYS, min_periods=MDAYS).std()


def f26_stwf_105_stoch_vol_of_vol_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (21d std of %K) over 63 bars — vol-of-vol of stoch."""
    k = _stoch_k(high, low, close, 14)
    sd21 = k.rolling(MDAYS, min_periods=WDAYS).std()
    return sd21.rolling(QDAYS, min_periods=MDAYS).std()


def f26_stwf_106_stoch_distance_from_21d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K(14) minus its rolling 21d mean — short-term mean-reversion distance."""
    k = _stoch_k(high, low, close, 14)
    return k - k.rolling(MDAYS, min_periods=WDAYS).mean()


def f26_stwf_107_stoch_distance_from_63d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K(14) minus its rolling 63d mean — quarterly mean-reversion distance."""
    k = _stoch_k(high, low, close, 14)
    return k - k.rolling(QDAYS, min_periods=MDAYS).mean()


def f26_stwf_108_stoch_distance_from_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K(14) minus its rolling 252d mean — annual mean-reversion distance."""
    k = _stoch_k(high, low, close, 14)
    return k - k.rolling(YDAYS, min_periods=QDAYS).mean()


def f26_stwf_109_stoch_skew_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of %K(14) over 63 bars — asymmetry of oscillator distribution."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(QDAYS, min_periods=MDAYS).skew()


def f26_stwf_110_stoch_kurtosis_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Excess kurtosis of %K(14) over 63 bars — tail behavior of stoch."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(QDAYS, min_periods=MDAYS).kurt()


# ============================================================
# Bucket N — multi-horizon stoch alignment (111-120)
# ============================================================

def f26_stwf_111_all_horizons_in_ob_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14), K(63), K(252) are all > 80 — confirmed multi-horizon OB."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    return ((k1 > 80.0) & (k2 > 80.0) & (k3 > 80.0)).astype(float).where(
        k1.notna() & k2.notna() & k3.notna(), np.nan)


def f26_stwf_112_count_horizons_in_ob(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons in {14, 63, 252} with K > 80 — multi-horizon OB breadth."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    cnt = (k1 > 80.0).astype(float) + (k2 > 80.0).astype(float) + (k3 > 80.0).astype(float)
    return cnt.where(k1.notna() & k2.notna() & k3.notna(), np.nan)


def f26_stwf_113_short_leads_long_ob_exit_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) exited OB but K(63) still > 80 — short-horizon leading-bearish indicator."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    return ((k1 <= 80.0) & (k2 > 80.0) & (k1.shift(1) > 80.0)).astype(float).where(
        k1.notna() & k2.notna(), np.nan)


def f26_stwf_114_monotonic_stoch_decline_across_horizons(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) < K(63) < K(252) — monotonic decline-across-horizons (short lower than long means deceleration)."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    return ((k1 < k2) & (k2 < k3)).astype(float).where(
        k1.notna() & k2.notna() & k3.notna(), np.nan)


def f26_stwf_115_ribbon_avg_stoch_k(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average of K(14), K(63), K(252) — multi-horizon stoch ribbon center."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    return (k1 + k2 + k3) / 3.0


def f26_stwf_116_ribbon_dispersion_stoch_k(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of {K(14), K(63), K(252)} — multi-horizon stoch ribbon dispersion (high = horizons disagree)."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    return pd.concat([k1.rename("k1"), k2.rename("k2"), k3.rename("k3")], axis=1).std(axis=1)


def f26_stwf_117_short_minus_long_horizon_k_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) - K(252) — short-horizon momentum minus long-horizon momentum (positive = short exceeding long)."""
    return _stoch_k(high, low, close, 14) - _stoch_k(high, low, close, YDAYS)


def f26_stwf_118_short_ob_followed_by_long_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) was in OB sometime in past 63 bars AND K(252) currently in OB — short-OB precedes long-OB."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, YDAYS)
    short_recent = (k1 > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
    return (short_recent & (k2 > 80.0)).astype(float).where(k1.notna() & k2.notna(), np.nan)


def f26_stwf_119_long_horizon_ob_while_short_exits(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(252) > 80 AND K(14) just exited OB — slow-trend OB while fast trend cools (bear setup)."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, YDAYS)
    just_exit = (k1.shift(1) > 80.0) & (k1 <= 80.0)
    return ((k2 > 80.0) & just_exit).astype(float).where(k1.notna() & k2.notna(), np.nan)


def f26_stwf_120_horizon_ob_ratio_short_to_long_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: (fraction time K(14) > 80 in 252d) / (fraction time K(252) > 80 in 252d) — short-fast/slow OB ratio."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, YDAYS)
    f1 = (k1 > 80.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    f2 = (k2 > 80.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(f1, f2)


# ============================================================
# Bucket O — time-since events (different reference points than 001-075) (121-130)
# ============================================================

def f26_stwf_121_days_since_stoch_above_95(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since %K(14) was > 95 — extreme-OB recency (different threshold than 028)."""
    k = _stoch_k(high, low, close, 14)
    return _bars_since_true(k > 95.0)


def f26_stwf_122_days_since_stoch_below_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since %K(14) was < 20 — oversold recency. Long dwell without OS = persistent up-trend
    (consistent with multi-year top-zone exhaustion before crash)."""
    k = _stoch_k(high, low, close, 14)
    return _bars_since_true(k < 20.0)


def f26_stwf_123_days_since_williams_r_above_minus10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since Williams %R > -10 — recency of extreme Williams OB."""
    wr = _williams_r(high, low, close, 14)
    return _bars_since_true(wr > -10.0)


def f26_stwf_124_days_since_stoch_rsi_at_252_max(close: pd.Series) -> pd.Series:
    """Days since Stoch-RSI K hit its 252d max — recency of momentum-of-RSI peak."""
    k, _ = _stoch_rsi_kd(close)
    at_max = k == k.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f26_stwf_125_days_since_ult_osc_above_75(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since UO > 75 — recency of strong UO OB (different threshold than 080)."""
    uo = _ultimate_osc(high, low, close)
    return _bars_since_true(uo > 75.0)


def f26_stwf_126_days_since_smi_above_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since SMI > 50 — extreme SMI recency (different threshold than SMI > 40 in bucket K)."""
    s = _smi(high, low, close)
    return _bars_since_true(s > 50.0)


def f26_stwf_127_days_since_last_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Days since most-recent annual-horizon bearish K-divergence — long-horizon div recency."""
    k = _stoch_k(high, low, close, 14)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_kmax = k.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = p_new & (k < prior_kmax)
    return _bars_since_true(ev)


def f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K re-entered OB within 21 bars after an exit — quick re-test (top-exhaustion bull bias eroding)."""
    k = _stoch_k(high, low, close, 14)
    exited = (k.shift(1) > 80.0) & (k <= 80.0)
    entered = (k.shift(1) <= 80.0) & (k > 80.0)
    recent_exit = exited.rolling(MDAYS, min_periods=1).sum().shift(1) > 0
    return (entered & recent_exit).astype(float).where(k.notna(), np.nan)


def f26_stwf_129_stoch_dwell_above_q90_distribution_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where %K exceeded its 252d 90th percentile — distribution-based OB dwell."""
    k = _stoch_k(high, low, close, 14)
    q90 = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (k > q90).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(k.notna() & q90.notna(), np.nan)


def f26_stwf_130_consecutive_higher_oscillator_peaks_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in past 63 where 21d K-max is higher than previous 21d K-max — series of higher peaks (still bullish-momentum context that becomes critical near top)."""
    k = _stoch_k(high, low, close, 14)
    pmax = k.rolling(MDAYS, min_periods=WDAYS).max()
    higher = (pmax > pmax.shift(MDAYS)).astype(float)
    return higher.rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


# ============================================================
# Bucket P — composite blow-off / topping (131-138)
# ============================================================

def f26_stwf_131_multi_oscillator_blowoff_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of {K(14)>80, Williams R(14)>-20, Stoch-RSI K>80, UO>70, SMI>40} — # of oscillators in OB."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sr_k, _ = _stoch_rsi_kd(close)
    uo = _ultimate_osc(high, low, close)
    sm = _smi(high, low, close)
    s = ((k > 80.0).astype(float).fillna(0)
         + (wr > -20.0).astype(float).fillna(0)
         + (sr_k > 80.0).astype(float).fillna(0)
         + (uo > 70.0).astype(float).fillna(0)
         + (sm > 40.0).astype(float).fillna(0))
    return s.where(k.notna(), np.nan)


def f26_stwf_132_multi_oscillator_exits_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct oscillators that had an OB-exit in past 21 bars — multi-osc bearish convergence."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sr_k, _ = _stoch_rsi_kd(close)
    uo = _ultimate_osc(high, low, close)
    sm = _smi(high, low, close)
    e1 = ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    e2 = ((wr.shift(1) > -20.0) & (wr <= -20.0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    e3 = ((sr_k.shift(1) > 80.0) & (sr_k <= 80.0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    e4 = ((uo.shift(1) > 70.0) & (uo <= 70.0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    e5 = ((sm.shift(1) > 40.0) & (sm <= 40.0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return (e1.astype(float) + e2.astype(float) + e3.astype(float) + e4.astype(float) + e5.astype(float)).where(
        k.notna(), np.nan)


def f26_stwf_133_stoch_climax_score_extreme_plus_duration(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(K(14) above 90 score: K-90 if K>90 else 0) × (current OB80 streak length) — climax intensity * duration."""
    k = _stoch_k(high, low, close, 14)
    excess = (k - 90.0).clip(lower=0).where(k.notna(), np.nan)
    streak = _streak_true(k > 80.0)
    return excess * streak


def f26_stwf_134_failure_after_252_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if price within 1% of 252d high AND %K(14) is at least 20 below its 21d max — momentum failing at price high."""
    k = _stoch_k(high, low, close, 14)
    near_max = high >= 0.99 * high.rolling(YDAYS, min_periods=QDAYS).max()
    k21max = k.rolling(MDAYS, min_periods=WDAYS).max()
    failing = (k21max - k) > 20.0
    return (near_max & failing).astype(float).where(k.notna(), np.nan)


def f26_stwf_135_stoch_persistence_above_q90_dist_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where %K above 252d-rolling 90th-percentile of itself — distribution-OB persistence."""
    k = _stoch_k(high, low, close, 14)
    q = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (k > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna() & q.notna(), np.nan)


def f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) has not been > 80 in the 63 bars following a prior OB exit — non-return signal (extended cool-off)."""
    k = _stoch_k(high, low, close, 14)
    in_ob = (k > 80.0)
    recent_ob = in_ob.rolling(QDAYS, min_periods=MDAYS).sum() == 0
    had_ob_before = in_ob.rolling(YDAYS, min_periods=QDAYS).sum() > 0
    return (recent_ob & had_ob_before).astype(float).where(k.notna(), np.nan)


def f26_stwf_137_stoch_in_ob_with_price_at_252_high_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) > 80 AND price = its 252d max — confluent peak-with-momentum-extreme state."""
    k = _stoch_k(high, low, close, 14)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((k > 80.0) & at_max).astype(float).where(k.notna(), np.nan)


def f26_stwf_138_stoch_topping_composite_count_at_top(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """When price at 252d-high: count of {K(14)>80, K(63)>80, K(252)>80, K-D bearish cross within 5 bars,
    21d K-max - K > 20}. Else NaN. Multi-signal topping at the price peak."""
    k1 = _stoch_k(high, low, close, 14)
    k2 = _stoch_k(high, low, close, QDAYS)
    k3 = _stoch_k(high, low, close, YDAYS)
    d1 = _stoch_d(k1, 3)
    diff = k1 - d1
    be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float).rolling(WDAYS, min_periods=1).sum() > 0
    fail = (k1.rolling(MDAYS, min_periods=WDAYS).max() - k1) > 20.0
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    score = ((k1 > 80.0).astype(float).fillna(0)
             + (k2 > 80.0).astype(float).fillna(0)
             + (k3 > 80.0).astype(float).fillna(0)
             + be.astype(float)
             + fail.astype(float))
    return score.where(at_max, np.nan)


# ============================================================
# Bucket Q — smoothing / regime / fast-vs-slow ratios (139-150)
# ============================================================

def f26_stwf_139_stoch_minus_ema_smoothing_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K(14) minus EMA(5) of itself — short-smoothing residual."""
    k = _stoch_k(high, low, close, 14)
    return k - k.ewm(span=5, adjust=False, min_periods=2).mean()


def f26_stwf_140_stoch_residual_zscore_vs_ema21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (K - EMA(21)(K)) over 63d — distribution-normalized smoothing residual."""
    k = _stoch_k(high, low, close, 14)
    res = k - k.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    return _rolling_zscore(res, QDAYS, min_periods=MDAYS)


def f26_stwf_141_stoch_regime_high_price_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BOTH close is above its 252d 90th-percentile AND K(14) > 80 — price/momentum regime confluence."""
    k = _stoch_k(high, low, close, 14)
    pq = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((close > pq) & (k > 80.0)).astype(float).where(k.notna() & pq.notna(), np.nan)


def f26_stwf_142_ob_regime_session_count_to_max_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: (current OB-session count in 252d) / (252d max of that count over its trailing 504d distribution)."""
    k = _stoch_k(high, low, close, 14)
    entered = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    sess = entered.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(sess, sess.rolling(DDAYS_2Y, min_periods=YDAYS).max())


def f26_stwf_143_ob_regime_intensity_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(cum OB area past 252) / (# of distinct OB sessions past 252) — average per-session intensity."""
    k = _stoch_k(high, low, close, 14)
    area = (k - 80.0).clip(lower=0).where(k.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    entered = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    sess = entered.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(area, sess)


def f26_stwf_144_fast_minus_slow_stoch_5_vs_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(5) - K(21) — fast-vs-slow stoch (weekly minus monthly)."""
    return _stoch_k(high, low, close, WDAYS) - _stoch_k(high, low, close, MDAYS)


def f26_stwf_145_med_minus_slow_stoch_14_vs_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) - K(63) — medium-vs-slow stoch (classical vs quarterly)."""
    return _stoch_k(high, low, close, 14) - _stoch_k(high, low, close, QDAYS)


def f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(63) - K(252) — quarterly minus annual stoch (regime gap)."""
    return _stoch_k(high, low, close, QDAYS) - _stoch_k(high, low, close, YDAYS)


def f26_stwf_147_connors_rsi_proxy_stoch_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Connors-RSI-style score using %K: (K + 100*streak_above_50/21 + 100*pct_rank_of_returns_5d) / 3.
    Composite momentum-extension index."""
    k = _stoch_k(high, low, close, 14)
    streak = _streak_true(k > 50.0).clip(upper=MDAYS) * (100.0 / MDAYS)
    ret = close.pct_change()
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return 100.0 * (v <= last).sum() / float(v.size) if v.size else np.nan
    pr = ret.rolling(MDAYS, min_periods=WDAYS).apply(_rk, raw=True)
    return (k.fillna(0) + streak.fillna(0) + pr.fillna(0)) / 3.0


def f26_stwf_148_stoch_dpo_overbought_proxy_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Detrended-stoch proxy: K(14) minus its right-anchored SMA(21) shifted by 11 bars — DPO-style filter
    (using historical shift only; no forward leak)."""
    k = _stoch_k(high, low, close, 14)
    sma21 = k.rolling(MDAYS, min_periods=WDAYS).mean()
    return k - sma21.shift(11)


def f26_stwf_149_stoch_rsi_kd_diff_252_zscore(close: pd.Series) -> pd.Series:
    """Z-score over 252d of (Stoch-RSI K - D) — distribution-normalized momentum-of-RSI cross magnitude."""
    k, d = _stoch_rsi_kd(close)
    return _rolling_zscore(k - d, YDAYS, min_periods=QDAYS)


def f26_stwf_150_stoch_topping_aggregate_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate topping score: (#osc in OB) × (OB80 streak / 21) — composite of breadth and persistence."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sr_k, _ = _stoch_rsi_kd(close)
    uo = _ultimate_osc(high, low, close)
    sm = _smi(high, low, close)
    breadth = ((k > 80.0).astype(float).fillna(0)
               + (wr > -20.0).astype(float).fillna(0)
               + (sr_k > 80.0).astype(float).fillna(0)
               + (uo > 70.0).astype(float).fillna(0)
               + (sm > 40.0).astype(float).fillna(0))
    streak = _streak_true(k > 80.0)
    return (breadth * streak / float(MDAYS)).where(k.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_BASE_REGISTRY_076_150 = {
    "f26_stwf_076_ult_osc_7_14_28": {"inputs": ["high", "low", "close"], "func": f26_stwf_076_ult_osc_7_14_28},
    "f26_stwf_077_ult_osc_above_70_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_077_ult_osc_above_70_state},
    "f26_stwf_078_ult_osc_just_exited_above_70": {"inputs": ["high", "low", "close"], "func": f26_stwf_078_ult_osc_just_exited_above_70},
    "f26_stwf_079_ult_osc_dwell_above_70_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_079_ult_osc_dwell_above_70_63},
    "f26_stwf_080_ult_osc_bars_since_topped_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_080_ult_osc_bars_since_topped_252},
    "f26_stwf_081_ult_osc_peak_decay_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_081_ult_osc_peak_decay_63},
    "f26_stwf_082_ult_osc_zscore_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_082_ult_osc_zscore_252},
    "f26_stwf_083_ult_osc_pct_rank_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_083_ult_osc_pct_rank_252},
    "f26_stwf_084_ult_osc_area_above_70_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_084_ult_osc_area_above_70_252},
    "f26_stwf_085_ult_osc_count_above_70_exits_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_085_ult_osc_count_above_70_exits_252},
    "f26_stwf_086_smi_25_13": {"inputs": ["high", "low", "close"], "func": f26_stwf_086_smi_25_13},
    "f26_stwf_087_smi_above_40_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_087_smi_above_40_state},
    "f26_stwf_088_smi_just_exited_above_40": {"inputs": ["high", "low", "close"], "func": f26_stwf_088_smi_just_exited_above_40},
    "f26_stwf_089_smi_dwell_above_40_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_089_smi_dwell_above_40_63},
    "f26_stwf_090_smi_bars_since_topped_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_090_smi_bars_since_topped_252},
    "f26_stwf_091_smi_peak_decay_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_091_smi_peak_decay_63},
    "f26_stwf_092_smi_zscore_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_092_smi_zscore_252},
    "f26_stwf_093_smi_signal_cross_down": {"inputs": ["high", "low", "close"], "func": f26_stwf_093_smi_signal_cross_down},
    "f26_stwf_094_kd_hook_at_top_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_094_kd_hook_at_top_indicator},
    "f26_stwf_095_bullish_then_bearish_cross_in_21d": {"inputs": ["high", "low", "close"], "func": f26_stwf_095_bullish_then_bearish_cross_in_21d},
    "f26_stwf_096_kd_compression_at_ob_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_096_kd_compression_at_ob_score},
    "f26_stwf_097_bearish_cross_at_or_above_90_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_097_bearish_cross_at_or_above_90_state},
    "f26_stwf_098_cross_density_in_ob_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_098_cross_density_in_ob_63},
    "f26_stwf_099_cross_failures_count_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_099_cross_failures_count_252},
    "f26_stwf_100_recurring_bearish_cross_pattern_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_100_recurring_bearish_cross_pattern_63},
    "f26_stwf_101_multi_horizon_kd_bearish_cross_count": {"inputs": ["high", "low", "close"], "func": f26_stwf_101_multi_horizon_kd_bearish_cross_count},
    "f26_stwf_102_stoch_range_high_minus_low_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_102_stoch_range_high_minus_low_63},
    "f26_stwf_103_stoch_vol_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_103_stoch_vol_21},
    "f26_stwf_104_stoch_vol_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_104_stoch_vol_63},
    "f26_stwf_105_stoch_vol_of_vol_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_105_stoch_vol_of_vol_21},
    "f26_stwf_106_stoch_distance_from_21d_mean": {"inputs": ["high", "low", "close"], "func": f26_stwf_106_stoch_distance_from_21d_mean},
    "f26_stwf_107_stoch_distance_from_63d_mean": {"inputs": ["high", "low", "close"], "func": f26_stwf_107_stoch_distance_from_63d_mean},
    "f26_stwf_108_stoch_distance_from_252d_mean": {"inputs": ["high", "low", "close"], "func": f26_stwf_108_stoch_distance_from_252d_mean},
    "f26_stwf_109_stoch_skew_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_109_stoch_skew_63},
    "f26_stwf_110_stoch_kurtosis_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_110_stoch_kurtosis_63},
    "f26_stwf_111_all_horizons_in_ob_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_111_all_horizons_in_ob_indicator},
    "f26_stwf_112_count_horizons_in_ob": {"inputs": ["high", "low", "close"], "func": f26_stwf_112_count_horizons_in_ob},
    "f26_stwf_113_short_leads_long_ob_exit_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_113_short_leads_long_ob_exit_21},
    "f26_stwf_114_monotonic_stoch_decline_across_horizons": {"inputs": ["high", "low", "close"], "func": f26_stwf_114_monotonic_stoch_decline_across_horizons},
    "f26_stwf_115_ribbon_avg_stoch_k": {"inputs": ["high", "low", "close"], "func": f26_stwf_115_ribbon_avg_stoch_k},
    "f26_stwf_116_ribbon_dispersion_stoch_k": {"inputs": ["high", "low", "close"], "func": f26_stwf_116_ribbon_dispersion_stoch_k},
    "f26_stwf_117_short_minus_long_horizon_k_diff": {"inputs": ["high", "low", "close"], "func": f26_stwf_117_short_minus_long_horizon_k_diff},
    "f26_stwf_118_short_ob_followed_by_long_ob_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_118_short_ob_followed_by_long_ob_63},
    "f26_stwf_119_long_horizon_ob_while_short_exits": {"inputs": ["high", "low", "close"], "func": f26_stwf_119_long_horizon_ob_while_short_exits},
    "f26_stwf_120_horizon_ob_ratio_short_to_long_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_120_horizon_ob_ratio_short_to_long_252},
    "f26_stwf_121_days_since_stoch_above_95": {"inputs": ["high", "low", "close"], "func": f26_stwf_121_days_since_stoch_above_95},
    "f26_stwf_122_days_since_stoch_below_20": {"inputs": ["high", "low", "close"], "func": f26_stwf_122_days_since_stoch_below_20},
    "f26_stwf_123_days_since_williams_r_above_minus10": {"inputs": ["high", "low", "close"], "func": f26_stwf_123_days_since_williams_r_above_minus10},
    "f26_stwf_124_days_since_stoch_rsi_at_252_max": {"inputs": ["close"], "func": f26_stwf_124_days_since_stoch_rsi_at_252_max},
    "f26_stwf_125_days_since_ult_osc_above_75": {"inputs": ["high", "low", "close"], "func": f26_stwf_125_days_since_ult_osc_above_75},
    "f26_stwf_126_days_since_smi_above_50": {"inputs": ["high", "low", "close"], "func": f26_stwf_126_days_since_smi_above_50},
    "f26_stwf_127_days_since_last_bearish_div_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_127_days_since_last_bearish_div_252},
    "f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit": {"inputs": ["high", "low", "close"], "func": f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit},
    "f26_stwf_129_stoch_dwell_above_q90_distribution_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_129_stoch_dwell_above_q90_distribution_63},
    "f26_stwf_130_consecutive_higher_oscillator_peaks_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_130_consecutive_higher_oscillator_peaks_63},
    "f26_stwf_131_multi_oscillator_blowoff_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_131_multi_oscillator_blowoff_score},
    "f26_stwf_132_multi_oscillator_exits_in_21d": {"inputs": ["high", "low", "close"], "func": f26_stwf_132_multi_oscillator_exits_in_21d},
    "f26_stwf_133_stoch_climax_score_extreme_plus_duration": {"inputs": ["high", "low", "close"], "func": f26_stwf_133_stoch_climax_score_extreme_plus_duration},
    "f26_stwf_134_failure_after_252_high_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_134_failure_after_252_high_indicator},
    "f26_stwf_135_stoch_persistence_above_q90_dist_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_135_stoch_persistence_above_q90_dist_252},
    "f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63},
    "f26_stwf_137_stoch_in_ob_with_price_at_252_high_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_137_stoch_in_ob_with_price_at_252_high_state},
    "f26_stwf_138_stoch_topping_composite_count_at_top": {"inputs": ["high", "low", "close"], "func": f26_stwf_138_stoch_topping_composite_count_at_top},
    "f26_stwf_139_stoch_minus_ema_smoothing_5": {"inputs": ["high", "low", "close"], "func": f26_stwf_139_stoch_minus_ema_smoothing_5},
    "f26_stwf_140_stoch_residual_zscore_vs_ema21": {"inputs": ["high", "low", "close"], "func": f26_stwf_140_stoch_residual_zscore_vs_ema21},
    "f26_stwf_141_stoch_regime_high_price_high_indicator": {"inputs": ["high", "low", "close"], "func": f26_stwf_141_stoch_regime_high_price_high_indicator},
    "f26_stwf_142_ob_regime_session_count_to_max_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_142_ob_regime_session_count_to_max_252},
    "f26_stwf_143_ob_regime_intensity_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_143_ob_regime_intensity_252},
    "f26_stwf_144_fast_minus_slow_stoch_5_vs_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_144_fast_minus_slow_stoch_5_vs_21},
    "f26_stwf_145_med_minus_slow_stoch_14_vs_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_145_med_minus_slow_stoch_14_vs_63},
    "f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252},
    "f26_stwf_147_connors_rsi_proxy_stoch_score": {"inputs": ["high", "low", "close"], "func": f26_stwf_147_connors_rsi_proxy_stoch_score},
    "f26_stwf_148_stoch_dpo_overbought_proxy_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_148_stoch_dpo_overbought_proxy_21},
    "f26_stwf_149_stoch_rsi_kd_diff_252_zscore": {"inputs": ["close"], "func": f26_stwf_149_stoch_rsi_kd_diff_252_zscore},
    "f26_stwf_150_stoch_topping_aggregate_score_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_150_stoch_topping_aggregate_score_252},
}


# === D3 wrappers + registry (076_150) ===
def f26_stwf_076_ult_osc_7_14_28_d3(high, low, close): return f26_stwf_076_ult_osc_7_14_28(high, low, close).diff().diff().diff()
def f26_stwf_077_ult_osc_above_70_state_d3(high, low, close): return f26_stwf_077_ult_osc_above_70_state(high, low, close).diff().diff().diff()
def f26_stwf_078_ult_osc_just_exited_above_70_d3(high, low, close): return f26_stwf_078_ult_osc_just_exited_above_70(high, low, close).diff().diff().diff()
def f26_stwf_079_ult_osc_dwell_above_70_63_d3(high, low, close): return f26_stwf_079_ult_osc_dwell_above_70_63(high, low, close).diff().diff().diff()
def f26_stwf_080_ult_osc_bars_since_topped_252_d3(high, low, close): return f26_stwf_080_ult_osc_bars_since_topped_252(high, low, close).diff().diff().diff()
def f26_stwf_081_ult_osc_peak_decay_63_d3(high, low, close): return f26_stwf_081_ult_osc_peak_decay_63(high, low, close).diff().diff().diff()
def f26_stwf_082_ult_osc_zscore_252_d3(high, low, close): return f26_stwf_082_ult_osc_zscore_252(high, low, close).diff().diff().diff()
def f26_stwf_083_ult_osc_pct_rank_252_d3(high, low, close): return f26_stwf_083_ult_osc_pct_rank_252(high, low, close).diff().diff().diff()
def f26_stwf_084_ult_osc_area_above_70_252_d3(high, low, close): return f26_stwf_084_ult_osc_area_above_70_252(high, low, close).diff().diff().diff()
def f26_stwf_085_ult_osc_count_above_70_exits_252_d3(high, low, close): return f26_stwf_085_ult_osc_count_above_70_exits_252(high, low, close).diff().diff().diff()
def f26_stwf_086_smi_25_13_d3(high, low, close): return f26_stwf_086_smi_25_13(high, low, close).diff().diff().diff()
def f26_stwf_087_smi_above_40_state_d3(high, low, close): return f26_stwf_087_smi_above_40_state(high, low, close).diff().diff().diff()
def f26_stwf_088_smi_just_exited_above_40_d3(high, low, close): return f26_stwf_088_smi_just_exited_above_40(high, low, close).diff().diff().diff()
def f26_stwf_089_smi_dwell_above_40_63_d3(high, low, close): return f26_stwf_089_smi_dwell_above_40_63(high, low, close).diff().diff().diff()
def f26_stwf_090_smi_bars_since_topped_252_d3(high, low, close): return f26_stwf_090_smi_bars_since_topped_252(high, low, close).diff().diff().diff()
def f26_stwf_091_smi_peak_decay_63_d3(high, low, close): return f26_stwf_091_smi_peak_decay_63(high, low, close).diff().diff().diff()
def f26_stwf_092_smi_zscore_252_d3(high, low, close): return f26_stwf_092_smi_zscore_252(high, low, close).diff().diff().diff()
def f26_stwf_093_smi_signal_cross_down_d3(high, low, close): return f26_stwf_093_smi_signal_cross_down(high, low, close).diff().diff().diff()
def f26_stwf_094_kd_hook_at_top_indicator_d3(high, low, close): return f26_stwf_094_kd_hook_at_top_indicator(high, low, close).diff().diff().diff()
def f26_stwf_095_bullish_then_bearish_cross_in_21d_d3(high, low, close): return f26_stwf_095_bullish_then_bearish_cross_in_21d(high, low, close).diff().diff().diff()
def f26_stwf_096_kd_compression_at_ob_score_d3(high, low, close): return f26_stwf_096_kd_compression_at_ob_score(high, low, close).diff().diff().diff()
def f26_stwf_097_bearish_cross_at_or_above_90_state_d3(high, low, close): return f26_stwf_097_bearish_cross_at_or_above_90_state(high, low, close).diff().diff().diff()
def f26_stwf_098_cross_density_in_ob_63_d3(high, low, close): return f26_stwf_098_cross_density_in_ob_63(high, low, close).diff().diff().diff()
def f26_stwf_099_cross_failures_count_252_d3(high, low, close): return f26_stwf_099_cross_failures_count_252(high, low, close).diff().diff().diff()
def f26_stwf_100_recurring_bearish_cross_pattern_63_d3(high, low, close): return f26_stwf_100_recurring_bearish_cross_pattern_63(high, low, close).diff().diff().diff()
def f26_stwf_101_multi_horizon_kd_bearish_cross_count_d3(high, low, close): return f26_stwf_101_multi_horizon_kd_bearish_cross_count(high, low, close).diff().diff().diff()
def f26_stwf_102_stoch_range_high_minus_low_63_d3(high, low, close): return f26_stwf_102_stoch_range_high_minus_low_63(high, low, close).diff().diff().diff()
def f26_stwf_103_stoch_vol_21_d3(high, low, close): return f26_stwf_103_stoch_vol_21(high, low, close).diff().diff().diff()
def f26_stwf_104_stoch_vol_63_d3(high, low, close): return f26_stwf_104_stoch_vol_63(high, low, close).diff().diff().diff()
def f26_stwf_105_stoch_vol_of_vol_21_d3(high, low, close): return f26_stwf_105_stoch_vol_of_vol_21(high, low, close).diff().diff().diff()
def f26_stwf_106_stoch_distance_from_21d_mean_d3(high, low, close): return f26_stwf_106_stoch_distance_from_21d_mean(high, low, close).diff().diff().diff()
def f26_stwf_107_stoch_distance_from_63d_mean_d3(high, low, close): return f26_stwf_107_stoch_distance_from_63d_mean(high, low, close).diff().diff().diff()
def f26_stwf_108_stoch_distance_from_252d_mean_d3(high, low, close): return f26_stwf_108_stoch_distance_from_252d_mean(high, low, close).diff().diff().diff()
def f26_stwf_109_stoch_skew_63_d3(high, low, close): return f26_stwf_109_stoch_skew_63(high, low, close).diff().diff().diff()
def f26_stwf_110_stoch_kurtosis_63_d3(high, low, close): return f26_stwf_110_stoch_kurtosis_63(high, low, close).diff().diff().diff()
def f26_stwf_111_all_horizons_in_ob_indicator_d3(high, low, close): return f26_stwf_111_all_horizons_in_ob_indicator(high, low, close).diff().diff().diff()
def f26_stwf_112_count_horizons_in_ob_d3(high, low, close): return f26_stwf_112_count_horizons_in_ob(high, low, close).diff().diff().diff()
def f26_stwf_113_short_leads_long_ob_exit_21_d3(high, low, close): return f26_stwf_113_short_leads_long_ob_exit_21(high, low, close).diff().diff().diff()
def f26_stwf_114_monotonic_stoch_decline_across_horizons_d3(high, low, close): return f26_stwf_114_monotonic_stoch_decline_across_horizons(high, low, close).diff().diff().diff()
def f26_stwf_115_ribbon_avg_stoch_k_d3(high, low, close): return f26_stwf_115_ribbon_avg_stoch_k(high, low, close).diff().diff().diff()
def f26_stwf_116_ribbon_dispersion_stoch_k_d3(high, low, close): return f26_stwf_116_ribbon_dispersion_stoch_k(high, low, close).diff().diff().diff()
def f26_stwf_117_short_minus_long_horizon_k_diff_d3(high, low, close): return f26_stwf_117_short_minus_long_horizon_k_diff(high, low, close).diff().diff().diff()
def f26_stwf_118_short_ob_followed_by_long_ob_63_d3(high, low, close): return f26_stwf_118_short_ob_followed_by_long_ob_63(high, low, close).diff().diff().diff()
def f26_stwf_119_long_horizon_ob_while_short_exits_d3(high, low, close): return f26_stwf_119_long_horizon_ob_while_short_exits(high, low, close).diff().diff().diff()
def f26_stwf_120_horizon_ob_ratio_short_to_long_252_d3(high, low, close): return f26_stwf_120_horizon_ob_ratio_short_to_long_252(high, low, close).diff().diff().diff()
def f26_stwf_121_days_since_stoch_above_95_d3(high, low, close): return f26_stwf_121_days_since_stoch_above_95(high, low, close).diff().diff().diff()
def f26_stwf_122_days_since_stoch_below_20_d3(high, low, close): return f26_stwf_122_days_since_stoch_below_20(high, low, close).diff().diff().diff()
def f26_stwf_123_days_since_williams_r_above_minus10_d3(high, low, close): return f26_stwf_123_days_since_williams_r_above_minus10(high, low, close).diff().diff().diff()
def f26_stwf_124_days_since_stoch_rsi_at_252_max_d3(close): return f26_stwf_124_days_since_stoch_rsi_at_252_max(close).diff().diff().diff()
def f26_stwf_125_days_since_ult_osc_above_75_d3(high, low, close): return f26_stwf_125_days_since_ult_osc_above_75(high, low, close).diff().diff().diff()
def f26_stwf_126_days_since_smi_above_50_d3(high, low, close): return f26_stwf_126_days_since_smi_above_50(high, low, close).diff().diff().diff()
def f26_stwf_127_days_since_last_bearish_div_252_d3(high, low, close): return f26_stwf_127_days_since_last_bearish_div_252(high, low, close).diff().diff().diff()
def f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit_d3(high, low, close): return f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit(high, low, close).diff().diff().diff()
def f26_stwf_129_stoch_dwell_above_q90_distribution_63_d3(high, low, close): return f26_stwf_129_stoch_dwell_above_q90_distribution_63(high, low, close).diff().diff().diff()
def f26_stwf_130_consecutive_higher_oscillator_peaks_63_d3(high, low, close): return f26_stwf_130_consecutive_higher_oscillator_peaks_63(high, low, close).diff().diff().diff()
def f26_stwf_131_multi_oscillator_blowoff_score_d3(high, low, close): return f26_stwf_131_multi_oscillator_blowoff_score(high, low, close).diff().diff().diff()
def f26_stwf_132_multi_oscillator_exits_in_21d_d3(high, low, close): return f26_stwf_132_multi_oscillator_exits_in_21d(high, low, close).diff().diff().diff()
def f26_stwf_133_stoch_climax_score_extreme_plus_duration_d3(high, low, close): return f26_stwf_133_stoch_climax_score_extreme_plus_duration(high, low, close).diff().diff().diff()
def f26_stwf_134_failure_after_252_high_indicator_d3(high, low, close): return f26_stwf_134_failure_after_252_high_indicator(high, low, close).diff().diff().diff()
def f26_stwf_135_stoch_persistence_above_q90_dist_252_d3(high, low, close): return f26_stwf_135_stoch_persistence_above_q90_dist_252(high, low, close).diff().diff().diff()
def f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63_d3(high, low, close): return f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63(high, low, close).diff().diff().diff()
def f26_stwf_137_stoch_in_ob_with_price_at_252_high_state_d3(high, low, close): return f26_stwf_137_stoch_in_ob_with_price_at_252_high_state(high, low, close).diff().diff().diff()
def f26_stwf_138_stoch_topping_composite_count_at_top_d3(high, low, close): return f26_stwf_138_stoch_topping_composite_count_at_top(high, low, close).diff().diff().diff()
def f26_stwf_139_stoch_minus_ema_smoothing_5_d3(high, low, close): return f26_stwf_139_stoch_minus_ema_smoothing_5(high, low, close).diff().diff().diff()
def f26_stwf_140_stoch_residual_zscore_vs_ema21_d3(high, low, close): return f26_stwf_140_stoch_residual_zscore_vs_ema21(high, low, close).diff().diff().diff()
def f26_stwf_141_stoch_regime_high_price_high_indicator_d3(high, low, close): return f26_stwf_141_stoch_regime_high_price_high_indicator(high, low, close).diff().diff().diff()
def f26_stwf_142_ob_regime_session_count_to_max_252_d3(high, low, close): return f26_stwf_142_ob_regime_session_count_to_max_252(high, low, close).diff().diff().diff()
def f26_stwf_143_ob_regime_intensity_252_d3(high, low, close): return f26_stwf_143_ob_regime_intensity_252(high, low, close).diff().diff().diff()
def f26_stwf_144_fast_minus_slow_stoch_5_vs_21_d3(high, low, close): return f26_stwf_144_fast_minus_slow_stoch_5_vs_21(high, low, close).diff().diff().diff()
def f26_stwf_145_med_minus_slow_stoch_14_vs_63_d3(high, low, close): return f26_stwf_145_med_minus_slow_stoch_14_vs_63(high, low, close).diff().diff().diff()
def f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252_d3(high, low, close): return f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252(high, low, close).diff().diff().diff()
def f26_stwf_147_connors_rsi_proxy_stoch_score_d3(high, low, close): return f26_stwf_147_connors_rsi_proxy_stoch_score(high, low, close).diff().diff().diff()
def f26_stwf_148_stoch_dpo_overbought_proxy_21_d3(high, low, close): return f26_stwf_148_stoch_dpo_overbought_proxy_21(high, low, close).diff().diff().diff()
def f26_stwf_149_stoch_rsi_kd_diff_252_zscore_d3(close): return f26_stwf_149_stoch_rsi_kd_diff_252_zscore(close).diff().diff().diff()
def f26_stwf_150_stoch_topping_aggregate_score_252_d3(high, low, close): return f26_stwf_150_stoch_topping_aggregate_score_252(high, low, close).diff().diff().diff()

STOCHASTIC_WILLIAMS_FAMILY_D3_REGISTRY_076_150 = {
    "f26_stwf_076_ult_osc_7_14_28_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_076_ult_osc_7_14_28_d3},
    "f26_stwf_077_ult_osc_above_70_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_077_ult_osc_above_70_state_d3},
    "f26_stwf_078_ult_osc_just_exited_above_70_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_078_ult_osc_just_exited_above_70_d3},
    "f26_stwf_079_ult_osc_dwell_above_70_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_079_ult_osc_dwell_above_70_63_d3},
    "f26_stwf_080_ult_osc_bars_since_topped_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_080_ult_osc_bars_since_topped_252_d3},
    "f26_stwf_081_ult_osc_peak_decay_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_081_ult_osc_peak_decay_63_d3},
    "f26_stwf_082_ult_osc_zscore_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_082_ult_osc_zscore_252_d3},
    "f26_stwf_083_ult_osc_pct_rank_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_083_ult_osc_pct_rank_252_d3},
    "f26_stwf_084_ult_osc_area_above_70_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_084_ult_osc_area_above_70_252_d3},
    "f26_stwf_085_ult_osc_count_above_70_exits_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_085_ult_osc_count_above_70_exits_252_d3},
    "f26_stwf_086_smi_25_13_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_086_smi_25_13_d3},
    "f26_stwf_087_smi_above_40_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_087_smi_above_40_state_d3},
    "f26_stwf_088_smi_just_exited_above_40_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_088_smi_just_exited_above_40_d3},
    "f26_stwf_089_smi_dwell_above_40_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_089_smi_dwell_above_40_63_d3},
    "f26_stwf_090_smi_bars_since_topped_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_090_smi_bars_since_topped_252_d3},
    "f26_stwf_091_smi_peak_decay_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_091_smi_peak_decay_63_d3},
    "f26_stwf_092_smi_zscore_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_092_smi_zscore_252_d3},
    "f26_stwf_093_smi_signal_cross_down_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_093_smi_signal_cross_down_d3},
    "f26_stwf_094_kd_hook_at_top_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_094_kd_hook_at_top_indicator_d3},
    "f26_stwf_095_bullish_then_bearish_cross_in_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_095_bullish_then_bearish_cross_in_21d_d3},
    "f26_stwf_096_kd_compression_at_ob_score_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_096_kd_compression_at_ob_score_d3},
    "f26_stwf_097_bearish_cross_at_or_above_90_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_097_bearish_cross_at_or_above_90_state_d3},
    "f26_stwf_098_cross_density_in_ob_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_098_cross_density_in_ob_63_d3},
    "f26_stwf_099_cross_failures_count_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_099_cross_failures_count_252_d3},
    "f26_stwf_100_recurring_bearish_cross_pattern_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_100_recurring_bearish_cross_pattern_63_d3},
    "f26_stwf_101_multi_horizon_kd_bearish_cross_count_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_101_multi_horizon_kd_bearish_cross_count_d3},
    "f26_stwf_102_stoch_range_high_minus_low_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_102_stoch_range_high_minus_low_63_d3},
    "f26_stwf_103_stoch_vol_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_103_stoch_vol_21_d3},
    "f26_stwf_104_stoch_vol_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_104_stoch_vol_63_d3},
    "f26_stwf_105_stoch_vol_of_vol_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_105_stoch_vol_of_vol_21_d3},
    "f26_stwf_106_stoch_distance_from_21d_mean_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_106_stoch_distance_from_21d_mean_d3},
    "f26_stwf_107_stoch_distance_from_63d_mean_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_107_stoch_distance_from_63d_mean_d3},
    "f26_stwf_108_stoch_distance_from_252d_mean_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_108_stoch_distance_from_252d_mean_d3},
    "f26_stwf_109_stoch_skew_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_109_stoch_skew_63_d3},
    "f26_stwf_110_stoch_kurtosis_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_110_stoch_kurtosis_63_d3},
    "f26_stwf_111_all_horizons_in_ob_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_111_all_horizons_in_ob_indicator_d3},
    "f26_stwf_112_count_horizons_in_ob_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_112_count_horizons_in_ob_d3},
    "f26_stwf_113_short_leads_long_ob_exit_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_113_short_leads_long_ob_exit_21_d3},
    "f26_stwf_114_monotonic_stoch_decline_across_horizons_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_114_monotonic_stoch_decline_across_horizons_d3},
    "f26_stwf_115_ribbon_avg_stoch_k_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_115_ribbon_avg_stoch_k_d3},
    "f26_stwf_116_ribbon_dispersion_stoch_k_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_116_ribbon_dispersion_stoch_k_d3},
    "f26_stwf_117_short_minus_long_horizon_k_diff_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_117_short_minus_long_horizon_k_diff_d3},
    "f26_stwf_118_short_ob_followed_by_long_ob_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_118_short_ob_followed_by_long_ob_63_d3},
    "f26_stwf_119_long_horizon_ob_while_short_exits_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_119_long_horizon_ob_while_short_exits_d3},
    "f26_stwf_120_horizon_ob_ratio_short_to_long_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_120_horizon_ob_ratio_short_to_long_252_d3},
    "f26_stwf_121_days_since_stoch_above_95_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_121_days_since_stoch_above_95_d3},
    "f26_stwf_122_days_since_stoch_below_20_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_122_days_since_stoch_below_20_d3},
    "f26_stwf_123_days_since_williams_r_above_minus10_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_123_days_since_williams_r_above_minus10_d3},
    "f26_stwf_124_days_since_stoch_rsi_at_252_max_d3": {"inputs": ["close"], "func": f26_stwf_124_days_since_stoch_rsi_at_252_max_d3},
    "f26_stwf_125_days_since_ult_osc_above_75_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_125_days_since_ult_osc_above_75_d3},
    "f26_stwf_126_days_since_smi_above_50_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_126_days_since_smi_above_50_d3},
    "f26_stwf_127_days_since_last_bearish_div_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_127_days_since_last_bearish_div_252_d3},
    "f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_128_stoch_ob_re_entry_within_21d_post_exit_d3},
    "f26_stwf_129_stoch_dwell_above_q90_distribution_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_129_stoch_dwell_above_q90_distribution_63_d3},
    "f26_stwf_130_consecutive_higher_oscillator_peaks_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_130_consecutive_higher_oscillator_peaks_63_d3},
    "f26_stwf_131_multi_oscillator_blowoff_score_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_131_multi_oscillator_blowoff_score_d3},
    "f26_stwf_132_multi_oscillator_exits_in_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_132_multi_oscillator_exits_in_21d_d3},
    "f26_stwf_133_stoch_climax_score_extreme_plus_duration_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_133_stoch_climax_score_extreme_plus_duration_d3},
    "f26_stwf_134_failure_after_252_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_134_failure_after_252_high_indicator_d3},
    "f26_stwf_135_stoch_persistence_above_q90_dist_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_135_stoch_persistence_above_q90_dist_252_d3},
    "f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_136_stoch_failed_to_re_enter_ob_after_exit_63_d3},
    "f26_stwf_137_stoch_in_ob_with_price_at_252_high_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_137_stoch_in_ob_with_price_at_252_high_state_d3},
    "f26_stwf_138_stoch_topping_composite_count_at_top_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_138_stoch_topping_composite_count_at_top_d3},
    "f26_stwf_139_stoch_minus_ema_smoothing_5_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_139_stoch_minus_ema_smoothing_5_d3},
    "f26_stwf_140_stoch_residual_zscore_vs_ema21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_140_stoch_residual_zscore_vs_ema21_d3},
    "f26_stwf_141_stoch_regime_high_price_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_141_stoch_regime_high_price_high_indicator_d3},
    "f26_stwf_142_ob_regime_session_count_to_max_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_142_ob_regime_session_count_to_max_252_d3},
    "f26_stwf_143_ob_regime_intensity_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_143_ob_regime_intensity_252_d3},
    "f26_stwf_144_fast_minus_slow_stoch_5_vs_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_144_fast_minus_slow_stoch_5_vs_21_d3},
    "f26_stwf_145_med_minus_slow_stoch_14_vs_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_145_med_minus_slow_stoch_14_vs_63_d3},
    "f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_146_quarterly_minus_annual_stoch_63_vs_252_d3},
    "f26_stwf_147_connors_rsi_proxy_stoch_score_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_147_connors_rsi_proxy_stoch_score_d3},
    "f26_stwf_148_stoch_dpo_overbought_proxy_21_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_148_stoch_dpo_overbought_proxy_21_d3},
    "f26_stwf_149_stoch_rsi_kd_diff_252_zscore_d3": {"inputs": ["close"], "func": f26_stwf_149_stoch_rsi_kd_diff_252_zscore_d3},
    "f26_stwf_150_stoch_topping_aggregate_score_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_150_stoch_topping_aggregate_score_252_d3},
}
