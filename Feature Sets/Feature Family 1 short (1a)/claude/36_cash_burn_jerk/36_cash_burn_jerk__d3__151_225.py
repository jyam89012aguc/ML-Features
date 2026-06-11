"""cash_burn_jerk d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def f36_cbjk_151_burn_jerk_onset_after_calm_d3(ncfo: pd.Series) -> pd.Series:
    if ncfo is None:
        return pd.Series(np.nan)
    jerk = ncfo.diff().diff().diff()
    jz = _rolling_zscore(jerk, QQTRS_2Y, min_periods=4).abs()
    prior_max = jz.shift(1).rolling(QQTRS, min_periods=2).max()
    cond = (jz > 3.0) & (prior_max < 1.0)
    out = cond.astype(float)
    return out.where(jz.notna() & prior_max.notna(), np.nan).diff().diff().diff()


CASH_BURN_JERK_D3_REGISTRY_151_225 = {
    "f36_cbjk_151_burn_jerk_onset_after_calm_d3": {"inputs": ["ncfo"], "func": f36_cbjk_151_burn_jerk_onset_after_calm_d3},
}
