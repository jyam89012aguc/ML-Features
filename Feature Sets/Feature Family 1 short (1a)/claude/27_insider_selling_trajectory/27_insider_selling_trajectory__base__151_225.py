"""insider_selling_trajectory base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for insider-selling-pattern detection.
This file carries indices 151 (1 distinct hypothesis). Reserved range up to 225.

Inputs: pre-computed daily series of insider event latencies. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20

# Daily windows
QDAYS = 63


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


# ============================================================
#                    FEATURES 151
# ============================================================


def f27_istj_151_form4_filing_latency_mean_63d(insider_transaction_date: pd.Series, insider_filing_date: pd.Series) -> pd.Series:
    """Mean (filing_date − transaction_date) days over insider events in trailing 63d.

    Inputs are pd.Series of datetime64 values indexed by date (one row = one event date per row;
    NaT/NaN where no event). The latency per event = (filing_date − transaction_date).days.
    Returned series: mean latency over trailing 63d; NaN where no events in window.

    The harness may also pass these as numeric pd.Series where each row is already days-latency
    (pre-computed upstream). We handle either case: if the inputs are not datetimelike, treat
    insider_transaction_date as the latency series directly.
    """
    if insider_transaction_date is None or insider_filing_date is None or len(insider_transaction_date) == 0:
        return pd.Series(np.nan, index=getattr(insider_transaction_date, "index", None))

    if pd.api.types.is_datetime64_any_dtype(insider_transaction_date) and pd.api.types.is_datetime64_any_dtype(insider_filing_date):
        latency_td = insider_filing_date - insider_transaction_date
        latency_days = latency_td.dt.days.astype(float)
    else:
        # treat insider_transaction_date as the pre-computed days-latency series
        latency_days = pd.Series(insider_transaction_date).astype(float)

    return latency_days.rolling(QDAYS, min_periods=1).mean()


# ============================================================
#                    REGISTRY
# ============================================================

INSIDER_SELLING_TRAJECTORY_BASE_REGISTRY_151_225 = {
    "f27_istj_151_form4_filing_latency_mean_63d": {"inputs": ["insider_transaction_date", "insider_filing_date"], "func": f27_istj_151_form4_filing_latency_mean_63d},
}
