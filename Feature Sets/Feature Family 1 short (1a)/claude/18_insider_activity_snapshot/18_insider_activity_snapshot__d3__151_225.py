"""insider_activity_snapshot d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
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


def f18_iasp_151_cluster_sell_within_5d_count_63d_d3(insider_sell_count_daily: pd.Series) -> pd.Series:
    rolling5 = insider_sell_count_daily.rolling(WDAYS, min_periods=1).sum()
    cluster_day = (rolling5 >= 3).astype(float)
    return cluster_day.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()


def f18_iasp_152_insider_sell_at_52w_high_dollar_63d_d3(insider_sell_value: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = (close >= 0.95 * rmax)
    masked = insider_sell_value.where(near_high, 0.0)
    return masked.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()


def f18_iasp_153_planned_sale_within_90d_of_plan_proxy_d3(insider_sell_value: pd.Series, planned_sell_value: pd.Series) -> pd.Series:
    plan_63 = planned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    tot_63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    ratio = _safe_div(plan_63, tot_63)
    return ratio.where(plan_63 > 0, np.nan).diff().diff().diff()


INSIDER_ACTIVITY_SNAPSHOT_D3_REGISTRY_151_225 = {
    "f18_iasp_151_cluster_sell_within_5d_count_63d_d3": {"inputs": ["insider_sell_count_daily"], "func": f18_iasp_151_cluster_sell_within_5d_count_63d_d3},
    "f18_iasp_152_insider_sell_at_52w_high_dollar_63d_d3": {"inputs": ["insider_sell_value", "high", "close"], "func": f18_iasp_152_insider_sell_at_52w_high_dollar_63d_d3},
    "f18_iasp_153_planned_sale_within_90d_of_plan_proxy_d3": {"inputs": ["insider_sell_value", "planned_sell_value"], "func": f18_iasp_153_planned_sale_within_90d_of_plan_proxy_d3},
}
