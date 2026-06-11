"""passive_flow_acceleration d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


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


def f33_pfac_151_etf_active_share_crossover_event_q_d2(etf_share: pd.Series, inst_share: pd.Series) -> pd.Series:
    if etf_share is None or inst_share is None:
        return pd.Series(np.nan)
    curr = etf_share >= inst_share
    prev = etf_share.shift(1) < inst_share.shift(1)
    out = (curr & prev).astype(float)
    valid = etf_share.notna() & inst_share.notna() & etf_share.shift(1).notna() & inst_share.shift(1).notna()
    return out.where(valid, np.nan).diff().diff()


def f33_pfac_152_index_membership_event_q_d2(index_event: pd.Series) -> pd.Series:
    if index_event is None:
        return pd.Series(np.nan)
    try:
        return index_event.astype(float).diff().diff()
    except Exception:
        return pd.Series(np.nan, index=index_event.index if hasattr(index_event, "index") else None)


def f33_pfac_153_inst_count_value_divergence_q_d2(inst_count: pd.Series, inst_value: pd.Series) -> pd.Series:
    if inst_count is None or inst_value is None:
        return pd.Series(np.nan)
    count_qoq = inst_count.diff()
    value_qoq = inst_value.diff()
    count_z = _rolling_zscore(count_qoq, QQTRS_2Y, min_periods=4)
    value_z = _rolling_zscore(value_qoq, QQTRS_2Y, min_periods=4)
    cond = (count_z < -2.0) & (value_z > -0.5)
    out = cond.astype(float)
    return out.where(count_z.notna() & value_z.notna(), np.nan).diff().diff()


def f33_pfac_154_filing_staleness_quarter_q_d2(days_since_filing: pd.Series) -> pd.Series:
    if days_since_filing is None:
        return pd.Series(np.nan)
    return (days_since_filing / 90.0).diff().diff()


PASSIVE_FLOW_ACCELERATION_D2_REGISTRY_151_225 = {
    "f33_pfac_151_etf_active_share_crossover_event_q_d2": {"inputs": ["etf_share", "inst_share"], "func": f33_pfac_151_etf_active_share_crossover_event_q_d2},
    "f33_pfac_152_index_membership_event_q_d2": {"inputs": ["index_event"], "func": f33_pfac_152_index_membership_event_q_d2},
    "f33_pfac_153_inst_count_value_divergence_q_d2": {"inputs": ["inst_count", "inst_value"], "func": f33_pfac_153_inst_count_value_divergence_q_d2},
    "f33_pfac_154_filing_staleness_quarter_q_d2": {"inputs": ["days_since_filing"], "func": f33_pfac_154_filing_staleness_quarter_q_d2},
}
