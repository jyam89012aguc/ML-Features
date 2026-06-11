"""semi_variance_asymmetry d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Every feature
in this family answers the question: *are the up moves and the down moves
different in size, frequency, or shape?* Concepts span downside/upside
semi-variance, semi-deviation ratios, Sortino-style risk-adjusted returns,
moment-based skewness, quantile (Bowley/Kelly) skewness, kurtosis, sign-
conditioned volatility, win/loss frequency, gain/loss magnitude asymmetry,
tail/drawdown asymmetry, volume-conditioned sign asymmetry, sign-aware
autocorrelation, and bar-shape (upper-wick vs lower-wick) asymmetry.

Symmetric realized volatility (no sign split) is OWNED by family 35 and is
absent here. Range-based estimators (Parkinson, GK, RS, YZ) are owned by
family 37 and are absent here.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(N). Self-contained helpers — no
cross-family imports.
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
    """Replace non-negative returns with 0 (preserves NaN)."""
    return r.where(r < 0, 0.0)


def _pos_part(r: pd.Series) -> pd.Series:
    """Replace non-positive returns with 0 (preserves NaN)."""
    return r.where(r > 0, 0.0)


def _when_neg(r: pd.Series) -> pd.Series:
    """Mask out non-negative returns to NaN (preserves NaN)."""
    return r.where(r < 0)


def _when_pos(r: pd.Series) -> pd.Series:
    """Mask out non-positive returns to NaN (preserves NaN)."""
    return r.where(r > 0)


# ============================================================
# Bucket A — Downside semi-variance, multi-horizon (001-008)
# Each horizon = different downside-risk-regime hypothesis.
# ============================================================

def f36_svas_001_downside_semivariance_21d(close: pd.Series) -> pd.Series:
    """Downside semi-variance (Markowitz lower partial moment, MAR=0) over trailing 21d — monthly downside risk."""
    r = _log_returns(close)
    return (_neg_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()


def f36_svas_002_downside_semivariance_63d(close: pd.Series) -> pd.Series:
    """Downside semi-variance over trailing 63d — quarterly downside regime."""
    r = _log_returns(close)
    return (_neg_part(r) ** 2).rolling(QDAYS, min_periods=MDAYS).mean()


def f36_svas_003_downside_semivariance_126d(close: pd.Series) -> pd.Series:
    """Downside semi-variance over trailing 126d — half-year downside regime."""
    r = _log_returns(close)
    return (_neg_part(r) ** 2).rolling(126, min_periods=QDAYS).mean()


def f36_svas_004_downside_semivariance_252d(close: pd.Series) -> pd.Series:
    """Downside semi-variance over trailing 252d — annual downside regime."""
    r = _log_returns(close)
    return (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_005_downside_semivariance_504d(close: pd.Series) -> pd.Series:
    """Downside semi-variance over trailing 504d — biennial downside regime."""
    r = _log_returns(close)
    return (_neg_part(r) ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f36_svas_006_downside_semideviation_252d(close: pd.Series) -> pd.Series:
    """Annual downside semi-deviation (sqrt of semi-variance) — vol-units form."""
    r = _log_returns(close)
    return np.sqrt((_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())


def f36_svas_007_log_downside_semivariance_252d(close: pd.Series) -> pd.Series:
    """log(downside semi-variance + eps) at 252d — heavy-tail-friendly scale."""
    r = _log_returns(close)
    sv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return np.log(sv + 1e-12).where(sv > 0, np.nan)


def f36_svas_008_conditional_downside_variance_252d(close: pd.Series) -> pd.Series:
    """Conditional variance of negative returns ONLY (denominator = count of negatives, not N)."""
    r = _log_returns(close)
    rn = _when_neg(r)
    return (rn ** 2).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket B — Upside semi-variance, multi-horizon (009-016)
# Symmetric counterparts of A. The TWIST is that for short-side
# "stuck" peaks, an unusually high upside semi-var late in a run can
# itself be a topping signal (blowoff-up vol).
# ============================================================

def f36_svas_009_upside_semivariance_21d(close: pd.Series) -> pd.Series:
    """Upside semi-variance (positive returns only, MAR=0) trailing 21d — monthly upside churn."""
    r = _log_returns(close)
    return (_pos_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()


def f36_svas_010_upside_semivariance_63d(close: pd.Series) -> pd.Series:
    """Upside semi-variance over trailing 63d — quarterly upside regime."""
    r = _log_returns(close)
    return (_pos_part(r) ** 2).rolling(QDAYS, min_periods=MDAYS).mean()


def f36_svas_011_upside_semivariance_126d(close: pd.Series) -> pd.Series:
    """Upside semi-variance over trailing 126d — half-year upside regime."""
    r = _log_returns(close)
    return (_pos_part(r) ** 2).rolling(126, min_periods=QDAYS).mean()


def f36_svas_012_upside_semivariance_252d(close: pd.Series) -> pd.Series:
    """Upside semi-variance over trailing 252d — annual upside regime."""
    r = _log_returns(close)
    return (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_013_upside_semivariance_504d(close: pd.Series) -> pd.Series:
    """Upside semi-variance over trailing 504d — biennial upside regime."""
    r = _log_returns(close)
    return (_pos_part(r) ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f36_svas_014_upside_semideviation_252d(close: pd.Series) -> pd.Series:
    """Annual upside semi-deviation (sqrt of upside semi-var) — vol-units form."""
    r = _log_returns(close)
    return np.sqrt((_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())


def f36_svas_015_log_upside_semivariance_252d(close: pd.Series) -> pd.Series:
    """log(upside semi-variance + eps) at 252d — heavy-tail-friendly scale."""
    r = _log_returns(close)
    sv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return np.log(sv + 1e-12).where(sv > 0, np.nan)


def f36_svas_016_conditional_upside_variance_252d(close: pd.Series) -> pd.Series:
    """Conditional variance of positive returns ONLY (denominator = count of positives)."""
    r = _log_returns(close)
    rp = _when_pos(r)
    return (rp ** 2).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket C — Semi-variance and semi-deviation ratios (017-026)
# Relative measures of down vs up.
# ============================================================

def f36_svas_017_semivar_ratio_down_over_up_21d(close: pd.Series) -> pd.Series:
    """Downside / upside semi-variance at 21d — short-horizon asymmetry index."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(dv, uv)


