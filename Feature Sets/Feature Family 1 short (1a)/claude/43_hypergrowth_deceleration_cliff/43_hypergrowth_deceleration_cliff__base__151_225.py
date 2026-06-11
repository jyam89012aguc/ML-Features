"""hypergrowth_deceleration_cliff base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for backlog depletion / acquisition-driven decel.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly fundamentals only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _yoy_pct(s, periods=QQTRS):
    return _safe_div(s - s.shift(periods), s.shift(periods))


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f43_hdcl_151_backlog_rpo_depletion_rate(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """yoy_pct(deferredrev) - yoy_pct(revenue). Negative = depletion outpacing revenue (forward growth depleting)."""
    return _yoy_pct(deferredrev) - _yoy_pct(revenue)


def f43_hdcl_152_acquisition_growth_deceleration_proxy(intangibles: pd.Series, revenue: pd.Series) -> pd.Series:
    """yoy_pct(intangibles) - yoy_pct(revenue). Widening gap = M&A-fueled-growth tapering."""
    return _yoy_pct(intangibles) - _yoy_pct(revenue)


def f43_hdcl_153_pricing_component_decay_during_decel(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """When revenue yoy < 0.05: compute (revenue/cor) yoy. Negative = pricing power lost simultaneously with decel."""
    rev_yoy = _yoy_pct(revenue)
    price_proxy = _safe_div(revenue, cor)
    price_yoy = _yoy_pct(price_proxy)
    return price_yoy.where(rev_yoy < 0.05, np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

HYPERGROWTH_DECELERATION_CLIFF_BASE_REGISTRY_151_225 = {
    "f43_hdcl_151_backlog_rpo_depletion_rate": {"inputs": ["deferredrev", "revenue"], "func": f43_hdcl_151_backlog_rpo_depletion_rate},
    "f43_hdcl_152_acquisition_growth_deceleration_proxy": {"inputs": ["intangibles", "revenue"], "func": f43_hdcl_152_acquisition_growth_deceleration_proxy},
    "f43_hdcl_153_pricing_component_decay_during_decel": {"inputs": ["revenue", "cor"], "func": f43_hdcl_153_pricing_component_decay_during_decel},
}
