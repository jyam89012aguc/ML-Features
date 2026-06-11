"""cash_flow_deterioration_trajectory base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for cash-flow deterioration detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
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


def f23_cfdt_151_dividend_cut_emergence_indicator_q(ncfdiv: pd.Series) -> pd.Series:
    """+1 if |ncfdiv_q| dropped ≥50% from prior 4q rolling mean of |ncfdiv|.

    ncfdiv is typically negative (cash outflow); use absolute magnitude.
    """
    if ncfdiv is None or len(ncfdiv) == 0:
        return pd.Series(np.nan, index=getattr(ncfdiv, "index", None))
    abs_div = ncfdiv.abs()
    prior_mean = abs_div.shift(1).rolling(QQTRS, min_periods=2).mean()
    drop = _safe_div(abs_div, prior_mean) - 1.0
    flag = (drop <= -0.5).astype(float)
    flag = flag.where(prior_mean.notna() & abs_div.notna() & (prior_mean > 0), np.nan)
    return flag


def f23_cfdt_152_buyback_funded_by_burn_indicator(ncfcommon: pd.Series, ncfo: pd.Series) -> pd.Series:
    """+1 if ncfcommon < 0 (net buyback) AND ncfo_ttm < ncfo_ttm.shift(4) (operating cash declining yoy)."""
    if ncfcommon is None or ncfo is None or len(ncfcommon) == 0:
        return pd.Series(np.nan, index=getattr(ncfcommon, "index", None))
    ncfo_ttm = ncfo.rolling(QQTRS, min_periods=2).sum()
    ncfo_decline = ncfo_ttm < ncfo_ttm.shift(QQTRS)
    is_buyback = ncfcommon < 0
    flag = (is_buyback & ncfo_decline).astype(float)
    flag = flag.where(ncfcommon.notna() & ncfo_ttm.notna() & ncfo_ttm.shift(QQTRS).notna(), np.nan)
    return flag


def f23_cfdt_153_capex_collapse_with_buyback_indicator(capex: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """+1 if capex_qoq_pct < -0.5 AND ncfcommon < 0 in same q (slashing investment to fund buybacks)."""
    if capex is None or ncfcommon is None or len(capex) == 0:
        return pd.Series(np.nan, index=getattr(capex, "index", None))
    # capex is typically reported as negative; use absolute magnitude for percent-change semantics
    abs_capex = capex.abs()
    capex_qoq = _safe_div(abs_capex, abs_capex.shift(1)) - 1.0
    capex_collapse = capex_qoq < -0.5
    is_buyback = ncfcommon < 0
    flag = (capex_collapse & is_buyback).astype(float)
    flag = flag.where(capex_qoq.notna() & ncfcommon.notna(), np.nan)
    return flag


# ============================================================
#                    REGISTRY
# ============================================================

CASH_FLOW_DETERIORATION_TRAJECTORY_BASE_REGISTRY_151_225 = {
    "f23_cfdt_151_dividend_cut_emergence_indicator_q": {"inputs": ["ncfdiv"], "func": f23_cfdt_151_dividend_cut_emergence_indicator_q},
    "f23_cfdt_152_buyback_funded_by_burn_indicator": {"inputs": ["ncfcommon", "ncfo"], "func": f23_cfdt_152_buyback_funded_by_burn_indicator},
    "f23_cfdt_153_capex_collapse_with_buyback_indicator": {"inputs": ["capex", "ncfcommon"], "func": f23_cfdt_153_capex_collapse_with_buyback_indicator},
}
