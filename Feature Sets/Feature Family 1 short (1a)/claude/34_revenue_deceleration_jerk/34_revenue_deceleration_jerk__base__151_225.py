"""revenue_deceleration_jerk base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for jerk-based revenue cliff detection.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly. PIT-clean: right-anchored rolling, explicit min_periods,
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


def _yoy(s):
    return _safe_div(s - s.shift(QQTRS), s.shift(QQTRS).abs())


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f34_rdjk_151_cliff_edge_jerk_conditional_on_neg_accel(revenue: pd.Series) -> pd.Series:
    """Max |jerk| in last 8q, gated to q where accel < 0. yoy → accel = yoy.diff().diff(); jerk = yoy.diff().diff().diff()."""
    if revenue is None:
        return pd.Series(np.nan)
    yoy = _yoy(revenue)
    accel = yoy.diff().diff()
    jerk = yoy.diff().diff().diff()
    gated = jerk.abs().where(accel < 0, np.nan)
    return gated.rolling(QQTRS_2Y, min_periods=2).max()


def f34_rdjk_152_jerk_onset_consistency_4q_8q_12q(revenue: pd.Series) -> pd.Series:
    """Sum: +1 per window where current |jerk z (W)| > 3 AND prior 4q |jerk z (W)| < 1, W ∈ {4q, 8q, 12q}."""
    if revenue is None:
        return pd.Series(np.nan)
    yoy = _yoy(revenue)
    jerk = yoy.diff().diff().diff()

    def _onset(window):
        jz = _rolling_zscore(jerk, window, min_periods=max(window // 3, 2)).abs()
        prior_max = jz.shift(1).rolling(QQTRS, min_periods=2).max()
        cond = (jz > 3.0) & (prior_max < 1.0)
        return cond.astype(float).where(jz.notna() & prior_max.notna(), np.nan)

    f4 = _onset(QQTRS)
    f8 = _onset(QQTRS_2Y)
    f12 = _onset(QQTRS_3Y)
    return f4.fillna(0) + f8.fillna(0) + f12.fillna(0)


# ============================================================
#                    REGISTRY
# ============================================================

REVENUE_DECELERATION_JERK_BASE_REGISTRY_151_225 = {
    "f34_rdjk_151_cliff_edge_jerk_conditional_on_neg_accel": {"inputs": ["revenue"], "func": f34_rdjk_151_cliff_edge_jerk_conditional_on_neg_accel},
    "f34_rdjk_152_jerk_onset_consistency_4q_8q_12q": {"inputs": ["revenue"], "func": f34_rdjk_152_jerk_onset_consistency_4q_8q_12q},
}
