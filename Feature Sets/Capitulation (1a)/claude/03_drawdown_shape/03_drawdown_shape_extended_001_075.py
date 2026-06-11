"""
03_drawdown_shape — Extended Features 001-075
Domain: convexity/concavity and geometric shape of the price decline path.
Asset class: US equities | Daily OHLCV only (SEP folder — no fundamentals).
Target context: capitulation bottom — absolute multi-year low / max distress.

Net-new depth: V/U/L/W shape scores; cubic polynomial coefficients/residuals;
segment-wise slope decomposition; shape symmetry/asymmetry; sharp-V vs rounded
bottom scoring; curvature sign distribution; path shape entropy; piecewise-linear
residuals; z-score/percentile-rank/regime transforms; rate-of-change variants.
All 75 features are distinct from the 200 in the existing four base files.
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
    """Rolling OLS slope (mean-centred)."""
    def _slope(y):
        n = len(y)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float) - (n - 1) / 2.0
        denom = np.dot(xi, xi)
        return np.dot(xi, y) / denom if denom > _EPS else np.nan
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
    """Rolling coefficient of x^2 from degree-2 polynomial fit."""
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
        return np.sqrt(np.mean((y - (a + b * x)) ** 2))
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_lrmse, raw=True)


# ── Feature functions ext_001 – ext_075 ──────────────────────────────────────

# --- Group A: Cubic polynomial coefficients and residuals ---

def dsh_ext_001_cubic_coef_price_63d(close: pd.Series) -> pd.Series:
    """Cubic (x^3) coefficient of a degree-3 polynomial fit to close over 63d.
    Captures S-curve or inflection structure in the decline path beyond parabola."""
    def _cub(y):
        n = len(y)
        if n < 4:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            return np.polyfit(x, y, 3)[0]
        except Exception:
            return np.nan
    return close.rolling(63, min_periods=30).apply(_cub, raw=True)


def dsh_ext_002_cubic_coef_price_126d(close: pd.Series) -> pd.Series:
    """Cubic coefficient of degree-3 poly fit to close over 126d."""
    def _cub(y):
        n = len(y)
        if n < 4:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            return np.polyfit(x, y, 3)[0]
        except Exception:
            return np.nan
    return close.rolling(126, min_periods=60).apply(_cub, raw=True)


def dsh_ext_003_cubic_rmse_vs_quad_rmse_63d(close: pd.Series) -> pd.Series:
    """RMSE(cubic) / RMSE(quadratic) over 63d — <1 means cubic captures
    meaningfully more shape structure than quadratic."""
    def _ratio(y):
        n = len(y)
        if n < 4:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            c3 = np.polyfit(x, y, 3)
            r3 = np.sqrt(np.mean((y - np.polyval(c3, x)) ** 2))
            c2 = np.polyfit(x, y, 2)
            r2 = np.sqrt(np.mean((y - np.polyval(c2, x)) ** 2))
            return r3 / r2 if r2 > _EPS else np.nan
        except Exception:
            return np.nan
    return close.rolling(63, min_periods=30).apply(_ratio, raw=True)


def dsh_ext_004_cubic_linear_coef_63d(close: pd.Series) -> pd.Series:
    """Linear (x^1) coefficient from degree-3 polynomial fit to close over 63d —
    instantaneous slope component after cubic and quadratic effects are removed."""
    def _lin_from_cubic(y):
        n = len(y)
        if n < 4:
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            return np.polyfit(x, y, 3)[2]
        except Exception:
            return np.nan
    return close.rolling(63, min_periods=30).apply(_lin_from_cubic, raw=True)


def dsh_ext_005_cubic_r2_improvement_63d(close: pd.Series) -> pd.Series:
    """R^2(cubic) minus R^2(quadratic) over 63d — additional shape variance
    explained by the cubic term."""
    def _diff_r2(y):
        n = len(y)
        if n < 4:
            return np.nan
        x = np.arange(n, dtype=float)
        ss_tot = np.sum((y - y.mean()) ** 2)
        if ss_tot < _EPS:
            return 0.0
        try:
            c3 = np.polyfit(x, y, 3)
            r2_3 = 1.0 - np.sum((y - np.polyval(c3, x)) ** 2) / ss_tot
            c2 = np.polyfit(x, y, 2)
            r2_2 = 1.0 - np.sum((y - np.polyval(c2, x)) ** 2) / ss_tot
            return r2_3 - r2_2
        except Exception:
            return np.nan
    return close.rolling(63, min_periods=30).apply(_diff_r2, raw=True)


# --- Group B: V / U / L / W shape classification scores ---

def dsh_ext_006_u_shape_score_63d(close: pd.Series) -> pd.Series:
    """U-shape score over 63d: how much the price path dips below the chord
    connecting start to end, normalised by the drop from start to path minimum.
    Positive = U (dipped and recovered towards end); near 0 = monotone."""
    def _u(y):
        n = len(y)
        if n < 4:
            return np.nan
        chord_mid = (y[0] + y[-1]) / 2.0
        path_min = y.min()
        rng = y[0] - path_min
        if rng < _EPS:
            return 0.0
        return (chord_mid - path_min) / rng
    return close.rolling(63, min_periods=30).apply(_u, raw=True)


def dsh_ext_007_u_shape_score_126d(close: pd.Series) -> pd.Series:
    """U-shape score over 126d window."""
    def _u(y):
        n = len(y)
        if n < 4:
            return np.nan
        chord_mid = (y[0] + y[-1]) / 2.0
        path_min = y.min()
        rng = y[0] - path_min
        if rng < _EPS:
            return 0.0
        return (chord_mid - path_min) / rng
    return close.rolling(126, min_periods=60).apply(_u, raw=True)


def dsh_ext_008_l_shape_score_63d(close: pd.Series) -> pd.Series:
    """L-shape score over 63d: fraction of total decline occurring in the first
    quarter with minimal recovery thereafter. High = abrupt drop then flat."""
    def _l(y):
        n = len(y)
        if n < 8:
            return np.nan
        q1 = n // 4
        total_drop = y[0] - y[-1]
        if abs(total_drop) < _EPS:
            return 0.0
        early_drop = y[0] - y[q1]
        late_range = y[q1:].max() - y[q1:].min()
        early_frac = early_drop / total_drop
        flat_frac = 1.0 - late_range / (abs(total_drop) + _EPS)
        return (early_frac + flat_frac) / 2.0
    return close.rolling(63, min_periods=30).apply(_l, raw=True)


def dsh_ext_009_w_shape_score_63d(close: pd.Series) -> pd.Series:
    """W-shape (double-bottom) score over 63d: detects whether price revisited
    near the window minimum after an interim recovery. High = W pattern."""
    def _w(y):
        n = len(y)
        if n < 10:
            return np.nan
        min_val = y.min()
        min_idx = int(np.argmin(y))
        rng = y[0] - min_val
        if rng < _EPS:
            return 0.0
        if min_idx < 2 or min_idx > n - 3:
            return 0.0
        recovery = y[min_idx:].max() - min_val
        recovery_frac = recovery / rng
        second_dip_depth = (y[min_idx:].max() - y[-1]) / rng
        return min(recovery_frac, second_dip_depth)
    return close.rolling(63, min_periods=30).apply(_w, raw=True)


def dsh_ext_010_sharp_v_bottom_score_63d(close: pd.Series) -> pd.Series:
    """Sharp-V bottom score over 63d: high = rapid capitulation spike rather than
    a slow grind (combines front-loaded descent with a narrow bottom range)."""
    def _sharp_v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        total_drop = y[0] - y.min()
        if total_drop < _EPS:
            return 0.0
        first_drop = y[0] - y[m]
        descent_frac = first_drop / total_drop
        lo = max(0, m - 2)
        hi = min(n, m + 3)
        bottom_range = y[lo:hi].max() - y[lo:hi].min()
        sharpness = 1.0 - bottom_range / (total_drop + _EPS)
        return descent_frac * sharpness
    return close.rolling(63, min_periods=30).apply(_sharp_v, raw=True)


def dsh_ext_011_sharp_v_bottom_score_126d(close: pd.Series) -> pd.Series:
    """Sharp-V bottom score over 126d window."""
    def _sharp_v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        total_drop = y[0] - y.min()
        if total_drop < _EPS:
            return 0.0
        first_drop = y[0] - y[m]
        descent_frac = first_drop / total_drop
        lo = max(0, m - 2)
        hi = min(n, m + 3)
        bottom_range = y[lo:hi].max() - y[lo:hi].min()
        sharpness = 1.0 - bottom_range / (total_drop + _EPS)
        return descent_frac * sharpness
    return close.rolling(126, min_periods=60).apply(_sharp_v, raw=True)


# --- Group C: Segment-wise slope decomposition (first/middle/last-third) ---

def dsh_ext_012_first_third_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of the first third of the 63d window — initial descent rate."""
    def _s1(y):
        n = len(y)
        if n < 6:
            return np.nan
        seg = y[:n // 3]
        if len(seg) < 2:
            return np.nan
        x = np.arange(len(seg), dtype=float)
        xi = x - x.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, seg - seg.mean()) / denom if denom > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_s1, raw=True)


