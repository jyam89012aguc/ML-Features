"""short_interest_buildup_trajectory base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for short-interest buildup trajectory detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: NSIR (shortinterest, daystocover), SF1 (revenue — quarterly, ffill to daily upstream),
SF2-derived (insider_sell_value). PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f25_sibt_151_si_build_during_revenue_decel_indicator(shortinterest: pd.Series, revenue: pd.Series) -> pd.Series:
    """+1 if log(SI) 63d log-diff > 0.3 AND revenue yoy < -0.05 (revenue is quarterly, ffill aligned)."""
    si_logdiff_63 = _safe_log(shortinterest).diff(QDAYS)
    rev_yoy = revenue.pct_change(YDAYS)
    return ((si_logdiff_63 > 0.3) & (rev_yoy < -0.05)).astype(float)


def f25_sibt_152_si_build_during_insider_selling_indicator(shortinterest: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """+1 if SI 63d log-diff > 0 AND insider_sell_value 63d sum > (252d rolling mean + 2*std)."""
    si_logdiff_63 = _safe_log(shortinterest).diff(QDAYS)
    sell_63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    m = sell_63.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = sell_63.rolling(YDAYS, min_periods=QDAYS).std()
    thresh = m + 2.0 * sd
    return ((si_logdiff_63 > 0) & (sell_63 > thresh)).astype(float)


def f25_sibt_153_dtc_above_10_persistence_63d(daystocover: pd.Series) -> pd.Series:
    """Fraction of last 63d with daystocover > 10."""
    return daystocover.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float((w > 10).mean()), raw=True)


# ============================================================
#                    REGISTRY
# ============================================================

SHORT_INTEREST_BUILDUP_TRAJECTORY_BASE_REGISTRY_151_225 = {
    "f25_sibt_151_si_build_during_revenue_decel_indicator": {"inputs": ["shortinterest", "revenue"], "func": f25_sibt_151_si_build_during_revenue_decel_indicator},
    "f25_sibt_152_si_build_during_insider_selling_indicator": {"inputs": ["shortinterest", "insider_sell_value"], "func": f25_sibt_152_si_build_during_insider_selling_indicator},
    "f25_sibt_153_dtc_above_10_persistence_63d": {"inputs": ["daystocover"], "func": f25_sibt_153_dtc_above_10_persistence_63d},
}
