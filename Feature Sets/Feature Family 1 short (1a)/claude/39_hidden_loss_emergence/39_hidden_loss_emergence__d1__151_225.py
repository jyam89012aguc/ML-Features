"""hidden_loss_emergence d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def f39_hlem_151_warranty_environmental_reserve_emergence_d1(accruedliab: pd.Series, revenue: pd.Series) -> pd.Series:
    ratio = _safe_div(accruedliab, revenue)
    avg_ratio = ratio.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 3, 2)).mean()
    expected = avg_ratio * revenue
    return (accruedliab - expected).diff()


def f39_hlem_152_kitchen_sink_quarter_detector_d1(opinc: pd.Series, intangibles: pd.Series, accruedliab: pd.Series, depamor: pd.Series, sgna: pd.Series) -> pd.Series:
    metrics = [opinc, intangibles, accruedliab, depamor, sgna]
    flag_sum = pd.Series(0.0, index=opinc.index)
    any_valid = pd.Series(False, index=opinc.index)
    for m in metrics:
        qoq = m.diff()
        z = _rolling_zscore(qoq, QQTRS_2Y)
        flag = (z.abs() > 2.0).astype(float)
        valid = z.notna()
        flag_sum = flag_sum + flag.where(valid, 0.0)
        any_valid = any_valid | valid
    return flag_sum.where(any_valid, np.nan).diff()


def f39_hlem_153_dta_valuation_allowance_proxy_d1(taxliabilities: pd.Series, netinc: pd.Series) -> pd.Series:
    yoy_tax = taxliabilities - taxliabilities.shift(QQTRS)
    yoy_ni = netinc - netinc.shift(QQTRS)
    return (yoy_tax - 0.25 * yoy_ni).diff()


HIDDEN_LOSS_EMERGENCE_D1_REGISTRY_151_225 = {
    "f39_hlem_151_warranty_environmental_reserve_emergence_d1": {"inputs": ["accruedliab", "revenue"], "func": f39_hlem_151_warranty_environmental_reserve_emergence_d1},
    "f39_hlem_152_kitchen_sink_quarter_detector_d1": {"inputs": ["opinc", "intangibles", "accruedliab", "depamor", "sgna"], "func": f39_hlem_152_kitchen_sink_quarter_detector_d1},
    "f39_hlem_153_dta_valuation_allowance_proxy_d1": {"inputs": ["taxliabilities", "netinc"], "func": f39_hlem_153_dta_valuation_allowance_proxy_d1},
}
