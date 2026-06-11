"""fraud_emergence_signal base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for SEC-event-driven fraud emergence detection.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: boolean / 0-1 event flag pd.Series sourced from the upstream EVENTS table. PIT-clean:
right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
Self-contained — no imports across families.
"""
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
    """Coerce a boolean/0-1 event series to float, leaving NaN where missing."""
    if s.dtype == bool:
        return s.astype(float)
    # treat non-NaN nonzero as 1, zero as 0, NaN stays NaN
    return s.astype(float)


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f47_frem_151_nt_filing_count_252d(nt_filing_event: pd.Series) -> pd.Series:
    """Sum of NT 10-K/Q event flags over trailing 252d window."""
    ev = _as_float_event(nt_filing_event).fillna(0.0)
    return ev.rolling(YDAYS, min_periods=max(YDAYS // 4, 5)).sum()


def f47_frem_152_going_concern_flag(going_concern_event: pd.Series) -> pd.Series:
    """Trailing 4q maximum of the going-concern audit-opinion event flag (quarterly index)."""
    ev = _as_float_event(going_concern_event).fillna(0.0)
    return ev.rolling(QQTRS, min_periods=1).max()


def f47_frem_153_item_4_02_non_reliance_count_252d(non_reliance_event: pd.Series) -> pd.Series:
    """Sum of 8-K Item 4.02 non-reliance event flags over trailing 252d window."""
    ev = _as_float_event(non_reliance_event).fillna(0.0)
    return ev.rolling(YDAYS, min_periods=max(YDAYS // 4, 5)).sum()


def f47_frem_154_internal_controls_material_weakness_flag(mw_event: pd.Series) -> pd.Series:
    """Trailing 4q maximum of the internal-controls material-weakness disclosure flag."""
    ev = _as_float_event(mw_event).fillna(0.0)
    return ev.rolling(QQTRS, min_periods=1).max()


# ============================================================
#                    REGISTRY
# ============================================================

FRAUD_EMERGENCE_SIGNAL_BASE_REGISTRY_151_225 = {
    "f47_frem_151_nt_filing_count_252d": {"inputs": ["nt_filing_event"], "func": f47_frem_151_nt_filing_count_252d},
    "f47_frem_152_going_concern_flag": {"inputs": ["going_concern_event"], "func": f47_frem_152_going_concern_flag},
    "f47_frem_153_item_4_02_non_reliance_count_252d": {"inputs": ["non_reliance_event"], "func": f47_frem_153_item_4_02_non_reliance_count_252d},
    "f47_frem_154_internal_controls_material_weakness_flag": {"inputs": ["mw_event"], "func": f47_frem_154_internal_controls_material_weakness_flag},
}
