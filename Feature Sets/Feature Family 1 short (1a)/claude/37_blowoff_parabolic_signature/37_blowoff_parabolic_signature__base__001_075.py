"""blowoff_parabolic_signature base features 001_075 — short blowup pipeline 1a-inverse.

Parabolic / super-exponential blowoff signatures at multi-year peaks: long-horizon log-quadratic fits, LPPL-inspired singularity proxies, volume-confirmed regimes, exhaustion patterns.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _logquad_c(s, n):
    """Quadratic coefficient (c) of polynomial fit y ~ a + b*t + c*t² over rolling window n."""
    def _c(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            coefs = np.polyfit(t, w, 2)
            return float(coefs[0])
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_c, raw=True)


def _logquad_b(s, n):
    """Linear coefficient (b) of polynomial fit y ~ a + b*t + c*t² over rolling window n."""
    def _b(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            coefs = np.polyfit(t, w, 2)
            return float(coefs[1])
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_b, raw=True)


def _logquad_r2_gain(s, n):
    """R² of quadratic fit minus R² of linear fit (positive = parabola explains more)."""
    def _g(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            ss_tot = float(np.sum((w - w.mean()) ** 2))
            if ss_tot == 0:
                return np.nan
            c_lin = np.polyfit(t, w, 1)
            r_lin = w - np.polyval(c_lin, t)
            r2_lin = 1.0 - float(np.sum(r_lin ** 2)) / ss_tot
            c_q = np.polyfit(t, w, 2)
            r_q = w - np.polyval(c_q, t)
            r2_q = 1.0 - float(np.sum(r_q ** 2)) / ss_tot
            return r2_q - r2_lin
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_g, raw=True)


def _logquad_resid_last(s, n):
    """Last-bar residual of log price minus its quadratic fit over window n."""
    def _r(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            return float(w[-1] - np.polyval(c, t[-1]))
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_r, raw=True)


def _logquad_resid_max_abs(s, n):
    """Max absolute residual from quadratic fit over window."""
    def _r(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            return float(np.max(np.abs(w - np.polyval(c, t))))
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_r, raw=True)


def _logcubic_r2_gain_over_quad(s, n):
    """R² of cubic minus R² of quadratic fit (positive = cubic explains more)."""
    def _g(w):
        if np.isnan(w).any() or len(w) < 6:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            ss_tot = float(np.sum((w - w.mean()) ** 2))
            if ss_tot == 0:
                return np.nan
            c_q = np.polyfit(t, w, 2)
            r_q = w - np.polyval(c_q, t)
            r2_q = 1.0 - float(np.sum(r_q ** 2)) / ss_tot
            c_c = np.polyfit(t, w, 3)
            r_c = w - np.polyval(c_c, t)
            r2_c = 1.0 - float(np.sum(r_c ** 2)) / ss_tot
            return r2_c - r2_q
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 6)).apply(_g, raw=True)


def _doubling_time(s, lookback):
    """Bars over which price doubled (causal): bars where price now is ~2x price `lookback` bars ago.
    Returns the implied doubling rate r such that exp(r*lookback) ~ ratio."""
    ratio = _safe_div(s, s.shift(lookback).abs())
    return _safe_log(ratio) / float(lookback)


def _hyper_growth_score(s, n):
    """Growth rate of growth rate: diff(log diff(log(s))) rolling mean."""
    g = _safe_log(s).diff()
    return g.diff().rolling(n, min_periods=max(n // 3, 2)).mean()


def _time_to_singularity_proxy(s, n):
    """LPPL-inspired finite-time-singularity ETA proxy from quadratic fit: -b/(2c) capped.
    Returns bars-from-now (positive = singularity ahead, NaN if not parabolic up)."""
    def _t(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(len(w), dtype=float)
        try:
            c = np.polyfit(t, w, 2)
            cc, bb = float(c[0]), float(c[1])
            if cc <= 0:
                return np.nan
            tc = -bb / (2.0 * cc)
            eta = tc - t[-1]
            if eta <= 0 or eta > 5000:
                return np.nan
            return float(eta)
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_t, raw=True)


def _power_law_exp(s, n):
    """Log-log slope of price vs bar index over rolling n — power-law growth exponent proxy."""
    def _e(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        t = np.arange(1, len(w) + 1, dtype=float)
        lt = np.log(t)
        try:
            mt = lt.mean(); mw = w.mean()
            num = float(((lt - mt) * (w - mw)).sum())
            den = float(((lt - mt) ** 2).sum())
            return num / den if den != 0 else np.nan
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_e, raw=True)

# ============================================================
#                    BASE FEATURES 001-075
# ============================================================

def f37_bpsg_001_logquad_c_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient c of log-price over 252d window (annual parabola)."""
    return _logquad_c(_safe_log(close), 252)


