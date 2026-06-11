"""revenue_growth_deceleration base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for revenue-growth-deceleration detection.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f21_rgdc_151_hard_comp_quarter_detector(revenue: pd.Series) -> pd.Series:
    """+1 when revenue.shift(4) sits in top decile vs trailing 5y (20q) AND current yoy growth < 0."""
    if revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    prior_rev = revenue.shift(QQTRS)
    # 90th-percentile threshold of trailing 5y of the same prior_rev series (right-anchored, PIT)
    p90 = prior_rev.rolling(QQTRS_5Y, min_periods=QQTRS_2Y).quantile(0.9)
    is_hard_comp = prior_rev >= p90
    yoy = _safe_div(revenue, prior_rev) - 1.0
    flag = (is_hard_comp & (yoy < 0)).astype(float)
    # propagate NaN where inputs missing
    flag = flag.where(prior_rev.notna() & p90.notna() & yoy.notna(), np.nan)
    return flag


def f21_rgdc_152_easy_comp_tailwind_decay_rate(revenue: pd.Series) -> pd.Series:
    """Geometric 2y CAGR (revenue / revenue.shift(8))^(1/2) − 1, then qoq diff = decay rate.

    Strips year-prior base effects (easy/hard comp distortions) by averaging over a 2-year window.
    """
    if revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    ratio = _safe_div(revenue, revenue.shift(QQTRS_2Y))
    # geometric 2y CAGR: ratio^(1/2) - 1
    cagr_2y = np.sign(ratio) * (ratio.abs() ** 0.5) - 1.0
    cagr_2y = cagr_2y.where(ratio > 0, np.nan)
    return cagr_2y.diff()


# ============================================================
#                    REGISTRY
# ============================================================

REVENUE_GROWTH_DECELERATION_BASE_REGISTRY_151_225 = {
    "f21_rgdc_151_hard_comp_quarter_detector": {"inputs": ["revenue"], "func": f21_rgdc_151_hard_comp_quarter_detector},
    "f21_rgdc_152_easy_comp_tailwind_decay_rate": {"inputs": ["revenue"], "func": f21_rgdc_152_easy_comp_tailwind_decay_rate},
}
