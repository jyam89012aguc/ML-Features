
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_slope_v001_signal(investorname):
    base = _mean(investorname, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_slope_v002_signal(investorname):
    base = _mean(investorname, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_21d_slope_v003_signal(investorname):
    base = _mean(investorname, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_slope_v004_signal(investorname):
    base = _mean(investorname, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_slope_v005_signal(investorname):
    base = _mean(investorname, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_63d_slope_v006_signal(investorname):
    base = _mean(investorname, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_slope_v007_signal(investorname):
    base = _mean(investorname, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_slope_v008_signal(investorname):
    base = _mean(investorname, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_126d_slope_v009_signal(investorname):
    base = _mean(investorname, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_slope_v010_signal(investorname):
    base = _mean(investorname, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_slope_v011_signal(investorname):
    base = _mean(investorname, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_252d_slope_v012_signal(investorname):
    base = _mean(investorname, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_slope_v013_signal(investorname):
    base = _mean(investorname, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_slope_v014_signal(investorname):
    base = _mean(investorname, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw investorname
def gm_f72_biotech_f72_institutional_holder_count_raw_504d_slope_v015_signal(investorname):
    base = _mean(investorname, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_slope_v016_signal(investorname):
    base = _mean(_log(investorname), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_slope_v017_signal(investorname):
    base = _mean(_log(investorname), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_21d_slope_v018_signal(investorname):
    base = _mean(_log(investorname), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_slope_v019_signal(investorname):
    base = _mean(_log(investorname), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_slope_v020_signal(investorname):
    base = _mean(_log(investorname), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_63d_slope_v021_signal(investorname):
    base = _mean(_log(investorname), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_slope_v022_signal(investorname):
    base = _mean(_log(investorname), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_slope_v023_signal(investorname):
    base = _mean(_log(investorname), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_126d_slope_v024_signal(investorname):
    base = _mean(_log(investorname), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_slope_v025_signal(investorname):
    base = _mean(_log(investorname), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_slope_v026_signal(investorname):
    base = _mean(_log(investorname), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_252d_slope_v027_signal(investorname):
    base = _mean(_log(investorname), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_slope_v028_signal(investorname):
    base = _mean(_log(investorname), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_slope_v029_signal(investorname):
    base = _mean(_log(investorname), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log investorname
def gm_f72_biotech_f72_institutional_holder_count_log_504d_slope_v030_signal(investorname):
    base = _mean(_log(investorname), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_slope_v031_signal(investorname):
    base = _z(investorname, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_slope_v032_signal(investorname):
    base = _z(investorname, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_21d_slope_v033_signal(investorname):
    base = _z(investorname, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_slope_v034_signal(investorname):
    base = _z(investorname, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_slope_v035_signal(investorname):
    base = _z(investorname, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_63d_slope_v036_signal(investorname):
    base = _z(investorname, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_slope_v037_signal(investorname):
    base = _z(investorname, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_slope_v038_signal(investorname):
    base = _z(investorname, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_126d_slope_v039_signal(investorname):
    base = _z(investorname, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_slope_v040_signal(investorname):
    base = _z(investorname, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_slope_v041_signal(investorname):
    base = _z(investorname, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_252d_slope_v042_signal(investorname):
    base = _z(investorname, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_slope_v043_signal(investorname):
    base = _z(investorname, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_slope_v044_signal(investorname):
    base = _z(investorname, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z investorname
def gm_f72_biotech_f72_institutional_holder_count_z_504d_slope_v045_signal(investorname):
    base = _z(investorname, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_slope_v046_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_slope_v047_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_21d_slope_v048_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_slope_v049_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_slope_v050_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_63d_slope_v051_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_slope_v052_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_slope_v053_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_126d_slope_v054_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_slope_v055_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_slope_v056_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_252d_slope_v057_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_slope_v058_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_slope_v059_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps investorname
def gm_f72_biotech_f72_institutional_holder_count_ps_504d_slope_v060_signal(investorname, sharesbas):
    base = _safe_div(_mean(investorname, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_slope_v061_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_slope_v062_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_21d_slope_v063_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_slope_v064_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_slope_v065_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_63d_slope_v066_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_slope_v067_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_slope_v068_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_126d_slope_v069_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_slope_v070_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_slope_v071_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_252d_slope_v072_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_slope_v073_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_slope_v074_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_asset_scaled_504d_slope_v075_signal(investorname, assets):
    base = _safe_div(_mean(investorname, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_slope_v076_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_slope_v077_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_21d_slope_v078_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_slope_v079_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_slope_v080_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_63d_slope_v081_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_slope_v082_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_slope_v083_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_126d_slope_v084_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_slope_v085_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_slope_v086_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_252d_slope_v087_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_slope_v088_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_slope_v089_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled investorname
def gm_f72_biotech_f72_institutional_holder_count_mcap_scaled_504d_slope_v090_signal(investorname, marketcap):
    base = _safe_div(_mean(investorname, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_slope_v091_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_slope_v092_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_21d_slope_v093_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(21).min(), investorname.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_slope_v094_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_slope_v095_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_63d_slope_v096_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(63).min(), investorname.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_slope_v097_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_slope_v098_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_126d_slope_v099_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(126).min(), investorname.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_slope_v100_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_slope_v101_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_252d_slope_v102_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(252).min(), investorname.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_slope_v103_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_slope_v104_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_low_504d_slope_v105_signal(investorname):
    base = _safe_div(investorname - investorname.rolling(504).min(), investorname.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_slope_v106_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_slope_v107_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_21d_slope_v108_signal(investorname):
    base = _safe_div(investorname.rolling(21).max() - investorname, investorname.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_slope_v109_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_slope_v110_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_63d_slope_v111_signal(investorname):
    base = _safe_div(investorname.rolling(63).max() - investorname, investorname.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_slope_v112_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_slope_v113_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_126d_slope_v114_signal(investorname):
    base = _safe_div(investorname.rolling(126).max() - investorname, investorname.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_slope_v115_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_slope_v116_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_252d_slope_v117_signal(investorname):
    base = _safe_div(investorname.rolling(252).max() - investorname, investorname.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_slope_v118_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_slope_v119_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high investorname
def gm_f72_biotech_f72_institutional_holder_count_dist_high_504d_slope_v120_signal(investorname):
    base = _safe_div(investorname.rolling(504).max() - investorname, investorname.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_slope_v121_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_slope_v122_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_21d_slope_v123_signal(investorname):
    base = _safe_div(_mean(investorname, 21) - _mean(investorname, 42), _mean(investorname, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_slope_v124_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_slope_v125_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_63d_slope_v126_signal(investorname):
    base = _safe_div(_mean(investorname, 63) - _mean(investorname, 126), _mean(investorname, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_slope_v127_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_slope_v128_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_126d_slope_v129_signal(investorname):
    base = _safe_div(_mean(investorname, 126) - _mean(investorname, 252), _mean(investorname, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_slope_v130_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_slope_v131_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_252d_slope_v132_signal(investorname):
    base = _safe_div(_mean(investorname, 252) - _mean(investorname, 504), _mean(investorname, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_slope_v133_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_slope_v134_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom investorname
def gm_f72_biotech_f72_institutional_holder_count_mom_504d_slope_v135_signal(investorname):
    base = _safe_div(_mean(investorname, 504) - _mean(investorname, 1008), _mean(investorname, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_slope_v136_signal(investorname):
    base = _std(investorname, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_slope_v137_signal(investorname):
    base = _std(investorname, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_21d_slope_v138_signal(investorname):
    base = _std(investorname, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_slope_v139_signal(investorname):
    base = _std(investorname, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_slope_v140_signal(investorname):
    base = _std(investorname, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_63d_slope_v141_signal(investorname):
    base = _std(investorname, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_slope_v142_signal(investorname):
    base = _std(investorname, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_slope_v143_signal(investorname):
    base = _std(investorname, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_126d_slope_v144_signal(investorname):
    base = _std(investorname, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_slope_v145_signal(investorname):
    base = _std(investorname, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_slope_v146_signal(investorname):
    base = _std(investorname, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_252d_slope_v147_signal(investorname):
    base = _std(investorname, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_slope_v148_signal(investorname):
    base = _std(investorname, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_slope_v149_signal(investorname):
    base = _std(investorname, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol investorname
def gm_f72_biotech_f72_institutional_holder_count_vol_504d_slope_v150_signal(investorname):
    base = _std(investorname, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

