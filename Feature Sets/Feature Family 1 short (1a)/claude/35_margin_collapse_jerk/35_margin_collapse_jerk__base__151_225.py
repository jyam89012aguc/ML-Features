"""margin_collapse_jerk base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for margin-jerk leading indicators.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_4Y = 16
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


def f35_mcjk_151_margin_jerk_onset_after_calm(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """om = opinc/revenue; jerk = om.diff().diff().diff(). +1 if |current jerk z (16q)| > 3 AND prior 4q |jerk z| < 1."""
    if revenue is None or opinc is None:
        return pd.Series(np.nan)
    om = _safe_div(opinc, revenue)
    jerk = om.diff().diff().diff()
    jz = _rolling_zscore(jerk, QQTRS_4Y, min_periods=6).abs()
    prior_max = jz.shift(1).rolling(QQTRS, min_periods=2).max()
    cond = (jz > 3.0) & (prior_max < 1.0)
    out = cond.astype(float)
    return out.where(jz.notna() & prior_max.notna(), np.nan)


def f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """cogs = revenue − gp; cogs_jerk z (8q) > 2 AND revenue_jerk z (8q) < 1 → +1 (pricing-power loss leading indicator)."""
    if revenue is None or gp is None:
        return pd.Series(np.nan)
    cogs = revenue - gp
    cogs_jerk = cogs.diff().diff().diff()
    rev_jerk = revenue.diff().diff().diff()
    cogs_z = _rolling_zscore(cogs_jerk, QQTRS_2Y, min_periods=4)
    rev_z = _rolling_zscore(rev_jerk, QQTRS_2Y, min_periods=4)
    cond = (cogs_z > 2.0) & (rev_z.abs() < 1.0)
    out = cond.astype(float)
    return out.where(cogs_z.notna() & rev_z.notna(), np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

MARGIN_COLLAPSE_JERK_BASE_REGISTRY_151_225 = {
    "f35_mcjk_151_margin_jerk_onset_after_calm": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_151_margin_jerk_onset_after_calm},
    "f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator": {"inputs": ["revenue", "gp"], "func": f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator},
}
