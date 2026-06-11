"""debt_buildup_trajectory d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
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


def f24_dbtj_151_distance_to_4x_debt_ebitda_d2(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    if debt is None or ebitda is None or len(debt) == 0:
        return pd.Series(np.nan, index=getattr(debt, "index", None))
    debt_avg4q = debt.rolling(QQTRS, min_periods=2).mean()
    ebitda_ttm = ebitda.rolling(QQTRS, min_periods=2).sum()
    return (4.0 - _safe_div(debt_avg4q, ebitda_ttm)).diff().diff()


DEBT_BUILDUP_TRAJECTORY_D2_REGISTRY_151_225 = {
    "f24_dbtj_151_distance_to_4x_debt_ebitda_d2": {"inputs": ["debt", "ebitda"], "func": f24_dbtj_151_distance_to_4x_debt_ebitda_d2},
}