def dsh_ext_013_middle_third_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of the middle third of the 63d window — mid-decline rate."""
    def _s2(y):
        n = len(y)
        if n < 6:
            return np.nan
        t1, t2 = n // 3, 2 * n // 3
        seg = y[t1:t2]
        if len(seg) < 2:
            return np.nan
        x = np.arange(len(seg), dtype=float)
        xi = x - x.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, seg - seg.mean()) / denom if denom > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_s2, raw=True)


def dsh_ext_014_last_third_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of the last third of the 63d window — terminal velocity."""
    def _s3(y):
        n = len(y)
        if n < 6:
            return np.nan
        seg = y[2 * n // 3:]
        if len(seg) < 2:
            return np.nan
        x = np.arange(len(seg), dtype=float)
        xi = x - x.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, seg - seg.mean()) / denom if denom > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_s3, raw=True)


def dsh_ext_015_first_to_last_slope_ratio_63d(close: pd.Series) -> pd.Series:
    """First-third slope / last-third slope over 63d — >1 = front-loaded descent;
    <1 = accelerating into period end."""
    s1 = dsh_ext_012_first_third_slope_63d(close)
    s3 = dsh_ext_014_last_third_slope_63d(close)
    return _safe_div(s1, s3)


def dsh_ext_016_middle_to_first_slope_ratio_63d(close: pd.Series) -> pd.Series:
    """Middle-third slope / first-third slope over 63d — did the middle leg
    accelerate or decelerate relative to the initial leg."""
    s2 = dsh_ext_013_middle_third_slope_63d(close)
    s1 = dsh_ext_012_first_third_slope_63d(close)
    return _safe_div(s2, s1)


