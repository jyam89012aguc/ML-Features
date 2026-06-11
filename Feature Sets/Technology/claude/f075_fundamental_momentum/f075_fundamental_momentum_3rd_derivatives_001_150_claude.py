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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f075_chg(s, n):
    return s.diff(periods=n)


# 21d acceleration of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accel_21d_3d_v001_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accel_63d_3d_v002_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accel_126d_3d_v003_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accel_252d_3d_v004_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accel_21d_3d_v005_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accel_63d_3d_v006_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accel_126d_3d_v007_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accel_252d_3d_v008_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accel_21d_3d_v009_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accel_63d_3d_v010_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accel_126d_3d_v011_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accel_252d_3d_v012_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accel_21d_3d_v013_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accel_63d_3d_v014_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accel_126d_3d_v015_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accel_252d_3d_v016_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accel_21d_3d_v017_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accel_63d_3d_v018_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accel_126d_3d_v019_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accel_252d_3d_v020_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accel_21d_3d_v021_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accel_63d_3d_v022_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accel_126d_3d_v023_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accel_252d_3d_v024_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accel_21d_3d_v025_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accel_63d_3d_v026_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accel_126d_3d_v027_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accel_252d_3d_v028_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accel_21d_3d_v029_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accel_63d_3d_v030_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accel_126d_3d_v031_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accel_252d_3d_v032_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accel_21d_3d_v033_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accel_63d_3d_v034_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accel_126d_3d_v035_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accel_252d_3d_v036_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_accel_21d_3d_v037_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_accel_63d_3d_v038_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_accel_126d_3d_v039_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_accel_252d_3d_v040_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_accel_21d_3d_v041_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_accel_63d_3d_v042_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_accel_126d_3d_v043_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_accel_252d_3d_v044_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_accel_21d_3d_v045_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_accel_63d_3d_v046_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_accel_126d_3d_v047_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_accel_252d_3d_v048_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_accel_21d_3d_v049_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_accel_63d_3d_v050_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_accel_126d_3d_v051_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_accel_252d_3d_v052_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_accel_21d_3d_v053_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_accel_63d_3d_v054_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_accel_126d_3d_v055_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_accel_252d_3d_v056_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slopez_21d_z126_3d_v057_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slopez_63d_z252_3d_v058_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slopez_126d_z252_3d_v059_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slopez_252d_z504_3d_v060_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slopez_21d_z126_3d_v061_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slopez_63d_z252_3d_v062_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slopez_126d_z252_3d_v063_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slopez_252d_z504_3d_v064_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slopez_21d_z126_3d_v065_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slopez_63d_z252_3d_v066_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slopez_126d_z252_3d_v067_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slopez_252d_z504_3d_v068_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slopez_21d_z126_3d_v069_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slopez_63d_z252_3d_v070_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slopez_126d_z252_3d_v071_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slopez_252d_z504_3d_v072_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slopez_21d_z126_3d_v073_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slopez_63d_z252_3d_v074_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slopez_126d_z252_3d_v075_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slopez_252d_z504_3d_v076_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slopez_21d_z126_3d_v077_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slopez_63d_z252_3d_v078_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slopez_126d_z252_3d_v079_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slopez_252d_z504_3d_v080_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slopez_21d_z126_3d_v081_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slopez_63d_z252_3d_v082_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slopez_126d_z252_3d_v083_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slopez_252d_z504_3d_v084_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slopez_21d_z126_3d_v085_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slopez_63d_z252_3d_v086_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slopez_126d_z252_3d_v087_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slopez_252d_z504_3d_v088_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slopez_21d_z126_3d_v089_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slopez_63d_z252_3d_v090_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slopez_126d_z252_3d_v091_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slopez_252d_z504_3d_v092_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slopez_21d_z126_3d_v093_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slopez_63d_z252_3d_v094_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slopez_126d_z252_3d_v095_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slopez_252d_z504_3d_v096_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slopez_21d_z126_3d_v097_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slopez_63d_z252_3d_v098_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slopez_126d_z252_3d_v099_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slopez_252d_z504_3d_v100_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slopez_21d_z126_3d_v101_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slopez_63d_z252_3d_v102_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slopez_126d_z252_3d_v103_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slopez_252d_z504_3d_v104_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slopez_21d_z126_3d_v105_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slopez_63d_z252_3d_v106_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slopez_126d_z252_3d_v107_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slopez_252d_z504_3d_v108_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slopez_21d_z126_3d_v109_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slopez_63d_z252_3d_v110_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slopez_126d_z252_3d_v111_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slopez_252d_z504_3d_v112_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_jerk_21d_3d_v113_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_jerk_63d_3d_v114_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_jerk_126d_3d_v115_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_jerk_21d_3d_v116_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_jerk_63d_3d_v117_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_jerk_126d_3d_v118_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_jerk_21d_3d_v119_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_jerk_63d_3d_v120_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_jerk_126d_3d_v121_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_jerk_21d_3d_v122_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_jerk_63d_3d_v123_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_jerk_126d_3d_v124_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_jerk_21d_3d_v125_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_jerk_63d_3d_v126_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_jerk_126d_3d_v127_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_jerk_21d_3d_v128_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_jerk_63d_3d_v129_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_jerk_126d_3d_v130_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_jerk_21d_3d_v131_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_jerk_63d_3d_v132_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_jerk_126d_3d_v133_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_jerk_21d_3d_v134_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_jerk_63d_3d_v135_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_jerk_126d_3d_v136_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_jerk_21d_3d_v137_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_jerk_63d_3d_v138_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_jerk_126d_3d_v139_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_jerk_21d_3d_v140_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_jerk_63d_3d_v141_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_jerk_126d_3d_v142_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_jerk_21d_3d_v143_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_jerk_63d_3d_v144_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_jerk_126d_3d_v145_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_jerk_21d_3d_v146_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_jerk_63d_3d_v147_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_jerk_126d_3d_v148_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_jerk_21d_3d_v149_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_jerk_63d_3d_v150_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_jerk_126d_3d_v151_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_jerk_21d_3d_v152_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_jerk_63d_3d_v153_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_jerk_126d_3d_v154_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_mom_y smoothed over 252d
def f075fmm_f075_fundamental_momentum_rev_mom_y_smoothaccel_63d_sm252_3d_v155_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_mom_y smoothed over 504d
def f075fmm_f075_fundamental_momentum_rev_mom_y_smoothaccel_252d_sm504_3d_v156_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_mom_y smoothed over 252d
def f075fmm_f075_fundamental_momentum_rnd_mom_y_smoothaccel_63d_sm252_3d_v157_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_mom_y smoothed over 504d
def f075fmm_f075_fundamental_momentum_rnd_mom_y_smoothaccel_252d_sm504_3d_v158_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_mom_y smoothed over 252d
def f075fmm_f075_fundamental_momentum_ocf_mom_y_smoothaccel_63d_sm252_3d_v159_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_mom_y smoothed over 504d
def f075fmm_f075_fundamental_momentum_ocf_mom_y_smoothaccel_252d_sm504_3d_v160_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rule_of_40 smoothed over 252d
def f075fmm_f075_fundamental_momentum_rule_of_40_smoothaccel_63d_sm252_3d_v161_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rule_of_40 smoothed over 504d
def f075fmm_f075_fundamental_momentum_rule_of_40_smoothaccel_252d_sm504_3d_v162_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rule_of_40_ocf smoothed over 252d
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_smoothaccel_63d_sm252_3d_v163_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rule_of_40_ocf smoothed over 504d
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_smoothaccel_252d_sm504_3d_v164_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rule_of_40_ebitda smoothed over 252d
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_smoothaccel_63d_sm252_3d_v165_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rule_of_40_ebitda smoothed over 504d
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_smoothaccel_252d_sm504_3d_v166_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of composite_up_count smoothed over 252d
def f075fmm_f075_fundamental_momentum_composite_up_count_smoothaccel_63d_sm252_3d_v167_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of composite_up_count smoothed over 504d
def f075fmm_f075_fundamental_momentum_composite_up_count_smoothaccel_252d_sm504_3d_v168_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of quality_of_40 smoothed over 252d
def f075fmm_f075_fundamental_momentum_quality_of_40_smoothaccel_63d_sm252_3d_v169_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of quality_of_40 smoothed over 504d
def f075fmm_f075_fundamental_momentum_quality_of_40_smoothaccel_252d_sm504_3d_v170_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rule_of_40_passes smoothed over 252d
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_smoothaccel_63d_sm252_3d_v171_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rule_of_40_passes smoothed over 504d
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_smoothaccel_252d_sm504_3d_v172_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rule_of_40_persistent_4q smoothed over 252d
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_smoothaccel_63d_sm252_3d_v173_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rule_of_40_persistent_4q smoothed over 504d
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_smoothaccel_252d_sm504_3d_v174_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_x_revgrowth smoothed over 252d
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_smoothaccel_63d_sm252_3d_v175_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_x_revgrowth smoothed over 504d
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_smoothaccel_252d_sm504_3d_v176_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcfm_x_roic smoothed over 252d
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_smoothaccel_63d_sm252_3d_v177_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcfm_x_roic smoothed over 504d
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_smoothaccel_252d_sm504_3d_v178_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of growth_decel_flag smoothed over 252d
def f075fmm_f075_fundamental_momentum_growth_decel_flag_smoothaccel_63d_sm252_3d_v179_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of growth_decel_flag smoothed over 504d
def f075fmm_f075_fundamental_momentum_growth_decel_flag_smoothaccel_252d_sm504_3d_v180_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of improving_breadth_q smoothed over 252d
def f075fmm_f075_fundamental_momentum_improving_breadth_q_smoothaccel_63d_sm252_3d_v181_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of improving_breadth_q smoothed over 504d
def f075fmm_f075_fundamental_momentum_improving_breadth_q_smoothaccel_252d_sm504_3d_v182_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accelz_21d_z252_3d_v183_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_accelz_63d_z504_3d_v184_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accelz_21d_z252_3d_v185_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_accelz_63d_z504_3d_v186_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accelz_21d_z252_3d_v187_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_accelz_63d_z504_3d_v188_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accelz_21d_z252_3d_v189_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_accelz_63d_z504_3d_v190_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accelz_21d_z252_3d_v191_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_accelz_63d_z504_3d_v192_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accelz_21d_z252_3d_v193_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_accelz_63d_z504_3d_v194_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accelz_21d_z252_3d_v195_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_accelz_63d_z504_3d_v196_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accelz_21d_z252_3d_v197_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_accelz_63d_z504_3d_v198_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accelz_21d_z252_3d_v199_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_accelz_63d_z504_3d_v200_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

