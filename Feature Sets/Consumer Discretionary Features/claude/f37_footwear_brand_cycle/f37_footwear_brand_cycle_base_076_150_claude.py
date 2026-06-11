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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f37_revenue_accel(revenue, w):
    # Second derivative of log revenue (acceleration)
    lr = np.log(revenue.replace(0, np.nan).abs())
    return lr.diff(w).diff(w)


def _f37_brand_cycle_signal(revenue, grossmargin, w):
    # Revenue growth + margin maintenance
    rev_g = revenue.pct_change(w)
    gm_stab = -_std(grossmargin, w)
    return rev_g + gm_stab


def _f37_product_cycle_score(revenue, ebitdamargin, w):
    # Revenue acceleration weighted by ebitda margin level
    lr = np.log(revenue.replace(0, np.nan).abs())
    accel = lr.diff(w).diff(w)
    return accel * _mean(ebitdamargin, w)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_5d_base_v076_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 5)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_10d_base_v077_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 10)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_21d_base_v078_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_42d_base_v079_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 42)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_63d_base_v080_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_126d_base_v081_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 126)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_189d_base_v082_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 189)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_252d_base_v083_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_378d_base_v084_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 378)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxrev_504d_base_v085_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 504)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_5d_base_v086_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 5)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_10d_base_v087_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 10)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_21d_base_v088_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_42d_base_v089_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 42)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_63d_base_v090_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_126d_base_v091_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_189d_base_v092_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 189)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_252d_base_v093_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_378d_base_v094_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycsq_504d_base_v095_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 504)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_5d_base_v096_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 5)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_10d_base_v097_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 10)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_21d_base_v098_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_42d_base_v099_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 42)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_63d_base_v100_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_126d_base_v101_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_189d_base_v102_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 189)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_252d_base_v103_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_378d_base_v104_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycsq_504d_base_v105_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 504)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_10d_base_v106_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 10)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_21d_base_v107_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_42d_base_v108_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 42)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_63d_base_v109_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_126d_base_v110_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 126)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_252d_base_v111_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 252)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelsign_504d_base_v112_signal(revenue, grossmargin, closeadj):
    d = _f37_revenue_accel(revenue, 504)
    result = np.sign(d) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_21d_base_v113_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = (d / _std(d, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_63d_base_v114_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = (d / _std(d, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_126d_base_v115_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = (d / _std(d, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_189d_base_v116_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 189)
    result = (d / _std(d, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_252d_base_v117_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = (d / _std(d, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_378d_base_v118_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = (d / _std(d, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycshr_504d_base_v119_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 504)
    result = (d / _std(d, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_21d_base_v120_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = (d / _std(d, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_63d_base_v121_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = (d / _std(d, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_126d_base_v122_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = (d / _std(d, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_189d_base_v123_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 189)
    result = (d / _std(d, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_252d_base_v124_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = (d / _std(d, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_378d_base_v125_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = (d / _std(d, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycshr_504d_base_v126_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 504)
    result = (d / _std(d, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_10d_base_v127_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_21d_base_v128_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_42d_base_v129_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_63d_base_v130_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_126d_base_v131_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_252d_base_v132_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelema_378d_base_v133_signal(revenue, closeadj):
    d = _f37_revenue_accel(revenue, 21)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_21d_base_v134_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 21)
    result = d * ebitdamargin.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_42d_base_v135_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 42)
    result = d * ebitdamargin.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_63d_base_v136_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = d * ebitdamargin.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_126d_base_v137_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 126)
    result = d * ebitdamargin.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_189d_base_v138_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 189)
    result = d * ebitdamargin.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_252d_base_v139_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 252)
    result = d * ebitdamargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxemd_378d_base_v140_signal(revenue, grossmargin, ebitdamargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 378)
    result = d * ebitdamargin.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_21d_base_v141_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 21)
    result = d * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_42d_base_v142_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 42)
    result = d * revenue.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_63d_base_v143_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 63)
    result = d * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_126d_base_v144_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 126)
    result = d * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_189d_base_v145_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 189)
    result = d * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_252d_base_v146_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 252)
    result = d * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_prodcycxrevg_378d_base_v147_signal(revenue, ebitdamargin, closeadj):
    d = _f37_product_cycle_score(revenue, ebitdamargin, 378)
    result = d * revenue.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxem_126d_base_v148_signal(revenue, ebitdamargin, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_revaccelxem_252d_base_v149_signal(revenue, ebitdamargin, closeadj):
    d = _f37_revenue_accel(revenue, 63)
    result = d * _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37fbc_f37_footwear_brand_cycle_brandcycxrev_252d_base_v150_signal(revenue, grossmargin, closeadj):
    d = _f37_brand_cycle_signal(revenue, grossmargin, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_5d_base_v076_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_10d_base_v077_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_21d_base_v078_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_42d_base_v079_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_63d_base_v080_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_126d_base_v081_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_189d_base_v082_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_252d_base_v083_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_378d_base_v084_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxrev_504d_base_v085_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_5d_base_v086_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_10d_base_v087_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_21d_base_v088_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_42d_base_v089_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_63d_base_v090_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_126d_base_v091_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_189d_base_v092_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_252d_base_v093_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_378d_base_v094_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycsq_504d_base_v095_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_5d_base_v096_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_10d_base_v097_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_21d_base_v098_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_42d_base_v099_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_63d_base_v100_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_126d_base_v101_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_189d_base_v102_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_252d_base_v103_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_378d_base_v104_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycsq_504d_base_v105_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_10d_base_v106_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_21d_base_v107_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_42d_base_v108_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_63d_base_v109_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_126d_base_v110_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_252d_base_v111_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelsign_504d_base_v112_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_21d_base_v113_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_63d_base_v114_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_126d_base_v115_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_189d_base_v116_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_252d_base_v117_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_378d_base_v118_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycshr_504d_base_v119_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_21d_base_v120_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_63d_base_v121_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_126d_base_v122_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_189d_base_v123_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_252d_base_v124_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_378d_base_v125_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycshr_504d_base_v126_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_10d_base_v127_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_21d_base_v128_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_42d_base_v129_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_63d_base_v130_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_126d_base_v131_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_252d_base_v132_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelema_378d_base_v133_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_21d_base_v134_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_42d_base_v135_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_63d_base_v136_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_126d_base_v137_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_189d_base_v138_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_252d_base_v139_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxemd_378d_base_v140_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_21d_base_v141_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_42d_base_v142_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_63d_base_v143_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_126d_base_v144_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_189d_base_v145_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_252d_base_v146_signal,
    f37fbc_f37_footwear_brand_cycle_prodcycxrevg_378d_base_v147_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxem_126d_base_v148_signal,
    f37fbc_f37_footwear_brand_cycle_revaccelxem_252d_base_v149_signal,
    f37fbc_f37_footwear_brand_cycle_brandcycxrev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_FOOTWEAR_BRAND_CYCLE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_revenue_accel", "_f37_brand_cycle_signal", "_f37_product_cycle_score",)
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
    print(f"OK f37_footwear_brand_cycle_076_150_claude: {n_features} features pass")
