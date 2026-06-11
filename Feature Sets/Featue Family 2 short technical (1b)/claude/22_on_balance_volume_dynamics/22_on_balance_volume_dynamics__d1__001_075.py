"""on_balance_volume_dynamics d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the OBV-and-related cumulative-signed-volume
theme: slope / divergence / regime / decay / momentum / structural events.

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
    """Classic OBV: cumulative sum of signed volume where sign = sign(close.diff())."""
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _obv_oo(close: pd.Series, open_: pd.Series, volume: pd.Series) -> pd.Series:
    """CSV-OO variant: cumulative volume signed by sign(close - open)."""
    sgn = np.sign(close - open_).fillna(0.0)
    return (sgn * volume).cumsum()


def _nvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative Volume Index: only updates on bars with vol < prior vol; otherwise carries forward."""
    r = close.pct_change().fillna(0.0)
    dv = volume.diff()
    contrib = np.where(dv < 0, r, 0.0)
    return pd.Series(contrib, index=close.index).cumsum()


def _pvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Positive Volume Index: only updates on bars with vol > prior vol; otherwise carries forward."""
    r = close.pct_change().fillna(0.0)
    dv = volume.diff()
    contrib = np.where(dv > 0, r, 0.0)
    return pd.Series(contrib, index=close.index).cumsum()


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


def _rolling_argmax_age(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _a(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return s.rolling(window, min_periods=min_periods).apply(_a, raw=True)


def _np_autocorr_lag(w, lag):
    v = w[~np.isnan(w)]
    if v.size < lag + 3:
        return np.nan
    a = v[:-lag] - v[:-lag].mean()
    b = v[lag:] - v[lag:].mean()
    den = np.sqrt((a * a).sum() * (b * b).sum())
    if den <= 0:
        return np.nan
    return float((a * b).sum() / den)


def _rolling_hurst(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 20)
    def _h(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < min_periods:
            return np.nan
        lags = [2, 4, 8, 16, 32]
        lags = [l for l in lags if l < n // 2]
        if len(lags) < 2:
            return np.nan
        tau = []
        for lag in lags:
            d = v[lag:] - v[:-lag]
            sd = d.std()
            if sd <= 0 or not np.isfinite(sd):
                return np.nan
            tau.append(sd)
        try:
            return float(np.polyfit(np.log(lags), np.log(tau), 1)[0])
        except Exception:
            return np.nan
    return s.rolling(window, min_periods=min_periods).apply(_h, raw=True)


# ============================================================
# Bucket A — OBV slope at multiple horizons (001-005)
# ============================================================

def f22_obvd_001_obv_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of OBV over trailing 21d — monthly accumulation/distribution rate."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, MDAYS)


def f22_obvd_002_obv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of OBV over trailing 63d — quarterly accumulation trend."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, QDAYS)


def f22_obvd_003_obv_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of OBV over trailing 252d — annual flow trend."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, YDAYS)


def f22_obvd_004_obv_slope_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of OBV over trailing 504d — biennial structural flow."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, DDAYS_2Y)


def f22_obvd_005_obv_slope_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of OBV over trailing 5d — weekly micro-flow."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, WDAYS)


# ============================================================
# Bucket B — OBV slope vs price slope (divergence intensity) (006-012)
# ============================================================

def f22_obvd_006_obv_minus_price_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(63d) minus log-price slope(63d) — slope divergence (negative = OBV lagging price)."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, QDAYS) - _rolling_slope(_safe_log(close), QDAYS)


def f22_obvd_007_obv_minus_price_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(252d) minus log-price slope(252d) — annual slope divergence."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


def f22_obvd_008_obv_minus_price_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(21d) minus log-price slope(21d) — monthly slope divergence."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, MDAYS) - _rolling_slope(_safe_log(close), MDAYS)


def f22_obvd_009_obv_vs_price_slope_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope / log-price slope over 63d — ratio < 1 = OBV lagging price ascent."""
    obv = _obv(close, volume)
    return _safe_div(_rolling_slope(obv, QDAYS), _rolling_slope(_safe_log(close), QDAYS))


