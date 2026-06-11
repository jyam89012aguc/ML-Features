
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_raw_21d_base_v001_signal(ebitdamargin, closeadj):
    result = _mean(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_raw_63d_base_v002_signal(ebitdamargin, closeadj):
    result = _mean(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_raw_126d_base_v003_signal(ebitdamargin, closeadj):
    result = _mean(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_raw_252d_base_v004_signal(ebitdamargin, closeadj):
    result = _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_raw_504d_base_v005_signal(ebitdamargin, closeadj):
    result = _mean(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_log_21d_base_v006_signal(ebitdamargin, closeadj):
    result = _mean(_log(ebitdamargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_log_63d_base_v007_signal(ebitdamargin, closeadj):
    result = _mean(_log(ebitdamargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_log_126d_base_v008_signal(ebitdamargin, closeadj):
    result = _mean(_log(ebitdamargin), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_log_252d_base_v009_signal(ebitdamargin, closeadj):
    result = _mean(_log(ebitdamargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_log_504d_base_v010_signal(ebitdamargin, closeadj):
    result = _mean(_log(ebitdamargin), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_z_21d_base_v011_signal(ebitdamargin):
    result = _z(ebitdamargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_z_63d_base_v012_signal(ebitdamargin):
    result = _z(ebitdamargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_z_126d_base_v013_signal(ebitdamargin):
    result = _z(ebitdamargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_z_252d_base_v014_signal(ebitdamargin):
    result = _z(ebitdamargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_z_504d_base_v015_signal(ebitdamargin):
    result = _z(ebitdamargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_pct_21d_base_v016_signal(ebitdamargin):
    result = _pct_change(ebitdamargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_pct_63d_base_v017_signal(ebitdamargin):
    result = _pct_change(ebitdamargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_pct_126d_base_v018_signal(ebitdamargin):
    result = _pct_change(ebitdamargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_pct_252d_base_v019_signal(ebitdamargin):
    result = _pct_change(ebitdamargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_pct_504d_base_v020_signal(ebitdamargin):
    result = _pct_change(ebitdamargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_ps_21d_base_v021_signal(ebitdamargin, sharesbas, closeadj):
    ps = _safe_div(ebitdamargin, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_ps_63d_base_v022_signal(ebitdamargin, sharesbas, closeadj):
    ps = _safe_div(ebitdamargin, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_ps_126d_base_v023_signal(ebitdamargin, sharesbas, closeadj):
    ps = _safe_div(ebitdamargin, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_ps_252d_base_v024_signal(ebitdamargin, sharesbas, closeadj):
    ps = _safe_div(ebitdamargin, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_ps_504d_base_v025_signal(ebitdamargin, sharesbas, closeadj):
    ps = _safe_div(ebitdamargin, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of ebitdamargin to revenue
def gm_f45_biotech_f45_operating_profit_margin_ratio_revenue_21d_base_v026_signal(ebitdamargin, revenue):
    ratio = _safe_div(ebitdamargin, revenue)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of ebitdamargin to revenue
def gm_f45_biotech_f45_operating_profit_margin_ratio_revenue_63d_base_v027_signal(ebitdamargin, revenue):
    ratio = _safe_div(ebitdamargin, revenue)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of ebitdamargin to revenue
def gm_f45_biotech_f45_operating_profit_margin_ratio_revenue_126d_base_v028_signal(ebitdamargin, revenue):
    ratio = _safe_div(ebitdamargin, revenue)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of ebitdamargin to revenue
def gm_f45_biotech_f45_operating_profit_margin_ratio_revenue_252d_base_v029_signal(ebitdamargin, revenue):
    ratio = _safe_div(ebitdamargin, revenue)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of ebitdamargin to revenue
def gm_f45_biotech_f45_operating_profit_margin_ratio_revenue_504d_base_v030_signal(ebitdamargin, revenue):
    ratio = _safe_div(ebitdamargin, revenue)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ebitdamargin scaled by assets
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_21d_base_v031_signal(ebitdamargin, assets):
    scaled = _safe_div(ebitdamargin, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ebitdamargin scaled by assets
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_63d_base_v032_signal(ebitdamargin, assets):
    scaled = _safe_div(ebitdamargin, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ebitdamargin scaled by assets
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_126d_base_v033_signal(ebitdamargin, assets):
    scaled = _safe_div(ebitdamargin, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ebitdamargin scaled by assets
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_252d_base_v034_signal(ebitdamargin, assets):
    scaled = _safe_div(ebitdamargin, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ebitdamargin scaled by assets
def gm_f45_biotech_f45_operating_profit_margin_asset_scaled_504d_base_v035_signal(ebitdamargin, assets):
    scaled = _safe_div(ebitdamargin, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ebitdamargin scaled by marketcap
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_21d_base_v036_signal(ebitdamargin, marketcap):
    scaled = _safe_div(ebitdamargin, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ebitdamargin scaled by marketcap
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_63d_base_v037_signal(ebitdamargin, marketcap):
    scaled = _safe_div(ebitdamargin, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ebitdamargin scaled by marketcap
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_126d_base_v038_signal(ebitdamargin, marketcap):
    scaled = _safe_div(ebitdamargin, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ebitdamargin scaled by marketcap
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_252d_base_v039_signal(ebitdamargin, marketcap):
    scaled = _safe_div(ebitdamargin, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ebitdamargin scaled by marketcap
def gm_f45_biotech_f45_operating_profit_margin_mcap_scaled_504d_base_v040_signal(ebitdamargin, marketcap):
    scaled = _safe_div(ebitdamargin, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_low_21d_base_v041_signal(ebitdamargin):
    low = ebitdamargin.rolling(21).min()
    result = _safe_div(ebitdamargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_low_63d_base_v042_signal(ebitdamargin):
    low = ebitdamargin.rolling(63).min()
    result = _safe_div(ebitdamargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_low_126d_base_v043_signal(ebitdamargin):
    low = ebitdamargin.rolling(126).min()
    result = _safe_div(ebitdamargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_low_252d_base_v044_signal(ebitdamargin):
    low = ebitdamargin.rolling(252).min()
    result = _safe_div(ebitdamargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_low_504d_base_v045_signal(ebitdamargin):
    low = ebitdamargin.rolling(504).min()
    result = _safe_div(ebitdamargin - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_high_21d_base_v046_signal(ebitdamargin):
    high = ebitdamargin.rolling(21).max()
    result = _safe_div(high - ebitdamargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_high_63d_base_v047_signal(ebitdamargin):
    high = ebitdamargin.rolling(63).max()
    result = _safe_div(high - ebitdamargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_high_126d_base_v048_signal(ebitdamargin):
    high = ebitdamargin.rolling(126).max()
    result = _safe_div(high - ebitdamargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_high_252d_base_v049_signal(ebitdamargin):
    high = ebitdamargin.rolling(252).max()
    result = _safe_div(high - ebitdamargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_dist_high_504d_base_v050_signal(ebitdamargin):
    high = ebitdamargin.rolling(504).max()
    result = _safe_div(high - ebitdamargin, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_mom_21d_base_v051_signal(ebitdamargin):
    m1 = _mean(ebitdamargin, 21)
    m2 = _mean(ebitdamargin, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_mom_63d_base_v052_signal(ebitdamargin):
    m1 = _mean(ebitdamargin, 63)
    m2 = _mean(ebitdamargin, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_mom_126d_base_v053_signal(ebitdamargin):
    m1 = _mean(ebitdamargin, 126)
    m2 = _mean(ebitdamargin, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_mom_252d_base_v054_signal(ebitdamargin):
    m1 = _mean(ebitdamargin, 252)
    m2 = _mean(ebitdamargin, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_mom_504d_base_v055_signal(ebitdamargin):
    m1 = _mean(ebitdamargin, 504)
    m2 = _mean(ebitdamargin, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_skew_21d_base_v056_signal(ebitdamargin):
    result = _skew(ebitdamargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_skew_63d_base_v057_signal(ebitdamargin):
    result = _skew(ebitdamargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_skew_126d_base_v058_signal(ebitdamargin):
    result = _skew(ebitdamargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_skew_252d_base_v059_signal(ebitdamargin):
    result = _skew(ebitdamargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_skew_504d_base_v060_signal(ebitdamargin):
    result = _skew(ebitdamargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_kurt_21d_base_v061_signal(ebitdamargin):
    result = _kurt(ebitdamargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_kurt_63d_base_v062_signal(ebitdamargin):
    result = _kurt(ebitdamargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_kurt_126d_base_v063_signal(ebitdamargin):
    result = _kurt(ebitdamargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_kurt_252d_base_v064_signal(ebitdamargin):
    result = _kurt(ebitdamargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_kurt_504d_base_v065_signal(ebitdamargin):
    result = _kurt(ebitdamargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_rank_21d_base_v066_signal(ebitdamargin, closeadj):
    result = _rank(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_rank_63d_base_v067_signal(ebitdamargin, closeadj):
    result = _rank(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_rank_126d_base_v068_signal(ebitdamargin, closeadj):
    result = _rank(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_rank_252d_base_v069_signal(ebitdamargin, closeadj):
    result = _rank(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_rank_504d_base_v070_signal(ebitdamargin, closeadj):
    result = _rank(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_autocorr_21d_base_v071_signal(ebitdamargin):
    result = _autocorr(ebitdamargin, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_autocorr_63d_base_v072_signal(ebitdamargin):
    result = _autocorr(ebitdamargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_autocorr_126d_base_v073_signal(ebitdamargin):
    result = _autocorr(ebitdamargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_autocorr_252d_base_v074_signal(ebitdamargin):
    result = _autocorr(ebitdamargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ebitdamargin
def gm_f45_biotech_f45_operating_profit_margin_autocorr_504d_base_v075_signal(ebitdamargin):
    result = _autocorr(ebitdamargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)

