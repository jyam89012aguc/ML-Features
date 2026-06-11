
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d smoothed assets
def gm_f08_biotech_f08_tangible_book_value_raw_21d_base_v001_signal(assets, closeadj):
    result = _mean(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smoothed assets
def gm_f08_biotech_f08_tangible_book_value_raw_63d_base_v002_signal(assets, closeadj):
    result = _mean(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smoothed assets
def gm_f08_biotech_f08_tangible_book_value_raw_126d_base_v003_signal(assets, closeadj):
    result = _mean(assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smoothed assets
def gm_f08_biotech_f08_tangible_book_value_raw_252d_base_v004_signal(assets, closeadj):
    result = _mean(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smoothed assets
def gm_f08_biotech_f08_tangible_book_value_raw_504d_base_v005_signal(assets, closeadj):
    result = _mean(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-smoothed assets
def gm_f08_biotech_f08_tangible_book_value_log_21d_base_v006_signal(assets, closeadj):
    result = _mean(_log(assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-smoothed assets
def gm_f08_biotech_f08_tangible_book_value_log_63d_base_v007_signal(assets, closeadj):
    result = _mean(_log(assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-smoothed assets
def gm_f08_biotech_f08_tangible_book_value_log_126d_base_v008_signal(assets, closeadj):
    result = _mean(_log(assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-smoothed assets
def gm_f08_biotech_f08_tangible_book_value_log_252d_base_v009_signal(assets, closeadj):
    result = _mean(_log(assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-smoothed assets
def gm_f08_biotech_f08_tangible_book_value_log_504d_base_v010_signal(assets, closeadj):
    result = _mean(_log(assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d z-score of assets
def gm_f08_biotech_f08_tangible_book_value_z_21d_base_v011_signal(assets):
    result = _z(assets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assets
def gm_f08_biotech_f08_tangible_book_value_z_63d_base_v012_signal(assets):
    result = _z(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assets
def gm_f08_biotech_f08_tangible_book_value_z_126d_base_v013_signal(assets):
    result = _z(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assets
def gm_f08_biotech_f08_tangible_book_value_z_252d_base_v014_signal(assets):
    result = _z(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assets
def gm_f08_biotech_f08_tangible_book_value_z_504d_base_v015_signal(assets):
    result = _z(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct change of assets
def gm_f08_biotech_f08_tangible_book_value_pct_21d_base_v016_signal(assets):
    result = _pct_change(assets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct change of assets
def gm_f08_biotech_f08_tangible_book_value_pct_63d_base_v017_signal(assets):
    result = _pct_change(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d pct change of assets
def gm_f08_biotech_f08_tangible_book_value_pct_126d_base_v018_signal(assets):
    result = _pct_change(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct change of assets
def gm_f08_biotech_f08_tangible_book_value_pct_252d_base_v019_signal(assets):
    result = _pct_change(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d pct change of assets
def gm_f08_biotech_f08_tangible_book_value_pct_504d_base_v020_signal(assets):
    result = _pct_change(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d per-share assets
def gm_f08_biotech_f08_tangible_book_value_ps_21d_base_v021_signal(assets, sharesbas, closeadj):
    ps = _safe_div(assets, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d per-share assets
def gm_f08_biotech_f08_tangible_book_value_ps_63d_base_v022_signal(assets, sharesbas, closeadj):
    ps = _safe_div(assets, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d per-share assets
def gm_f08_biotech_f08_tangible_book_value_ps_126d_base_v023_signal(assets, sharesbas, closeadj):
    ps = _safe_div(assets, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d per-share assets
def gm_f08_biotech_f08_tangible_book_value_ps_252d_base_v024_signal(assets, sharesbas, closeadj):
    ps = _safe_div(assets, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d per-share assets
def gm_f08_biotech_f08_tangible_book_value_ps_504d_base_v025_signal(assets, sharesbas, closeadj):
    ps = _safe_div(assets, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assets to intangibles
def gm_f08_biotech_f08_tangible_book_value_ratio_intangibles_21d_base_v026_signal(assets, intangibles):
    ratio = _safe_div(assets, intangibles)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assets to intangibles
def gm_f08_biotech_f08_tangible_book_value_ratio_intangibles_63d_base_v027_signal(assets, intangibles):
    ratio = _safe_div(assets, intangibles)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assets to intangibles
def gm_f08_biotech_f08_tangible_book_value_ratio_intangibles_126d_base_v028_signal(assets, intangibles):
    ratio = _safe_div(assets, intangibles)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assets to intangibles
def gm_f08_biotech_f08_tangible_book_value_ratio_intangibles_252d_base_v029_signal(assets, intangibles):
    ratio = _safe_div(assets, intangibles)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assets to intangibles
def gm_f08_biotech_f08_tangible_book_value_ratio_intangibles_504d_base_v030_signal(assets, intangibles):
    ratio = _safe_div(assets, intangibles)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ratio of assets to liabilities
def gm_f08_biotech_f08_tangible_book_value_ratio_liabilities_21d_base_v031_signal(assets, liabilities):
    ratio = _safe_div(assets, liabilities)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ratio of assets to liabilities
def gm_f08_biotech_f08_tangible_book_value_ratio_liabilities_63d_base_v032_signal(assets, liabilities):
    ratio = _safe_div(assets, liabilities)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ratio of assets to liabilities
def gm_f08_biotech_f08_tangible_book_value_ratio_liabilities_126d_base_v033_signal(assets, liabilities):
    ratio = _safe_div(assets, liabilities)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ratio of assets to liabilities
def gm_f08_biotech_f08_tangible_book_value_ratio_liabilities_252d_base_v034_signal(assets, liabilities):
    ratio = _safe_div(assets, liabilities)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ratio of assets to liabilities
def gm_f08_biotech_f08_tangible_book_value_ratio_liabilities_504d_base_v035_signal(assets, liabilities):
    ratio = _safe_div(assets, liabilities)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assets scaled by assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_21d_base_v036_signal(assets):
    scaled = _safe_div(assets, assets)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assets scaled by assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_63d_base_v037_signal(assets):
    scaled = _safe_div(assets, assets)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assets scaled by assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_126d_base_v038_signal(assets):
    scaled = _safe_div(assets, assets)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assets scaled by assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_252d_base_v039_signal(assets):
    scaled = _safe_div(assets, assets)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assets scaled by assets
def gm_f08_biotech_f08_tangible_book_value_asset_scaled_504d_base_v040_signal(assets):
    scaled = _safe_div(assets, assets)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d assets scaled by marketcap
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_21d_base_v041_signal(assets, marketcap):
    scaled = _safe_div(assets, marketcap)
    result = _mean(scaled, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d assets scaled by marketcap
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_63d_base_v042_signal(assets, marketcap):
    scaled = _safe_div(assets, marketcap)
    result = _mean(scaled, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d assets scaled by marketcap
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_126d_base_v043_signal(assets, marketcap):
    scaled = _safe_div(assets, marketcap)
    result = _mean(scaled, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d assets scaled by marketcap
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_252d_base_v044_signal(assets, marketcap):
    scaled = _safe_div(assets, marketcap)
    result = _mean(scaled, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d assets scaled by marketcap
def gm_f08_biotech_f08_tangible_book_value_mcap_scaled_504d_base_v045_signal(assets, marketcap):
    scaled = _safe_div(assets, marketcap)
    result = _mean(scaled, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_21d_base_v046_signal(assets):
    low = assets.rolling(21).min()
    result = _safe_div(assets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_63d_base_v047_signal(assets):
    low = assets.rolling(63).min()
    result = _safe_div(assets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_126d_base_v048_signal(assets):
    low = assets.rolling(126).min()
    result = _safe_div(assets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_252d_base_v049_signal(assets):
    low = assets.rolling(252).min()
    result = _safe_div(assets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling low assets
def gm_f08_biotech_f08_tangible_book_value_dist_low_504d_base_v050_signal(assets):
    low = assets.rolling(504).min()
    result = _safe_div(assets - low, low.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d distance from rolling high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_21d_base_v051_signal(assets):
    high = assets.rolling(21).max()
    result = _safe_div(high - assets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d distance from rolling high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_63d_base_v052_signal(assets):
    high = assets.rolling(63).max()
    result = _safe_div(high - assets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_126d_base_v053_signal(assets):
    high = assets.rolling(126).max()
    result = _safe_div(high - assets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_252d_base_v054_signal(assets):
    high = assets.rolling(252).max()
    result = _safe_div(high - assets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling high assets
def gm_f08_biotech_f08_tangible_book_value_dist_high_504d_base_v055_signal(assets):
    high = assets.rolling(504).max()
    result = _safe_div(high - assets, high.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level momentum of assets
def gm_f08_biotech_f08_tangible_book_value_mom_21d_base_v056_signal(assets):
    m1 = _mean(assets, 21)
    m2 = _mean(assets, 42)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d level momentum of assets
def gm_f08_biotech_f08_tangible_book_value_mom_63d_base_v057_signal(assets):
    m1 = _mean(assets, 63)
    m2 = _mean(assets, 126)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level momentum of assets
def gm_f08_biotech_f08_tangible_book_value_mom_126d_base_v058_signal(assets):
    m1 = _mean(assets, 126)
    m2 = _mean(assets, 252)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level momentum of assets
def gm_f08_biotech_f08_tangible_book_value_mom_252d_base_v059_signal(assets):
    m1 = _mean(assets, 252)
    m2 = _mean(assets, 504)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level momentum of assets
def gm_f08_biotech_f08_tangible_book_value_mom_504d_base_v060_signal(assets):
    m1 = _mean(assets, 504)
    m2 = _mean(assets, 1008)
    result = _safe_div(m1 - m2, m2.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling skew of assets
def gm_f08_biotech_f08_tangible_book_value_skew_21d_base_v061_signal(assets):
    result = _skew(assets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling skew of assets
def gm_f08_biotech_f08_tangible_book_value_skew_63d_base_v062_signal(assets):
    result = _skew(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling skew of assets
def gm_f08_biotech_f08_tangible_book_value_skew_126d_base_v063_signal(assets):
    result = _skew(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling skew of assets
def gm_f08_biotech_f08_tangible_book_value_skew_252d_base_v064_signal(assets):
    result = _skew(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling skew of assets
def gm_f08_biotech_f08_tangible_book_value_skew_504d_base_v065_signal(assets):
    result = _skew(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling kurtosis of assets
def gm_f08_biotech_f08_tangible_book_value_kurt_21d_base_v066_signal(assets):
    result = _kurt(assets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of assets
def gm_f08_biotech_f08_tangible_book_value_kurt_63d_base_v067_signal(assets):
    result = _kurt(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of assets
def gm_f08_biotech_f08_tangible_book_value_kurt_126d_base_v068_signal(assets):
    result = _kurt(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of assets
def gm_f08_biotech_f08_tangible_book_value_kurt_252d_base_v069_signal(assets):
    result = _kurt(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of assets
def gm_f08_biotech_f08_tangible_book_value_kurt_504d_base_v070_signal(assets):
    result = _kurt(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of assets
def gm_f08_biotech_f08_tangible_book_value_rank_21d_base_v071_signal(assets, closeadj):
    result = _rank(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of assets
def gm_f08_biotech_f08_tangible_book_value_rank_63d_base_v072_signal(assets, closeadj):
    result = _rank(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of assets
def gm_f08_biotech_f08_tangible_book_value_rank_126d_base_v073_signal(assets, closeadj):
    result = _rank(assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of assets
def gm_f08_biotech_f08_tangible_book_value_rank_252d_base_v074_signal(assets, closeadj):
    result = _rank(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of assets
def gm_f08_biotech_f08_tangible_book_value_rank_504d_base_v075_signal(assets, closeadj):
    result = _rank(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

