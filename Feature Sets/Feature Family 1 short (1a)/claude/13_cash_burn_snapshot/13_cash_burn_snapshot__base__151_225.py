"""cash_burn_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for cash burn / runway detection.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 fundamentals only. PIT-clean: right-anchored rolling, explicit min_periods,
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


def _ttm(s):
    return s.rolling(QQTRS, min_periods=1).sum()


def _avg4(s):
    return s.rolling(QQTRS, min_periods=1).mean()


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f13_cbsp_151_fcf_ex_sbc_ttm(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """fcf_ttm − sbcomp_ttm — FCF after deducting stock-based comp economic cost."""
    return _ttm(fcf) - _ttm(sbcomp)


def f13_cbsp_152_distance_to_4x_debt_ebitda(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """4.0 − (debt_avg4 / ebitda_ttm). Negative = past leverage trigger."""
    debt_avg4 = _avg4(debt)
    ebitda_ttm = _ttm(ebitda)
    return 4.0 - _safe_div(debt_avg4, ebitda_ttm)


def f13_cbsp_153_months_of_opex_in_cash(cashneq: pd.Series, opex: pd.Series) -> pd.Series:
    """cashneq / (opex_ttm/12) — months of runway. NaN if opex_ttm<=0."""
    opex_ttm = _ttm(opex)
    monthly_opex = _safe_div(opex_ttm, 12.0)
    # blank where opex_ttm <= 0
    monthly_opex = monthly_opex.where(opex_ttm > 0, np.nan)
    return _safe_div(cashneq, monthly_opex)


def f13_cbsp_154_fcf_to_marketcap_intensity(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """|fcf_ttm| / marketcap when fcf<0, else 0 — burn intensity scaled by market cap."""
    fcf_ttm = _ttm(fcf)
    raw = _safe_div(fcf_ttm.abs(), marketcap)
    out = raw.where(fcf_ttm < 0, 0.0)
    # propagate NaN where fcf_ttm or marketcap is NaN
    out = out.where(~(fcf_ttm.isna() | marketcap.isna()), np.nan)
    return out


# ============================================================
#                    REGISTRY
# ============================================================

CASH_BURN_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f13_cbsp_151_fcf_ex_sbc_ttm": {"inputs": ["fcf", "sbcomp"], "func": f13_cbsp_151_fcf_ex_sbc_ttm},
    "f13_cbsp_152_distance_to_4x_debt_ebitda": {"inputs": ["debt", "ebitda"], "func": f13_cbsp_152_distance_to_4x_debt_ebitda},
    "f13_cbsp_153_months_of_opex_in_cash": {"inputs": ["cashneq", "opex"], "func": f13_cbsp_153_months_of_opex_in_cash},
    "f13_cbsp_154_fcf_to_marketcap_intensity": {"inputs": ["fcf", "marketcap"], "func": f13_cbsp_154_fcf_to_marketcap_intensity},
}