def f22_obvd_010_obv_slope_sign_mismatch_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when sign(OBV slope, 252d) != sign(log-price slope, 252d), else 0 — divergence event."""
    obv = _obv(close, volume)
    so = _rolling_slope(obv, YDAYS)
    sp = _rolling_slope(_safe_log(close), YDAYS)
    return (np.sign(so) != np.sign(sp)).astype(float)


def f22_obvd_011_obv_slope_sign_mismatch_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where sign(OBV slope 21d) != sign(log-price slope 21d)."""
    obv = _obv(close, volume)
    so = _rolling_slope(obv, MDAYS)
    sp = _rolling_slope(_safe_log(close), MDAYS)
    return (np.sign(so) != np.sign(sp)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_012_obv_slope_decline_while_price_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV slope(63d) < 0 AND log-price slope(63d) > 0 — classical bearish divergence flag."""
    obv = _obv(close, volume)
    so = _rolling_slope(obv, QDAYS)
    sp = _rolling_slope(_safe_log(close), QDAYS)
    return ((so < 0) & (sp > 0)).astype(float)


# ============================================================
# Bucket C — OBV z-score vs trailing distribution (013-018)
# ============================================================

def f22_obvd_013_obv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV over trailing 252d — annual flow-level extreme."""
    return _rolling_zscore(_obv(close, volume), YDAYS)


def f22_obvd_014_obv_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV over trailing 63d — quarterly flow-level extreme."""
    return _rolling_zscore(_obv(close, volume), QDAYS)


def f22_obvd_015_obv_zscore_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV over trailing 504d — biennial flow extreme."""
    return _rolling_zscore(_obv(close, volume), DDAYS_2Y)


def f22_obvd_016_obv_robust_z_mad_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of OBV over trailing 252d."""
    obv = _obv(close, volume)
    med = obv.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (obv - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(obv - med, 1.4826 * mad)


def f22_obvd_017_obv_zscore_diff_63_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV z(63d) minus z(252d) — short-vs-long rank-extreme contrast."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv, QDAYS) - _rolling_zscore(obv, YDAYS)


def f22_obvd_018_obv_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current OBV within trailing 252d distribution."""
    return _rolling_pct_rank(_obv(close, volume), YDAYS)


# ============================================================
# Bucket D — OBV vs its own MA (019-024)
# ============================================================

def f22_obvd_019_obv_minus_sma21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 21d SMA — short-term flow regime above/below."""
    obv = _obv(close, volume)
    return obv - obv.rolling(MDAYS, min_periods=WDAYS).mean()


def f22_obvd_020_obv_minus_sma63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 63d SMA — quarterly flow regime."""
    obv = _obv(close, volume)
    return obv - obv.rolling(QDAYS, min_periods=MDAYS).mean()


def f22_obvd_021_obv_minus_sma252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 252d SMA — annual flow regime."""
    obv = _obv(close, volume)
    return obv - obv.rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_022_obv_ema_distance_atr_normalized_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - EMA21(OBV)) / (volume.rolling(21).mean()) — flow distance from MA, normalized by volume baseline."""
    obv = _obv(close, volume)
    ema = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    base = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(obv - ema, base)


def f22_obvd_023_obv_ema21_minus_ema63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA21(OBV) minus EMA63(OBV) — MACD-style fast-vs-slow OBV momentum."""
    obv = _obv(close, volume)
    return obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() - obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f22_obvd_024_obv_ema9_minus_ema21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA9(OBV) minus EMA21(OBV) — very-short fast-vs-slow OBV momentum."""
    obv = _obv(close, volume)
    return obv.ewm(span=9, min_periods=3, adjust=False).mean() - obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()


# ============================================================
# Bucket E — OBV high-water-mark dynamics (025-031)
# ============================================================

def f22_obvd_025_obv_minus_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus 252d trailing max OBV — always <= 0; flow drawdown from peak."""
    obv = _obv(close, volume)
    return obv - obv.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_026_obv_minus_max_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus 504d trailing max OBV — biennial flow drawdown."""
    obv = _obv(close, volume)
    return obv - obv.rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f22_obvd_027_obv_max_age_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 252d trailing OBV max — staleness of last flow peak."""
    return _rolling_argmax_age(_obv(close, volume), YDAYS)


def f22_obvd_028_obv_max_age_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 504d trailing OBV max."""
    return _rolling_argmax_age(_obv(close, volume), DDAYS_2Y)


def f22_obvd_029_obv_recovery_failure_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if OBV has not exceeded 90% of its 252d trailing peak after dropping below it, else 0."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return ((obv < 0.9 * rmax) & (rmax > 0)).astype(float)


def f22_obvd_030_obv_drawdown_from_max_norm_by_std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 252d-max-OBV) / 252d-std-OBV — std-normalized flow drawdown."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    sd = obv.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(obv - rmax, sd)


def f22_obvd_031_obv_new_high_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV equals 252d trailing max (new flow highs)."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return (obv >= rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — OBV vs price new-high count (032-037)
# ============================================================

def f22_obvd_032_obv_new_high_minus_price_new_high_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of OBV new-252d-highs minus count of price new-252d-highs over trailing 252d. Negative = OBV lagging price."""
    obv = _obv(close, volume)
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    on = (obv >= omax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    pn = (high >= pmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return on - pn


def f22_obvd_033_price_new_high_no_obv_new_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when current bar is a price 63d new-high AND OBV is NOT at its 63d new-high — bearish divergence event."""
    obv = _obv(close, volume)
    omax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    pmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return ((high >= pmax) & (obv < omax)).astype(float)


def f22_obvd_034_price_new_high_no_obv_new_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where price prints a new 63d high but OBV does not."""
    obv = _obv(close, volume)
    omax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    pmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    flag = ((high >= pmax) & (obv < omax)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_035_obv_peak_age_minus_price_peak_age_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV peak age(252d) minus price peak age(252d) — positive = OBV peak older than price peak (divergence)."""
    obv = _obv(close, volume)
    return _rolling_argmax_age(obv, YDAYS) - _rolling_argmax_age(high, YDAYS)


