"""blowoff_parabolic_signature base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for parabolic / power-law / hyperbolic blowoff detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _quad_coeff_c(w):
    """Quadratic coefficient c in c*t^2 + b*t + a on values w (centered t=0..n-1)."""
    valid = ~np.isnan(w)
    if valid.sum() < 20:
        return np.nan
    y = w[valid]
    x = np.arange(len(w), dtype=float)[valid]
    try:
        c, b, a = np.polyfit(x, y, 2)
    except Exception:
        return np.nan
    return float(c)


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f37_bpsg_151_acceleration_then_flatten_indicator_252d(close: pd.Series) -> pd.Series:
    """+1 if 252d-126d prior 252d-window quadratic c > 0.0001 (was accelerating) AND |recent 63d c| < 0.0001*|prior c|. Else 0."""
    logc = _safe_log(close)
    c_recent = logc.rolling(QDAYS, min_periods=max(QDAYS // 2, 20)).apply(_quad_coeff_c, raw=True)
    c_prior_full = logc.rolling(YDAYS, min_periods=max(YDAYS // 2, 60)).apply(_quad_coeff_c, raw=True)
    c_prior = c_prior_full.shift(126)
    cond_prior_accel = c_prior > 0.0001
    cond_recent_flat = c_recent.abs() < (0.0001 * c_prior.abs())
    out = (cond_prior_accel & cond_recent_flat).astype(float)
    out = out.where(c_recent.notna() & c_prior.notna(), np.nan)
    return out


def f37_bpsg_152_power_law_exp_252d_standard_error(close: pd.Series) -> pd.Series:
    """Std error of slope b in log(close) = a + b*log(t) over trailing 252d."""
    logc = _safe_log(close)

    def _se_b(y):
        valid = ~np.isnan(y)
        if valid.sum() < 60:
            return np.nan
        yv = y[valid]
        # t index inside the window, 1-based to avoid log(0)
        idx = np.where(valid)[0] + 1.0
        x = np.log(idx)
        n = len(yv)
        x_mean = x.mean()
        y_mean = yv.mean()
        sxx = ((x - x_mean) ** 2).sum()
        if sxx <= 0:
            return np.nan
        sxy = ((x - x_mean) * (yv - y_mean)).sum()
        b = sxy / sxx
        a = y_mean - b * x_mean
        resid = yv - (a + b * x)
        if n - 2 <= 0:
            return np.nan
        sigma2 = (resid ** 2).sum() / (n - 2)
        if sigma2 < 0 or not np.isfinite(sigma2):
            return np.nan
        se_b = np.sqrt(sigma2 / sxx)
        return float(se_b)

    return logc.rolling(YDAYS, min_periods=max(YDAYS // 2, 60)).apply(_se_b, raw=True)


def f37_bpsg_153_hyperbolic_growth_singularity_fit_252d(close: pd.Series) -> pd.Series:
    """Fit 1/close = (t* - t)/a → linear OLS of 1/close on t. Return implied (t* - current_t).

    From slope = -1/a (so a = -1/slope) and intercept = t*/a (so t* = intercept*a = -intercept/slope).
    Implied days-to-singularity at end of window = t* - t_last (t_last = n-1 in window coords).
    """
    def _t_star_minus_now(y):
        valid = ~np.isnan(y) & (y > 0)
        if valid.sum() < 60:
            return np.nan
        yv = y[valid]
        inv_c = 1.0 / yv
        t_idx = np.where(valid)[0].astype(float)
        n_full = len(y)
        # OLS slope/intercept of inv_c on t_idx
        try:
            slope, intercept = np.polyfit(t_idx, inv_c, 1)
        except Exception:
            return np.nan
        if slope == 0 or not np.isfinite(slope):
            return np.nan
        # t* = -intercept / slope (since intercept = t*/a and slope = -1/a → t* = -intercept/slope)
        t_star = -intercept / slope
        t_last = float(n_full - 1)
        days_to = t_star - t_last
        if not np.isfinite(days_to):
            return np.nan
        return float(days_to)

    return close.rolling(YDAYS, min_periods=max(YDAYS // 2, 60)).apply(_t_star_minus_now, raw=True)


# ============================================================
#                    REGISTRY
# ============================================================

BLOWOFF_PARABOLIC_SIGNATURE_BASE_REGISTRY_151_225 = {
    "f37_bpsg_151_acceleration_then_flatten_indicator_252d": {"inputs": ["close"], "func": f37_bpsg_151_acceleration_then_flatten_indicator_252d},
    "f37_bpsg_152_power_law_exp_252d_standard_error": {"inputs": ["close"], "func": f37_bpsg_152_power_law_exp_252d_standard_error},
    "f37_bpsg_153_hyperbolic_growth_singularity_fit_252d": {"inputs": ["close"], "func": f37_bpsg_153_hyperbolic_growth_singularity_fit_252d},
}
