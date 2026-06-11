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


# ===== folder domain primitives =====
def _f06_revenue_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f06_sss_growth_proxy(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    return rpp.pct_change(periods=w)


def _f06_comp_growth_score(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    m = rpp.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = rpp.rolling(w, min_periods=max(1, w // 2)).std()
    return (rpp - m) / sd.replace(0, np.nan)

def f06sss_f06_same_store_sales_proxy_sss_gstd_126d_base_v076_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 126)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_189d_base_v077_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 189)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_252d_base_v078_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 252)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_378d_base_v079_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 378)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_504d_base_v080_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 504)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_5d_base_v081_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 5)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_10d_base_v082_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 10)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_21d_base_v083_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 21)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_42d_base_v084_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 42)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_63d_base_v085_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 63)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_126d_base_v086_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 126)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_189d_base_v087_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 189)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_252d_base_v088_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 252)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_378d_base_v089_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 378)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gz_504d_base_v090_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 504)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_5d_base_v091_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 5)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_10d_base_v092_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 10)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_21d_base_v093_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 21)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_42d_base_v094_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 42)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_63d_base_v095_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 63)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_126d_base_v096_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 126)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_189d_base_v097_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 189)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_252d_base_v098_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 252)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_378d_base_v099_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 378)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gema_504d_base_v100_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 504)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_5d_base_v101_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_10d_base_v102_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_21d_base_v103_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_42d_base_v104_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_63d_base_v105_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_126d_base_v106_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_189d_base_v107_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_252d_base_v108_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_378d_base_v109_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_504d_base_v110_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_5d_base_v111_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 5)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_10d_base_v112_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 10)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_21d_base_v113_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 21)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_42d_base_v114_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 42)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_63d_base_v115_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 63)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_126d_base_v116_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 126)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_189d_base_v117_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 189)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_252d_base_v118_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 252)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_378d_base_v119_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 378)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_mean_504d_base_v120_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 504)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_5d_base_v121_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 5)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_10d_base_v122_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 10)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_21d_base_v123_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 21)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_42d_base_v124_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 42)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_63d_base_v125_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 63)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_126d_base_v126_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 126)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_189d_base_v127_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 189)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_252d_base_v128_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 252)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_378d_base_v129_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 378)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_std_504d_base_v130_signal(revenue, ppnenet, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 504)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_5d_base_v131_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 5)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_10d_base_v132_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 10)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_21d_base_v133_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 21)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_42d_base_v134_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 42)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_63d_base_v135_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 63)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_126d_base_v136_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 126)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_189d_base_v137_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 189)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_252d_base_v138_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 252)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_378d_base_v139_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 378)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xvol_504d_base_v140_signal(revenue, ppnenet, closeadj, volume):
    s = _f06_comp_growth_score(revenue, ppnenet, 504)
    result = s * closeadj * _mean(volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_5d_base_v141_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 5)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_10d_base_v142_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 10)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_21d_base_v143_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 21)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_42d_base_v144_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 42)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_63d_base_v145_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 63)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_126d_base_v146_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 126)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_189d_base_v147_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 189)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_252d_base_v148_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 252)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_378d_base_v149_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 378)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_compsc_xcapex_504d_base_v150_signal(revenue, ppnenet, capex, closeadj):
    s = _f06_comp_growth_score(revenue, ppnenet, 504)
    cap_int = capex / revenue.replace(0, np.nan)
    result = s * cap_int * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f06sss_f06_same_store_sales_proxy_sss_gstd_126d_base_v076_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_189d_base_v077_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_252d_base_v078_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_378d_base_v079_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_504d_base_v080_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_5d_base_v081_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_10d_base_v082_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_21d_base_v083_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_42d_base_v084_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_63d_base_v085_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_126d_base_v086_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_189d_base_v087_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_252d_base_v088_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_378d_base_v089_signal,
    f06sss_f06_same_store_sales_proxy_sss_gz_504d_base_v090_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_5d_base_v091_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_10d_base_v092_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_21d_base_v093_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_42d_base_v094_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_63d_base_v095_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_126d_base_v096_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_189d_base_v097_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_252d_base_v098_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_378d_base_v099_signal,
    f06sss_f06_same_store_sales_proxy_sss_gema_504d_base_v100_signal,
    f06sss_f06_same_store_sales_proxy_compsc_5d_base_v101_signal,
    f06sss_f06_same_store_sales_proxy_compsc_10d_base_v102_signal,
    f06sss_f06_same_store_sales_proxy_compsc_21d_base_v103_signal,
    f06sss_f06_same_store_sales_proxy_compsc_42d_base_v104_signal,
    f06sss_f06_same_store_sales_proxy_compsc_63d_base_v105_signal,
    f06sss_f06_same_store_sales_proxy_compsc_126d_base_v106_signal,
    f06sss_f06_same_store_sales_proxy_compsc_189d_base_v107_signal,
    f06sss_f06_same_store_sales_proxy_compsc_252d_base_v108_signal,
    f06sss_f06_same_store_sales_proxy_compsc_378d_base_v109_signal,
    f06sss_f06_same_store_sales_proxy_compsc_504d_base_v110_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_5d_base_v111_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_10d_base_v112_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_21d_base_v113_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_42d_base_v114_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_63d_base_v115_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_126d_base_v116_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_189d_base_v117_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_252d_base_v118_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_378d_base_v119_signal,
    f06sss_f06_same_store_sales_proxy_compsc_mean_504d_base_v120_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_5d_base_v121_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_10d_base_v122_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_21d_base_v123_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_42d_base_v124_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_63d_base_v125_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_126d_base_v126_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_189d_base_v127_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_252d_base_v128_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_378d_base_v129_signal,
    f06sss_f06_same_store_sales_proxy_compsc_std_504d_base_v130_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_5d_base_v131_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_10d_base_v132_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_21d_base_v133_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_42d_base_v134_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_63d_base_v135_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_126d_base_v136_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_189d_base_v137_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_252d_base_v138_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_378d_base_v139_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xvol_504d_base_v140_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_5d_base_v141_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_10d_base_v142_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_21d_base_v143_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_42d_base_v144_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_63d_base_v145_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_126d_base_v146_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_189d_base_v147_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_252d_base_v148_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_378d_base_v149_signal,
    f06sss_f06_same_store_sales_proxy_compsc_xcapex_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_SAME_STORE_SALES_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_revenue_per_ppe", "_f06_sss_growth_proxy", "_f06_comp_growth_score")
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
    print(f"OK f06_same_store_sales_proxy_076_150_claude: {n_features} features pass")
