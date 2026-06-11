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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f16_revenue_growth_intensity(revenue, w):
    return revenue.pct_change(periods=w)


def _f16_wc_to_revenue(workingcapital, revenue):
    return workingcapital / revenue.replace(0, np.nan)


def _f16_gmv_proxy_score(revenue, workingcapital, w):
    g = revenue.pct_change(periods=w)
    wcr = workingcapital / revenue.replace(0, np.nan)
    return g / wcr.replace(0, np.nan).abs()


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_21d_slope_v001_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_63d_slope_v002_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_126d_slope_v003_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_189d_slope_v004_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_252d_slope_v005_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_378d_slope_v006_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_21d_slope_v007_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    base_val = base * revenue
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_63d_slope_v008_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    base_val = base * revenue
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_126d_slope_v009_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    base_val = base * revenue
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_189d_slope_v010_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    base_val = base * revenue
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_252d_slope_v011_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    base_val = base * revenue
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_378d_slope_v012_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    base_val = base * revenue
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_21d_slope_v013_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    base_val = base * _z(revenue, 252)
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_63d_slope_v014_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    base_val = base * _z(revenue, 252)
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_126d_slope_v015_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    base_val = base * _z(revenue, 252)
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_189d_slope_v016_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    base_val = base * _z(revenue, 252)
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_252d_slope_v017_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    base_val = base * _z(revenue, 252)
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_z_378d_slope_v018_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    base_val = base * _z(revenue, 252)
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_21d_slope_v019_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    base_val = base * _mean(revenue, 21)
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_63d_slope_v020_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    base_val = base * _mean(revenue, 21)
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_126d_slope_v021_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    base_val = base * _mean(revenue, 21)
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_189d_slope_v022_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    base_val = base * _mean(revenue, 21)
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_252d_slope_v023_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    base_val = base * _mean(revenue, 21)
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_378d_slope_v024_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    base_val = base * _mean(revenue, 21)
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_21d_slope_v025_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 21)
    base_val = base * _mean(closeadj, 63)
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_63d_slope_v026_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 63)
    base_val = base * _mean(closeadj, 63)
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_126d_slope_v027_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 126)
    base_val = base * _mean(closeadj, 63)
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_189d_slope_v028_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 189)
    base_val = base * _mean(closeadj, 63)
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_252d_slope_v029_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 252)
    base_val = base * _mean(closeadj, 63)
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_378d_slope_v030_signal(revenue, closeadj):
    base = _f16_revenue_growth_intensity(revenue, 378)
    base_val = base * _mean(closeadj, 63)
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_21d_slope_v031_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_63d_slope_v032_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_126d_slope_v033_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_189d_slope_v034_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_252d_slope_v035_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_378d_slope_v036_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr * _mean(closeadj, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_21d_slope_v037_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_63d_slope_v038_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_126d_slope_v039_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_189d_slope_v040_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_252d_slope_v041_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_378d_slope_v042_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(wcr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_21d_slope_v043_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_63d_slope_v044_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_126d_slope_v045_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_189d_slope_v046_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_252d_slope_v047_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_378d_slope_v048_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _std(wcr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_21d_slope_v049_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_63d_slope_v050_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_126d_slope_v051_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_189d_slope_v052_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_252d_slope_v053_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_378d_slope_v054_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _z(wcr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_21d_slope_v055_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_63d_slope_v056_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_126d_slope_v057_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_189d_slope_v058_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_252d_slope_v059_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=252, min_periods=max(1, 252//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_378d_slope_v060_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.ewm(span=378, min_periods=max(1, 378//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_21d_slope_v061_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_63d_slope_v062_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_126d_slope_v063_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_189d_slope_v064_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_252d_slope_v065_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_378d_slope_v066_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_21d_slope_v067_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_63d_slope_v068_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_126d_slope_v069_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_189d_slope_v070_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_252d_slope_v071_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_378d_slope_v072_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = _mean(g, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_21d_slope_v073_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_63d_slope_v074_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_126d_slope_v075_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_189d_slope_v076_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_252d_slope_v077_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_378d_slope_v078_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_21d_slope_v079_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_63d_slope_v080_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_126d_slope_v081_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_189d_slope_v082_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_252d_slope_v083_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_378d_slope_v084_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g.abs() * np.sign(g)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_21d_slope_v085_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_63d_slope_v086_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_126d_slope_v087_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_189d_slope_v088_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_252d_slope_v089_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_378d_slope_v090_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g * g.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_10d_slope_v091_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_21d_slope_v092_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_42d_slope_v093_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_63d_slope_v094_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_126d_slope_v095_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_189d_slope_v096_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_10d_slope_v097_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_21d_slope_v098_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_42d_slope_v099_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_63d_slope_v100_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_126d_slope_v101_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_189d_slope_v102_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_10d_slope_v103_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = g + rg
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_21d_slope_v104_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = g + rg
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_42d_slope_v105_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = g + rg
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_63d_slope_v106_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = g + rg
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_126d_slope_v107_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = g + rg
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_189d_slope_v108_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = g + rg
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_10d_slope_v109_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 10) * _mean(wcr, 10)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_21d_slope_v110_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 21) * _mean(wcr, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_42d_slope_v111_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 42) * _mean(wcr, 42)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_63d_slope_v112_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 63) * _mean(wcr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_126d_slope_v113_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 126) * _mean(wcr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_189d_slope_v114_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 189) * _mean(wcr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_10d_slope_v115_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    base = _z(g, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_21d_slope_v116_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _z(g, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_42d_slope_v117_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    base = _z(g, 84)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_63d_slope_v118_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _z(g, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_126d_slope_v119_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _z(g, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_189d_slope_v120_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _z(g, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_10d_slope_v121_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = rg * _mean(closeadj, 10)
    base_val = base
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_21d_slope_v122_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = rg * _mean(closeadj, 21)
    base_val = base
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_42d_slope_v123_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = rg * _mean(closeadj, 42)
    base_val = base
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_63d_slope_v124_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = rg * _mean(closeadj, 63)
    base_val = base
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_126d_slope_v125_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = rg * _mean(closeadj, 126)
    base_val = base
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_189d_slope_v126_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = rg * _mean(closeadj, 189)
    base_val = base
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_10d_slope_v127_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(10, min_periods=max(1, 10//2)).max() - wcr.rolling(10, min_periods=max(1, 10//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_21d_slope_v128_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(21, min_periods=max(1, 21//2)).max() - wcr.rolling(21, min_periods=max(1, 21//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_42d_slope_v129_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(42, min_periods=max(1, 42//2)).max() - wcr.rolling(42, min_periods=max(1, 42//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_63d_slope_v130_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(63, min_periods=max(1, 63//2)).max() - wcr.rolling(63, min_periods=max(1, 63//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_126d_slope_v131_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(126, min_periods=max(1, 126//2)).max() - wcr.rolling(126, min_periods=max(1, 126//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_189d_slope_v132_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(189, min_periods=max(1, 189//2)).max() - wcr.rolling(189, min_periods=max(1, 189//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_10d_slope_v133_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    base = g.rolling(10, min_periods=max(1, 10//2)).max()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_21d_slope_v134_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g.rolling(21, min_periods=max(1, 21//2)).max()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_42d_slope_v135_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    base = g.rolling(42, min_periods=max(1, 42//2)).max()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_63d_slope_v136_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g.rolling(63, min_periods=max(1, 63//2)).max()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_126d_slope_v137_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g.rolling(126, min_periods=max(1, 126//2)).max()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_189d_slope_v138_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g.rolling(189, min_periods=max(1, 189//2)).max()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_10d_slope_v139_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = rg.ewm(span=10, min_periods=max(1, 10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_21d_slope_v140_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = rg.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_42d_slope_v141_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = rg.ewm(span=42, min_periods=max(1, 42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_63d_slope_v142_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = rg.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_126d_slope_v143_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = rg.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_189d_slope_v144_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = rg.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_10d_slope_v145_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(10, min_periods=max(1, 10//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_21d_slope_v146_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(21, min_periods=max(1, 21//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_42d_slope_v147_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(42, min_periods=max(1, 42//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_63d_slope_v148_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(63, min_periods=max(1, 63//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_126d_slope_v149_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(126, min_periods=max(1, 126//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_189d_slope_v150_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(189, min_periods=max(1, 189//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_21d_slope_v001_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_63d_slope_v002_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_126d_slope_v003_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_189d_slope_v004_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_252d_slope_v005_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xclose_378d_slope_v006_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_21d_slope_v007_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_63d_slope_v008_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_126d_slope_v009_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_189d_slope_v010_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_252d_slope_v011_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_xrev_378d_slope_v012_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_21d_slope_v013_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_63d_slope_v014_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_126d_slope_v015_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_189d_slope_v016_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_252d_slope_v017_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_z_378d_slope_v018_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_21d_slope_v019_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_63d_slope_v020_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_126d_slope_v021_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_189d_slope_v022_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_252d_slope_v023_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_mean21_378d_slope_v024_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_21d_slope_v025_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_63d_slope_v026_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_126d_slope_v027_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_189d_slope_v028_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_252d_slope_v029_signal,
    f16egg_f16_ecommerce_gmv_growth_revgrowth_rolavg_378d_slope_v030_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_21d_slope_v031_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_63d_slope_v032_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_126d_slope_v033_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_189d_slope_v034_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_252d_slope_v035_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_xclmean_378d_slope_v036_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_21d_slope_v037_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_63d_slope_v038_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_126d_slope_v039_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_189d_slope_v040_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_252d_slope_v041_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rmean_378d_slope_v042_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_21d_slope_v043_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_63d_slope_v044_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_126d_slope_v045_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_189d_slope_v046_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_252d_slope_v047_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_rstd_378d_slope_v048_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_21d_slope_v049_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_63d_slope_v050_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_126d_slope_v051_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_189d_slope_v052_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_252d_slope_v053_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_zscore_378d_slope_v054_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_21d_slope_v055_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_63d_slope_v056_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_126d_slope_v057_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_189d_slope_v058_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_252d_slope_v059_signal,
    f16egg_f16_ecommerce_gmv_growth_wcrev_emaw_378d_slope_v060_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_21d_slope_v061_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_63d_slope_v062_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_126d_slope_v063_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_189d_slope_v064_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_252d_slope_v065_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_raw_378d_slope_v066_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_21d_slope_v067_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_63d_slope_v068_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_126d_slope_v069_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_189d_slope_v070_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_252d_slope_v071_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_smean_378d_slope_v072_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_21d_slope_v073_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_63d_slope_v074_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_126d_slope_v075_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_189d_slope_v076_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_252d_slope_v077_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_378d_slope_v078_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_21d_slope_v079_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_63d_slope_v080_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_126d_slope_v081_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_189d_slope_v082_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_252d_slope_v083_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_378d_slope_v084_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_21d_slope_v085_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_63d_slope_v086_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_126d_slope_v087_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_189d_slope_v088_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_252d_slope_v089_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_378d_slope_v090_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_10d_slope_v091_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_21d_slope_v092_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_42d_slope_v093_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_63d_slope_v094_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_126d_slope_v095_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_189d_slope_v096_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_10d_slope_v097_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_21d_slope_v098_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_42d_slope_v099_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_63d_slope_v100_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_126d_slope_v101_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_189d_slope_v102_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_10d_slope_v103_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_21d_slope_v104_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_42d_slope_v105_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_63d_slope_v106_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_126d_slope_v107_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_189d_slope_v108_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_10d_slope_v109_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_21d_slope_v110_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_42d_slope_v111_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_63d_slope_v112_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_126d_slope_v113_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_189d_slope_v114_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_10d_slope_v115_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_21d_slope_v116_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_42d_slope_v117_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_63d_slope_v118_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_126d_slope_v119_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_189d_slope_v120_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_10d_slope_v121_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_21d_slope_v122_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_42d_slope_v123_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_63d_slope_v124_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_126d_slope_v125_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_189d_slope_v126_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_10d_slope_v127_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_21d_slope_v128_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_42d_slope_v129_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_63d_slope_v130_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_126d_slope_v131_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_189d_slope_v132_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_10d_slope_v133_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_21d_slope_v134_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_42d_slope_v135_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_63d_slope_v136_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_126d_slope_v137_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_189d_slope_v138_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_10d_slope_v139_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_21d_slope_v140_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_42d_slope_v141_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_63d_slope_v142_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_126d_slope_v143_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_189d_slope_v144_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_10d_slope_v145_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_21d_slope_v146_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_42d_slope_v147_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_63d_slope_v148_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_126d_slope_v149_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_GMV_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_ecommerce_gmv_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