def f36_svas_018_semivar_ratio_down_over_up_63d(close: pd.Series) -> pd.Series:
    """Downside / upside semi-variance at 63d — quarter-horizon asymmetry."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(dv, uv)


def f36_svas_019_semivar_ratio_down_over_up_252d(close: pd.Series) -> pd.Series:
    """Downside / upside semi-variance at 252d — annual asymmetry regime."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(dv, uv)


def f36_svas_020_semivar_ratio_up_over_down_252d(close: pd.Series) -> pd.Series:
    """Upside / downside semi-variance at 252d — inverse asymmetry (high = upside-dominant)."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(uv, dv)


def f36_svas_021_log_semivar_ratio_down_up_252d(close: pd.Series) -> pd.Series:
    """log(downside / upside semi-variance) at 252d — symmetric scale, zero = balanced."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return np.log(_safe_div(dv, uv))


def f36_svas_022_downside_share_of_total_variance_21d(close: pd.Series) -> pd.Series:
    """Downside semi-variance / total variance at 21d — what fraction of vol is downside?"""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    tv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(dv, tv)


def f36_svas_023_downside_share_of_total_variance_252d(close: pd.Series) -> pd.Series:
    """Downside semi-variance / total variance at 252d — annual downside-share regime."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    tv = (r ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(dv, tv)


def f36_svas_024_semivar_delta_down_minus_up_252d(close: pd.Series) -> pd.Series:
    """Downside MINUS upside semi-variance at 252d — additive (not ratio) asymmetry."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return dv - uv


