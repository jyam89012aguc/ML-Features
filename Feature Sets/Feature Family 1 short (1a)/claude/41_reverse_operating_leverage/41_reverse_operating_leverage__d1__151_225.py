"""reverse_operating_leverage d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def f41_rolv_151_variable_to_fixed_cost_ratio_d1(cor: pd.Series, sgna: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    fixed = sgna.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    return _safe_div(cor, fixed).diff()


def f41_rolv_152_realized_dol_during_prior_trough_5y_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    rev_arr = revenue.to_numpy(dtype=float)
    op_arr = opinc.to_numpy(dtype=float)
    n = len(rev_arr)
    out = np.full(n, np.nan, dtype=float)
    win = QQTRS_5Y
    min_obs = max(win // 3, 4)
    half = QQTRS // 2
    for i in range(n):
        lo = max(0, i - win + 1)
        rw = rev_arr[lo:i + 1]
        valid = ~np.isnan(rw)
        if valid.sum() < min_obs:
            continue
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
    return pd.Series(out, index=revenue.index).replace([np.inf, -np.inf], np.nan).diff()


def f41_rolv_153_capacity_utilization_trend_slope_8q_d1(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
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

    return util.rolling(win, min_periods=min_periods).apply(_slope, raw=True).diff()


def f41_rolv_154_operating_leverage_convexity_8q_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
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
    return pd.Series(out, index=revenue.index).replace([np.inf, -np.inf], np.nan).diff()


REVERSE_OPERATING_LEVERAGE_D1_REGISTRY_151_225 = {
    "f41_rolv_151_variable_to_fixed_cost_ratio_d1": {"inputs": ["cor", "sgna", "rnd", "depamor"], "func": f41_rolv_151_variable_to_fixed_cost_ratio_d1},
    "f41_rolv_152_realized_dol_during_prior_trough_5y_d1": {"inputs": ["revenue", "opinc"], "func": f41_rolv_152_realized_dol_during_prior_trough_5y_d1},
    "f41_rolv_153_capacity_utilization_trend_slope_8q_d1": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_153_capacity_utilization_trend_slope_8q_d1},
    "f41_rolv_154_operating_leverage_convexity_8q_d1": {"inputs": ["revenue", "opinc"], "func": f41_rolv_154_operating_leverage_convexity_8q_d1},
}