def f37_bpsg_002_logquad_c_504d(close: pd.Series) -> pd.Series:
    """Quadratic c of log-price over 504d window (biennial parabola)."""
    return _logquad_c(_safe_log(close), 504)


def f37_bpsg_003_logquad_c_1260d(close: pd.Series) -> pd.Series:
    """Quadratic c of log-price over 1260d (5y parabola)."""
    return _logquad_c(_safe_log(close), 1260)


def f37_bpsg_004_logquad_c_252d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d log-quadratic c within 1260d."""
    return _rolling_zscore(_logquad_c(_safe_log(close), 252), 1260)


def f37_bpsg_005_logquad_c_504d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 504d log-quadratic c within 1260d."""
    return _rolling_zscore(_logquad_c(_safe_log(close), 504), 1260)


def f37_bpsg_006_logquad_c_252d_pctrank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d log-quadratic c within 1260d."""
    c = _logquad_c(_safe_log(close), 252)
    return c.rolling(1260, min_periods=252).rank(pct=True)


def f37_bpsg_007_logquad_c_504d_pctrank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 504d log-quadratic c within 1260d."""
    c = _logquad_c(_safe_log(close), 504)
    return c.rolling(1260, min_periods=252).rank(pct=True)


def f37_bpsg_008_logquad_c_atr_norm_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d log-quadratic c scaled by 252d ATR / close."""
    c = _logquad_c(_safe_log(close), 252)
    atr_n = _atr(high, low, close, 252) / close.replace(0, np.nan)
    return _safe_div(c, atr_n)


def f37_bpsg_009_logquad_c_atr_norm_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """504d log-quadratic c scaled by 252d ATR / close."""
    c = _logquad_c(_safe_log(close), 504)
    atr_n = _atr(high, low, close, 252) / close.replace(0, np.nan)
    return _safe_div(c, atr_n)


def f37_bpsg_010_logquad_b_252d(close: pd.Series) -> pd.Series:
    """Linear coefficient b of log-price over 252d (drift)."""
    return _logquad_b(_safe_log(close), 252)


def f37_bpsg_011_logquad_b_504d(close: pd.Series) -> pd.Series:
    """Linear coefficient b of log-price over 504d."""
    return _logquad_b(_safe_log(close), 504)


def f37_bpsg_012_logquad_c_to_b_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of quadratic c to linear b over 252d (parabolic dominance)."""
    lc = _logquad_c(_safe_log(close), 252); lb = _logquad_b(_safe_log(close), 252)
    return _safe_div(lc, lb.abs())


def f37_bpsg_013_logquad_c_to_b_ratio_504d(close: pd.Series) -> pd.Series:
    """Ratio of quadratic c to linear b over 504d."""
    lc = _logquad_c(_safe_log(close), 504); lb = _logquad_b(_safe_log(close), 504)
    return _safe_div(lc, lb.abs())


def f37_bpsg_014_logquad_c_positive_streak_max_252d(close: pd.Series) -> pd.Series:
    """Max consecutive bars with positive 252d log-quadratic c, over 252d."""
    c = _logquad_c(_safe_log(close), 252)
    pos = (c > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return streak.rolling(252, min_periods=63).max().astype(float)


def f37_bpsg_015_logquad_c_252d_to_c_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 252d-window c to 504d-window c — short-vs-long parabolic dominance."""
    a = _logquad_c(_safe_log(close), 252); b = _logquad_c(_safe_log(close), 504)
    return _safe_div(a, b)


def f37_bpsg_016_logquad_c_504d_to_c_1260d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 504d-window c to 1260d-window c."""
    a = _logquad_c(_safe_log(close), 504); b = _logquad_c(_safe_log(close), 1260)
    return _safe_div(a, b)


def f37_bpsg_017_logquad_c_252d_diff_21d(close: pd.Series) -> pd.Series:
    """21-bar change in 252d log-quadratic c — parabolic-dominance velocity."""
    c = _logquad_c(_safe_log(close), 252)
    return c.diff(21)


def f37_bpsg_018_logquad_c_504d_diff_63d(close: pd.Series) -> pd.Series:
    """63-bar change in 504d log-quadratic c."""
    c = _logquad_c(_safe_log(close), 504)
    return c.diff(63)


def f37_bpsg_019_logquad_c_max_252d_minus_current(close: pd.Series) -> pd.Series:
    """252d rolling max of 252d log-quadratic c minus current — parabola fading."""
    c = _logquad_c(_safe_log(close), 252)
    return c.rolling(252, min_periods=63).max() - c


def f37_bpsg_020_days_since_logquad_c_504d_max_504d(close: pd.Series) -> pd.Series:
    """Bars since 504d log-quadratic c reached its 504d max."""
    c = _logquad_c(_safe_log(close), 504)
    def _b(w):
        v = w[~np.isnan(w)]
        if len(v) == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmax(w)))
    return c.rolling(504, min_periods=126).apply(_b, raw=True)