def f36_svas_025_normalized_asymmetry_index_252d(close: pd.Series) -> pd.Series:
    """(dv - uv) / (dv + uv) at 252d — bounded asymmetry index in [-1, 1]."""
    r = _log_returns(close)
    dv = (_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    uv = (_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(dv - uv, dv + uv)


def f36_svas_026_semideviation_ratio_down_over_up_252d(close: pd.Series) -> pd.Series:
    """sqrt(down semi-var) / sqrt(up semi-var) at 252d — semi-deviation form of the ratio."""
    r = _log_returns(close)
    dd = np.sqrt((_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    ud = np.sqrt((_pos_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(dd, ud)


# ============================================================
# Bucket D — Sortino-style risk-adjusted returns (027-032)
# Mean return divided by downside risk (not symmetric vol).
# ============================================================

def f36_svas_027_sortino_21d(close: pd.Series) -> pd.Series:
    """Mean return / downside semi-deviation at 21d — monthly Sortino ratio (MAR=0)."""
    r = _log_returns(close)
    mr = r.rolling(MDAYS, min_periods=WDAYS).mean()
    dd = np.sqrt((_neg_part(r) ** 2).rolling(MDAYS, min_periods=WDAYS).mean())
    return _safe_div(mr, dd)


def f36_svas_028_sortino_63d(close: pd.Series) -> pd.Series:
    """Mean return / downside semi-deviation at 63d — quarterly Sortino."""
    r = _log_returns(close)
    mr = r.rolling(QDAYS, min_periods=MDAYS).mean()
    dd = np.sqrt((_neg_part(r) ** 2).rolling(QDAYS, min_periods=MDAYS).mean())
    return _safe_div(mr, dd)


def f36_svas_029_sortino_252d(close: pd.Series) -> pd.Series:
    """Mean return / downside semi-deviation at 252d — annual Sortino ratio."""
    r = _log_returns(close)
    mr = r.rolling(YDAYS, min_periods=QDAYS).mean()
    dd = np.sqrt((_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(mr, dd)


def f36_svas_030_upside_potential_ratio_252d(close: pd.Series) -> pd.Series:
    """Mean positive returns / downside semi-deviation at 252d — upside potential vs downside risk."""
    r = _log_returns(close)
    up = _pos_part(r).rolling(YDAYS, min_periods=QDAYS).mean()
    dd = np.sqrt((_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(up, dd)


def f36_svas_031_sortino_minus_sharpe_252d(close: pd.Series) -> pd.Series:
    """Sortino - Sharpe at 252d — direct measure of how much asymmetry inflates the ratio."""
    r = _log_returns(close)
    mr = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    dd = np.sqrt((_neg_part(r) ** 2).rolling(YDAYS, min_periods=QDAYS).mean())
    return _safe_div(mr, dd) - _safe_div(mr, sd)


def f36_svas_032_gain_loss_ratio_lpm_252d(close: pd.Series) -> pd.Series:
    """E[r | r>0] / E[|r| | r<0] at 252d — Bernardo-Ledoit-style gain/loss ratio."""
    r = _log_returns(close)
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(g, l)


# ============================================================
# Bucket E — Pearson moment-based skewness (033-038)
# Third-central-moment / sigma^3 of returns.
# ============================================================

def f36_svas_033_sample_skewness_21d(close: pd.Series) -> pd.Series:
    """Sample skewness of log returns over 21d — short-horizon distributional asymmetry."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).skew()


def f36_svas_034_sample_skewness_63d(close: pd.Series) -> pd.Series:
    """Sample skewness over 63d — quarterly distributional asymmetry."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).skew()


def f36_svas_035_sample_skewness_252d(close: pd.Series) -> pd.Series:
    """Sample skewness over 252d — annual distributional asymmetry regime."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).skew()


def f36_svas_036_sample_skewness_504d(close: pd.Series) -> pd.Series:
    """Sample skewness over 504d — biennial distributional asymmetry."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).skew()


def f36_svas_037_abs_skewness_252d(close: pd.Series) -> pd.Series:
    """|skewness| at 252d — magnitude of asymmetry regardless of sign."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).skew().abs()


def f36_svas_038_skewness_of_squared_returns_252d(close: pd.Series) -> pd.Series:
    """Skewness of squared returns at 252d — asymmetry of the |return| distribution (vol-clumping asymmetry)."""
    r = _log_returns(close)
    return (r ** 2).rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket F — Bowley / quantile-based skewness (039-043)
# Robust to outliers — uses quantiles instead of moments.
# ============================================================

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


def f36_svas_039_bowley_skewness_63d(close: pd.Series) -> pd.Series:
    """Bowley quantile skewness (Q1+Q3-2*Q2)/(Q3-Q1) over 63d — robust quarterly asymmetry."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_bowley_window, raw=True)


def f36_svas_040_bowley_skewness_252d(close: pd.Series) -> pd.Series:
    """Bowley quantile skewness over 252d — robust annual asymmetry."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_bowley_window, raw=True)


def f36_svas_041_bowley_skewness_504d(close: pd.Series) -> pd.Series:
    """Bowley quantile skewness over 504d — robust biennial asymmetry."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_bowley_window, raw=True)


def f36_svas_042_outer_quantile_skew_10_90_252d(close: pd.Series) -> pd.Series:
    """Outer-quantile skewness using 10/90 instead of 25/75 over 252d — tail-leaning asymmetry."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _quantile_skew_window(w, 0.10, 0.90), raw=True
    )


def f36_svas_043_outer_quantile_skew_05_95_252d(close: pd.Series) -> pd.Series:
    """Outer-quantile skewness using 5/95 over 252d — extreme-tail asymmetry."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _quantile_skew_window(w, 0.05, 0.95), raw=True
    )


# ============================================================
# Bucket G — Kelly / median-based skewness (044-048)
# (mean - median) / sigma family — robust mode/mean shift.
# ============================================================

def f36_svas_044_kelly_skewness_21d(close: pd.Series) -> pd.Series:
    """(mean - median) / std at 21d — Kelly's measure of skewness, short horizon."""
    r = _log_returns(close)
    m = r.rolling(MDAYS, min_periods=WDAYS).mean()
    med = r.rolling(MDAYS, min_periods=WDAYS).median()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(m - med, sd)


def f36_svas_045_kelly_skewness_63d(close: pd.Series) -> pd.Series:
    """(mean - median) / std at 63d — Kelly skew, quarterly horizon."""
    r = _log_returns(close)
    m = r.rolling(QDAYS, min_periods=MDAYS).mean()
    med = r.rolling(QDAYS, min_periods=MDAYS).median()
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(m - med, sd)


def f36_svas_046_kelly_skewness_252d(close: pd.Series) -> pd.Series:
    """(mean - median) / std at 252d — Kelly skew, annual horizon."""
    r = _log_returns(close)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    med = r.rolling(YDAYS, min_periods=QDAYS).median()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(m - med, sd)


def f36_svas_047_kelly_skewness_504d(close: pd.Series) -> pd.Series:
    """(mean - median) / std at 504d — Kelly skew, biennial horizon."""
    r = _log_returns(close)
    m = r.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    med = r.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    sd = r.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _safe_div(m - med, sd)


def f36_svas_048_pearson_median_skewness_252d(close: pd.Series) -> pd.Series:
    """3*(mean - median)/std at 252d — Pearson's second skewness coefficient (Kelly × 3)."""
    r = _log_returns(close)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    med = r.rolling(YDAYS, min_periods=QDAYS).median()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(3.0 * (m - med), sd)


# ============================================================
# Bucket H — Sample kurtosis (049-054)
# Tail thickness — pairs with skew to characterise heavy-tail asymmetry.
# ============================================================

def f36_svas_049_excess_kurtosis_21d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log returns over 21d — short-horizon tail thickness."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).kurt()


def f36_svas_050_excess_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis over 63d — quarterly tail thickness."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).kurt()


def f36_svas_051_excess_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis over 252d — annual tail-thickness regime."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).kurt()


def f36_svas_052_excess_kurtosis_504d(close: pd.Series) -> pd.Series:
    """Excess kurtosis over 504d — biennial tail-thickness regime."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).kurt()


def f36_svas_053_log_kurtosis_plus_4_252d(close: pd.Series) -> pd.Series:
    """log(excess kurt + 4) at 252d — scale-compressed kurtosis (kurt+3 is the raw moment; +4 keeps log defined)."""
    r = _log_returns(close)
    k = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    return np.log((k + 4.0).where(k + 4.0 > 0, np.nan))


def f36_svas_054_kurtosis_of_abs_returns_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of |returns| at 252d — concentration of magnitude (vol-cluster severity)."""
    r = _log_returns(close)
    return r.abs().rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket I — Sign-conditioned (asymmetric) volatility (055-062)
# Vol when up vs vol when down — captures the conditional vol asymmetry
# that semi-variance only partially captures.
# ============================================================

def f36_svas_055_std_on_up_days_21d(close: pd.Series) -> pd.Series:
    """std(returns | return > 0) over trailing 21d — short-horizon upside vol."""
    r = _log_returns(close)
    return _when_pos(r).rolling(MDAYS, min_periods=WDAYS).std()


def f36_svas_056_std_on_up_days_252d(close: pd.Series) -> pd.Series:
    """std(returns | return > 0) over trailing 252d — annual upside vol."""
    r = _log_returns(close)
    return _when_pos(r).rolling(YDAYS, min_periods=QDAYS).std()


def f36_svas_057_std_on_down_days_21d(close: pd.Series) -> pd.Series:
    """std(returns | return < 0) over trailing 21d — short-horizon downside vol."""
    r = _log_returns(close)
    return _when_neg(r).rolling(MDAYS, min_periods=WDAYS).std()


def f36_svas_058_std_on_down_days_252d(close: pd.Series) -> pd.Series:
    """std(returns | return < 0) over trailing 252d — annual downside vol."""
    r = _log_returns(close)
    return _when_neg(r).rolling(YDAYS, min_periods=QDAYS).std()


def f36_svas_059_std_ratio_up_over_down_21d(close: pd.Series) -> pd.Series:
    """std(up returns) / std(down returns) at 21d — short-horizon conditional-vol asymmetry."""
    r = _log_returns(close)
    su = _when_pos(r).rolling(MDAYS, min_periods=WDAYS).std()
    sd = _when_neg(r).rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(su, sd)


def f36_svas_060_std_ratio_up_over_down_252d(close: pd.Series) -> pd.Series:
    """std(up returns) / std(down returns) at 252d — annual conditional-vol asymmetry."""
    r = _log_returns(close)
    su = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).std()
    sd = _when_neg(r).rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(su, sd)


def f36_svas_061_log_std_ratio_up_down_252d(close: pd.Series) -> pd.Series:
    """log(std up / std down) at 252d — symmetric scale of conditional-vol asymmetry."""
    r = _log_returns(close)
    su = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).std()
    sd = _when_neg(r).rolling(YDAYS, min_periods=QDAYS).std()
    return np.log(_safe_div(su, sd))


def f36_svas_062_std_delta_down_minus_up_252d(close: pd.Series) -> pd.Series:
    """std(down returns) - std(up returns) at 252d — additive (not ratio) conditional-vol asymmetry."""
    r = _log_returns(close)
    su = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).std()
    sd = _when_neg(r).rolling(YDAYS, min_periods=QDAYS).std()
    return sd - su


# ============================================================
# Bucket J — Win/loss frequency asymmetry (063-067)
# ============================================================

def f36_svas_063_up_down_count_ratio_21d(close: pd.Series) -> pd.Series:
    """count(up days) / count(down days) over 21d — short-horizon frequency asymmetry."""
    r = _log_returns(close)
    nu = (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    nd = (r < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(nu, nd)


def f36_svas_064_up_down_count_ratio_63d(close: pd.Series) -> pd.Series:
    """count(up days) / count(down days) over 63d — quarterly frequency asymmetry."""
    r = _log_returns(close)
    nu = (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    nd = (r < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nu, nd)


def f36_svas_065_up_down_count_ratio_252d(close: pd.Series) -> pd.Series:
    """count(up days) / count(down days) over 252d — annual win/loss frequency."""
    r = _log_returns(close)
    nu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    nd = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(nu, nd)


def f36_svas_066_up_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of days with positive return over 252d — bounded win rate."""
    r = _log_returns(close)
    return (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_067_log_up_down_count_ratio_252d(close: pd.Series) -> pd.Series:
    """log(count up / count down) over 252d — symmetric scale of frequency asymmetry."""
    r = _log_returns(close)
    nu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    nd = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return np.log(_safe_div(nu, nd))


# ============================================================
# Bucket K — Gain/loss magnitude asymmetry (068-075)
# Average size of wins vs average size of losses — distinct from
# semi-variance which is squared-magnitude.
# ============================================================

def f36_svas_068_avg_gain_on_up_days_21d(close: pd.Series) -> pd.Series:
    """E[r | r>0] over 21d — average size of an up day, short horizon."""
    r = _log_returns(close)
    return _when_pos(r).rolling(MDAYS, min_periods=WDAYS).mean()


def f36_svas_069_avg_gain_on_up_days_63d(close: pd.Series) -> pd.Series:
    """E[r | r>0] over 63d — average size of an up day, quarter horizon."""
    r = _log_returns(close)
    return _when_pos(r).rolling(QDAYS, min_periods=MDAYS).mean()


def f36_svas_070_avg_gain_on_up_days_252d(close: pd.Series) -> pd.Series:
    """E[r | r>0] over 252d — average size of an up day, annual horizon."""
    r = _log_returns(close)
    return _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_071_avg_loss_on_down_days_21d(close: pd.Series) -> pd.Series:
    """E[|r| | r<0] over 21d — average size of a down day (positive magnitude), short horizon."""
    r = _log_returns(close)
    return (-_when_neg(r)).rolling(MDAYS, min_periods=WDAYS).mean()


def f36_svas_072_avg_loss_on_down_days_252d(close: pd.Series) -> pd.Series:
    """E[|r| | r<0] over 252d — average size of a down day, annual horizon."""
    r = _log_returns(close)
    return (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()


def f36_svas_073_gain_over_loss_magnitude_252d(close: pd.Series) -> pd.Series:
    """avg gain / avg |loss| at 252d — magnitude-only gain/loss ratio (distinct from Bernardo-Ledoit which uses conditional means; here computed directly via .mean() of masked series)."""
    r = _log_returns(close)
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(g, l)


def f36_svas_074_profit_factor_252d(close: pd.Series) -> pd.Series:
    """sum(gains) / sum(|losses|) at 252d — classical 'profit factor' from systematic trading."""
    r = _log_returns(close)
    g = _pos_part(r).rolling(YDAYS, min_periods=QDAYS).sum()
    l = (-_neg_part(r)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(g, l)


def f36_svas_075_expectancy_252d(close: pd.Series) -> pd.Series:
    """E[r] decomposed: P(up)*avg_gain - P(down)*avg_loss at 252d — trader's expectancy."""
    r = _log_returns(close)
    pu = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    pd_ = (r < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    g = _when_pos(r).rolling(YDAYS, min_periods=QDAYS).mean()
    l = (-_when_neg(r)).rolling(YDAYS, min_periods=QDAYS).mean()
    return pu * g - pd_ * l


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f36_svas_001_downside_semivariance_21d_d1(close):
    return f36_svas_001_downside_semivariance_21d(close).diff()


def f36_svas_002_downside_semivariance_63d_d1(close):
    return f36_svas_002_downside_semivariance_63d(close).diff()


def f36_svas_003_downside_semivariance_126d_d1(close):
    return f36_svas_003_downside_semivariance_126d(close).diff()


def f36_svas_004_downside_semivariance_252d_d1(close):
    return f36_svas_004_downside_semivariance_252d(close).diff()


def f36_svas_005_downside_semivariance_504d_d1(close):
    return f36_svas_005_downside_semivariance_504d(close).diff()


def f36_svas_006_downside_semideviation_252d_d1(close):
    return f36_svas_006_downside_semideviation_252d(close).diff()


def f36_svas_007_log_downside_semivariance_252d_d1(close):
    return f36_svas_007_log_downside_semivariance_252d(close).diff()


def f36_svas_008_conditional_downside_variance_252d_d1(close):
    return f36_svas_008_conditional_downside_variance_252d(close).diff()


def f36_svas_009_upside_semivariance_21d_d1(close):
    return f36_svas_009_upside_semivariance_21d(close).diff()


def f36_svas_010_upside_semivariance_63d_d1(close):
    return f36_svas_010_upside_semivariance_63d(close).diff()


def f36_svas_011_upside_semivariance_126d_d1(close):
    return f36_svas_011_upside_semivariance_126d(close).diff()


def f36_svas_012_upside_semivariance_252d_d1(close):
    return f36_svas_012_upside_semivariance_252d(close).diff()


def f36_svas_013_upside_semivariance_504d_d1(close):
    return f36_svas_013_upside_semivariance_504d(close).diff()


def f36_svas_014_upside_semideviation_252d_d1(close):
    return f36_svas_014_upside_semideviation_252d(close).diff()


def f36_svas_015_log_upside_semivariance_252d_d1(close):
    return f36_svas_015_log_upside_semivariance_252d(close).diff()


def f36_svas_016_conditional_upside_variance_252d_d1(close):
    return f36_svas_016_conditional_upside_variance_252d(close).diff()


def f36_svas_017_semivar_ratio_down_over_up_21d_d1(close):
    return f36_svas_017_semivar_ratio_down_over_up_21d(close).diff()


def f36_svas_018_semivar_ratio_down_over_up_63d_d1(close):
    return f36_svas_018_semivar_ratio_down_over_up_63d(close).diff()


def f36_svas_019_semivar_ratio_down_over_up_252d_d1(close):
    return f36_svas_019_semivar_ratio_down_over_up_252d(close).diff()


def f36_svas_020_semivar_ratio_up_over_down_252d_d1(close):
    return f36_svas_020_semivar_ratio_up_over_down_252d(close).diff()


def f36_svas_021_log_semivar_ratio_down_up_252d_d1(close):
    return f36_svas_021_log_semivar_ratio_down_up_252d(close).diff()


def f36_svas_022_downside_share_of_total_variance_21d_d1(close):
    return f36_svas_022_downside_share_of_total_variance_21d(close).diff()


def f36_svas_023_downside_share_of_total_variance_252d_d1(close):
    return f36_svas_023_downside_share_of_total_variance_252d(close).diff()


def f36_svas_024_semivar_delta_down_minus_up_252d_d1(close):
    return f36_svas_024_semivar_delta_down_minus_up_252d(close).diff()


def f36_svas_025_normalized_asymmetry_index_252d_d1(close):
    return f36_svas_025_normalized_asymmetry_index_252d(close).diff()


def f36_svas_026_semideviation_ratio_down_over_up_252d_d1(close):
    return f36_svas_026_semideviation_ratio_down_over_up_252d(close).diff()


def f36_svas_027_sortino_21d_d1(close):
    return f36_svas_027_sortino_21d(close).diff()


def f36_svas_028_sortino_63d_d1(close):
    return f36_svas_028_sortino_63d(close).diff()


def f36_svas_029_sortino_252d_d1(close):
    return f36_svas_029_sortino_252d(close).diff()


def f36_svas_030_upside_potential_ratio_252d_d1(close):
    return f36_svas_030_upside_potential_ratio_252d(close).diff()


def f36_svas_031_sortino_minus_sharpe_252d_d1(close):
    return f36_svas_031_sortino_minus_sharpe_252d(close).diff()


def f36_svas_032_gain_loss_ratio_lpm_252d_d1(close):
    return f36_svas_032_gain_loss_ratio_lpm_252d(close).diff()


def f36_svas_033_sample_skewness_21d_d1(close):
    return f36_svas_033_sample_skewness_21d(close).diff()


def f36_svas_034_sample_skewness_63d_d1(close):
    return f36_svas_034_sample_skewness_63d(close).diff()


def f36_svas_035_sample_skewness_252d_d1(close):
    return f36_svas_035_sample_skewness_252d(close).diff()


def f36_svas_036_sample_skewness_504d_d1(close):
    return f36_svas_036_sample_skewness_504d(close).diff()


def f36_svas_037_abs_skewness_252d_d1(close):
    return f36_svas_037_abs_skewness_252d(close).diff()


def f36_svas_038_skewness_of_squared_returns_252d_d1(close):
    return f36_svas_038_skewness_of_squared_returns_252d(close).diff()


def f36_svas_039_bowley_skewness_63d_d1(close):
    return f36_svas_039_bowley_skewness_63d(close).diff()


def f36_svas_040_bowley_skewness_252d_d1(close):
    return f36_svas_040_bowley_skewness_252d(close).diff()


def f36_svas_041_bowley_skewness_504d_d1(close):
    return f36_svas_041_bowley_skewness_504d(close).diff()


def f36_svas_042_outer_quantile_skew_10_90_252d_d1(close):
    return f36_svas_042_outer_quantile_skew_10_90_252d(close).diff()


def f36_svas_043_outer_quantile_skew_05_95_252d_d1(close):
    return f36_svas_043_outer_quantile_skew_05_95_252d(close).diff()


def f36_svas_044_kelly_skewness_21d_d1(close):
    return f36_svas_044_kelly_skewness_21d(close).diff()


def f36_svas_045_kelly_skewness_63d_d1(close):
    return f36_svas_045_kelly_skewness_63d(close).diff()


def f36_svas_046_kelly_skewness_252d_d1(close):
    return f36_svas_046_kelly_skewness_252d(close).diff()


def f36_svas_047_kelly_skewness_504d_d1(close):
    return f36_svas_047_kelly_skewness_504d(close).diff()


def f36_svas_048_pearson_median_skewness_252d_d1(close):
    return f36_svas_048_pearson_median_skewness_252d(close).diff()


def f36_svas_049_excess_kurtosis_21d_d1(close):
    return f36_svas_049_excess_kurtosis_21d(close).diff()


def f36_svas_050_excess_kurtosis_63d_d1(close):
    return f36_svas_050_excess_kurtosis_63d(close).diff()


def f36_svas_051_excess_kurtosis_252d_d1(close):
    return f36_svas_051_excess_kurtosis_252d(close).diff()


def f36_svas_052_excess_kurtosis_504d_d1(close):
    return f36_svas_052_excess_kurtosis_504d(close).diff()


def f36_svas_053_log_kurtosis_plus_4_252d_d1(close):
    return f36_svas_053_log_kurtosis_plus_4_252d(close).diff()


def f36_svas_054_kurtosis_of_abs_returns_252d_d1(close):
    return f36_svas_054_kurtosis_of_abs_returns_252d(close).diff()


def f36_svas_055_std_on_up_days_21d_d1(close):
    return f36_svas_055_std_on_up_days_21d(close).diff()


def f36_svas_056_std_on_up_days_252d_d1(close):
    return f36_svas_056_std_on_up_days_252d(close).diff()


def f36_svas_057_std_on_down_days_21d_d1(close):
    return f36_svas_057_std_on_down_days_21d(close).diff()


def f36_svas_058_std_on_down_days_252d_d1(close):
    return f36_svas_058_std_on_down_days_252d(close).diff()


def f36_svas_059_std_ratio_up_over_down_21d_d1(close):
    return f36_svas_059_std_ratio_up_over_down_21d(close).diff()


def f36_svas_060_std_ratio_up_over_down_252d_d1(close):
    return f36_svas_060_std_ratio_up_over_down_252d(close).diff()


def f36_svas_061_log_std_ratio_up_down_252d_d1(close):
    return f36_svas_061_log_std_ratio_up_down_252d(close).diff()


def f36_svas_062_std_delta_down_minus_up_252d_d1(close):
    return f36_svas_062_std_delta_down_minus_up_252d(close).diff()


def f36_svas_063_up_down_count_ratio_21d_d1(close):
    return f36_svas_063_up_down_count_ratio_21d(close).diff()


def f36_svas_064_up_down_count_ratio_63d_d1(close):
    return f36_svas_064_up_down_count_ratio_63d(close).diff()


def f36_svas_065_up_down_count_ratio_252d_d1(close):
    return f36_svas_065_up_down_count_ratio_252d(close).diff()


def f36_svas_066_up_fraction_252d_d1(close):
    return f36_svas_066_up_fraction_252d(close).diff()


def f36_svas_067_log_up_down_count_ratio_252d_d1(close):
    return f36_svas_067_log_up_down_count_ratio_252d(close).diff()


def f36_svas_068_avg_gain_on_up_days_21d_d1(close):
    return f36_svas_068_avg_gain_on_up_days_21d(close).diff()


def f36_svas_069_avg_gain_on_up_days_63d_d1(close):
    return f36_svas_069_avg_gain_on_up_days_63d(close).diff()


def f36_svas_070_avg_gain_on_up_days_252d_d1(close):
    return f36_svas_070_avg_gain_on_up_days_252d(close).diff()


def f36_svas_071_avg_loss_on_down_days_21d_d1(close):
    return f36_svas_071_avg_loss_on_down_days_21d(close).diff()


def f36_svas_072_avg_loss_on_down_days_252d_d1(close):
    return f36_svas_072_avg_loss_on_down_days_252d(close).diff()


def f36_svas_073_gain_over_loss_magnitude_252d_d1(close):
    return f36_svas_073_gain_over_loss_magnitude_252d(close).diff()


def f36_svas_074_profit_factor_252d_d1(close):
    return f36_svas_074_profit_factor_252d(close).diff()


def f36_svas_075_expectancy_252d_d1(close):
    return f36_svas_075_expectancy_252d(close).diff()


SEMI_VARIANCE_ASYMMETRY_D1_REGISTRY_001_075 = {
    "f36_svas_001_downside_semivariance_21d_d1": {"inputs": ["close"], "func": f36_svas_001_downside_semivariance_21d_d1},
    "f36_svas_002_downside_semivariance_63d_d1": {"inputs": ["close"], "func": f36_svas_002_downside_semivariance_63d_d1},
    "f36_svas_003_downside_semivariance_126d_d1": {"inputs": ["close"], "func": f36_svas_003_downside_semivariance_126d_d1},
    "f36_svas_004_downside_semivariance_252d_d1": {"inputs": ["close"], "func": f36_svas_004_downside_semivariance_252d_d1},
    "f36_svas_005_downside_semivariance_504d_d1": {"inputs": ["close"], "func": f36_svas_005_downside_semivariance_504d_d1},
    "f36_svas_006_downside_semideviation_252d_d1": {"inputs": ["close"], "func": f36_svas_006_downside_semideviation_252d_d1},
    "f36_svas_007_log_downside_semivariance_252d_d1": {"inputs": ["close"], "func": f36_svas_007_log_downside_semivariance_252d_d1},
    "f36_svas_008_conditional_downside_variance_252d_d1": {"inputs": ["close"], "func": f36_svas_008_conditional_downside_variance_252d_d1},
    "f36_svas_009_upside_semivariance_21d_d1": {"inputs": ["close"], "func": f36_svas_009_upside_semivariance_21d_d1},
    "f36_svas_010_upside_semivariance_63d_d1": {"inputs": ["close"], "func": f36_svas_010_upside_semivariance_63d_d1},
    "f36_svas_011_upside_semivariance_126d_d1": {"inputs": ["close"], "func": f36_svas_011_upside_semivariance_126d_d1},
    "f36_svas_012_upside_semivariance_252d_d1": {"inputs": ["close"], "func": f36_svas_012_upside_semivariance_252d_d1},
    "f36_svas_013_upside_semivariance_504d_d1": {"inputs": ["close"], "func": f36_svas_013_upside_semivariance_504d_d1},
    "f36_svas_014_upside_semideviation_252d_d1": {"inputs": ["close"], "func": f36_svas_014_upside_semideviation_252d_d1},
    "f36_svas_015_log_upside_semivariance_252d_d1": {"inputs": ["close"], "func": f36_svas_015_log_upside_semivariance_252d_d1},
    "f36_svas_016_conditional_upside_variance_252d_d1": {"inputs": ["close"], "func": f36_svas_016_conditional_upside_variance_252d_d1},
    "f36_svas_017_semivar_ratio_down_over_up_21d_d1": {"inputs": ["close"], "func": f36_svas_017_semivar_ratio_down_over_up_21d_d1},
    "f36_svas_018_semivar_ratio_down_over_up_63d_d1": {"inputs": ["close"], "func": f36_svas_018_semivar_ratio_down_over_up_63d_d1},
    "f36_svas_019_semivar_ratio_down_over_up_252d_d1": {"inputs": ["close"], "func": f36_svas_019_semivar_ratio_down_over_up_252d_d1},
    "f36_svas_020_semivar_ratio_up_over_down_252d_d1": {"inputs": ["close"], "func": f36_svas_020_semivar_ratio_up_over_down_252d_d1},
    "f36_svas_021_log_semivar_ratio_down_up_252d_d1": {"inputs": ["close"], "func": f36_svas_021_log_semivar_ratio_down_up_252d_d1},
    "f36_svas_022_downside_share_of_total_variance_21d_d1": {"inputs": ["close"], "func": f36_svas_022_downside_share_of_total_variance_21d_d1},
    "f36_svas_023_downside_share_of_total_variance_252d_d1": {"inputs": ["close"], "func": f36_svas_023_downside_share_of_total_variance_252d_d1},
    "f36_svas_024_semivar_delta_down_minus_up_252d_d1": {"inputs": ["close"], "func": f36_svas_024_semivar_delta_down_minus_up_252d_d1},
    "f36_svas_025_normalized_asymmetry_index_252d_d1": {"inputs": ["close"], "func": f36_svas_025_normalized_asymmetry_index_252d_d1},
    "f36_svas_026_semideviation_ratio_down_over_up_252d_d1": {"inputs": ["close"], "func": f36_svas_026_semideviation_ratio_down_over_up_252d_d1},
    "f36_svas_027_sortino_21d_d1": {"inputs": ["close"], "func": f36_svas_027_sortino_21d_d1},
    "f36_svas_028_sortino_63d_d1": {"inputs": ["close"], "func": f36_svas_028_sortino_63d_d1},
    "f36_svas_029_sortino_252d_d1": {"inputs": ["close"], "func": f36_svas_029_sortino_252d_d1},
    "f36_svas_030_upside_potential_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_030_upside_potential_ratio_252d_d1},
    "f36_svas_031_sortino_minus_sharpe_252d_d1": {"inputs": ["close"], "func": f36_svas_031_sortino_minus_sharpe_252d_d1},
    "f36_svas_032_gain_loss_ratio_lpm_252d_d1": {"inputs": ["close"], "func": f36_svas_032_gain_loss_ratio_lpm_252d_d1},
    "f36_svas_033_sample_skewness_21d_d1": {"inputs": ["close"], "func": f36_svas_033_sample_skewness_21d_d1},
    "f36_svas_034_sample_skewness_63d_d1": {"inputs": ["close"], "func": f36_svas_034_sample_skewness_63d_d1},
    "f36_svas_035_sample_skewness_252d_d1": {"inputs": ["close"], "func": f36_svas_035_sample_skewness_252d_d1},
    "f36_svas_036_sample_skewness_504d_d1": {"inputs": ["close"], "func": f36_svas_036_sample_skewness_504d_d1},
    "f36_svas_037_abs_skewness_252d_d1": {"inputs": ["close"], "func": f36_svas_037_abs_skewness_252d_d1},
    "f36_svas_038_skewness_of_squared_returns_252d_d1": {"inputs": ["close"], "func": f36_svas_038_skewness_of_squared_returns_252d_d1},
    "f36_svas_039_bowley_skewness_63d_d1": {"inputs": ["close"], "func": f36_svas_039_bowley_skewness_63d_d1},
    "f36_svas_040_bowley_skewness_252d_d1": {"inputs": ["close"], "func": f36_svas_040_bowley_skewness_252d_d1},
    "f36_svas_041_bowley_skewness_504d_d1": {"inputs": ["close"], "func": f36_svas_041_bowley_skewness_504d_d1},
    "f36_svas_042_outer_quantile_skew_10_90_252d_d1": {"inputs": ["close"], "func": f36_svas_042_outer_quantile_skew_10_90_252d_d1},
    "f36_svas_043_outer_quantile_skew_05_95_252d_d1": {"inputs": ["close"], "func": f36_svas_043_outer_quantile_skew_05_95_252d_d1},
    "f36_svas_044_kelly_skewness_21d_d1": {"inputs": ["close"], "func": f36_svas_044_kelly_skewness_21d_d1},
    "f36_svas_045_kelly_skewness_63d_d1": {"inputs": ["close"], "func": f36_svas_045_kelly_skewness_63d_d1},
    "f36_svas_046_kelly_skewness_252d_d1": {"inputs": ["close"], "func": f36_svas_046_kelly_skewness_252d_d1},
    "f36_svas_047_kelly_skewness_504d_d1": {"inputs": ["close"], "func": f36_svas_047_kelly_skewness_504d_d1},
    "f36_svas_048_pearson_median_skewness_252d_d1": {"inputs": ["close"], "func": f36_svas_048_pearson_median_skewness_252d_d1},
    "f36_svas_049_excess_kurtosis_21d_d1": {"inputs": ["close"], "func": f36_svas_049_excess_kurtosis_21d_d1},
    "f36_svas_050_excess_kurtosis_63d_d1": {"inputs": ["close"], "func": f36_svas_050_excess_kurtosis_63d_d1},
    "f36_svas_051_excess_kurtosis_252d_d1": {"inputs": ["close"], "func": f36_svas_051_excess_kurtosis_252d_d1},
    "f36_svas_052_excess_kurtosis_504d_d1": {"inputs": ["close"], "func": f36_svas_052_excess_kurtosis_504d_d1},
    "f36_svas_053_log_kurtosis_plus_4_252d_d1": {"inputs": ["close"], "func": f36_svas_053_log_kurtosis_plus_4_252d_d1},
    "f36_svas_054_kurtosis_of_abs_returns_252d_d1": {"inputs": ["close"], "func": f36_svas_054_kurtosis_of_abs_returns_252d_d1},
    "f36_svas_055_std_on_up_days_21d_d1": {"inputs": ["close"], "func": f36_svas_055_std_on_up_days_21d_d1},
    "f36_svas_056_std_on_up_days_252d_d1": {"inputs": ["close"], "func": f36_svas_056_std_on_up_days_252d_d1},
    "f36_svas_057_std_on_down_days_21d_d1": {"inputs": ["close"], "func": f36_svas_057_std_on_down_days_21d_d1},
    "f36_svas_058_std_on_down_days_252d_d1": {"inputs": ["close"], "func": f36_svas_058_std_on_down_days_252d_d1},
    "f36_svas_059_std_ratio_up_over_down_21d_d1": {"inputs": ["close"], "func": f36_svas_059_std_ratio_up_over_down_21d_d1},
    "f36_svas_060_std_ratio_up_over_down_252d_d1": {"inputs": ["close"], "func": f36_svas_060_std_ratio_up_over_down_252d_d1},
    "f36_svas_061_log_std_ratio_up_down_252d_d1": {"inputs": ["close"], "func": f36_svas_061_log_std_ratio_up_down_252d_d1},
    "f36_svas_062_std_delta_down_minus_up_252d_d1": {"inputs": ["close"], "func": f36_svas_062_std_delta_down_minus_up_252d_d1},
    "f36_svas_063_up_down_count_ratio_21d_d1": {"inputs": ["close"], "func": f36_svas_063_up_down_count_ratio_21d_d1},
    "f36_svas_064_up_down_count_ratio_63d_d1": {"inputs": ["close"], "func": f36_svas_064_up_down_count_ratio_63d_d1},
    "f36_svas_065_up_down_count_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_065_up_down_count_ratio_252d_d1},
    "f36_svas_066_up_fraction_252d_d1": {"inputs": ["close"], "func": f36_svas_066_up_fraction_252d_d1},
    "f36_svas_067_log_up_down_count_ratio_252d_d1": {"inputs": ["close"], "func": f36_svas_067_log_up_down_count_ratio_252d_d1},
    "f36_svas_068_avg_gain_on_up_days_21d_d1": {"inputs": ["close"], "func": f36_svas_068_avg_gain_on_up_days_21d_d1},
    "f36_svas_069_avg_gain_on_up_days_63d_d1": {"inputs": ["close"], "func": f36_svas_069_avg_gain_on_up_days_63d_d1},
    "f36_svas_070_avg_gain_on_up_days_252d_d1": {"inputs": ["close"], "func": f36_svas_070_avg_gain_on_up_days_252d_d1},
    "f36_svas_071_avg_loss_on_down_days_21d_d1": {"inputs": ["close"], "func": f36_svas_071_avg_loss_on_down_days_21d_d1},
    "f36_svas_072_avg_loss_on_down_days_252d_d1": {"inputs": ["close"], "func": f36_svas_072_avg_loss_on_down_days_252d_d1},
    "f36_svas_073_gain_over_loss_magnitude_252d_d1": {"inputs": ["close"], "func": f36_svas_073_gain_over_loss_magnitude_252d_d1},
    "f36_svas_074_profit_factor_252d_d1": {"inputs": ["close"], "func": f36_svas_074_profit_factor_252d_d1},
    "f36_svas_075_expectancy_252d_d1": {"inputs": ["close"], "func": f36_svas_075_expectancy_252d_d1},
}
