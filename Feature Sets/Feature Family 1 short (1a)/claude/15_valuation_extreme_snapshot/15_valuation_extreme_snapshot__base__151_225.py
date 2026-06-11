"""valuation_extreme_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for valuation-extreme detection.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: SF1/Daily fundamentals (ev, gp, marketcap, fcf, pe, ps, debt, equity, netinc).
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
Self-contained — no imports across families.
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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return _safe_div(s - m, sd)


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f15_vesp_151_ev_to_gross_profit(ev: pd.Series, gp: pd.Series) -> pd.Series:
    """EV / gross-profit_ttm — Novy-Marx quality multiple. High = expensive given gross profitability."""
    return _safe_div(ev, _ttm(gp))


def f15_vesp_152_marketcap_to_burn_rate(marketcap: pd.Series, fcf: pd.Series) -> pd.Series:
    """marketcap / |fcf_ttm| when fcf<0, else NaN — years priced into the cash burn."""
    fcf_ttm = _ttm(fcf)
    raw = _safe_div(marketcap, fcf_ttm.abs())
    return raw.where(fcf_ttm < 0, np.nan)


def f15_vesp_153_valuation_x_leverage_joint_z_252d(pe: pd.Series, ps: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """mean(z-score-20q(pe), z-score-20q(ps)) × (debt/equity) — joint expensive-and-levered score."""
    z_pe = _rolling_zscore(pe, QQTRS_5Y)
    z_ps = _rolling_zscore(ps, QQTRS_5Y)
    z_mean = (z_pe + z_ps) / 2.0
    leverage = _safe_div(debt, equity)
    return z_mean * leverage


def f15_vesp_154_quarters_with_negative_eps_x_log_marketcap_8q(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """sum(netinc<0 over 8q) × log(marketcap) — money-losing-but-large quality penalty."""
    neg = (netinc < 0).astype(float)
    neg = neg.where(~netinc.isna(), np.nan)
    n_neg_8q = neg.rolling(QQTRS_2Y, min_periods=max(QQTRS_2Y // 2, 4)).sum()
    return n_neg_8q * _safe_log(marketcap)


# ============================================================
#                    REGISTRY
# ============================================================

VALUATION_EXTREME_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f15_vesp_151_ev_to_gross_profit": {"inputs": ["ev", "gp"], "func": f15_vesp_151_ev_to_gross_profit},
    "f15_vesp_152_marketcap_to_burn_rate": {"inputs": ["marketcap", "fcf"], "func": f15_vesp_152_marketcap_to_burn_rate},
    "f15_vesp_153_valuation_x_leverage_joint_z_252d": {"inputs": ["pe", "ps", "debt", "equity"], "func": f15_vesp_153_valuation_x_leverage_joint_z_252d},
    "f15_vesp_154_quarters_with_negative_eps_x_log_marketcap_8q": {"inputs": ["netinc", "marketcap"], "func": f15_vesp_154_quarters_with_negative_eps_x_log_marketcap_8q},
}
