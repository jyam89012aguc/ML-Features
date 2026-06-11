"""
03_drawdown_shape — Base Features 076-150
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
    """Rolling OLS slope via mean-centred dot products."""
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
    """Rolling autocorrelation at a given lag."""
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group L: Open-to-close shape within bars ---

def dsh_076_otc_negative_fraction_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 21d bars closing below their open — intrabar bearishness."""
    neg = (close < open).astype(float)
    return neg.rolling(21, min_periods=10).mean()


def dsh_077_otc_negative_fraction_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63d bars closing below their open."""
    neg = (close < open).astype(float)
    return neg.rolling(63, min_periods=30).mean()


def dsh_078_otc_body_size_trend_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of |close-open| / open over 63d — increasing body size = panic."""
    body = (close - open).abs() / open.replace(0, np.nan)
    return _roll_slope(body, 63)


def dsh_079_bearish_body_frac_of_range_21d(open: pd.Series, close: pd.Series,
                                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (open-close)/(high-low) on down bars over 21d — bigger = more fill
    of range on down days."""
    rng = (high - low).replace(0, np.nan)
    down = (close < open)
    body_frac = ((open - close) / rng).where(down)
    return body_frac.rolling(21, min_periods=7).mean()


def dsh_080_bearish_body_frac_of_range_63d(open: pd.Series, close: pd.Series,
                                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean bearish body fraction of range over 63d."""
    rng = (high - low).replace(0, np.nan)
    down = (close < open)
    body_frac = ((open - close) / rng).where(down)
    return body_frac.rolling(63, min_periods=20).mean()


def dsh_081_upper_shadow_fraction_21d(open: pd.Series, close: pd.Series,
                                       high: pd.Series) -> pd.Series:
    """Mean upper shadow / (high-max(open,close)) over 21d — rejection of highs."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    upper = (high - body_top).clip(lower=0)
    rng = high - pd.concat([open, close], axis=1).min(axis=1)
    frac = _safe_div(upper, rng.replace(0, np.nan))
    return frac.rolling(21, min_periods=10).mean()


def dsh_082_lower_shadow_fraction_21d(open: pd.Series, close: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """Mean lower shadow fraction over 21d — wicks below body."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    lower = (body_bot - low).clip(lower=0)
    rng = pd.concat([open, close], axis=1).max(axis=1) - low
    frac = _safe_div(lower, rng.replace(0, np.nan))
    return frac.rolling(21, min_periods=10).mean()


def dsh_083_lower_shadow_fraction_63d(open: pd.Series, close: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """Mean lower shadow fraction over 63d."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    lower = (body_bot - low).clip(lower=0)
    rng = pd.concat([open, close], axis=1).max(axis=1) - low
    frac = _safe_div(lower, rng.replace(0, np.nan))
    return frac.rolling(63, min_periods=20).mean()


# --- Group M: Drawdown path autocorrelation (momentum/mean-reversion structure) ---

def dsh_084_price_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over 21d — negative = mean
    reverting (bouncy), positive = trending (persistent decline)."""
    ret = close.pct_change()
    return _roll_autocorr(ret, 21, lag=1)


def dsh_085_price_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over 63d."""
    ret = close.pct_change()
    return _roll_autocorr(ret, 63, lag=1)


def dsh_086_price_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Lag-5 (weekly) autocorrelation of daily returns over 63d."""
    ret = close.pct_change()
    return _roll_autocorr(ret, 63, lag=5)


def dsh_087_price_autocorr_lag1_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of returns over 126d."""
    ret = close.pct_change()
    return _roll_autocorr(ret, 126, lag=1)


def dsh_088_drawdown_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of the drawdown level series over 63d — how sticky
    is the depth of drawdown day to day."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_autocorr(dd, 63, lag=1)


# --- Group N: Intraday range shape ---

def dsh_089_hl_range_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of daily H-L range over 21d — expanding ranges in decline."""
    rng = high - low
    return _roll_slope(rng, 21)


def dsh_090_hl_range_slope_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of daily H-L range over 63d."""
    rng = high - low
    return _roll_slope(rng, 63)


def dsh_091_hl_range_r2_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """R^2 of linear fit to daily H-L range over 63d — is range expanding
    steadily or erratically."""
    rng = high - low
    return _roll_r2(rng, 63)


def dsh_092_hl_range_quad_coef_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Quadratic coefficient of H-L range over 63d — accelerating expansion."""
    rng = high - low
    return _roll_quad_coef(rng, 63)


def dsh_093_true_range_slope_21d(close: pd.Series, high: pd.Series,
                                  low: pd.Series) -> pd.Series:
    """Slope of true range over 21d."""
    prev_c = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_c).abs(),
                    (low - prev_c).abs()], axis=1).max(axis=1)
    return _roll_slope(tr, 21)


