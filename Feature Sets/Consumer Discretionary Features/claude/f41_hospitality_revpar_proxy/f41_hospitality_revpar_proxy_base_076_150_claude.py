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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f41_revenue_per_asset(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f41_revpar_growth(revenue, ppnenet, w):
    r = revenue / ppnenet.replace(0, np.nan)
    return r.pct_change(periods=w)


def _f41_asset_utilization(revenue, assets, w):
    r = revenue / assets.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f41hrp_f41_hospitality_revpar_proxy_rpadiff_21m63_base_v076_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 21) - _mean(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiff_63m252_base_v077_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 63) - _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiff_252m504_base_v078_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 252) - _mean(r, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiff_21m252_base_v079_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 21) - _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparat_63v252_base_v080_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 63) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparat_21v63_base_v081_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 21) / _mean(r, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparat_252v504_base_v082_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 252) / _mean(r, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparat_126v252_base_v083_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_mean(r, 126) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxdv_21d_base_v084_signal(revenue, ppnenet, closeadj, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxdv_63d_base_v085_signal(revenue, ppnenet, closeadj, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxdv_252d_base_v086_signal(revenue, ppnenet, closeadj, volume):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aulog_63d_base_v087_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = np.log(au.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aulog_252d_base_v088_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = np.log(au.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aulog_504d_base_v089_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 504)
    result = np.log(au.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxau_63d_base_v090_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    au = _f41_asset_utilization(revenue, assets, 63)
    result = g * au * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxau_126d_base_v091_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    au = _f41_asset_utilization(revenue, assets, 126)
    result = g * au * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxau_252d_base_v092_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    au = _f41_asset_utilization(revenue, assets, 252)
    result = g * au * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxau_504d_base_v093_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 504)
    au = _f41_asset_utilization(revenue, assets, 504)
    result = g * au * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_compositeq_63d_base_v094_signal(revenue, ppnenet, assets, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (_mean(r, 63) + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_compositeq_126d_base_v095_signal(revenue, ppnenet, assets, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    au = _f41_asset_utilization(revenue, assets, 126)
    result = (_mean(r, 126) + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_compositeq_252d_base_v096_signal(revenue, ppnenet, assets, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    au = _f41_asset_utilization(revenue, assets, 252)
    result = (_mean(r, 252) + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_compositeq_504d_base_v097_signal(revenue, ppnenet, assets, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    au = _f41_asset_utilization(revenue, assets, 504)
    result = (_mean(r, 504) + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxvol_21d_base_v098_signal(revenue, ppnenet, volume):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = g * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxvol_63d_base_v099_signal(revenue, ppnenet, volume):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    result = g * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxvol_252d_base_v100_signal(revenue, ppnenet, volume):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    result = g * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpamedian_21d_base_v101_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpamedian_63d_base_v102_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpamedian_252d_base_v103_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparange_63d_base_v104_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (r.rolling(63, min_periods=max(1, 63//2)).max() - r.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparange_252d_base_v105_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (r.rolling(252, min_periods=max(1, 252//2)).max() - r.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparange_504d_base_v106_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (r.rolling(504, min_periods=max(1, 504//2)).max() - r.rolling(504, min_periods=max(1, 504//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_austd_63d_base_v107_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = _std(au, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_austd_252d_base_v108_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = _std(au, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_austd_504d_base_v109_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 504)
    result = _std(au, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurange_63d_base_v110_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (au.rolling(63, min_periods=max(1, 63//2)).max() - au.rolling(63, min_periods=max(1, 63//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurange_252d_base_v111_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = (au.rolling(252, min_periods=max(1, 252//2)).max() - au.rolling(252, min_periods=max(1, 252//2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpasqdev_63d_base_v112_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    m = _mean(r, 63)
    result = ((r - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpasqdev_252d_base_v113_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    m = _mean(r, 252)
    result = ((r - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_21d_base_v114_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet).replace(0, np.nan).abs()
    result = np.log(r).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_63d_base_v115_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet).replace(0, np.nan).abs()
    result = np.log(r).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_252d_base_v116_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet).replace(0, np.nan).abs()
    result = np.log(r).diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxv_42d_base_v117_signal(revenue, ppnenet, volume, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 42) * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxv_126d_base_v118_signal(revenue, ppnenet, volume, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 126) * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaxv_378d_base_v119_signal(revenue, ppnenet, volume, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = _mean(r, 378) * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgstd_63d_base_v120_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgstd_126d_base_v121_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _std(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgstd_252d_base_v122_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auema_21d_base_v123_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 21)
    result = _ema(au, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auema_63d_base_v124_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = _ema(au, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auema_126d_base_v125_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 126)
    result = _ema(au, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auema_252d_base_v126_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = _ema(au, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparank_63d_base_v127_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparank_126d_base_v128_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparank_252d_base_v129_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rparank_504d_base_v130_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = r.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurank_63d_base_v131_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = au.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurank_252d_base_v132_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 252)
    result = au.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_aurank_504d_base_v133_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 504)
    result = au.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_21d_base_v134_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = np.sign(r.diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_63d_base_v135_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = np.sign(r.diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_252d_base_v136_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = np.sign(r.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaemadiff_21m63_base_v137_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_ema(r, 21) - _ema(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaemadiff_63m252_base_v138_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    result = (_ema(r, 63) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auemadiff_21m63_base_v139_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (_ema(au, 21) - _ema(au, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auemadiff_63m252_base_v140_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (_ema(au, 63) - _ema(au, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auemadiff_126m252_base_v141_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (_ema(au, 126) - _ema(au, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgema_21d_base_v142_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 21)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgema_63d_base_v143_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    result = _ema(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgema_126d_base_v144_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 126)
    result = _ema(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgema_252d_base_v145_signal(revenue, ppnenet, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    result = _ema(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxaudiff_63d_base_v146_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 63)
    au = _f41_asset_utilization(revenue, assets, 63)
    result = (g + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpgxaudiff_252d_base_v147_signal(revenue, ppnenet, assets, closeadj):
    g = _f41_revpar_growth(revenue, ppnenet, 252)
    au = _f41_asset_utilization(revenue, assets, 252)
    result = (g + au) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaminmax_63d_base_v148_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    hi = r.rolling(63, min_periods=max(1, 63//2)).max()
    lo = r.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_rpaminmax_252d_base_v149_signal(revenue, ppnenet, closeadj):
    r = _f41_revenue_per_asset(revenue, ppnenet)
    hi = r.rolling(252, min_periods=max(1, 252//2)).max()
    lo = r.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41hrp_f41_hospitality_revpar_proxy_auminmax_63d_base_v150_signal(revenue, assets, closeadj):
    au = _f41_asset_utilization(revenue, assets, 63)
    hi = au.rolling(63, min_periods=max(1, 63//2)).max()
    lo = au.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((au - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41hrp_f41_hospitality_revpar_proxy_rpadiff_21m63_base_v076_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiff_63m252_base_v077_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiff_252m504_base_v078_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiff_21m252_base_v079_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparat_63v252_base_v080_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparat_21v63_base_v081_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparat_252v504_base_v082_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparat_126v252_base_v083_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxdv_21d_base_v084_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxdv_63d_base_v085_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxdv_252d_base_v086_signal,
    f41hrp_f41_hospitality_revpar_proxy_aulog_63d_base_v087_signal,
    f41hrp_f41_hospitality_revpar_proxy_aulog_252d_base_v088_signal,
    f41hrp_f41_hospitality_revpar_proxy_aulog_504d_base_v089_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxau_63d_base_v090_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxau_126d_base_v091_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxau_252d_base_v092_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxau_504d_base_v093_signal,
    f41hrp_f41_hospitality_revpar_proxy_compositeq_63d_base_v094_signal,
    f41hrp_f41_hospitality_revpar_proxy_compositeq_126d_base_v095_signal,
    f41hrp_f41_hospitality_revpar_proxy_compositeq_252d_base_v096_signal,
    f41hrp_f41_hospitality_revpar_proxy_compositeq_504d_base_v097_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxvol_21d_base_v098_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxvol_63d_base_v099_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxvol_252d_base_v100_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpamedian_21d_base_v101_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpamedian_63d_base_v102_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpamedian_252d_base_v103_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparange_63d_base_v104_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparange_252d_base_v105_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparange_504d_base_v106_signal,
    f41hrp_f41_hospitality_revpar_proxy_austd_63d_base_v107_signal,
    f41hrp_f41_hospitality_revpar_proxy_austd_252d_base_v108_signal,
    f41hrp_f41_hospitality_revpar_proxy_austd_504d_base_v109_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurange_63d_base_v110_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurange_252d_base_v111_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpasqdev_63d_base_v112_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpasqdev_252d_base_v113_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_21d_base_v114_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_63d_base_v115_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpalogdiff_252d_base_v116_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxv_42d_base_v117_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxv_126d_base_v118_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaxv_378d_base_v119_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgstd_63d_base_v120_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgstd_126d_base_v121_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgstd_252d_base_v122_signal,
    f41hrp_f41_hospitality_revpar_proxy_auema_21d_base_v123_signal,
    f41hrp_f41_hospitality_revpar_proxy_auema_63d_base_v124_signal,
    f41hrp_f41_hospitality_revpar_proxy_auema_126d_base_v125_signal,
    f41hrp_f41_hospitality_revpar_proxy_auema_252d_base_v126_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparank_63d_base_v127_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparank_126d_base_v128_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparank_252d_base_v129_signal,
    f41hrp_f41_hospitality_revpar_proxy_rparank_504d_base_v130_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurank_63d_base_v131_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurank_252d_base_v132_signal,
    f41hrp_f41_hospitality_revpar_proxy_aurank_504d_base_v133_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_21d_base_v134_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_63d_base_v135_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpadiffsign_252d_base_v136_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaemadiff_21m63_base_v137_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaemadiff_63m252_base_v138_signal,
    f41hrp_f41_hospitality_revpar_proxy_auemadiff_21m63_base_v139_signal,
    f41hrp_f41_hospitality_revpar_proxy_auemadiff_63m252_base_v140_signal,
    f41hrp_f41_hospitality_revpar_proxy_auemadiff_126m252_base_v141_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgema_21d_base_v142_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgema_63d_base_v143_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgema_126d_base_v144_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgema_252d_base_v145_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxaudiff_63d_base_v146_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpgxaudiff_252d_base_v147_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaminmax_63d_base_v148_signal,
    f41hrp_f41_hospitality_revpar_proxy_rpaminmax_252d_base_v149_signal,
    f41hrp_f41_hospitality_revpar_proxy_auminmax_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_HOSPITALITY_REVPAR_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ppnenet": ppnenet, "assets": assets }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_revenue_per_asset", "_f41_revpar_growth", "_f41_asset_utilization")
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
    print(f"OK hospitality_revpar_proxy_base_076_150_claude: {n_features} features pass")
