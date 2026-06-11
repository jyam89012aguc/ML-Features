"""
03_drawdown_shape — 2nd Derivatives (Features drv2_001 to drv2_025)
Domain: rate-of-change of base shape features — captures acceleration of the
decline geometry (how fast convexity/curvature/jaggedness is evolving).
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


# ── 2nd-derivative feature functions ─────────────────────────────────────────
# Each function computes a base shape metric then takes diff(5) or a rolling
# slope to capture how fast that shape attribute is changing.

def dsh_drv2_001_quad_coef_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in the 63d quadratic coefficient — acceleration of curvature
    reversal (is the parabolic shape of decline sharpening or easing)."""
    base = _roll_quad_coef(close, 63)
    return base.diff(5)


def dsh_drv2_002_quad_coef_126d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in the 126d quadratic coefficient."""
    base = _roll_quad_coef(close, 126)
    return base.diff(5)


def dsh_drv2_003_linear_r2_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in linear R^2 (63d) — is the decline path becoming more or
    less linear (orderly vs disorderly)."""
    base = _roll_r2(close, 63)
    return base.diff(5)


def dsh_drv2_004_linear_r2_126d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in linear R^2 (126d) — longer-horizon linearity velocity."""
    base = _roll_r2(close, 126)
    return base.diff(10)


def dsh_drv2_005_lin_rmse_normed_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in normalised linear RMSE (63d) — is path noise
    increasing or decreasing."""
    rmse = _roll_lin_rmse(close, 63)
    mean_p = _roll_mean(close, 63)
    base = _safe_div(rmse, mean_p)
    return base.diff(5)


def dsh_drv2_006_jaggedness_21d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in arc-length/chord jaggedness (21d) — is the recent path
    becoming choppier or smoother."""
    arc = close.diff().abs().rolling(21, min_periods=10).sum()
    chord = (close - close.shift(20)).abs()
    base = _safe_div(arc, chord)
    return base.diff(5)


def dsh_drv2_007_jaggedness_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in 63d jaggedness."""
    arc = close.diff().abs().rolling(63, min_periods=30).sum()
    chord = (close - close.shift(62)).abs()
    base = _safe_div(arc, chord)
    return base.diff(10)


def dsh_drv2_008_v_shape_score_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in the V-shape descent score (63d) — is the half-slope
    difference evolving toward or away from a V."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
        s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        return s1 - s2
    base = close.rolling(63, min_periods=30).apply(_v, raw=True)
    return base.diff(5)


def dsh_drv2_009_rounded_bottom_score_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in rounded-bottom score (63d quad coef / price range)."""
    qc = _roll_quad_coef(close, 63)
    rng = _roll_max(close, 63) - _roll_min(close, 63)
    base = _safe_div(qc, rng)
    return base.diff(5)


def dsh_drv2_010_stair_step_ratio_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in the stair-step day fraction (63d) — is the step-down
    cadence accelerating."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    big = (dc.abs() > 1.5 * std).astype(float)
    base = big.rolling(63, min_periods=30).mean()
    return base.diff(10)


def dsh_drv2_011_plateau_fraction_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in plateau fraction (63d) — are quiet consolidation pauses
    becoming more or less frequent."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    flat = (dc.abs() < 0.25 * std).astype(float)
    base = flat.rolling(63, min_periods=30).mean()
    return base.diff(10)


def dsh_drv2_012_drawdown_convexity_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in drawdown convexity (mean/max drawdown ratio, 63d)."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    base = _safe_div(dd.rolling(63, min_periods=30).mean(),
                     dd.rolling(63, min_periods=30).max())
    return base.diff(5)


def dsh_drv2_013_drawdown_r2_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in R^2 of linear fit to the drawdown series (63d)."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    base = _roll_r2(dd, 63)
    return base.diff(5)


def dsh_drv2_014_drawdown_quad_coef_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in quadratic coefficient of the drawdown path (63d)."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    base = _roll_quad_coef(dd, 63)
    return base.diff(5)


def dsh_drv2_015_price_autocorr_lag1_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in lag-1 return autocorrelation (63d) — is momentum
    structure shifting."""
    ret = close.pct_change()
    base = _roll_autocorr(ret, 63, lag=1)
    return base.diff(10)


