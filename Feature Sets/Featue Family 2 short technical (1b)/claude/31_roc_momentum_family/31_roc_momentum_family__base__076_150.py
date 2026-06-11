"""roc_momentum_family base features 076-150 — Pipeline 1b-technical.

Continuation of 001-075. Buckets in this file:
E (asymmetry/skew, finishing 076-080), F (composites/spreads/dispersion across
horizons, 081-100), G (ROC extremes / distance-from-rolling-extreme / decay,
101-120), H (regime/persistence/acceleration/vol-of-ROC, 121-150).

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


# ============================================================
# Bucket E (continued) — Asymmetry / capture / skew (076-080)
# ============================================================

def f31_rcmf_076_upside_downside_capture_ratio_63d(close: pd.Series) -> pd.Series:
    """Sum of positive 1d returns / |sum of negative 1d returns| in trailing 63d — upside-vs-downside capture."""
    r = close.pct_change(1)
    pos_sum = r.clip(lower=0).rolling(QDAYS, min_periods=MDAYS).sum()
    neg_sum_abs = (-r.clip(upper=0)).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(pos_sum, neg_sum_abs)


def f31_rcmf_077_skew_1d_returns_63d(close: pd.Series) -> pd.Series:
    """Sample skewness of 1d returns in trailing 63d — distributional asymmetry."""
    r = close.pct_change(1)
    return r.rolling(QDAYS, min_periods=MDAYS).skew()


def f31_rcmf_078_skew_1d_returns_252d(close: pd.Series) -> pd.Series:
    """Sample skewness of 1d returns in trailing 252d — annual return distributional skew."""
    r = close.pct_change(1)
    return r.rolling(YDAYS, min_periods=QDAYS).skew()


def f31_rcmf_079_max_minus_min_1d_return_63d(close: pd.Series) -> pd.Series:
    """Best-day minus worst-day 1d return in trailing 63d — single-day amplitude range."""
    r = close.pct_change(1)
    return r.rolling(QDAYS, min_periods=MDAYS).max() - r.rolling(QDAYS, min_periods=MDAYS).min()


def f31_rcmf_080_positive_day_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of positive 1d returns in trailing 252d — bullish-day proportion over the year."""
    r = close.pct_change(1)
    pos = (r > 0).astype(float)
    valid = r.notna().astype(float)
    return _safe_div(pos.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
# Bucket F — Composites / spreads / dispersion across horizons (081-100)
# Multi-horizon agreement / divergence — each = a different *concept* of how
# the momentum term-structure shapes up.
# ============================================================

def f31_rcmf_081_roc_5d_minus_roc_21d_spread(close: pd.Series) -> pd.Series:
    """5d ROC minus 21d ROC — short-vs-medium momentum divergence."""
    return close.pct_change(WDAYS) - close.pct_change(MDAYS)


def f31_rcmf_082_roc_21d_minus_roc_63d_spread(close: pd.Series) -> pd.Series:
    """21d ROC minus 63d ROC — medium-vs-long momentum divergence."""
    return close.pct_change(MDAYS) - close.pct_change(QDAYS)


def f31_rcmf_083_roc_63d_minus_roc_252d_spread(close: pd.Series) -> pd.Series:
    """63d ROC minus 252d ROC — quarterly vs annual momentum divergence."""
    return close.pct_change(QDAYS) - close.pct_change(YDAYS)


def f31_rcmf_084_roc_5d_minus_roc_63d_spread(close: pd.Series) -> pd.Series:
    """5d ROC minus 63d ROC — weekly vs quarterly momentum divergence."""
    return close.pct_change(WDAYS) - close.pct_change(QDAYS)


def f31_rcmf_085_roc_short_horizon_avg(close: pd.Series) -> pd.Series:
    """Mean of {5d, 10d, 21d} ROCs — composite short-horizon momentum."""
    a = close.pct_change(WDAYS)
    b = close.pct_change(10)
    c = close.pct_change(MDAYS)
    return (a + b + c) / 3.0


def f31_rcmf_086_roc_long_horizon_avg(close: pd.Series) -> pd.Series:
    """Mean of {126d, 252d, 504d} ROCs — composite long-horizon momentum."""
    a = close.pct_change(126)
    b = close.pct_change(YDAYS)
    c = close.pct_change(DDAYS_2Y)
    return (a + b + c) / 3.0


def f31_rcmf_087_roc_short_minus_long_composite(close: pd.Series) -> pd.Series:
    """Short-horizon composite minus long-horizon composite — fast vs slow momentum disagreement."""
    short = (close.pct_change(WDAYS) + close.pct_change(10) + close.pct_change(MDAYS)) / 3.0
    long_ = (close.pct_change(126) + close.pct_change(YDAYS) + close.pct_change(DDAYS_2Y)) / 3.0
    return short - long_


def f31_rcmf_088_roc_dispersion_across_horizons(close: pd.Series) -> pd.Series:
    """Cross-sectional std-dev of ROCs at {5,21,63,252} — momentum-term-structure dispersion."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
    ], axis=1)
    return parts.std(axis=1)


def f31_rcmf_089_roc_term_structure_slope(close: pd.Series) -> pd.Series:
    """Slope of (ROC at h ∈ {5,21,63,252}) vs log(h) — momentum term-structure slope."""
    h_vals = np.array([WDAYS, MDAYS, QDAYS, YDAYS], dtype=float)
    x = np.log(h_vals)
    xm = x.mean(); sx = ((x - xm) ** 2).sum()
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
    ], axis=1)
    arr = parts.values
    mean_y = np.nanmean(arr, axis=1, keepdims=True)
    cov = np.nansum((arr - mean_y) * (x - xm), axis=1)
    slope = cov / sx
    valid = np.isfinite(arr).sum(axis=1) >= 2
    slope = np.where(valid, slope, np.nan)
    return pd.Series(slope, index=close.index)


def f31_rcmf_090_roc_term_structure_concavity(close: pd.Series) -> pd.Series:
    """ROC(63d) − 0.5*(ROC(5d)+ROC(252d)) — concavity / kink of the momentum term-structure."""
    return close.pct_change(QDAYS) - 0.5 * (close.pct_change(WDAYS) + close.pct_change(YDAYS))


def f31_rcmf_091_all_positive_horizons_indicator(close: pd.Series) -> pd.Series:
    """Indicator: ROCs at {5,21,63,252} all positive — full-stack-up alignment."""
    a = close.pct_change(WDAYS)
    b = close.pct_change(MDAYS)
    c = close.pct_change(QDAYS)
    d = close.pct_change(YDAYS)
    cond = (a > 0) & (b > 0) & (c > 0) & (d > 0)
    valid = a.notna() & b.notna() & c.notna() & d.notna()
    return cond.astype(float).where(valid, np.nan)


def f31_rcmf_092_all_negative_horizons_indicator(close: pd.Series) -> pd.Series:
    """Indicator: ROCs at {5,21,63,252} all negative — full-stack-down alignment."""
    a = close.pct_change(WDAYS)
    b = close.pct_change(MDAYS)
    c = close.pct_change(QDAYS)
    d = close.pct_change(YDAYS)
    cond = (a < 0) & (b < 0) & (c < 0) & (d < 0)
    valid = a.notna() & b.notna() & c.notna() & d.notna()
    return cond.astype(float).where(valid, np.nan)


def f31_rcmf_093_horizon_alignment_count(close: pd.Series) -> pd.Series:
    """Number of horizons (out of {5,21,63,252}) with positive ROC — directional-alignment count."""
    a = (close.pct_change(WDAYS) > 0).astype(float)
    b = (close.pct_change(MDAYS) > 0).astype(float)
    c = (close.pct_change(QDAYS) > 0).astype(float)
    d = (close.pct_change(YDAYS) > 0).astype(float)
    valid = close.pct_change(WDAYS).notna() & close.pct_change(MDAYS).notna() & close.pct_change(QDAYS).notna() & close.pct_change(YDAYS).notna()
    return (a + b + c + d).where(valid, np.nan)


def f31_rcmf_094_short_positive_long_negative_indicator(close: pd.Series) -> pd.Series:
    """Indicator: short(21d) > 0 AND long(252d) < 0 — bear-market rally pattern."""
    s = close.pct_change(MDAYS)
    l = close.pct_change(YDAYS)
    cond = (s > 0) & (l < 0)
    return cond.astype(float).where(s.notna() & l.notna(), np.nan)


def f31_rcmf_095_short_negative_long_positive_indicator(close: pd.Series) -> pd.Series:
    """Indicator: short(21d) < 0 AND long(252d) > 0 — distribution-in-uptrend pattern."""
    s = close.pct_change(MDAYS)
    l = close.pct_change(YDAYS)
    cond = (s < 0) & (l > 0)
    return cond.astype(float).where(s.notna() & l.notna(), np.nan)


def f31_rcmf_096_roc_5d_to_roc_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d ROC to 21d ROC — relative pace of weekly vs monthly impulse."""
    return _safe_div(close.pct_change(WDAYS), close.pct_change(MDAYS))


def f31_rcmf_097_roc_21d_to_roc_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21d ROC to 252d ROC — relative pace of monthly vs annual impulse."""
    return _safe_div(close.pct_change(MDAYS), close.pct_change(YDAYS))


def f31_rcmf_098_max_horizon_roc(close: pd.Series) -> pd.Series:
    """Max of ROCs at {5,21,63,252} — best-horizon momentum reading."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
    ], axis=1)
    return parts.max(axis=1)


