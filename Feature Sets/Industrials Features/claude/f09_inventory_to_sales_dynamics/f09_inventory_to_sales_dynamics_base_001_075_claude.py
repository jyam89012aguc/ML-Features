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
    # cost of revenue / inventory ~= inventory turns
    return cor / inventory.replace(0, np.nan).abs()


# 21d inv/sales ratio mean * closeadj
def f09isd_f09_inventory_to_sales_dynamics_invsale_21d_base_v001_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inv/sales mean
def f09isd_f09_inventory_to_sales_dynamics_invsale_63d_base_v002_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d inv/sales mean
def f09isd_f09_inventory_to_sales_dynamics_invsale_126d_base_v003_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inv/sales mean
def f09isd_f09_inventory_to_sales_dynamics_invsale_252d_base_v004_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inv/sales mean
def f09isd_f09_inventory_to_sales_dynamics_invsale_504d_base_v005_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d inv-rev gap * closeadj
def f09isd_f09_inventory_to_sales_dynamics_gap_21d_base_v006_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_63d_base_v007_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_126d_base_v008_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_252d_base_v009_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_504d_base_v010_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d inv velocity * closeadj
def f09isd_f09_inventory_to_sales_dynamics_vel_21d_base_v011_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inv velocity
def f09isd_f09_inventory_to_sales_dynamics_vel_63d_base_v012_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d inv velocity
def f09isd_f09_inventory_to_sales_dynamics_vel_126d_base_v013_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inv velocity
def f09isd_f09_inventory_to_sales_dynamics_vel_252d_base_v014_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inv velocity
def f09isd_f09_inventory_to_sales_dynamics_vel_504d_base_v015_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invsale_5d_base_v016_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invsale_10d_base_v017_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invsale_42d_base_v018_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invsale_189d_base_v019_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invsale_378d_base_v020_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_5d_base_v021_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_10d_base_v022_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_42d_base_v023_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_189d_base_v024_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d gap
def f09isd_f09_inventory_to_sales_dynamics_gap_378d_base_v025_signal(inventory, revenue, closeadj):
    base = _f09_inv_revenue_gap(inventory, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invstd_21d_base_v026_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invstd_63d_base_v027_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invstd_252d_base_v028_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invstd_504d_base_v029_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std velocity
def f09isd_f09_inventory_to_sales_dynamics_velstd_21d_base_v030_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std velocity
def f09isd_f09_inventory_to_sales_dynamics_velstd_63d_base_v031_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std velocity
def f09isd_f09_inventory_to_sales_dynamics_velstd_252d_base_v032_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std velocity
def f09isd_f09_inventory_to_sales_dynamics_velstd_504d_base_v033_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invz_21d_base_v034_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invz_63d_base_v035_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invz_252d_base_v036_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invz_504d_base_v037_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z velocity
def f09isd_f09_inventory_to_sales_dynamics_velz_21d_base_v038_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z velocity
def f09isd_f09_inventory_to_sales_dynamics_velz_63d_base_v039_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z velocity
def f09isd_f09_inventory_to_sales_dynamics_velz_252d_base_v040_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z velocity
def f09isd_f09_inventory_to_sales_dynamics_velz_504d_base_v041_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invema_21d_base_v042_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invema_63d_base_v043_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA inv/sales
def f09isd_f09_inventory_to_sales_dynamics_invema_252d_base_v044_signal(inventory, revenue, closeadj):
    base = _f09_inv_sales_ratio(inventory, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA velocity
def f09isd_f09_inventory_to_sales_dynamics_velema_21d_base_v045_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA velocity
def f09isd_f09_inventory_to_sales_dynamics_velema_63d_base_v046_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA velocity
def f09isd_f09_inventory_to_sales_dynamics_velema_252d_base_v047_signal(inventory, cor, closeadj):
    base = _f09_inv_velocity(inventory, cor)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 inv/sales gap
def f09isd_f09_inventory_to_sales_dynamics_invsalegap_21v252_base_v048_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 inv/sales gap
def f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v252_base_v049_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v504 inv/sales gap
def f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v504_base_v050_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 velocity gap
def f09isd_f09_inventory_to_sales_dynamics_velgap_21v252_base_v051_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 velocity gap
def f09isd_f09_inventory_to_sales_dynamics_velgap_63v252_base_v052_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v504 velocity gap
def f09isd_f09_inventory_to_sales_dynamics_velgap_63v504_base_v053_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales * close^2
def f09isd_f09_inventory_to_sales_dynamics_invxprice_21d_base_v054_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales 63d * close^2
def f09isd_f09_inventory_to_sales_dynamics_invxprice_63d_base_v055_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales 252d * close^2
def f09isd_f09_inventory_to_sales_dynamics_invxprice_252d_base_v056_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales x revenue 63d
def f09isd_f09_inventory_to_sales_dynamics_invxrev_63d_base_v057_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b * revenue, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales x revenue 252d
def f09isd_f09_inventory_to_sales_dynamics_invxrev_252d_base_v058_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = _mean(b * revenue, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# velocity x close^2
def f09isd_f09_inventory_to_sales_dynamics_velxprice_63d_base_v059_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = _mean(b, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity x close^2 252d
def f09isd_f09_inventory_to_sales_dynamics_velxprice_252d_base_v060_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = _mean(b, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# velocity x cor 63d
def f09isd_f09_inventory_to_sales_dynamics_velxcor_63d_base_v061_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = _mean(b * cor, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# velocity x cor 252d
def f09isd_f09_inventory_to_sales_dynamics_velxcor_252d_base_v062_signal(inventory, cor, closeadj):
    b = _f09_inv_velocity(inventory, cor)
    result = _mean(b * cor, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap x revenue 63d
def f09isd_f09_inventory_to_sales_dynamics_gapxrev_63d_base_v063_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap x revenue 252d
def f09isd_f09_inventory_to_sales_dynamics_gapxrev_252d_base_v064_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales * velocity 63d
def f09isd_f09_inventory_to_sales_dynamics_invxvel_63d_base_v065_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = _mean(a * v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales * velocity 252d
def f09isd_f09_inventory_to_sales_dynamics_invxvel_252d_base_v066_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = _mean(a * v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales / velocity 63d
def f09isd_f09_inventory_to_sales_dynamics_invovervel_63d_base_v067_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 63) / _mean(v, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inv/sales / velocity 252d
def f09isd_f09_inventory_to_sales_dynamics_invovervel_252d_base_v068_signal(inventory, revenue, cor, closeadj):
    a = _f09_inv_sales_ratio(inventory, revenue)
    v = _f09_inv_velocity(inventory, cor)
    result = (_mean(a, 252) / _mean(v, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap squared 63d
def f09isd_f09_inventory_to_sales_dynamics_gapsq_63d_base_v069_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap squared 252d
def f09isd_f09_inventory_to_sales_dynamics_gapsq_252d_base_v070_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gap * close return
def f09isd_f09_inventory_to_sales_dynamics_gapxcret_21d_base_v071_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 21)
    cret = closeadj.pct_change(21)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap * close return
def f09isd_f09_inventory_to_sales_dynamics_gapxcret_63d_base_v072_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 63)
    cret = closeadj.pct_change(63)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap * close return
def f09isd_f09_inventory_to_sales_dynamics_gapxcret_252d_base_v073_signal(inventory, revenue, closeadj):
    g = _f09_inv_revenue_gap(inventory, revenue, 252)
    cret = closeadj.pct_change(252)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt inv/sales 252d
def f09isd_f09_inventory_to_sales_dynamics_invsqrt_252d_base_v074_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue).abs()
    result = np.sqrt(_mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log inv/sales 252d
def f09isd_f09_inventory_to_sales_dynamics_invlog_252d_base_v075_signal(inventory, revenue, closeadj):
    b = _f09_inv_sales_ratio(inventory, revenue)
    result = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09isd_f09_inventory_to_sales_dynamics_invsale_21d_base_v001_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_63d_base_v002_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_126d_base_v003_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_252d_base_v004_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_504d_base_v005_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_21d_base_v006_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_63d_base_v007_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_126d_base_v008_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_252d_base_v009_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_504d_base_v010_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_21d_base_v011_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_63d_base_v012_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_126d_base_v013_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_252d_base_v014_signal,
    f09isd_f09_inventory_to_sales_dynamics_vel_504d_base_v015_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_5d_base_v016_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_10d_base_v017_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_42d_base_v018_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_189d_base_v019_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsale_378d_base_v020_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_5d_base_v021_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_10d_base_v022_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_42d_base_v023_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_189d_base_v024_signal,
    f09isd_f09_inventory_to_sales_dynamics_gap_378d_base_v025_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_21d_base_v026_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_63d_base_v027_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_252d_base_v028_signal,
    f09isd_f09_inventory_to_sales_dynamics_invstd_504d_base_v029_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_21d_base_v030_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_63d_base_v031_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_252d_base_v032_signal,
    f09isd_f09_inventory_to_sales_dynamics_velstd_504d_base_v033_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_21d_base_v034_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_63d_base_v035_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_252d_base_v036_signal,
    f09isd_f09_inventory_to_sales_dynamics_invz_504d_base_v037_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_21d_base_v038_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_63d_base_v039_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_252d_base_v040_signal,
    f09isd_f09_inventory_to_sales_dynamics_velz_504d_base_v041_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_21d_base_v042_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_63d_base_v043_signal,
    f09isd_f09_inventory_to_sales_dynamics_invema_252d_base_v044_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_21d_base_v045_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_63d_base_v046_signal,
    f09isd_f09_inventory_to_sales_dynamics_velema_252d_base_v047_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_21v252_base_v048_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v252_base_v049_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsalegap_63v504_base_v050_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_21v252_base_v051_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_63v252_base_v052_signal,
    f09isd_f09_inventory_to_sales_dynamics_velgap_63v504_base_v053_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxprice_21d_base_v054_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxprice_63d_base_v055_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxprice_252d_base_v056_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxrev_63d_base_v057_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxrev_252d_base_v058_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxprice_63d_base_v059_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxprice_252d_base_v060_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxcor_63d_base_v061_signal,
    f09isd_f09_inventory_to_sales_dynamics_velxcor_252d_base_v062_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxrev_63d_base_v063_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxrev_252d_base_v064_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvel_63d_base_v065_signal,
    f09isd_f09_inventory_to_sales_dynamics_invxvel_252d_base_v066_signal,
    f09isd_f09_inventory_to_sales_dynamics_invovervel_63d_base_v067_signal,
    f09isd_f09_inventory_to_sales_dynamics_invovervel_252d_base_v068_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapsq_63d_base_v069_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapsq_252d_base_v070_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcret_21d_base_v071_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcret_63d_base_v072_signal,
    f09isd_f09_inventory_to_sales_dynamics_gapxcret_252d_base_v073_signal,
    f09isd_f09_inventory_to_sales_dynamics_invsqrt_252d_base_v074_signal,
    f09isd_f09_inventory_to_sales_dynamics_invlog_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_INVENTORY_TO_SALES_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f09_inventory_to_sales_dynamics_base_001_075_claude: {n_features} features pass")
