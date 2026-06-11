
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_raw_21d_base_v001_signal(netmargin, closeadj):
    result = _mean(netmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_raw_63d_base_v002_signal(netmargin, closeadj):
    result = _mean(netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_raw_126d_base_v003_signal(netmargin, closeadj):
    result = _mean(netmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_raw_252d_base_v004_signal(netmargin, closeadj):
    result = _mean(netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_raw_504d_base_v005_signal(netmargin, closeadj):
    result = _mean(netmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_log_21d_base_v006_signal(netmargin, closeadj):
    result = _mean(_log(netmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_log_63d_base_v007_signal(netmargin, closeadj):
    result = _mean(_log(netmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_log_126d_base_v008_signal(netmargin, closeadj):
    result = _mean(_log(netmargin), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_log_252d_base_v009_signal(netmargin, closeadj):
    result = _mean(_log(netmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed netmargin
def gm_f46_biotech_f46_net_profit_margin_log_504d_base_v010_signal(netmargin, closeadj):
    result = _mean(_log(netmargin), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of netmargin
def gm_f46_biotech_f46_net_profit_margin_z_21d_base_v011_signal(netmargin):
    result = _z(netmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netmargin
def gm_f46_biotech_f46_net_profit_margin_z_63d_base_v012_signal(netmargin):
    result = _z(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netmargin
def gm_f46_biotech_f46_net_profit_margin_z_126d_base_v013_signal(netmargin):
    result = _z(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netmargin
def gm_f46_biotech_f46_net_profit_margin_z_252d_base_v014_signal(netmargin):
    result = _z(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netmargin
def gm_f46_biotech_f46_net_profit_margin_z_504d_base_v015_signal(netmargin):
    result = _z(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of netmargin
def gm_f46_biotech_f46_net_profit_margin_pct_21d_base_v016_signal(netmargin):
    result = _pct_change(netmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of netmargin
def gm_f46_biotech_f46_net_profit_margin_pct_63d_base_v017_signal(netmargin):
    result = _pct_change(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of netmargin
def gm_f46_biotech_f46_net_profit_margin_pct_126d_base_v018_signal(netmargin):
    result = _pct_change(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of netmargin
def gm_f46_biotech_f46_net_profit_margin_pct_252d_base_v019_signal(netmargin):
    result = _pct_change(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of netmargin
def gm_f46_biotech_f46_net_profit_margin_pct_504d_base_v020_signal(netmargin):
    result = _pct_change(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share netmargin
def gm_f46_biotech_f46_net_profit_margin_ps_21d_base_v021_signal(netmargin, sharesbas, closeadj):
    ps = _safe_div(netmargin, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share netmargin
def gm_f46_biotech_f46_net_profit_margin_ps_63d_base_v022_signal(netmargin, sharesbas, closeadj):
    ps = _safe_div(netmargin, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share netmargin
def gm_f46_biotech_f46_net_profit_margin_ps_126d_base_v023_signal(netmargin, sharesbas, closeadj):
    ps = _safe_div(netmargin, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share netmargin
def gm_f46_biotech_f46_net_profit_margin_ps_252d_base_v024_signal(netmargin, sharesbas, closeadj):
    ps = _safe_div(netmargin, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share netmargin
def gm_f46_biotech_f46_net_profit_margin_ps_504d_base_v025_signal(netmargin, sharesbas, closeadj):
    ps = _safe_div(netmargin, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of netmargin to revenue
def gm_f46_biotech_f46_net_profit_margin_ratio_revenue_21d_base_v026_signal(netmargin, revenue):
    ratio = _safe_div(netmargin, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of netmargin to revenue
def gm_f46_biotech_f46_net_profit_margin_ratio_revenue_63d_base_v027_signal(netmargin, revenue):
    ratio = _safe_div(netmargin, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of netmargin to revenue
def gm_f46_biotech_f46_net_profit_margin_ratio_revenue_126d_base_v028_signal(netmargin, revenue):
    ratio = _safe_div(netmargin, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of netmargin to revenue
def gm_f46_biotech_f46_net_profit_margin_ratio_revenue_252d_base_v029_signal(netmargin, revenue):
    ratio = _safe_div(netmargin, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of netmargin to revenue
def gm_f46_biotech_f46_net_profit_margin_ratio_revenue_504d_base_v030_signal(netmargin, revenue):
    ratio = _safe_div(netmargin, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d netmargin scaled by assets
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_21d_base_v031_signal(netmargin, assets):
    scaled = _safe_div(netmargin, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d netmargin scaled by assets
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_63d_base_v032_signal(netmargin, assets):
    scaled = _safe_div(netmargin, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d netmargin scaled by assets
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_126d_base_v033_signal(netmargin, assets):
    scaled = _safe_div(netmargin, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d netmargin scaled by assets
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_252d_base_v034_signal(netmargin, assets):
    scaled = _safe_div(netmargin, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d netmargin scaled by assets
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_504d_base_v035_signal(netmargin, assets):
    scaled = _safe_div(netmargin, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d netmargin scaled by marketcap
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_21d_base_v036_signal(netmargin, marketcap):
    scaled = _safe_div(netmargin, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d netmargin scaled by marketcap
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_63d_base_v037_signal(netmargin, marketcap):
    scaled = _safe_div(netmargin, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d netmargin scaled by marketcap
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_126d_base_v038_signal(netmargin, marketcap):
    scaled = _safe_div(netmargin, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d netmargin scaled by marketcap
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_252d_base_v039_signal(netmargin, marketcap):
    scaled = _safe_div(netmargin, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d netmargin scaled by marketcap
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_504d_base_v040_signal(netmargin, marketcap):
    scaled = _safe_div(netmargin, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_low_21d_base_v041_signal(netmargin):
    low = netmargin.rolling(21).min()
    result = _safe_div(netmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_low_63d_base_v042_signal(netmargin):
    low = netmargin.rolling(63).min()
    result = _safe_div(netmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_low_126d_base_v043_signal(netmargin):
    low = netmargin.rolling(126).min()
    result = _safe_div(netmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_low_252d_base_v044_signal(netmargin):
    low = netmargin.rolling(252).min()
    result = _safe_div(netmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_low_504d_base_v045_signal(netmargin):
    low = netmargin.rolling(504).min()
    result = _safe_div(netmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_high_21d_base_v046_signal(netmargin):
    high = netmargin.rolling(21).max()
    result = _safe_div(high - netmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_high_63d_base_v047_signal(netmargin):
    high = netmargin.rolling(63).max()
    result = _safe_div(high - netmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_high_126d_base_v048_signal(netmargin):
    high = netmargin.rolling(126).max()
    result = _safe_div(high - netmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_high_252d_base_v049_signal(netmargin):
    high = netmargin.rolling(252).max()
    result = _safe_div(high - netmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high netmargin
def gm_f46_biotech_f46_net_profit_margin_dist_high_504d_base_v050_signal(netmargin):
    high = netmargin.rolling(504).max()
    result = _safe_div(high - netmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of netmargin
def gm_f46_biotech_f46_net_profit_margin_mom_21d_base_v051_signal(netmargin):
    m1 = _mean(netmargin, 21)
    m2 = _mean(netmargin, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of netmargin
def gm_f46_biotech_f46_net_profit_margin_mom_63d_base_v052_signal(netmargin):
    m1 = _mean(netmargin, 63)
    m2 = _mean(netmargin, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of netmargin
def gm_f46_biotech_f46_net_profit_margin_mom_126d_base_v053_signal(netmargin):
    m1 = _mean(netmargin, 126)
    m2 = _mean(netmargin, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of netmargin
def gm_f46_biotech_f46_net_profit_margin_mom_252d_base_v054_signal(netmargin):
    m1 = _mean(netmargin, 252)
    m2 = _mean(netmargin, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of netmargin
def gm_f46_biotech_f46_net_profit_margin_mom_504d_base_v055_signal(netmargin):
    m1 = _mean(netmargin, 504)
    m2 = _mean(netmargin, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of netmargin
def gm_f46_biotech_f46_net_profit_margin_skew_21d_base_v056_signal(netmargin):
    result = _skew(netmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of netmargin
def gm_f46_biotech_f46_net_profit_margin_skew_63d_base_v057_signal(netmargin):
    result = _skew(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of netmargin
def gm_f46_biotech_f46_net_profit_margin_skew_126d_base_v058_signal(netmargin):
    result = _skew(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of netmargin
def gm_f46_biotech_f46_net_profit_margin_skew_252d_base_v059_signal(netmargin):
    result = _skew(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of netmargin
def gm_f46_biotech_f46_net_profit_margin_skew_504d_base_v060_signal(netmargin):
    result = _skew(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of netmargin
def gm_f46_biotech_f46_net_profit_margin_kurt_21d_base_v061_signal(netmargin):
    result = _kurt(netmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of netmargin
def gm_f46_biotech_f46_net_profit_margin_kurt_63d_base_v062_signal(netmargin):
    result = _kurt(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of netmargin
def gm_f46_biotech_f46_net_profit_margin_kurt_126d_base_v063_signal(netmargin):
    result = _kurt(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of netmargin
def gm_f46_biotech_f46_net_profit_margin_kurt_252d_base_v064_signal(netmargin):
    result = _kurt(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of netmargin
def gm_f46_biotech_f46_net_profit_margin_kurt_504d_base_v065_signal(netmargin):
    result = _kurt(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of netmargin
def gm_f46_biotech_f46_net_profit_margin_rank_21d_base_v066_signal(netmargin, closeadj):
    result = _rank(netmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of netmargin
def gm_f46_biotech_f46_net_profit_margin_rank_63d_base_v067_signal(netmargin, closeadj):
    result = _rank(netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of netmargin
def gm_f46_biotech_f46_net_profit_margin_rank_126d_base_v068_signal(netmargin, closeadj):
    result = _rank(netmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of netmargin
def gm_f46_biotech_f46_net_profit_margin_rank_252d_base_v069_signal(netmargin, closeadj):
    result = _rank(netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of netmargin
def gm_f46_biotech_f46_net_profit_margin_rank_504d_base_v070_signal(netmargin, closeadj):
    result = _rank(netmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of netmargin
def gm_f46_biotech_f46_net_profit_margin_autocorr_21d_base_v071_signal(netmargin):
    result = _autocorr(netmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of netmargin
def gm_f46_biotech_f46_net_profit_margin_autocorr_63d_base_v072_signal(netmargin):
    result = _autocorr(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of netmargin
def gm_f46_biotech_f46_net_profit_margin_autocorr_126d_base_v073_signal(netmargin):
    result = _autocorr(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of netmargin
def gm_f46_biotech_f46_net_profit_margin_autocorr_252d_base_v074_signal(netmargin):
    result = _autocorr(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of netmargin
def gm_f46_biotech_f46_net_profit_margin_autocorr_504d_base_v075_signal(netmargin):
    result = _autocorr(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

