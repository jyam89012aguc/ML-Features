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
def _f09_inv_sales_ratio(inventory, revenue):
    return inventory / revenue.replace(0, np.nan).abs()


def _f09_inv_revenue_gap(inventory, revenue, w):
    inv_g = inventory.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return inv_g - rev_g


def _f09_inv_velocity(inventory, cor):
    return cor / inventory.replace(0, np.nan).abs()


# inv/sales max 252d * close
def f09isd_f09_inventory_to_sales_dynamics_invmax_252d_base_v076_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmax_504d_base_v077_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmin_252d_base_v078_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmin_504d_base_v079_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invrng_252d_base_v080_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invrng_504d_base_v081_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    rng = b.rolling(504, min_periods=126).max() - b.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invpct_252d_base_v082_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invpct_504d_base_v083_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velmax_252d_base_v084_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = b.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velmin_252d_base_v085_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = b.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velrng_252d_base_v086_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velpct_252d_base_v087_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velpct_504d_base_v088_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcv_63d_base_v089_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcv_252d_base_v090_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velcv_63d_base_v091_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velcv_252d_base_v092_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_21v252_base_v093_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_63v252_base_v094_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_63v504_base_v095_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velratio_63v252_base_v096_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velratio_63v504_base_v097_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxvolproxy_63d_base_v098_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _mean(closeadj, 63) * closeadj
    result = _mean(b, 63) * cv
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velxvolproxy_63d_base_v099_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _mean(closeadj, 63) * closeadj
    result = _mean(b, 63) * cv
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invlong_base_v100_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vellong_base_v101_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapabs_63d_base_v102_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapabs_252d_base_v103_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of gap>0
def f09isd_f09_inventory_to_sales_dynamics_excesscount_63d_base_v104_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    excess = (g > 0.05).astype(float)
    result = (excess.rolling(63, min_periods=21).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_excesscount_252d_base_v105_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    excess = (g > 0.05).astype(float)
    result = (excess.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_excesscount_504d_base_v106_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    excess = (g > 0.05).astype(float)
    result = (excess.rolling(504, min_periods=126).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cum gap (rolling sum)
def f09isd_f09_inventory_to_sales_dynamics_gapcum_63d_base_v107_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapcum_252d_base_v108_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapcum_504d_base_v109_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# z of gap 21d
def f09isd_f09_inventory_to_sales_dynamics_gapz_21d_base_v110_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# z of gap 63d
def f09isd_f09_inventory_to_sales_dynamics_gapz_63d_base_v111_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# z of gap 252d
def f09isd_f09_inventory_to_sales_dynamics_gapz_252d_base_v112_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap std 63d
def f09isd_f09_inventory_to_sales_dynamics_gapstd_63d_base_v113_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap std 252d
def f09isd_f09_inventory_to_sales_dynamics_gapstd_252d_base_v114_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales sqrt 63d
def f09isd_f09_inventory_to_sales_dynamics_invsqrt_63d_base_v115_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue).abs()
    result = np.sqrt(_mean(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity sqrt 63d
def f09isd_f09_inventory_to_sales_dynamics_velsqrt_63d_base_v116_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor).abs()
    result = np.sqrt(_mean(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity sqrt 252d
def f09isd_f09_inventory_to_sales_dynamics_velsqrt_252d_base_v117_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor).abs()
    result = np.sqrt(_mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity log 252d
def f09isd_f09_inventory_to_sales_dynamics_vellog_252d_base_v118_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sign of (inv/sales - mean) * close
def f09isd_f09_inventory_to_sales_dynamics_invsign_63d_base_v119_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    dev = b - _mean(b, 252)
    result = np.sign(dev) * _std(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity sign
def f09isd_f09_inventory_to_sales_dynamics_velsign_63d_base_v120_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    dev = b - _mean(b, 252)
    result = np.sign(dev) * _std(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite (inv/sales + velocity) * close
def f09isd_f09_inventory_to_sales_dynamics_comp_21d_base_v121_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 21) + _mean(v, 21) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite
def f09isd_f09_inventory_to_sales_dynamics_comp_63d_base_v122_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 63) + _mean(v, 63) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite
def f09isd_f09_inventory_to_sales_dynamics_comp_252d_base_v123_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 252) + _mean(v, 252) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite
def f09isd_f09_inventory_to_sales_dynamics_comp_504d_base_v124_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 504) + _mean(v, 504) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# diff (inv/sales - velocity) 63d
def f09isd_f09_inventory_to_sales_dynamics_diff_63d_base_v125_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 63) - _mean(v, 63) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# diff 252d
def f09isd_f09_inventory_to_sales_dynamics_diff_252d_base_v126_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 252) - _mean(v, 252) / 100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex of revenue alignment: gap vs cor change
def f09isd_f09_inventory_to_sales_dynamics_gapxcor_63d_base_v127_signal(inventory, revenue, cor, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    cor_g = cor.pct_change(63)
    result = g * cor_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap x cor growth
def f09isd_f09_inventory_to_sales_dynamics_gapxcor_252d_base_v128_signal(inventory, revenue, cor, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    cor_g = cor.pct_change(252)
    result = g * cor_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv growth - cor growth 63d
def f09isd_f09_inventory_to_sales_dynamics_invcorgap_63d_base_v129_signal(inventory, cor, closeadj):
    # similar to inv_revenue_gap, but use cor (cost of revenue)
    v_inv = _f09_inv_velocity(inventory, cor)  # use velocity primitive
    inv_g = inventory.pct_change(63)
    cor_g = cor.pct_change(63)
    result = (inv_g - cor_g) * closeadj + v_inv * 0
    return result.replace([np.inf, -np.inf], np.nan)


# inv growth - cor growth 252d
def f09isd_f09_inventory_to_sales_dynamics_invcorgap_252d_base_v130_signal(inventory, cor, closeadj):
    v_inv = _f09_inv_velocity(inventory, cor)
    inv_g = inventory.pct_change(252)
    cor_g = cor.pct_change(252)
    result = (inv_g - cor_g) * closeadj + v_inv * 0
    return result.replace([np.inf, -np.inf], np.nan)


# inv level normalized by revenue 63d
def f09isd_f09_inventory_to_sales_dynamics_invlevel_63d_base_v131_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv level normalized 252d
def f09isd_f09_inventory_to_sales_dynamics_invlevel_252d_base_v132_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity level normalized
def f09isd_f09_inventory_to_sales_dynamics_vellevel_63d_base_v133_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity level normalized 252d
def f09isd_f09_inventory_to_sales_dynamics_vellevel_252d_base_v134_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales * revenue (dollar value) 63d
def f09isd_f09_inventory_to_sales_dynamics_invdoll_63d_base_v135_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = b * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales * revenue 252d
def f09isd_f09_inventory_to_sales_dynamics_invdoll_252d_base_v136_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b * revenue, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap * inventory 63d
def f09isd_f09_inventory_to_sales_dynamics_gapxinv_63d_base_v137_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = g * inventory * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap * inventory 252d
def f09isd_f09_inventory_to_sales_dynamics_gapxinv_252d_base_v138_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = g * inventory * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap_z * close_ret 63d
def f09isd_f09_inventory_to_sales_dynamics_gapzxcret_63d_base_v139_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    z = _z(g, 252)
    cret = closeadj.pct_change(63)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap_z * close_ret 252d
def f09isd_f09_inventory_to_sales_dynamics_gapzxcret_252d_base_v140_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    z = _z(g, 504)
    cret = closeadj.pct_change(252)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv glut: gap>0 and inv/sales > 252d mean
def f09isd_f09_inventory_to_sales_dynamics_glut_63d_base_v141_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    glut = ((g > 0.05) & (a > _mean(a, 252))).astype(float)
    result = (glut.rolling(63, min_periods=21).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv glut 252d
def f09isd_f09_inventory_to_sales_dynamics_glut_252d_base_v142_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    glut = ((g > 0.05) & (a > _mean(a, 252))).astype(float)
    result = (glut.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv shortage 252d
def f09isd_f09_inventory_to_sales_dynamics_short_252d_base_v143_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    short = ((g < -0.05) & (a < _mean(a, 252))).astype(float)
    result = (short.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSI proxy 252d (inv/cor * 365)
def f09isd_f09_inventory_to_sales_dynamics_dsi_252d_base_v144_signal(inventory, cor, closeadj):
    b = 1.0 / _f09_inv_velocity(inventory, cor).replace(0, np.nan).abs()
    result = _mean(b, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSI 504d
def f09isd_f09_inventory_to_sales_dynamics_dsi_504d_base_v145_signal(inventory, cor, closeadj):
    b = 1.0 / _f09_inv_velocity(inventory, cor).replace(0, np.nan).abs()
    result = _mean(b, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv velocity * inv/sales (composite)
def f09isd_f09_inventory_to_sales_dynamics_velxinv_252d_base_v146_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = _mean(a * v / 100, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# vel x inv sq 63d
def f09isd_f09_inventory_to_sales_dynamics_velxinvsq_63d_base_v147_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = _mean((a * v) ** 2, 63) * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales x ret 21d composite
def f09isd_f09_inventory_to_sales_dynamics_invxret_21d_base_v148_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cret = closeadj.pct_change(21)
    result = b * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales x ret 252d
def f09isd_f09_inventory_to_sales_dynamics_invxret_252d_base_v149_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cret = closeadj.pct_change(252)
    result = b * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# global I/S composite 504d
def f09isd_f09_inventory_to_sales_dynamics_globcomp_504d_base_v150_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = (_mean(a, 504) + _mean(v, 504) / 100 + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09isd_f09_inventory_to_sales_dynamics_invmax_252d_base_v076_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmax_504d_base_v077_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmin_252d_base_v078_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmin_504d_base_v079_signal,
    f09isd_f09_inventory_to_sales_dynamics_invrng_252d_base_v080_signal,
    f09isd_f09_inventory_to_sales_dynamics_invrng_504d_base_v081_signal,
    f09isd_f09_inventory_to_sales_dynamics_invpct_252d_base_v082_signal,
    f09isd_f09_inventory_to_sales_dynamics_invpct_504d_base_v083_signal,
    f09isd_f09_inventory_to_sales_dynamics_velmax_252d_base_v084_signal,
    f09isd_f09_inventory_to_sales_dynamics_velmin_252d_base_v085_signal,
    f09isd_f09_inventory_to_sales_dynamics_velrng_252d_base_v086_signal,
    f09isd_f09_inventory_to_sales_dynamics_velpct_252d_base_v087_signal,
    f09isd_f09_inventory_to_sales_dynamics_velpct_504d_base_v088_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcv_63d_base_v089_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcv_252d_base_v090_signal,
    f09isd_f09_inventory_to_sales_dynamics_velcv_63d_base_v091_signal,
    f09isd_f09_inventory_to_sales_dynamics_velcv_252d_base_v092_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_21v252_base_v093_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_63v252_base_v094_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_63v504_base_v095_signal,
    f09isd_f09_inventory_to_sales_dynamics_velratio_63v252_base_v096_signal,
    f09isd_f09_inventory_to_sales_dynamics_velratio_63v504_base_v097_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvolproxy_63d_base_v098_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxvolproxy_63d_base_v099_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlong_base_v100_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellong_base_v101_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapabs_63d_base_v102_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapabs_252d_base_v103_signal,
    f09isd_f09_inventory_to_sales_dynamics_excesscount_63d_base_v104_signal,
    f09isd_f09_inventory_to_sales_dynamics_excesscount_252d_base_v105_signal,
    f09isd_f09_inventory_to_sales_dynamics_excesscount_504d_base_v106_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_63d_base_v107_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_252d_base_v108_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_504d_base_v109_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_21d_base_v110_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_63d_base_v111_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_252d_base_v112_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapstd_63d_base_v113_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapstd_252d_base_v114_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsqrt_63d_base_v115_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsqrt_63d_base_v116_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsqrt_252d_base_v117_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellog_252d_base_v118_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsign_63d_base_v119_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsign_63d_base_v120_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_21d_base_v121_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_63d_base_v122_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_252d_base_v123_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_504d_base_v124_signal,
    f09isd_f09_inventory_to_sales_dynamics_diff_63d_base_v125_signal,
    f09isd_f09_inventory_to_sales_dynamics_diff_252d_base_v126_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcor_63d_base_v127_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcor_252d_base_v128_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcorgap_63d_base_v129_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcorgap_252d_base_v130_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlevel_63d_base_v131_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlevel_252d_base_v132_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellevel_63d_base_v133_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellevel_252d_base_v134_signal,
    f09isd_f09_inventory_to_sales_dynamics_invdoll_63d_base_v135_signal,
    f09isd_f09_inventory_to_sales_dynamics_invdoll_252d_base_v136_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxinv_63d_base_v137_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxinv_252d_base_v138_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapzxcret_63d_base_v139_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapzxcret_252d_base_v140_signal,
    f09isd_f09_inventory_to_sales_dynamics_glut_63d_base_v141_signal,
    f09isd_f09_inventory_to_sales_dynamics_glut_252d_base_v142_signal,
    f09isd_f09_inventory_to_sales_dynamics_short_252d_base_v143_signal,
    f09isd_f09_inventory_to_sales_dynamics_dsi_252d_base_v144_signal,
    f09isd_f09_inventory_to_sales_dynamics_dsi_504d_base_v145_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxinv_252d_base_v146_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxinvsq_63d_base_v147_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxret_21d_base_v148_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxret_252d_base_v149_signal,
    f09isd_f09_inventory_to_sales_dynamics_globcomp_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_INVENTORY_TO_SALES_DYNAMICS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    inventory   = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {"closeadj": closeadj, "inventory": inventory, "revenue": revenue, "cor": cor}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_inv_sales_ratio", "_f09_inv_revenue_gap", "_f09_inv_velocity")
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
    print(f"OK f09_inventory_to_sales_dynamics_base_076_150_claude: {n_features} features pass")