def f37_bpsg_021_logquad_r2_gain_252d(close: pd.Series) -> pd.Series:
    """R²(quadratic) - R²(linear) of log-price over 252d."""
    return _logquad_r2_gain(_safe_log(close), 252)


def f37_bpsg_022_logquad_r2_gain_504d(close: pd.Series) -> pd.Series:
    """R² gain of quadratic over linear, 504d window."""
    return _logquad_r2_gain(_safe_log(close), 504)


def f37_bpsg_023_logquad_r2_gain_1260d(close: pd.Series) -> pd.Series:
    """R² gain of quadratic over linear, 1260d window."""
    return _logquad_r2_gain(_safe_log(close), 1260)


def f37_bpsg_024_logquad_r2_gain_252d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d R² gain within 1260d."""
    return _rolling_zscore(_logquad_r2_gain(_safe_log(close), 252), 1260)


def f37_bpsg_025_logquad_r2_gain_504d_pctrank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 504d R² gain within 1260d."""
    g = _logquad_r2_gain(_safe_log(close), 504)
    return g.rolling(1260, min_periods=252).rank(pct=True)


def f37_bpsg_026_logquad_r2_gain_above_005_streak_max_252d(close: pd.Series) -> pd.Series:
    """Max consecutive bars with 252d R² gain > 0.05, over 252d."""
    g = _logquad_r2_gain(_safe_log(close), 252)
    above = (g > 0.05).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.rolling(252, min_periods=63).max().astype(float)


def f37_bpsg_027_logquad_r2_gain_252d_max_minus_current(close: pd.Series) -> pd.Series:
    """252d max of R² gain minus current."""
    g = _logquad_r2_gain(_safe_log(close), 252)
    return g.rolling(252, min_periods=63).max() - g


def f37_bpsg_028_logquad_r2_gain_252d_diff_21d(close: pd.Series) -> pd.Series:
    """21-bar change in R² gain over 252d."""
    g = _logquad_r2_gain(_safe_log(close), 252)
    return g.diff(21)


def f37_bpsg_029_logcubic_over_quad_r2_gain_252d(close: pd.Series) -> pd.Series:
    """R²(cubic) - R²(quadratic) of log-price over 252d — beyond parabolic."""
    return _logcubic_r2_gain_over_quad(_safe_log(close), 252)


def f37_bpsg_030_logcubic_over_quad_r2_gain_504d(close: pd.Series) -> pd.Series:
    """R²(cubic) - R²(quadratic), 504d."""
    return _logcubic_r2_gain_over_quad(_safe_log(close), 504)


def f37_bpsg_031_bic_proxy_quadratic_vs_linear_252d(close: pd.Series) -> pd.Series:
    """BIC-style: n*log((1-r2_quad)/(1-r2_lin)) over 252d — quadratic preferred when negative."""
    g = _logquad_r2_gain(_safe_log(close), 252)
    return -252.0 * np.log(1.0 - g.clip(lower=-0.99, upper=0.99))


def f37_bpsg_032_aic_proxy_quadratic_vs_linear_504d(close: pd.Series) -> pd.Series:
    """AIC-style: n*log((1-r2_quad)/(1-r2_lin)) + 2 penalty over 504d."""
    g = _logquad_r2_gain(_safe_log(close), 504)
    return -504.0 * np.log(1.0 - g.clip(lower=-0.99, upper=0.99)) + 2.0


def f37_bpsg_033_logquad_r2_gain_252d_minus_504d(close: pd.Series) -> pd.Series:
    """Diff between 252d and 504d R² gain — parabolic-window selection."""
    return _logquad_r2_gain(_safe_log(close), 252) - _logquad_r2_gain(_safe_log(close), 504)


def f37_bpsg_034_logquad_r2_gain_504d_minus_1260d(close: pd.Series) -> pd.Series:
    """Diff between 504d and 1260d R² gain."""
    return _logquad_r2_gain(_safe_log(close), 504) - _logquad_r2_gain(_safe_log(close), 1260)