def f31_rcmf_099_min_horizon_roc(close: pd.Series) -> pd.Series:
    """Min of ROCs at {5,21,63,252} — worst-horizon momentum reading."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
    ], axis=1)
    return parts.min(axis=1)


def f31_rcmf_100_roc_horizon_argmax(close: pd.Series) -> pd.Series:
    """Index (0..3) of horizon with max ROC among {5,21,63,252} — which time-scale dominates."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename(0),
        close.pct_change(MDAYS).rename(1),
        close.pct_change(QDAYS).rename(2),
        close.pct_change(YDAYS).rename(3),
    ], axis=1)
    any_valid = parts.notna().any(axis=1)
    res = parts.fillna(-np.inf).idxmax(axis=1).where(any_valid, np.nan).astype(float)
    return res


# ============================================================
# Bucket G — ROC extremes / distance-from-rolling-extreme / decay (101-120)
# ============================================================

def f31_rcmf_101_roc_21d_max_in_63d(close: pd.Series) -> pd.Series:
    """Max of 21d ROC over trailing 63d — best monthly-momentum reading of the quarter."""
    return close.pct_change(MDAYS).rolling(QDAYS, min_periods=MDAYS).max()


def f31_rcmf_102_roc_21d_min_in_63d(close: pd.Series) -> pd.Series:
    """Min of 21d ROC over trailing 63d — worst monthly-momentum reading of the quarter."""
    return close.pct_change(MDAYS).rolling(QDAYS, min_periods=MDAYS).min()


