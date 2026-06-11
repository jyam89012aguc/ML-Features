import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)

# ===== folder domain primitives =====
def _f071_deferred_change(deferredrev, w):
    return _slope_diff_norm_local(deferredrev, w) * deferredrev


def _f071_backlog_growth(deferredrev, w):
    avg = deferredrev.rolling(w, min_periods=max(1, w // 2)).mean()
    return (deferredrev - avg) / avg.replace(0, np.nan).abs() * deferredrev


def _f071_forward_demand(deferredrev, revenue, w):
    ratio = deferredrev / revenue.replace(0, np.nan).abs()
    return ratio * deferredrev.rolling(w, min_periods=max(1, w // 2)).mean()


def _slope_diff_norm_local(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v001_signal(deferredrev, revenue, closeadj):
    result = _f071_deferred_change(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v002_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v003_signal(deferredrev, revenue, closeadj):
    result = np.sign(_f071_deferred_change(deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v004_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_deferred_change(deferredrev, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v005_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_deferred_change(deferredrev, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v006_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_deferred_change(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v007_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 21)) * (_f071_deferred_change(deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v008_signal(deferredrev, revenue, closeadj):
    result = np.sqrt((_f071_deferred_change(deferredrev, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v009_signal(deferredrev, revenue, closeadj):
    result = np.log1p((_f071_deferred_change(deferredrev, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v010_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v011_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_deferred_change(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v012_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_deferred_change(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v013_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v014_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v015_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_deferred_change(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v016_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v017_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v018_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v019_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v020_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v021_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v022_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 252)) * (_f071_deferred_change(deferredrev, 252)) * (_f071_deferred_change(deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v023_signal(deferredrev, revenue, closeadj):
    result = (_f071_deferred_change(deferredrev, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v024_signal(deferredrev, revenue, closeadj):
    result = ((_f071_deferred_change(deferredrev, 252)) - (_f071_deferred_change(deferredrev, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v025_signal(deferredrev, revenue, closeadj):
    result = ((_f071_deferred_change(deferredrev, 252)) / (_f071_deferred_change(deferredrev, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v026_signal(deferredrev, revenue, closeadj):
    result = _f071_backlog_growth(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v027_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v028_signal(deferredrev, revenue, closeadj):
    result = np.sign(_f071_backlog_growth(deferredrev, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v029_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_backlog_growth(deferredrev, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v030_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_backlog_growth(deferredrev, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v031_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_backlog_growth(deferredrev, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v032_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 21)) * (_f071_backlog_growth(deferredrev, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v033_signal(deferredrev, revenue, closeadj):
    result = np.sqrt((_f071_backlog_growth(deferredrev, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v034_signal(deferredrev, revenue, closeadj):
    result = np.log1p((_f071_backlog_growth(deferredrev, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v035_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v036_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v037_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v038_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v039_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v040_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_backlog_growth(deferredrev, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v041_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v042_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v043_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v044_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v045_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v046_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v047_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 252)) * (_f071_backlog_growth(deferredrev, 252)) * (_f071_backlog_growth(deferredrev, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v048_signal(deferredrev, revenue, closeadj):
    result = (_f071_backlog_growth(deferredrev, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v049_signal(deferredrev, revenue, closeadj):
    result = ((_f071_backlog_growth(deferredrev, 252)) - (_f071_backlog_growth(deferredrev, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v050_signal(deferredrev, revenue, closeadj):
    result = ((_f071_backlog_growth(deferredrev, 252)) / (_f071_backlog_growth(deferredrev, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v051_signal(deferredrev, revenue, closeadj):
    result = _f071_forward_demand(deferredrev, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v052_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v053_signal(deferredrev, revenue, closeadj):
    result = np.sign(_f071_forward_demand(deferredrev, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v054_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_forward_demand(deferredrev, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v055_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_forward_demand(deferredrev, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v056_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_forward_demand(deferredrev, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v057_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 21)) * (_f071_forward_demand(deferredrev, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v058_signal(deferredrev, revenue, closeadj):
    result = np.sqrt((_f071_forward_demand(deferredrev, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v059_signal(deferredrev, revenue, closeadj):
    result = np.log1p((_f071_forward_demand(deferredrev, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v060_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v061_signal(deferredrev, revenue, closeadj):
    result = _mean(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v062_signal(deferredrev, revenue, closeadj):
    result = _std(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v063_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v064_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v065_signal(deferredrev, revenue, closeadj):
    result = _z(_f071_forward_demand(deferredrev, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v066_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v067_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v068_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v069_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v070_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v071_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v072_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 252)) * (_f071_forward_demand(deferredrev, revenue, 252)) * (_f071_forward_demand(deferredrev, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v073_signal(deferredrev, revenue, closeadj):
    result = (_f071_forward_demand(deferredrev, revenue, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v074_signal(deferredrev, revenue, closeadj):
    result = ((_f071_forward_demand(deferredrev, revenue, 252)) - (_f071_forward_demand(deferredrev, revenue, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v075_signal(deferredrev, revenue, closeadj):
    result = ((_f071_forward_demand(deferredrev, revenue, 252)) / (_f071_forward_demand(deferredrev, revenue, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v001_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v002_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v003_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v004_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_5d_base_v005_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v006_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v007_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v008_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v009_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_21d_base_v010_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v011_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v012_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v013_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v014_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_63d_base_v015_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v016_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v017_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v018_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v019_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_126d_base_v020_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v021_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v022_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v023_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v024_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_deferredchg_252d_base_v025_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v026_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v027_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v028_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v029_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_5d_base_v030_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v031_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v032_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v033_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v034_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_21d_base_v035_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v036_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v037_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v038_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v039_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_63d_base_v040_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v041_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v042_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v043_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v044_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_126d_base_v045_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v046_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v047_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v048_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v049_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_backloggrowth_252d_base_v050_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v051_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v052_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v053_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v054_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_5d_base_v055_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v056_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v057_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v058_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v059_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_21d_base_v060_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v061_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v062_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v063_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v064_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_63d_base_v065_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v066_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v067_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v068_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v069_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_126d_base_v070_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v071_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v072_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v073_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v074_signal,
    f071bdr_f071_backlog_deferred_revenue_proxy_fwddemand_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F071_BACKLOG_DEFERRED_REVENUE_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    cols = {"deferredrev": deferredrev, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f071_deferred_change", "_f071_backlog_growth", "_f071_forward_demand")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f071_backlog_deferred_revenue_proxy_001_075_claude: {n_features} features pass")
