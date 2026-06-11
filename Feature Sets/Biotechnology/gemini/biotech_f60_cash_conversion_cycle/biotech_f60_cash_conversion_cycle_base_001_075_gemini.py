
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_raw_21d_base_v001_signal(ccc, closeadj):
    result = _mean(ccc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_raw_63d_base_v002_signal(ccc, closeadj):
    result = _mean(ccc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_raw_126d_base_v003_signal(ccc, closeadj):
    result = _mean(ccc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_raw_252d_base_v004_signal(ccc, closeadj):
    result = _mean(ccc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_raw_504d_base_v005_signal(ccc, closeadj):
    result = _mean(ccc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_log_21d_base_v006_signal(ccc, closeadj):
    result = _mean(_log(ccc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_log_63d_base_v007_signal(ccc, closeadj):
    result = _mean(_log(ccc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_log_126d_base_v008_signal(ccc, closeadj):
    result = _mean(_log(ccc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_log_252d_base_v009_signal(ccc, closeadj):
    result = _mean(_log(ccc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ccc
def gm_f60_biotech_f60_cash_conversion_cycle_log_504d_base_v010_signal(ccc, closeadj):
    result = _mean(_log(ccc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_z_21d_base_v011_signal(ccc):
    result = _z(ccc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_z_63d_base_v012_signal(ccc):
    result = _z(ccc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_z_126d_base_v013_signal(ccc):
    result = _z(ccc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_z_252d_base_v014_signal(ccc):
    result = _z(ccc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_z_504d_base_v015_signal(ccc):
    result = _z(ccc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_pct_21d_base_v016_signal(ccc):
    result = _pct_change(ccc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_pct_63d_base_v017_signal(ccc):
    result = _pct_change(ccc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_pct_126d_base_v018_signal(ccc):
    result = _pct_change(ccc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_pct_252d_base_v019_signal(ccc):
    result = _pct_change(ccc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_pct_504d_base_v020_signal(ccc):
    result = _pct_change(ccc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ccc
def gm_f60_biotech_f60_cash_conversion_cycle_ps_21d_base_v021_signal(ccc, sharesbas, closeadj):
    ps = _safe_div(ccc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ccc
def gm_f60_biotech_f60_cash_conversion_cycle_ps_63d_base_v022_signal(ccc, sharesbas, closeadj):
    ps = _safe_div(ccc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ccc
def gm_f60_biotech_f60_cash_conversion_cycle_ps_126d_base_v023_signal(ccc, sharesbas, closeadj):
    ps = _safe_div(ccc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ccc
def gm_f60_biotech_f60_cash_conversion_cycle_ps_252d_base_v024_signal(ccc, sharesbas, closeadj):
    ps = _safe_div(ccc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ccc
def gm_f60_biotech_f60_cash_conversion_cycle_ps_504d_base_v025_signal(ccc, sharesbas, closeadj):
    ps = _safe_div(ccc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ccc to revenue
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_revenue_21d_base_v026_signal(ccc, revenue):
    ratio = _safe_div(ccc, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ccc to revenue
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_revenue_63d_base_v027_signal(ccc, revenue):
    ratio = _safe_div(ccc, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ccc to revenue
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_revenue_126d_base_v028_signal(ccc, revenue):
    ratio = _safe_div(ccc, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ccc to revenue
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_revenue_252d_base_v029_signal(ccc, revenue):
    ratio = _safe_div(ccc, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ccc to revenue
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_revenue_504d_base_v030_signal(ccc, revenue):
    ratio = _safe_div(ccc, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ccc to inventory
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_inventory_21d_base_v031_signal(ccc, inventory):
    ratio = _safe_div(ccc, inventory)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ccc to inventory
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_inventory_63d_base_v032_signal(ccc, inventory):
    ratio = _safe_div(ccc, inventory)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ccc to inventory
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_inventory_126d_base_v033_signal(ccc, inventory):
    ratio = _safe_div(ccc, inventory)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ccc to inventory
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_inventory_252d_base_v034_signal(ccc, inventory):
    ratio = _safe_div(ccc, inventory)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ccc to inventory
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_inventory_504d_base_v035_signal(ccc, inventory):
    ratio = _safe_div(ccc, inventory)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ccc to cor
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_cor_21d_base_v036_signal(ccc, cor):
    ratio = _safe_div(ccc, cor)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ccc to cor
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_cor_63d_base_v037_signal(ccc, cor):
    ratio = _safe_div(ccc, cor)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ccc to cor
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_cor_126d_base_v038_signal(ccc, cor):
    ratio = _safe_div(ccc, cor)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ccc to cor
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_cor_252d_base_v039_signal(ccc, cor):
    ratio = _safe_div(ccc, cor)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ccc to cor
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_cor_504d_base_v040_signal(ccc, cor):
    ratio = _safe_div(ccc, cor)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ccc to payables
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_payables_21d_base_v041_signal(ccc, payables):
    ratio = _safe_div(ccc, payables)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ccc to payables
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_payables_63d_base_v042_signal(ccc, payables):
    ratio = _safe_div(ccc, payables)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ccc to payables
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_payables_126d_base_v043_signal(ccc, payables):
    ratio = _safe_div(ccc, payables)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ccc to payables
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_payables_252d_base_v044_signal(ccc, payables):
    ratio = _safe_div(ccc, payables)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ccc to payables
def gm_f60_biotech_f60_cash_conversion_cycle_ratio_payables_504d_base_v045_signal(ccc, payables):
    ratio = _safe_div(ccc, payables)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ccc scaled by assets
def gm_f60_biotech_f60_cash_conversion_cycle_asset_scaled_21d_base_v046_signal(ccc, assets):
    scaled = _safe_div(ccc, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ccc scaled by assets
def gm_f60_biotech_f60_cash_conversion_cycle_asset_scaled_63d_base_v047_signal(ccc, assets):
    scaled = _safe_div(ccc, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ccc scaled by assets
def gm_f60_biotech_f60_cash_conversion_cycle_asset_scaled_126d_base_v048_signal(ccc, assets):
    scaled = _safe_div(ccc, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ccc scaled by assets
def gm_f60_biotech_f60_cash_conversion_cycle_asset_scaled_252d_base_v049_signal(ccc, assets):
    scaled = _safe_div(ccc, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ccc scaled by assets
def gm_f60_biotech_f60_cash_conversion_cycle_asset_scaled_504d_base_v050_signal(ccc, assets):
    scaled = _safe_div(ccc, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ccc scaled by marketcap
def gm_f60_biotech_f60_cash_conversion_cycle_mcap_scaled_21d_base_v051_signal(ccc, marketcap):
    scaled = _safe_div(ccc, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ccc scaled by marketcap
def gm_f60_biotech_f60_cash_conversion_cycle_mcap_scaled_63d_base_v052_signal(ccc, marketcap):
    scaled = _safe_div(ccc, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ccc scaled by marketcap
def gm_f60_biotech_f60_cash_conversion_cycle_mcap_scaled_126d_base_v053_signal(ccc, marketcap):
    scaled = _safe_div(ccc, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ccc scaled by marketcap
def gm_f60_biotech_f60_cash_conversion_cycle_mcap_scaled_252d_base_v054_signal(ccc, marketcap):
    scaled = _safe_div(ccc, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ccc scaled by marketcap
def gm_f60_biotech_f60_cash_conversion_cycle_mcap_scaled_504d_base_v055_signal(ccc, marketcap):
    scaled = _safe_div(ccc, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_low_21d_base_v056_signal(ccc):
    low = ccc.rolling(21).min()
    result = _safe_div(ccc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_low_63d_base_v057_signal(ccc):
    low = ccc.rolling(63).min()
    result = _safe_div(ccc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_low_126d_base_v058_signal(ccc):
    low = ccc.rolling(126).min()
    result = _safe_div(ccc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_low_252d_base_v059_signal(ccc):
    low = ccc.rolling(252).min()
    result = _safe_div(ccc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_low_504d_base_v060_signal(ccc):
    low = ccc.rolling(504).min()
    result = _safe_div(ccc - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_high_21d_base_v061_signal(ccc):
    high = ccc.rolling(21).max()
    result = _safe_div(high - ccc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_high_63d_base_v062_signal(ccc):
    high = ccc.rolling(63).max()
    result = _safe_div(high - ccc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_high_126d_base_v063_signal(ccc):
    high = ccc.rolling(126).max()
    result = _safe_div(high - ccc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_high_252d_base_v064_signal(ccc):
    high = ccc.rolling(252).max()
    result = _safe_div(high - ccc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ccc
def gm_f60_biotech_f60_cash_conversion_cycle_dist_high_504d_base_v065_signal(ccc):
    high = ccc.rolling(504).max()
    result = _safe_div(high - ccc, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_mom_21d_base_v066_signal(ccc):
    m1 = _mean(ccc, 21)
    m2 = _mean(ccc, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_mom_63d_base_v067_signal(ccc):
    m1 = _mean(ccc, 63)
    m2 = _mean(ccc, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_mom_126d_base_v068_signal(ccc):
    m1 = _mean(ccc, 126)
    m2 = _mean(ccc, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_mom_252d_base_v069_signal(ccc):
    m1 = _mean(ccc, 252)
    m2 = _mean(ccc, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_mom_504d_base_v070_signal(ccc):
    m1 = _mean(ccc, 504)
    m2 = _mean(ccc, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_skew_21d_base_v071_signal(ccc):
    result = _skew(ccc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_skew_63d_base_v072_signal(ccc):
    result = _skew(ccc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_skew_126d_base_v073_signal(ccc):
    result = _skew(ccc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_skew_252d_base_v074_signal(ccc):
    result = _skew(ccc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ccc
def gm_f60_biotech_f60_cash_conversion_cycle_skew_504d_base_v075_signal(ccc):
    result = _skew(ccc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