def f31_rcmf_103_roc_63d_max_in_252d(close: pd.Series) -> pd.Series:
    """Max of 63d ROC over trailing 252d — best quarterly-momentum reading of the year."""
    return close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max()


def f31_rcmf_104_roc_63d_min_in_252d(close: pd.Series) -> pd.Series:
    """Min of 63d ROC over trailing 252d — worst quarterly-momentum reading of the year."""
    return close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).min()


def f31_rcmf_105_roc_252d_max_in_1260d(close: pd.Series) -> pd.Series:
    """Max of 252d ROC over trailing 1260d — best annual-momentum reading of the 5-year window."""
    return close.pct_change(YDAYS).rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f31_rcmf_106_roc_21d_decay_from_63d_max(close: pd.Series) -> pd.Series:
    """Current 21d ROC minus its trailing-63d max — exhaustion distance below recent peak."""
    r = close.pct_change(MDAYS)
    return r - r.rolling(QDAYS, min_periods=MDAYS).max()


def f31_rcmf_107_roc_63d_decay_from_252d_max(close: pd.Series) -> pd.Series:
    """Current 63d ROC minus its trailing-252d max — exhaustion distance below annual momentum peak."""
    r = close.pct_change(QDAYS)
    return r - r.rolling(YDAYS, min_periods=QDAYS).max()


def f31_rcmf_108_roc_252d_decay_from_1260d_max(close: pd.Series) -> pd.Series:
    """Current 252d ROC minus its trailing-1260d max — distance below 5-year-window momentum peak."""
    r = close.pct_change(YDAYS)
    return r - r.rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f31_rcmf_109_roc_21d_normalized_distance_from_63d_max(close: pd.Series) -> pd.Series:
    """(roc_21 − max_63(roc_21)) / |max_63(roc_21)| — scale-free exhaustion ratio."""
    r = close.pct_change(MDAYS)
    rmax = r.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(r - rmax, rmax.abs())


def f31_rcmf_110_days_since_roc_21d_max_63d(close: pd.Series) -> pd.Series:
    """Bars since trailing-63d argmax of 21d ROC — momentum-peak age in days."""
    r = close.pct_change(MDAYS)
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)


def f31_rcmf_111_days_since_roc_63d_max_252d(close: pd.Series) -> pd.Series:
    """Bars since trailing-252d argmax of 63d ROC — quarterly-momentum-peak age."""
    r = close.pct_change(QDAYS)
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f31_rcmf_112_days_since_roc_252d_max_1260d(close: pd.Series) -> pd.Series:
    """Bars since trailing-1260d argmax of 252d ROC — annual-momentum-peak age over 5y."""
    r = close.pct_change(YDAYS)
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_bsm, raw=True)


def f31_rcmf_113_days_since_roc_21d_min_63d(close: pd.Series) -> pd.Series:
    """Bars since trailing-63d argmin of 21d ROC — bars since worst monthly-momentum reading."""
    r = close.pct_change(MDAYS)
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        idx = int(np.nanargmin(w))
        return float(len(w) - 1 - idx)
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)


def f31_rcmf_114_roc_5d_max_in_21d(close: pd.Series) -> pd.Series:
    """Max of 5d ROC over trailing 21d — best weekly-momentum reading of the month."""
    return close.pct_change(WDAYS).rolling(MDAYS, min_periods=WDAYS).max()


def f31_rcmf_115_roc_5d_decay_from_21d_max(close: pd.Series) -> pd.Series:
    """Current 5d ROC minus its trailing-21d max — short-horizon exhaustion."""
    r = close.pct_change(WDAYS)
    return r - r.rolling(MDAYS, min_periods=WDAYS).max()


