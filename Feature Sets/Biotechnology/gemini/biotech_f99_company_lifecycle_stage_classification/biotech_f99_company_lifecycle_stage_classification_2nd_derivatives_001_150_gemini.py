
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_21d_slope_v001_signal(revenue):
    base = _mean(revenue, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_21d_slope_v002_signal(revenue):
    base = _mean(revenue, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_21d_slope_v003_signal(revenue):
    base = _mean(revenue, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_63d_slope_v004_signal(revenue):
    base = _mean(revenue, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_63d_slope_v005_signal(revenue):
    base = _mean(revenue, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_63d_slope_v006_signal(revenue):
    base = _mean(revenue, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_126d_slope_v007_signal(revenue):
    base = _mean(revenue, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_126d_slope_v008_signal(revenue):
    base = _mean(revenue, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_126d_slope_v009_signal(revenue):
    base = _mean(revenue, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_252d_slope_v010_signal(revenue):
    base = _mean(revenue, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_252d_slope_v011_signal(revenue):
    base = _mean(revenue, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_252d_slope_v012_signal(revenue):
    base = _mean(revenue, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_504d_slope_v013_signal(revenue):
    base = _mean(revenue, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_504d_slope_v014_signal(revenue):
    base = _mean(revenue, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_raw_504d_slope_v015_signal(revenue):
    base = _mean(revenue, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_21d_slope_v016_signal(revenue):
    base = _mean(_log(revenue), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_21d_slope_v017_signal(revenue):
    base = _mean(_log(revenue), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_21d_slope_v018_signal(revenue):
    base = _mean(_log(revenue), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_63d_slope_v019_signal(revenue):
    base = _mean(_log(revenue), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_63d_slope_v020_signal(revenue):
    base = _mean(_log(revenue), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_63d_slope_v021_signal(revenue):
    base = _mean(_log(revenue), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_126d_slope_v022_signal(revenue):
    base = _mean(_log(revenue), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_126d_slope_v023_signal(revenue):
    base = _mean(_log(revenue), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_126d_slope_v024_signal(revenue):
    base = _mean(_log(revenue), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_252d_slope_v025_signal(revenue):
    base = _mean(_log(revenue), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_252d_slope_v026_signal(revenue):
    base = _mean(_log(revenue), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_252d_slope_v027_signal(revenue):
    base = _mean(_log(revenue), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_504d_slope_v028_signal(revenue):
    base = _mean(_log(revenue), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_504d_slope_v029_signal(revenue):
    base = _mean(_log(revenue), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_log_504d_slope_v030_signal(revenue):
    base = _mean(_log(revenue), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_21d_slope_v031_signal(revenue):
    base = _z(revenue, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_21d_slope_v032_signal(revenue):
    base = _z(revenue, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_21d_slope_v033_signal(revenue):
    base = _z(revenue, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_63d_slope_v034_signal(revenue):
    base = _z(revenue, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_63d_slope_v035_signal(revenue):
    base = _z(revenue, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_63d_slope_v036_signal(revenue):
    base = _z(revenue, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_126d_slope_v037_signal(revenue):
    base = _z(revenue, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_126d_slope_v038_signal(revenue):
    base = _z(revenue, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_126d_slope_v039_signal(revenue):
    base = _z(revenue, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_252d_slope_v040_signal(revenue):
    base = _z(revenue, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_252d_slope_v041_signal(revenue):
    base = _z(revenue, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_252d_slope_v042_signal(revenue):
    base = _z(revenue, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_504d_slope_v043_signal(revenue):
    base = _z(revenue, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_504d_slope_v044_signal(revenue):
    base = _z(revenue, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_z_504d_slope_v045_signal(revenue):
    base = _z(revenue, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_21d_slope_v046_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_21d_slope_v047_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_21d_slope_v048_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_63d_slope_v049_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_63d_slope_v050_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_63d_slope_v051_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_126d_slope_v052_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_126d_slope_v053_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_126d_slope_v054_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_252d_slope_v055_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_252d_slope_v056_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_252d_slope_v057_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_504d_slope_v058_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_504d_slope_v059_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ps_504d_slope_v060_signal(revenue, sharesbas):
    base = _safe_div(_mean(revenue, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_21d_slope_v061_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_21d_slope_v062_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_21d_slope_v063_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_63d_slope_v064_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_63d_slope_v065_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_63d_slope_v066_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_126d_slope_v067_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_126d_slope_v068_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_126d_slope_v069_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_252d_slope_v070_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_252d_slope_v071_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_252d_slope_v072_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_504d_slope_v073_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_504d_slope_v074_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_asset_scaled_504d_slope_v075_signal(revenue, assets):
    base = _safe_div(_mean(revenue, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_21d_slope_v076_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_21d_slope_v077_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_21d_slope_v078_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_63d_slope_v079_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_63d_slope_v080_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_63d_slope_v081_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_126d_slope_v082_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_126d_slope_v083_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_126d_slope_v084_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_252d_slope_v085_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_252d_slope_v086_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_252d_slope_v087_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_504d_slope_v088_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_504d_slope_v089_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mcap_scaled_504d_slope_v090_signal(revenue, marketcap):
    base = _safe_div(_mean(revenue, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_21d_slope_v091_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_21d_slope_v092_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_21d_slope_v093_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(21).min(), revenue.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_63d_slope_v094_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_63d_slope_v095_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_63d_slope_v096_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(63).min(), revenue.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_126d_slope_v097_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_126d_slope_v098_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_126d_slope_v099_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(126).min(), revenue.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_252d_slope_v100_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_252d_slope_v101_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_252d_slope_v102_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(252).min(), revenue.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_504d_slope_v103_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_504d_slope_v104_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_low_504d_slope_v105_signal(revenue):
    base = _safe_div(revenue - revenue.rolling(504).min(), revenue.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_21d_slope_v106_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_21d_slope_v107_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_21d_slope_v108_signal(revenue):
    base = _safe_div(revenue.rolling(21).max() - revenue, revenue.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_63d_slope_v109_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_63d_slope_v110_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_63d_slope_v111_signal(revenue):
    base = _safe_div(revenue.rolling(63).max() - revenue, revenue.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_126d_slope_v112_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_126d_slope_v113_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_126d_slope_v114_signal(revenue):
    base = _safe_div(revenue.rolling(126).max() - revenue, revenue.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_252d_slope_v115_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_252d_slope_v116_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_252d_slope_v117_signal(revenue):
    base = _safe_div(revenue.rolling(252).max() - revenue, revenue.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_504d_slope_v118_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_504d_slope_v119_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_dist_high_504d_slope_v120_signal(revenue):
    base = _safe_div(revenue.rolling(504).max() - revenue, revenue.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_21d_slope_v121_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_21d_slope_v122_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_21d_slope_v123_signal(revenue):
    base = _safe_div(_mean(revenue, 21) - _mean(revenue, 42), _mean(revenue, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_63d_slope_v124_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_63d_slope_v125_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_63d_slope_v126_signal(revenue):
    base = _safe_div(_mean(revenue, 63) - _mean(revenue, 126), _mean(revenue, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_126d_slope_v127_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_126d_slope_v128_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_126d_slope_v129_signal(revenue):
    base = _safe_div(_mean(revenue, 126) - _mean(revenue, 252), _mean(revenue, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_252d_slope_v130_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_252d_slope_v131_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_252d_slope_v132_signal(revenue):
    base = _safe_div(_mean(revenue, 252) - _mean(revenue, 504), _mean(revenue, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_504d_slope_v133_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_504d_slope_v134_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mom_504d_slope_v135_signal(revenue):
    base = _safe_div(_mean(revenue, 504) - _mean(revenue, 1008), _mean(revenue, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_21d_slope_v136_signal(revenue):
    base = _std(revenue, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_21d_slope_v137_signal(revenue):
    base = _std(revenue, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_21d_slope_v138_signal(revenue):
    base = _std(revenue, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_63d_slope_v139_signal(revenue):
    base = _std(revenue, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_63d_slope_v140_signal(revenue):
    base = _std(revenue, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_63d_slope_v141_signal(revenue):
    base = _std(revenue, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_126d_slope_v142_signal(revenue):
    base = _std(revenue, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_126d_slope_v143_signal(revenue):
    base = _std(revenue, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_126d_slope_v144_signal(revenue):
    base = _std(revenue, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_252d_slope_v145_signal(revenue):
    base = _std(revenue, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_252d_slope_v146_signal(revenue):
    base = _std(revenue, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_252d_slope_v147_signal(revenue):
    base = _std(revenue, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_504d_slope_v148_signal(revenue):
    base = _std(revenue, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_504d_slope_v149_signal(revenue):
    base = _std(revenue, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_vol_504d_slope_v150_signal(revenue):
    base = _std(revenue, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

