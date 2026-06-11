"""institutional_ownership_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for institutional-ownership detection at peak.
This file carries indices 151-154 (4 distinct hypotheses). Reserved range up to 225.

Inputs: SF3A-derived per-day Series (quarterly-aligned via ffill upstream):
  - inst_units_top5, inst_units_total
  - inst_top5_value, inst_value_total
  - inst_full_sellers_count, inst_value_prior_q, inst_value
  - ceo_sell_value, cfo_sell_value, top10_holder_qoq_change
NaN-stub policy: all-NaN inputs return pd.Series(np.nan, index=input.index).
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
QQTRS = 4


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


def _nan_series_like(*candidates):
    for c in candidates:
        if c is not None and hasattr(c, "index"):
            return pd.Series(np.nan, index=c.index)
    return pd.Series(dtype=float)


def _is_unusable(s):
    if s is None:
        return True
    if not isinstance(s, pd.Series):
        return True
    if len(s) == 0:
        return True
    if s.isna().all():
        return True
    return False


# ============================================================
#                    FEATURES 151-154
# ============================================================


def f20_iosp_151_position_size_hhi_proxy_q(inst_units_top5: pd.Series, inst_units_total: pd.Series) -> pd.Series:
    """HHI proxy (top5_units / total_units)^2 — concentration of basket in top holders."""
    if _is_unusable(inst_units_top5) or _is_unusable(inst_units_total):
        return _nan_series_like(inst_units_top5, inst_units_total)
    share = _safe_div(inst_units_top5, inst_units_total)
    return share ** 2


def f20_iosp_152_top5_holder_share_of_value(inst_top5_value: pd.Series, inst_value_total: pd.Series) -> pd.Series:
    """inst_top5_value / inst_value_total — pass-through; NaN-stub if either input is all-NaN."""
    if _is_unusable(inst_top5_value) or _is_unusable(inst_value_total):
        return _nan_series_like(inst_top5_value, inst_value_total)
    return _safe_div(inst_top5_value, inst_value_total)


def f20_iosp_153_single_fund_full_exit_event_q(inst_full_sellers_count: pd.Series, inst_value_prior_q: pd.Series, inst_value: pd.Series) -> pd.Series:
    """+1 if inst_full_sellers_count > 0 AND (prior_q_value - value) / prior_q_value > 0.05 (>5% basket lost)."""
    if _is_unusable(inst_full_sellers_count) or _is_unusable(inst_value_prior_q) or _is_unusable(inst_value):
        return _nan_series_like(inst_full_sellers_count, inst_value_prior_q, inst_value)
    cost = _safe_div(inst_value_prior_q - inst_value, inst_value_prior_q)
    return ((inst_full_sellers_count > 0) & (cost > 0.05)).astype(float)


def f20_iosp_154_smart_money_joint_exit_composite_8q(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, top10_holder_qoq_change: pd.Series) -> pd.Series:
    """Sum of 8q rolling counts: (ceo>0) + (cfo>0) + (top10_qoq<0) — joint exit breadth."""
    if _is_unusable(ceo_sell_value) or _is_unusable(cfo_sell_value) or _is_unusable(top10_holder_qoq_change):
        return _nan_series_like(ceo_sell_value, cfo_sell_value, top10_holder_qoq_change)
    win = 8 * QDAYS
    mp = max(win // 3, 2)
    a = (ceo_sell_value > 0).astype(float).rolling(win, min_periods=mp).sum()
    b = (cfo_sell_value > 0).astype(float).rolling(win, min_periods=mp).sum()
    c = (top10_holder_qoq_change < 0).astype(float).rolling(win, min_periods=mp).sum()
    return a + b + c


# ============================================================
#                    REGISTRY
# ============================================================

INSTITUTIONAL_OWNERSHIP_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f20_iosp_151_position_size_hhi_proxy_q": {"inputs": ["inst_units_top5", "inst_units_total"], "func": f20_iosp_151_position_size_hhi_proxy_q},
    "f20_iosp_152_top5_holder_share_of_value": {"inputs": ["inst_top5_value", "inst_value_total"], "func": f20_iosp_152_top5_holder_share_of_value},
    "f20_iosp_153_single_fund_full_exit_event_q": {"inputs": ["inst_full_sellers_count", "inst_value_prior_q", "inst_value"], "func": f20_iosp_153_single_fund_full_exit_event_q},
    "f20_iosp_154_smart_money_joint_exit_composite_8q": {"inputs": ["ceo_sell_value", "cfo_sell_value", "top10_holder_qoq_change"], "func": f20_iosp_154_smart_money_joint_exit_composite_8q},
}
