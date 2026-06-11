"""revenue_growth_deceleration d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def f21_rgdc_151_hard_comp_quarter_detector_d1(revenue: pd.Series) -> pd.Series:
    if revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    prior_rev = revenue.shift(QQTRS)
    p90 = prior_rev.rolling(QQTRS_5Y, min_periods=QQTRS_2Y).quantile(0.9)
    is_hard_comp = prior_rev >= p90
    yoy = _safe_div(revenue, prior_rev) - 1.0
    flag = (is_hard_comp & (yoy < 0)).astype(float)
    flag = flag.where(prior_rev.notna() & p90.notna() & yoy.notna(), np.nan)
    return flag.diff()


def f21_rgdc_152_easy_comp_tailwind_decay_rate_d1(revenue: pd.Series) -> pd.Series:
    if revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    ratio = _safe_div(revenue, revenue.shift(QQTRS_2Y))
    cagr_2y = np.sign(ratio) * (ratio.abs() ** 0.5) - 1.0
    cagr_2y = cagr_2y.where(ratio > 0, np.nan)
    return cagr_2y.diff().diff()


REVENUE_GROWTH_DECELERATION_D1_REGISTRY_151_225 = {
    "f21_rgdc_151_hard_comp_quarter_detector_d1": {"inputs": ["revenue"], "func": f21_rgdc_151_hard_comp_quarter_detector_d1},
    "f21_rgdc_152_easy_comp_tailwind_decay_rate_d1": {"inputs": ["revenue"], "func": f21_rgdc_152_easy_comp_tailwind_decay_rate_d1},
}
