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


# 21d mean of rev_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rev_mom_y_mean_21d_base_v001_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rev_mom_y_mean_63d_base_v002_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rev_mom_y_mean_126d_base_v003_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rev_mom_y_mean_252d_base_v004_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rev_mom_y_mean_504d_base_v005_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rnd_mom_y_mean_21d_base_v006_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rnd_mom_y_mean_63d_base_v007_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rnd_mom_y_mean_126d_base_v008_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rnd_mom_y_mean_252d_base_v009_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_rnd_mom_y_mean_504d_base_v010_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_ocf_mom_y_mean_21d_base_v011_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_ocf_mom_y_mean_63d_base_v012_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_ocf_mom_y_mean_126d_base_v013_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_ocf_mom_y_mean_252d_base_v014_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_mom_y scaled by closeadj
def f075fmm_f075_fundamental_momentum_ocf_mom_y_mean_504d_base_v015_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rule_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_mean_21d_base_v016_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rule_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_mean_63d_base_v017_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rule_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_mean_126d_base_v018_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rule_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_mean_252d_base_v019_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rule_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_mean_504d_base_v020_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rule_of_40_ocf scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_mean_21d_base_v021_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rule_of_40_ocf scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_mean_63d_base_v022_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rule_of_40_ocf scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_mean_126d_base_v023_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rule_of_40_ocf scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_mean_252d_base_v024_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rule_of_40_ocf scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_mean_504d_base_v025_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rule_of_40_ebitda scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_mean_21d_base_v026_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rule_of_40_ebitda scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_mean_63d_base_v027_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rule_of_40_ebitda scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_mean_126d_base_v028_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rule_of_40_ebitda scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_mean_252d_base_v029_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rule_of_40_ebitda scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_mean_504d_base_v030_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of composite_up_count scaled by closeadj
def f075fmm_f075_fundamental_momentum_composite_up_count_mean_21d_base_v031_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of composite_up_count scaled by closeadj
def f075fmm_f075_fundamental_momentum_composite_up_count_mean_63d_base_v032_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of composite_up_count scaled by closeadj
def f075fmm_f075_fundamental_momentum_composite_up_count_mean_126d_base_v033_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of composite_up_count scaled by closeadj
def f075fmm_f075_fundamental_momentum_composite_up_count_mean_252d_base_v034_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of composite_up_count scaled by closeadj
def f075fmm_f075_fundamental_momentum_composite_up_count_mean_504d_base_v035_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of quality_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_quality_of_40_mean_21d_base_v036_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of quality_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_quality_of_40_mean_63d_base_v037_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of quality_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_quality_of_40_mean_126d_base_v038_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of quality_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_quality_of_40_mean_252d_base_v039_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of quality_of_40 scaled by closeadj
def f075fmm_f075_fundamental_momentum_quality_of_40_mean_504d_base_v040_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rule_of_40_passes scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_mean_21d_base_v041_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rule_of_40_passes scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_mean_63d_base_v042_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rule_of_40_passes scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_mean_126d_base_v043_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rule_of_40_passes scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_mean_252d_base_v044_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rule_of_40_passes scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_mean_504d_base_v045_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rule_of_40_persistent_4q scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_mean_21d_base_v046_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rule_of_40_persistent_4q scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_mean_63d_base_v047_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rule_of_40_persistent_4q scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_mean_126d_base_v048_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rule_of_40_persistent_4q scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_mean_252d_base_v049_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rule_of_40_persistent_4q scaled by closeadj
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_mean_504d_base_v050_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_x_revgrowth scaled by closeadj
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_mean_21d_base_v051_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_x_revgrowth scaled by closeadj
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_mean_63d_base_v052_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_x_revgrowth scaled by closeadj
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_mean_126d_base_v053_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_x_revgrowth scaled by closeadj
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_mean_252d_base_v054_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_x_revgrowth scaled by closeadj
def f075fmm_f075_fundamental_momentum_gm_x_revgrowth_mean_504d_base_v055_signal(gp, revenue, closeadj):
    base = (gp / revenue.replace(0, np.nan).abs()) * revenue.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_x_roic scaled by closeadj
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_mean_21d_base_v056_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_x_roic scaled by closeadj
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_mean_63d_base_v057_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_x_roic scaled by closeadj
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_mean_126d_base_v058_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_x_roic scaled by closeadj
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_mean_252d_base_v059_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_x_roic scaled by closeadj
def f075fmm_f075_fundamental_momentum_fcfm_x_roic_mean_504d_base_v060_signal(fcf, revenue, roic, closeadj):
    base = (fcf / revenue.abs().replace(0, np.nan)) * roic
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of growth_decel_flag scaled by closeadj
def f075fmm_f075_fundamental_momentum_growth_decel_flag_mean_21d_base_v061_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of growth_decel_flag scaled by closeadj
def f075fmm_f075_fundamental_momentum_growth_decel_flag_mean_63d_base_v062_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of growth_decel_flag scaled by closeadj
def f075fmm_f075_fundamental_momentum_growth_decel_flag_mean_126d_base_v063_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of growth_decel_flag scaled by closeadj
def f075fmm_f075_fundamental_momentum_growth_decel_flag_mean_252d_base_v064_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of growth_decel_flag scaled by closeadj
def f075fmm_f075_fundamental_momentum_growth_decel_flag_mean_504d_base_v065_signal(revenue, closeadj):
    base = ((revenue.pct_change(periods=252) > 0.50) & (revenue.pct_change(periods=63) < revenue.pct_change(periods=252) * 0.5)).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of improving_breadth_q scaled by closeadj
