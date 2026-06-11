"""
03_drawdown_shape — Base Features 001-075
Domain: convexity/concavity and geometric shape of the price decline path.
Asset class: US equities | Daily OHLCV only (SEP folder — no fundamentals).
Target context: capitulation bottom — absolute multi-year low / max distress.
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
    """Element-wise division guarded against zero/NaN denominator."""
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
    """Rolling OLS slope (normalised by window length so units are comparable)."""
    def _slope(y):
        n = len(y)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi -= xi.mean()
        yi = y - y.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, yi) / denom if denom > _EPS else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


def _roll_r2(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS R-squared."""
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
    """Rolling coefficient of x^2 from a degree-2 polynomial fit."""
    def _quad(y):
        n = len(y)
        if n < 3:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            c = np.polyfit(x, y, 2)
            return c[0]
        except Exception:
            return np.nan
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_quad, raw=True)


def _roll_quad_r2(s: pd.Series, w: int) -> pd.Series:
    """Rolling R^2 of a degree-2 polynomial fit."""
    def _qr2(y):
        n = len(y)
        if n < 3:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            c = np.polyfit(x, y, 2)
            yhat = np.polyval(c, x)
            ss_res = np.sum((y - yhat) ** 2)
            ss_tot = np.sum((y - y.mean()) ** 2)
            return 1.0 - ss_res / ss_tot if ss_tot > _EPS else 1.0
        except Exception:
            return np.nan
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_qr2, raw=True)


def _roll_lin_rmse(s: pd.Series, w: int) -> pd.Series:
    """Rolling RMSE of a linear fit."""
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
        resid = y - (a + b * x)
        return np.sqrt(np.mean(resid ** 2))
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_lrmse, raw=True)


