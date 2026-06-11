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


# 21d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slope_21d_2d_v001_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slope_63d_2d_v002_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slope_126d_2d_v003_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slope_252d_2d_v004_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_slope_504d_2d_v005_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slope_21d_2d_v006_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slope_63d_2d_v007_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slope_126d_2d_v008_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slope_252d_2d_v009_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_slope_504d_2d_v010_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slope_21d_2d_v011_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slope_63d_2d_v012_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slope_126d_2d_v013_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slope_252d_2d_v014_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_slope_504d_2d_v015_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slope_21d_2d_v016_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slope_63d_2d_v017_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slope_126d_2d_v018_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slope_252d_2d_v019_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_slope_504d_2d_v020_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slope_21d_2d_v021_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slope_63d_2d_v022_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slope_126d_2d_v023_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slope_252d_2d_v024_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_slope_504d_2d_v025_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slope_21d_2d_v026_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slope_63d_2d_v027_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slope_126d_2d_v028_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slope_252d_2d_v029_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_slope_504d_2d_v030_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slope_21d_2d_v031_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slope_63d_2d_v032_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slope_126d_2d_v033_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slope_252d_2d_v034_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_slope_504d_2d_v035_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slope_21d_2d_v036_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slope_63d_2d_v037_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slope_126d_2d_v038_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slope_252d_2d_v039_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_slope_504d_2d_v040_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slope_21d_2d_v041_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slope_63d_2d_v042_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slope_126d_2d_v043_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slope_252d_2d_v044_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_slope_504d_2d_v045_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slope_21d_2d_v046_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slope_63d_2d_v047_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slope_126d_2d_v048_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slope_252d_2d_v049_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_slope_504d_2d_v050_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slope_21d_2d_v051_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slope_63d_2d_v052_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slope_126d_2d_v053_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slope_252d_2d_v054_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_slope_504d_2d_v055_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slope_21d_2d_v056_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slope_63d_2d_v057_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slope_126d_2d_v058_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slope_252d_2d_v059_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_slope_504d_2d_v060_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slope_21d_2d_v061_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slope_63d_2d_v062_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slope_126d_2d_v063_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slope_252d_2d_v064_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_slope_504d_2d_v065_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slope_21d_2d_v066_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slope_63d_2d_v067_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slope_126d_2d_v068_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slope_252d_2d_v069_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_slope_504d_2d_v070_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sm21_sl21_2d_v071_signal(revenue, closeadj):
    base = _mean(_f075_chg(revenue, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sm63_sl21_2d_v072_signal(revenue, closeadj):
    base = _mean(_f075_chg(revenue, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sm63_sl63_2d_v073_signal(revenue, closeadj):
    base = _mean(_f075_chg(revenue, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sm252_sl63_2d_v074_signal(revenue, closeadj):
    base = _mean(_f075_chg(revenue, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sm252_sl126_2d_v075_signal(revenue, closeadj):
    base = _mean(_f075_chg(revenue, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sm21_sl21_2d_v076_signal(rnd, closeadj):
    base = _mean(_f075_chg(rnd, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sm63_sl21_2d_v077_signal(rnd, closeadj):
    base = _mean(_f075_chg(rnd, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sm63_sl63_2d_v078_signal(rnd, closeadj):
    base = _mean(_f075_chg(rnd, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sm252_sl63_2d_v079_signal(rnd, closeadj):
    base = _mean(_f075_chg(rnd, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sm252_sl126_2d_v080_signal(rnd, closeadj):
    base = _mean(_f075_chg(rnd, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sm21_sl21_2d_v081_signal(ncfo, closeadj):
    base = _mean(_f075_chg(ncfo, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sm63_sl21_2d_v082_signal(ncfo, closeadj):
    base = _mean(_f075_chg(ncfo, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sm63_sl63_2d_v083_signal(ncfo, closeadj):
    base = _mean(_f075_chg(ncfo, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sm252_sl63_2d_v084_signal(ncfo, closeadj):
    base = _mean(_f075_chg(ncfo, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sm252_sl126_2d_v085_signal(ncfo, closeadj):
    base = _mean(_f075_chg(ncfo, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sm21_sl21_2d_v086_signal(revenue, fcf, closeadj):
    base = _mean(revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sm63_sl21_2d_v087_signal(revenue, fcf, closeadj):
    base = _mean(revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sm63_sl63_2d_v088_signal(revenue, fcf, closeadj):
    base = _mean(revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sm252_sl63_2d_v089_signal(revenue, fcf, closeadj):
    base = _mean(revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sm252_sl126_2d_v090_signal(revenue, fcf, closeadj):
    base = _mean(revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sm21_sl21_2d_v091_signal(revenue, ncfo, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sm63_sl21_2d_v092_signal(revenue, ncfo, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sm63_sl63_2d_v093_signal(revenue, ncfo, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sm252_sl63_2d_v094_signal(revenue, ncfo, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sm252_sl126_2d_v095_signal(revenue, ncfo, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sm21_sl21_2d_v096_signal(revenue, ebitda, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sm63_sl21_2d_v097_signal(revenue, ebitda, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sm63_sl63_2d_v098_signal(revenue, ebitda, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sm252_sl63_2d_v099_signal(revenue, ebitda, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sm252_sl126_2d_v100_signal(revenue, ebitda, closeadj):
    base = _mean(revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_sm21_sl21_2d_v101_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = _mean(((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_sm63_sl21_2d_v102_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = _mean(((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_sm63_sl63_2d_v103_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = _mean(((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_sm252_sl63_2d_v104_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = _mean(((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_sm252_sl126_2d_v105_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = _mean(((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_sm21_sl21_2d_v106_signal(revenue, fcf, gp, closeadj):
    base = _mean((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_sm63_sl21_2d_v107_signal(revenue, fcf, gp, closeadj):
    base = _mean((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_sm63_sl63_2d_v108_signal(revenue, fcf, gp, closeadj):
    base = _mean((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_sm252_sl63_2d_v109_signal(revenue, fcf, gp, closeadj):
    base = _mean((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_sm252_sl126_2d_v110_signal(revenue, fcf, gp, closeadj):
    base = _mean((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_sm21_sl21_2d_v111_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_sm63_sl21_2d_v112_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_sm63_sl63_2d_v113_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_sm252_sl63_2d_v114_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_sm252_sl126_2d_v115_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_sm21_sl21_2d_v116_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_sm63_sl21_2d_v117_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_sm63_sl63_2d_v118_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_sm252_sl63_2d_v119_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_sm252_sl126_2d_v120_signal(revenue, fcf, closeadj):
    base = _mean(((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_sm21_sl21_2d_v121_signal(gp, revenue, closeadj):
    base = _mean((gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_sm63_sl21_2d_v122_signal(gp, revenue, closeadj):
    base = _mean((gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_sm63_sl63_2d_v123_signal(gp, revenue, closeadj):
    base = _mean((gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_sm252_sl63_2d_v124_signal(gp, revenue, closeadj):
    base = _mean((gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_sm252_sl126_2d_v125_signal(gp, revenue, closeadj):
    base = _mean((gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_sm21_sl21_2d_v126_signal(fcf, revenue, roic, closeadj):
    base = _mean((fcf / revenue.abs().replace(0, np.nan)) * roic, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_sm63_sl21_2d_v127_signal(fcf, revenue, roic, closeadj):
    base = _mean((fcf / revenue.abs().replace(0, np.nan)) * roic, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_sm63_sl63_2d_v128_signal(fcf, revenue, roic, closeadj):
    base = _mean((fcf / revenue.abs().replace(0, np.nan)) * roic, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_sm252_sl63_2d_v129_signal(fcf, revenue, roic, closeadj):
    base = _mean((fcf / revenue.abs().replace(0, np.nan)) * roic, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_sm252_sl126_2d_v130_signal(fcf, revenue, roic, closeadj):
    base = _mean((fcf / revenue.abs().replace(0, np.nan)) * roic, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_sm21_sl21_2d_v131_signal(revenue, closeadj):
    base = _mean(((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_sm63_sl21_2d_v132_signal(revenue, closeadj):
    base = _mean(((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_sm63_sl63_2d_v133_signal(revenue, closeadj):
    base = _mean(((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_sm252_sl63_2d_v134_signal(revenue, closeadj):
    base = _mean(((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_sm252_sl126_2d_v135_signal(revenue, closeadj):
    base = _mean(((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_sm21_sl21_2d_v136_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = _mean(((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_sm63_sl21_2d_v137_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = _mean(((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_sm63_sl63_2d_v138_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = _mean(((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_sm252_sl63_2d_v139_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = _mean(((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_sm252_sl126_2d_v140_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = _mean(((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_pctslope_21d_2d_v141_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_pctslope_63d_2d_v142_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_pctslope_252d_2d_v143_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_pctslope_21d_2d_v144_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_pctslope_63d_2d_v145_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_pctslope_252d_2d_v146_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_pctslope_21d_2d_v147_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_pctslope_63d_2d_v148_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_pctslope_252d_2d_v149_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_pctslope_21d_2d_v150_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_pctslope_63d_2d_v151_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_pctslope_252d_2d_v152_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_pctslope_21d_2d_v153_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_pctslope_63d_2d_v154_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_pctslope_252d_2d_v155_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_pctslope_21d_2d_v156_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_pctslope_63d_2d_v157_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_pctslope_252d_2d_v158_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_pctslope_21d_2d_v159_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_pctslope_63d_2d_v160_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_pctslope_252d_2d_v161_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_pctslope_21d_2d_v162_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_pctslope_63d_2d_v163_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_pctslope_252d_2d_v164_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_pctslope_21d_2d_v165_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_pctslope_63d_2d_v166_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_pctslope_252d_2d_v167_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_pctslope_21d_2d_v168_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_pctslope_63d_2d_v169_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_pctslope_252d_2d_v170_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_pctslope_21d_2d_v171_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_pctslope_63d_2d_v172_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_x_revgrowth
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_pctslope_252d_2d_v173_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_pctslope_21d_2d_v174_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_pctslope_63d_2d_v175_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of fcfm_x_roic
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_pctslope_252d_2d_v176_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_pctslope_21d_2d_v177_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_pctslope_63d_2d_v178_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of growth_decel_flag
def f075fmm_f075_fundamental_momentum_growth_decel_flag_pctslope_252d_2d_v179_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_pctslope_21d_2d_v180_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_pctslope_63d_2d_v181_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of improving_breadth_q
def f075fmm_f075_fundamental_momentum_improving_breadth_q_pctslope_252d_2d_v182_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sgnslope_21d_2d_v183_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sgnslope_63d_2d_v184_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_sgnslope_252d_2d_v185_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sgnslope_21d_2d_v186_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sgnslope_63d_2d_v187_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_sgnslope_252d_2d_v188_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sgnslope_21d_2d_v189_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sgnslope_63d_2d_v190_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_sgnslope_252d_2d_v191_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sgnslope_21d_2d_v192_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sgnslope_63d_2d_v193_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_sgnslope_252d_2d_v194_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sgnslope_21d_2d_v195_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sgnslope_63d_2d_v196_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_sgnslope_252d_2d_v197_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sgnslope_21d_2d_v198_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sgnslope_63d_2d_v199_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_sgnslope_252d_2d_v200_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

