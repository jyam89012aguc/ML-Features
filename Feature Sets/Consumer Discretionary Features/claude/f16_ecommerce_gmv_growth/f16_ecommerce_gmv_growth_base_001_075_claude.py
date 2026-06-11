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
def _f16_revenue_growth_intensity(revenue, w):
    return revenue.pct_change(periods=w)


def _f16_wc_to_revenue(workingcapital, revenue):
    return workingcapital / revenue.replace(0, np.nan)


def _f16_gmv_proxy_score(revenue, workingcapital, w):
    g = revenue.pct_change(periods=w)
    wcr = workingcapital / revenue.replace(0, np.nan)
    return g / wcr.replace(0, np.nan).abs()


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_21d_base_v001_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_63d_base_v002_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_126d_base_v003_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_189d_base_v004_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_252d_base_v005_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_378d_base_v006_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_21d_base_v007_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_63d_base_v008_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_126d_base_v009_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_189d_base_v010_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_252d_base_v011_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_378d_base_v012_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_21d_base_v013_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_63d_base_v014_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_126d_base_v015_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_189d_base_v016_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_252d_base_v017_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_378d_base_v018_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    result = base * _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_21d_base_v019_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_63d_base_v020_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_126d_base_v021_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_189d_base_v022_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_252d_base_v023_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_378d_base_v024_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    result = base * _mean(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_21d_base_v025_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_63d_base_v026_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_126d_base_v027_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_189d_base_v028_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_252d_base_v029_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_378d_base_v030_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_21d_base_v031_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_63d_base_v032_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_126d_base_v033_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_189d_base_v034_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_252d_base_v035_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_378d_base_v036_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_21d_base_v037_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_63d_base_v038_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_126d_base_v039_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_189d_base_v040_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_252d_base_v041_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_378d_base_v042_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_21d_base_v043_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_63d_base_v044_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_126d_base_v045_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_189d_base_v046_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_252d_base_v047_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_378d_base_v048_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_21d_base_v049_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_63d_base_v050_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_126d_base_v051_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_189d_base_v052_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_252d_base_v053_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_378d_base_v054_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_21d_base_v055_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_63d_base_v056_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_126d_base_v057_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_189d_base_v058_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_252d_base_v059_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=252, min_periods=max(1, 252//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_378d_base_v060_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=378, min_periods=max(1, 378//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_21d_base_v061_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_63d_base_v062_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_126d_base_v063_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_189d_base_v064_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_252d_base_v065_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_378d_base_v066_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_21d_base_v067_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_63d_base_v068_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_126d_base_v069_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_189d_base_v070_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_252d_base_v071_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_378d_base_v072_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = _mean(g, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_21d_base_v073_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_63d_base_v074_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_126d_base_v075_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_21d_base_v001_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_63d_base_v002_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_126d_base_v003_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_189d_base_v004_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_252d_base_v005_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_378d_base_v006_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_21d_base_v007_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_63d_base_v008_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_126d_base_v009_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_189d_base_v010_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_252d_base_v011_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_378d_base_v012_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_21d_base_v013_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_63d_base_v014_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_126d_base_v015_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_189d_base_v016_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_252d_base_v017_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_378d_base_v018_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_21d_base_v019_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_63d_base_v020_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_126d_base_v021_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_189d_base_v022_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_252d_base_v023_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_378d_base_v024_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_21d_base_v025_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_63d_base_v026_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_126d_base_v027_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_189d_base_v028_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_252d_base_v029_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_378d_base_v030_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_21d_base_v031_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_63d_base_v032_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_126d_base_v033_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_189d_base_v034_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_252d_base_v035_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_378d_base_v036_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_21d_base_v037_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_63d_base_v038_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_126d_base_v039_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_189d_base_v040_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_252d_base_v041_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_378d_base_v042_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_21d_base_v043_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_63d_base_v044_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_126d_base_v045_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_189d_base_v046_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_252d_base_v047_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_378d_base_v048_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_21d_base_v049_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_63d_base_v050_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_126d_base_v051_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_189d_base_v052_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_252d_base_v053_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_378d_base_v054_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_21d_base_v055_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_63d_base_v056_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_126d_base_v057_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_189d_base_v058_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_252d_base_v059_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_378d_base_v060_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_21d_base_v061_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_63d_base_v062_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_126d_base_v063_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_189d_base_v064_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_252d_base_v065_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_378d_base_v066_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_21d_base_v067_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_63d_base_v068_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_126d_base_v069_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_189d_base_v070_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_252d_base_v071_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_378d_base_v072_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_21d_base_v073_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_63d_base_v074_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_GMV_GROWTH_REGISTRY_001_075 = REGISTRY


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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "sgna": sgna, "opex": opex,
        "gp": gp, "workingcapital": workingcapital,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f16_revenue_growth_intensity", "_f16_wc_to_revenue", "_f16_gmv_proxy_score",)
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
    print(f"OK f16_ecommerce_gmv_growth_base_001_075_claude: {n_features} features pass")
