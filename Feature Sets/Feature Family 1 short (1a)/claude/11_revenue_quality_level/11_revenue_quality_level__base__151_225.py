"""revenue_quality_level base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for revenue-quality detection.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 fundamentals only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
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


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f11_rqlv_151_benford_first_digit_chi2_12q(revenue: pd.Series) -> pd.Series:
    """Chi-square stat of first-digit distribution of quarterly revenue values (last 12q) vs Benford expected.

    Benford expected p(d) = log10(1 + 1/d) for d=1..9. First digit derived from
    floor(|x| / 10**floor(log10(|x|))). Returns Σ((obs−exp)²/exp).
    """
    benford_p = np.array([np.log10(1.0 + 1.0 / d) for d in range(1, 10)])

    def _chi2(w):
        valid = w[~np.isnan(w)]
        valid = valid[valid != 0]
        if valid.size < 6:
            return np.nan
        a = np.abs(valid)
        # first digit via floor(a / 10**floor(log10(a)))
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

    return revenue.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).apply(_chi2, raw=True)


def f11_rqlv_152_revenue_seasonality_residual_std_12q(revenue: pd.Series) -> pd.Series:
    """Stddev of residuals from yoy-seasonal model over 12q.

    residual_t = revenue_t − rolling-median over 12q of (revenue − revenue.shift(4));
    return stddev of residuals over 12q.
    """
    yoy = revenue - revenue.shift(QQTRS)
    yoy_med = yoy.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).median()
    residual = revenue - (revenue.shift(QQTRS) + yoy_med)
    return residual.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 2, 4)).std()


# ============================================================
#                    REGISTRY
# ============================================================

REVENUE_QUALITY_LEVEL_BASE_REGISTRY_151_225 = {
    "f11_rqlv_151_benford_first_digit_chi2_12q": {"inputs": ["revenue"], "func": f11_rqlv_151_benford_first_digit_chi2_12q},
    "f11_rqlv_152_revenue_seasonality_residual_std_12q": {"inputs": ["revenue"], "func": f11_rqlv_152_revenue_seasonality_residual_std_12q},
}
