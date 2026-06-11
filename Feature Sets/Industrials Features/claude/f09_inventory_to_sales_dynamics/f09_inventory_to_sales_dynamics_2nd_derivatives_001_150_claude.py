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


# ===== folder domain primitives =====
def _f09_inv_sales_ratio(inventory, revenue):
    return inventory / revenue.replace(0, np.nan).abs()


def _f09_inv_revenue_gap(inventory, revenue, w):
    inv_g = inventory.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return inv_g - rev_g


def _f09_inv_velocity(inventory, cor):
    return cor / inventory.replace(0, np.nan).abs()


# Slope of 21d inv/sales mean * close, 5d
def f09isd_f09_inventory_to_sales_dynamics_invsale_21d_slope_v001_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 21) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_21d_slope_v002_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_63d_slope_v003_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_63d_slope_v004_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 63) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_126d_slope_v005_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 126) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_126d_slope_v006_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 126) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_252d_slope_v007_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 252) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_252d_slope_v008_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_504d_slope_v009_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 504) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_504d_slope_v010_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_21d_slope_v011_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_21d_slope_v012_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_63d_slope_v013_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_126d_slope_v014_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 126) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_252d_slope_v015_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_504d_slope_v016_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_21d_slope_v017_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 21) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_21d_slope_v018_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_63d_slope_v019_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_63d_slope_v020_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 63) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_126d_slope_v021_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 126) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_126d_slope_v022_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 126) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_252d_slope_v023_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 252) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_252d_slope_v024_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_504d_slope_v025_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 504) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_504d_slope_v026_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_5d_slope_v027_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 5) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_10d_slope_v028_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 10) * closeadj
    return _slope_pct(base, 10).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_42d_slope_v029_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 42) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_189d_slope_v030_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 189) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_378d_slope_v031_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 378) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_5d_slope_v032_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 5) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_10d_slope_v033_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 10) * closeadj
    return _slope_diff_norm(base, 10).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_42d_slope_v034_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 42) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_189d_slope_v035_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 189) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gap_378d_slope_v036_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 378) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invstd_21d_slope_v037_signal(inventory, revenue, closeadj):
    base = _std(_f09_inv_sales_ratio(inventory, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invstd_63d_slope_v038_signal(inventory, revenue, closeadj):
    base = _std(_f09_inv_sales_ratio(inventory, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invstd_252d_slope_v039_signal(inventory, revenue, closeadj):
    base = _std(_f09_inv_sales_ratio(inventory, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invstd_504d_slope_v040_signal(inventory, revenue, closeadj):
    base = _std(_f09_inv_sales_ratio(inventory, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velstd_21d_slope_v041_signal(inventory, cor, closeadj):
    base = _std(_f09_inv_velocity(inventory, cor), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velstd_63d_slope_v042_signal(inventory, cor, closeadj):
    base = _std(_f09_inv_velocity(inventory, cor), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velstd_252d_slope_v043_signal(inventory, cor, closeadj):
    base = _std(_f09_inv_velocity(inventory, cor), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velstd_504d_slope_v044_signal(inventory, cor, closeadj):
    base = _std(_f09_inv_velocity(inventory, cor), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invz_21d_slope_v045_signal(inventory, revenue, closeadj):
    base = _z(_f09_inv_sales_ratio(inventory, revenue), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invz_63d_slope_v046_signal(inventory, revenue, closeadj):
    base = _z(_f09_inv_sales_ratio(inventory, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invz_252d_slope_v047_signal(inventory, revenue, closeadj):
    base = _z(_f09_inv_sales_ratio(inventory, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invz_504d_slope_v048_signal(inventory, revenue, closeadj):
    base = _z(_f09_inv_sales_ratio(inventory, revenue), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velz_21d_slope_v049_signal(inventory, cor, closeadj):
    base = _z(_f09_inv_velocity(inventory, cor), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velz_63d_slope_v050_signal(inventory, cor, closeadj):
    base = _z(_f09_inv_velocity(inventory, cor), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velz_252d_slope_v051_signal(inventory, cor, closeadj):
    base = _z(_f09_inv_velocity(inventory, cor), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velz_504d_slope_v052_signal(inventory, cor, closeadj):
    base = _z(_f09_inv_velocity(inventory, cor), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invema_21d_slope_v053_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invema_63d_slope_v054_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invema_252d_slope_v055_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velema_21d_slope_v056_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velema_63d_slope_v057_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velema_252d_slope_v058_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsalegap_21v252_slope_v059_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v252_slope_v060_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v504_slope_v061_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velgap_21v252_slope_v062_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velgap_63v252_slope_v063_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velgap_63v504_slope_v064_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxprice_63d_slope_v065_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = _mean(b, 63) * closeadj * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxprice_252d_slope_v066_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = _mean(b, 252) * closeadj * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxrev_63d_slope_v067_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = _mean(b * revenue, 63) * closeadj / 1e9
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxrev_252d_slope_v068_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = _mean(b * revenue, 252) * closeadj / 1e9
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velxcor_63d_slope_v069_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = _mean(b * cor, 63) * closeadj / 1e9
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velxcor_252d_slope_v070_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = _mean(b * cor, 252) * closeadj / 1e9
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxrev_63d_slope_v071_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxrev_252d_slope_v072_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxvel_63d_slope_v073_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = _mean(a * v, 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxvel_252d_slope_v074_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = _mean(a * v, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invovervel_63d_slope_v075_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 63) / _mean(v, 63).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invovervel_252d_slope_v076_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 252) / _mean(v, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapsq_63d_slope_v077_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapsq_252d_slope_v078_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxcret_63d_slope_v079_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    cret = closeadj.pct_change(63)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxcret_252d_slope_v080_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    cret = closeadj.pct_change(252)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsqrt_252d_slope_v081_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invlog_252d_slope_v082_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmax_252d_slope_v083_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = b.rolling(252, min_periods=63).max() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmax_504d_slope_v084_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = b.rolling(504, min_periods=126).max() * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invmin_252d_slope_v085_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = b.rolling(252, min_periods=63).min() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invrng_252d_slope_v086_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invpct_252d_slope_v087_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invpct_504d_slope_v088_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velmax_252d_slope_v089_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = b.rolling(252, min_periods=63).max() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velpct_252d_slope_v090_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcv_63d_slope_v091_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcv_252d_slope_v092_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velcv_63d_slope_v093_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velcv_252d_slope_v094_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_21v252_slope_v095_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_63v252_slope_v096_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invratio_63v504_slope_v097_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velratio_63v252_slope_v098_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velratio_63v504_slope_v099_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapabs_63d_slope_v100_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    base = g.abs() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapabs_252d_slope_v101_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = g.abs() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_excesscount_63d_slope_v102_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    excess = (g > 0.05).astype(float)
    base = (excess.rolling(63, min_periods=21).sum() + g) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_excesscount_252d_slope_v103_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    excess = (g > 0.05).astype(float)
    base = (excess.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapcum_63d_slope_v104_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = g.rolling(63, min_periods=21).sum() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapcum_252d_slope_v105_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapcum_504d_slope_v106_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = g.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapz_21d_slope_v107_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = _z(g, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapz_63d_slope_v108_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    base = _z(g, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapz_252d_slope_v109_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = _z(g, 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapstd_63d_slope_v110_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = _std(g, 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapstd_252d_slope_v111_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    base = _std(g, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velsqrt_63d_slope_v112_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor).abs()
    base = np.sqrt(_mean(b, 63)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velsqrt_252d_slope_v113_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vellog_252d_slope_v114_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    base = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_comp_63d_slope_v115_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 63) + _mean(v, 63) / 100) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_comp_252d_slope_v116_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 252) + _mean(v, 252) / 100) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_comp_504d_slope_v117_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 504) + _mean(v, 504) / 100) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_diff_63d_slope_v118_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 63) - _mean(v, 63) / 100) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_diff_252d_slope_v119_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = (_mean(a, 252) - _mean(v, 252) / 100) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxcor_63d_slope_v120_signal(inventory, revenue, cor, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    cor_g = cor.pct_change(63)
    base = g * cor_g * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxcor_252d_slope_v121_signal(inventory, revenue, cor, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    cor_g = cor.pct_change(252)
    base = g * cor_g * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcorgap_63d_slope_v122_signal(inventory, cor, closeadj):
    v_inv = _f09_inv_velocity(inventory, cor)
    inv_g = inventory.pct_change(63)
    cor_g = cor.pct_change(63)
    base = (inv_g - cor_g) * closeadj + v_inv * 0
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invcorgap_252d_slope_v123_signal(inventory, cor, closeadj):
    v_inv = _f09_inv_velocity(inventory, cor)
    inv_g = inventory.pct_change(252)
    cor_g = cor.pct_change(252)
    base = (inv_g - cor_g) * closeadj + v_inv * 0
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invlevel_63d_slope_v124_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invlevel_252d_slope_v125_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vellevel_63d_slope_v126_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vellevel_252d_slope_v127_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invdoll_63d_slope_v128_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = b * revenue * closeadj / 1e9
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invdoll_252d_slope_v129_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    base = _mean(b * revenue, 252) * closeadj / 1e9
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxinv_63d_slope_v130_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    base = g * inventory * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapxinv_252d_slope_v131_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = g * inventory * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_glut_63d_slope_v132_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    glut = ((g > 0.05) & (a > _mean(a, 252))).astype(float)
    base = (glut.rolling(63, min_periods=21).sum() + g) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_glut_252d_slope_v133_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    glut = ((g > 0.05) & (a > _mean(a, 252))).astype(float)
    base = (glut.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_short_252d_slope_v134_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    a = _f09_inv_sales_ratio(inventory, revenue)
    short = ((g < -0.05) & (a < _mean(a, 252))).astype(float)
    base = (short.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_dsi_252d_slope_v135_signal(inventory, cor, closeadj):
    b = 1.0 / _f09_inv_velocity(inventory, cor).replace(0, np.nan).abs()
    base = _mean(b, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_dsi_504d_slope_v136_signal(inventory, cor, closeadj):
    b = 1.0 / _f09_inv_velocity(inventory, cor).replace(0, np.nan).abs()
    base = _mean(b, 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velxinv_252d_slope_v137_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    base = _mean(a * v / 100, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxret_21d_slope_v138_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cret = closeadj.pct_change(21)
    base = b * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxret_252d_slope_v139_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cret = closeadj.pct_change(252)
    base = b * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_globcomp_504d_slope_v140_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    base = (_mean(a, 504) + _mean(v, 504) / 100 + g) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapzxcret_63d_slope_v141_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    z = _z(g, 252)
    cret = closeadj.pct_change(63)
    base = z * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_gapzxcret_252d_slope_v142_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    z = _z(g, 504)
    cret = closeadj.pct_change(252)
    base = z * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsign_63d_slope_v143_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    dev = b - _mean(b, 252)
    base = np.sign(dev) * _std(b, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velsign_63d_slope_v144_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    dev = b - _mean(b, 252)
    base = np.sign(dev) * _std(b, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invxvolproxy_63d_slope_v145_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    cv = _mean(closeadj, 63) * closeadj
    base = _mean(b, 63) * cv
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_velxvolproxy_63d_slope_v146_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    cv = _mean(closeadj, 63) * closeadj
    base = _mean(b, 63) * cv
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invlong_slope_v147_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vellong_slope_v148_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_invsale_252d_long_slope_v149_signal(inventory, revenue, closeadj):
    base = _mean(_f09_inv_sales_ratio(inventory, revenue), 252) * closeadj
    return _slope_pct(base, 252).replace([np.inf, -np.inf], np.nan)


def f09isd_f09_inventory_to_sales_dynamics_vel_252d_long_slope_v150_signal(inventory, cor, closeadj):
    base = _mean(_f09_inv_velocity(inventory, cor), 252) * closeadj
    return _slope_pct(base, 252).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09isd_f09_inventory_to_sales_dynamics_invsale_21d_slope_v001_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_21d_slope_v002_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_63d_slope_v003_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_63d_slope_v004_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_126d_slope_v005_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_126d_slope_v006_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_252d_slope_v007_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_252d_slope_v008_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_504d_slope_v009_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_504d_slope_v010_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_21d_slope_v011_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_21d_slope_v012_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_63d_slope_v013_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_126d_slope_v014_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_252d_slope_v015_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_504d_slope_v016_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_21d_slope_v017_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_21d_slope_v018_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_63d_slope_v019_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_63d_slope_v020_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_126d_slope_v021_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_126d_slope_v022_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_252d_slope_v023_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_252d_slope_v024_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_504d_slope_v025_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_504d_slope_v026_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_5d_slope_v027_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_10d_slope_v028_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_42d_slope_v029_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_189d_slope_v030_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_378d_slope_v031_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_5d_slope_v032_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_10d_slope_v033_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_42d_slope_v034_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_189d_slope_v035_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_378d_slope_v036_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_21d_slope_v037_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_63d_slope_v038_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_252d_slope_v039_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_504d_slope_v040_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_21d_slope_v041_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_63d_slope_v042_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_252d_slope_v043_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_504d_slope_v044_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_21d_slope_v045_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_63d_slope_v046_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_252d_slope_v047_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_504d_slope_v048_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_21d_slope_v049_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_63d_slope_v050_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_252d_slope_v051_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_504d_slope_v052_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_21d_slope_v053_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_63d_slope_v054_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_252d_slope_v055_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_21d_slope_v056_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_63d_slope_v057_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_252d_slope_v058_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_21v252_slope_v059_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v252_slope_v060_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v504_slope_v061_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_21v252_slope_v062_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_63v252_slope_v063_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_63v504_slope_v064_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxprice_63d_slope_v065_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxprice_252d_slope_v066_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxrev_63d_slope_v067_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxrev_252d_slope_v068_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxcor_63d_slope_v069_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxcor_252d_slope_v070_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxrev_63d_slope_v071_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxrev_252d_slope_v072_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvel_63d_slope_v073_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvel_252d_slope_v074_signal,
    f09isd_f09_inventory_to_sales_dynamics_invovervel_63d_slope_v075_signal,
    f09isd_f09_inventory_to_sales_dynamics_invovervel_252d_slope_v076_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapsq_63d_slope_v077_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapsq_252d_slope_v078_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcret_63d_slope_v079_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcret_252d_slope_v080_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsqrt_252d_slope_v081_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlog_252d_slope_v082_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmax_252d_slope_v083_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmax_504d_slope_v084_signal,
    f09isd_f09_inventory_to_sales_dynamics_invmin_252d_slope_v085_signal,
    f09isd_f09_inventory_to_sales_dynamics_invrng_252d_slope_v086_signal,
    f09isd_f09_inventory_to_sales_dynamics_invpct_252d_slope_v087_signal,
    f09isd_f09_inventory_to_sales_dynamics_invpct_504d_slope_v088_signal,
    f09isd_f09_inventory_to_sales_dynamics_velmax_252d_slope_v089_signal,
    f09isd_f09_inventory_to_sales_dynamics_velpct_252d_slope_v090_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcv_63d_slope_v091_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcv_252d_slope_v092_signal,
    f09isd_f09_inventory_to_sales_dynamics_velcv_63d_slope_v093_signal,
    f09isd_f09_inventory_to_sales_dynamics_velcv_252d_slope_v094_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_21v252_slope_v095_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_63v252_slope_v096_signal,
    f09isd_f09_inventory_to_sales_dynamics_invratio_63v504_slope_v097_signal,
    f09isd_f09_inventory_to_sales_dynamics_velratio_63v252_slope_v098_signal,
    f09isd_f09_inventory_to_sales_dynamics_velratio_63v504_slope_v099_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapabs_63d_slope_v100_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapabs_252d_slope_v101_signal,
    f09isd_f09_inventory_to_sales_dynamics_excesscount_63d_slope_v102_signal,
    f09isd_f09_inventory_to_sales_dynamics_excesscount_252d_slope_v103_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_63d_slope_v104_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_252d_slope_v105_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapcum_504d_slope_v106_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_21d_slope_v107_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_63d_slope_v108_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapz_252d_slope_v109_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapstd_63d_slope_v110_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapstd_252d_slope_v111_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsqrt_63d_slope_v112_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsqrt_252d_slope_v113_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellog_252d_slope_v114_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_63d_slope_v115_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_252d_slope_v116_signal,
    f09isd_f09_inventory_to_sales_dynamics_comp_504d_slope_v117_signal,
    f09isd_f09_inventory_to_sales_dynamics_diff_63d_slope_v118_signal,
    f09isd_f09_inventory_to_sales_dynamics_diff_252d_slope_v119_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcor_63d_slope_v120_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcor_252d_slope_v121_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcorgap_63d_slope_v122_signal,
    f09isd_f09_inventory_to_sales_dynamics_invcorgap_252d_slope_v123_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlevel_63d_slope_v124_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlevel_252d_slope_v125_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellevel_63d_slope_v126_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellevel_252d_slope_v127_signal,
    f09isd_f09_inventory_to_sales_dynamics_invdoll_63d_slope_v128_signal,
    f09isd_f09_inventory_to_sales_dynamics_invdoll_252d_slope_v129_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxinv_63d_slope_v130_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxinv_252d_slope_v131_signal,
    f09isd_f09_inventory_to_sales_dynamics_glut_63d_slope_v132_signal,
    f09isd_f09_inventory_to_sales_dynamics_glut_252d_slope_v133_signal,
    f09isd_f09_inventory_to_sales_dynamics_short_252d_slope_v134_signal,
    f09isd_f09_inventory_to_sales_dynamics_dsi_252d_slope_v135_signal,
    f09isd_f09_inventory_to_sales_dynamics_dsi_504d_slope_v136_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxinv_252d_slope_v137_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxret_21d_slope_v138_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxret_252d_slope_v139_signal,
    f09isd_f09_inventory_to_sales_dynamics_globcomp_504d_slope_v140_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapzxcret_63d_slope_v141_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapzxcret_252d_slope_v142_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsign_63d_slope_v143_signal,
    f09isd_f09_inventory_to_sales_dynamics_velsign_63d_slope_v144_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvolproxy_63d_slope_v145_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxvolproxy_63d_slope_v146_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlong_slope_v147_signal,
    f09isd_f09_inventory_to_sales_dynamics_vellong_slope_v148_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_252d_long_slope_v149_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_252d_long_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_INVENTORY_TO_SALES_DYNAMICS_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f09_inventory_to_sales_dynamics_2nd_derivatives_001_150_claude: {n_features} features pass")
