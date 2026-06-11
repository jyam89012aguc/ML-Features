
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_raw_21d_base_v001_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_raw_63d_base_v002_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_raw_126d_base_v003_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_raw_252d_base_v004_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_raw_504d_base_v005_signal(grossmargin, closeadj):
    result = _mean(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_log_21d_base_v006_signal(grossmargin, closeadj):
    result = _mean(_log(grossmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_log_63d_base_v007_signal(grossmargin, closeadj):
    result = _mean(_log(grossmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_log_126d_base_v008_signal(grossmargin, closeadj):
    result = _mean(_log(grossmargin), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_log_252d_base_v009_signal(grossmargin, closeadj):
    result = _mean(_log(grossmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed grossmargin
def gm_f44_biotech_f44_gross_profit_margin_log_504d_base_v010_signal(grossmargin, closeadj):
    result = _mean(_log(grossmargin), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_z_21d_base_v011_signal(grossmargin):
    result = _z(grossmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_z_63d_base_v012_signal(grossmargin):
    result = _z(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_z_126d_base_v013_signal(grossmargin):
    result = _z(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_z_252d_base_v014_signal(grossmargin):
    result = _z(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_z_504d_base_v015_signal(grossmargin):
    result = _z(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_pct_21d_base_v016_signal(grossmargin):
    result = _pct_change(grossmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_pct_63d_base_v017_signal(grossmargin):
    result = _pct_change(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_pct_126d_base_v018_signal(grossmargin):
    result = _pct_change(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_pct_252d_base_v019_signal(grossmargin):
    result = _pct_change(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_pct_504d_base_v020_signal(grossmargin):
    result = _pct_change(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share grossmargin
def gm_f44_biotech_f44_gross_profit_margin_ps_21d_base_v021_signal(grossmargin, sharesbas, closeadj):
    ps = _safe_div(grossmargin, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share grossmargin
def gm_f44_biotech_f44_gross_profit_margin_ps_63d_base_v022_signal(grossmargin, sharesbas, closeadj):
    ps = _safe_div(grossmargin, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share grossmargin
def gm_f44_biotech_f44_gross_profit_margin_ps_126d_base_v023_signal(grossmargin, sharesbas, closeadj):
    ps = _safe_div(grossmargin, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share grossmargin
def gm_f44_biotech_f44_gross_profit_margin_ps_252d_base_v024_signal(grossmargin, sharesbas, closeadj):
    ps = _safe_div(grossmargin, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share grossmargin
def gm_f44_biotech_f44_gross_profit_margin_ps_504d_base_v025_signal(grossmargin, sharesbas, closeadj):
    ps = _safe_div(grossmargin, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of grossmargin to revenue
def gm_f44_biotech_f44_gross_profit_margin_ratio_revenue_21d_base_v026_signal(grossmargin, revenue):
    ratio = _safe_div(grossmargin, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of grossmargin to revenue
def gm_f44_biotech_f44_gross_profit_margin_ratio_revenue_63d_base_v027_signal(grossmargin, revenue):
    ratio = _safe_div(grossmargin, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of grossmargin to revenue
def gm_f44_biotech_f44_gross_profit_margin_ratio_revenue_126d_base_v028_signal(grossmargin, revenue):
    ratio = _safe_div(grossmargin, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of grossmargin to revenue
def gm_f44_biotech_f44_gross_profit_margin_ratio_revenue_252d_base_v029_signal(grossmargin, revenue):
    ratio = _safe_div(grossmargin, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of grossmargin to revenue
def gm_f44_biotech_f44_gross_profit_margin_ratio_revenue_504d_base_v030_signal(grossmargin, revenue):
    ratio = _safe_div(grossmargin, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d grossmargin scaled by assets
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_21d_base_v031_signal(grossmargin, assets):
    scaled = _safe_div(grossmargin, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d grossmargin scaled by assets
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_63d_base_v032_signal(grossmargin, assets):
    scaled = _safe_div(grossmargin, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d grossmargin scaled by assets
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_126d_base_v033_signal(grossmargin, assets):
    scaled = _safe_div(grossmargin, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d grossmargin scaled by assets
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_252d_base_v034_signal(grossmargin, assets):
    scaled = _safe_div(grossmargin, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d grossmargin scaled by assets
def gm_f44_biotech_f44_gross_profit_margin_asset_scaled_504d_base_v035_signal(grossmargin, assets):
    scaled = _safe_div(grossmargin, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d grossmargin scaled by marketcap
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_21d_base_v036_signal(grossmargin, marketcap):
    scaled = _safe_div(grossmargin, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d grossmargin scaled by marketcap
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_63d_base_v037_signal(grossmargin, marketcap):
    scaled = _safe_div(grossmargin, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d grossmargin scaled by marketcap
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_126d_base_v038_signal(grossmargin, marketcap):
    scaled = _safe_div(grossmargin, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d grossmargin scaled by marketcap
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_252d_base_v039_signal(grossmargin, marketcap):
    scaled = _safe_div(grossmargin, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d grossmargin scaled by marketcap
def gm_f44_biotech_f44_gross_profit_margin_mcap_scaled_504d_base_v040_signal(grossmargin, marketcap):
    scaled = _safe_div(grossmargin, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_low_21d_base_v041_signal(grossmargin):
    low = grossmargin.rolling(21).min()
    result = _safe_div(grossmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_low_63d_base_v042_signal(grossmargin):
    low = grossmargin.rolling(63).min()
    result = _safe_div(grossmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_low_126d_base_v043_signal(grossmargin):
    low = grossmargin.rolling(126).min()
    result = _safe_div(grossmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_low_252d_base_v044_signal(grossmargin):
    low = grossmargin.rolling(252).min()
    result = _safe_div(grossmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_low_504d_base_v045_signal(grossmargin):
    low = grossmargin.rolling(504).min()
    result = _safe_div(grossmargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_high_21d_base_v046_signal(grossmargin):
    high = grossmargin.rolling(21).max()
    result = _safe_div(high - grossmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_high_63d_base_v047_signal(grossmargin):
    high = grossmargin.rolling(63).max()
    result = _safe_div(high - grossmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_high_126d_base_v048_signal(grossmargin):
    high = grossmargin.rolling(126).max()
    result = _safe_div(high - grossmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_high_252d_base_v049_signal(grossmargin):
    high = grossmargin.rolling(252).max()
    result = _safe_div(high - grossmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high grossmargin
def gm_f44_biotech_f44_gross_profit_margin_dist_high_504d_base_v050_signal(grossmargin):
    high = grossmargin.rolling(504).max()
    result = _safe_div(high - grossmargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_mom_21d_base_v051_signal(grossmargin):
    m1 = _mean(grossmargin, 21)
    m2 = _mean(grossmargin, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_mom_63d_base_v052_signal(grossmargin):
    m1 = _mean(grossmargin, 63)
    m2 = _mean(grossmargin, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_mom_126d_base_v053_signal(grossmargin):
    m1 = _mean(grossmargin, 126)
    m2 = _mean(grossmargin, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_mom_252d_base_v054_signal(grossmargin):
    m1 = _mean(grossmargin, 252)
    m2 = _mean(grossmargin, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_mom_504d_base_v055_signal(grossmargin):
    m1 = _mean(grossmargin, 504)
    m2 = _mean(grossmargin, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_skew_21d_base_v056_signal(grossmargin):
    result = _skew(grossmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_skew_63d_base_v057_signal(grossmargin):
    result = _skew(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_skew_126d_base_v058_signal(grossmargin):
    result = _skew(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_skew_252d_base_v059_signal(grossmargin):
    result = _skew(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_skew_504d_base_v060_signal(grossmargin):
    result = _skew(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_kurt_21d_base_v061_signal(grossmargin):
    result = _kurt(grossmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_kurt_63d_base_v062_signal(grossmargin):
    result = _kurt(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_kurt_126d_base_v063_signal(grossmargin):
    result = _kurt(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_kurt_252d_base_v064_signal(grossmargin):
    result = _kurt(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_kurt_504d_base_v065_signal(grossmargin):
    result = _kurt(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_rank_21d_base_v066_signal(grossmargin, closeadj):
    result = _rank(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_rank_63d_base_v067_signal(grossmargin, closeadj):
    result = _rank(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_rank_126d_base_v068_signal(grossmargin, closeadj):
    result = _rank(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_rank_252d_base_v069_signal(grossmargin, closeadj):
    result = _rank(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_rank_504d_base_v070_signal(grossmargin, closeadj):
    result = _rank(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_autocorr_21d_base_v071_signal(grossmargin):
    result = _autocorr(grossmargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_autocorr_63d_base_v072_signal(grossmargin):
    result = _autocorr(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_autocorr_126d_base_v073_signal(grossmargin):
    result = _autocorr(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_autocorr_252d_base_v074_signal(grossmargin):
    result = _autocorr(grossmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of grossmargin
def gm_f44_biotech_f44_gross_profit_margin_autocorr_504d_base_v075_signal(grossmargin):
    result = _autocorr(grossmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

