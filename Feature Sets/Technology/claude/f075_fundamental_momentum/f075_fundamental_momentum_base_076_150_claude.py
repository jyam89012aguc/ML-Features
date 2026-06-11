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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f075_chg(s, n):
    return s.diff(periods=n)


# 63d z-score of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_z_63d_base_v076_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_z_126d_base_v077_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_z_252d_base_v078_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_z_504d_base_v079_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_z_63d_base_v080_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_z_126d_base_v081_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_z_252d_base_v082_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_z_504d_base_v083_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_z_63d_base_v084_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_z_126d_base_v085_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_z_252d_base_v086_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_z_504d_base_v087_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_z_63d_base_v088_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_z_126d_base_v089_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_z_252d_base_v090_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_z_504d_base_v091_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_z_63d_base_v092_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_z_126d_base_v093_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_z_252d_base_v094_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_z_504d_base_v095_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_z_63d_base_v096_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_z_126d_base_v097_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_z_252d_base_v098_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_z_504d_base_v099_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_z_63d_base_v100_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_z_126d_base_v101_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_z_252d_base_v102_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_z_504d_base_v103_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_z_63d_base_v104_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_z_126d_base_v105_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_z_252d_base_v106_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_z_504d_base_v107_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_z_63d_base_v108_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_z_126d_base_v109_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_z_252d_base_v110_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_z_504d_base_v111_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_z_63d_base_v112_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_z_126d_base_v113_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_z_252d_base_v114_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_z_504d_base_v115_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_z_63d_base_v116_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_z_126d_base_v117_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_z_252d_base_v118_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_z_504d_base_v119_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_z_63d_base_v120_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_z_126d_base_v121_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_z_252d_base_v122_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_z_504d_base_v123_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_z_63d_base_v124_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_z_126d_base_v125_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_z_252d_base_v126_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_z_504d_base_v127_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_z_63d_base_v128_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_z_126d_base_v129_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_z_252d_base_v130_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_z_504d_base_v131_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_distmax_252d_base_v132_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_distmax_504d_base_v133_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_distmax_252d_base_v134_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_distmax_504d_base_v135_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_distmax_252d_base_v136_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_distmax_504d_base_v137_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_distmax_252d_base_v138_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_distmax_504d_base_v139_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_distmax_252d_base_v140_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_distmax_504d_base_v141_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_distmax_252d_base_v142_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_distmax_504d_base_v143_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_distmax_252d_base_v144_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_distmax_504d_base_v145_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_distmax_252d_base_v146_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_distmax_504d_base_v147_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_distmax_252d_base_v148_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_distmax_504d_base_v149_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_distmax_252d_base_v150_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_distmax_504d_base_v151_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_distmax_252d_base_v152_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_distmax_504d_base_v153_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_distmax_252d_base_v154_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_distmax_504d_base_v155_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_distmax_252d_base_v156_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_distmax_504d_base_v157_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_distmax_252d_base_v158_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_distmax_504d_base_v159_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_distmed_126d_base_v160_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_distmed_252d_base_v161_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_distmed_504d_base_v162_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_distmed_126d_base_v163_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_distmed_252d_base_v164_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_distmed_504d_base_v165_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_distmed_126d_base_v166_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_distmed_252d_base_v167_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_distmed_504d_base_v168_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_distmed_126d_base_v169_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_distmed_252d_base_v170_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_distmed_504d_base_v171_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_distmed_126d_base_v172_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_distmed_252d_base_v173_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_distmed_504d_base_v174_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_distmed_126d_base_v175_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

