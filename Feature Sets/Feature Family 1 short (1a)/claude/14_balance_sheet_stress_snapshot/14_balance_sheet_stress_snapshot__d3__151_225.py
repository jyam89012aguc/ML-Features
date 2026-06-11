"""balance_sheet_stress_snapshot d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def f14_bsss_151_springate_score_d3(workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series, revenue: pd.Series, liabilities: pd.Series) -> pd.Series:
    a = 1.03 * _safe_div(workingcapital, assets)
    b = 3.07 * _safe_div(ebit, assets)
    c = 0.66 * _safe_div(ebit, liabilities)
    d = 0.4 * _safe_div(revenue, assets)
    return (a + b + c + d).diff().diff().diff()


def f14_bsss_152_zmijewski_score_d3(netinc: pd.Series, assets: pd.Series, liabilities: pd.Series, currentassets: pd.Series, currentliab: pd.Series) -> pd.Series:
    a = -4.513 * _safe_div(netinc, assets)
    b = 5.679 * _safe_div(liabilities, assets)
    c = 0.004 * _safe_div(currentassets, currentliab)
    return (-4.336 + a + b + c).diff().diff().diff()


def f14_bsss_153_taffler_score_d3(opinc: pd.Series, currentliab: pd.Series, currentassets: pd.Series, liabilities: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    a = 0.53 * _safe_div(opinc, currentliab)
    b = 0.13 * _safe_div(currentassets, liabilities)
    c = 0.18 * _safe_div(currentliab, assets)
    d = 0.16 * _safe_div(revenue, assets)
    return (a + b + c + d).diff().diff().diff()


def f14_bsss_154_fulmer_h_score_d3(retearn: pd.Series, assets: pd.Series, revenue: pd.Series, opinc: pd.Series, liabilities: pd.Series, equity: pd.Series, cashneq: pd.Series, currentliab: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    t1 = 5.528 * _safe_div(retearn, assets)
    t2 = 0.212 * _safe_div(revenue, assets)
    t3 = 0.073 * _safe_div(ebit, equity)
    t4 = 1.270 * _safe_div(cashneq, currentliab)
    t5 = -0.120 * _safe_div(liabilities, equity)
    t6 = 2.335 * _safe_div(currentliab, assets)
    t7 = 0.575 * _safe_log(assets)
    t8 = 0.0
    t9 = 0.894 * _safe_div(ebit, intexp)
    return (t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9).diff().diff().diff()


def f14_bsss_155_net_operating_assets_to_assets_d3(workingcapital: pd.Series, ppnenet: pd.Series, intangibles: pd.Series, debt: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    noa = workingcapital + ppnenet + intangibles - debt + cashneq
    return _safe_div(noa, assets).diff().diff().diff()


def f14_bsss_156_tangible_equity_to_debt_d3(equity: pd.Series, intangibles: pd.Series, debt: pd.Series) -> pd.Series:
    return _safe_div(equity - intangibles, debt).diff().diff().diff()


def f14_bsss_157_capex_to_depamor_below_1_streak_8q_d3(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    indicator = (capex.abs() < depamor.abs()).astype(float)
    mask_nan = capex.isna() | depamor.isna()
    indicator = indicator.where(~mask_nan, np.nan)
    return indicator.rolling(QQTRS_2Y, min_periods=max(QQTRS_2Y // 2, 4)).sum().diff().diff().diff()


BALANCE_SHEET_STRESS_SNAPSHOT_D3_REGISTRY_151_225 = {
    "f14_bsss_151_springate_score_d3": {"inputs": ["workingcapital", "assets", "ebit", "revenue", "liabilities"], "func": f14_bsss_151_springate_score_d3},
    "f14_bsss_152_zmijewski_score_d3": {"inputs": ["netinc", "assets", "liabilities", "currentassets", "currentliab"], "func": f14_bsss_152_zmijewski_score_d3},
    "f14_bsss_153_taffler_score_d3": {"inputs": ["opinc", "currentliab", "currentassets", "liabilities", "revenue", "assets"], "func": f14_bsss_153_taffler_score_d3},
    "f14_bsss_154_fulmer_h_score_d3": {"inputs": ["retearn", "assets", "revenue", "opinc", "liabilities", "equity", "cashneq", "currentliab", "ebit", "intexp"], "func": f14_bsss_154_fulmer_h_score_d3},
    "f14_bsss_155_net_operating_assets_to_assets_d3": {"inputs": ["workingcapital", "ppnenet", "intangibles", "debt", "cashneq", "assets"], "func": f14_bsss_155_net_operating_assets_to_assets_d3},
    "f14_bsss_156_tangible_equity_to_debt_d3": {"inputs": ["equity", "intangibles", "debt"], "func": f14_bsss_156_tangible_equity_to_debt_d3},
    "f14_bsss_157_capex_to_depamor_below_1_streak_8q_d3": {"inputs": ["capex", "depamor"], "func": f14_bsss_157_capex_to_depamor_below_1_streak_8q_d3},
}