def f37_bpsg_035_logquad_resid_last_atr_norm_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Last-bar quadratic-fit residual / ATR(21) at 252d."""
    r = _logquad_resid_last(_safe_log(close), 252)
    atr_n = _atr(high, low, close, 21) / close.replace(0, np.nan)
    return _safe_div(r, atr_n)


def f37_bpsg_036_time_to_singularity_proxy_252d(close: pd.Series) -> pd.Series:
    """ETA (bars) to parabolic singularity from 252d log-quadratic fit (-b/(2c))."""
    return _time_to_singularity_proxy(_safe_log(close), 252)


def f37_bpsg_037_time_to_singularity_proxy_504d(close: pd.Series) -> pd.Series:
    """ETA to parabolic singularity from 504d fit."""
    return _time_to_singularity_proxy(_safe_log(close), 504)


def f37_bpsg_038_inverse_time_to_singularity_252d(close: pd.Series) -> pd.Series:
    """1 / ETA-to-singularity from 252d fit — singularity-imminence proxy."""
    eta = _time_to_singularity_proxy(_safe_log(close), 252)
    return _safe_div(pd.Series(1.0, index=close.index), eta)


def f37_bpsg_039_inverse_time_to_singularity_504d(close: pd.Series) -> pd.Series:
    """1 / ETA-to-singularity from 504d fit."""
    eta = _time_to_singularity_proxy(_safe_log(close), 504)
    return _safe_div(pd.Series(1.0, index=close.index), eta)


def f37_bpsg_040_eta_singularity_decline_streak_max_63d(close: pd.Series) -> pd.Series:
    """Max consecutive bars where 252d-fit ETA shrank, over 63d (singularity approaching)."""
    eta = _time_to_singularity_proxy(_safe_log(close), 252)
    dec = (eta < eta.shift(1)).astype(int)
    grp = (dec.diff().ne(0)).cumsum()
    streak = dec.groupby(grp).cumsum() * dec
    return streak.rolling(63, min_periods=21).max().astype(float)


def f37_bpsg_041_power_law_exp_252d(close: pd.Series) -> pd.Series:
    """Log-log slope of close vs bar index over 252d — power-law growth exponent."""
    return _power_law_exp(close, 252)


def f37_bpsg_042_power_law_exp_504d(close: pd.Series) -> pd.Series:
    """Power-law exponent over 504d."""
    return _power_law_exp(close, 504)


def f37_bpsg_043_power_law_exp_1260d(close: pd.Series) -> pd.Series:
    """Power-law exponent over 1260d."""
    return _power_law_exp(close, 1260)


def f37_bpsg_044_power_law_exp_252d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d power-law exponent within 1260d."""
    return _rolling_zscore(_power_law_exp(close, 252), 1260)


def f37_bpsg_045_power_law_exp_252d_diff_21d(close: pd.Series) -> pd.Series:
    """21d change in 252d power-law exponent."""
    return _power_law_exp(close, 252).diff(21)


def f37_bpsg_046_doubling_time_implied_rate_252d(close: pd.Series) -> pd.Series:
    """Implied compounding rate r such that close_t = close_{t-252}*exp(r*252)."""
    return _doubling_time(close, 252)


def f37_bpsg_047_doubling_time_implied_rate_504d(close: pd.Series) -> pd.Series:
    """Implied compounding rate over 504d."""
    return _doubling_time(close, 504)


def f37_bpsg_048_doubling_time_rate_252d_minus_1260d(close: pd.Series) -> pd.Series:
    """252d implied rate minus 1260d — acceleration of compounding."""
    return _doubling_time(close, 252) - _doubling_time(close, 1260)


def f37_bpsg_049_hyper_growth_score_63d(close: pd.Series) -> pd.Series:
    """Mean over 63d of diff of log-return — growth rate of growth rate."""
    return _hyper_growth_score(close, 63)


def f37_bpsg_050_hyper_growth_score_252d(close: pd.Series) -> pd.Series:
    """Mean over 252d of diff of log-return."""
    return _hyper_growth_score(close, 252)


def f37_bpsg_051_hyper_growth_score_252d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d hyper-growth score within 504d."""
    return _rolling_zscore(_hyper_growth_score(close, 252), 504)


def f37_bpsg_052_hyper_growth_score_above_zero_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252d where d(log return) > 0 — sustained acceleration."""
    return (_safe_log(close).diff().diff() > 0).astype(float).rolling(252, min_periods=63).mean()


def f37_bpsg_053_log_log_return_acceleration_252d(close: pd.Series) -> pd.Series:
    """Mean over 252d of log(1 + |log_return|) — proxy for log-of-log growth signature."""
    r = _safe_log(close).diff().abs()
    return _safe_log(1.0 + r).rolling(252, min_periods=63).mean()


def f37_bpsg_054_eta_to_b_to_c_ratio_252d(close: pd.Series) -> pd.Series:
    """|b|/|c| from 252d fit (smaller = closer to singularity)."""
    lb = _logquad_b(_safe_log(close), 252); lc = _logquad_c(_safe_log(close), 252)
    return _safe_div(lb.abs(), lc.abs())


def f37_bpsg_055_power_law_exp_to_drift_ratio_252d(close: pd.Series) -> pd.Series:
    """Power-law exponent over 252d divided by 252d log-return — super-linear growth proxy."""
    pe = _power_law_exp(close, 252); dr = _safe_log(close) - _safe_log(close.shift(252))
    return _safe_div(pe, dr)


def f37_bpsg_056_logquad_resid_max_abs_252d(close: pd.Series) -> pd.Series:
    """Max |residual| from 252d log-quadratic fit (relative to log price)."""
    return _logquad_resid_max_abs(_safe_log(close), 252)