def f22_obvd_036_obv_at_price_new_252d_high_zscore(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV z-score (252d) at bars when high prints new 252d max — flow strength at price peaks."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv, YDAYS)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return z.where(high >= pmax, np.nan)


def f22_obvd_037_obv_max_minus_price_max_count_252d_consec(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak with (OBV not at 252d max) AND (price at 252d max) — divergence persistence."""
    obv = _obv(close, volume)
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (high >= pmax) & (obv < omax)
    return _consecutive_true_streak(cond).astype(float)


# ============================================================
# Bucket G — OBV momentum / ROC (038-042)
# ============================================================

def f22_obvd_038_obv_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV ROC over 21d: OBV(t) - OBV(t-21)."""
    obv = _obv(close, volume)
    return obv - obv.shift(MDAYS)


def f22_obvd_039_obv_roc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV ROC over 63d."""
    obv = _obv(close, volume)
    return obv - obv.shift(QDAYS)


def f22_obvd_040_obv_roc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV ROC over 252d."""
    obv = _obv(close, volume)
    return obv - obv.shift(YDAYS)


def f22_obvd_041_obv_roc_21d_norm_by_vol_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV(t) - OBV(t-21)) / mean_volume(21d) — normalized per-bar flow rate."""
    obv = _obv(close, volume)
    base = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(obv - obv.shift(MDAYS), base * MDAYS)


def f22_obvd_042_obv_roc_acceleration_21_minus_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV ROC(21d/21) minus OBV ROC(63d/63) — flow acceleration vs decelerating baseline."""
    obv = _obv(close, volume)
    return (obv - obv.shift(MDAYS)) / float(MDAYS) - (obv - obv.shift(QDAYS)) / float(QDAYS)


# ============================================================
# Bucket H — OBV decay post peak / half-life (043-048)
# ============================================================

def f22_obvd_043_obv_decay_ratio_since_252d_peak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV / 252d-trailing-max OBV — when max > 0, fraction-of-peak."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(obv, rmax)


def f22_obvd_044_obv_decay_post_peak_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of OBV, masked to bars within 21 days of a 252d-OBV-peak event."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = obv >= rmax
    age = (~is_peak).astype(int).groupby(is_peak.cumsum()).cumsum()
    slope = _rolling_slope(obv, MDAYS)
    return slope.where(age <= MDAYS, np.nan)


def f22_obvd_045_obv_post_peak_half_life_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from 63d-trailing OBV peak to first bar with OBV <= 0.5*peak; window 63d."""
    obv = _obv(close, volume)
    def _hl(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak):
            return np.nan
        thresh = peak / 2.0 if peak > 0 else peak * 1.5
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= thresh:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return obv.rolling(QDAYS, min_periods=MDAYS).apply(_hl, raw=True)


def f22_obvd_046_obv_cumulative_post_peak_deficit_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 252d window of (peak_OBV - current_OBV) since peak — cumulative flow deficit."""
    obv = _obv(close, volume)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak):
            return np.nan
        seg = w[peak_idx + 1 :]
        seg = seg[~np.isnan(seg)]
        if seg.size == 0:
            return 0.0
        return float(np.sum(peak - seg))
    return obv.rolling(YDAYS, min_periods=QDAYS).apply(_cd, raw=True)


def f22_obvd_047_obv_recovery_indicator_to_peak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV has recovered to within 5% of 252d trailing peak, else 0."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(obv, rmax) >= 0.95).astype(float)


def f22_obvd_048_obv_consecutive_below_max_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak with OBV < 252d trailing max — persistence of post-peak deficit."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return _consecutive_true_streak(obv < rmax).astype(float)


# ============================================================
# Bucket I — OBV regime persistence (Hurst etc.) (049-052)
# ============================================================

def f22_obvd_049_hurst_obv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent on OBV-returns over 252d — flow persistence vs mean-reversion."""
    obv = _obv(close, volume)
    return _rolling_hurst(obv.diff(), YDAYS)


def f22_obvd_050_hurst_obv_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent on OBV-returns over 504d."""
    obv = _obv(close, volume)
    return _rolling_hurst(obv.diff(), DDAYS_2Y)


def f22_obvd_051_obv_autocorr_lag1_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of OBV-returns over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 1), raw=True)


def f22_obvd_052_obv_autocorr_lag5_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of OBV-returns over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _np_autocorr_lag(w, 5), raw=True)


# ============================================================
# Bucket J — OBV-price divergence detector explicit (053-058)
# ============================================================

def f22_obvd_053_obv_corr_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation of OBV and close over trailing 252d. Low = divergence."""
    obv = _obv(close, volume)
    return obv.rolling(YDAYS, min_periods=QDAYS).corr(close)


def f22_obvd_054_obv_corr_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation of OBV and close over trailing 63d."""
    obv = _obv(close, volume)
    return obv.rolling(QDAYS, min_periods=MDAYS).corr(close)


def f22_obvd_055_obv_rank_corr_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation of OBV and close over trailing 252d."""
    obv = _obv(close, volume)
    ro = obv.rolling(YDAYS, min_periods=QDAYS).rank()
    rc = close.rolling(YDAYS, min_periods=QDAYS).rank()
    return ro.rolling(YDAYS, min_periods=QDAYS).corr(rc)


def f22_obvd_056_bearish_divergence_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """For each bar: (price 21d-high - OBV 21d-rank-relative) — positive when price ahead of OBV in rank."""
    obv = _obv(close, volume)
    pr_p = _rolling_pct_rank(high, MDAYS)
    pr_o = _rolling_pct_rank(obv, MDAYS)
    return pr_p - pr_o


def f22_obvd_057_obv_failure_to_new_high_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where price prints new 252d high but OBV is below its own 63d trailing max."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    flag = ((high >= pmax) & (obv < omax63)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_058_obv_underperformance_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank(63d) minus close pct rank(63d) — negative = OBV underperforming price."""
    obv = _obv(close, volume)
    return _rolling_pct_rank(obv, QDAYS) - _rolling_pct_rank(close, QDAYS)


