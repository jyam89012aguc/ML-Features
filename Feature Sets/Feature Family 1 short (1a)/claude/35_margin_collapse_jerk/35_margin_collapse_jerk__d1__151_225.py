"""margin_collapse_jerk d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def f35_mcjk_151_margin_jerk_onset_after_calm_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    if revenue is None or opinc is None:
        return pd.Series(np.nan)
    om = _safe_div(opinc, revenue)
    jerk = om.diff().diff().diff()
    jz = _rolling_zscore(jerk, QQTRS_4Y, min_periods=6).abs()
    prior_max = jz.shift(1).rolling(QQTRS, min_periods=2).max()
    cond = (jz > 3.0) & (prior_max < 1.0)
    out = cond.astype(float)
    return out.where(jz.notna() & prior_max.notna(), np.nan).diff()


def f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    if revenue is None or gp is None:
        return pd.Series(np.nan)
    cogs = revenue - gp
    cogs_jerk = cogs.diff().diff().diff()
    rev_jerk = revenue.diff().diff().diff()
    cogs_z = _rolling_zscore(cogs_jerk, QQTRS_2Y, min_periods=4)
    rev_z = _rolling_zscore(rev_jerk, QQTRS_2Y, min_periods=4)
    cond = (cogs_z > 2.0) & (rev_z.abs() < 1.0)
    out = cond.astype(float)
    return out.where(cogs_z.notna() & rev_z.notna(), np.nan).diff()


MARGIN_COLLAPSE_JERK_D1_REGISTRY_151_225 = {
    "f35_mcjk_151_margin_jerk_onset_after_calm_d1": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_151_margin_jerk_onset_after_calm_d1},
    "f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator_d1": {"inputs": ["revenue", "gp"], "func": f35_mcjk_152_cogs_jerk_without_rev_jerk_indicator_d1},
}
