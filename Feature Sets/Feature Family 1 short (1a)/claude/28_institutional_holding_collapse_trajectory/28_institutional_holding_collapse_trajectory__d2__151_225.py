"""institutional_holding_collapse_trajectory d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20
QDAYS = 63


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


def f28_ihct_151_lockup_expiry_window_flag_d2(inst_units: pd.Series, days_since_ipo: pd.Series) -> pd.Series:
    if days_since_ipo is None or len(days_since_ipo) == 0:
        idx = getattr(inst_units, "index", None)
        if idx is None:
            idx = getattr(days_since_ipo, "index", None)
        return pd.Series(np.nan, index=idx)
    dsi = pd.Series(days_since_ipo).astype(float)
    flag = ((dsi >= 165) & (dsi <= 195)).astype(float)
    flag = flag.where(dsi.notna(), np.nan)
    return flag.diff().diff()


INSTITUTIONAL_HOLDING_COLLAPSE_TRAJECTORY_D2_REGISTRY_151_225 = {
    "f28_ihct_151_lockup_expiry_window_flag_d2": {"inputs": ["inst_units", "days_since_ipo"], "func": f28_ihct_151_lockup_expiry_window_flag_d2},
}