# ============================================================
# Bucket K — OBV-MA crossover events (059-064)
# ============================================================

def f22_obvd_059_obv_above_sma21_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV > 21d-SMA(OBV), else 0 — short-term regime indicator."""
    obv = _obv(close, volume)
    return (obv > obv.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float)


def f22_obvd_060_obv_above_sma63_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV > 63d-SMA(OBV), else 0 — quarterly regime."""
    obv = _obv(close, volume)
    return (obv > obv.rolling(QDAYS, min_periods=MDAYS).mean()).astype(float)


def f22_obvd_061_obv_cross_sma21_down_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV crosses BELOW its 21d-SMA (was above, now below), else 0."""
    obv = _obv(close, volume)
    sma = obv.rolling(MDAYS, min_periods=WDAYS).mean()
    cur_above = obv > sma
    prev_above = cur_above.shift(1)
    return (prev_above & ~cur_above).astype(float)


def f22_obvd_062_obv_cross_sma63_down_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV crosses BELOW its 63d-SMA, else 0."""
    obv = _obv(close, volume)
    sma = obv.rolling(QDAYS, min_periods=MDAYS).mean()
    cur_above = obv > sma
    prev_above = cur_above.shift(1)
    return (prev_above & ~cur_above).astype(float)


def f22_obvd_063_obv_cross_sma21_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of OBV/21d-SMA crossover events (either direction) in trailing 252d."""
    obv = _obv(close, volume)
    sma = obv.rolling(MDAYS, min_periods=WDAYS).mean()
    cross = (np.sign(obv - sma).diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_064_obv_below_sma21_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d that OBV was below its 21d-SMA."""
    obv = _obv(close, volume)
    sma = obv.rolling(MDAYS, min_periods=WDAYS).mean()
    return (obv < sma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket L — OBV volatility / R² / cleanliness (065-069)
# ============================================================

def f22_obvd_065_obv_std_diff_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling std of OBV-diff (= signed volume) over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).std()


