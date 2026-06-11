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


# 21d mean of roic_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_lvl_mean_21d_base_v001_signal(roic, closeadj):
    base = roic
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_lvl_mean_63d_base_v002_signal(roic, closeadj):
    base = roic
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_lvl_mean_126d_base_v003_signal(roic, closeadj):
    base = roic
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_lvl_mean_252d_base_v004_signal(roic, closeadj):
    base = roic
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_lvl_mean_504d_base_v005_signal(roic, closeadj):
    base = roic
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_calc scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_calc_mean_21d_base_v006_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_calc scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_calc_mean_63d_base_v007_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_calc scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_calc_mean_126d_base_v008_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_calc scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_calc_mean_252d_base_v009_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_calc scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_calc_mean_504d_base_v010_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of invcap_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_lvl_mean_21d_base_v011_signal(invcap, closeadj):
    base = invcap
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of invcap_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_lvl_mean_63d_base_v012_signal(invcap, closeadj):
    base = invcap
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of invcap_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_lvl_mean_126d_base_v013_signal(invcap, closeadj):
    base = invcap
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of invcap_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_lvl_mean_252d_base_v014_signal(invcap, closeadj):
    base = invcap
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of invcap_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_lvl_mean_504d_base_v015_signal(invcap, closeadj):
    base = invcap
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_yoy_chg scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_mean_21d_base_v016_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_yoy_chg scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_mean_63d_base_v017_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_yoy_chg scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_mean_126d_base_v018_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_yoy_chg scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_mean_252d_base_v019_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_yoy_chg scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_mean_504d_base_v020_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_vol_252 scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_vol_252_mean_21d_base_v021_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_vol_252 scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_vol_252_mean_63d_base_v022_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_vol_252 scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_vol_252_mean_126d_base_v023_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_vol_252 scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_vol_252_mean_252d_base_v024_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_vol_252 scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_vol_252_mean_504d_base_v025_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of invcap_growth scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_growth_mean_21d_base_v026_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of invcap_growth scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_growth_mean_63d_base_v027_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of invcap_growth scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_growth_mean_126d_base_v028_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of invcap_growth scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_growth_mean_252d_base_v029_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of invcap_growth scaled by closeadj
def f065ric_f065_return_on_invested_capital_invcap_growth_mean_504d_base_v030_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ros_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_ros_lvl_mean_21d_base_v031_signal(ros, closeadj):
    base = ros
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ros_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_ros_lvl_mean_63d_base_v032_signal(ros, closeadj):
    base = ros
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ros_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_ros_lvl_mean_126d_base_v033_signal(ros, closeadj):
    base = ros
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ros_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_ros_lvl_mean_252d_base_v034_signal(ros, closeadj):
    base = ros
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ros_lvl scaled by closeadj
def f065ric_f065_return_on_invested_capital_ros_lvl_mean_504d_base_v035_signal(ros, closeadj):
    base = ros
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_sector_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_mean_21d_base_v036_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_sector_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_mean_63d_base_v037_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_sector_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_mean_126d_base_v038_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_sector_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_mean_252d_base_v039_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_sector_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_mean_504d_base_v040_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_sector_z scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_mean_21d_base_v041_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_sector_z scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_mean_63d_base_v042_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_sector_z scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_mean_126d_base_v043_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_sector_z scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_mean_252d_base_v044_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_sector_z scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_mean_504d_base_v045_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_industry_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_mean_21d_base_v046_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_industry_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_mean_63d_base_v047_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_industry_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_mean_126d_base_v048_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_industry_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_mean_252d_base_v049_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_industry_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_mean_504d_base_v050_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_mcap_bucket_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_mean_21d_base_v051_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_mcap_bucket_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_mean_63d_base_v052_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_mcap_bucket_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_mean_126d_base_v053_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_mcap_bucket_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_mean_252d_base_v054_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_mcap_bucket_dist scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_mean_504d_base_v055_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_sector_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_mean_21d_base_v056_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_sector_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_mean_63d_base_v057_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_sector_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_mean_126d_base_v058_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_sector_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_mean_252d_base_v059_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_sector_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_mean_504d_base_v060_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of roic_peer_industry_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_mean_21d_base_v061_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of roic_peer_industry_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_mean_63d_base_v062_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of roic_peer_industry_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_mean_126d_base_v063_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of roic_peer_industry_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_mean_252d_base_v064_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of roic_peer_industry_pctile scaled by closeadj
def f065ric_f065_return_on_invested_capital_roic_peer_industry_pctile_mean_504d_base_v065_signal(roic_industry_pctile, closeadj):
    base = roic_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_median_63d_base_v066_signal(roic, closeadj):
    base = roic
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_median_252d_base_v067_signal(roic, closeadj):
    base = roic
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_lvl
def f065ric_f065_return_on_invested_capital_roic_lvl_median_504d_base_v068_signal(roic, closeadj):
    base = roic
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_median_63d_base_v069_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_median_252d_base_v070_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_calc
def f065ric_f065_return_on_invested_capital_roic_calc_median_504d_base_v071_signal(ebit, invcapavg, closeadj):
    base = _f065_invcap_ratio(ebit, invcapavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_median_63d_base_v072_signal(invcap, closeadj):
    base = invcap
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_median_252d_base_v073_signal(invcap, closeadj):
    base = invcap
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of invcap_lvl
def f065ric_f065_return_on_invested_capital_invcap_lvl_median_504d_base_v074_signal(invcap, closeadj):
    base = invcap
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_median_63d_base_v075_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_median_252d_base_v076_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_yoy_chg
def f065ric_f065_return_on_invested_capital_roic_yoy_chg_median_504d_base_v077_signal(roic, closeadj):
    base = roic.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_median_63d_base_v078_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_median_252d_base_v079_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_vol_252
def f065ric_f065_return_on_invested_capital_roic_vol_252_median_504d_base_v080_signal(roic, closeadj):
    base = roic.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_median_63d_base_v081_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_median_252d_base_v082_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of invcap_growth
def f065ric_f065_return_on_invested_capital_invcap_growth_median_504d_base_v083_signal(invcap, closeadj):
    base = invcap.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_median_63d_base_v084_signal(ros, closeadj):
    base = ros
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_median_252d_base_v085_signal(ros, closeadj):
    base = ros
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ros_lvl
def f065ric_f065_return_on_invested_capital_ros_lvl_median_504d_base_v086_signal(ros, closeadj):
    base = ros
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_median_63d_base_v087_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_median_252d_base_v088_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_peer_sector_dist
def f065ric_f065_return_on_invested_capital_roic_peer_sector_dist_median_504d_base_v089_signal(roic, roic_sector_med, closeadj):
    base = (roic - roic_sector_med) / roic_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_median_63d_base_v090_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_median_252d_base_v091_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_peer_sector_z
def f065ric_f065_return_on_invested_capital_roic_peer_sector_z_median_504d_base_v092_signal(roic, roic_sector_med, roic_sector_std, closeadj):
    base = (roic - roic_sector_med) / roic_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_median_63d_base_v093_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_median_252d_base_v094_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_peer_industry_dist
def f065ric_f065_return_on_invested_capital_roic_peer_industry_dist_median_504d_base_v095_signal(roic, roic_industry_med, closeadj):
    base = (roic - roic_industry_med) / roic_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_median_63d_base_v096_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_median_252d_base_v097_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of roic_peer_mcap_bucket_dist
def f065ric_f065_return_on_invested_capital_roic_peer_mcap_bucket_dist_median_504d_base_v098_signal(roic, roic_mcap_med, closeadj):
    base = (roic - roic_mcap_med) / roic_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_median_63d_base_v099_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of roic_peer_sector_pctile
def f065ric_f065_return_on_invested_capital_roic_peer_sector_pctile_median_252d_base_v100_signal(roic_sector_pctile, closeadj):
    base = roic_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

