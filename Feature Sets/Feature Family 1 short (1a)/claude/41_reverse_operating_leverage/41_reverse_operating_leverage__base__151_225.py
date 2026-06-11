"""reverse_operating_leverage base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for cost-structure rigidity / DOL detection.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly fundamentals only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


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


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f41_rolv_151_variable_to_fixed_cost_ratio(cor: pd.Series, sgna: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """COR / (SGNA + R&D + D&A) — higher = more variable-cost dominated; lower = more fixed-cost exposure."""
    fixed = sgna.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    return _safe_div(cor, fixed)


def f41_rolv_152_realized_dol_during_prior_trough_5y(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Find prior 20q minimum-revenue quarter; compute (Δopinc / Δrevenue) over 4q surrounding that trough."""
    rev_arr = revenue.to_numpy(dtype=float)
    op_arr = opinc.to_numpy(dtype=float)
    n = len(rev_arr)
    out = np.full(n, np.nan, dtype=float)
    win = QQTRS_5Y
    min_obs = max(win // 3, 4)
    half = QQTRS // 2  # 2 quarters either side
    for i in range(n):
        lo = max(0, i - win + 1)
        rw = rev_arr[lo:i + 1]
        valid = ~np.isnan(rw)
        if valid.sum() < min_obs:
            continue
        # rolling-window-local index of trough
        rw_masked = np.where(valid, rw, np.inf)
        trough_local = int(np.argmin(rw_masked))
        if not np.isfinite(rw_masked[trough_local]):
            continue
        trough_global = lo + trough_local
        a = max(0, trough_global - half)
        b = min(n - 1, trough_global + half)
        if b <= a:
            continue
        d_rev = rev_arr[b] - rev_arr[a]
        d_op = op_arr[b] - op_arr[a]
        if not np.isfinite(d_rev) or not np.isfinite(d_op) or d_rev == 0:
            continue
        out[i] = d_op / d_rev
    return pd.Series(out, index=revenue.index).replace([np.inf, -np.inf], np.nan)


def f41_rolv_153_capacity_utilization_trend_slope_8q(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """Linear regression slope of (revenue/ppnenet) over trailing 8q. Negative = decaying utilization."""
    util = _safe_div(revenue, ppnenet)
    win = QQTRS_2Y
    min_periods = max(win // 3, 3)

    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        xv = np.arange(len(w))[valid].astype(float)
        wv = w[valid]
        xm = xv.mean()
        wm = wv.mean()
        num = ((xv - xm) * (wv - wm)).sum()
        den = ((xv - xm) ** 2).sum()
        return num / den if den != 0 else np.nan

    return util.rolling(win, min_periods=min_periods).apply(_slope, raw=True)


def f41_rolv_154_operating_leverage_convexity_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """2nd-derivative of margin-to-revenue: 8q rolling np.polyfit(x=log(revenue), y=opinc/revenue, deg=2) -> x² coef."""
    log_rev = _safe_log(revenue)
    margin = _safe_div(opinc, revenue)
    log_rev_arr = log_rev.to_numpy(dtype=float)
    margin_arr = margin.to_numpy(dtype=float)
    n = len(log_rev_arr)
    out = np.full(n, np.nan, dtype=float)
    win = QQTRS_2Y
    min_obs = max(win // 3, 4)
    for i in range(n):
        lo = max(0, i - win + 1)
        x = log_rev_arr[lo:i + 1]
        y = margin_arr[lo:i + 1]
        valid = ~np.isnan(x) & ~np.isnan(y)
        if valid.sum() < min_obs:
            continue
        xv = x[valid]
        yv = y[valid]
        if np.ptp(xv) == 0:
            continue
        try:
            coefs = np.polyfit(xv, yv, 2)
            out[i] = float(coefs[0])
        except (np.linalg.LinAlgError, ValueError):
            continue
    return pd.Series(out, index=revenue.index).replace([np.inf, -np.inf], np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

REVERSE_OPERATING_LEVERAGE_BASE_REGISTRY_151_225 = {
    "f41_rolv_151_variable_to_fixed_cost_ratio": {"inputs": ["cor", "sgna", "rnd", "depamor"], "func": f41_rolv_151_variable_to_fixed_cost_ratio},
    "f41_rolv_152_realized_dol_during_prior_trough_5y": {"inputs": ["revenue", "opinc"], "func": f41_rolv_152_realized_dol_during_prior_trough_5y},
    "f41_rolv_153_capacity_utilization_trend_slope_8q": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_153_capacity_utilization_trend_slope_8q},
    "f41_rolv_154_operating_leverage_convexity_8q": {"inputs": ["revenue", "opinc"], "func": f41_rolv_154_operating_leverage_convexity_8q},
}