def f22_obvd_066_obv_r2_trend_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R² of linear regression of OBV over 252d — trend cleanliness."""
    obv = _obv(close, volume)
    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean(); ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((v - ym) ** 2).sum()
        sxy = ((x - xm) * (v - ym)).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        r = sxy / np.sqrt(sxx * syy)
        return float(r * r)
    return obv.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)


def f22_obvd_067_obv_atr_normalized_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(63d) divided by ATR21 — normalize flow rate by volatility scale."""
    obv = _obv(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(_rolling_slope(obv, QDAYS), atr)


def f22_obvd_068_obv_volatility_to_signal_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std(OBV-diff, 252d) / |slope(OBV, 252d)| — noise-to-signal ratio for flow trend."""
    obv = _obv(close, volume)
    sig = _rolling_slope(obv, YDAYS).abs()
    noise = obv.diff().rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(noise, sig)


def f22_obvd_069_obv_skew_diff_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of OBV-diff (signed-volume) over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket M — Sign-run / down-day streak (070-075)
# ============================================================

def f22_obvd_070_obv_sign_run_length_current(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar run length of same-sign OBV change."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    same = sgn == sgn.shift(1)
    grp = (~same.fillna(False)).cumsum()
    return same.fillna(False).astype(int).groupby(grp).cumsum().astype(float) + 1.0


def f22_obvd_071_obv_negative_runs_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distinct negative-sign OBV runs in trailing 252d."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    starts = ((sgn == -1) & (sgn.shift(1) != -1)).astype(float)
    return starts.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_072_obv_max_negative_run_length_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar negative-OBV-change run length in trailing 252d."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    streak = _consecutive_true_streak(sgn == -1).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_073_obv_down_volume_weighted_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on consecutive OBV-negative bars in current streak — magnitude-weighted streak."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    cond = sgn == -1
    streak_grp = (~cond.fillna(False)).cumsum()
    return volume.where(cond.fillna(False), 0.0).groupby(streak_grp).cumsum()


def f22_obvd_074_obv_positive_to_negative_run_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of positive-OBV-change run lengths / sum of negative run lengths in trailing 252d."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    pos = (sgn == 1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = (sgn == -1).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pos, neg + 1.0)


def f22_obvd_075_obv_consecutive_below_zero_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak of OBV-diff < 0 (current streak)."""
    obv = _obv(close, volume)
    return _consecutive_true_streak(obv.diff() < 0).astype(float)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f22_obvd_001_obv_slope_21d_d1(close, volume):
    return f22_obvd_001_obv_slope_21d(close, volume).diff()


def f22_obvd_002_obv_slope_63d_d1(close, volume):
    return f22_obvd_002_obv_slope_63d(close, volume).diff()


def f22_obvd_003_obv_slope_252d_d1(close, volume):
    return f22_obvd_003_obv_slope_252d(close, volume).diff()


def f22_obvd_004_obv_slope_504d_d1(close, volume):
    return f22_obvd_004_obv_slope_504d(close, volume).diff()


def f22_obvd_005_obv_slope_5d_d1(close, volume):
    return f22_obvd_005_obv_slope_5d(close, volume).diff()


def f22_obvd_006_obv_minus_price_slope_63d_d1(close, volume):
    return f22_obvd_006_obv_minus_price_slope_63d(close, volume).diff()


def f22_obvd_007_obv_minus_price_slope_252d_d1(close, volume):
    return f22_obvd_007_obv_minus_price_slope_252d(close, volume).diff()


def f22_obvd_008_obv_minus_price_slope_21d_d1(close, volume):
    return f22_obvd_008_obv_minus_price_slope_21d(close, volume).diff()


def f22_obvd_009_obv_vs_price_slope_ratio_63d_d1(close, volume):
    return f22_obvd_009_obv_vs_price_slope_ratio_63d(close, volume).diff()


def f22_obvd_010_obv_slope_sign_mismatch_252d_d1(close, volume):
    return f22_obvd_010_obv_slope_sign_mismatch_252d(close, volume).diff()


def f22_obvd_011_obv_slope_sign_mismatch_count_252d_d1(close, volume):
    return f22_obvd_011_obv_slope_sign_mismatch_count_252d(close, volume).diff()


def f22_obvd_012_obv_slope_decline_while_price_up_252d_d1(close, volume):
    return f22_obvd_012_obv_slope_decline_while_price_up_252d(close, volume).diff()


def f22_obvd_013_obv_zscore_252d_d1(close, volume):
    return f22_obvd_013_obv_zscore_252d(close, volume).diff()


def f22_obvd_014_obv_zscore_63d_d1(close, volume):
    return f22_obvd_014_obv_zscore_63d(close, volume).diff()


def f22_obvd_015_obv_zscore_504d_d1(close, volume):
    return f22_obvd_015_obv_zscore_504d(close, volume).diff()


def f22_obvd_016_obv_robust_z_mad_252d_d1(close, volume):
    return f22_obvd_016_obv_robust_z_mad_252d(close, volume).diff()


def f22_obvd_017_obv_zscore_diff_63_minus_252_d1(close, volume):
    return f22_obvd_017_obv_zscore_diff_63_minus_252(close, volume).diff()


def f22_obvd_018_obv_pct_rank_252d_d1(close, volume):
    return f22_obvd_018_obv_pct_rank_252d(close, volume).diff()


def f22_obvd_019_obv_minus_sma21_d1(close, volume):
    return f22_obvd_019_obv_minus_sma21(close, volume).diff()


def f22_obvd_020_obv_minus_sma63_d1(close, volume):
    return f22_obvd_020_obv_minus_sma63(close, volume).diff()


def f22_obvd_021_obv_minus_sma252_d1(close, volume):
    return f22_obvd_021_obv_minus_sma252(close, volume).diff()


def f22_obvd_022_obv_ema_distance_atr_normalized_21d_d1(high, low, close, volume):
    return f22_obvd_022_obv_ema_distance_atr_normalized_21d(high, low, close, volume).diff()


def f22_obvd_023_obv_ema21_minus_ema63_d1(close, volume):
    return f22_obvd_023_obv_ema21_minus_ema63(close, volume).diff()


def f22_obvd_024_obv_ema9_minus_ema21_d1(close, volume):
    return f22_obvd_024_obv_ema9_minus_ema21(close, volume).diff()


def f22_obvd_025_obv_minus_max_252d_d1(close, volume):
    return f22_obvd_025_obv_minus_max_252d(close, volume).diff()


def f22_obvd_026_obv_minus_max_504d_d1(close, volume):
    return f22_obvd_026_obv_minus_max_504d(close, volume).diff()


def f22_obvd_027_obv_max_age_252d_d1(close, volume):
    return f22_obvd_027_obv_max_age_252d(close, volume).diff()


def f22_obvd_028_obv_max_age_504d_d1(close, volume):
    return f22_obvd_028_obv_max_age_504d(close, volume).diff()


def f22_obvd_029_obv_recovery_failure_252d_d1(close, volume):
    return f22_obvd_029_obv_recovery_failure_252d(close, volume).diff()


def f22_obvd_030_obv_drawdown_from_max_norm_by_std_252d_d1(close, volume):
    return f22_obvd_030_obv_drawdown_from_max_norm_by_std_252d(close, volume).diff()


def f22_obvd_031_obv_new_high_count_252d_d1(close, volume):
    return f22_obvd_031_obv_new_high_count_252d(close, volume).diff()


def f22_obvd_032_obv_new_high_minus_price_new_high_252d_d1(high, close, volume):
    return f22_obvd_032_obv_new_high_minus_price_new_high_252d(high, close, volume).diff()


def f22_obvd_033_price_new_high_no_obv_new_high_indicator_d1(high, close, volume):
    return f22_obvd_033_price_new_high_no_obv_new_high_indicator(high, close, volume).diff()


def f22_obvd_034_price_new_high_no_obv_new_high_count_252d_d1(high, close, volume):
    return f22_obvd_034_price_new_high_no_obv_new_high_count_252d(high, close, volume).diff()


def f22_obvd_035_obv_peak_age_minus_price_peak_age_252d_d1(high, close, volume):
    return f22_obvd_035_obv_peak_age_minus_price_peak_age_252d(high, close, volume).diff()


def f22_obvd_036_obv_at_price_new_252d_high_zscore_d1(high, close, volume):
    return f22_obvd_036_obv_at_price_new_252d_high_zscore(high, close, volume).diff()


def f22_obvd_037_obv_max_minus_price_max_count_252d_consec_d1(high, close, volume):
    return f22_obvd_037_obv_max_minus_price_max_count_252d_consec(high, close, volume).diff()


def f22_obvd_038_obv_roc_21d_d1(close, volume):
    return f22_obvd_038_obv_roc_21d(close, volume).diff()


def f22_obvd_039_obv_roc_63d_d1(close, volume):
    return f22_obvd_039_obv_roc_63d(close, volume).diff()


def f22_obvd_040_obv_roc_252d_d1(close, volume):
    return f22_obvd_040_obv_roc_252d(close, volume).diff()


def f22_obvd_041_obv_roc_21d_norm_by_vol_mean_d1(close, volume):
    return f22_obvd_041_obv_roc_21d_norm_by_vol_mean(close, volume).diff()


def f22_obvd_042_obv_roc_acceleration_21_minus_63_d1(close, volume):
    return f22_obvd_042_obv_roc_acceleration_21_minus_63(close, volume).diff()


def f22_obvd_043_obv_decay_ratio_since_252d_peak_d1(close, volume):
    return f22_obvd_043_obv_decay_ratio_since_252d_peak(close, volume).diff()


def f22_obvd_044_obv_decay_post_peak_slope_21d_d1(close, volume):
    return f22_obvd_044_obv_decay_post_peak_slope_21d(close, volume).diff()


def f22_obvd_045_obv_post_peak_half_life_63d_d1(close, volume):
    return f22_obvd_045_obv_post_peak_half_life_63d(close, volume).diff()


def f22_obvd_046_obv_cumulative_post_peak_deficit_252d_d1(close, volume):
    return f22_obvd_046_obv_cumulative_post_peak_deficit_252d(close, volume).diff()


def f22_obvd_047_obv_recovery_indicator_to_peak_252d_d1(close, volume):
    return f22_obvd_047_obv_recovery_indicator_to_peak_252d(close, volume).diff()


def f22_obvd_048_obv_consecutive_below_max_streak_252d_d1(close, volume):
    return f22_obvd_048_obv_consecutive_below_max_streak_252d(close, volume).diff()


def f22_obvd_049_hurst_obv_252d_d1(close, volume):
    return f22_obvd_049_hurst_obv_252d(close, volume).diff()


def f22_obvd_050_hurst_obv_504d_d1(close, volume):
    return f22_obvd_050_hurst_obv_504d(close, volume).diff()


def f22_obvd_051_obv_autocorr_lag1_252d_d1(close, volume):
    return f22_obvd_051_obv_autocorr_lag1_252d(close, volume).diff()


def f22_obvd_052_obv_autocorr_lag5_252d_d1(close, volume):
    return f22_obvd_052_obv_autocorr_lag5_252d(close, volume).diff()


def f22_obvd_053_obv_corr_price_252d_d1(close, volume):
    return f22_obvd_053_obv_corr_price_252d(close, volume).diff()


def f22_obvd_054_obv_corr_price_63d_d1(close, volume):
    return f22_obvd_054_obv_corr_price_63d(close, volume).diff()


def f22_obvd_055_obv_rank_corr_price_252d_d1(close, volume):
    return f22_obvd_055_obv_rank_corr_price_252d(close, volume).diff()


def f22_obvd_056_bearish_divergence_score_252d_d1(high, close, volume):
    return f22_obvd_056_bearish_divergence_score_252d(high, close, volume).diff()


def f22_obvd_057_obv_failure_to_new_high_score_252d_d1(high, close, volume):
    return f22_obvd_057_obv_failure_to_new_high_score_252d(high, close, volume).diff()


def f22_obvd_058_obv_underperformance_score_63d_d1(close, volume):
    return f22_obvd_058_obv_underperformance_score_63d(close, volume).diff()


def f22_obvd_059_obv_above_sma21_indicator_d1(close, volume):
    return f22_obvd_059_obv_above_sma21_indicator(close, volume).diff()


def f22_obvd_060_obv_above_sma63_indicator_d1(close, volume):
    return f22_obvd_060_obv_above_sma63_indicator(close, volume).diff()


def f22_obvd_061_obv_cross_sma21_down_indicator_d1(close, volume):
    return f22_obvd_061_obv_cross_sma21_down_indicator(close, volume).diff()


def f22_obvd_062_obv_cross_sma63_down_indicator_d1(close, volume):
    return f22_obvd_062_obv_cross_sma63_down_indicator(close, volume).diff()


def f22_obvd_063_obv_cross_sma21_count_252d_d1(close, volume):
    return f22_obvd_063_obv_cross_sma21_count_252d(close, volume).diff()


def f22_obvd_064_obv_below_sma21_dwell_252d_d1(close, volume):
    return f22_obvd_064_obv_below_sma21_dwell_252d(close, volume).diff()


def f22_obvd_065_obv_std_diff_252d_d1(close, volume):
    return f22_obvd_065_obv_std_diff_252d(close, volume).diff()


def f22_obvd_066_obv_r2_trend_252d_d1(close, volume):
    return f22_obvd_066_obv_r2_trend_252d(close, volume).diff()


def f22_obvd_067_obv_atr_normalized_slope_63d_d1(high, low, close, volume):
    return f22_obvd_067_obv_atr_normalized_slope_63d(high, low, close, volume).diff()


def f22_obvd_068_obv_volatility_to_signal_ratio_252d_d1(close, volume):
    return f22_obvd_068_obv_volatility_to_signal_ratio_252d(close, volume).diff()


def f22_obvd_069_obv_skew_diff_252d_d1(close, volume):
    return f22_obvd_069_obv_skew_diff_252d(close, volume).diff()


def f22_obvd_070_obv_sign_run_length_current_d1(close, volume):
    return f22_obvd_070_obv_sign_run_length_current(close, volume).diff()


def f22_obvd_071_obv_negative_runs_count_252d_d1(close, volume):
    return f22_obvd_071_obv_negative_runs_count_252d(close, volume).diff()


def f22_obvd_072_obv_max_negative_run_length_252d_d1(close, volume):
    return f22_obvd_072_obv_max_negative_run_length_252d(close, volume).diff()


def f22_obvd_073_obv_down_volume_weighted_streak_d1(close, volume):
    return f22_obvd_073_obv_down_volume_weighted_streak(close, volume).diff()


def f22_obvd_074_obv_positive_to_negative_run_ratio_252d_d1(close, volume):
    return f22_obvd_074_obv_positive_to_negative_run_ratio_252d(close, volume).diff()


def f22_obvd_075_obv_consecutive_below_zero_252d_d1(close, volume):
    return f22_obvd_075_obv_consecutive_below_zero_252d(close, volume).diff()


ON_BALANCE_VOLUME_DYNAMICS_D1_REGISTRY_001_075 = {
    "f22_obvd_001_obv_slope_21d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_001_obv_slope_21d_d1},
    "f22_obvd_002_obv_slope_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_002_obv_slope_63d_d1},
    "f22_obvd_003_obv_slope_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_003_obv_slope_252d_d1},
    "f22_obvd_004_obv_slope_504d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_004_obv_slope_504d_d1},
    "f22_obvd_005_obv_slope_5d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_005_obv_slope_5d_d1},
    "f22_obvd_006_obv_minus_price_slope_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_006_obv_minus_price_slope_63d_d1},
    "f22_obvd_007_obv_minus_price_slope_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_007_obv_minus_price_slope_252d_d1},
    "f22_obvd_008_obv_minus_price_slope_21d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_008_obv_minus_price_slope_21d_d1},
    "f22_obvd_009_obv_vs_price_slope_ratio_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_009_obv_vs_price_slope_ratio_63d_d1},
    "f22_obvd_010_obv_slope_sign_mismatch_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_010_obv_slope_sign_mismatch_252d_d1},
    "f22_obvd_011_obv_slope_sign_mismatch_count_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_011_obv_slope_sign_mismatch_count_252d_d1},
    "f22_obvd_012_obv_slope_decline_while_price_up_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_012_obv_slope_decline_while_price_up_252d_d1},
    "f22_obvd_013_obv_zscore_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_013_obv_zscore_252d_d1},
    "f22_obvd_014_obv_zscore_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_014_obv_zscore_63d_d1},
    "f22_obvd_015_obv_zscore_504d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_015_obv_zscore_504d_d1},
    "f22_obvd_016_obv_robust_z_mad_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_016_obv_robust_z_mad_252d_d1},
    "f22_obvd_017_obv_zscore_diff_63_minus_252_d1": {"inputs": ["close", "volume"], "func": f22_obvd_017_obv_zscore_diff_63_minus_252_d1},
    "f22_obvd_018_obv_pct_rank_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_018_obv_pct_rank_252d_d1},
    "f22_obvd_019_obv_minus_sma21_d1": {"inputs": ["close", "volume"], "func": f22_obvd_019_obv_minus_sma21_d1},
    "f22_obvd_020_obv_minus_sma63_d1": {"inputs": ["close", "volume"], "func": f22_obvd_020_obv_minus_sma63_d1},
    "f22_obvd_021_obv_minus_sma252_d1": {"inputs": ["close", "volume"], "func": f22_obvd_021_obv_minus_sma252_d1},
    "f22_obvd_022_obv_ema_distance_atr_normalized_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_022_obv_ema_distance_atr_normalized_21d_d1},
    "f22_obvd_023_obv_ema21_minus_ema63_d1": {"inputs": ["close", "volume"], "func": f22_obvd_023_obv_ema21_minus_ema63_d1},
    "f22_obvd_024_obv_ema9_minus_ema21_d1": {"inputs": ["close", "volume"], "func": f22_obvd_024_obv_ema9_minus_ema21_d1},
    "f22_obvd_025_obv_minus_max_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_025_obv_minus_max_252d_d1},
    "f22_obvd_026_obv_minus_max_504d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_026_obv_minus_max_504d_d1},
    "f22_obvd_027_obv_max_age_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_027_obv_max_age_252d_d1},
    "f22_obvd_028_obv_max_age_504d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_028_obv_max_age_504d_d1},
    "f22_obvd_029_obv_recovery_failure_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_029_obv_recovery_failure_252d_d1},
    "f22_obvd_030_obv_drawdown_from_max_norm_by_std_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_030_obv_drawdown_from_max_norm_by_std_252d_d1},
    "f22_obvd_031_obv_new_high_count_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_031_obv_new_high_count_252d_d1},
    "f22_obvd_032_obv_new_high_minus_price_new_high_252d_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_032_obv_new_high_minus_price_new_high_252d_d1},
    "f22_obvd_033_price_new_high_no_obv_new_high_indicator_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_033_price_new_high_no_obv_new_high_indicator_d1},
    "f22_obvd_034_price_new_high_no_obv_new_high_count_252d_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_034_price_new_high_no_obv_new_high_count_252d_d1},
    "f22_obvd_035_obv_peak_age_minus_price_peak_age_252d_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_035_obv_peak_age_minus_price_peak_age_252d_d1},
    "f22_obvd_036_obv_at_price_new_252d_high_zscore_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_036_obv_at_price_new_252d_high_zscore_d1},
    "f22_obvd_037_obv_max_minus_price_max_count_252d_consec_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_037_obv_max_minus_price_max_count_252d_consec_d1},
    "f22_obvd_038_obv_roc_21d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_038_obv_roc_21d_d1},
    "f22_obvd_039_obv_roc_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_039_obv_roc_63d_d1},
    "f22_obvd_040_obv_roc_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_040_obv_roc_252d_d1},
    "f22_obvd_041_obv_roc_21d_norm_by_vol_mean_d1": {"inputs": ["close", "volume"], "func": f22_obvd_041_obv_roc_21d_norm_by_vol_mean_d1},
    "f22_obvd_042_obv_roc_acceleration_21_minus_63_d1": {"inputs": ["close", "volume"], "func": f22_obvd_042_obv_roc_acceleration_21_minus_63_d1},
    "f22_obvd_043_obv_decay_ratio_since_252d_peak_d1": {"inputs": ["close", "volume"], "func": f22_obvd_043_obv_decay_ratio_since_252d_peak_d1},
    "f22_obvd_044_obv_decay_post_peak_slope_21d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_044_obv_decay_post_peak_slope_21d_d1},
    "f22_obvd_045_obv_post_peak_half_life_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_045_obv_post_peak_half_life_63d_d1},
    "f22_obvd_046_obv_cumulative_post_peak_deficit_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_046_obv_cumulative_post_peak_deficit_252d_d1},
    "f22_obvd_047_obv_recovery_indicator_to_peak_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_047_obv_recovery_indicator_to_peak_252d_d1},
    "f22_obvd_048_obv_consecutive_below_max_streak_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_048_obv_consecutive_below_max_streak_252d_d1},
    "f22_obvd_049_hurst_obv_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_049_hurst_obv_252d_d1},
    "f22_obvd_050_hurst_obv_504d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_050_hurst_obv_504d_d1},
    "f22_obvd_051_obv_autocorr_lag1_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_051_obv_autocorr_lag1_252d_d1},
    "f22_obvd_052_obv_autocorr_lag5_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_052_obv_autocorr_lag5_252d_d1},
    "f22_obvd_053_obv_corr_price_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_053_obv_corr_price_252d_d1},
    "f22_obvd_054_obv_corr_price_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_054_obv_corr_price_63d_d1},
    "f22_obvd_055_obv_rank_corr_price_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_055_obv_rank_corr_price_252d_d1},
    "f22_obvd_056_bearish_divergence_score_252d_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_056_bearish_divergence_score_252d_d1},
    "f22_obvd_057_obv_failure_to_new_high_score_252d_d1": {"inputs": ["high", "close", "volume"], "func": f22_obvd_057_obv_failure_to_new_high_score_252d_d1},
    "f22_obvd_058_obv_underperformance_score_63d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_058_obv_underperformance_score_63d_d1},
    "f22_obvd_059_obv_above_sma21_indicator_d1": {"inputs": ["close", "volume"], "func": f22_obvd_059_obv_above_sma21_indicator_d1},
    "f22_obvd_060_obv_above_sma63_indicator_d1": {"inputs": ["close", "volume"], "func": f22_obvd_060_obv_above_sma63_indicator_d1},
    "f22_obvd_061_obv_cross_sma21_down_indicator_d1": {"inputs": ["close", "volume"], "func": f22_obvd_061_obv_cross_sma21_down_indicator_d1},
    "f22_obvd_062_obv_cross_sma63_down_indicator_d1": {"inputs": ["close", "volume"], "func": f22_obvd_062_obv_cross_sma63_down_indicator_d1},
    "f22_obvd_063_obv_cross_sma21_count_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_063_obv_cross_sma21_count_252d_d1},
    "f22_obvd_064_obv_below_sma21_dwell_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_064_obv_below_sma21_dwell_252d_d1},
    "f22_obvd_065_obv_std_diff_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_065_obv_std_diff_252d_d1},
    "f22_obvd_066_obv_r2_trend_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_066_obv_r2_trend_252d_d1},
    "f22_obvd_067_obv_atr_normalized_slope_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_067_obv_atr_normalized_slope_63d_d1},
    "f22_obvd_068_obv_volatility_to_signal_ratio_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_068_obv_volatility_to_signal_ratio_252d_d1},
    "f22_obvd_069_obv_skew_diff_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_069_obv_skew_diff_252d_d1},
    "f22_obvd_070_obv_sign_run_length_current_d1": {"inputs": ["close", "volume"], "func": f22_obvd_070_obv_sign_run_length_current_d1},
    "f22_obvd_071_obv_negative_runs_count_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_071_obv_negative_runs_count_252d_d1},
    "f22_obvd_072_obv_max_negative_run_length_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_072_obv_max_negative_run_length_252d_d1},
    "f22_obvd_073_obv_down_volume_weighted_streak_d1": {"inputs": ["close", "volume"], "func": f22_obvd_073_obv_down_volume_weighted_streak_d1},
    "f22_obvd_074_obv_positive_to_negative_run_ratio_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_074_obv_positive_to_negative_run_ratio_252d_d1},
    "f22_obvd_075_obv_consecutive_below_zero_252d_d1": {"inputs": ["close", "volume"], "func": f22_obvd_075_obv_consecutive_below_zero_252d_d1},
}
