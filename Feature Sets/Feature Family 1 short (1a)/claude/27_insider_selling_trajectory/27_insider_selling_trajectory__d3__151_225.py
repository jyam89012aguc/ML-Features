"""insider_selling_trajectory d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20
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


def f27_istj_151_form4_filing_latency_mean_63d_d3(insider_transaction_date: pd.Series, insider_filing_date: pd.Series) -> pd.Series:
    if insider_transaction_date is None or insider_filing_date is None or len(insider_transaction_date) == 0:
        return pd.Series(np.nan, index=getattr(insider_transaction_date, "index", None))
    if pd.api.types.is_datetime64_any_dtype(insider_transaction_date) and pd.api.types.is_datetime64_any_dtype(insider_filing_date):
        latency_td = insider_filing_date - insider_transaction_date
        latency_days = latency_td.dt.days.astype(float)
    else:
        latency_days = pd.Series(insider_transaction_date).astype(float)
    return latency_days.rolling(QDAYS, min_periods=1).mean().diff().diff().diff()


INSIDER_SELLING_TRAJECTORY_D3_REGISTRY_151_225 = {
    "f27_istj_151_form4_filing_latency_mean_63d_d3": {"inputs": ["insider_transaction_date", "insider_filing_date"], "func": f27_istj_151_form4_filing_latency_mean_63d_d3},
}
