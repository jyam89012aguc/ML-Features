"""insider_activity_snapshot base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for insider-activity detection at peak.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: SF2-derived per-day series (insider_sell_count_daily, insider_sell_value, planned_sell_value)
plus SEP (high, close). PIT-clean: right-anchored rolling, explicit min_periods, no centered windows,
no .shift(-N). Self-contained — no imports across families.
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


def f18_iasp_151_cluster_sell_within_5d_count_63d(insider_sell_count_daily: pd.Series) -> pd.Series:
    """Count of 5d windows in last 63d where unique-seller-count >=3 (cluster events)."""
    rolling5 = insider_sell_count_daily.rolling(WDAYS, min_periods=1).sum()
    cluster_day = (rolling5 >= 3).astype(float)
    return cluster_day.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_152_insider_sell_at_52w_high_dollar_63d(insider_sell_value: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of insider_sell_value on days where close >= 0.95 * 252d high, over last 63d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = (close >= 0.95 * rmax)
    masked = insider_sell_value.where(near_high, 0.0)
    return masked.rolling(QDAYS, min_periods=MDAYS).sum()


def f18_iasp_153_planned_sale_within_90d_of_plan_proxy(insider_sell_value: pd.Series, planned_sell_value: pd.Series) -> pd.Series:
    """planned_sell_value / total_sell_value (63d sums) where planned_sell_value > 0 in window."""
    plan_63 = planned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    tot_63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    ratio = _safe_div(plan_63, tot_63)
    return ratio.where(plan_63 > 0, np.nan)


# ============================================================
#                    REGISTRY
# ============================================================

INSIDER_ACTIVITY_SNAPSHOT_BASE_REGISTRY_151_225 = {
    "f18_iasp_151_cluster_sell_within_5d_count_63d": {"inputs": ["insider_sell_count_daily"], "func": f18_iasp_151_cluster_sell_within_5d_count_63d},
    "f18_iasp_152_insider_sell_at_52w_high_dollar_63d": {"inputs": ["insider_sell_value", "high", "close"], "func": f18_iasp_152_insider_sell_at_52w_high_dollar_63d},
    "f18_iasp_153_planned_sale_within_90d_of_plan_proxy": {"inputs": ["insider_sell_value", "planned_sell_value"], "func": f18_iasp_153_planned_sale_within_90d_of_plan_proxy},
}
