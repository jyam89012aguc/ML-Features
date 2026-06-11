"""cash_burn_snapshot d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def f13_cbsp_151_fcf_ex_sbc_ttm_d3(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    return (_ttm(fcf) - _ttm(sbcomp)).diff().diff().diff()


def f13_cbsp_152_distance_to_4x_debt_ebitda_d3(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    debt_avg4 = _avg4(debt)
    ebitda_ttm = _ttm(ebitda)
    return (4.0 - _safe_div(debt_avg4, ebitda_ttm)).diff().diff().diff()


def f13_cbsp_153_months_of_opex_in_cash_d3(cashneq: pd.Series, opex: pd.Series) -> pd.Series:
    opex_ttm = _ttm(opex)
    monthly_opex = _safe_div(opex_ttm, 12.0)
    monthly_opex = monthly_opex.where(opex_ttm > 0, np.nan)
    return _safe_div(cashneq, monthly_opex).diff().diff().diff()


def f13_cbsp_154_fcf_to_marketcap_intensity_d3(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    fcf_ttm = _ttm(fcf)
    raw = _safe_div(fcf_ttm.abs(), marketcap)
    out = raw.where(fcf_ttm < 0, 0.0)
    out = out.where(~(fcf_ttm.isna() | marketcap.isna()), np.nan)
    return out.diff().diff().diff()


CASH_BURN_SNAPSHOT_D3_REGISTRY_151_225 = {
    "f13_cbsp_151_fcf_ex_sbc_ttm_d3": {"inputs": ["fcf", "sbcomp"], "func": f13_cbsp_151_fcf_ex_sbc_ttm_d3},
    "f13_cbsp_152_distance_to_4x_debt_ebitda_d3": {"inputs": ["debt", "ebitda"], "func": f13_cbsp_152_distance_to_4x_debt_ebitda_d3},
    "f13_cbsp_153_months_of_opex_in_cash_d3": {"inputs": ["cashneq", "opex"], "func": f13_cbsp_153_months_of_opex_in_cash_d3},
    "f13_cbsp_154_fcf_to_marketcap_intensity_d3": {"inputs": ["fcf", "marketcap"], "func": f13_cbsp_154_fcf_to_marketcap_intensity_d3},
}