def _roll_quad_rmse(s: pd.Series, w: int) -> pd.Series:
    """Rolling RMSE of a quadratic fit."""
    def _qrmse(y):
        n = len(y)
        if n < 3:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            c = np.polyfit(x, y, 2)
            resid = y - np.polyval(c, x)
            return np.sqrt(np.mean(resid ** 2))
        except Exception:
            return np.nan
    return s.rolling(w, min_periods=max(3, w // 2)).apply(_qrmse, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A: Curvature of the drawdown path (quadratic coefficient) ---

def dsh_001_quad_coef_price_21d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of close price over 21-day window — captures whether
    the decline is accelerating (negative) or decelerating (positive)."""
    return _roll_quad_coef(close, 21)


def dsh_002_quad_coef_price_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of close over 63-day window."""
    return _roll_quad_coef(close, 63)


def dsh_003_quad_coef_price_126d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of close over 126-day window."""
    return _roll_quad_coef(close, 126)


def dsh_004_quad_coef_price_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of close over 252-day window."""
    return _roll_quad_coef(close, 252)


def dsh_005_quad_coef_logprice_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of log(close) over 63-day window — log scale
    emphasises percentage curvature."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_quad_coef(lp, 63)


def dsh_006_quad_coef_logprice_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of log(close) over 252-day window."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_quad_coef(lp, 252)


def dsh_007_quad_vs_linear_r2_improvement_63d(close: pd.Series) -> pd.Series:
    """R^2(quadratic) minus R^2(linear) over 63d — positive means meaningful
    curve beyond a straight-line decline."""
    r2q = _roll_quad_r2(close, 63)
    r2l = _roll_r2(close, 63)
    return r2q - r2l


def dsh_008_quad_vs_linear_r2_improvement_126d(close: pd.Series) -> pd.Series:
    """R^2(quadratic) minus R^2(linear) over 126d."""
    r2q = _roll_quad_r2(close, 126)
    r2l = _roll_r2(close, 126)
    return r2q - r2l


def dsh_009_quad_vs_linear_rmse_ratio_63d(close: pd.Series) -> pd.Series:
    """RMSE(quadratic) / RMSE(linear) over 63d — <1 means quadratic is a
    meaningfully better shape description."""
    return _safe_div(_roll_quad_rmse(close, 63), _roll_lin_rmse(close, 63))


def dsh_010_quad_vs_linear_rmse_ratio_126d(close: pd.Series) -> pd.Series:
    """RMSE(quadratic) / RMSE(linear) over 126d."""
    return _safe_div(_roll_quad_rmse(close, 126), _roll_lin_rmse(close, 126))


# --- Group B: Linear fit quality (R^2 of decline) ---

def dsh_011_linear_r2_21d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to close over 21d — high = very steady decline."""
    return _roll_r2(close, 21)


def dsh_012_linear_r2_63d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to close over 63d."""
    return _roll_r2(close, 63)


def dsh_013_linear_r2_126d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to close over 126d."""
    return _roll_r2(close, 126)


def dsh_014_linear_r2_252d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to close over 252d."""
    return _roll_r2(close, 252)


def dsh_015_linear_r2_logprice_63d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to log(close) over 63d — geometric regularity."""
    return _roll_r2(np.log(close.clip(lower=_EPS)), 63)


def dsh_016_linear_rmse_normed_21d(close: pd.Series) -> pd.Series:
    """Linear RMSE divided by rolling mean price over 21d — normalised residual."""
    return _safe_div(_roll_lin_rmse(close, 21), _roll_mean(close, 21))


def dsh_017_linear_rmse_normed_63d(close: pd.Series) -> pd.Series:
    """Linear RMSE divided by rolling mean price over 63d."""
    return _safe_div(_roll_lin_rmse(close, 63), _roll_mean(close, 63))


def dsh_018_linear_rmse_normed_126d(close: pd.Series) -> pd.Series:
    """Linear RMSE divided by rolling mean price over 126d."""
    return _safe_div(_roll_lin_rmse(close, 126), _roll_mean(close, 126))


# --- Group C: Path-length jaggedness (arc length / chord ratio) ---

def dsh_019_jaggedness_close_21d(close: pd.Series) -> pd.Series:
    """Arc-length of close path / net price movement over 21d.
    High = choppy/jagged descent; 1 = monotone."""
    arc = close.diff().abs().rolling(21, min_periods=10).sum()
    chord = (close - close.shift(20)).abs()
    return _safe_div(arc, chord)


def dsh_020_jaggedness_close_63d(close: pd.Series) -> pd.Series:
    """Arc-length / chord over 63d window."""
    arc = close.diff().abs().rolling(63, min_periods=30).sum()
    chord = (close - close.shift(62)).abs()
    return _safe_div(arc, chord)


def dsh_021_jaggedness_close_126d(close: pd.Series) -> pd.Series:
    """Arc-length / chord over 126d window."""
    arc = close.diff().abs().rolling(126, min_periods=60).sum()
    chord = (close - close.shift(125)).abs()
    return _safe_div(arc, chord)


def dsh_022_jaggedness_close_252d(close: pd.Series) -> pd.Series:
    """Arc-length / chord over 252d window."""
    arc = close.diff().abs().rolling(252, min_periods=120).sum()
    chord = (close - close.shift(251)).abs()
    return _safe_div(arc, chord)


def dsh_023_jaggedness_hl_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Arc-length using daily H-L range sums vs HL band over 21d — captures
    intraday jaggedness of the decline."""
    arc = (high - low).rolling(21, min_periods=10).sum()
    band = _roll_max(high, 21) - _roll_min(low, 21)
    return _safe_div(arc, band)


def dsh_024_jaggedness_hl_range_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Arc-length HL arc / HL band over 63d."""
    arc = (high - low).rolling(63, min_periods=30).sum()
    band = _roll_max(high, 63) - _roll_min(low, 63)
    return _safe_div(arc, band)


def dsh_025_jaggedness_logprice_63d(close: pd.Series) -> pd.Series:
    """Arc-length / chord on log price over 63d — geometric jaggedness."""
    lp = np.log(close.clip(lower=_EPS))
    arc = lp.diff().abs().rolling(63, min_periods=30).sum()
    chord = (lp - lp.shift(62)).abs()
    return _safe_div(arc, chord)


# --- Group D: First-third vs last-third decline concentration ---

def dsh_026_first_third_decline_share_63d(close: pd.Series) -> pd.Series:
    """Share of total 63d decline that occurred in the first 21 days.
    High = front-loaded capitulation."""
    def _f3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        first = y[0] - y[len(y) // 3]
        return first / total
    return close.rolling(63, min_periods=30).apply(_f3, raw=True)


def dsh_027_last_third_decline_share_63d(close: pd.Series) -> pd.Series:
    """Share of total 63d decline in the last 21 days — back-loaded = recent
    acceleration."""
    def _l3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        last = y[2 * len(y) // 3] - y[-1]
        return last / total
    return close.rolling(63, min_periods=30).apply(_l3, raw=True)


def dsh_028_first_third_decline_share_126d(close: pd.Series) -> pd.Series:
    """Share of 126d decline in first 42 days."""
    def _f3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        return (y[0] - y[len(y) // 3]) / total
    return close.rolling(126, min_periods=60).apply(_f3, raw=True)


def dsh_029_last_third_decline_share_126d(close: pd.Series) -> pd.Series:
    """Share of 126d decline in last 42 days."""
    def _l3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        return (y[2 * len(y) // 3] - y[-1]) / total
    return close.rolling(126, min_periods=60).apply(_l3, raw=True)


def dsh_030_first_third_decline_share_252d(close: pd.Series) -> pd.Series:
    """Share of 252d decline in first 84 days."""
    def _f3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        return (y[0] - y[len(y) // 3]) / total
    return close.rolling(252, min_periods=120).apply(_f3, raw=True)


def dsh_031_last_third_decline_share_252d(close: pd.Series) -> pd.Series:
    """Share of 252d decline in last 84 days."""
    def _l3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        return (y[2 * len(y) // 3] - y[-1]) / total
    return close.rolling(252, min_periods=120).apply(_l3, raw=True)


def dsh_032_middle_third_decline_share_63d(close: pd.Series) -> pd.Series:
    """Share of 63d decline in the middle third."""
    def _m3(y):
        total = y[0] - y[-1]
        if abs(total) < _EPS:
            return np.nan
        t1 = len(y) // 3
        t2 = 2 * len(y) // 3
        return (y[t1] - y[t2]) / total
    return close.rolling(63, min_periods=30).apply(_m3, raw=True)


# --- Group E: V-shape vs rounded descent scoring ---

def dsh_033_v_shape_descent_score_63d(close: pd.Series) -> pd.Series:
    """Slope of first half minus slope of second half over 63d.
    Large negative = V-shape (steep then stabilising), positive = worsening."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        x1 = np.arange(m, dtype=float)
        s1 = np.polyfit(x1, y[:m], 1)[0] if m > 1 else 0.0
        x2 = np.arange(n - m, dtype=float)
        s2 = np.polyfit(x2, y[m:], 1)[0] if (n - m) > 1 else 0.0
        return s1 - s2
    return close.rolling(63, min_periods=30).apply(_v, raw=True)


def dsh_034_v_shape_descent_score_126d(close: pd.Series) -> pd.Series:
    """V-shape descent score over 126d."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
        s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        return s1 - s2
    return close.rolling(126, min_periods=60).apply(_v, raw=True)


def dsh_035_v_shape_descent_score_252d(close: pd.Series) -> pd.Series:
    """V-shape descent score over 252d."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
        s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        return s1 - s2
    return close.rolling(252, min_periods=120).apply(_v, raw=True)


def dsh_036_rounded_bottom_score_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient normalised by price range over 63d — positive large
    = U-shaped (rounded bottom); negative = inverted-U (parabolic acceleration)."""
    qc = _roll_quad_coef(close, 63)
    rng = _roll_max(close, 63) - _roll_min(close, 63)
    return _safe_div(qc, rng)


def dsh_037_rounded_bottom_score_126d(close: pd.Series) -> pd.Series:
    """Rounded-bottom curvature score normalised over 126d."""
    qc = _roll_quad_coef(close, 126)
    rng = _roll_max(close, 126) - _roll_min(close, 126)
    return _safe_div(qc, rng)


def dsh_038_rounded_bottom_score_252d(close: pd.Series) -> pd.Series:
    """Rounded-bottom curvature score normalised over 252d."""
    qc = _roll_quad_coef(close, 252)
    rng = _roll_max(close, 252) - _roll_min(close, 252)
    return _safe_div(qc, rng)


# --- Group F: Stair-step structure ---

def dsh_039_stair_step_count_21d(close: pd.Series) -> pd.Series:
    """Count of 1-day moves > 1.5 std of 21d daily moves — discrete 'steps'."""
    dc = close.diff()
    std = _roll_std(dc, 21)
    big = (dc.abs() > 1.5 * std).astype(float)
    return big.rolling(21, min_periods=10).sum()


def dsh_040_stair_step_count_63d(close: pd.Series) -> pd.Series:
    """Count of big-step days over 63d."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    big = (dc.abs() > 1.5 * std).astype(float)
    return big.rolling(63, min_periods=30).sum()


def dsh_041_stair_step_ratio_63d(close: pd.Series) -> pd.Series:
    """Big-step days / total days in 63d window — density of step-downs."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    big = (dc.abs() > 1.5 * std).astype(float)
    return big.rolling(63, min_periods=30).mean()


def dsh_042_down_step_count_63d(close: pd.Series) -> pd.Series:
    """Count of large DOWN-step days over 63d (step-downs only)."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    big_down = ((dc < 0) & (dc.abs() > 1.5 * std)).astype(float)
    return big_down.rolling(63, min_periods=30).sum()


def dsh_043_up_step_count_63d(close: pd.Series) -> pd.Series:
    """Count of large UP-step (dead-cat bounce) days over 63d."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    big_up = ((dc > 0) & (dc.abs() > 1.5 * std)).astype(float)
    return big_up.rolling(63, min_periods=30).sum()


def dsh_044_step_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Down-step count / up-step count over 63d — >1 = more big drops than
    big rallies."""
    d = dsh_042_down_step_count_63d(close)
    u = dsh_043_up_step_count_63d(close)
    return _safe_div(d, u)


def dsh_045_plateau_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63d days where |close.diff()| < 0.25*std — measures 'pause'
    periods between legs down."""
    dc = close.diff()
    std = _roll_std(dc, 63)
    flat = (dc.abs() < 0.25 * std).astype(float)
    return flat.rolling(63, min_periods=30).mean()


def dsh_046_plateau_fraction_126d(close: pd.Series) -> pd.Series:
    """Plateau fraction over 126d."""
    dc = close.diff()
    std = _roll_std(dc, 126)
    flat = (dc.abs() < 0.25 * std).astype(float)
    return flat.rolling(126, min_periods=60).mean()


# --- Group G: Decline path shape via high-low structure ---

def dsh_047_lower_high_streak_21d(high: pd.Series) -> pd.Series:
    """Fraction of 21d days with a lower daily high than the prior day — measures
    sustained downward pressure in intraday structure."""
    lh = (high < high.shift(1)).astype(float)
    return lh.rolling(21, min_periods=10).mean()


def dsh_048_lower_low_streak_21d(low: pd.Series) -> pd.Series:
    """Fraction of 21d days with a lower daily low — structural weakness."""
    ll = (low < low.shift(1)).astype(float)
    return ll.rolling(21, min_periods=10).mean()


def dsh_049_lower_high_streak_63d(high: pd.Series) -> pd.Series:
    """Fraction of 63d with lower daily highs."""
    lh = (high < high.shift(1)).astype(float)
    return lh.rolling(63, min_periods=30).mean()


def dsh_050_lower_low_streak_63d(low: pd.Series) -> pd.Series:
    """Fraction of 63d with lower daily lows."""
    ll = (low < low.shift(1)).astype(float)
    return ll.rolling(63, min_periods=30).mean()


def dsh_051_hl_midpoint_slope_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of the H-L midpoint over 63d — unbiased trend of the bar centre."""
    mid = (high + low) / 2.0
    return _roll_slope(mid, 63)


def dsh_052_hl_midpoint_r2_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """R^2 of linear fit to H-L midpoint over 63d."""
    mid = (high + low) / 2.0
    return _roll_r2(mid, 63)


def dsh_053_hl_midpoint_quad_coef_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Quadratic coefficient of H-L midpoint over 63d."""
    mid = (high + low) / 2.0
    return _roll_quad_coef(mid, 63)


def dsh_054_closing_position_in_range_21d(close: pd.Series, high: pd.Series,
                                           low: pd.Series) -> pd.Series:
    """Rolling mean of (close-low)/(high-low) over 21d — where closes land
    within daily ranges; near 0 = persistent close near lows."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return pos.rolling(21, min_periods=10).mean()


def dsh_055_closing_position_in_range_63d(close: pd.Series, high: pd.Series,
                                           low: pd.Series) -> pd.Series:
    """Rolling 63d mean of close position within daily range."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return pos.rolling(63, min_periods=30).mean()


# --- Group H: Volume-weighted path shape ---

def dsh_056_volume_weighted_price_slope_63d(close: pd.Series,
                                             volume: pd.Series) -> pd.Series:
    """Slope of volume-weighted close over 63d — emphasises high-activity days."""
    vwp = close * volume
    sv = volume.rolling(63, min_periods=30).sum()
    svwp = vwp.rolling(63, min_periods=30).sum()
    vwap_roll = _safe_div(svwp, sv)
    return _roll_slope(vwap_roll, 63)


def dsh_057_volume_weighted_price_r2_63d(close: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """R^2 of linear fit to rolling VWAP over 63d."""
    vwp = close * volume
    sv = volume.rolling(63, min_periods=30).sum()
    svwp = vwp.rolling(63, min_periods=30).sum()
    vwap_roll = _safe_div(svwp, sv)
    return _roll_r2(vwap_roll, 63)


def dsh_058_vol_surge_on_down_days_63d(close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Mean volume on down days / mean volume on up days over 63d — high =
    volume concentrated on declines, classic capitulation shape."""
    dc = close.diff()
    down_v = volume.where(dc < 0)
    up_v = volume.where(dc > 0)
    mean_d = down_v.rolling(63, min_periods=20).mean()
    mean_u = up_v.rolling(63, min_periods=20).mean()
    return _safe_div(mean_d, mean_u)


def dsh_059_vol_surge_on_down_days_21d(close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Mean down-day volume / mean up-day volume over 21d."""
    dc = close.diff()
    down_v = volume.where(dc < 0)
    up_v = volume.where(dc > 0)
    mean_d = down_v.rolling(21, min_periods=7).mean()
    mean_u = up_v.rolling(21, min_periods=7).mean()
    return _safe_div(mean_d, mean_u)


def dsh_060_vol_path_length_ratio_63d(close: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """Volume-weighted arc-length of price path / simple arc-length over 63d.
    Weights price movements by volume to detect if big drops are heavy-vol."""
    w = volume / volume.rolling(63, min_periods=30).mean()
    w = w.fillna(1.0)
    weighted_arc = (close.diff().abs() * w).rolling(63, min_periods=30).sum()
    plain_arc = close.diff().abs().rolling(63, min_periods=30).sum()
    return _safe_div(weighted_arc, plain_arc)


# --- Group I: Concavity via drawdown path ---

def dsh_061_drawdown_convexity_21d(close: pd.Series) -> pd.Series:
    """Mean drawdown / max drawdown over 21d. Near 0.5 = linear; >0.5 = concave
    (stays deep); <0.5 = convex (V-shaped spike)."""
    h = _roll_max(close, 21)
    dd = (h - close) / h.replace(0, np.nan)
    mean_dd = dd.rolling(21, min_periods=10).mean()
    max_dd = dd.rolling(21, min_periods=10).max()
    return _safe_div(mean_dd, max_dd)


def dsh_062_drawdown_convexity_63d(close: pd.Series) -> pd.Series:
    """Mean/max drawdown over 63d — concavity proxy."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _safe_div(dd.rolling(63, min_periods=30).mean(),
                     dd.rolling(63, min_periods=30).max())


def dsh_063_drawdown_convexity_126d(close: pd.Series) -> pd.Series:
    """Mean/max drawdown over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return _safe_div(dd.rolling(126, min_periods=60).mean(),
                     dd.rolling(126, min_periods=60).max())


def dsh_064_drawdown_path_skewness_63d(close: pd.Series) -> pd.Series:
    """Skewness of the drawdown distribution over 63d — negative = rare deep
    spikes; positive = mostly deep with rare recoveries."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return dd.rolling(63, min_periods=20).skew()


def dsh_065_drawdown_path_skewness_126d(close: pd.Series) -> pd.Series:
    """Skewness of drawdown distribution over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return dd.rolling(126, min_periods=40).skew()


def dsh_066_drawdown_path_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of drawdown distribution over 63d — high = fat-tailed
    extreme drops."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return dd.rolling(63, min_periods=20).kurt()


def dsh_067_drawdown_path_kurtosis_126d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of drawdown path over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return dd.rolling(126, min_periods=40).kurt()


# --- Group J: Log-scale curvature ---

def dsh_068_log_price_quad_coef_21d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of log price over 21d window."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_quad_coef(lp, 21)


def dsh_069_log_price_lin_r2_21d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to log price over 21d."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_r2(lp, 21)


def dsh_070_log_price_lin_rmse_63d(close: pd.Series) -> pd.Series:
    """RMSE of linear fit to log price over 63d — unexplained path deviation."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_lin_rmse(lp, 63)


def dsh_071_log_price_quad_rmse_63d(close: pd.Series) -> pd.Series:
    """RMSE of quadratic fit to log price over 63d."""
    lp = np.log(close.clip(lower=_EPS))
    return _roll_quad_rmse(lp, 63)


def dsh_072_log_jaggedness_63d(close: pd.Series) -> pd.Series:
    """Arc-length / chord on log(close) over 63d."""
    lp = np.log(close.clip(lower=_EPS))
    arc = lp.diff().abs().rolling(63, min_periods=30).sum()
    chord = (lp - lp.shift(62)).abs()
    return _safe_div(arc, chord)


# --- Group K: Decline acceleration captured via slope-of-slope ---

def dsh_073_slope_acceleration_21d(close: pd.Series) -> pd.Series:
    """5-day change in the 21d rolling slope of close — positive = slope
    is steepening (accelerating down or decelerating up)."""
    s = _roll_slope(close, 21)
    return s.diff(5)


def dsh_074_slope_acceleration_63d(close: pd.Series) -> pd.Series:
    """5-day change in the 63d rolling slope of close."""
    s = _roll_slope(close, 63)
    return s.diff(5)


def dsh_075_slope_acceleration_126d(close: pd.Series) -> pd.Series:
    """5-day change in the 126d rolling slope of close."""
    s = _roll_slope(close, 126)
    return s.diff(5)


# ── Registry ───────────────────────────────────────────────────────────────────

DRAWDOWN_SHAPE_REGISTRY_001_075 = {
    "dsh_001_quad_coef_price_21d":            {"inputs": ["close"],                        "func": dsh_001_quad_coef_price_21d},
    "dsh_002_quad_coef_price_63d":            {"inputs": ["close"],                        "func": dsh_002_quad_coef_price_63d},
    "dsh_003_quad_coef_price_126d":           {"inputs": ["close"],                        "func": dsh_003_quad_coef_price_126d},
    "dsh_004_quad_coef_price_252d":           {"inputs": ["close"],                        "func": dsh_004_quad_coef_price_252d},
    "dsh_005_quad_coef_logprice_63d":         {"inputs": ["close"],                        "func": dsh_005_quad_coef_logprice_63d},
    "dsh_006_quad_coef_logprice_252d":        {"inputs": ["close"],                        "func": dsh_006_quad_coef_logprice_252d},
    "dsh_007_quad_vs_linear_r2_improvement_63d":  {"inputs": ["close"],                   "func": dsh_007_quad_vs_linear_r2_improvement_63d},
    "dsh_008_quad_vs_linear_r2_improvement_126d": {"inputs": ["close"],                   "func": dsh_008_quad_vs_linear_r2_improvement_126d},
    "dsh_009_quad_vs_linear_rmse_ratio_63d":  {"inputs": ["close"],                       "func": dsh_009_quad_vs_linear_rmse_ratio_63d},
    "dsh_010_quad_vs_linear_rmse_ratio_126d": {"inputs": ["close"],                       "func": dsh_010_quad_vs_linear_rmse_ratio_126d},
    "dsh_011_linear_r2_21d":                  {"inputs": ["close"],                        "func": dsh_011_linear_r2_21d},
    "dsh_012_linear_r2_63d":                  {"inputs": ["close"],                        "func": dsh_012_linear_r2_63d},
    "dsh_013_linear_r2_126d":                 {"inputs": ["close"],                        "func": dsh_013_linear_r2_126d},
    "dsh_014_linear_r2_252d":                 {"inputs": ["close"],                        "func": dsh_014_linear_r2_252d},
    "dsh_015_linear_r2_logprice_63d":         {"inputs": ["close"],                        "func": dsh_015_linear_r2_logprice_63d},
    "dsh_016_linear_rmse_normed_21d":         {"inputs": ["close"],                        "func": dsh_016_linear_rmse_normed_21d},
    "dsh_017_linear_rmse_normed_63d":         {"inputs": ["close"],                        "func": dsh_017_linear_rmse_normed_63d},
    "dsh_018_linear_rmse_normed_126d":        {"inputs": ["close"],                        "func": dsh_018_linear_rmse_normed_126d},
    "dsh_019_jaggedness_close_21d":           {"inputs": ["close"],                        "func": dsh_019_jaggedness_close_21d},
    "dsh_020_jaggedness_close_63d":           {"inputs": ["close"],                        "func": dsh_020_jaggedness_close_63d},
    "dsh_021_jaggedness_close_126d":          {"inputs": ["close"],                        "func": dsh_021_jaggedness_close_126d},
    "dsh_022_jaggedness_close_252d":          {"inputs": ["close"],                        "func": dsh_022_jaggedness_close_252d},
    "dsh_023_jaggedness_hl_range_21d":        {"inputs": ["high", "low"],                  "func": dsh_023_jaggedness_hl_range_21d},
    "dsh_024_jaggedness_hl_range_63d":        {"inputs": ["high", "low"],                  "func": dsh_024_jaggedness_hl_range_63d},
    "dsh_025_jaggedness_logprice_63d":        {"inputs": ["close"],                        "func": dsh_025_jaggedness_logprice_63d},
    "dsh_026_first_third_decline_share_63d":  {"inputs": ["close"],                        "func": dsh_026_first_third_decline_share_63d},
    "dsh_027_last_third_decline_share_63d":   {"inputs": ["close"],                        "func": dsh_027_last_third_decline_share_63d},
    "dsh_028_first_third_decline_share_126d": {"inputs": ["close"],                        "func": dsh_028_first_third_decline_share_126d},
    "dsh_029_last_third_decline_share_126d":  {"inputs": ["close"],                        "func": dsh_029_last_third_decline_share_126d},
    "dsh_030_first_third_decline_share_252d": {"inputs": ["close"],                        "func": dsh_030_first_third_decline_share_252d},
    "dsh_031_last_third_decline_share_252d":  {"inputs": ["close"],                        "func": dsh_031_last_third_decline_share_252d},
    "dsh_032_middle_third_decline_share_63d": {"inputs": ["close"],                        "func": dsh_032_middle_third_decline_share_63d},
    "dsh_033_v_shape_descent_score_63d":      {"inputs": ["close"],                        "func": dsh_033_v_shape_descent_score_63d},
    "dsh_034_v_shape_descent_score_126d":     {"inputs": ["close"],                        "func": dsh_034_v_shape_descent_score_126d},
    "dsh_035_v_shape_descent_score_252d":     {"inputs": ["close"],                        "func": dsh_035_v_shape_descent_score_252d},
    "dsh_036_rounded_bottom_score_63d":       {"inputs": ["close"],                        "func": dsh_036_rounded_bottom_score_63d},
    "dsh_037_rounded_bottom_score_126d":      {"inputs": ["close"],                        "func": dsh_037_rounded_bottom_score_126d},
    "dsh_038_rounded_bottom_score_252d":      {"inputs": ["close"],                        "func": dsh_038_rounded_bottom_score_252d},
    "dsh_039_stair_step_count_21d":           {"inputs": ["close"],                        "func": dsh_039_stair_step_count_21d},
    "dsh_040_stair_step_count_63d":           {"inputs": ["close"],                        "func": dsh_040_stair_step_count_63d},
    "dsh_041_stair_step_ratio_63d":           {"inputs": ["close"],                        "func": dsh_041_stair_step_ratio_63d},
    "dsh_042_down_step_count_63d":            {"inputs": ["close"],                        "func": dsh_042_down_step_count_63d},
    "dsh_043_up_step_count_63d":              {"inputs": ["close"],                        "func": dsh_043_up_step_count_63d},
    "dsh_044_step_asymmetry_63d":             {"inputs": ["close"],                        "func": dsh_044_step_asymmetry_63d},
    "dsh_045_plateau_fraction_63d":           {"inputs": ["close"],                        "func": dsh_045_plateau_fraction_63d},
    "dsh_046_plateau_fraction_126d":          {"inputs": ["close"],                        "func": dsh_046_plateau_fraction_126d},
    "dsh_047_lower_high_streak_21d":          {"inputs": ["high"],                         "func": dsh_047_lower_high_streak_21d},
    "dsh_048_lower_low_streak_21d":           {"inputs": ["low"],                          "func": dsh_048_lower_low_streak_21d},
    "dsh_049_lower_high_streak_63d":          {"inputs": ["high"],                         "func": dsh_049_lower_high_streak_63d},
    "dsh_050_lower_low_streak_63d":           {"inputs": ["low"],                          "func": dsh_050_lower_low_streak_63d},
    "dsh_051_hl_midpoint_slope_63d":          {"inputs": ["high", "low"],                  "func": dsh_051_hl_midpoint_slope_63d},
    "dsh_052_hl_midpoint_r2_63d":             {"inputs": ["high", "low"],                  "func": dsh_052_hl_midpoint_r2_63d},
    "dsh_053_hl_midpoint_quad_coef_63d":      {"inputs": ["high", "low"],                  "func": dsh_053_hl_midpoint_quad_coef_63d},
    "dsh_054_closing_position_in_range_21d":  {"inputs": ["close", "high", "low"],         "func": dsh_054_closing_position_in_range_21d},
    "dsh_055_closing_position_in_range_63d":  {"inputs": ["close", "high", "low"],         "func": dsh_055_closing_position_in_range_63d},
    "dsh_056_volume_weighted_price_slope_63d": {"inputs": ["close", "volume"],             "func": dsh_056_volume_weighted_price_slope_63d},
    "dsh_057_volume_weighted_price_r2_63d":   {"inputs": ["close", "volume"],              "func": dsh_057_volume_weighted_price_r2_63d},
    "dsh_058_vol_surge_on_down_days_63d":     {"inputs": ["close", "volume"],              "func": dsh_058_vol_surge_on_down_days_63d},
    "dsh_059_vol_surge_on_down_days_21d":     {"inputs": ["close", "volume"],              "func": dsh_059_vol_surge_on_down_days_21d},
    "dsh_060_vol_path_length_ratio_63d":      {"inputs": ["close", "volume"],              "func": dsh_060_vol_path_length_ratio_63d},
    "dsh_061_drawdown_convexity_21d":         {"inputs": ["close"],                        "func": dsh_061_drawdown_convexity_21d},
    "dsh_062_drawdown_convexity_63d":         {"inputs": ["close"],                        "func": dsh_062_drawdown_convexity_63d},
    "dsh_063_drawdown_convexity_126d":        {"inputs": ["close"],                        "func": dsh_063_drawdown_convexity_126d},
    "dsh_064_drawdown_path_skewness_63d":     {"inputs": ["close"],                        "func": dsh_064_drawdown_path_skewness_63d},
    "dsh_065_drawdown_path_skewness_126d":    {"inputs": ["close"],                        "func": dsh_065_drawdown_path_skewness_126d},
    "dsh_066_drawdown_path_kurtosis_63d":     {"inputs": ["close"],                        "func": dsh_066_drawdown_path_kurtosis_63d},
    "dsh_067_drawdown_path_kurtosis_126d":    {"inputs": ["close"],                        "func": dsh_067_drawdown_path_kurtosis_126d},
    "dsh_068_log_price_quad_coef_21d":        {"inputs": ["close"],                        "func": dsh_068_log_price_quad_coef_21d},
    "dsh_069_log_price_lin_r2_21d":           {"inputs": ["close"],                        "func": dsh_069_log_price_lin_r2_21d},
    "dsh_070_log_price_lin_rmse_63d":         {"inputs": ["close"],                        "func": dsh_070_log_price_lin_rmse_63d},
    "dsh_071_log_price_quad_rmse_63d":        {"inputs": ["close"],                        "func": dsh_071_log_price_quad_rmse_63d},
    "dsh_072_log_jaggedness_63d":             {"inputs": ["close"],                        "func": dsh_072_log_jaggedness_63d},
    "dsh_073_slope_acceleration_21d":         {"inputs": ["close"],                        "func": dsh_073_slope_acceleration_21d},
    "dsh_074_slope_acceleration_63d":         {"inputs": ["close"],                        "func": dsh_074_slope_acceleration_63d},
    "dsh_075_slope_acceleration_126d":        {"inputs": ["close"],                        "func": dsh_075_slope_acceleration_126d},
}
