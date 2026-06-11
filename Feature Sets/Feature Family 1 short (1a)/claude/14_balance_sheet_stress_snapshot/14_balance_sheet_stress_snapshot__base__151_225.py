"""balance_sheet_stress_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for balance-sheet distress detection.
This file carries indices 151-157 (7 distinct hypotheses: Springate, Zmijewski, Taffler, Fulmer H,
NOA/A, tangible-equity/debt, capex<dep streak). Reserved range up to 225.

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


# ============================================================
#                    FEATURES 151-157
# ============================================================


def f14_bsss_151_springate_score(workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series, revenue: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Springate distress score: 1.03*(wc/a)+3.07*(ebit/a)+0.66*(ebit/cl_proxy)+0.4*(rev/a). cl_proxy=liabilities."""
    a = 1.03 * _safe_div(workingcapital, assets)
    b = 3.07 * _safe_div(ebit, assets)
    c = 0.66 * _safe_div(ebit, liabilities)
    d = 0.4 * _safe_div(revenue, assets)
    return a + b + c + d


def f14_bsss_152_zmijewski_score(netinc: pd.Series, assets: pd.Series, liabilities: pd.Series, currentassets: pd.Series, currentliab: pd.Series) -> pd.Series:
    """Zmijewski X-score: -4.336 -4.513*(ni/a) +5.679*(l/a) +0.004*(ca/cl)."""
    a = -4.513 * _safe_div(netinc, assets)
    b = 5.679 * _safe_div(liabilities, assets)
    c = 0.004 * _safe_div(currentassets, currentliab)
    return -4.336 + a + b + c


def f14_bsss_153_taffler_score(opinc: pd.Series, currentliab: pd.Series, currentassets: pd.Series, liabilities: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Taffler Z-score: 0.53*(opinc/cl)+0.13*(ca/l)+0.18*(cl/a)+0.16*(rev/a)."""
    a = 0.53 * _safe_div(opinc, currentliab)
    b = 0.13 * _safe_div(currentassets, liabilities)
    c = 0.18 * _safe_div(currentliab, assets)
    d = 0.16 * _safe_div(revenue, assets)
    return a + b + c + d


def f14_bsss_154_fulmer_h_score(retearn: pd.Series, assets: pd.Series, revenue: pd.Series, opinc: pd.Series, liabilities: pd.Series, equity: pd.Series, cashneq: pd.Series, currentliab: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fulmer H-score (simplified per spec). Distress when H<0."""
    t1 = 5.528 * _safe_div(retearn, assets)
    t2 = 0.212 * _safe_div(revenue, assets)
    t3 = 0.073 * _safe_div(ebit, equity)
    t4 = 1.270 * _safe_div(cashneq, currentliab)
    t5 = -0.120 * _safe_div(liabilities, equity)
    t6 = 2.335 * _safe_div(currentliab, assets)
    t7 = 0.575 * _safe_log(assets)
    # working-capital term per spec skipped (cl proxy term skip)
    t8 = 0.0
    t9 = 0.894 * _safe_div(ebit, intexp)
    return t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9


def f14_bsss_155_net_operating_assets_to_assets(workingcapital: pd.Series, ppnenet: pd.Series, intangibles: pd.Series, debt: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    """NOA / assets, where NOA ≈ workingcapital + ppnenet + intangibles − debt + cashneq."""
    noa = workingcapital + ppnenet + intangibles - debt + cashneq
    return _safe_div(noa, assets)


def f14_bsss_156_tangible_equity_to_debt(equity: pd.Series, intangibles: pd.Series, debt: pd.Series) -> pd.Series:
    """(equity − intangibles) / debt — tangible cushion vs leverage."""
    return _safe_div(equity - intangibles, debt)


def f14_bsss_157_capex_to_depamor_below_1_streak_8q(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Count of last 8q where |capex| < |depamor| — under-investment streak."""
    indicator = (capex.abs() < depamor.abs()).astype(float)
    # propagate NaN where either input is NaN
    mask_nan = capex.isna() | depamor.isna()
    indicator = indicator.where(~mask_nan, np.nan)
    return indicator.rolling(QQTRS_2Y, min_periods=max(QQTRS_2Y // 2, 4)).sum()


# ============================================================
#                    REGISTRY
# ============================================================

BALANCE_SHEET_STRESS_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f14_bsss_151_springate_score": {"inputs": ["workingcapital", "assets", "ebit", "revenue", "liabilities"], "func": f14_bsss_151_springate_score},
    "f14_bsss_152_zmijewski_score": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliab"], "func": f14_bsss_152_zmijewski_score},
    "f14_bsss_153_taffler_score": {"inputs": ["opinc", "currentliab", "currentassets", "liabilities", "revenue", "assets"], "func": f14_bsss_153_taffler_score},
    "f14_bsss_154_fulmer_h_score": {"inputs": ["retearn", "assets", "revenue", "opinc", "liabilities", "equity", "cashneq", "currentliab", "ebit", "intexp"], "func": f14_bsss_154_fulmer_h_score},
    "f14_bsss_155_net_operating_assets_to_assets": {"inputs": ["workingcapital", "ppnenet", "intangibles", "debt", "cashneq", "assets"], "func": f14_bsss_155_net_operating_assets_to_assets},
    "f14_bsss_156_tangible_equity_to_debt": {"inputs": ["equity", "intangibles", "debt"], "func": f14_bsss_156_tangible_equity_to_debt},
    "f14_bsss_157_capex_to_depamor_below_1_streak_8q": {"inputs": ["capex", "depamor"], "func": f14_bsss_157_capex_to_depamor_below_1_streak_8q},
}