def f37_bpsg_057_logquad_resid_max_abs_504d(close: pd.Series) -> pd.Series:
    """Max |residual| from 504d log-quadratic fit."""
    return _logquad_resid_max_abs(_safe_log(close), 504)


def f37_bpsg_058_logquad_resid_max_abs_252d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d max residual within 1260d."""
    return _rolling_zscore(_logquad_resid_max_abs(_safe_log(close), 252), 1260)


def f37_bpsg_059_logquad_resid_last_252d(close: pd.Series) -> pd.Series:
    """Latest-bar residual of log price minus 252d quadratic fit."""
    return _logquad_resid_last(_safe_log(close), 252)


def f37_bpsg_060_logquad_resid_last_504d(close: pd.Series) -> pd.Series:
    """Latest-bar residual minus 504d quadratic fit."""
    return _logquad_resid_last(_safe_log(close), 504)


def f37_bpsg_061_logquad_resid_last_above_2sigma_count_63d(close: pd.Series) -> pd.Series:
    """Count last 63d where bar's quad-fit residual exceeded 2-sigma of fit residuals."""
    r = _logquad_resid_last(_safe_log(close), 252)
    sd = r.rolling(252, min_periods=63).std()
    return (r.abs() > 2 * sd).astype(float).rolling(63, min_periods=21).sum()


def f37_bpsg_062_logquad_resid_last_below_neg2sigma_count_63d(close: pd.Series) -> pd.Series:
    """Count last 63d where residual fell below -2sigma — parabolic-fail tail."""
    r = _logquad_resid_last(_safe_log(close), 252)
    sd = r.rolling(252, min_periods=63).std()
    return (r < -2 * sd).astype(float).rolling(63, min_periods=21).sum()