def dsh_ext_017_segment_slope_std_63d(close: pd.Series) -> pd.Series:
    """Standard deviation of the three segment slopes (first/mid/last third)
    over 63d — high = highly non-uniform descent; low = steady uniform slope."""
    def _seg_std(y):
        n = len(y)
        if n < 9:
            return np.nan
        segs = [y[:n // 3], y[n // 3: 2 * n // 3], y[2 * n // 3:]]
        slopes = []
        for seg in segs:
            if len(seg) < 2:
                continue
            x = np.arange(len(seg), dtype=float)
            xi = x - x.mean()
            denom = np.dot(xi, xi)
            if denom > _EPS:
                slopes.append(np.dot(xi, seg - seg.mean()) / denom)
        return float(np.std(slopes)) if len(slopes) >= 2 else np.nan
    return close.rolling(63, min_periods=30).apply(_seg_std, raw=True)


def dsh_ext_018_first_third_slope_126d(close: pd.Series) -> pd.Series:
    """OLS slope of the first third of the 126d window."""
    def _s1(y):
        n = len(y)
        if n < 6:
            return np.nan
        seg = y[:n // 3]
        if len(seg) < 2:
            return np.nan
        x = np.arange(len(seg), dtype=float)
        xi = x - x.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, seg - seg.mean()) / denom if denom > _EPS else np.nan
    return close.rolling(126, min_periods=60).apply(_s1, raw=True)


def dsh_ext_019_last_third_slope_126d(close: pd.Series) -> pd.Series:
    """OLS slope of the last third of the 126d window."""
    def _s3(y):
        n = len(y)
        if n < 6:
            return np.nan
        seg = y[2 * n // 3:]
        if len(seg) < 2:
            return np.nan
        x = np.arange(len(seg), dtype=float)
        xi = x - x.mean()
        denom = np.dot(xi, xi)
        return np.dot(xi, seg - seg.mean()) / denom if denom > _EPS else np.nan
    return close.rolling(126, min_periods=60).apply(_s3, raw=True)


def dsh_ext_020_first_to_last_slope_ratio_126d(close: pd.Series) -> pd.Series:
    """First-third / last-third slope ratio over 126d."""
    s1 = dsh_ext_018_first_third_slope_126d(close)
    s3 = dsh_ext_019_last_third_slope_126d(close)
    return _safe_div(s1, s3)


# --- Group D: Path shape symmetry / asymmetry ---

def dsh_ext_021_decline_path_symmetry_63d(close: pd.Series) -> pd.Series:
    """Shape symmetry over 63d: Pearson correlation of the price path with its
    own time-reversal. +1 = perfectly symmetric; -1 = fully asymmetric."""
    def _sym(y):
        n = len(y)
        if n < 4:
            return np.nan
        y_rev = y[::-1]
        a = y - y.mean()
        b = y_rev - y_rev.mean()
        denom = np.sqrt(np.dot(a, a) * np.dot(b, b))
        return np.dot(a, b) / denom if denom > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_sym, raw=True)


def dsh_ext_022_decline_path_symmetry_126d(close: pd.Series) -> pd.Series:
    """Shape symmetry over 126d — correlation with time-reversal."""
    def _sym(y):
        n = len(y)
        if n < 4:
            return np.nan
        y_rev = y[::-1]
        a = y - y.mean()
        b = y_rev - y_rev.mean()
        denom = np.sqrt(np.dot(a, a) * np.dot(b, b))
        return np.dot(a, b) / denom if denom > _EPS else np.nan
    return close.rolling(126, min_periods=60).apply(_sym, raw=True)


def dsh_ext_023_left_right_variance_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Variance of first half / variance of second half over 63d.
    >1 = volatile early then calmer; <1 = calm then volatile."""
    def _var_asym(y):
        n = len(y)
        if n < 4:
            return np.nan
        m = n // 2
        v1 = np.var(y[:m])
        v2 = np.var(y[m:])
        return v1 / v2 if v2 > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_var_asym, raw=True)


def dsh_ext_024_left_right_range_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Range of first half / range of second half over 63d.
    >1 = most price action concentrated early."""
    def _rng_asym(y):
        n = len(y)
        if n < 4:
            return np.nan
        m = n // 2
        r1 = y[:m].max() - y[:m].min()
        r2 = y[m:].max() - y[m:].min()
        return r1 / r2 if r2 > _EPS else np.nan
    return close.rolling(63, min_periods=30).apply(_rng_asym, raw=True)


def dsh_ext_025_min_position_in_window_63d(close: pd.Series) -> pd.Series:
    """Normalised time position of window minimum within 63d: 0 = at the start,
    1 = at the end. Near 0.5 = symmetric U-shape bottom."""
    def _min_pos(y):
        n = len(y)
        if n < 2:
            return np.nan
        return float(np.argmin(y)) / (n - 1)
    return close.rolling(63, min_periods=30).apply(_min_pos, raw=True)


def dsh_ext_026_min_position_in_window_126d(close: pd.Series) -> pd.Series:
    """Normalised time position of minimum within 126d window."""
    def _min_pos(y):
        n = len(y)
        if n < 2:
            return np.nan
        return float(np.argmin(y)) / (n - 1)
    return close.rolling(126, min_periods=60).apply(_min_pos, raw=True)


# --- Group E: Curvature sign distribution and shape entropy ---

def dsh_ext_027_curvature_sign_fraction_pos_63d(close: pd.Series) -> pd.Series:
    """Fraction of 5-day sub-windows within 63d where quadratic coefficient > 0
    (concave-up / decelerating decline)."""
    def _pos_frac(y):
        n = len(y)
        if n < 10:
            return np.nan
        signs = []
        for i in range(0, n - 4, 3):
            seg = y[i:i + 5]
            x = np.arange(5, dtype=float)
            try:
                c = np.polyfit(x, seg, 2)[0]
                signs.append(1.0 if c > 0 else 0.0)
            except Exception:
                pass
        return float(np.mean(signs)) if signs else np.nan
    return close.rolling(63, min_periods=30).apply(_pos_frac, raw=True)


def dsh_ext_028_curvature_sign_fraction_pos_126d(close: pd.Series) -> pd.Series:
    """Fraction of 7-day sub-windows within 126d with positive quadratic coef."""
    def _pos_frac(y):
        n = len(y)
        if n < 14:
            return np.nan
        signs = []
        for i in range(0, n - 6, 5):
            seg = y[i:i + 7]
            x = np.arange(7, dtype=float)
            try:
                c = np.polyfit(x, seg, 2)[0]
                signs.append(1.0 if c > 0 else 0.0)
            except Exception:
                pass
        return float(np.mean(signs)) if signs else np.nan
    return close.rolling(126, min_periods=60).apply(_pos_frac, raw=True)


def dsh_ext_029_path_shape_entropy_63d(close: pd.Series) -> pd.Series:
    """Entropy of the normalised price path shape over 63d (8 bins). High = complex
    multi-level path; low = clean single-direction shape."""
    def _shape_ent(y):
        n = len(y)
        if n < 8:
            return np.nan
        rng = y.max() - y.min()
        if rng < _EPS:
            return 0.0
        yn = (y - y.min()) / rng
        h, _ = np.histogram(yn, bins=8, range=(0.0, 1.0))
        h = h[h > 0].astype(float)
        h /= h.sum()
        return float(-np.sum(h * np.log(h + _EPS)))
    return close.rolling(63, min_periods=30).apply(_shape_ent, raw=True)


def dsh_ext_030_path_shape_entropy_126d(close: pd.Series) -> pd.Series:
    """Path-shape entropy over 126d window with 10 bins."""
    def _shape_ent(y):
        n = len(y)
        if n < 10:
            return np.nan
        rng = y.max() - y.min()
        if rng < _EPS:
            return 0.0
        yn = (y - y.min()) / rng
        h, _ = np.histogram(yn, bins=10, range=(0.0, 1.0))
        h = h[h > 0].astype(float)
        h /= h.sum()
        return float(-np.sum(h * np.log(h + _EPS)))
    return close.rolling(126, min_periods=60).apply(_shape_ent, raw=True)


def dsh_ext_031_curvature_entropy_63d(close: pd.Series) -> pd.Series:
    """Entropy of the distribution of quadratic coefficients over overlapping 7-day
    sub-windows within the 63d window. High = varied curvature structure."""
    def _curv_ent(y):
        n = len(y)
        if n < 14:
            return np.nan
        coefs = []
        for i in range(0, n - 6, 2):
            seg = y[i:i + 7]
            x = np.arange(7, dtype=float)
            try:
                coefs.append(np.polyfit(x, seg, 2)[0])
            except Exception:
                pass
        if len(coefs) < 3:
            return np.nan
        coefs = np.array(coefs)
        bins = min(6, len(coefs) // 2)
        h, _ = np.histogram(coefs, bins=bins)
        h = h[h > 0].astype(float)
        h /= h.sum()
        return float(-np.sum(h * np.log(h + _EPS)))
    return close.rolling(63, min_periods=30).apply(_curv_ent, raw=True)


# --- Group F: Piecewise-linear residuals (two-segment fit) ---

def dsh_ext_032_piecewise_linear_rmse_63d(close: pd.Series) -> pd.Series:
    """RMSE of optimal two-segment piecewise-linear fit over 63d. Lower than
    single-segment RMSE implies a kink in the decline path."""
    def _pw_rmse(y):
        n = len(y)
        if n < 6:
            return np.nan
        x = np.arange(n, dtype=float)
        best = np.inf
        for bp in range(2, n - 2):
            def _sr(xs, ys):
                xm, ym = xs.mean(), ys.mean()
                xi = xs - xm
                d = np.dot(xi, xi)
                b = np.dot(xi, ys - ym) / d if d > _EPS else 0.0
                a = ym - b * xm
                return np.sum((ys - (a + b * xs)) ** 2)
            r = _sr(x[:bp], y[:bp]) + _sr(x[bp:], y[bp:])
            if r < best:
                best = r
        return np.sqrt(best / n)
    return close.rolling(63, min_periods=30).apply(_pw_rmse, raw=True)


def dsh_ext_033_piecewise_vs_linear_rmse_ratio_63d(close: pd.Series) -> pd.Series:
    """Piecewise-linear RMSE / single-linear RMSE over 63d — <1 means a kink
    significantly improves fit; near 1 = monotone-linear decline."""
    pw = dsh_ext_032_piecewise_linear_rmse_63d(close)
    lin = _roll_lin_rmse(close, 63)
    return _safe_div(pw, lin)


def dsh_ext_034_piecewise_kink_position_63d(close: pd.Series) -> pd.Series:
    """Normalised position [0,1] of the optimal piecewise kink within the 63d
    window — tells whether acceleration/deceleration occurs early or late."""
    def _kink_pos(y):
        n = len(y)
        if n < 6:
            return np.nan
        x = np.arange(n, dtype=float)
        best_r, best_bp = np.inf, 2
        for bp in range(2, n - 2):
            def _sr(xs, ys):
                xm, ym = xs.mean(), ys.mean()
                xi = xs - xm
                d = np.dot(xi, xi)
                b = np.dot(xi, ys - ym) / d if d > _EPS else 0.0
                a = ym - b * xm
                return np.sum((ys - (a + b * xs)) ** 2)
            r = _sr(x[:bp], y[:bp]) + _sr(x[bp:], y[bp:])
            if r < best_r:
                best_r = r
                best_bp = bp
        return float(best_bp) / (n - 1)
    return close.rolling(63, min_periods=30).apply(_kink_pos, raw=True)


# --- Group G: Z-score and percentile-rank transforms of shape metrics ---

def dsh_ext_035_quad_coef_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of the 63d quadratic coefficient over a 252d rolling window —
    how extreme is current curvature vs the past year."""
    q63 = _roll_quad_coef(close, 63)
    mu = q63.rolling(252, min_periods=120).mean()
    sd = q63.rolling(252, min_periods=120).std()
    return _safe_div(q63 - mu, sd)


def dsh_ext_036_linear_r2_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63d linear R^2 over 252d rolling window."""
    r63 = _roll_r2(close, 63)
    mu = r63.rolling(252, min_periods=120).mean()
    sd = r63.rolling(252, min_periods=120).std()
    return _safe_div(r63 - mu, sd)


def dsh_ext_037_jaggedness_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63d path jaggedness (arc/chord) over 252d rolling window."""
    arc = close.diff().abs().rolling(63, min_periods=30).sum()
    chord = (close - close.shift(62)).abs()
    jag = _safe_div(arc, chord)
    mu = jag.rolling(252, min_periods=120).mean()
    sd = jag.rolling(252, min_periods=120).std()
    return _safe_div(jag - mu, sd)


def dsh_ext_038_v_shape_score_percentile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of the 63d V-shape descent score vs trailing 252d history.
    0 = least V-shape; 1 = sharpest V seen in the past year."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        try:
            s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
            s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        except Exception:
            return np.nan
        return s1 - s2
    v_score = close.rolling(63, min_periods=30).apply(_v, raw=True)
    def _pct(y):
        valid = y[~np.isnan(y)]
        if len(valid) < 2:
            return np.nan
        return float(np.mean(valid < valid[-1]))
    return v_score.rolling(252, min_periods=120).apply(_pct, raw=True)


def dsh_ext_039_drawdown_convexity_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of mean/max drawdown ratio (63d) over 252d history."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    conv = _safe_div(dd.rolling(63, min_periods=30).mean(),
                     dd.rolling(63, min_periods=30).max())
    mu = conv.rolling(252, min_periods=120).mean()
    sd = conv.rolling(252, min_periods=120).std()
    return _safe_div(conv - mu, sd)


def dsh_ext_040_path_shape_entropy_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63d path-shape entropy over 252d rolling window."""
    ent = dsh_ext_029_path_shape_entropy_63d(close)
    mu = ent.rolling(252, min_periods=120).mean()
    sd = ent.rolling(252, min_periods=120).std()
    return _safe_div(ent - mu, sd)


# --- Group H: Regime flags based on shape thresholds ---

def dsh_ext_041_v_shape_regime_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: 1 if current 63d V-shape score is in the top-20th-percentile
    vs trailing 252d distribution (extreme sharp-reversal mode)."""
    def _v(y):
        n = len(y)
        if n < 6:
            return np.nan
        m = n // 2
        try:
            s1 = np.polyfit(np.arange(m, dtype=float), y[:m], 1)[0] if m > 1 else 0.0
            s2 = np.polyfit(np.arange(n - m, dtype=float), y[m:], 1)[0] if (n - m) > 1 else 0.0
        except Exception:
            return np.nan
        return s1 - s2
    v_score = close.rolling(63, min_periods=30).apply(_v, raw=True)
    p80 = v_score.rolling(252, min_periods=120).quantile(0.80)
    return (v_score > p80).astype(float)


def dsh_ext_042_high_jaggedness_regime_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: 1 if 63d jaggedness is in the top-20th-percentile vs trailing
    252d (choppy decline regime)."""
    arc = close.diff().abs().rolling(63, min_periods=30).sum()
    chord = (close - close.shift(62)).abs()
    jag = _safe_div(arc, chord)
    p80 = jag.rolling(252, min_periods=120).quantile(0.80)
    return (jag > p80).astype(float)


def dsh_ext_043_concave_curvature_regime_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: 1 if 63d quadratic coefficient is in the bottom-20th-percentile
    (strongly negative curvature = accelerating decline)."""
    q63 = _roll_quad_coef(close, 63)
    p20 = q63.rolling(252, min_periods=120).quantile(0.20)
    return (q63 < p20).astype(float)


def dsh_ext_044_low_linearity_regime_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: 1 if 63d linear R^2 is in the bottom-20th-percentile
    (highly non-linear/disorderly decline)."""
    r63 = _roll_r2(close, 63)
    p20 = r63.rolling(252, min_periods=120).quantile(0.20)
    return (r63 < p20).astype(float)


# --- Group I: Rate-of-change / acceleration of extended shape metrics ---

def dsh_ext_045_cubic_coef_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in cubic polynomial coefficient (63d) — rate of change of
    the S-curve inflection structure."""
    return dsh_ext_001_cubic_coef_price_63d(close).diff(5)


def dsh_ext_046_u_shape_score_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in U-shape score (63d) — is the U deepening or filling."""
    return dsh_ext_006_u_shape_score_63d(close).diff(5)


def dsh_ext_047_segment_slope_std_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in segment-slope standard deviation (63d) — is slope
    non-uniformity increasing or resolving."""
    return dsh_ext_017_segment_slope_std_63d(close).diff(5)


def dsh_ext_048_path_symmetry_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in 63d decline-path symmetry score."""
    return dsh_ext_021_decline_path_symmetry_63d(close).diff(5)


def dsh_ext_049_min_position_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in normalised minimum position (63d) — is the bottom point
    migrating toward period end (bottoming process)."""
    return dsh_ext_025_min_position_in_window_63d(close).diff(5)


def dsh_ext_050_path_shape_entropy_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in path-shape entropy (63d) — is the decline becoming more
    or less structurally complex."""
    return dsh_ext_029_path_shape_entropy_63d(close).diff(5)


def dsh_ext_051_curvature_pos_frac_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in fraction of sub-windows with positive curvature (63d) —
    is decelerating-curvature structure increasing."""
    return dsh_ext_027_curvature_sign_fraction_pos_63d(close).diff(5)


def dsh_ext_052_piecewise_kink_position_roc_63d(close: pd.Series) -> pd.Series:
    """5-day change in piecewise-linear kink position (63d) — is the structural
    kink migrating toward the present."""
    return dsh_ext_034_piecewise_kink_position_63d(close).diff(5)


# --- Group J: Smoothness metrics and Hurst-like persistence ---

def dsh_ext_053_signed_curvature_sum_63d(close: pd.Series) -> pd.Series:
    """Rolling sum of sign(second-finite-difference of close) over 63d.
    Positive = net convex path; negative = net concave (accelerating down)."""
    d2 = close.diff().diff()
    return np.sign(d2).rolling(63, min_periods=30).sum()


def dsh_ext_054_signed_curvature_sum_126d(close: pd.Series) -> pd.Series:
    """Signed curvature sum over 126d."""
    d2 = close.diff().diff()
    return np.sign(d2).rolling(126, min_periods=60).sum()


def dsh_ext_055_convex_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63d days where second finite difference of close > 0
    (locally decelerating / convex curvature)."""
    d2 = close.diff().diff()
    return (d2 > 0).astype(float).rolling(63, min_periods=30).mean()


def dsh_ext_056_concave_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63d days where second finite difference < 0
    (locally accelerating down / concave curvature)."""
    d2 = close.diff().diff()
    return (d2 < 0).astype(float).rolling(63, min_periods=30).mean()


def dsh_ext_057_rescaled_range_63d(close: pd.Series) -> pd.Series:
    """Rescaled range R/S of daily returns over 63d — a Hurst-related measure;
    high = persistent trending decline, low = mean-reverting choppiness."""
    ret = close.pct_change()
    def _rs(y):
        y = y[~np.isnan(y)]
        if len(y) < 4:
            return np.nan
        cum_dev = np.cumsum(y - y.mean())
        R = cum_dev.max() - cum_dev.min()
        S = y.std()
        return R / S if S > _EPS else np.nan
    return ret.rolling(63, min_periods=30).apply(_rs, raw=True)


def dsh_ext_058_rescaled_range_126d(close: pd.Series) -> pd.Series:
    """Rescaled range R/S of daily returns over 126d."""
    ret = close.pct_change()
    def _rs(y):
        y = y[~np.isnan(y)]
        if len(y) < 4:
            return np.nan
        cum_dev = np.cumsum(y - y.mean())
        R = cum_dev.max() - cum_dev.min()
        S = y.std()
        return R / S if S > _EPS else np.nan
    return ret.rolling(126, min_periods=60).apply(_rs, raw=True)


def dsh_ext_059_path_smoothness_ratio_21d(close: pd.Series) -> pd.Series:
    """Total variation of 3-day MA / total variation of raw close over 21d.
    Near 1 = already smooth; low = raw path much choppier than its trend."""
    smooth = close.rolling(3, min_periods=2, center=True).mean()
    raw_tv = close.diff().abs().rolling(21, min_periods=10).sum()
    smooth_tv = smooth.diff().abs().rolling(21, min_periods=10).sum()
    return _safe_div(smooth_tv, raw_tv)


def dsh_ext_060_path_smoothness_ratio_63d(close: pd.Series) -> pd.Series:
    """Total variation of 5-day MA / total variation of raw close over 63d."""
    smooth = close.rolling(5, min_periods=3).mean()
    raw_tv = close.diff().abs().rolling(63, min_periods=30).sum()
    smooth_tv = smooth.diff().abs().rolling(63, min_periods=30).sum()
    return _safe_div(smooth_tv, raw_tv)


# --- Group K: Volume-shape extended features ---

def dsh_ext_061_volume_curvature_sign_agreement_63d(close: pd.Series,
                                                      volume: pd.Series) -> pd.Series:
    """Sign agreement between quadratic coef of close and of volume over 63d.
    +1 = both concave-up or both concave-down; -1 = diverging curvature."""
    qc = _roll_quad_coef(close, 63)
    qv = _roll_quad_coef(volume, 63)
    return np.sign(qc) * np.sign(qv)


def dsh_ext_062_vol_weighted_segment_slope_ratio_63d(close: pd.Series,
                                                       volume: pd.Series) -> pd.Series:
    """Volume-weighted first-third slope / volume-weighted last-third slope (63d).
    >1 = heavy-volume sessions dominated the beginning of the decline."""
    def _vw_slope(ys, vs):
        n = len(ys)
        if n < 2:
            return np.nan
        tot_v = vs.sum()
        if tot_v < _EPS:
            return np.nan
        ws = vs / tot_v
        xw = np.arange(n, dtype=float)
        xwm = np.sum(ws * xw)
        ywm = np.sum(ws * ys)
        num = np.sum(ws * (xw - xwm) * (ys - ywm))
        den = np.sum(ws * (xw - xwm) ** 2)
        return num / den if den > _EPS else np.nan

    result = pd.Series(np.nan, index=close.index)
    n_total = len(close)
    for i in range(63, n_total + 1):
        wc = close.iloc[i - 63:i].values
        wv = volume.iloc[i - 63:i].values
        n = len(wc)
        t1, t2 = n // 3, 2 * n // 3
        s1 = _vw_slope(wc[:t1], wv[:t1])
        s3 = _vw_slope(wc[t2:], wv[t2:])
        if s1 is not None and s3 is not None and not np.isnan(s1) and not np.isnan(s3) and abs(s3) > _EPS:
            result.iloc[i - 1] = s1 / s3
    return result


def dsh_ext_063_down_vol_curvature_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Quadratic coefficient of down-day volume (forward-filled) series over 63d.
    Positive = down-day volume decelerating (selling exhaustion); negative = panic."""
    dc = close.diff()
    down_v = volume.where(dc < 0, other=np.nan).ffill()
    return _roll_quad_coef(down_v, 63)


# --- Group L: High-low structure extended shape ---

def dsh_ext_064_hl_range_symmetry_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Correlation of daily H-L range series with its time-reversal over 63d.
    Near +1 = symmetric volatility expansion; near -1 = front- or back-loaded."""
    rng = high - low
    def _sym(y):
        n = len(y)
        if n < 4:
            return np.nan
        y_rev = y[::-1]
        a = y - y.mean()
        b = y_rev - y_rev.mean()
        denom = np.sqrt(np.dot(a, a) * np.dot(b, b))
        return np.dot(a, b) / denom if denom > _EPS else np.nan
    return rng.rolling(63, min_periods=30).apply(_sym, raw=True)


def dsh_ext_065_hl_range_skewness_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Skewness of daily H-L range over 63d — positive = occasional giant-range
    days; negative = compressing ranges."""
    rng = high - low
    return rng.rolling(63, min_periods=20).skew()


def dsh_ext_066_hl_midpoint_symmetry_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Correlation of H-L midpoint series with its time-reversal over 63d."""
    mid = (high + low) / 2.0
    def _sym(y):
        n = len(y)
        if n < 4:
            return np.nan
        y_rev = y[::-1]
        a = y - y.mean()
        b = y_rev - y_rev.mean()
        denom = np.sqrt(np.dot(a, a) * np.dot(b, b))
        return np.dot(a, b) / denom if denom > _EPS else np.nan
    return mid.rolling(63, min_periods=30).apply(_sym, raw=True)


def dsh_ext_067_close_vs_midpoint_trend_63d(close: pd.Series, high: pd.Series,
                                              low: pd.Series) -> pd.Series:
    """Slope of (close - H-L midpoint) over 63d — persistent negative = close
    drifting to lower half of daily range (bearish intraday evolution)."""
    bias = close - (high + low) / 2.0
    return _roll_slope(bias, 63)


def dsh_ext_068_open_close_range_fraction_slope_63d(open: pd.Series,
                                                      close: pd.Series,
                                                      high: pd.Series,
                                                      low: pd.Series) -> pd.Series:
    """Slope of daily |close-open|/(high-low) over 63d — trend in how much of the
    daily range is captured by the body (increasing = more decisive sessions)."""
    rng = (high - low).replace(0, np.nan)
    body_frac = (close - open).abs() / rng
    return _roll_slope(body_frac, 63)


# --- Group M: Statistical shape cross-section (return distribution metrics) ---

def dsh_ext_069_return_range_63d(close: pd.Series) -> pd.Series:
    """Max daily return minus min daily return over 63d — total return spread."""
    ret = close.pct_change()
    return (ret.rolling(63, min_periods=30).max() -
            ret.rolling(63, min_periods=30).min())


def dsh_ext_070_return_interquartile_range_63d(close: pd.Series) -> pd.Series:
    """IQR of daily returns over 63d — robust return spread less affected by
    extreme outlier days than standard deviation."""
    ret = close.pct_change()
    q75 = ret.rolling(63, min_periods=20).quantile(0.75)
    q25 = ret.rolling(63, min_periods=20).quantile(0.25)
    return q75 - q25


def dsh_ext_071_negative_return_concentration_63d(close: pd.Series) -> pd.Series:
    """Sum of squared negative returns / sum of squared all returns over 63d.
    >0.5 = return variance dominated by down-side sessions."""
    ret = close.pct_change()
    neg_sq = (ret.clip(upper=0) ** 2).rolling(63, min_periods=20).sum()
    tot_sq = (ret ** 2).rolling(63, min_periods=20).sum()
    return _safe_div(neg_sq, tot_sq)


def dsh_ext_072_gain_loss_ratio_63d(close: pd.Series) -> pd.Series:
    """Mean positive daily return / mean absolute negative daily return over 63d.
    <1 = losses outpace gains on average."""
    ret = close.pct_change()
    gains = ret.where(ret > 0).rolling(63, min_periods=10).mean()
    losses = ret.where(ret < 0).abs().rolling(63, min_periods=10).mean()
    return _safe_div(gains, losses)


def dsh_ext_073_median_vs_mean_return_63d(close: pd.Series) -> pd.Series:
    """Median daily return / mean daily return over 63d. Departs from 1 when
    extreme sessions distort the mean (panic days pull mean below median)."""
    ret = close.pct_change()
    med = ret.rolling(63, min_periods=20).median()
    mn = ret.rolling(63, min_periods=20).mean()
    return _safe_div(med, mn.replace(0, np.nan))


def dsh_ext_074_tail_to_body_ratio_63d(close: pd.Series) -> pd.Series:
    """(|p5 return| + |p95 return|) / (|p25 return| + |p75 return|) over 63d.
    Tail fatness relative to the IQR body — high = fat-tailed decline."""
    ret = close.pct_change()
    p5  = ret.rolling(63, min_periods=20).quantile(0.05).abs()
    p95 = ret.rolling(63, min_periods=20).quantile(0.95).abs()
    p25 = ret.rolling(63, min_periods=20).quantile(0.25).abs()
    p75 = ret.rolling(63, min_periods=20).quantile(0.75).abs()
    return _safe_div(p5 + p95, p25 + p75)


def dsh_ext_075_drawdown_depth_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of the current 21d maximum drawdown vs the trailing 252d
    distribution of 21d max drawdowns. 1.0 = worst seen in the past year."""
    h21 = _roll_max(close, 21)
    dd21 = (h21 - close) / h21.replace(0, np.nan)
    max_dd21 = dd21.rolling(21, min_periods=10).max()
    def _pct(y):
        valid = y[~np.isnan(y)]
        if len(valid) < 2:
            return np.nan
        return float(np.mean(valid <= valid[-1]))
    return max_dd21.rolling(252, min_periods=120).apply(_pct, raw=True)


# ── Registry ───────────────────────────────────────────────────────────────────

DRAWDOWN_SHAPE_EXTENDED_REGISTRY_001_075 = {
    "dsh_ext_001_cubic_coef_price_63d":                {"inputs": ["close"],                         "func": dsh_ext_001_cubic_coef_price_63d},
    "dsh_ext_002_cubic_coef_price_126d":               {"inputs": ["close"],                         "func": dsh_ext_002_cubic_coef_price_126d},
    "dsh_ext_003_cubic_rmse_vs_quad_rmse_63d":         {"inputs": ["close"],                         "func": dsh_ext_003_cubic_rmse_vs_quad_rmse_63d},
    "dsh_ext_004_cubic_linear_coef_63d":               {"inputs": ["close"],                         "func": dsh_ext_004_cubic_linear_coef_63d},
    "dsh_ext_005_cubic_r2_improvement_63d":            {"inputs": ["close"],                         "func": dsh_ext_005_cubic_r2_improvement_63d},
    "dsh_ext_006_u_shape_score_63d":                   {"inputs": ["close"],                         "func": dsh_ext_006_u_shape_score_63d},
    "dsh_ext_007_u_shape_score_126d":                  {"inputs": ["close"],                         "func": dsh_ext_007_u_shape_score_126d},
    "dsh_ext_008_l_shape_score_63d":                   {"inputs": ["close"],                         "func": dsh_ext_008_l_shape_score_63d},
    "dsh_ext_009_w_shape_score_63d":                   {"inputs": ["close"],                         "func": dsh_ext_009_w_shape_score_63d},
    "dsh_ext_010_sharp_v_bottom_score_63d":            {"inputs": ["close"],                         "func": dsh_ext_010_sharp_v_bottom_score_63d},
    "dsh_ext_011_sharp_v_bottom_score_126d":           {"inputs": ["close"],                         "func": dsh_ext_011_sharp_v_bottom_score_126d},
    "dsh_ext_012_first_third_slope_63d":               {"inputs": ["close"],                         "func": dsh_ext_012_first_third_slope_63d},
    "dsh_ext_013_middle_third_slope_63d":              {"inputs": ["close"],                         "func": dsh_ext_013_middle_third_slope_63d},
    "dsh_ext_014_last_third_slope_63d":                {"inputs": ["close"],                         "func": dsh_ext_014_last_third_slope_63d},
    "dsh_ext_015_first_to_last_slope_ratio_63d":       {"inputs": ["close"],                         "func": dsh_ext_015_first_to_last_slope_ratio_63d},
    "dsh_ext_016_middle_to_first_slope_ratio_63d":     {"inputs": ["close"],                         "func": dsh_ext_016_middle_to_first_slope_ratio_63d},
    "dsh_ext_017_segment_slope_std_63d":               {"inputs": ["close"],                         "func": dsh_ext_017_segment_slope_std_63d},
    "dsh_ext_018_first_third_slope_126d":              {"inputs": ["close"],                         "func": dsh_ext_018_first_third_slope_126d},
    "dsh_ext_019_last_third_slope_126d":               {"inputs": ["close"],                         "func": dsh_ext_019_last_third_slope_126d},
    "dsh_ext_020_first_to_last_slope_ratio_126d":      {"inputs": ["close"],                         "func": dsh_ext_020_first_to_last_slope_ratio_126d},
    "dsh_ext_021_decline_path_symmetry_63d":           {"inputs": ["close"],                         "func": dsh_ext_021_decline_path_symmetry_63d},
    "dsh_ext_022_decline_path_symmetry_126d":          {"inputs": ["close"],                         "func": dsh_ext_022_decline_path_symmetry_126d},
    "dsh_ext_023_left_right_variance_asymmetry_63d":   {"inputs": ["close"],                         "func": dsh_ext_023_left_right_variance_asymmetry_63d},
    "dsh_ext_024_left_right_range_asymmetry_63d":      {"inputs": ["close"],                         "func": dsh_ext_024_left_right_range_asymmetry_63d},
    "dsh_ext_025_min_position_in_window_63d":          {"inputs": ["close"],                         "func": dsh_ext_025_min_position_in_window_63d},
    "dsh_ext_026_min_position_in_window_126d":         {"inputs": ["close"],                         "func": dsh_ext_026_min_position_in_window_126d},
    "dsh_ext_027_curvature_sign_fraction_pos_63d":     {"inputs": ["close"],                         "func": dsh_ext_027_curvature_sign_fraction_pos_63d},
    "dsh_ext_028_curvature_sign_fraction_pos_126d":    {"inputs": ["close"],                         "func": dsh_ext_028_curvature_sign_fraction_pos_126d},
    "dsh_ext_029_path_shape_entropy_63d":              {"inputs": ["close"],                         "func": dsh_ext_029_path_shape_entropy_63d},
    "dsh_ext_030_path_shape_entropy_126d":             {"inputs": ["close"],                         "func": dsh_ext_030_path_shape_entropy_126d},
    "dsh_ext_031_curvature_entropy_63d":               {"inputs": ["close"],                         "func": dsh_ext_031_curvature_entropy_63d},
    "dsh_ext_032_piecewise_linear_rmse_63d":           {"inputs": ["close"],                         "func": dsh_ext_032_piecewise_linear_rmse_63d},
    "dsh_ext_033_piecewise_vs_linear_rmse_ratio_63d":  {"inputs": ["close"],                         "func": dsh_ext_033_piecewise_vs_linear_rmse_ratio_63d},
    "dsh_ext_034_piecewise_kink_position_63d":         {"inputs": ["close"],                         "func": dsh_ext_034_piecewise_kink_position_63d},
    "dsh_ext_035_quad_coef_zscore_63d":                {"inputs": ["close"],                         "func": dsh_ext_035_quad_coef_zscore_63d},
    "dsh_ext_036_linear_r2_zscore_63d":                {"inputs": ["close"],                         "func": dsh_ext_036_linear_r2_zscore_63d},
    "dsh_ext_037_jaggedness_zscore_63d":               {"inputs": ["close"],                         "func": dsh_ext_037_jaggedness_zscore_63d},
    "dsh_ext_038_v_shape_score_percentile_63d":        {"inputs": ["close"],                         "func": dsh_ext_038_v_shape_score_percentile_63d},
    "dsh_ext_039_drawdown_convexity_zscore_63d":       {"inputs": ["close"],                         "func": dsh_ext_039_drawdown_convexity_zscore_63d},
    "dsh_ext_040_path_shape_entropy_zscore_63d":       {"inputs": ["close"],                         "func": dsh_ext_040_path_shape_entropy_zscore_63d},
    "dsh_ext_041_v_shape_regime_flag_63d":             {"inputs": ["close"],                         "func": dsh_ext_041_v_shape_regime_flag_63d},
    "dsh_ext_042_high_jaggedness_regime_flag_63d":     {"inputs": ["close"],                         "func": dsh_ext_042_high_jaggedness_regime_flag_63d},
    "dsh_ext_043_concave_curvature_regime_flag_63d":   {"inputs": ["close"],                         "func": dsh_ext_043_concave_curvature_regime_flag_63d},
    "dsh_ext_044_low_linearity_regime_flag_63d":       {"inputs": ["close"],                         "func": dsh_ext_044_low_linearity_regime_flag_63d},
    "dsh_ext_045_cubic_coef_roc_63d":                  {"inputs": ["close"],                         "func": dsh_ext_045_cubic_coef_roc_63d},
    "dsh_ext_046_u_shape_score_roc_63d":               {"inputs": ["close"],                         "func": dsh_ext_046_u_shape_score_roc_63d},
    "dsh_ext_047_segment_slope_std_roc_63d":           {"inputs": ["close"],                         "func": dsh_ext_047_segment_slope_std_roc_63d},
    "dsh_ext_048_path_symmetry_roc_63d":               {"inputs": ["close"],                         "func": dsh_ext_048_path_symmetry_roc_63d},
    "dsh_ext_049_min_position_roc_63d":                {"inputs": ["close"],                         "func": dsh_ext_049_min_position_roc_63d},
    "dsh_ext_050_path_shape_entropy_roc_63d":          {"inputs": ["close"],                         "func": dsh_ext_050_path_shape_entropy_roc_63d},
    "dsh_ext_051_curvature_pos_frac_roc_63d":          {"inputs": ["close"],                         "func": dsh_ext_051_curvature_pos_frac_roc_63d},
    "dsh_ext_052_piecewise_kink_position_roc_63d":     {"inputs": ["close"],                         "func": dsh_ext_052_piecewise_kink_position_roc_63d},
    "dsh_ext_053_signed_curvature_sum_63d":            {"inputs": ["close"],                         "func": dsh_ext_053_signed_curvature_sum_63d},
    "dsh_ext_054_signed_curvature_sum_126d":           {"inputs": ["close"],                         "func": dsh_ext_054_signed_curvature_sum_126d},
    "dsh_ext_055_convex_day_fraction_63d":             {"inputs": ["close"],                         "func": dsh_ext_055_convex_day_fraction_63d},
    "dsh_ext_056_concave_day_fraction_63d":            {"inputs": ["close"],                         "func": dsh_ext_056_concave_day_fraction_63d},
    "dsh_ext_057_rescaled_range_63d":                  {"inputs": ["close"],                         "func": dsh_ext_057_rescaled_range_63d},
    "dsh_ext_058_rescaled_range_126d":                 {"inputs": ["close"],                         "func": dsh_ext_058_rescaled_range_126d},
    "dsh_ext_059_path_smoothness_ratio_21d":           {"inputs": ["close"],                         "func": dsh_ext_059_path_smoothness_ratio_21d},
    "dsh_ext_060_path_smoothness_ratio_63d":           {"inputs": ["close"],                         "func": dsh_ext_060_path_smoothness_ratio_63d},
    "dsh_ext_061_volume_curvature_sign_agreement_63d": {"inputs": ["close", "volume"],               "func": dsh_ext_061_volume_curvature_sign_agreement_63d},
    "dsh_ext_062_vol_weighted_segment_slope_ratio_63d":{"inputs": ["close", "volume"],               "func": dsh_ext_062_vol_weighted_segment_slope_ratio_63d},
    "dsh_ext_063_down_vol_curvature_63d":              {"inputs": ["close", "volume"],               "func": dsh_ext_063_down_vol_curvature_63d},
    "dsh_ext_064_hl_range_symmetry_63d":               {"inputs": ["high", "low"],                   "func": dsh_ext_064_hl_range_symmetry_63d},
    "dsh_ext_065_hl_range_skewness_63d":               {"inputs": ["high", "low"],                   "func": dsh_ext_065_hl_range_skewness_63d},
    "dsh_ext_066_hl_midpoint_symmetry_63d":            {"inputs": ["high", "low"],                   "func": dsh_ext_066_hl_midpoint_symmetry_63d},
    "dsh_ext_067_close_vs_midpoint_trend_63d":         {"inputs": ["close", "high", "low"],          "func": dsh_ext_067_close_vs_midpoint_trend_63d},
    "dsh_ext_068_open_close_range_fraction_slope_63d": {"inputs": ["open", "close", "high", "low"],  "func": dsh_ext_068_open_close_range_fraction_slope_63d},
    "dsh_ext_069_return_range_63d":                    {"inputs": ["close"],                         "func": dsh_ext_069_return_range_63d},
    "dsh_ext_070_return_interquartile_range_63d":      {"inputs": ["close"],                         "func": dsh_ext_070_return_interquartile_range_63d},
    "dsh_ext_071_negative_return_concentration_63d":   {"inputs": ["close"],                         "func": dsh_ext_071_negative_return_concentration_63d},
    "dsh_ext_072_gain_loss_ratio_63d":                 {"inputs": ["close"],                         "func": dsh_ext_072_gain_loss_ratio_63d},
    "dsh_ext_073_median_vs_mean_return_63d":           {"inputs": ["close"],                         "func": dsh_ext_073_median_vs_mean_return_63d},
    "dsh_ext_074_tail_to_body_ratio_63d":              {"inputs": ["close"],                         "func": dsh_ext_074_tail_to_body_ratio_63d},
    "dsh_ext_075_drawdown_depth_percentile_252d":      {"inputs": ["close"],                         "func": dsh_ext_075_drawdown_depth_percentile_252d},
}