def f31_rcmf_116_log_return_252d_decay_from_1260d_max(close: pd.Series) -> pd.Series:
    """Current 252d log-return minus its 1260d max — log-momentum distance from 5y-window peak."""
    r = _safe_log(close).diff(YDAYS)
    return r - r.rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f31_rcmf_117_roc_21d_amplitude_252d(close: pd.Series) -> pd.Series:
    """Trailing-252d max minus min of 21d ROC — annual amplitude of monthly-momentum oscillation."""
    r = close.pct_change(MDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).max() - r.rolling(YDAYS, min_periods=QDAYS).min()


def f31_rcmf_118_roc_63d_amplitude_504d(close: pd.Series) -> pd.Series:
    """Trailing-504d max minus min of 63d ROC — biennial amplitude of quarterly-momentum oscillation."""
    r = close.pct_change(QDAYS)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).max() - r.rolling(DDAYS_2Y, min_periods=YDAYS).min()


def f31_rcmf_119_roc_21d_position_in_252d_range(close: pd.Series) -> pd.Series:
    """(roc_21 − min_252) / (max_252 − min_252) — current monthly-momentum position in annual range."""
    r = close.pct_change(MDAYS)
    rmax = r.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = r.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(r - rmin, rmax - rmin)


def f31_rcmf_120_roc_63d_position_in_504d_range(close: pd.Series) -> pd.Series:
    """(roc_63 − min_504) / (max_504 − min_504) — current quarterly-momentum position in biennial range."""
    r = close.pct_change(QDAYS)
    rmax = r.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    rmin = r.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(r - rmin, rmax - rmin)


# ============================================================
# Bucket H — Regime / persistence / acceleration / vol-of-ROC (121-150)
# ============================================================

def f31_rcmf_121_roc_21d_smoothed_5d(close: pd.Series) -> pd.Series:
    """5d trailing-mean smoothing of 21d ROC — denoised monthly momentum."""
    return close.pct_change(MDAYS).rolling(WDAYS, min_periods=2).mean()


def f31_rcmf_122_roc_63d_smoothed_21d(close: pd.Series) -> pd.Series:
    """21d trailing-mean smoothing of 63d ROC — denoised quarterly momentum."""
    return close.pct_change(QDAYS).rolling(MDAYS, min_periods=WDAYS).mean()


def f31_rcmf_123_roc_252d_smoothed_63d(close: pd.Series) -> pd.Series:
    """63d trailing-mean smoothing of 252d ROC — denoised annual momentum."""
    return close.pct_change(YDAYS).rolling(QDAYS, min_periods=MDAYS).mean()


def f31_rcmf_124_roc_21d_acceleration_5d(close: pd.Series) -> pd.Series:
    """5d change in 21d ROC — short-horizon monthly-momentum acceleration."""
    r = close.pct_change(MDAYS)
    return r - r.shift(WDAYS)


def f31_rcmf_125_roc_63d_acceleration_21d(close: pd.Series) -> pd.Series:
    """21d change in 63d ROC — monthly-horizon quarterly-momentum acceleration."""
    r = close.pct_change(QDAYS)
    return r - r.shift(MDAYS)


def f31_rcmf_126_roc_252d_acceleration_63d(close: pd.Series) -> pd.Series:
    """63d change in 252d ROC — quarterly-horizon annual-momentum acceleration."""
    r = close.pct_change(YDAYS)
    return r - r.shift(QDAYS)


def f31_rcmf_127_roc_21d_slope_21d(close: pd.Series) -> pd.Series:
    """21d linear-regression slope of 21d ROC — momentum-of-momentum trend."""
    return _rolling_slope(close.pct_change(MDAYS), MDAYS)


def f31_rcmf_128_roc_63d_slope_63d(close: pd.Series) -> pd.Series:
    """63d linear-regression slope of 63d ROC — quarterly momentum-of-momentum trend."""
    return _rolling_slope(close.pct_change(QDAYS), QDAYS)


def f31_rcmf_129_roc_252d_slope_252d(close: pd.Series) -> pd.Series:
    """252d linear-regression slope of 252d ROC — annual momentum-of-momentum trend."""
    return _rolling_slope(close.pct_change(YDAYS), YDAYS)


def f31_rcmf_130_roc_sign_change_count_21d(close: pd.Series) -> pd.Series:
    """Count of 1d-return sign flips in trailing 21d — daily-momentum-chop frequency."""
    r = close.pct_change(1)
    s = np.sign(r)
    flip = (s != s.shift(1)) & r.notna() & r.shift(1).notna()
    return flip.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f31_rcmf_131_roc_sign_change_count_63d(close: pd.Series) -> pd.Series:
    """Count of 1d-return sign flips in trailing 63d — quarterly daily-momentum-chop frequency."""
    r = close.pct_change(1)
    s = np.sign(r)
    flip = (s != s.shift(1)) & r.notna() & r.shift(1).notna()
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f31_rcmf_132_consecutive_positive_1d_streak(close: pd.Series) -> pd.Series:
    """Length of current consecutive up-day streak — persistence of positive daily returns."""
    r = close.pct_change(1)
    up = (r > 0).astype(float).values
    valid = r.notna().values
    n = len(up)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if not valid[i]:
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if up[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=r.index)


