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


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_189d_base_v076_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_252d_base_v077_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_z_378d_base_v078_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_21d_base_v079_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_63d_base_v080_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_126d_base_v081_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_189d_base_v082_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_252d_base_v083_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_378d_base_v084_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g.abs() * np.sign(g)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_21d_base_v085_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_63d_base_v086_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_126d_base_v087_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_189d_base_v088_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_252d_base_v089_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 252)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_378d_base_v090_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 378)
    base = g * g.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_10d_base_v091_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_21d_base_v092_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_42d_base_v093_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_63d_base_v094_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_126d_base_v095_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_189d_base_v096_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg / wcr.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_10d_base_v097_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_21d_base_v098_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_42d_base_v099_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_63d_base_v100_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_126d_base_v101_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_189d_base_v102_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = rg - wcr
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_10d_base_v103_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_21d_base_v104_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_42d_base_v105_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_63d_base_v106_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_126d_base_v107_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvprgsum_189d_base_v108_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = g + rg
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_10d_base_v109_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 10) * _mean(wcr, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_21d_base_v110_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 21) * _mean(wcr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_42d_base_v111_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 42) * _mean(wcr, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_63d_base_v112_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 63) * _mean(wcr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_126d_base_v113_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 126) * _mean(wcr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_189d_base_v114_signal(revenue, workingcapital, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = _mean(rg, 189) * _mean(wcr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_10d_base_v115_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    base = _z(g, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_21d_base_v116_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = _z(g, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_42d_base_v117_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    base = _z(g, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_63d_base_v118_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = _z(g, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_126d_base_v119_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmvzx_189d_base_v120_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = _z(g, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_10d_base_v121_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = rg * _mean(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_21d_base_v122_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = rg * _mean(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_42d_base_v123_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = rg * _mean(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_63d_base_v124_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = rg * _mean(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_126d_base_v125_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = rg * _mean(closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rgxclmean_189d_base_v126_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = rg * _mean(closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_10d_base_v127_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(10, min_periods=max(1, 10//2)).max() - wcr.rolling(10, min_periods=max(1, 10//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_21d_base_v128_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(21, min_periods=max(1, 21//2)).max() - wcr.rolling(21, min_periods=max(1, 21//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_42d_base_v129_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(42, min_periods=max(1, 42//2)).max() - wcr.rolling(42, min_periods=max(1, 42//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_63d_base_v130_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(63, min_periods=max(1, 63//2)).max() - wcr.rolling(63, min_periods=max(1, 63//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_126d_base_v131_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(126, min_periods=max(1, 126//2)).max() - wcr.rolling(126, min_periods=max(1, 126//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_range_189d_base_v132_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = wcr.rolling(189, min_periods=max(1, 189//2)).max() - wcr.rolling(189, min_periods=max(1, 189//2)).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_10d_base_v133_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 10)
    base = g.rolling(10, min_periods=max(1, 10//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_21d_base_v134_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 21)
    base = g.rolling(21, min_periods=max(1, 21//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_42d_base_v135_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 42)
    base = g.rolling(42, min_periods=max(1, 42//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_63d_base_v136_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 63)
    base = g.rolling(63, min_periods=max(1, 63//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_126d_base_v137_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 126)
    base = g.rolling(126, min_periods=max(1, 126//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_gmv_rmax_189d_base_v138_signal(revenue, workingcapital, closeadj):
    g = _f16_gmv_proxy_score(revenue, workingcapital, 189)
    base = g.rolling(189, min_periods=max(1, 189//2)).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_10d_base_v139_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 10)
    base = rg.ewm(span=10, min_periods=max(1, 10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_21d_base_v140_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 21)
    base = rg.ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_42d_base_v141_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 42)
    base = rg.ewm(span=42, min_periods=max(1, 42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_63d_base_v142_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 63)
    base = rg.ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_126d_base_v143_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 126)
    base = rg.ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_rg_ema_189d_base_v144_signal(revenue, closeadj):
    rg = _f16_revenue_growth_intensity(revenue, 189)
    base = rg.ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_10d_base_v145_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(10, min_periods=max(1, 10//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_21d_base_v146_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(21, min_periods=max(1, 21//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_42d_base_v147_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(42, min_periods=max(1, 42//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_63d_base_v148_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(63, min_periods=max(1, 63//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_126d_base_v149_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(126, min_periods=max(1, 126//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16egg_f16_ecommerce_gmv_growth_wcr_dmed_189d_base_v150_signal(workingcapital, revenue, closeadj):
    wcr = _f16_wc_to_revenue(workingcapital, revenue)
    base = (wcr - wcr.rolling(189, min_periods=max(1, 189//2)).median())
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_189d_base_v076_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_252d_base_v077_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_z_378d_base_v078_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_21d_base_v079_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_63d_base_v080_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_126d_base_v081_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_189d_base_v082_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_252d_base_v083_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_absx_378d_base_v084_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_21d_base_v085_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_63d_base_v086_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_126d_base_v087_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_189d_base_v088_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_252d_base_v089_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvscore_sq_378d_base_v090_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_10d_base_v091_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_21d_base_v092_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_42d_base_v093_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_63d_base_v094_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_126d_base_v095_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_mix_189d_base_v096_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_10d_base_v097_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_21d_base_v098_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_42d_base_v099_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_63d_base_v100_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_126d_base_v101_signal,
    f16egg_f16_ecommerce_gmv_growth_rgmwcr_diff_189d_base_v102_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_10d_base_v103_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_21d_base_v104_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_42d_base_v105_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_63d_base_v106_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_126d_base_v107_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvprgsum_189d_base_v108_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_10d_base_v109_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_21d_base_v110_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_42d_base_v111_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_63d_base_v112_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_126d_base_v113_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxwcr_smooth_189d_base_v114_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_10d_base_v115_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_21d_base_v116_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_42d_base_v117_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_63d_base_v118_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_126d_base_v119_signal,
    f16egg_f16_ecommerce_gmv_growth_gmvzx_189d_base_v120_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_10d_base_v121_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_21d_base_v122_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_42d_base_v123_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_63d_base_v124_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_126d_base_v125_signal,
    f16egg_f16_ecommerce_gmv_growth_rgxclmean_189d_base_v126_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_10d_base_v127_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_21d_base_v128_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_42d_base_v129_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_63d_base_v130_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_126d_base_v131_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_range_189d_base_v132_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_10d_base_v133_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_21d_base_v134_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_42d_base_v135_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_63d_base_v136_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_126d_base_v137_signal,
    f16egg_f16_ecommerce_gmv_growth_gmv_rmax_189d_base_v138_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_10d_base_v139_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_21d_base_v140_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_42d_base_v141_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_63d_base_v142_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_126d_base_v143_signal,
    f16egg_f16_ecommerce_gmv_growth_rg_ema_189d_base_v144_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_10d_base_v145_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_21d_base_v146_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_42d_base_v147_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_63d_base_v148_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_126d_base_v149_signal,
    f16egg_f16_ecommerce_gmv_growth_wcr_dmed_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_GMV_GROWTH_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f16_ecommerce_gmv_growth_base_076_150_claude: {n_features} features pass")
