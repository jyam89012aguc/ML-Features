"""cash_burn_acceleration base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for cash burn/runway detection.
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


def f31_cbac_151_runway_doubling_down_indicator_q(fcf: pd.Series, cashneq: pd.Series) -> pd.Series:
    """+1 if |fcf_q| > 2 × prior 4q mean |fcf| AND cashneq < 0.5 × prior 4q mean cashneq."""
    if fcf is None or cashneq is None:
        return pd.Series(np.nan)
    abs_fcf = fcf.abs()
    prior_fcf_mean = abs_fcf.shift(1).rolling(QQTRS, min_periods=2).mean()
    prior_cash_mean = cashneq.shift(1).rolling(QQTRS, min_periods=2).mean()
    cond1 = abs_fcf > 2.0 * prior_fcf_mean
    cond2 = cashneq < 0.5 * prior_cash_mean
    out = (cond1 & cond2).astype(float)
    return out.where(prior_fcf_mean.notna() & prior_cash_mean.notna() & fcf.notna() & cashneq.notna(), np.nan)


def f31_cbac_152_financing_bridge_collapse_q(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """+1 if rolling 4q ncff > 0 (sustained financing inflow) THEN current ncff_q < 0."""
    if ncff is None or ncfo is None:
        return pd.Series(np.nan)
    prior_ncff_sum = ncff.rolling(QQTRS, min_periods=2).sum().shift(1)
    cond1 = prior_ncff_sum > 0
    cond2 = ncff < 0
    out = (cond1 & cond2).astype(float)
    return out.where(prior_ncff_sum.notna() & ncff.notna(), np.nan)


def f31_cbac_153_going_concern_composite_q(cashneq: pd.Series, fcf: pd.Series, debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """+1 if cashneq < 4 × |fcf_q| AND fcf<0 AND debtc/debt > 0.5 (short-maturity dominant)."""
    if cashneq is None or fcf is None or debtc is None or debt is None:
        return pd.Series(np.nan)
    cond1 = cashneq < (4.0 * fcf.abs())
    cond2 = fcf < 0
    short_ratio = _safe_div(debtc, debt)
    cond3 = short_ratio > 0.5
    out = (cond1 & cond2 & cond3).astype(float)
    valid = cashneq.notna() & fcf.notna() & debtc.notna() & debt.notna()
    return out.where(valid, np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

CASH_BURN_ACCELERATION_BASE_REGISTRY_151_225 = {
    "f31_cbac_151_runway_doubling_down_indicator_q": {"inputs": ["fcf", "cashneq"], "func": f31_cbac_151_runway_doubling_down_indicator_q},
    "f31_cbac_152_financing_bridge_collapse_q": {"inputs": ["ncff", "ncfo"], "func": f31_cbac_152_financing_bridge_collapse_q},
    "f31_cbac_153_going_concern_composite_q": {"inputs": ["cashneq", "fcf", "debtc", "debt"], "func": f31_cbac_153_going_concern_composite_q},
}
