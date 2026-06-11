"""hypergrowth_deceleration_cliff d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def f43_hdcl_151_backlog_rpo_depletion_rate_d1(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_yoy_pct(deferredrev) - _yoy_pct(revenue)).diff()


def f43_hdcl_152_acquisition_growth_deceleration_proxy_d1(intangibles: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_yoy_pct(intangibles) - _yoy_pct(revenue)).diff()


def f43_hdcl_153_pricing_component_decay_during_decel_d1(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    rev_yoy = _yoy_pct(revenue)
    price_proxy = _safe_div(revenue, cor)
    price_yoy = _yoy_pct(price_proxy)
    return price_yoy.where(rev_yoy < 0.05, np.nan).diff()


HYPERGROWTH_DECELERATION_CLIFF_D1_REGISTRY_151_225 = {
    "f43_hdcl_151_backlog_rpo_depletion_rate_d1": {"inputs": ["deferredrev", "revenue"], "func": f43_hdcl_151_backlog_rpo_depletion_rate_d1},
    "f43_hdcl_152_acquisition_growth_deceleration_proxy_d1": {"inputs": ["intangibles", "revenue"], "func": f43_hdcl_152_acquisition_growth_deceleration_proxy_d1},
    "f43_hdcl_153_pricing_component_decay_during_decel_d1": {"inputs": ["revenue", "cor"], "func": f43_hdcl_153_pricing_component_decay_during_decel_d1},
}
