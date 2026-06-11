
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_slope_v001_signal(ev):
    base = _mean(ev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_slope_v002_signal(ev):
    base = _mean(ev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_21d_slope_v003_signal(ev):
    base = _mean(ev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_slope_v004_signal(ev):
    base = _mean(ev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_slope_v005_signal(ev):
    base = _mean(ev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_63d_slope_v006_signal(ev):
    base = _mean(ev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_slope_v007_signal(ev):
    base = _mean(ev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_slope_v008_signal(ev):
    base = _mean(ev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_126d_slope_v009_signal(ev):
    base = _mean(ev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_slope_v010_signal(ev):
    base = _mean(ev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_slope_v011_signal(ev):
    base = _mean(ev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_252d_slope_v012_signal(ev):
    base = _mean(ev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_slope_v013_signal(ev):
    base = _mean(ev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_slope_v014_signal(ev):
    base = _mean(ev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_raw_504d_slope_v015_signal(ev):
    base = _mean(ev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_slope_v016_signal(ev):
    base = _mean(_log(ev), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_slope_v017_signal(ev):
    base = _mean(_log(ev), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_21d_slope_v018_signal(ev):
    base = _mean(_log(ev), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_slope_v019_signal(ev):
    base = _mean(_log(ev), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_slope_v020_signal(ev):
    base = _mean(_log(ev), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_63d_slope_v021_signal(ev):
    base = _mean(_log(ev), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_slope_v022_signal(ev):
    base = _mean(_log(ev), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_slope_v023_signal(ev):
    base = _mean(_log(ev), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_126d_slope_v024_signal(ev):
    base = _mean(_log(ev), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_slope_v025_signal(ev):
    base = _mean(_log(ev), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_slope_v026_signal(ev):
    base = _mean(_log(ev), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_252d_slope_v027_signal(ev):
    base = _mean(_log(ev), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_slope_v028_signal(ev):
    base = _mean(_log(ev), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_slope_v029_signal(ev):
    base = _mean(_log(ev), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_log_504d_slope_v030_signal(ev):
    base = _mean(_log(ev), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_slope_v031_signal(ev):
    base = _z(ev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_slope_v032_signal(ev):
    base = _z(ev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_21d_slope_v033_signal(ev):
    base = _z(ev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_slope_v034_signal(ev):
    base = _z(ev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_slope_v035_signal(ev):
    base = _z(ev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_63d_slope_v036_signal(ev):
    base = _z(ev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_slope_v037_signal(ev):
    base = _z(ev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_slope_v038_signal(ev):
    base = _z(ev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_126d_slope_v039_signal(ev):
    base = _z(ev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_slope_v040_signal(ev):
    base = _z(ev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_slope_v041_signal(ev):
    base = _z(ev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_252d_slope_v042_signal(ev):
    base = _z(ev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_slope_v043_signal(ev):
    base = _z(ev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_slope_v044_signal(ev):
    base = _z(ev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_z_504d_slope_v045_signal(ev):
    base = _z(ev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_slope_v046_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_slope_v047_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_21d_slope_v048_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_slope_v049_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_slope_v050_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_63d_slope_v051_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_slope_v052_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_slope_v053_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_126d_slope_v054_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_slope_v055_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_slope_v056_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_252d_slope_v057_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_slope_v058_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_slope_v059_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_ps_504d_slope_v060_signal(ev, sharesbas):
    base = _safe_div(_mean(ev, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_slope_v061_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_slope_v062_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_21d_slope_v063_signal(ev, assets):
    base = _safe_div(_mean(ev, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_slope_v064_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_slope_v065_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_63d_slope_v066_signal(ev, assets):
    base = _safe_div(_mean(ev, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_slope_v067_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_slope_v068_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_126d_slope_v069_signal(ev, assets):
    base = _safe_div(_mean(ev, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_slope_v070_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_slope_v071_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_252d_slope_v072_signal(ev, assets):
    base = _safe_div(_mean(ev, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_slope_v073_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_slope_v074_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_asset_scaled_504d_slope_v075_signal(ev, assets):
    base = _safe_div(_mean(ev, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_slope_v076_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_slope_v077_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_21d_slope_v078_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_slope_v079_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_slope_v080_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_63d_slope_v081_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_slope_v082_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_slope_v083_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_126d_slope_v084_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_slope_v085_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_slope_v086_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_252d_slope_v087_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_slope_v088_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_slope_v089_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mcap_scaled_504d_slope_v090_signal(ev, marketcap):
    base = _safe_div(_mean(ev, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_slope_v091_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_slope_v092_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_21d_slope_v093_signal(ev):
    base = _safe_div(ev - ev.rolling(21).min(), ev.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_slope_v094_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_slope_v095_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_63d_slope_v096_signal(ev):
    base = _safe_div(ev - ev.rolling(63).min(), ev.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_slope_v097_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_slope_v098_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_126d_slope_v099_signal(ev):
    base = _safe_div(ev - ev.rolling(126).min(), ev.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_slope_v100_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_slope_v101_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_252d_slope_v102_signal(ev):
    base = _safe_div(ev - ev.rolling(252).min(), ev.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_slope_v103_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_slope_v104_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_low_504d_slope_v105_signal(ev):
    base = _safe_div(ev - ev.rolling(504).min(), ev.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_slope_v106_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_slope_v107_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_21d_slope_v108_signal(ev):
    base = _safe_div(ev.rolling(21).max() - ev, ev.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_slope_v109_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_slope_v110_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_63d_slope_v111_signal(ev):
    base = _safe_div(ev.rolling(63).max() - ev, ev.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_slope_v112_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_slope_v113_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_126d_slope_v114_signal(ev):
    base = _safe_div(ev.rolling(126).max() - ev, ev.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_slope_v115_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_slope_v116_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_252d_slope_v117_signal(ev):
    base = _safe_div(ev.rolling(252).max() - ev, ev.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_slope_v118_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_slope_v119_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_dist_high_504d_slope_v120_signal(ev):
    base = _safe_div(ev.rolling(504).max() - ev, ev.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_slope_v121_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_slope_v122_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_21d_slope_v123_signal(ev):
    base = _safe_div(_mean(ev, 21) - _mean(ev, 42), _mean(ev, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_slope_v124_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_slope_v125_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_63d_slope_v126_signal(ev):
    base = _safe_div(_mean(ev, 63) - _mean(ev, 126), _mean(ev, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_slope_v127_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_slope_v128_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_126d_slope_v129_signal(ev):
    base = _safe_div(_mean(ev, 126) - _mean(ev, 252), _mean(ev, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_slope_v130_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_slope_v131_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_252d_slope_v132_signal(ev):
    base = _safe_div(_mean(ev, 252) - _mean(ev, 504), _mean(ev, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_slope_v133_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_slope_v134_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_mom_504d_slope_v135_signal(ev):
    base = _safe_div(_mean(ev, 504) - _mean(ev, 1008), _mean(ev, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_slope_v136_signal(ev):
    base = _std(ev, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_slope_v137_signal(ev):
    base = _std(ev, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_21d_slope_v138_signal(ev):
    base = _std(ev, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_slope_v139_signal(ev):
    base = _std(ev, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_slope_v140_signal(ev):
    base = _std(ev, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_63d_slope_v141_signal(ev):
    base = _std(ev, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_slope_v142_signal(ev):
    base = _std(ev, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_slope_v143_signal(ev):
    base = _std(ev, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_126d_slope_v144_signal(ev):
    base = _std(ev, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_slope_v145_signal(ev):
    base = _std(ev, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_slope_v146_signal(ev):
    base = _std(ev, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_252d_slope_v147_signal(ev):
    base = _std(ev, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_slope_v148_signal(ev):
    base = _std(ev, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_slope_v149_signal(ev):
    base = _std(ev, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ev
def gm_f78_biotech_f78_enterprise_value_to_rnd_ratio_vol_504d_slope_v150_signal(ev):
    base = _std(ev, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

