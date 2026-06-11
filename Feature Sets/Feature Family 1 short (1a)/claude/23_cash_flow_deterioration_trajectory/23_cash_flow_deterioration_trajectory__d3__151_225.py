"""cash_flow_deterioration_trajectory d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def f23_cfdt_151_dividend_cut_emergence_indicator_q_d3(ncfdiv: pd.Series) -> pd.Series:
    if ncfdiv is None or len(ncfdiv) == 0:
        return pd.Series(np.nan, index=getattr(ncfdiv, "index", None))
    abs_div = ncfdiv.abs()
    prior_mean = abs_div.shift(1).rolling(QQTRS, min_periods=2).mean()
    drop = _safe_div(abs_div, prior_mean) - 1.0
    flag = (drop <= -0.5).astype(float)
    flag = flag.where(prior_mean.notna() & abs_div.notna() & (prior_mean > 0), np.nan)
    return flag.diff().diff().diff()


def f23_cfdt_152_buyback_funded_by_burn_indicator_d3(ncfcommon: pd.Series, ncfo: pd.Series) -> pd.Series:
    if ncfcommon is None or ncfo is None or len(ncfcommon) == 0:
        return pd.Series(np.nan, index=getattr(ncfcommon, "index", None))
    ncfo_ttm = ncfo.rolling(QQTRS, min_periods=2).sum()
    ncfo_decline = ncfo_ttm < ncfo_ttm.shift(QQTRS)
    is_buyback = ncfcommon < 0
    flag = (is_buyback & ncfo_decline).astype(float)
    flag = flag.where(ncfcommon.notna() & ncfo_ttm.notna() & ncfo_ttm.shift(QQTRS).notna(), np.nan)
    return flag.diff().diff().diff()


def f23_cfdt_153_capex_collapse_with_buyback_indicator_d3(capex: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    if capex is None or ncfcommon is None or len(capex) == 0:
        return pd.Series(np.nan, index=getattr(capex, "index", None))
    abs_capex = capex.abs()
    capex_qoq = _safe_div(abs_capex, abs_capex.shift(1)) - 1.0
    capex_collapse = capex_qoq < -0.5
    is_buyback = ncfcommon < 0
    flag = (capex_collapse & is_buyback).astype(float)
    flag = flag.where(capex_qoq.notna() & ncfcommon.notna(), np.nan)
    return flag.diff().diff().diff()


CASH_FLOW_DETERIORATION_TRAJECTORY_D3_REGISTRY_151_225 = {
    "f23_cfdt_151_dividend_cut_emergence_indicator_q_d3": {"inputs": ["ncfdiv"], "func": f23_cfdt_151_dividend_cut_emergence_indicator_q_d3},
    "f23_cfdt_152_buyback_funded_by_burn_indicator_d3": {"inputs": ["ncfcommon", "ncfo"], "func": f23_cfdt_152_buyback_funded_by_burn_indicator_d3},
    "f23_cfdt_153_capex_collapse_with_buyback_indicator_d3": {"inputs": ["capex", "ncfcommon"], "func": f23_cfdt_153_capex_collapse_with_buyback_indicator_d3},
}
