"""margin_collapse_acceleration d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def _yoy(s):
    return _safe_div(s - s.shift(QQTRS), s.shift(QQTRS).abs())


def f30_mcac_151_hmm_rev_margin_joint_state_posterior_8q_d3(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    if revenue is None or opinc is None:
        return pd.Series(np.nan)
    rev_yoy = _yoy(revenue)
    om = _safe_div(opinc, revenue)
    df = pd.concat([rev_yoy, om], axis=1)
    df.columns = ["a", "b"]
    a_med = df["a"].rolling(QQTRS_2Y, min_periods=4).median()
    b_med = df["b"].rolling(QQTRS_2Y, min_periods=4).median()
    a_min = df["a"].rolling(QQTRS_2Y, min_periods=4).min()
    b_min = df["b"].rolling(QQTRS_2Y, min_periods=4).min()
    a_sd = df["a"].rolling(QQTRS_2Y, min_periods=4).std().replace(0, np.nan)
    b_sd = df["b"].rolling(QQTRS_2Y, min_periods=4).std().replace(0, np.nan)
    da_h = ((df["a"] - a_med) / a_sd) ** 2
    db_h = ((df["b"] - b_med) / b_sd) ** 2
    da_d = ((df["a"] - a_min) / a_sd) ** 2
    db_d = ((df["b"] - b_min) / b_sd) ** 2
    dist_h = np.sqrt(da_h + db_h)
    dist_d = np.sqrt(da_d + db_d)
    inv_h = 1.0 / dist_h.replace(0, np.nan)
    inv_d = 1.0 / dist_d.replace(0, np.nan)
    denom = (inv_h + inv_d).replace(0, np.nan)
    return _safe_div(inv_d, denom).diff().diff().diff()


def f30_mcac_152_conditional_om_accel_by_rev_decile_8q_d3(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    if revenue is None or opinc is None:
        return pd.Series(np.nan)
    rev_yoy = _yoy(revenue)
    om = _safe_div(opinc, revenue)
    om_accel = om.diff().diff()
    om_accel_z = _rolling_zscore(om_accel, QQTRS_2Y, min_periods=4)
    q30 = rev_yoy.rolling(QQTRS_2Y, min_periods=4).quantile(0.30)
    gate = (rev_yoy <= q30).astype(float)
    gated = om_accel_z * gate.replace(0, np.nan)
    return gated.rolling(QQTRS_2Y, min_periods=2).mean().diff().diff().diff()


MARGIN_COLLAPSE_ACCELERATION_D3_REGISTRY_151_225 = {
    "f30_mcac_151_hmm_rev_margin_joint_state_posterior_8q_d3": {"inputs": ["revenue", "opinc"], "func": f30_mcac_151_hmm_rev_margin_joint_state_posterior_8q_d3},
    "f30_mcac_152_conditional_om_accel_by_rev_decile_8q_d3": {"inputs": ["revenue", "opinc"], "func": f30_mcac_152_conditional_om_accel_by_rev_decile_8q_d3},
}
