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
def _f065_invcap_ratio(ebit, invcapavg):
    return ebit / invcapavg.replace(0, np.nan).abs()


# 63d z-score of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_z_63d_base_v076_signal(roic, closeadj):
    base = roic
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_z_126d_base_v077_signal(roic, closeadj):
    base = roic
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_z_252d_base_v078_signal(roic, closeadj):
    base = roic
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_z_504d_base_v079_signal(roic, closeadj):
    base = roic
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_z_63d_base_v080_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_z_126d_base_v081_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_z_252d_base_v082_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_z_504d_base_v083_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_z_63d_base_v084_signal(invcap, closeadj):
    base = invcap
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_z_126d_base_v085_signal(invcap, closeadj):
    base = invcap
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_z_252d_base_v086_signal(invcap, closeadj):
    base = invcap
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_z_504d_base_v087_signal(invcap, closeadj):
    base = invcap
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_z_63d_base_v088_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_z_126d_base_v089_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_z_252d_base_v090_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_z_504d_base_v091_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_z_63d_base_v092_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_z_126d_base_v093_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_z_252d_base_v094_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_z_504d_base_v095_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_z_63d_base_v096_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_z_126d_base_v097_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_z_252d_base_v098_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_z_504d_base_v099_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_z_63d_base_v100_signal(ros, closeadj):
    base = ros
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_z_126d_base_v101_signal(ros, closeadj):
    base = ros
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_z_252d_base_v102_signal(ros, closeadj):
    base = ros
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_z_504d_base_v103_signal(ros, closeadj):
    base = ros
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_z_63d_base_v104_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_z_126d_base_v105_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_z_252d_base_v106_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_z_504d_base_v107_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_z_63d_base_v108_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_z_126d_base_v109_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_z_252d_base_v110_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_z_504d_base_v111_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_z_63d_base_v112_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_z_126d_base_v113_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_z_252d_base_v114_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_z_504d_base_v115_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_z_63d_base_v116_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_z_126d_base_v117_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_z_252d_base_v118_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_z_504d_base_v119_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_z_63d_base_v120_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_z_126d_base_v121_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_z_252d_base_v122_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_z_504d_base_v123_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_z_63d_base_v124_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_z_126d_base_v125_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_z_252d_base_v126_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_z_504d_base_v127_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_distmax_252d_base_v128_signal(roic, closeadj):
    base = roic
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_distmax_504d_base_v129_signal(roic, closeadj):
    base = roic
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_distmax_252d_base_v130_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_distmax_504d_base_v131_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_distmax_252d_base_v132_signal(invcap, closeadj):
    base = invcap
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_distmax_504d_base_v133_signal(invcap, closeadj):
    base = invcap
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_distmax_252d_base_v134_signal(roic, closeadj):
    base = roic.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_distmax_504d_base_v135_signal(roic, closeadj):
    base = roic.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_distmax_252d_base_v136_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_distmax_504d_base_v137_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_distmax_252d_base_v138_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_distmax_504d_base_v139_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_distmax_252d_base_v140_signal(ros, closeadj):
    base = ros
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_distmax_504d_base_v141_signal(ros, closeadj):
    base = ros
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_distmax_252d_base_v142_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_distmax_504d_base_v143_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_distmax_252d_base_v144_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_distmax_504d_base_v145_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_distmax_252d_base_v146_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_distmax_504d_base_v147_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_distmax_252d_base_v150_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_distmax_504d_base_v151_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_distmax_252d_base_v152_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_distmax_504d_base_v153_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_distmed_126d_base_v154_signal(roic, closeadj):
    base = roic
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_distmed_252d_base_v155_signal(roic, closeadj):
    base = roic
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_distmed_504d_base_v156_signal(roic, closeadj):
    base = roic
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_distmed_126d_base_v157_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_distmed_252d_base_v158_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_distmed_504d_base_v159_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_distmed_126d_base_v160_signal(invcap, closeadj):
    base = invcap
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_distmed_252d_base_v161_signal(invcap, closeadj):
    base = invcap
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_distmed_504d_base_v162_signal(invcap, closeadj):
    base = invcap
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_distmed_126d_base_v163_signal(roic, closeadj):
    base = roic.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_distmed_252d_base_v164_signal(roic, closeadj):
    base = roic.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_distmed_504d_base_v165_signal(roic, closeadj):
    base = roic.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_distmed_126d_base_v166_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_distmed_252d_base_v167_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_distmed_504d_base_v168_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_distmed_126d_base_v169_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_distmed_252d_base_v170_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_distmed_504d_base_v171_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_distmed_126d_base_v172_signal(ros, closeadj):
    base = ros
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_distmed_252d_base_v173_signal(ros, closeadj):
    base = ros
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_distmed_504d_base_v174_signal(ros, closeadj):
    base = ros
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_distmed_126d_base_v175_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

