"""revenue_quality_level d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


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


def f11_rqlv_151_benford_first_digit_chi2_12q_d2(revenue: pd.Series) -> pd.Series:
    benford_p = np.array([np.log10(1.0 + 1.0 / d) for d in range(1, 10)])

    def _chi2(w):
        valid = w[~np.isnan(w)]
        valid = valid[valid != 0]
        if valid.size < 6:
            return np.nan
        a = np.abs(valid)
        with np.errstate(divide="ignore", invalid="ignore"):
            e = np.floor(np.log10(a))
            fd = np.floor(a / (10.0 ** e)).astype(int)
        fd = fd[(fd >= 1) & (fd <= 9)]
        if fd.size == 0:
            return np.nan
        n = fd.size
        obs_counts = np.bincount(fd, minlength=10)[1:10].astype(float)
        exp_counts = benford_p * n
        exp_safe = np.where(exp_counts > 0, exp_counts, np.nan)
        return float(np.nansum(((obs_counts - exp_counts) ** 2) / exp_safe))

    return revenue.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).apply(_chi2, raw=True).diff().diff()


def f11_rqlv_152_revenue_seasonality_residual_std_12q_d2(revenue: pd.Series) -> pd.Series:
    yoy = revenue - revenue.shift(QQTRS)
    yoy_med = yoy.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).median()
    residual = revenue - (revenue.shift(QQTRS) + yoy_med)
    return residual.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).std().diff().diff()


REVENUE_QUALITY_LEVEL_D2_REGISTRY_151_225 = {
    "f11_rqlv_151_benford_first_digit_chi2_12q_d2": {"inputs": ["revenue"], "func": f11_rqlv_151_benford_first_digit_chi2_12q_d2},
    "f11_rqlv_152_revenue_seasonality_residual_std_12q_d2": {"inputs": ["revenue"], "func": f11_rqlv_152_revenue_seasonality_residual_std_12q_d2},
}
