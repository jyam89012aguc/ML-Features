"""fraud_emergence_signal d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20
YDAYS = 252


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


def _as_float_event(s: pd.Series) -> pd.Series:
    if s.dtype == bool:
        return s.astype(float)
    return s.astype(float)


def f47_frem_151_nt_filing_count_252d_d3(nt_filing_event: pd.Series) -> pd.Series:
    ev = _as_float_event(nt_filing_event).fillna(0.0)
    return ev.rolling(YDAYS, min_periods=max(YDAYS // 4, 5)).sum().diff().diff().diff()


def f47_frem_152_going_concern_flag_d3(going_concern_event: pd.Series) -> pd.Series:
    ev = _as_float_event(going_concern_event).fillna(0.0)
    return ev.rolling(QQTRS, min_periods=1).max().diff().diff().diff()


def f47_frem_153_item_4_02_non_reliance_count_252d_d3(non_reliance_event: pd.Series) -> pd.Series:
    ev = _as_float_event(non_reliance_event).fillna(0.0)
    return ev.rolling(YDAYS, min_periods=max(YDAYS // 4, 5)).sum().diff().diff().diff()


def f47_frem_154_internal_controls_material_weakness_flag_d3(mw_event: pd.Series) -> pd.Series:
    ev = _as_float_event(mw_event).fillna(0.0)
    return ev.rolling(QQTRS, min_periods=1).max().diff().diff().diff()


FRAUD_EMERGENCE_SIGNAL_D3_REGISTRY_151_225 = {
    "f47_frem_151_nt_filing_count_252d_d3": {"inputs": ["nt_filing_event"], "func": f47_frem_151_nt_filing_count_252d_d3},
    "f47_frem_152_going_concern_flag_d3": {"inputs": ["going_concern_event"], "func": f47_frem_152_going_concern_flag_d3},
    "f47_frem_153_item_4_02_non_reliance_count_252d_d3": {"inputs": ["non_reliance_event"], "func": f47_frem_153_item_4_02_non_reliance_count_252d_d3},
    "f47_frem_154_internal_controls_material_weakness_flag_d3": {"inputs": ["mw_event"], "func": f47_frem_154_internal_controls_material_weakness_flag_d3},
}
