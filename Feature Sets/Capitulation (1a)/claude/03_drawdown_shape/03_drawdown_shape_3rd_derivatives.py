"""
03_drawdown_shape — 3rd Derivatives (Features drv3_001 to drv3_025)
Domain: rate-of-change of 2nd-derivative shape concepts — captures exhaustion /
inflection signals in the geometry of the decline (jerk of curvature, entropy
of acceleration, etc.).
Asset class: US equities | Daily OHLCV only (SEP folder).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_YEAR = 252
_QTR = 63
_MO = 21
_WK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _roll_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _roll_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _roll_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _roll_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _roll_slope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope."""
    def _slope(y):
        n = len(y)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float) - (n - 1) / 2.0
        denom = np.dot(xi, xi)
        return np.dot(xi, y) / denom if denom > _EPS else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


def _roll_r2(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS R^2."""
    def _r2(y):
        n = len(y)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi -= xi.mean()
        yi = y - y.mean()
        ss_tot = np.dot(yi, yi)
        if ss_tot < _EPS:
            return 1.0
        denom = np.dot(xi, xi)
        if denom < _EPS:
            return np.nan
        b = np.dot(xi, yi) / denom
        ss_res = ss_tot - b * np.dot(xi, yi)
        return max(0.0, 1.0 - ss_res / ss_tot)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_r2, raw=True)


def _roll_quad_coef(s: pd.Series, w: int) -> pd.Series:
    """Rolling quadratic coefficient."""
    def _quad(y):
        n = len(y)
        if n < 3:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            return np.polyfit(x, y, 2)[0]
        except Exception:
            return np.nan
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_quad, raw=True)


def _roll_lin_rmse(s: pd.Series, w: int) -> pd.Series:
    """Rolling RMSE of linear fit."""
    def _lrmse(y):
        n = len(y)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), y.mean()
        xi = x - xm
        denom = np.dot(xi, xi)
        b = np.dot(xi, y - ym) / denom if denom > _EPS else 0.0
        a = ym - b * xm
        return np.sqrt(np.mean((y - (a + b * x)) ** 2))
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_lrmse, raw=True)


def _roll_autocorr(s: pd.Series, w: int, lag: int = 1) -> pd.Series:
    """Rolling autocorrelation at given lag."""
    def _ac(y):
        n = len(y)
        if n <= lag:
            return np.nan
        y1 = y[:-lag] - y[:-lag].mean()
        y2 = y[lag:] - y[lag:].mean()
        d1 = np.dot(y1, y1)
        d2 = np.dot(y2, y2)
        denom = np.sqrt(d1 * d2)
        return np.dot(y1, y2) / denom if denom > _EPS else np.nan
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).apply(_ac, raw=True)


# ── Helper: build the 2nd-derivative series from base shape concepts ──────────
# Each helper returns the same quantity as the drv2 file counterpart, defined
# locally so this file is self-contained.

def _base_quad_coef_63d(close: pd.Series) -> pd.Series:
    return _roll_quad_coef(close, 63)

def _base_linear_r2_63d(close: pd.Series) -> pd.Series:
    return _roll_r2(close, 63)

def _base_jaggedness_21d(close: pd.Series) -> pd.Series:
    arc = close.diff().abs().rolling(21, min_periods=10).sum()
    chord = (close - close.shift(20)).abs()
    return _safe_div(arc, chord)

def _base_jaggedness_63d(close: pd.Series) -> pd.Series:
    arc = close.diff().abs().rolling(63, min_periods=30).sum()
    chord = (close - close.shift(62)).abs()
    return _safe_div(arc, chord)

def _base_v_shape_63d(close: pd.Series) -> pd.Series:
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
        s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        return s1 - s2
    return close.rolling(63, min_periods=30).apply(_v, raw=True)

def _base_rounded_bottom_63d(close: pd.Series) -> pd.Series:
    qc = _roll_quad_coef(close, 63)
    rng = _roll_max(close, 63) - _roll_min(close, 63)
    return _safe_div(qc, rng)

def _base_drawdown_convexity_63d(close: pd.Series) -> pd.Series:
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _safe_div(dd.rolling(63, min_periods=30).mean(),
                     dd.rolling(63, min_periods=30).max())

def _base_drawdown_r2_63d(close: pd.Series) -> pd.Series:
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_r2(dd, 63)

def _base_return_skew_63d(close: pd.Series) -> pd.Series:
    return close.pct_change().rolling(63, min_periods=20).skew()

def _base_return_kurt_63d(close: pd.Series) -> pd.Series:
    return close.pct_change().rolling(63, min_periods=20).kurt()

def _base_stair_step_ratio_63d(close: pd.Series) -> pd.Series:
    dc = close.diff()
    std = _roll_std(dc, 63)
    big = (dc.abs() > 1.5 * std).astype(float)
    return big.rolling(63, min_periods=30).mean()

def _base_plateau_fraction_63d(close: pd.Series) -> pd.Series:
    dc = close.diff()
    std = _roll_std(dc, 63)
    flat = (dc.abs() < 0.25 * std).astype(float)
    return flat.rolling(63, min_periods=30).mean()

def _base_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    return _roll_autocorr(close.pct_change(), 63, lag=1)

def _base_lower_low_frac_63d(low: pd.Series) -> pd.Series:
    ll = (low < low.shift(1)).astype(float)
    return ll.rolling(63, min_periods=30).mean()

def _base_midpoint_vs_linear_63d(close: pd.Series) -> pd.Series:
    def _mid_dev(y):
        n = len(y)
        if n < 3:
            return np.nan
        lin = np.linspace(y[0], y[-1], n)
        return y[n // 2] - lin[n // 2]
    return close.rolling(63, min_periods=30).apply(_mid_dev, raw=True)

def _base_drawdown_quad_coef_63d(close: pd.Series) -> pd.Series:
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_quad_coef(dd, 63)

def _base_vol_surge_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dc = close.diff()
    down_v = volume.where(dc < 0)
    up_v = volume.where(dc > 0)
    mean_d = down_v.rolling(63, min_periods=20).mean()
    mean_u = up_v.rolling(63, min_periods=20).mean()
    return _safe_div(mean_d, mean_u)

def _base_hl_range_quad_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    rng = high - low
    return _roll_quad_coef(rng, 63)


# ── 3rd-derivative feature functions ─────────────────────────────────────────
# Pattern: compute 2nd-derivative (diff(5) of base), then diff(5) again to get
# the 3rd derivative — the rate of change of acceleration.

def dsh_drv3_001_quad_coef_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of 63d quadratic coefficient: diff(5) applied twice to curvature —
    detects exhaustion of curvature acceleration."""
    d2 = _base_quad_coef_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_002_linear_r2_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of 63d linear R^2 change — does the change in linearity itself
    reverse (inflection of path regularity)."""
    d2 = _base_linear_r2_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_003_jaggedness_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of 21d jaggedness — is the acceleration of path choppiness itself
    reversing."""
    d2 = _base_jaggedness_21d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_004_jaggedness_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of 63d jaggedness."""
    d2 = _base_jaggedness_63d(close).diff(10)
    return d2.diff(5)


def dsh_drv3_005_v_shape_score_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of V-shape descent score (63d)."""
    d2 = _base_v_shape_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_006_rounded_bottom_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of rounded-bottom score (63d) — third-order inflection of convexity."""
    d2 = _base_rounded_bottom_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_007_drawdown_convexity_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of drawdown convexity (mean/max drawdown ratio, 63d)."""
    d2 = _base_drawdown_convexity_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_008_drawdown_r2_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of drawdown-path linear R^2 (63d)."""
    d2 = _base_drawdown_r2_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_009_return_skew_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of return skewness (63d) — third-order movement of tail asymmetry."""
    d2 = _base_return_skew_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_010_return_kurt_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of return kurtosis (63d)."""
    d2 = _base_return_kurt_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_011_stair_step_ratio_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of stair-step density (63d) — third-order exhaustion of step-down
    cadence."""
    d2 = _base_stair_step_ratio_63d(close).diff(10)
    return d2.diff(5)


def dsh_drv3_012_plateau_fraction_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of plateau fraction (63d)."""
    d2 = _base_plateau_fraction_63d(close).diff(10)
    return d2.diff(5)


def dsh_drv3_013_autocorr_lag1_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of lag-1 return autocorrelation (63d) — third-order momentum
    structure shift."""
    d2 = _base_autocorr_lag1_63d(close).diff(10)
    return d2.diff(5)


def dsh_drv3_014_lower_low_frac_63d_jerk(low: pd.Series) -> pd.Series:
    """Jerk of lower-low fraction (63d) — inflection of structural weakness
    intensification."""
    d2 = _base_lower_low_frac_63d(low).diff(5)
    return d2.diff(5)


def dsh_drv3_015_midpoint_vs_linear_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of midpoint-vs-linear deviation (63d)."""
    d2 = _base_midpoint_vs_linear_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_016_drawdown_quad_coef_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of quadratic coefficient of the drawdown path (63d)."""
    d2 = _base_drawdown_quad_coef_63d(close).diff(5)
    return d2.diff(5)


def dsh_drv3_017_vol_surge_63d_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jerk of down-day vs up-day volume ratio (63d) — is the panic-volume
    surge itself decelerating (exhaustion signal)."""
    d2 = _base_vol_surge_63d(close, volume).diff(10)
    return d2.diff(5)


def dsh_drv3_018_hl_range_quad_63d_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """Jerk of H-L range quadratic coefficient (63d)."""
    d2 = _base_hl_range_quad_63d(high, low).diff(5)
    return d2.diff(5)


def dsh_drv3_019_slope_jerk_21d(close: pd.Series) -> pd.Series:
    """Third derivative of the 21d slope of close: diff(5) of [diff(5) of slope]
    — jerk of the linear trend."""
    slope = _roll_slope(close, 21)
    d2 = slope.diff(5)
    return d2.diff(5)


def dsh_drv3_020_slope_jerk_63d(close: pd.Series) -> pd.Series:
    """Third derivative of the 63d slope of close."""
    slope = _roll_slope(close, 63)
    d2 = slope.diff(5)
    return d2.diff(5)


def dsh_drv3_021_drawdown_convexity_slope_jerk(close: pd.Series) -> pd.Series:
    """5-day change of [5-day slope of drawdown convexity (63d)] — captures
    inflection of the convexity trend itself."""
    base = _base_drawdown_convexity_63d(close)
    slope_of_base = _roll_slope(base, 21)
    d2 = slope_of_base.diff(5)
    return d2.diff(5)


def dsh_drv3_022_return_skew_slope_jerk(close: pd.Series) -> pd.Series:
    """Jerk via rolling slope of the skewness series (63d)."""
    base = _base_return_skew_63d(close)
    slope_of_base = _roll_slope(base, 21)
    d2 = slope_of_base.diff(5)
    return d2.diff(5)


def dsh_drv3_023_jaggedness_slope_jerk(close: pd.Series) -> pd.Series:
    """Jerk of the rolling slope of 63d jaggedness — detects inflection in
    path-choppiness trend."""
    base = _base_jaggedness_63d(close)
    slope_of_base = _roll_slope(base, 21)
    d2 = slope_of_base.diff(5)
    return d2.diff(5)


def dsh_drv3_024_vol_surge_slope_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jerk of rolling slope of down/up volume ratio (63d) — exhaustion of
    volume panic."""
    base = _base_vol_surge_63d(close, volume)
    slope_of_base = _roll_slope(base, 21)
    d2 = slope_of_base.diff(5)
    return d2.diff(5)


def dsh_drv3_025_r2_slope_jerk(close: pd.Series) -> pd.Series:
    """Jerk of rolling slope of 63d linear R^2 — detects whether the path-
    regularity trend is reaching its own inflection point."""
    base = _base_linear_r2_63d(close)
    slope_of_base = _roll_slope(base, 21)
    d2 = slope_of_base.diff(5)
    return d2.diff(5)


# ── Registry ───────────────────────────────────────────────────────────────────

DRAWDOWN_SHAPE_REGISTRY_3RD_DERIVATIVES = {
    "dsh_drv3_001_quad_coef_63d_jerk":              {"inputs": ["close"],           "func": dsh_drv3_001_quad_coef_63d_jerk},
    "dsh_drv3_002_linear_r2_63d_jerk":              {"inputs": ["close"],           "func": dsh_drv3_002_linear_r2_63d_jerk},
    "dsh_drv3_003_jaggedness_21d_jerk":             {"inputs": ["close"],           "func": dsh_drv3_003_jaggedness_21d_jerk},
    "dsh_drv3_004_jaggedness_63d_jerk":             {"inputs": ["close"],           "func": dsh_drv3_004_jaggedness_63d_jerk},
    "dsh_drv3_005_v_shape_score_63d_jerk":          {"inputs": ["close"],           "func": dsh_drv3_005_v_shape_score_63d_jerk},
    "dsh_drv3_006_rounded_bottom_63d_jerk":         {"inputs": ["close"],           "func": dsh_drv3_006_rounded_bottom_63d_jerk},
    "dsh_drv3_007_drawdown_convexity_63d_jerk":     {"inputs": ["close"],           "func": dsh_drv3_007_drawdown_convexity_63d_jerk},
    "dsh_drv3_008_drawdown_r2_63d_jerk":            {"inputs": ["close"],           "func": dsh_drv3_008_drawdown_r2_63d_jerk},
    "dsh_drv3_009_return_skew_63d_jerk":            {"inputs": ["close"],           "func": dsh_drv3_009_return_skew_63d_jerk},
    "dsh_drv3_010_return_kurt_63d_jerk":            {"inputs": ["close"],           "func": dsh_drv3_010_return_kurt_63d_jerk},
    "dsh_drv3_011_stair_step_ratio_63d_jerk":       {"inputs": ["close"],           "func": dsh_drv3_011_stair_step_ratio_63d_jerk},
    "dsh_drv3_012_plateau_fraction_63d_jerk":       {"inputs": ["close"],           "func": dsh_drv3_012_plateau_fraction_63d_jerk},
    "dsh_drv3_013_autocorr_lag1_63d_jerk":          {"inputs": ["close"],           "func": dsh_drv3_013_autocorr_lag1_63d_jerk},
    "dsh_drv3_014_lower_low_frac_63d_jerk":         {"inputs": ["low"],             "func": dsh_drv3_014_lower_low_frac_63d_jerk},
    "dsh_drv3_015_midpoint_vs_linear_63d_jerk":     {"inputs": ["close"],           "func": dsh_drv3_015_midpoint_vs_linear_63d_jerk},
    "dsh_drv3_016_drawdown_quad_coef_63d_jerk":     {"inputs": ["close"],           "func": dsh_drv3_016_drawdown_quad_coef_63d_jerk},
    "dsh_drv3_017_vol_surge_63d_jerk":              {"inputs": ["close", "volume"], "func": dsh_drv3_017_vol_surge_63d_jerk},
    "dsh_drv3_018_hl_range_quad_63d_jerk":          {"inputs": ["high", "low"],     "func": dsh_drv3_018_hl_range_quad_63d_jerk},
    "dsh_drv3_019_slope_jerk_21d":                  {"inputs": ["close"],           "func": dsh_drv3_019_slope_jerk_21d},
    "dsh_drv3_020_slope_jerk_63d":                  {"inputs": ["close"],           "func": dsh_drv3_020_slope_jerk_63d},
    "dsh_drv3_021_drawdown_convexity_slope_jerk":   {"inputs": ["close"],           "func": dsh_drv3_021_drawdown_convexity_slope_jerk},
    "dsh_drv3_022_return_skew_slope_jerk":          {"inputs": ["close"],           "func": dsh_drv3_022_return_skew_slope_jerk},
    "dsh_drv3_023_jaggedness_slope_jerk":           {"inputs": ["close"],           "func": dsh_drv3_023_jaggedness_slope_jerk},
    "dsh_drv3_024_vol_surge_slope_jerk":            {"inputs": ["close", "volume"], "func": dsh_drv3_024_vol_surge_slope_jerk},
    "dsh_drv3_025_r2_slope_jerk":                   {"inputs": ["close"],           "func": dsh_drv3_025_r2_slope_jerk},
}