def dsh_094_true_range_slope_63d(close: pd.Series, high: pd.Series,
                                  low: pd.Series) -> pd.Series:
    """Slope of true range over 63d."""
    prev_c = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_c).abs(),
                    (low - prev_c).abs()], axis=1).max(axis=1)
    return _roll_slope(tr, 63)


def dsh_095_true_range_r2_63d(close: pd.Series, high: pd.Series,
                               low: pd.Series) -> pd.Series:
    """R^2 of linear fit to true range over 63d."""
    prev_c = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_c).abs(),
                    (low - prev_c).abs()], axis=1).max(axis=1)
    return _roll_r2(tr, 63)


# --- Group O: Path-shape ratios using open/close gaps ---

def dsh_096_overnight_gap_slope_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of overnight gap (open/prev_close - 1) over 63d."""
    gap = open / close.shift(1) - 1.0
    return _roll_slope(gap, 63)


def dsh_097_overnight_gap_autocorr_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of overnight gaps over 63d — persistent gap-downs."""
    gap = open / close.shift(1) - 1.0
    return _roll_autocorr(gap, 63, lag=1)


def dsh_098_intraday_return_slope_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of intraday return (close/open - 1) over 63d — trend in intraday
    direction."""
    idr = close / open.replace(0, np.nan) - 1.0
    return _roll_slope(idr, 63)


def dsh_099_open_low_gap_fraction_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21d bars where low equals open (gapped down to open = worst
    case open)."""
    eq = ((open - low).abs() < 0.001 * open).astype(float)
    return eq.rolling(21, min_periods=10).mean()


def dsh_100_close_low_gap_fraction_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21d bars where close equals low (closes at worst = maximum
    bearish close structure)."""
    eq = ((close - low).abs() < 0.001 * close.clip(lower=_EPS)).astype(float)
    return eq.rolling(21, min_periods=10).mean()


# --- Group P: Drawdown path polynomial residuals ---

def dsh_101_drawdown_lin_rmse_63d(close: pd.Series) -> pd.Series:
    """RMSE of linear fit to the drawdown series (h-c)/h over 63d."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_lin_rmse(dd, 63)


def dsh_102_drawdown_lin_rmse_126d(close: pd.Series) -> pd.Series:
    """RMSE of linear fit to drawdown over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_lin_rmse(dd, 126)


def dsh_103_drawdown_quad_coef_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of drawdown path over 63d — positive = convex
    (drawdown decelerating), negative = concave (deepening)."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_quad_coef(dd, 63)


def dsh_104_drawdown_quad_coef_126d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of drawdown over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_quad_coef(dd, 126)


def dsh_105_drawdown_quad_coef_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of drawdown over 252d."""
    h = _roll_max(close, 252)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_quad_coef(dd, 252)


def dsh_106_drawdown_r2_63d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to drawdown path over 63d."""
    h = _roll_max(close, 63)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_r2(dd, 63)


def dsh_107_drawdown_r2_126d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to drawdown path over 126d."""
    h = _roll_max(close, 126)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_r2(dd, 126)


def dsh_108_drawdown_r2_252d(close: pd.Series) -> pd.Series:
    """R^2 of linear fit to drawdown path over 252d."""
    h = _roll_max(close, 252)
    dd = (h - close) / h.replace(0, np.nan)
    return _roll_r2(dd, 252)


# --- Group Q: Volume shape geometry ---

def dsh_109_volume_slope_21d(volume: pd.Series) -> pd.Series:
    """Slope of daily volume over 21d — rising volume = selling pressure."""
    return _roll_slope(volume, 21)


def dsh_110_volume_slope_63d(volume: pd.Series) -> pd.Series:
    """Slope of daily volume over 63d."""
    return _roll_slope(volume, 63)


def dsh_111_volume_r2_63d(volume: pd.Series) -> pd.Series:
    """R^2 of linear fit to volume over 63d — is volume expansion steady."""
    return _roll_r2(volume, 63)


def dsh_112_volume_quad_coef_63d(volume: pd.Series) -> pd.Series:
    """Quadratic coefficient of volume over 63d — accelerating volume."""
    return _roll_quad_coef(volume, 63)


