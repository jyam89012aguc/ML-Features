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
def _f065_invcap_ratio(ebit, invcapavg):
    return ebit / invcapavg.replace(0, np.nan).abs()


# 21d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_slope_21d_2d_v001_signal(roic, closeadj):
    base = roic
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_slope_63d_2d_v002_signal(roic, closeadj):
    base = roic
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_slope_126d_2d_v003_signal(roic, closeadj):
    base = roic
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_slope_252d_2d_v004_signal(roic, closeadj):
    base = roic
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_slope_504d_2d_v005_signal(roic, closeadj):
    base = roic
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_slope_21d_2d_v006_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_slope_63d_2d_v007_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_slope_126d_2d_v008_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_slope_252d_2d_v009_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_slope_504d_2d_v010_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_slope_21d_2d_v011_signal(invcap, closeadj):
    base = invcap
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_slope_63d_2d_v012_signal(invcap, closeadj):
    base = invcap
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_slope_126d_2d_v013_signal(invcap, closeadj):
    base = invcap
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_slope_252d_2d_v014_signal(invcap, closeadj):
    base = invcap
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_slope_504d_2d_v015_signal(invcap, closeadj):
    base = invcap
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_slope_21d_2d_v016_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_slope_63d_2d_v017_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_slope_126d_2d_v018_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_slope_252d_2d_v019_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_slope_504d_2d_v020_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_slope_21d_2d_v021_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_slope_63d_2d_v022_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_slope_126d_2d_v023_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_slope_252d_2d_v024_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_slope_504d_2d_v025_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_slope_21d_2d_v026_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_slope_63d_2d_v027_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_slope_126d_2d_v028_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_slope_252d_2d_v029_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_slope_504d_2d_v030_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_slope_21d_2d_v031_signal(ros, closeadj):
    base = ros
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_slope_63d_2d_v032_signal(ros, closeadj):
    base = ros
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_slope_126d_2d_v033_signal(ros, closeadj):
    base = ros
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_slope_252d_2d_v034_signal(ros, closeadj):
    base = ros
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_slope_504d_2d_v035_signal(ros, closeadj):
    base = ros
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_slope_21d_2d_v036_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_slope_63d_2d_v037_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_slope_126d_2d_v038_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_slope_252d_2d_v039_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_slope_504d_2d_v040_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_slope_21d_2d_v041_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_slope_63d_2d_v042_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_slope_126d_2d_v043_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_slope_252d_2d_v044_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_slope_504d_2d_v045_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_slope_21d_2d_v046_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_slope_63d_2d_v047_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_slope_126d_2d_v048_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_slope_252d_2d_v049_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_slope_504d_2d_v050_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_slope_21d_2d_v056_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_slope_63d_2d_v057_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_slope_126d_2d_v058_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_slope_252d_2d_v059_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_slope_504d_2d_v060_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_slope_21d_2d_v061_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_slope_63d_2d_v062_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_slope_126d_2d_v063_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_slope_252d_2d_v064_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_slope_504d_2d_v065_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sm21_sl21_2d_v066_signal(roic, closeadj):
    base = _mean(roic, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sm63_sl21_2d_v067_signal(roic, closeadj):
    base = _mean(roic, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sm63_sl63_2d_v068_signal(roic, closeadj):
    base = _mean(roic, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sm252_sl63_2d_v069_signal(roic, closeadj):
    base = _mean(roic, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sm252_sl126_2d_v070_signal(roic, closeadj):
    base = _mean(roic, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sm21_sl21_2d_v071_signal(ebit, invcapavg, closeadj):
    base = _mean(_f065_invcap_ratio(ebit, invcapavg), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sm63_sl21_2d_v072_signal(ebit, invcapavg, closeadj):
    base = _mean(_f065_invcap_ratio(ebit, invcapavg), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sm63_sl63_2d_v073_signal(ebit, invcapavg, closeadj):
    base = _mean(_f065_invcap_ratio(ebit, invcapavg), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sm252_sl63_2d_v074_signal(ebit, invcapavg, closeadj):
    base = _mean(_f065_invcap_ratio(ebit, invcapavg), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sm252_sl126_2d_v075_signal(ebit, invcapavg, closeadj):
    base = _mean(_f065_invcap_ratio(ebit, invcapavg), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sm21_sl21_2d_v076_signal(invcap, closeadj):
    base = _mean(invcap, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sm63_sl21_2d_v077_signal(invcap, closeadj):
    base = _mean(invcap, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sm63_sl63_2d_v078_signal(invcap, closeadj):
    base = _mean(invcap, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sm252_sl63_2d_v079_signal(invcap, closeadj):
    base = _mean(invcap, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sm252_sl126_2d_v080_signal(invcap, closeadj):
    base = _mean(invcap, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sm21_sl21_2d_v081_signal(roic, closeadj):
    base = _mean(roic.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sm63_sl21_2d_v082_signal(roic, closeadj):
    base = _mean(roic.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sm63_sl63_2d_v083_signal(roic, closeadj):
    base = _mean(roic.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sm252_sl63_2d_v084_signal(roic, closeadj):
    base = _mean(roic.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sm252_sl126_2d_v085_signal(roic, closeadj):
    base = _mean(roic.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sm21_sl21_2d_v086_signal(roic, closeadj):
    base = _mean(roic.rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sm63_sl21_2d_v087_signal(roic, closeadj):
    base = _mean(roic.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sm63_sl63_2d_v088_signal(roic, closeadj):
    base = _mean(roic.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sm252_sl63_2d_v089_signal(roic, closeadj):
    base = _mean(roic.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sm252_sl126_2d_v090_signal(roic, closeadj):
    base = _mean(roic.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sm21_sl21_2d_v091_signal(invcap, closeadj):
    base = _mean(invcap.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sm63_sl21_2d_v092_signal(invcap, closeadj):
    base = _mean(invcap.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sm63_sl63_2d_v093_signal(invcap, closeadj):
    base = _mean(invcap.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sm252_sl63_2d_v094_signal(invcap, closeadj):
    base = _mean(invcap.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sm252_sl126_2d_v095_signal(invcap, closeadj):
    base = _mean(invcap.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sm21_sl21_2d_v096_signal(ros, closeadj):
    base = _mean(ros, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sm63_sl21_2d_v097_signal(ros, closeadj):
    base = _mean(ros, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sm63_sl63_2d_v098_signal(ros, closeadj):
    base = _mean(ros, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sm252_sl63_2d_v099_signal(ros, closeadj):
    base = _mean(ros, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sm252_sl126_2d_v100_signal(ros, closeadj):
    base = _mean(ros, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sm21_sl21_2d_v101_signal(roic, roic_sector_med, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sm63_sl21_2d_v102_signal(roic, roic_sector_med, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sm63_sl63_2d_v103_signal(roic, roic_sector_med, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sm252_sl63_2d_v104_signal(roic, roic_sector_med, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sm252_sl126_2d_v105_signal(roic, roic_sector_med, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sm21_sl21_2d_v106_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sm63_sl21_2d_v107_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sm63_sl63_2d_v108_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sm252_sl63_2d_v109_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sm252_sl126_2d_v110_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = _mean((roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sm21_sl21_2d_v111_signal(roic, roic_industry_med, closeadj):
    base = _mean((roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sm63_sl21_2d_v112_signal(roic, roic_industry_med, closeadj):
    base = _mean((roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sm63_sl63_2d_v113_signal(roic, roic_industry_med, closeadj):
    base = _mean((roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sm252_sl63_2d_v114_signal(roic, roic_industry_med, closeadj):
    base = _mean((roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sm252_sl126_2d_v115_signal(roic, roic_industry_med, closeadj):
    base = _mean((roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(roic, roic_mcap_med, closeadj):
    base = _mean((roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(roic, roic_mcap_med, closeadj):
    base = _mean((roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(roic, roic_mcap_med, closeadj):
    base = _mean((roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(roic, roic_mcap_med, closeadj):
    base = _mean((roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(roic, roic_mcap_med, closeadj):
    base = _mean((roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_sm21_sl21_2d_v121_signal(roic_sector_pctile, closeadj):
    base = _mean(roic_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_sm63_sl21_2d_v122_signal(roic_sector_pctile, closeadj):
    base = _mean(roic_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_sm63_sl63_2d_v123_signal(roic_sector_pctile, closeadj):
    base = _mean(roic_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_sm252_sl63_2d_v124_signal(roic_sector_pctile, closeadj):
    base = _mean(roic_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_sm252_sl126_2d_v125_signal(roic_sector_pctile, closeadj):
    base = _mean(roic_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_sm21_sl21_2d_v126_signal(roic_industry_pctile, closeadj):
    base = _mean(roic_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_sm63_sl21_2d_v127_signal(roic_industry_pctile, closeadj):
    base = _mean(roic_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_sm63_sl63_2d_v128_signal(roic_industry_pctile, closeadj):
    base = _mean(roic_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_sm252_sl63_2d_v129_signal(roic_industry_pctile, closeadj):
    base = _mean(roic_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_sm252_sl126_2d_v130_signal(roic_industry_pctile, closeadj):
    base = _mean(roic_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_pctslope_21d_2d_v131_signal(roic, closeadj):
    base = roic
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_pctslope_63d_2d_v132_signal(roic, closeadj):
    base = roic
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_pctslope_252d_2d_v133_signal(roic, closeadj):
    base = roic
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_pctslope_21d_2d_v134_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_pctslope_63d_2d_v135_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_pctslope_252d_2d_v136_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_pctslope_21d_2d_v137_signal(invcap, closeadj):
    base = invcap
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_pctslope_63d_2d_v138_signal(invcap, closeadj):
    base = invcap
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_pctslope_252d_2d_v139_signal(invcap, closeadj):
    base = invcap
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_pctslope_21d_2d_v140_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_pctslope_63d_2d_v141_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_pctslope_252d_2d_v142_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_pctslope_21d_2d_v143_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_pctslope_63d_2d_v144_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_pctslope_252d_2d_v145_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_pctslope_21d_2d_v146_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_pctslope_63d_2d_v147_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_pctslope_252d_2d_v148_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_pctslope_21d_2d_v149_signal(ros, closeadj):
    base = ros
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_pctslope_63d_2d_v150_signal(ros, closeadj):
    base = ros
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_pctslope_252d_2d_v151_signal(ros, closeadj):
    base = ros
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_pctslope_21d_2d_v152_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_pctslope_63d_2d_v153_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_pctslope_252d_2d_v154_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_pctslope_21d_2d_v155_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_pctslope_63d_2d_v156_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_pctslope_252d_2d_v157_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_pctslope_21d_2d_v158_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_pctslope_63d_2d_v159_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_pctslope_252d_2d_v160_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_pctslope_21d_2d_v164_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_pctslope_63d_2d_v165_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_pctslope_252d_2d_v166_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_pctslope_21d_2d_v167_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_pctslope_63d_2d_v168_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of roic_peer_industry_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_pctslope_252d_2d_v169_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sgnslope_21d_2d_v170_signal(roic, closeadj):
    base = roic
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sgnslope_63d_2d_v171_signal(roic, closeadj):
    base = roic
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_sgnslope_252d_2d_v172_signal(roic, closeadj):
    base = roic
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sgnslope_21d_2d_v173_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sgnslope_63d_2d_v174_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_sgnslope_252d_2d_v175_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sgnslope_21d_2d_v176_signal(invcap, closeadj):
    base = invcap
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sgnslope_63d_2d_v177_signal(invcap, closeadj):
    base = invcap
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_sgnslope_252d_2d_v178_signal(invcap, closeadj):
    base = invcap
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sgnslope_21d_2d_v179_signal(roic, closeadj):
    base = roic.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sgnslope_63d_2d_v180_signal(roic, closeadj):
    base = roic.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_sgnslope_252d_2d_v181_signal(roic, closeadj):
    base = roic.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sgnslope_21d_2d_v182_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sgnslope_63d_2d_v183_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_sgnslope_252d_2d_v184_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sgnslope_21d_2d_v185_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sgnslope_63d_2d_v186_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_sgnslope_252d_2d_v187_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sgnslope_21d_2d_v188_signal(ros, closeadj):
    base = ros
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sgnslope_63d_2d_v189_signal(ros, closeadj):
    base = ros
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_sgnslope_252d_2d_v190_signal(ros, closeadj):
    base = ros
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sgnslope_21d_2d_v191_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sgnslope_63d_2d_v192_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_sgnslope_252d_2d_v193_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sgnslope_21d_2d_v194_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sgnslope_63d_2d_v195_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_sgnslope_252d_2d_v196_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sgnslope_21d_2d_v197_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sgnslope_63d_2d_v198_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_sgnslope_252d_2d_v199_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

