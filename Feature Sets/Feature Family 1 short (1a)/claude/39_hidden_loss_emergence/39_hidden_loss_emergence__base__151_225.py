"""hidden_loss_emergence base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for hidden-loss emergence:
warranty/environmental reserve build, kitchen-sink quarter detection, and DTA-valuation-allowance proxy.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
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


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f39_hlem_151_warranty_environmental_reserve_emergence(accruedliab: pd.Series, revenue: pd.Series) -> pd.Series:
    """Residual of accruedliab vs revenue-scaled expected reserve over 12q — large positive = reserve buildup unconnected to revenue scaling."""
    ratio = _safe_div(accruedliab, revenue)
    avg_ratio = ratio.rolling(QQTRS_3Y, min_periods=max(QQTRS_3Y // 3, 2)).mean()
    expected = avg_ratio * revenue
    return accruedliab - expected


def f39_hlem_152_kitchen_sink_quarter_detector(opinc: pd.Series, intangibles: pd.Series, accruedliab: pd.Series, depamor: pd.Series, sgna: pd.Series) -> pd.Series:
    """Count of metrics out of [opinc, intangibles, accruedliab, depamor, sgna] with |qoq-change z 8q| > 2 in same quarter — 0-5."""
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
    return flag_sum.where(any_valid, np.nan)


def f39_hlem_153_dta_valuation_allowance_proxy(taxliabilities: pd.Series, netinc: pd.Series) -> pd.Series:
    """yoy(taxliabilities) − 0.25 × yoy(netinc). Large negative = DTA write-down proxy."""
    yoy_tax = taxliabilities - taxliabilities.shift(QQTRS)
    yoy_ni = netinc - netinc.shift(QQTRS)
    return yoy_tax - 0.25 * yoy_ni


# ============================================================
#                    REGISTRY
# ============================================================

HIDDEN_LOSS_EMERGENCE_BASE_REGISTRY_151_225 = {
    "f39_hlem_151_warranty_environmental_reserve_emergence": {"inputs": ["accruedliab", "revenue"], "func": f39_hlem_151_warranty_environmental_reserve_emergence},
    "f39_hlem_152_kitchen_sink_quarter_detector": {"inputs": ["opinc", "intangibles", "accruedliab", "depamor", "sgna"], "func": f39_hlem_152_kitchen_sink_quarter_detector},
    "f39_hlem_153_dta_valuation_allowance_proxy": {"inputs": ["taxliabilities", "netinc"], "func": f39_hlem_153_dta_valuation_allowance_proxy},
}
