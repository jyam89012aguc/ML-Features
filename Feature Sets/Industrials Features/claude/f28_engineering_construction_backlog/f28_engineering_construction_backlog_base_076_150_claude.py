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
def _f28_backlog_proxy(deferredrev, revenue):
    # backlog proxy: deferred revenue as fraction of trailing 252d revenue mean
    rev_ma = revenue.rolling(252, min_periods=63).mean()
    return deferredrev / rev_ma.replace(0, np.nan)


def _f28_pipeline_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f28_backlog_consumption(deferredrev, revenue, w):
    # backlog consumption: revenue growth relative to backlog growth
    rg = revenue.pct_change(periods=w)
    bg = deferredrev.pct_change(periods=w)
    return rg - bg


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_5d_base_v076_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_10d_base_v077_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_21d_base_v078_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_42d_base_v079_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_63d_base_v080_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_126d_base_v081_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_189d_base_v082_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_252d_base_v083_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_378d_base_v084_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_504d_base_v085_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_proxy(deferredrev, revenue) * closeadj.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxvol_21d_base_v086_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 21) * _std(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxvol_63d_base_v087_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 63) * _std(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxvol_126d_base_v088_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 126) * _std(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxvol_252d_base_v089_signal(deferredrev, closeadj):
    result = _f28_pipeline_growth(deferredrev, 252) * _std(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxrev_63d_base_v090_signal(deferredrev, revenue, closeadj):
    result = _f28_pipeline_growth(deferredrev, 63) * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxrev_252d_base_v091_signal(deferredrev, revenue, closeadj):
    result = _f28_pipeline_growth(deferredrev, 252) * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxrev_63d_base_v092_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 63) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxrev_252d_base_v093_signal(deferredrev, revenue, closeadj):
    result = _f28_backlog_consumption(deferredrev, revenue, 252) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_dev_63d_base_v094_signal(deferredrev, revenue, closeadj):
    b = _f28_backlog_proxy(deferredrev, revenue)
    result = (b - _mean(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_dev_126d_base_v095_signal(deferredrev, revenue, closeadj):
    b = _f28_backlog_proxy(deferredrev, revenue)
    result = (b - _mean(b, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_dev_252d_base_v096_signal(deferredrev, revenue, closeadj):
    b = _f28_backlog_proxy(deferredrev, revenue)
    result = (b - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_dev_63d_base_v097_signal(deferredrev, closeadj):
    g = _f28_pipeline_growth(deferredrev, 63)
    result = (g - _mean(g, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_dev_126d_base_v098_signal(deferredrev, closeadj):
    g = _f28_pipeline_growth(deferredrev, 126)
    result = (g - _mean(g, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_dev_252d_base_v099_signal(deferredrev, closeadj):
    g = _f28_pipeline_growth(deferredrev, 252)
    result = (g - _mean(g, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyrank_504d_base_v100_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthrank_504d_base_v101_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumrank_252d_base_v102_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumrank_504d_base_v103_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyema_252d_base_v104_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthema_126d_base_v105_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 252).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumema_252d_base_v106_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 252).ewm(span=126, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyabs_base_v107_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthabs_63d_base_v108_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumabs_252d_base_v109_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxysign_base_v110_signal(deferredrev, revenue, closeadj):
    result = (np.sign(_f28_backlog_proxy(deferredrev, revenue) - 0.1)) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumsign_base_v111_signal(deferredrev, revenue, closeadj):
    result = (np.sign(_f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxdet_63d_base_v112_signal(deferredrev, revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_backlog_proxy(deferredrev, revenue)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxpxdet_63d_base_v113_signal(deferredrev, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_pipeline_growth(deferredrev, 63)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpxdet_63d_base_v114_signal(deferredrev, revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_backlog_consumption(deferredrev, revenue, 63)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpxdet_252d_base_v115_signal(deferredrev, revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_backlog_proxy(deferredrev, revenue)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxpxdet_252d_base_v116_signal(deferredrev, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_pipeline_growth(deferredrev, 252)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpxdet_252d_base_v117_signal(deferredrev, revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = (_f28_backlog_consumption(deferredrev, revenue, 252)) * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpkgap_63d_base_v118_signal(deferredrev, revenue, closeadj):
    peak = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_backlog_proxy(deferredrev, revenue)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxpkgap_63d_base_v119_signal(deferredrev, closeadj):
    peak = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_pipeline_growth(deferredrev, 63)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpkgap_63d_base_v120_signal(deferredrev, revenue, closeadj):
    peak = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_backlog_consumption(deferredrev, revenue, 63)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpkgap_252d_base_v121_signal(deferredrev, revenue, closeadj):
    peak = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_backlog_proxy(deferredrev, revenue)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxpkgap_252d_base_v122_signal(deferredrev, closeadj):
    peak = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_pipeline_growth(deferredrev, 252)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpkgap_252d_base_v123_signal(deferredrev, revenue, closeadj):
    peak = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = (_f28_backlog_consumption(deferredrev, revenue, 252)) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxrange_63d_base_v124_signal(deferredrev, revenue, closeadj):
    rng = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max() - closeadj.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = (_f28_backlog_proxy(deferredrev, revenue)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxrange_63d_base_v125_signal(deferredrev, closeadj):
    rng = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max() - closeadj.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = (_f28_pipeline_growth(deferredrev, 63)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxrange_63d_base_v126_signal(deferredrev, revenue, closeadj):
    rng = closeadj.rolling(63, min_periods=max(1, 63 // 2)).max() - closeadj.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = (_f28_backlog_consumption(deferredrev, revenue, 63)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxrange_252d_base_v127_signal(deferredrev, revenue, closeadj):
    rng = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max() - closeadj.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = (_f28_backlog_proxy(deferredrev, revenue)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxrange_252d_base_v128_signal(deferredrev, closeadj):
    rng = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max() - closeadj.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = (_f28_pipeline_growth(deferredrev, 252)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxrange_252d_base_v129_signal(deferredrev, revenue, closeadj):
    rng = closeadj.rolling(252, min_periods=max(1, 252 // 2)).max() - closeadj.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = (_f28_backlog_consumption(deferredrev, revenue, 252)) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_compo_252d_v1_base_v130_signal(deferredrev, revenue, closeadj):
    result = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 252) + _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_compo_252d_v2_base_v131_signal(deferredrev, revenue, closeadj):
    result = ((0.5 * _f28_backlog_proxy(deferredrev, revenue) + 0.3 * _f28_pipeline_growth(deferredrev, 252) + 0.2 * _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_compo_63d_v1_base_v132_signal(deferredrev, revenue, closeadj):
    result = ((_f28_backlog_proxy(deferredrev, revenue) + _f28_pipeline_growth(deferredrev, 63) + _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_compo_63d_v2_base_v133_signal(deferredrev, revenue, closeadj):
    result = ((0.5 * _f28_backlog_proxy(deferredrev, revenue) + 0.3 * _f28_pipeline_growth(deferredrev, 63) + 0.2 * _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_minus_bconsum_63d_base_v134_signal(deferredrev, revenue, closeadj):
    result = ((_f28_backlog_proxy(deferredrev, revenue) - _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_minus_pgrowth_63d_base_v135_signal(deferredrev, revenue, closeadj):
    result = ((_f28_backlog_proxy(deferredrev, revenue) - _f28_pipeline_growth(deferredrev, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowth_minus_bconsum_63d_base_v136_signal(deferredrev, revenue, closeadj):
    result = ((_f28_pipeline_growth(deferredrev, 63) - _f28_backlog_consumption(deferredrev, revenue, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxy_x_revgrowth_63d_base_v137_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * revenue.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxlogrev_252d_base_v138_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxlogrev_252d_base_v139_signal(deferredrev, revenue, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxlogrev_252d_base_v140_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxlogdr_252d_base_v141_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthxlogdr_252d_base_v142_signal(deferredrev, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 252) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxlogdr_252d_base_v143_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 252) * np.log(deferredrev.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxbproxydiff_252d_base_v144_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * _f28_backlog_proxy(deferredrev, revenue).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxydivpgrowth_63d_base_v145_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) / (_f28_pipeline_growth(deferredrev, 63).abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxydivbconsum_63d_base_v146_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) / (_f28_backlog_consumption(deferredrev, revenue, 63).abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_pgrowthdivbconsum_63d_base_v147_signal(deferredrev, revenue, closeadj):
    result = (_f28_pipeline_growth(deferredrev, 63) / (_f28_backlog_consumption(deferredrev, revenue, 63).abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bproxyxpgrowthsign_63d_base_v148_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_proxy(deferredrev, revenue) * np.sign(_f28_pipeline_growth(deferredrev, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_bconsumxpx_63d_base_v149_signal(deferredrev, revenue, closeadj):
    result = (_f28_backlog_consumption(deferredrev, revenue, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28ecb_f28_engineering_construction_backlog_compow3_252d_base_v150_signal(deferredrev, revenue, closeadj):
    result = ((0.4 * _f28_backlog_proxy(deferredrev, revenue) + 0.3 * _f28_pipeline_growth(deferredrev, 252) + 0.3 * _f28_backlog_consumption(deferredrev, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_5d_base_v076_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_10d_base_v077_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_21d_base_v078_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_42d_base_v079_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_63d_base_v080_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_126d_base_v081_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_189d_base_v082_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_252d_base_v083_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_378d_base_v084_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxchg_504d_base_v085_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxvol_21d_base_v086_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxvol_63d_base_v087_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxvol_126d_base_v088_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxvol_252d_base_v089_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxrev_63d_base_v090_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxrev_252d_base_v091_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxrev_63d_base_v092_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxrev_252d_base_v093_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_dev_63d_base_v094_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_dev_126d_base_v095_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_dev_252d_base_v096_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_dev_63d_base_v097_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_dev_126d_base_v098_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_dev_252d_base_v099_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyrank_504d_base_v100_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthrank_504d_base_v101_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumrank_252d_base_v102_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumrank_504d_base_v103_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyema_252d_base_v104_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthema_126d_base_v105_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumema_252d_base_v106_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyabs_base_v107_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthabs_63d_base_v108_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumabs_252d_base_v109_signal,
    f28ecb_f28_engineering_construction_backlog_bproxysign_base_v110_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumsign_base_v111_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxdet_63d_base_v112_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxpxdet_63d_base_v113_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpxdet_63d_base_v114_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpxdet_252d_base_v115_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxpxdet_252d_base_v116_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpxdet_252d_base_v117_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpkgap_63d_base_v118_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxpkgap_63d_base_v119_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpkgap_63d_base_v120_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpkgap_252d_base_v121_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxpkgap_252d_base_v122_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpkgap_252d_base_v123_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxrange_63d_base_v124_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxrange_63d_base_v125_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxrange_63d_base_v126_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxrange_252d_base_v127_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxrange_252d_base_v128_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxrange_252d_base_v129_signal,
    f28ecb_f28_engineering_construction_backlog_compo_252d_v1_base_v130_signal,
    f28ecb_f28_engineering_construction_backlog_compo_252d_v2_base_v131_signal,
    f28ecb_f28_engineering_construction_backlog_compo_63d_v1_base_v132_signal,
    f28ecb_f28_engineering_construction_backlog_compo_63d_v2_base_v133_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_minus_bconsum_63d_base_v134_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_minus_pgrowth_63d_base_v135_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowth_minus_bconsum_63d_base_v136_signal,
    f28ecb_f28_engineering_construction_backlog_bproxy_x_revgrowth_63d_base_v137_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxlogrev_252d_base_v138_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxlogrev_252d_base_v139_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxlogrev_252d_base_v140_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxlogdr_252d_base_v141_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthxlogdr_252d_base_v142_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxlogdr_252d_base_v143_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxbproxydiff_252d_base_v144_signal,
    f28ecb_f28_engineering_construction_backlog_bproxydivpgrowth_63d_base_v145_signal,
    f28ecb_f28_engineering_construction_backlog_bproxydivbconsum_63d_base_v146_signal,
    f28ecb_f28_engineering_construction_backlog_pgrowthdivbconsum_63d_base_v147_signal,
    f28ecb_f28_engineering_construction_backlog_bproxyxpgrowthsign_63d_base_v148_signal,
    f28ecb_f28_engineering_construction_backlog_bconsumxpx_63d_base_v149_signal,
    f28ecb_f28_engineering_construction_backlog_compow3_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_ENGINEERING_CONSTRUCTION_BACKLOG_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "deferredrev": deferredrev,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_backlog_proxy", "_f28_pipeline_growth", "_f28_backlog_consumption")
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
    print(f"OK f28_engineering_construction_backlog_base_076_150_claude: {n_features} features pass")
