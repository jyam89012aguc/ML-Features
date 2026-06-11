"""leverage_buildup_acceleration base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for distressed leverage buildup detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

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


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f32_lbac_151_issuance_on_distress_indicator_q(debt: pd.Series, marketcap: pd.Series) -> pd.Series:
    """+1 if debt qoq z > 2 AND marketcap drawdown (1 − mc/mc.rolling(4).max()) > 0.30."""
    if debt is None or marketcap is None:
        return pd.Series(np.nan)
    debt_qoq = debt.diff()
    debt_z = _rolling_zscore(debt_qoq, QQTRS_2Y, min_periods=4)
    mc_max4 = marketcap.rolling(QQTRS, min_periods=2).max()
    dd = 1.0 - _safe_div(marketcap, mc_max4)
    cond = (debt_z > 2.0) & (dd > 0.30)
    out = cond.astype(float)
    return out.where(debt_z.notna() & dd.notna(), np.nan)


def f32_lbac_152_net_debt_sign_flip_then_accel_q(debt: pd.Series, cashneq: pd.Series) -> pd.Series:
    """+1 if net debt was declining 4q (each q < prior) then current q increase > 2σ of prior 4q changes."""
    if debt is None or cashneq is None:
        return pd.Series(np.nan)
    net_debt = debt - cashneq
    nd_ch = net_debt.diff()
    # Declining for 4 consecutive q before current = all four (t-4..t-1) negative
    decl1 = nd_ch.shift(1) < 0
    decl2 = nd_ch.shift(2) < 0
    decl3 = nd_ch.shift(3) < 0
    decl4 = nd_ch.shift(4) < 0
    declining = decl1 & decl2 & decl3 & decl4
    # Std of prior 4q changes
    prior_sd = nd_ch.shift(1).rolling(QQTRS, min_periods=2).std()
    cond_jump = nd_ch > (2.0 * prior_sd)
    out = (declining & cond_jump).astype(float)
    return out.where(prior_sd.notna() & nd_ch.notna(), np.nan)


def f32_lbac_153_leverage_regime_2state_posterior(debt: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Joint 2-state posterior on (debt/ebitda, ebit/intexp) — Mahalanobis-distance proxy. P(distressed)."""
    if debt is None or ebitda is None or ebit is None or intexp is None:
        return pd.Series(np.nan)
    lev = _safe_div(debt, ebitda)
    icov = _safe_div(ebit, intexp)
    df = pd.concat([lev, icov], axis=1)
    df.columns = ["a", "b"]
    # Healthy: low lev, high icov → use median for healthy
    a_med = df["a"].rolling(QQTRS_2Y, min_periods=4).median()
    b_med = df["b"].rolling(QQTRS_2Y, min_periods=4).median()
    # Distressed: high lev (max), low icov (min)
    a_dist = df["a"].rolling(QQTRS_2Y, min_periods=4).max()
    b_dist = df["b"].rolling(QQTRS_2Y, min_periods=4).min()
    a_sd = df["a"].rolling(QQTRS_2Y, min_periods=4).std().replace(0, np.nan)
    b_sd = df["b"].rolling(QQTRS_2Y, min_periods=4).std().replace(0, np.nan)
    dist_h = np.sqrt(((df["a"] - a_med) / a_sd) ** 2 + ((df["b"] - b_med) / b_sd) ** 2)
    dist_d = np.sqrt(((df["a"] - a_dist) / a_sd) ** 2 + ((df["b"] - b_dist) / b_sd) ** 2)
    inv_h = 1.0 / dist_h.replace(0, np.nan)
    inv_d = 1.0 / dist_d.replace(0, np.nan)
    denom = (inv_h + inv_d).replace(0, np.nan)
    return _safe_div(inv_d, denom)


# ============================================================
#                    REGISTRY
# ============================================================

LEVERAGE_BUILDUP_ACCELERATION_BASE_REGISTRY_151_225 = {
    "f32_lbac_151_issuance_on_distress_indicator_q": {"inputs": ["debt", "marketcap"], "func": f32_lbac_151_issuance_on_distress_indicator_q},
    "f32_lbac_152_net_debt_sign_flip_then_accel_q": {"inputs": ["debt", "cashneq"], "func": f32_lbac_152_net_debt_sign_flip_then_accel_q},
    "f32_lbac_153_leverage_regime_2state_posterior": {"inputs": ["debt", "ebitda", "ebit", "intexp"], "func": f32_lbac_153_leverage_regime_2state_posterior},
}