def f31_rcmf_133_consecutive_negative_1d_streak(close: pd.Series) -> pd.Series:
    """Length of current consecutive down-day streak — persistence of negative daily returns."""
    r = close.pct_change(1)
    dn = (r < 0).astype(float).values
    valid = r.notna().values
    n = len(dn)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if not valid[i]:
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if dn[i] > 0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=r.index)


def f31_rcmf_134_roc_21d_persistence_positive_5d(close: pd.Series) -> pd.Series:
    """Indicator: 21d ROC > 0 every bar in trailing 5d — fresh-sustained-positive monthly momentum."""
    r = close.pct_change(MDAYS)
    pos = (r > 0).astype(float)
    s = pos.rolling(WDAYS, min_periods=WDAYS).sum()
    return (s >= WDAYS).astype(float).where(r.notna(), np.nan)


def f31_rcmf_135_roc_63d_persistence_negative_21d(close: pd.Series) -> pd.Series:
    """Indicator: 63d ROC < 0 every bar in trailing 21d — sustained-negative quarterly momentum."""
    r = close.pct_change(QDAYS)
    neg = (r < 0).astype(float)
    s = neg.rolling(MDAYS, min_periods=MDAYS).sum()
    return (s >= MDAYS).astype(float).where(r.notna(), np.nan)


def f31_rcmf_136_vol_of_1d_returns_21d(close: pd.Series) -> pd.Series:
    """Std-dev of 1d returns in trailing 21d — short-horizon realized volatility of daily ROC."""
    return close.pct_change(1).rolling(MDAYS, min_periods=WDAYS).std()


def f31_rcmf_137_vol_of_1d_returns_63d(close: pd.Series) -> pd.Series:
    """Std-dev of 1d returns in trailing 63d — quarterly realized volatility of daily ROC."""
    return close.pct_change(1).rolling(QDAYS, min_periods=MDAYS).std()


def f31_rcmf_138_vol_of_21d_roc_252d(close: pd.Series) -> pd.Series:
    """Std-dev of 21d ROC in trailing 252d — annual volatility of monthly-momentum readings."""
    return close.pct_change(MDAYS).rolling(YDAYS, min_periods=QDAYS).std()


def f31_rcmf_139_vol_of_63d_roc_504d(close: pd.Series) -> pd.Series:
    """Std-dev of 63d ROC in trailing 504d — biennial volatility of quarterly-momentum readings."""
    return close.pct_change(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f31_rcmf_140_vol_of_vol_1d_returns(close: pd.Series) -> pd.Series:
    """Std of (21d rolling std of 1d returns) over 63d — vol-of-vol on daily ROC."""
    s = close.pct_change(1).rolling(MDAYS, min_periods=WDAYS).std()
    return s.rolling(QDAYS, min_periods=MDAYS).std()


def f31_rcmf_141_roc_21d_drawdown_252d(close: pd.Series) -> pd.Series:
    """21d ROC minus its 252d running max — drawdown of monthly-momentum series."""
    r = close.pct_change(MDAYS)
    return r - r.rolling(YDAYS, min_periods=QDAYS).max()


def f31_rcmf_142_first_negative_roc_21d_after_positive_extreme(close: pd.Series) -> pd.Series:
    """Event: 21d ROC turned negative today AND its trailing-63d max was ≥ +20%."""
    r = close.pct_change(MDAYS)
    prior_max = r.rolling(QDAYS, min_periods=MDAYS).max().shift(1)
    cond = (r < 0) & (r.shift(1) >= 0) & (prior_max >= 0.20)
    return cond.astype(float).where(r.notna() & r.shift(1).notna() & prior_max.notna(), np.nan)


def f31_rcmf_143_roc_21d_half_life_decay_proxy(close: pd.Series) -> pd.Series:
    """Current 21d ROC divided by its trailing-63d max — proxy for fraction-of-peak-momentum remaining."""
    r = close.pct_change(MDAYS)
    rmax = r.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(r, rmax)


def f31_rcmf_144_recovery_speed_from_roc_21d_min(close: pd.Series) -> pd.Series:
    """(roc_21 − min_63(roc_21)) / bars_since_min — recovery rate from quarterly momentum trough."""
    r = close.pct_change(MDAYS)
    rmin = r.rolling(QDAYS, min_periods=MDAYS).min()
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        idx = int(np.nanargmin(w))
        return float(len(w) - 1 - idx)
    bars_since = r.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)
    return _safe_div(r - rmin, bars_since.replace(0, np.nan))