def f075fmm_f075_fundamental_momentum_improving_breadth_q_mean_21d_base_v066_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of improving_breadth_q scaled by closeadj
def f075fmm_f075_fundamental_momentum_improving_breadth_q_mean_63d_base_v067_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of improving_breadth_q scaled by closeadj
def f075fmm_f075_fundamental_momentum_improving_breadth_q_mean_126d_base_v068_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of improving_breadth_q scaled by closeadj
def f075fmm_f075_fundamental_momentum_improving_breadth_q_mean_252d_base_v069_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of improving_breadth_q scaled by closeadj
def f075fmm_f075_fundamental_momentum_improving_breadth_q_mean_504d_base_v070_signal(revenue, gp, ncfo, fcf, opinc, closeadj):
    base = ((revenue.diff(periods=63) > 0).astype(float) + (gp.diff(periods=63) > 0).astype(float) + (ncfo.diff(periods=63) > 0).astype(float) + (fcf.diff(periods=63) > 0).astype(float) + (opinc.diff(periods=63) > 0).astype(float))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_median_63d_base_v071_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_median_252d_base_v072_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_mom_y
def f075fmm_f075_fundamental_momentum_rev_mom_y_median_504d_base_v073_signal(revenue, closeadj):
    base = _f075_chg(revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_median_63d_base_v074_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_median_252d_base_v075_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_mom_y
def f075fmm_f075_fundamental_momentum_rnd_mom_y_median_504d_base_v076_signal(rnd, closeadj):
    base = _f075_chg(rnd, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_median_63d_base_v077_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_median_252d_base_v078_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_mom_y
def f075fmm_f075_fundamental_momentum_ocf_mom_y_median_504d_base_v079_signal(ncfo, closeadj):
    base = _f075_chg(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_median_63d_base_v080_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_median_252d_base_v081_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rule_of_40
def f075fmm_f075_fundamental_momentum_rule_of_40_median_504d_base_v082_signal(revenue, fcf, closeadj):
    base = revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_median_63d_base_v083_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_median_252d_base_v084_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rule_of_40_ocf
def f075fmm_f075_fundamental_momentum_rule_of_40_ocf_median_504d_base_v085_signal(revenue, ncfo, closeadj):
    base = revenue.pct_change(periods=252) + ncfo/revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_median_63d_base_v086_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_median_252d_base_v087_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rule_of_40_ebitda
def f075fmm_f075_fundamental_momentum_rule_of_40_ebitda_median_504d_base_v088_signal(revenue, ebitda, closeadj):
    base = revenue.pct_change(periods=252) + ebitda/revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_median_63d_base_v089_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_median_252d_base_v090_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of composite_up_count
def f075fmm_f075_fundamental_momentum_composite_up_count_median_504d_base_v091_signal(revenue, ncfo, fcf, opinc, closeadj):
    base = ((_f075_chg(revenue, 252) > 0).astype(float) + (_f075_chg(ncfo, 252) > 0).astype(float) + (_f075_chg(fcf, 252) > 0).astype(float) + (_f075_chg(opinc, 252) > 0).astype(float))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_median_63d_base_v092_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_median_252d_base_v093_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of quality_of_40
def f075fmm_f075_fundamental_momentum_quality_of_40_median_504d_base_v094_signal(revenue, fcf, gp, closeadj):
    base = (revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) * (gp / revenue.replace(0, np.nan).abs())
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_median_63d_base_v095_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_median_252d_base_v096_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rule_of_40_passes
def f075fmm_f075_fundamental_momentum_rule_of_40_passes_median_504d_base_v097_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_median_63d_base_v098_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_median_252d_base_v099_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rule_of_40_persistent_4q
def f075fmm_f075_fundamental_momentum_rule_of_40_persistent_4q_median_504d_base_v100_signal(revenue, fcf, closeadj):
    base = ((revenue.pct_change(periods=252) + fcf/revenue.abs().replace(0, np.nan)) > 0.40).astype(float).rolling(252, min_periods=63).min()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