def dsh_drv2_016_vol_surge_down_days_63d_diff10(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """10-day change in down-day vs up-day volume ratio (63d)."""
    dc = close.diff()
    down_v = volume.where(dc < 0)
    up_v = volume.where(dc > 0)
    mean_d = down_v.rolling(63, min_periods=20).mean()
    mean_u = up_v.rolling(63, min_periods=20).mean()
    base = _safe_div(mean_d, mean_u)
    return base.diff(10)


def dsh_drv2_017_lower_low_streak_63d_diff5(low: pd.Series) -> pd.Series:
    """5-day change in lower-low fraction (63d) — is structural weakness
    intensifying."""
    ll = (low < low.shift(1)).astype(float)
    base = ll.rolling(63, min_periods=30).mean()
    return base.diff(5)


def dsh_drv2_018_exp_decay_rate_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in exponential decay rate (63d)."""
    def _exp_rate(y):
        n = len(y)
        if n < 3 or np.any(y <= 0):
            return np.nan
        x = np.arange(n, dtype=float) - (n - 1) / 2.0
        logy = np.log(y)
        denom = np.dot(x, x)
        return np.dot(x, logy) / denom if denom > _EPS else np.nan
    base = close.rolling(63, min_periods=30).apply(_exp_rate, raw=True)
    return base.diff(10)


def dsh_drv2_019_return_skew_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in return skewness (63d) — increasingly negative skew =
    panic acceleration."""
    ret = close.pct_change()
    base = ret.rolling(63, min_periods=20).skew()
    return base.diff(5)


def dsh_drv2_020_return_kurt_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in return kurtosis (63d) — fat-tail buildup rate."""
    ret = close.pct_change()
    base = ret.rolling(63, min_periods=20).kurt()
    return base.diff(5)


def dsh_drv2_021_midpoint_vs_linear_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change in midpoint deviation from linear interpolation (63d)."""
    def _mid_dev(y):
        n = len(y)
        if n < 3:
            return np.nan
        lin = np.linspace(y[0], y[-1], n)
        return y[n // 2] - lin[n // 2]
    base = close.rolling(63, min_periods=30).apply(_mid_dev, raw=True)
    return base.diff(5)


def dsh_drv2_022_hl_range_quad_coef_63d_diff5(high: pd.Series,
                                                low: pd.Series) -> pd.Series:
    """5-day change in quadratic coefficient of H-L range (63d)."""
    rng = high - low
    base = _roll_quad_coef(rng, 63)
    return base.diff(5)


def dsh_drv2_023_drawdown_path_skew_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in skewness of the drawdown level distribution (63d)."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    base = dd.rolling(63, min_periods=20).skew()
    return base.diff(10)


def dsh_drv2_024_first_third_decline_share_63d_diff10(close: pd.Series) -> pd.Series:
    """10-day change in the first-third decline share (63d) — is the front-
    loading of the drop increasing."""
    def _f3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        return (y[0] - y[len(y) // 3]) / total
    base = close.rolling(63, min_periods=30).apply(_f3, raw=True)
    return base.diff(10)


def dsh_drv2_025_slope_acceleration_63d_diff5(close: pd.Series) -> pd.Series:
    """5-day change of the 5-day change in 63d slope — third-order term
    expressed as a 2nd-derivative construct (jerk of the slope)."""
    s = _roll_slope(close, 63)
    accel = s.diff(5)
    return accel.diff(5)


# ── Registry ───────────────────────────────────────────────────────────────────

DRAWDOWN_SHAPE_REGISTRY_2ND_DERIVATIVES = {
    "dsh_drv2_001_quad_coef_63d_diff5":              {"inputs": ["close"],          "func": dsh_drv2_001_quad_coef_63d_diff5},
    "dsh_drv2_002_quad_coef_126d_diff5":             {"inputs": ["close"],          "func": dsh_drv2_002_quad_coef_126d_diff5},
    "dsh_drv2_003_linear_r2_63d_diff5":              {"inputs": ["close"],          "func": dsh_drv2_003_linear_r2_63d_diff5},
    "dsh_drv2_004_linear_r2_126d_diff10":            {"inputs": ["close"],          "func": dsh_drv2_004_linear_r2_126d_diff10},
    "dsh_drv2_005_lin_rmse_normed_63d_diff5":        {"inputs": ["close"],          "func": dsh_drv2_005_lin_rmse_normed_63d_diff5},
    "dsh_drv2_006_jaggedness_21d_diff5":             {"inputs": ["close"],          "func": dsh_drv2_006_jaggedness_21d_diff5},
    "dsh_drv2_007_jaggedness_63d_diff10":            {"inputs": ["close"],          "func": dsh_drv2_007_jaggedness_63d_diff10},
    "dsh_drv2_008_v_shape_score_63d_diff5":          {"inputs": ["close"],          "func": dsh_drv2_008_v_shape_score_63d_diff5},
    "dsh_drv2_009_rounded_bottom_score_63d_diff5":   {"inputs": ["close"],          "func": dsh_drv2_009_rounded_bottom_score_63d_diff5},
    "dsh_drv2_010_stair_step_ratio_63d_diff10":      {"inputs": ["close"],          "func": dsh_drv2_010_stair_step_ratio_63d_diff10},
    "dsh_drv2_011_plateau_fraction_63d_diff10":      {"inputs": ["close"],          "func": dsh_drv2_011_plateau_fraction_63d_diff10},
    "dsh_drv2_012_drawdown_convexity_63d_diff5":     {"inputs": ["close"],          "func": dsh_drv2_012_drawdown_convexity_63d_diff5},
    "dsh_drv2_013_drawdown_r2_63d_diff5":            {"inputs": ["close"],          "func": dsh_drv2_013_drawdown_r2_63d_diff5},
    "dsh_drv2_014_drawdown_quad_coef_63d_diff5":     {"inputs": ["close"],          "func": dsh_drv2_014_drawdown_quad_coef_63d_diff5},
    "dsh_drv2_015_price_autocorr_lag1_63d_diff10":   {"inputs": ["close"],          "func": dsh_drv2_015_price_autocorr_lag1_63d_diff10},
    "dsh_drv2_016_vol_surge_down_days_63d_diff10":   {"inputs": ["close", "volume"],"func": dsh_drv2_016_vol_surge_down_days_63d_diff10},
    "dsh_drv2_017_lower_low_streak_63d_diff5":       {"inputs": ["low"],            "func": dsh_drv2_017_lower_low_streak_63d_diff5},
    "dsh_drv2_018_exp_decay_rate_63d_diff10":        {"inputs": ["close"],          "func": dsh_drv2_018_exp_decay_rate_63d_diff10},
    "dsh_drv2_019_return_skew_63d_diff5":            {"inputs": ["close"],          "func": dsh_drv2_019_return_skew_63d_diff5},
    "dsh_drv2_020_return_kurt_63d_diff5":            {"inputs": ["close"],          "func": dsh_drv2_020_return_kurt_63d_diff5},
    "dsh_drv2_021_midpoint_vs_linear_63d_diff5":     {"inputs": ["close"],          "func": dsh_drv2_021_midpoint_vs_linear_63d_diff5},
    "dsh_drv2_022_hl_range_quad_coef_63d_diff5":     {"inputs": ["high", "low"],    "func": dsh_drv2_022_hl_range_quad_coef_63d_diff5},
    "dsh_drv2_023_drawdown_path_skew_63d_diff10":    {"inputs": ["close"],          "func": dsh_drv2_023_drawdown_path_skew_63d_diff10},
    "dsh_drv2_024_first_third_decline_share_63d_diff10": {"inputs": ["close"],      "func": dsh_drv2_024_first_third_decline_share_63d_diff10},
    "dsh_drv2_025_slope_acceleration_63d_diff5":     {"inputs": ["close"],          "func": dsh_drv2_025_slope_acceleration_63d_diff5},
}