def f31_rcmf_145_roc_composite_index(close: pd.Series) -> pd.Series:
    """Sum of signs of ROCs at {5,21,63,252} — composite directional index in {−4..+4}."""
    a = np.sign(close.pct_change(WDAYS))
    b = np.sign(close.pct_change(MDAYS))
    c = np.sign(close.pct_change(QDAYS))
    d = np.sign(close.pct_change(YDAYS))
    s = a + b + c + d
    valid = close.pct_change(WDAYS).notna() & close.pct_change(MDAYS).notna() & close.pct_change(QDAYS).notna() & close.pct_change(YDAYS).notna()
    return s.where(valid, np.nan)


def f31_rcmf_146_roc_21d_above_long_run_mean_indicator(close: pd.Series) -> pd.Series:
    """Indicator: current 21d ROC above its trailing-252d mean — above-long-run-mean regime."""
    r = close.pct_change(MDAYS)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    return (r > m).astype(float).where(r.notna() & m.notna(), np.nan)


def f31_rcmf_147_roc_63d_dwell_above_zero_252d(close: pd.Series) -> pd.Series:
    """Bars in trailing 252d with 63d ROC > 0 — quarterly-momentum-positive dwell over the year."""
    r = close.pct_change(QDAYS)
    return (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f31_rcmf_148_roc_252d_dwell_above_zero_1260d(close: pd.Series) -> pd.Series:
    """Bars in trailing 1260d with 252d ROC > 0 — annual-momentum-positive dwell over the 5-year window."""
    r = close.pct_change(YDAYS)
    return (r > 0).astype(float).rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f31_rcmf_149_acceleration_to_volatility_ratio_21d(close: pd.Series) -> pd.Series:
    """5d change in 21d ROC divided by 21d return-volatility — momentum-acceleration normalized by noise."""
    r = close.pct_change(MDAYS)
    accel = r - r.shift(WDAYS)
    sigma = close.pct_change(1).rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(accel, sigma)


def f31_rcmf_150_post_peak_decay_speed_21d(close: pd.Series) -> pd.Series:
    """(trailing-63d max of roc_21 − current roc_21) / bars_since_max — post-peak momentum decay speed."""
    r = close.pct_change(MDAYS)
    rmax = r.rolling(QDAYS, min_periods=MDAYS).max()
    def _bsm(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    bars_since = r.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)
    return _safe_div(rmax - r, bars_since.replace(0, np.nan))


# ============================================================
#                         REGISTRY 076-150
# ============================================================

ROC_MOMENTUM_FAMILY_BASE_REGISTRY_076_150 = {
    "f31_rcmf_076_upside_downside_capture_ratio_63d": {"inputs": ["close"], "func": f31_rcmf_076_upside_downside_capture_ratio_63d},
    "f31_rcmf_077_skew_1d_returns_63d": {"inputs": ["close"], "func": f31_rcmf_077_skew_1d_returns_63d},
    "f31_rcmf_078_skew_1d_returns_252d": {"inputs": ["close"], "func": f31_rcmf_078_skew_1d_returns_252d},
    "f31_rcmf_079_max_minus_min_1d_return_63d": {"inputs": ["close"], "func": f31_rcmf_079_max_minus_min_1d_return_63d},
    "f31_rcmf_080_positive_day_fraction_252d": {"inputs": ["close"], "func": f31_rcmf_080_positive_day_fraction_252d},
    "f31_rcmf_081_roc_5d_minus_roc_21d_spread": {"inputs": ["close"], "func": f31_rcmf_081_roc_5d_minus_roc_21d_spread},
    "f31_rcmf_082_roc_21d_minus_roc_63d_spread": {"inputs": ["close"], "func": f31_rcmf_082_roc_21d_minus_roc_63d_spread},
    "f31_rcmf_083_roc_63d_minus_roc_252d_spread": {"inputs": ["close"], "func": f31_rcmf_083_roc_63d_minus_roc_252d_spread},
    "f31_rcmf_084_roc_5d_minus_roc_63d_spread": {"inputs": ["close"], "func": f31_rcmf_084_roc_5d_minus_roc_63d_spread},
    "f31_rcmf_085_roc_short_horizon_avg": {"inputs": ["close"], "func": f31_rcmf_085_roc_short_horizon_avg},
    "f31_rcmf_086_roc_long_horizon_avg": {"inputs": ["close"], "func": f31_rcmf_086_roc_long_horizon_avg},
    "f31_rcmf_087_roc_short_minus_long_composite": {"inputs": ["close"], "func": f31_rcmf_087_roc_short_minus_long_composite},
    "f31_rcmf_088_roc_dispersion_across_horizons": {"inputs": ["close"], "func": f31_rcmf_088_roc_dispersion_across_horizons},
    "f31_rcmf_089_roc_term_structure_slope": {"inputs": ["close"], "func": f31_rcmf_089_roc_term_structure_slope},
    "f31_rcmf_090_roc_term_structure_concavity": {"inputs": ["close"], "func": f31_rcmf_090_roc_term_structure_concavity},
    "f31_rcmf_091_all_positive_horizons_indicator": {"inputs": ["close"], "func": f31_rcmf_091_all_positive_horizons_indicator},
    "f31_rcmf_092_all_negative_horizons_indicator": {"inputs": ["close"], "func": f31_rcmf_092_all_negative_horizons_indicator},
    "f31_rcmf_093_horizon_alignment_count": {"inputs": ["close"], "func": f31_rcmf_093_horizon_alignment_count},
    "f31_rcmf_094_short_positive_long_negative_indicator": {"inputs": ["close"], "func": f31_rcmf_094_short_positive_long_negative_indicator},
    "f31_rcmf_095_short_negative_long_positive_indicator": {"inputs": ["close"], "func": f31_rcmf_095_short_negative_long_positive_indicator},
    "f31_rcmf_096_roc_5d_to_roc_21d_ratio": {"inputs": ["close"], "func": f31_rcmf_096_roc_5d_to_roc_21d_ratio},
    "f31_rcmf_097_roc_21d_to_roc_252d_ratio": {"inputs": ["close"], "func": f31_rcmf_097_roc_21d_to_roc_252d_ratio},
    "f31_rcmf_098_max_horizon_roc": {"inputs": ["close"], "func": f31_rcmf_098_max_horizon_roc},
    "f31_rcmf_099_min_horizon_roc": {"inputs": ["close"], "func": f31_rcmf_099_min_horizon_roc},
    "f31_rcmf_100_roc_horizon_argmax": {"inputs": ["close"], "func": f31_rcmf_100_roc_horizon_argmax},
    "f31_rcmf_101_roc_21d_max_in_63d": {"inputs": ["close"], "func": f31_rcmf_101_roc_21d_max_in_63d},
    "f31_rcmf_102_roc_21d_min_in_63d": {"inputs": ["close"], "func": f31_rcmf_102_roc_21d_min_in_63d},
    "f31_rcmf_103_roc_63d_max_in_252d": {"inputs": ["close"], "func": f31_rcmf_103_roc_63d_max_in_252d},
    "f31_rcmf_104_roc_63d_min_in_252d": {"inputs": ["close"], "func": f31_rcmf_104_roc_63d_min_in_252d},
    "f31_rcmf_105_roc_252d_max_in_1260d": {"inputs": ["close"], "func": f31_rcmf_105_roc_252d_max_in_1260d},
    "f31_rcmf_106_roc_21d_decay_from_63d_max": {"inputs": ["close"], "func": f31_rcmf_106_roc_21d_decay_from_63d_max},
    "f31_rcmf_107_roc_63d_decay_from_252d_max": {"inputs": ["close"], "func": f31_rcmf_107_roc_63d_decay_from_252d_max},
    "f31_rcmf_108_roc_252d_decay_from_1260d_max": {"inputs": ["close"], "func": f31_rcmf_108_roc_252d_decay_from_1260d_max},
    "f31_rcmf_109_roc_21d_normalized_distance_from_63d_max": {"inputs": ["close"], "func": f31_rcmf_109_roc_21d_normalized_distance_from_63d_max},
    "f31_rcmf_110_days_since_roc_21d_max_63d": {"inputs": ["close"], "func": f31_rcmf_110_days_since_roc_21d_max_63d},
    "f31_rcmf_111_days_since_roc_63d_max_252d": {"inputs": ["close"], "func": f31_rcmf_111_days_since_roc_63d_max_252d},
    "f31_rcmf_112_days_since_roc_252d_max_1260d": {"inputs": ["close"], "func": f31_rcmf_112_days_since_roc_252d_max_1260d},
    "f31_rcmf_113_days_since_roc_21d_min_63d": {"inputs": ["close"], "func": f31_rcmf_113_days_since_roc_21d_min_63d},
    "f31_rcmf_114_roc_5d_max_in_21d": {"inputs": ["close"], "func": f31_rcmf_114_roc_5d_max_in_21d},
    "f31_rcmf_115_roc_5d_decay_from_21d_max": {"inputs": ["close"], "func": f31_rcmf_115_roc_5d_decay_from_21d_max},
    "f31_rcmf_116_log_return_252d_decay_from_1260d_max": {"inputs": ["close"], "func": f31_rcmf_116_log_return_252d_decay_from_1260d_max},
    "f31_rcmf_117_roc_21d_amplitude_252d": {"inputs": ["close"], "func": f31_rcmf_117_roc_21d_amplitude_252d},
    "f31_rcmf_118_roc_63d_amplitude_504d": {"inputs": ["close"], "func": f31_rcmf_118_roc_63d_amplitude_504d},
    "f31_rcmf_119_roc_21d_position_in_252d_range": {"inputs": ["close"], "func": f31_rcmf_119_roc_21d_position_in_252d_range},
    "f31_rcmf_120_roc_63d_position_in_504d_range": {"inputs": ["close"], "func": f31_rcmf_120_roc_63d_position_in_504d_range},
    "f31_rcmf_121_roc_21d_smoothed_5d": {"inputs": ["close"], "func": f31_rcmf_121_roc_21d_smoothed_5d},
    "f31_rcmf_122_roc_63d_smoothed_21d": {"inputs": ["close"], "func": f31_rcmf_122_roc_63d_smoothed_21d},
    "f31_rcmf_123_roc_252d_smoothed_63d": {"inputs": ["close"], "func": f31_rcmf_123_roc_252d_smoothed_63d},
    "f31_rcmf_124_roc_21d_acceleration_5d": {"inputs": ["close"], "func": f31_rcmf_124_roc_21d_acceleration_5d},
    "f31_rcmf_125_roc_63d_acceleration_21d": {"inputs": ["close"], "func": f31_rcmf_125_roc_63d_acceleration_21d},
    "f31_rcmf_126_roc_252d_acceleration_63d": {"inputs": ["close"], "func": f31_rcmf_126_roc_252d_acceleration_63d},
    "f31_rcmf_127_roc_21d_slope_21d": {"inputs": ["close"], "func": f31_rcmf_127_roc_21d_slope_21d},
    "f31_rcmf_128_roc_63d_slope_63d": {"inputs": ["close"], "func": f31_rcmf_128_roc_63d_slope_63d},
    "f31_rcmf_129_roc_252d_slope_252d": {"inputs": ["close"], "func": f31_rcmf_129_roc_252d_slope_252d},
    "f31_rcmf_130_roc_sign_change_count_21d": {"inputs": ["close"], "func": f31_rcmf_130_roc_sign_change_count_21d},
    "f31_rcmf_131_roc_sign_change_count_63d": {"inputs": ["close"], "func": f31_rcmf_131_roc_sign_change_count_63d},
    "f31_rcmf_132_consecutive_positive_1d_streak": {"inputs": ["close"], "func": f31_rcmf_132_consecutive_positive_1d_streak},
    "f31_rcmf_133_consecutive_negative_1d_streak": {"inputs": ["close"], "func": f31_rcmf_133_consecutive_negative_1d_streak},
    "f31_rcmf_134_roc_21d_persistence_positive_5d": {"inputs": ["close"], "func": f31_rcmf_134_roc_21d_persistence_positive_5d},
    "f31_rcmf_135_roc_63d_persistence_negative_21d": {"inputs": ["close"], "func": f31_rcmf_135_roc_63d_persistence_negative_21d},
    "f31_rcmf_136_vol_of_1d_returns_21d": {"inputs": ["close"], "func": f31_rcmf_136_vol_of_1d_returns_21d},
    "f31_rcmf_137_vol_of_1d_returns_63d": {"inputs": ["close"], "func": f31_rcmf_137_vol_of_1d_returns_63d},
    "f31_rcmf_138_vol_of_21d_roc_252d": {"inputs": ["close"], "func": f31_rcmf_138_vol_of_21d_roc_252d},
    "f31_rcmf_139_vol_of_63d_roc_504d": {"inputs": ["close"], "func": f31_rcmf_139_vol_of_63d_roc_504d},
    "f31_rcmf_140_vol_of_vol_1d_returns": {"inputs": ["close"], "func": f31_rcmf_140_vol_of_vol_1d_returns},
    "f31_rcmf_141_roc_21d_drawdown_252d": {"inputs": ["close"], "func": f31_rcmf_141_roc_21d_drawdown_252d},
    "f31_rcmf_142_first_negative_roc_21d_after_positive_extreme": {"inputs": ["close"], "func": f31_rcmf_142_first_negative_roc_21d_after_positive_extreme},
    "f31_rcmf_143_roc_21d_half_life_decay_proxy": {"inputs": ["close"], "func": f31_rcmf_143_roc_21d_half_life_decay_proxy},
    "f31_rcmf_144_recovery_speed_from_roc_21d_min": {"inputs": ["close"], "func": f31_rcmf_144_recovery_speed_from_roc_21d_min},
    "f31_rcmf_145_roc_composite_index": {"inputs": ["close"], "func": f31_rcmf_145_roc_composite_index},
    "f31_rcmf_146_roc_21d_above_long_run_mean_indicator": {"inputs": ["close"], "func": f31_rcmf_146_roc_21d_above_long_run_mean_indicator},
    "f31_rcmf_147_roc_63d_dwell_above_zero_252d": {"inputs": ["close"], "func": f31_rcmf_147_roc_63d_dwell_above_zero_252d},
    "f31_rcmf_148_roc_252d_dwell_above_zero_1260d": {"inputs": ["close"], "func": f31_rcmf_148_roc_252d_dwell_above_zero_1260d},
    "f31_rcmf_149_acceleration_to_volatility_ratio_21d": {"inputs": ["close"], "func": f31_rcmf_149_acceleration_to_volatility_ratio_21d},
    "f31_rcmf_150_post_peak_decay_speed_21d": {"inputs": ["close"], "func": f31_rcmf_150_post_peak_decay_speed_21d},
}
