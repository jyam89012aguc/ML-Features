"""short_interest_buildup_trajectory d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
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


def f25_sibt_151_si_build_during_revenue_decel_indicator_d2(shortinterest: pd.Series, revenue: pd.Series) -> pd.Series:
    si_logdiff_63 = _safe_log(shortinterest).diff(QDAYS)
    rev_yoy = revenue.pct_change(YDAYS)
    return ((si_logdiff_63 > 0.3) & (rev_yoy < -0.05)).astype(float).diff().diff()


def f25_sibt_152_si_build_during_insider_selling_indicator_d2(shortinterest: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    si_logdiff_63 = _safe_log(shortinterest).diff(QDAYS)
    sell_63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    m = sell_63.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = sell_63.rolling(YDAYS, min_periods=QDAYS).std()
    thresh = m + 2.0 * sd
    return ((si_logdiff_63 > 0) & (sell_63 > thresh)).astype(float).diff().diff()


def f25_sibt_153_dtc_above_10_persistence_63d_d2(daystocover: pd.Series) -> pd.Series:
    return daystocover.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float((w > 10).mean()), raw=True).diff().diff()


SHORT_INTEREST_BUILDUP_TRAJECTORY_D2_REGISTRY_151_225 = {
    "f25_sibt_151_si_build_during_revenue_decel_indicator_d2": {"inputs": ["shortinterest", "revenue"], "func": f25_sibt_151_si_build_during_revenue_decel_indicator_d2},
    "f25_sibt_152_si_build_during_insider_selling_indicator_d2": {"inputs": ["shortinterest", "insider_sell_value"], "func": f25_sibt_152_si_build_during_insider_selling_indicator_d2},
    "f25_sibt_153_dtc_above_10_persistence_63d_d2": {"inputs": ["daystocover"], "func": f25_sibt_153_dtc_above_10_persistence_63d_d2},
}
