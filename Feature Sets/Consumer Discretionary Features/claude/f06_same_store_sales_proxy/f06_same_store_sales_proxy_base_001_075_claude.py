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

def f06sss_f06_same_store_sales_proxy_rpp_mean_5d_base_v001_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_10d_base_v002_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_21d_base_v003_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_42d_base_v004_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_63d_base_v005_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_126d_base_v006_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_189d_base_v007_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_252d_base_v008_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_378d_base_v009_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_mean_504d_base_v010_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _mean(rpp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_5d_base_v011_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_10d_base_v012_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_21d_base_v013_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_42d_base_v014_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_63d_base_v015_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_126d_base_v016_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_189d_base_v017_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_252d_base_v018_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_378d_base_v019_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_std_504d_base_v020_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _std(rpp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_5d_base_v021_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_10d_base_v022_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_21d_base_v023_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_42d_base_v024_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_63d_base_v025_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_126d_base_v026_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_189d_base_v027_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_252d_base_v028_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_378d_base_v029_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_z_504d_base_v030_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _z(rpp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_5d_base_v031_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_10d_base_v032_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_21d_base_v033_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_42d_base_v034_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_63d_base_v035_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_126d_base_v036_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_189d_base_v037_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_252d_base_v038_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_378d_base_v039_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_ema_504d_base_v040_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = _ema(rpp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_5d_base_v041_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_10d_base_v042_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_21d_base_v043_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_42d_base_v044_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_63d_base_v045_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_126d_base_v046_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_189d_base_v047_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_252d_base_v048_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_378d_base_v049_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_rpp_diff_504d_base_v050_signal(revenue, ppnenet, closeadj):
    rpp = _f06_revenue_per_ppe(revenue, ppnenet)
    result = (rpp - rpp.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_5d_base_v051_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 5)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_10d_base_v052_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 10)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_21d_base_v053_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 21)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_42d_base_v054_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 42)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_63d_base_v055_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 63)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_126d_base_v056_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 126)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_189d_base_v057_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 189)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_252d_base_v058_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 252)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_378d_base_v059_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 378)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_g_504d_base_v060_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 504)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_5d_base_v061_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 5)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_10d_base_v062_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 10)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_21d_base_v063_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 21)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_42d_base_v064_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 42)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_63d_base_v065_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 63)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_126d_base_v066_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 126)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_189d_base_v067_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 189)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_252d_base_v068_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 252)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_378d_base_v069_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 378)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gmean_504d_base_v070_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 504)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_5d_base_v071_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 5)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_10d_base_v072_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 10)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_21d_base_v073_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 21)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_42d_base_v074_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 42)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f06sss_f06_same_store_sales_proxy_sss_gstd_63d_base_v075_signal(revenue, ppnenet, closeadj):
    g = _f06_sss_growth_proxy(revenue, ppnenet, 63)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f06sss_f06_same_store_sales_proxy_rpp_mean_5d_base_v001_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_10d_base_v002_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_21d_base_v003_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_42d_base_v004_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_63d_base_v005_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_126d_base_v006_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_189d_base_v007_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_252d_base_v008_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_378d_base_v009_signal,
    f06sss_f06_same_store_sales_proxy_rpp_mean_504d_base_v010_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_5d_base_v011_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_10d_base_v012_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_21d_base_v013_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_42d_base_v014_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_63d_base_v015_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_126d_base_v016_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_189d_base_v017_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_252d_base_v018_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_378d_base_v019_signal,
    f06sss_f06_same_store_sales_proxy_rpp_std_504d_base_v020_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_5d_base_v021_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_10d_base_v022_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_21d_base_v023_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_42d_base_v024_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_63d_base_v025_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_126d_base_v026_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_189d_base_v027_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_252d_base_v028_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_378d_base_v029_signal,
    f06sss_f06_same_store_sales_proxy_rpp_z_504d_base_v030_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_5d_base_v031_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_10d_base_v032_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_21d_base_v033_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_42d_base_v034_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_63d_base_v035_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_126d_base_v036_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_189d_base_v037_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_252d_base_v038_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_378d_base_v039_signal,
    f06sss_f06_same_store_sales_proxy_rpp_ema_504d_base_v040_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_5d_base_v041_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_10d_base_v042_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_21d_base_v043_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_42d_base_v044_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_63d_base_v045_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_126d_base_v046_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_189d_base_v047_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_252d_base_v048_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_378d_base_v049_signal,
    f06sss_f06_same_store_sales_proxy_rpp_diff_504d_base_v050_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_5d_base_v051_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_10d_base_v052_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_21d_base_v053_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_42d_base_v054_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_63d_base_v055_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_126d_base_v056_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_189d_base_v057_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_252d_base_v058_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_378d_base_v059_signal,
    f06sss_f06_same_store_sales_proxy_sss_g_504d_base_v060_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_5d_base_v061_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_10d_base_v062_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_21d_base_v063_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_42d_base_v064_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_63d_base_v065_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_126d_base_v066_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_189d_base_v067_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_252d_base_v068_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_378d_base_v069_signal,
    f06sss_f06_same_store_sales_proxy_sss_gmean_504d_base_v070_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_5d_base_v071_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_10d_base_v072_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_21d_base_v073_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_42d_base_v074_signal,
    f06sss_f06_same_store_sales_proxy_sss_gstd_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_SAME_STORE_SALES_PROXY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f06_same_store_sales_proxy_001_075_claude: {n_features} features pass")