def dsh_113_log_volume_slope_63d(volume: pd.Series) -> pd.Series:
    """Slope of log(volume) over 63d — percentage rate of volume growth."""
    lv = np.log(volume.clip(lower=1))
    return _roll_slope(lv, 63)


def dsh_114_volume_jaggedness_63d(volume: pd.Series) -> pd.Series:
    """Arc-length / chord of volume over 63d — is volume expansion smooth."""
    arc = volume.diff().abs().rolling(63, min_periods=30).sum()
    chord = (volume - volume.shift(62)).abs()
    return _safe_div(arc, chord)


def dsh_115_volume_first_third_share_63d(volume: pd.Series) -> pd.Series:
    """Volume in first 21d / total volume over 63d."""
    def _f3(y):
        tot = y.sum()
        return y[:len(y) // 3].sum() / tot if tot > 0 else np.nan
    return volume.rolling(63, min_periods=30).apply(_f3, raw=True)


def dsh_116_volume_last_third_share_63d(volume: pd.Series) -> pd.Series:
    """Volume in last 21d / total volume over 63d."""
    def _l3(y):
        tot = y.sum()
        return y[2 * len(y) // 3:].sum() / tot if tot > 0 else np.nan
    return volume.rolling(63, min_periods=30).apply(_l3, raw=True)


# --- Group R: Price path shape via window-percentile approach ---

def dsh_117_price_percentile_in_window_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's close within 21d window — 0 = at window low."""
    def _pct(y):
        return (y[-1] - y.min()) / (y.max() - y.min()) if y.max() > y.min() else 0.5
    return close.rolling(21, min_periods=10).apply(_pct, raw=True)


def dsh_118_price_percentile_in_window_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within 63d window."""
    def _pct(y):
        return (y[-1] - y.min()) / (y.max() - y.min()) if y.max() > y.min() else 0.5
    return close.rolling(63, min_periods=30).apply(_pct, raw=True)


def dsh_119_price_percentile_in_window_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within 126d window."""
    def _pct(y):
        return (y[-1] - y.min()) / (y.max() - y.min()) if y.max() > y.min() else 0.5
    return close.rolling(126, min_periods=60).apply(_pct, raw=True)


def dsh_120_price_percentile_in_window_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of close within 252d window."""
    def _pct(y):
        return (y[-1] - y.min()) / (y.max() - y.min()) if y.max() > y.min() else 0.5
    return close.rolling(252, min_periods=120).apply(_pct, raw=True)


# --- Group S: Consecutive run structure ---

def dsh_121_max_consecutive_down_days_21d(close: pd.Series) -> pd.Series:
    """Longest streak of consecutive down-close days within rolling 21d window."""
    def _max_run(y):
        best = cur = 0
        for i in range(1, len(y)):
            if y[i] < y[i - 1]:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return close.rolling(21, min_periods=10).apply(_max_run, raw=True)


def dsh_122_max_consecutive_down_days_63d(close: pd.Series) -> pd.Series:
    """Longest streak of consecutive down-close days within rolling 63d window."""
    def _max_run(y):
        best = cur = 0
        for i in range(1, len(y)):
            if y[i] < y[i - 1]:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return close.rolling(63, min_periods=30).apply(_max_run, raw=True)


def dsh_123_down_day_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21d days with a down close."""
    dc = (close.diff() < 0).astype(float)
    return dc.rolling(21, min_periods=10).mean()


def dsh_124_down_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63d days with a down close."""
    dc = (close.diff() < 0).astype(float)
    return dc.rolling(63, min_periods=30).mean()


def dsh_125_down_day_fraction_126d(close: pd.Series) -> pd.Series:
    """Fraction of 126d days with a down close."""
    dc = (close.diff() < 0).astype(float)
    return dc.rolling(126, min_periods=60).mean()


def dsh_126_run_ratio_down_vs_up_63d(close: pd.Series) -> pd.Series:
    """Down-day fraction / up-day fraction over 63d — asymmetry of direction."""
    down = (close.diff() < 0).astype(float).rolling(63, min_periods=30).mean()
    up = (close.diff() > 0).astype(float).rolling(63, min_periods=30).mean()
    return _safe_div(down, up)


# --- Group T: Path convexity via midpoint comparison ---

def dsh_127_midpoint_vs_linear_21d(close: pd.Series) -> pd.Series:
    """Midpoint of 21d window close minus midpoint of linear interpolation —
    positive = above line (convex/U-shape), negative = below (concave/L)."""
    def _mid_dev(y):
        n = len(y)
        if n < 3:
            return np.nan
        lin = np.linspace(y[0], y[-1], n)
        return y[n // 2] - lin[n // 2]
    return close.rolling(21, min_periods=10).apply(_mid_dev, raw=True)


def dsh_128_midpoint_vs_linear_63d(close: pd.Series) -> pd.Series:
    """Midpoint deviation from linear interpolation over 63d."""
    def _mid_dev(y):
        n = len(y)
        if n < 3:
            return np.nan
        lin = np.linspace(y[0], y[-1], n)
        return y[n // 2] - lin[n // 2]
    return close.rolling(63, min_periods=30).apply(_mid_dev, raw=True)


def dsh_129_midpoint_vs_linear_normed_63d(close: pd.Series) -> pd.Series:
    """Midpoint deviation from linear interpolation over 63d, divided by price
    range — normalised convexity."""
    def _mid_dev_n(y):
        n = len(y)
        if n < 3:
            return np.nan
        rng = y.max() - y.min()
        if rng < _EPS:
            return 0.0
        lin = np.linspace(y[0], y[-1], n)
        return (y[n // 2] - lin[n // 2]) / rng
    return close.rolling(63, min_periods=30).apply(_mid_dev_n, raw=True)


def dsh_130_midpoint_vs_linear_normed_126d(close: pd.Series) -> pd.Series:
    """Normalised midpoint deviation from linear interpolation over 126d."""
    def _mid_dev_n(y):
        n = len(y)
        if n < 3:
            return np.nan
        rng = y.max() - y.min()
        if rng < _EPS:
            return 0.0
        lin = np.linspace(y[0], y[-1], n)
        return (y[n // 2] - lin[n // 2]) / rng
    return close.rolling(126, min_periods=60).apply(_mid_dev_n, raw=True)


# --- Group U: Entropy and complexity of decline path ---

def dsh_131_return_entropy_21d(close: pd.Series) -> pd.Series:
    """Approximate entropy of daily returns over 21d — high = complex/noisy
    path, low = clean directional move."""
    ret = close.pct_change()
    def _ent(y):
        y = y[~np.isnan(y)]
        if len(y) < 5:
            return np.nan
        h, _ = np.histogram(y, bins=min(8, len(y) // 2))
        h = h[h > 0].astype(float)
        h /= h.sum()
        return -np.sum(h * np.log(h + _EPS))
    return ret.rolling(21, min_periods=10).apply(_ent, raw=True)


def dsh_132_return_entropy_63d(close: pd.Series) -> pd.Series:
    """Approximate entropy of daily returns over 63d."""
    ret = close.pct_change()
    def _ent(y):
        y = y[~np.isnan(y)]
        if len(y) < 5:
            return np.nan
        h, _ = np.histogram(y, bins=min(10, len(y) // 3))
        h = h[h > 0].astype(float)
        h /= h.sum()
        return -np.sum(h * np.log(h + _EPS))
    return ret.rolling(63, min_periods=20).apply(_ent, raw=True)


def dsh_133_volume_entropy_63d(volume: pd.Series) -> pd.Series:
    """Entropy of volume distribution over 63d."""
    def _ent(y):
        y = y[y > 0]
        if len(y) < 5:
            return np.nan
        h, _ = np.histogram(y, bins=min(10, len(y) // 3))
        h = h[h > 0].astype(float)
        h /= h.sum()
        return -np.sum(h * np.log(h + _EPS))
    return volume.rolling(63, min_periods=20).apply(_ent, raw=True)


# --- Group V: Exponential-fit of decline ---

def dsh_134_exp_decay_rate_63d(close: pd.Series) -> pd.Series:
    """Rate parameter of exponential fit to close over 63d — negative = declining
    exponential."""
    def _exp_rate(y):
        n = len(y)
        if n < 3 or np.any(y <= 0):
            return np.nan
        x = np.arange(n, dtype=float)
        try:
            logy = np.log(y)
            x -= x.mean()
            denom = np.dot(x, x)
            return np.dot(x, logy) / denom if denom > _EPS else np.nan
        except Exception:
            return np.nan
    return close.rolling(63, min_periods=30).apply(_exp_rate, raw=True)


def dsh_135_exp_decay_rate_126d(close: pd.Series) -> pd.Series:
    """Exponential decay rate over 126d."""
    def _exp_rate(y):
        n = len(y)
        if n < 3 or np.any(y <= 0):
            return np.nan
        x = np.arange(n, dtype=float) - (n - 1) / 2.0
        logy = np.log(y)
        denom = np.dot(x, x)
        return np.dot(x, logy) / denom if denom > _EPS else np.nan
    return close.rolling(126, min_periods=60).apply(_exp_rate, raw=True)


def dsh_136_exp_fit_r2_63d(close: pd.Series) -> pd.Series:
    """R^2 of exponential fit to close over 63d — is decline truly exponential."""
    def _er2(y):
        n = len(y)
        if n < 3 or np.any(y <= 0):
            return np.nan
        x = np.arange(n, dtype=float)
        logy = np.log(y)
        xm, ym = x.mean(), logy.mean()
        xi = x - xm
        denom = np.dot(xi, xi)
        if denom < _EPS:
            return np.nan
        b = np.dot(xi, logy - ym) / denom
        a = ym - b * xm
        ss_res = np.sum((logy - (a + b * x)) ** 2)
        ss_tot = np.sum((logy - ym) ** 2)
        return max(0.0, 1.0 - ss_res / ss_tot) if ss_tot > _EPS else 1.0
    return close.rolling(63, min_periods=30).apply(_er2, raw=True)


# --- Group W: Multi-period shape cross-section ---

def dsh_137_short_vs_long_curvature_ratio(close: pd.Series) -> pd.Series:
    """Quadratic coefficient over 21d / quadratic coefficient over 63d — detects
    whether short-term curve has opposite sign to long-term."""
    q21 = _roll_quad_coef(close, 21)
    q63 = _roll_quad_coef(close, 63)
    return _safe_div(q21, q63)


def dsh_138_short_vs_long_r2_ratio(close: pd.Series) -> pd.Series:
    """Linear R^2 over 21d / R^2 over 63d — relative linearity short vs long."""
    r21 = _roll_r2(close, 21)
    r63 = _roll_r2(close, 63)
    return _safe_div(r21, r63)


def dsh_139_curvature_sign_agreement_63_vs_126(close: pd.Series) -> pd.Series:
    """1 if sign(quad coef 63d) == sign(quad coef 126d), else -1 — shape
    consistency across horizons."""
    q63 = _roll_quad_coef(close, 63)
    q126 = _roll_quad_coef(close, 126)
    return np.sign(q63) * np.sign(q126)


def dsh_140_jaggedness_21_vs_63_ratio(close: pd.Series) -> pd.Series:
    """Jaggedness over 21d / jaggedness over 63d — are recent moves choppier
    than the longer-term path."""
    arc21 = close.diff().abs().rolling(21, min_periods=10).sum()
    chord21 = (close - close.shift(20)).abs()
    jag21 = _safe_div(arc21, chord21)
    arc63 = close.diff().abs().rolling(63, min_periods=30).sum()
    chord63 = (close - close.shift(62)).abs()
    jag63 = _safe_div(arc63, chord63)
    return _safe_div(jag21, jag63)


# --- Group X: Volume-price path geometry ---

def dsh_141_vol_weighted_jaggedness_63d(close: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Volume-weighted arc-length / volume-weighted chord over 63d."""
    w = volume / volume.rolling(63, min_periods=30).mean().replace(0, np.nan)
    w = w.fillna(1.0)
    warc = (close.diff().abs() * w).rolling(63, min_periods=30).sum()
    wchord = ((close - close.shift(62)).abs() * w).rolling(63, min_periods=30).mean()
    return _safe_div(warc, wchord)


def dsh_142_price_vol_correlation_slope_63d(close: pd.Series,
                                              volume: pd.Series) -> pd.Series:
    """Rolling 21d correlation between daily return and volume, then slope of
    that correlation over 63d — is price-volume relationship changing."""
    ret = close.pct_change()
    corr = ret.rolling(21, min_periods=10).corr(volume)
    return _roll_slope(corr, 63)


def dsh_143_cumvol_path_r2_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R^2 of linear fit to rolling-summed volume over 63d — is selling volume
    arriving at a steady pace."""
    return _roll_r2(volume.rolling(63, min_periods=30).sum(), 63)


# --- Group Y: Harmonic mean and geometric shape ---

def dsh_144_harmonic_vs_arithmetic_close_63d(close: pd.Series) -> pd.Series:
    """Harmonic mean of close / arithmetic mean of close over 63d — ratio < 1
    always; more negative departure = more skewed decline with outlier lows."""
    def _harm(y):
        y = y[y > 0]
        if len(y) == 0:
            return np.nan
        return len(y) / np.sum(1.0 / y)
    hmean = close.rolling(63, min_periods=30).apply(_harm, raw=True)
    amean = _roll_mean(close, 63)
    return _safe_div(hmean, amean)


def dsh_145_geometric_vs_arithmetic_close_63d(close: pd.Series) -> pd.Series:
    """Geometric mean / arithmetic mean over 63d (Jensen's inequality gap)."""
    def _geom(y):
        y = y[y > 0]
        if len(y) == 0:
            return np.nan
        return np.exp(np.mean(np.log(y)))
    gmean = close.rolling(63, min_periods=30).apply(_geom, raw=True)
    amean = _roll_mean(close, 63)
    return _safe_div(gmean, amean)


# --- Group Z: Higher-order shape statistics ---

def dsh_146_return_skew_21d(close: pd.Series) -> pd.Series:
    """Skewness of daily returns over 21d — large negative = fat left tail
    (panic days dominate)."""
    ret = close.pct_change()
    return ret.rolling(21, min_periods=10).skew()


def dsh_147_return_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of daily returns over 63d."""
    ret = close.pct_change()
    return ret.rolling(63, min_periods=20).skew()


def dsh_148_return_kurt_21d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns over 21d."""
    ret = close.pct_change()
    return ret.rolling(21, min_periods=10).kurt()


def dsh_149_return_kurt_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns over 63d."""
    ret = close.pct_change()
    return ret.rolling(63, min_periods=20).kurt()


def dsh_150_price_range_asymmetry_63d(close: pd.Series, high: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """(rolling_max_high - rolling_median_close) / (rolling_median_close -
    rolling_min_low) over 63d — where is the median close relative to the
    extremes; <1 = median skewed toward the bottom."""
    rmax = _roll_max(high, 63)
    rmin = _roll_min(low, 63)
    rmed = close.rolling(63, min_periods=30).median()
    upper = rmax - rmed
    lower = rmed - rmin
    return _safe_div(upper, lower)


# ── Registry ───────────────────────────────────────────────────────────────────

DRAWDOWN_SHAPE_REGISTRY_076_150 = {
    "dsh_076_otc_negative_fraction_21d":         {"inputs": ["open", "close"],                   "func": dsh_076_otc_negative_fraction_21d},
    "dsh_077_otc_negative_fraction_63d":         {"inputs": ["open", "close"],                   "func": dsh_077_otc_negative_fraction_63d},
    "dsh_078_otc_body_size_trend_63d":           {"inputs": ["open", "close"],                   "func": dsh_078_otc_body_size_trend_63d},
    "dsh_079_bearish_body_frac_of_range_21d":    {"inputs": ["open", "close", "high", "low"],    "func": dsh_079_bearish_body_frac_of_range_21d},
    "dsh_080_bearish_body_frac_of_range_63d":    {"inputs": ["open", "close", "high", "low"],    "func": dsh_080_bearish_body_frac_of_range_63d},
    "dsh_081_upper_shadow_fraction_21d":         {"inputs": ["open", "close", "high"],           "func": dsh_081_upper_shadow_fraction_21d},
    "dsh_082_lower_shadow_fraction_21d":         {"inputs": ["open", "close", "low"],            "func": dsh_082_lower_shadow_fraction_21d},
    "dsh_083_lower_shadow_fraction_63d":         {"inputs": ["open", "close", "low"],            "func": dsh_083_lower_shadow_fraction_63d},
    "dsh_084_price_autocorr_lag1_21d":           {"inputs": ["close"],                           "func": dsh_084_price_autocorr_lag1_21d},
    "dsh_085_price_autocorr_lag1_63d":           {"inputs": ["close"],                           "func": dsh_085_price_autocorr_lag1_63d},
    "dsh_086_price_autocorr_lag5_63d":           {"inputs": ["close"],                           "func": dsh_086_price_autocorr_lag5_63d},
    "dsh_087_price_autocorr_lag1_126d":          {"inputs": ["close"],                           "func": dsh_087_price_autocorr_lag1_126d},
    "dsh_088_drawdown_autocorr_lag1_63d":        {"inputs": ["close"],                           "func": dsh_088_drawdown_autocorr_lag1_63d},
    "dsh_089_hl_range_slope_21d":                {"inputs": ["high", "low"],                     "func": dsh_089_hl_range_slope_21d},
    "dsh_090_hl_range_slope_63d":                {"inputs": ["high", "low"],                     "func": dsh_090_hl_range_slope_63d},
    "dsh_091_hl_range_r2_63d":                   {"inputs": ["high", "low"],                     "func": dsh_091_hl_range_r2_63d},
    "dsh_092_hl_range_quad_coef_63d":            {"inputs": ["high", "low"],                     "func": dsh_092_hl_range_quad_coef_63d},
    "dsh_093_true_range_slope_21d":              {"inputs": ["close", "high", "low"],            "func": dsh_093_true_range_slope_21d},
    "dsh_094_true_range_slope_63d":              {"inputs": ["close", "high", "low"],            "func": dsh_094_true_range_slope_63d},
    "dsh_095_true_range_r2_63d":                 {"inputs": ["close", "high", "low"],            "func": dsh_095_true_range_r2_63d},
    "dsh_096_overnight_gap_slope_63d":           {"inputs": ["open", "close"],                   "func": dsh_096_overnight_gap_slope_63d},
    "dsh_097_overnight_gap_autocorr_63d":        {"inputs": ["open", "close"],                   "func": dsh_097_overnight_gap_autocorr_63d},
    "dsh_098_intraday_return_slope_63d":         {"inputs": ["open", "close"],                   "func": dsh_098_intraday_return_slope_63d},
    "dsh_099_open_low_gap_fraction_21d":         {"inputs": ["open", "low"],                     "func": dsh_099_open_low_gap_fraction_21d},
    "dsh_100_close_low_gap_fraction_21d":        {"inputs": ["close", "low"],                    "func": dsh_100_close_low_gap_fraction_21d},
    "dsh_101_drawdown_lin_rmse_63d":             {"inputs": ["close"],                           "func": dsh_101_drawdown_lin_rmse_63d},
    "dsh_102_drawdown_lin_rmse_126d":            {"inputs": ["close"],                           "func": dsh_102_drawdown_lin_rmse_126d},
    "dsh_103_drawdown_quad_coef_63d":            {"inputs": ["close"],                           "func": dsh_103_drawdown_quad_coef_63d},
    "dsh_104_drawdown_quad_coef_126d":           {"inputs": ["close"],                           "func": dsh_104_drawdown_quad_coef_126d},
    "dsh_105_drawdown_quad_coef_252d":           {"inputs": ["close"],                           "func": dsh_105_drawdown_quad_coef_252d},
    "dsh_106_drawdown_r2_63d":                   {"inputs": ["close"],                           "func": dsh_106_drawdown_r2_63d},
    "dsh_107_drawdown_r2_126d":                  {"inputs": ["close"],                           "func": dsh_107_drawdown_r2_126d},
    "dsh_108_drawdown_r2_252d":                  {"inputs": ["close"],                           "func": dsh_108_drawdown_r2_252d},
    "dsh_109_volume_slope_21d":                  {"inputs": ["volume"],                          "func": dsh_109_volume_slope_21d},
    "dsh_110_volume_slope_63d":                  {"inputs": ["volume"],                          "func": dsh_110_volume_slope_63d},
    "dsh_111_volume_r2_63d":                     {"inputs": ["volume"],                          "func": dsh_111_volume_r2_63d},
    "dsh_112_volume_quad_coef_63d":              {"inputs": ["volume"],                          "func": dsh_112_volume_quad_coef_63d},
    "dsh_113_log_volume_slope_63d":              {"inputs": ["volume"],                          "func": dsh_113_log_volume_slope_63d},
    "dsh_114_volume_jaggedness_63d":             {"inputs": ["volume"],                          "func": dsh_114_volume_jaggedness_63d},
    "dsh_115_volume_first_third_share_63d":      {"inputs": ["volume"],                          "func": dsh_115_volume_first_third_share_63d},
    "dsh_116_volume_last_third_share_63d":       {"inputs": ["volume"],                          "func": dsh_116_volume_last_third_share_63d},
    "dsh_117_price_percentile_in_window_21d":    {"inputs": ["close"],                           "func": dsh_117_price_percentile_in_window_21d},
    "dsh_118_price_percentile_in_window_63d":    {"inputs": ["close"],                           "func": dsh_118_price_percentile_in_window_63d},
    "dsh_119_price_percentile_in_window_126d":   {"inputs": ["close"],                           "func": dsh_119_price_percentile_in_window_126d},
    "dsh_120_price_percentile_in_window_252d":   {"inputs": ["close"],                           "func": dsh_120_price_percentile_in_window_252d},
    "dsh_121_max_consecutive_down_days_21d":     {"inputs": ["close"],                           "func": dsh_121_max_consecutive_down_days_21d},
    "dsh_122_max_consecutive_down_days_63d":     {"inputs": ["close"],                           "func": dsh_122_max_consecutive_down_days_63d},
    "dsh_123_down_day_fraction_21d":             {"inputs": ["close"],                           "func": dsh_123_down_day_fraction_21d},
    "dsh_124_down_day_fraction_63d":             {"inputs": ["close"],                           "func": dsh_124_down_day_fraction_63d},
    "dsh_125_down_day_fraction_126d":            {"inputs": ["close"],                           "func": dsh_125_down_day_fraction_126d},
    "dsh_126_run_ratio_down_vs_up_63d":          {"inputs": ["close"],                           "func": dsh_126_run_ratio_down_vs_up_63d},
    "dsh_127_midpoint_vs_linear_21d":            {"inputs": ["close"],                           "func": dsh_127_midpoint_vs_linear_21d},
    "dsh_128_midpoint_vs_linear_63d":            {"inputs": ["close"],                           "func": dsh_128_midpoint_vs_linear_63d},
    "dsh_129_midpoint_vs_linear_normed_63d":     {"inputs": ["close"],                           "func": dsh_129_midpoint_vs_linear_normed_63d},
    "dsh_130_midpoint_vs_linear_normed_126d":    {"inputs": ["close"],                           "func": dsh_130_midpoint_vs_linear_normed_126d},
    "dsh_131_return_entropy_21d":                {"inputs": ["close"],                           "func": dsh_131_return_entropy_21d},
    "dsh_132_return_entropy_63d":                {"inputs": ["close"],                           "func": dsh_132_return_entropy_63d},
    "dsh_133_volume_entropy_63d":                {"inputs": ["volume"],                          "func": dsh_133_volume_entropy_63d},
    "dsh_134_exp_decay_rate_63d":                {"inputs": ["close"],                           "func": dsh_134_exp_decay_rate_63d},
    "dsh_135_exp_decay_rate_126d":               {"inputs": ["close"],                           "func": dsh_135_exp_decay_rate_126d},
    "dsh_136_exp_fit_r2_63d":                    {"inputs": ["close"],                           "func": dsh_136_exp_fit_r2_63d},
    "dsh_137_short_vs_long_curvature_ratio":     {"inputs": ["close"],                           "func": dsh_137_short_vs_long_curvature_ratio},
    "dsh_138_short_vs_long_r2_ratio":            {"inputs": ["close"],                           "func": dsh_138_short_vs_long_r2_ratio},
    "dsh_139_curvature_sign_agreement_63_vs_126":{"inputs": ["close"],                           "func": dsh_139_curvature_sign_agreement_63_vs_126},
    "dsh_140_jaggedness_21_vs_63_ratio":         {"inputs": ["close"],                           "func": dsh_140_jaggedness_21_vs_63_ratio},
    "dsh_141_vol_weighted_jaggedness_63d":       {"inputs": ["close", "volume"],                 "func": dsh_141_vol_weighted_jaggedness_63d},
    "dsh_142_price_vol_correlation_slope_63d":   {"inputs": ["close", "volume"],                 "func": dsh_142_price_vol_correlation_slope_63d},
    "dsh_143_cumvol_path_r2_63d":                {"inputs": ["close", "volume"],                 "func": dsh_143_cumvol_path_r2_63d},
    "dsh_144_harmonic_vs_arithmetic_close_63d":  {"inputs": ["close"],                           "func": dsh_144_harmonic_vs_arithmetic_close_63d},
    "dsh_145_geometric_vs_arithmetic_close_63d": {"inputs": ["close"],                           "func": dsh_145_geometric_vs_arithmetic_close_63d},
    "dsh_146_return_skew_21d":                   {"inputs": ["close"],                           "func": dsh_146_return_skew_21d},
    "dsh_147_return_skew_63d":                   {"inputs": ["close"],                           "func": dsh_147_return_skew_63d},
    "dsh_148_return_kurt_21d":                   {"inputs": ["close"],                           "func": dsh_148_return_kurt_21d},
    "dsh_149_return_kurt_63d":                   {"inputs": ["close"],                           "func": dsh_149_return_kurt_63d},
    "dsh_150_price_range_asymmetry_63d":         {"inputs": ["close", "high", "low"],            "func": dsh_150_price_range_asymmetry_63d},
}