def f37_bpsg_063_logquad_resid_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of residual-from-252d-fit over trailing 63d."""
    r = _logquad_resid_last(_safe_log(close), 252)
    return r.rolling(63, min_periods=21).skew()


def f37_bpsg_064_logquad_resid_kurt_63d(close: pd.Series) -> pd.Series:
    """Kurtosis of residual-from-252d-fit over trailing 63d."""
    r = _logquad_resid_last(_safe_log(close), 252)
    return r.rolling(63, min_periods=21).kurt()


def f37_bpsg_065_logquad_resid_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """63d autocorr (lag 1) of residual-from-252d-fit — vol-clustering in residual."""
    r = _logquad_resid_last(_safe_log(close), 252)
    return r.rolling(63, min_periods=21).corr(r.shift(1))


def f37_bpsg_066_logquad_resid_max_in_63d_minus_current(close: pd.Series) -> pd.Series:
    """63d max of residual minus current residual — fading parabolic alignment."""
    r = _logquad_resid_last(_safe_log(close), 252)
    return r.rolling(63, min_periods=21).max() - r


def f37_bpsg_067_parabolic_break_signal_252d(close: pd.Series) -> pd.Series:
    """Indicator: residual < -2*sigma AND was > +1*sigma 21 bars ago — parabolic failure."""
    r = _logquad_resid_last(_safe_log(close), 252)
    sd = r.rolling(252, min_periods=63).std()
    return ((r < -2 * sd) & (r.shift(21) > sd.shift(21))).astype(float)


def f37_bpsg_068_parabolic_break_count_252d(close: pd.Series) -> pd.Series:
    """Count over 252d of parabolic-break events (per above definition)."""
    r = _logquad_resid_last(_safe_log(close), 252)
    sd = r.rolling(252, min_periods=63).std()
    ev = ((r < -2 * sd) & (r.shift(21) > sd.shift(21))).astype(float)
    return ev.rolling(252, min_periods=63).sum()


def f37_bpsg_069_logquad_resid_neg_streak_max_63d(close: pd.Series) -> pd.Series:
    """Max consecutive negative-residual streak in trailing 63d."""
    r = _logquad_resid_last(_safe_log(close), 252)
    neg = (r < 0).astype(int)
    grp = (neg.diff().ne(0)).cumsum()
    streak = neg.groupby(grp).cumsum() * neg
    return streak.rolling(63, min_periods=21).max().astype(float)


def f37_bpsg_070_logquad_resid_pos_streak_max_252d(close: pd.Series) -> pd.Series:
    """Max consecutive positive-residual streak (super-parabolic) in 252d."""
    r = _logquad_resid_last(_safe_log(close), 252)
    pos = (r > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return streak.rolling(252, min_periods=63).max().astype(float)


def f37_bpsg_071_logquad_fit_curvature_drawdown_63d(close: pd.Series) -> pd.Series:
    """Current 252d-quadratic c minus rolling 63d max c — curvature drawdown."""
    c = _logquad_c(_safe_log(close), 252)
    return c - c.rolling(63, min_periods=21).max()


def f37_bpsg_072_logquad_fit_curvature_signflip_count_252d(close: pd.Series) -> pd.Series:
    """Count 252d-c sign flips over trailing 252d."""
    c = _logquad_c(_safe_log(close), 252)
    s = np.sign(c.fillna(0))
    flip = ((s != s.shift(1)) & s.shift(1).ne(0)).astype(float)
    return flip.rolling(252, min_periods=63).sum()


def f37_bpsg_073_days_since_logquad_c_positive_252d(close: pd.Series) -> pd.Series:
    """Bars since the 252d log-quadratic c last turned positive."""
    c = _logquad_c(_safe_log(close), 252)
    pos_now = c > 0
    flip_up = pos_now & (~pos_now.shift(1).fillna(False))
    idx = np.arange(len(close))
    last = pd.Series(np.where(flip_up.values, idx, np.nan), index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f37_bpsg_074_logquad_c_dispersion_across_subwindows_63d_in_252d(close: pd.Series) -> pd.Series:
    """Std of 63d log-quadratic c over trailing 252d — curvature instability."""
    c = _logquad_c(_safe_log(close), 63)
    return c.rolling(252, min_periods=63).std()


def f37_bpsg_075_logquad_c_persistence_lag21_252d(close: pd.Series) -> pd.Series:
    """252d autocorr at lag 21 of 252d-window c — curvature persistence."""
    c = _logquad_c(_safe_log(close), 252)
    return c.rolling(252, min_periods=63).corr(c.shift(21))


BLOWOFF_PARABOLIC_SIGNATURE_BASE_REGISTRY_001_075 = {
    "f37_bpsg_001_logquad_c_252d": {"inputs": ["close"], "func": f37_bpsg_001_logquad_c_252d},
    "f37_bpsg_002_logquad_c_504d": {"inputs": ["close"], "func": f37_bpsg_002_logquad_c_504d},
    "f37_bpsg_003_logquad_c_1260d": {"inputs": ["close"], "func": f37_bpsg_003_logquad_c_1260d},
    "f37_bpsg_004_logquad_c_252d_zscore_1260d": {"inputs": ["close"], "func": f37_bpsg_004_logquad_c_252d_zscore_1260d},
    "f37_bpsg_005_logquad_c_504d_zscore_1260d": {"inputs": ["close"], "func": f37_bpsg_005_logquad_c_504d_zscore_1260d},
    "f37_bpsg_006_logquad_c_252d_pctrank_1260d": {"inputs": ["close"], "func": f37_bpsg_006_logquad_c_252d_pctrank_1260d},
    "f37_bpsg_007_logquad_c_504d_pctrank_1260d": {"inputs": ["close"], "func": f37_bpsg_007_logquad_c_504d_pctrank_1260d},
    "f37_bpsg_008_logquad_c_atr_norm_252d": {"inputs": ["close", "high", "low"], "func": f37_bpsg_008_logquad_c_atr_norm_252d},
    "f37_bpsg_009_logquad_c_atr_norm_504d": {"inputs": ["close", "high", "low"], "func": f37_bpsg_009_logquad_c_atr_norm_504d},
    "f37_bpsg_010_logquad_b_252d": {"inputs": ["close"], "func": f37_bpsg_010_logquad_b_252d},
    "f37_bpsg_011_logquad_b_504d": {"inputs": ["close"], "func": f37_bpsg_011_logquad_b_504d},
    "f37_bpsg_012_logquad_c_to_b_ratio_252d": {"inputs": ["close"], "func": f37_bpsg_012_logquad_c_to_b_ratio_252d},
    "f37_bpsg_013_logquad_c_to_b_ratio_504d": {"inputs": ["close"], "func": f37_bpsg_013_logquad_c_to_b_ratio_504d},
    "f37_bpsg_014_logquad_c_positive_streak_max_252d": {"inputs": ["close"], "func": f37_bpsg_014_logquad_c_positive_streak_max_252d},
    "f37_bpsg_015_logquad_c_252d_to_c_504d_ratio": {"inputs": ["close"], "func": f37_bpsg_015_logquad_c_252d_to_c_504d_ratio},
    "f37_bpsg_016_logquad_c_504d_to_c_1260d_ratio": {"inputs": ["close"], "func": f37_bpsg_016_logquad_c_504d_to_c_1260d_ratio},
    "f37_bpsg_017_logquad_c_252d_diff_21d": {"inputs": ["close"], "func": f37_bpsg_017_logquad_c_252d_diff_21d},
    "f37_bpsg_018_logquad_c_504d_diff_63d": {"inputs": ["close"], "func": f37_bpsg_018_logquad_c_504d_diff_63d},
    "f37_bpsg_019_logquad_c_max_252d_minus_current": {"inputs": ["close"], "func": f37_bpsg_019_logquad_c_max_252d_minus_current},
    "f37_bpsg_020_days_since_logquad_c_504d_max_504d": {"inputs": ["close"], "func": f37_bpsg_020_days_since_logquad_c_504d_max_504d},
    "f37_bpsg_021_logquad_r2_gain_252d": {"inputs": ["close"], "func": f37_bpsg_021_logquad_r2_gain_252d},
    "f37_bpsg_022_logquad_r2_gain_504d": {"inputs": ["close"], "func": f37_bpsg_022_logquad_r2_gain_504d},
    "f37_bpsg_023_logquad_r2_gain_1260d": {"inputs": ["close"], "func": f37_bpsg_023_logquad_r2_gain_1260d},
    "f37_bpsg_024_logquad_r2_gain_252d_zscore_1260d": {"inputs": ["close"], "func": f37_bpsg_024_logquad_r2_gain_252d_zscore_1260d},
    "f37_bpsg_025_logquad_r2_gain_504d_pctrank_1260d": {"inputs": ["close"], "func": f37_bpsg_025_logquad_r2_gain_504d_pctrank_1260d},
    "f37_bpsg_026_logquad_r2_gain_above_005_streak_max_252d": {"inputs": ["close"], "func": f37_bpsg_026_logquad_r2_gain_above_005_streak_max_252d},
    "f37_bpsg_027_logquad_r2_gain_252d_max_minus_current": {"inputs": ["close"], "func": f37_bpsg_027_logquad_r2_gain_252d_max_minus_current},
    "f37_bpsg_028_logquad_r2_gain_252d_diff_21d": {"inputs": ["close"], "func": f37_bpsg_028_logquad_r2_gain_252d_diff_21d},
    "f37_bpsg_029_logcubic_over_quad_r2_gain_252d": {"inputs": ["close"], "func": f37_bpsg_029_logcubic_over_quad_r2_gain_252d},
    "f37_bpsg_030_logcubic_over_quad_r2_gain_504d": {"inputs": ["close"], "func": f37_bpsg_030_logcubic_over_quad_r2_gain_504d},
    "f37_bpsg_031_bic_proxy_quadratic_vs_linear_252d": {"inputs": ["close"], "func": f37_bpsg_031_bic_proxy_quadratic_vs_linear_252d},
    "f37_bpsg_032_aic_proxy_quadratic_vs_linear_504d": {"inputs": ["close"], "func": f37_bpsg_032_aic_proxy_quadratic_vs_linear_504d},
    "f37_bpsg_033_logquad_r2_gain_252d_minus_504d": {"inputs": ["close"], "func": f37_bpsg_033_logquad_r2_gain_252d_minus_504d},
    "f37_bpsg_034_logquad_r2_gain_504d_minus_1260d": {"inputs": ["close"], "func": f37_bpsg_034_logquad_r2_gain_504d_minus_1260d},
    "f37_bpsg_035_logquad_resid_last_atr_norm_252d": {"inputs": ["close", "high", "low"], "func": f37_bpsg_035_logquad_resid_last_atr_norm_252d},
    "f37_bpsg_036_time_to_singularity_proxy_252d": {"inputs": ["close"], "func": f37_bpsg_036_time_to_singularity_proxy_252d},
    "f37_bpsg_037_time_to_singularity_proxy_504d": {"inputs": ["close"], "func": f37_bpsg_037_time_to_singularity_proxy_504d},
    "f37_bpsg_038_inverse_time_to_singularity_252d": {"inputs": ["close"], "func": f37_bpsg_038_inverse_time_to_singularity_252d},
    "f37_bpsg_039_inverse_time_to_singularity_504d": {"inputs": ["close"], "func": f37_bpsg_039_inverse_time_to_singularity_504d},
    "f37_bpsg_040_eta_singularity_decline_streak_max_63d": {"inputs": ["close"], "func": f37_bpsg_040_eta_singularity_decline_streak_max_63d},
    "f37_bpsg_041_power_law_exp_252d": {"inputs": ["close"], "func": f37_bpsg_041_power_law_exp_252d},
    "f37_bpsg_042_power_law_exp_504d": {"inputs": ["close"], "func": f37_bpsg_042_power_law_exp_504d},
    "f37_bpsg_043_power_law_exp_1260d": {"inputs": ["close"], "func": f37_bpsg_043_power_law_exp_1260d},
    "f37_bpsg_044_power_law_exp_252d_zscore_1260d": {"inputs": ["close"], "func": f37_bpsg_044_power_law_exp_252d_zscore_1260d},
    "f37_bpsg_045_power_law_exp_252d_diff_21d": {"inputs": ["close"], "func": f37_bpsg_045_power_law_exp_252d_diff_21d},
    "f37_bpsg_046_doubling_time_implied_rate_252d": {"inputs": ["close"], "func": f37_bpsg_046_doubling_time_implied_rate_252d},
    "f37_bpsg_047_doubling_time_implied_rate_504d": {"inputs": ["close"], "func": f37_bpsg_047_doubling_time_implied_rate_504d},
    "f37_bpsg_048_doubling_time_rate_252d_minus_1260d": {"inputs": ["close"], "func": f37_bpsg_048_doubling_time_rate_252d_minus_1260d},
    "f37_bpsg_049_hyper_growth_score_63d": {"inputs": ["close"], "func": f37_bpsg_049_hyper_growth_score_63d},
    "f37_bpsg_050_hyper_growth_score_252d": {"inputs": ["close"], "func": f37_bpsg_050_hyper_growth_score_252d},
    "f37_bpsg_051_hyper_growth_score_252d_zscore_504d": {"inputs": ["close"], "func": f37_bpsg_051_hyper_growth_score_252d_zscore_504d},
    "f37_bpsg_052_hyper_growth_score_above_zero_fraction_252d": {"inputs": ["close"], "func": f37_bpsg_052_hyper_growth_score_above_zero_fraction_252d},
    "f37_bpsg_053_log_log_return_acceleration_252d": {"inputs": ["close"], "func": f37_bpsg_053_log_log_return_acceleration_252d},
    "f37_bpsg_054_eta_to_b_to_c_ratio_252d": {"inputs": ["close"], "func": f37_bpsg_054_eta_to_b_to_c_ratio_252d},
    "f37_bpsg_055_power_law_exp_to_drift_ratio_252d": {"inputs": ["close"], "func": f37_bpsg_055_power_law_exp_to_drift_ratio_252d},
    "f37_bpsg_056_logquad_resid_max_abs_252d": {"inputs": ["close"], "func": f37_bpsg_056_logquad_resid_max_abs_252d},
    "f37_bpsg_057_logquad_resid_max_abs_504d": {"inputs": ["close"], "func": f37_bpsg_057_logquad_resid_max_abs_504d},
    "f37_bpsg_058_logquad_resid_max_abs_252d_zscore_1260d": {"inputs": ["close"], "func": f37_bpsg_058_logquad_resid_max_abs_252d_zscore_1260d},
    "f37_bpsg_059_logquad_resid_last_252d": {"inputs": ["close"], "func": f37_bpsg_059_logquad_resid_last_252d},
    "f37_bpsg_060_logquad_resid_last_504d": {"inputs": ["close"], "func": f37_bpsg_060_logquad_resid_last_504d},
    "f37_bpsg_061_logquad_resid_last_above_2sigma_count_63d": {"inputs": ["close"], "func": f37_bpsg_061_logquad_resid_last_above_2sigma_count_63d},
    "f37_bpsg_062_logquad_resid_last_below_neg2sigma_count_63d": {"inputs": ["close"], "func": f37_bpsg_062_logquad_resid_last_below_neg2sigma_count_63d},
    "f37_bpsg_063_logquad_resid_skew_63d": {"inputs": ["close"], "func": f37_bpsg_063_logquad_resid_skew_63d},
    "f37_bpsg_064_logquad_resid_kurt_63d": {"inputs": ["close"], "func": f37_bpsg_064_logquad_resid_kurt_63d},
    "f37_bpsg_065_logquad_resid_autocorr_lag1_63d": {"inputs": ["close"], "func": f37_bpsg_065_logquad_resid_autocorr_lag1_63d},
    "f37_bpsg_066_logquad_resid_max_in_63d_minus_current": {"inputs": ["close"], "func": f37_bpsg_066_logquad_resid_max_in_63d_minus_current},
    "f37_bpsg_067_parabolic_break_signal_252d": {"inputs": ["close"], "func": f37_bpsg_067_parabolic_break_signal_252d},
    "f37_bpsg_068_parabolic_break_count_252d": {"inputs": ["close"], "func": f37_bpsg_068_parabolic_break_count_252d},
    "f37_bpsg_069_logquad_resid_neg_streak_max_63d": {"inputs": ["close"], "func": f37_bpsg_069_logquad_resid_neg_streak_max_63d},
    "f37_bpsg_070_logquad_resid_pos_streak_max_252d": {"inputs": ["close"], "func": f37_bpsg_070_logquad_resid_pos_streak_max_252d},
    "f37_bpsg_071_logquad_fit_curvature_drawdown_63d": {"inputs": ["close"], "func": f37_bpsg_071_logquad_fit_curvature_drawdown_63d},
    "f37_bpsg_072_logquad_fit_curvature_signflip_count_252d": {"inputs": ["close"], "func": f37_bpsg_072_logquad_fit_curvature_signflip_count_252d},
    "f37_bpsg_073_days_since_logquad_c_positive_252d": {"inputs": ["close"], "func": f37_bpsg_073_days_since_logquad_c_positive_252d},
    "f37_bpsg_074_logquad_c_dispersion_across_subwindows_63d_in_252d": {"inputs": ["close"], "func": f37_bpsg_074_logquad_c_dispersion_across_subwindows_63d_in_252d},
    "f37_bpsg_075_logquad_c_persistence_lag21_252d": {"inputs": ["close"], "func": f37_bpsg_075_logquad_c_persistence_lag21_252d},
}
