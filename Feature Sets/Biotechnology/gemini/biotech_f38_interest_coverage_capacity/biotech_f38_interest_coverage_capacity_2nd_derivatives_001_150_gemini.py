
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_21d_slope_v001_signal(ebit):
    base = _mean(ebit, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_21d_slope_v002_signal(ebit):
    base = _mean(ebit, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_21d_slope_v003_signal(ebit):
    base = _mean(ebit, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_63d_slope_v004_signal(ebit):
    base = _mean(ebit, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_63d_slope_v005_signal(ebit):
    base = _mean(ebit, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_63d_slope_v006_signal(ebit):
    base = _mean(ebit, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_126d_slope_v007_signal(ebit):
    base = _mean(ebit, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_126d_slope_v008_signal(ebit):
    base = _mean(ebit, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_126d_slope_v009_signal(ebit):
    base = _mean(ebit, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_252d_slope_v010_signal(ebit):
    base = _mean(ebit, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_252d_slope_v011_signal(ebit):
    base = _mean(ebit, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_252d_slope_v012_signal(ebit):
    base = _mean(ebit, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_504d_slope_v013_signal(ebit):
    base = _mean(ebit, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_504d_slope_v014_signal(ebit):
    base = _mean(ebit, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ebit
def gm_f38_biotech_f38_interest_coverage_capacity_raw_504d_slope_v015_signal(ebit):
    base = _mean(ebit, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_21d_slope_v016_signal(ebit):
    base = _mean(_log(ebit), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_21d_slope_v017_signal(ebit):
    base = _mean(_log(ebit), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_21d_slope_v018_signal(ebit):
    base = _mean(_log(ebit), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_63d_slope_v019_signal(ebit):
    base = _mean(_log(ebit), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_63d_slope_v020_signal(ebit):
    base = _mean(_log(ebit), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_63d_slope_v021_signal(ebit):
    base = _mean(_log(ebit), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_126d_slope_v022_signal(ebit):
    base = _mean(_log(ebit), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_126d_slope_v023_signal(ebit):
    base = _mean(_log(ebit), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_126d_slope_v024_signal(ebit):
    base = _mean(_log(ebit), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_252d_slope_v025_signal(ebit):
    base = _mean(_log(ebit), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_252d_slope_v026_signal(ebit):
    base = _mean(_log(ebit), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_252d_slope_v027_signal(ebit):
    base = _mean(_log(ebit), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_504d_slope_v028_signal(ebit):
    base = _mean(_log(ebit), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_504d_slope_v029_signal(ebit):
    base = _mean(_log(ebit), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ebit
def gm_f38_biotech_f38_interest_coverage_capacity_log_504d_slope_v030_signal(ebit):
    base = _mean(_log(ebit), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_21d_slope_v031_signal(ebit):
    base = _z(ebit, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_21d_slope_v032_signal(ebit):
    base = _z(ebit, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_21d_slope_v033_signal(ebit):
    base = _z(ebit, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_63d_slope_v034_signal(ebit):
    base = _z(ebit, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_63d_slope_v035_signal(ebit):
    base = _z(ebit, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_63d_slope_v036_signal(ebit):
    base = _z(ebit, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_126d_slope_v037_signal(ebit):
    base = _z(ebit, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_126d_slope_v038_signal(ebit):
    base = _z(ebit, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_126d_slope_v039_signal(ebit):
    base = _z(ebit, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_252d_slope_v040_signal(ebit):
    base = _z(ebit, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_252d_slope_v041_signal(ebit):
    base = _z(ebit, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_252d_slope_v042_signal(ebit):
    base = _z(ebit, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_504d_slope_v043_signal(ebit):
    base = _z(ebit, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_504d_slope_v044_signal(ebit):
    base = _z(ebit, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ebit
def gm_f38_biotech_f38_interest_coverage_capacity_z_504d_slope_v045_signal(ebit):
    base = _z(ebit, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_21d_slope_v046_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_21d_slope_v047_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_21d_slope_v048_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_63d_slope_v049_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_63d_slope_v050_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_63d_slope_v051_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_126d_slope_v052_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_126d_slope_v053_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_126d_slope_v054_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_252d_slope_v055_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_252d_slope_v056_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_252d_slope_v057_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_504d_slope_v058_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_504d_slope_v059_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ebit
def gm_f38_biotech_f38_interest_coverage_capacity_ps_504d_slope_v060_signal(ebit, sharesbas):
    base = _safe_div(_mean(ebit, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_21d_slope_v061_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_21d_slope_v062_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_21d_slope_v063_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_63d_slope_v064_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_63d_slope_v065_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_63d_slope_v066_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_126d_slope_v067_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_126d_slope_v068_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_126d_slope_v069_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_252d_slope_v070_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_252d_slope_v071_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_252d_slope_v072_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_504d_slope_v073_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_504d_slope_v074_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_asset_scaled_504d_slope_v075_signal(ebit, assets):
    base = _safe_div(_mean(ebit, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_21d_slope_v076_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_21d_slope_v077_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_21d_slope_v078_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_63d_slope_v079_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_63d_slope_v080_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_63d_slope_v081_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_126d_slope_v082_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_126d_slope_v083_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_126d_slope_v084_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_252d_slope_v085_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_252d_slope_v086_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_252d_slope_v087_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_504d_slope_v088_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_504d_slope_v089_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mcap_scaled_504d_slope_v090_signal(ebit, marketcap):
    base = _safe_div(_mean(ebit, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_21d_slope_v091_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_21d_slope_v092_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_21d_slope_v093_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(21).min(), ebit.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_63d_slope_v094_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_63d_slope_v095_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_63d_slope_v096_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(63).min(), ebit.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_126d_slope_v097_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_126d_slope_v098_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_126d_slope_v099_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(126).min(), ebit.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_252d_slope_v100_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_252d_slope_v101_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_252d_slope_v102_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(252).min(), ebit.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_504d_slope_v103_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_504d_slope_v104_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_low_504d_slope_v105_signal(ebit):
    base = _safe_div(ebit - ebit.rolling(504).min(), ebit.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_21d_slope_v106_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_21d_slope_v107_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_21d_slope_v108_signal(ebit):
    base = _safe_div(ebit.rolling(21).max() - ebit, ebit.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_63d_slope_v109_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_63d_slope_v110_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_63d_slope_v111_signal(ebit):
    base = _safe_div(ebit.rolling(63).max() - ebit, ebit.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_126d_slope_v112_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_126d_slope_v113_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_126d_slope_v114_signal(ebit):
    base = _safe_div(ebit.rolling(126).max() - ebit, ebit.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_252d_slope_v115_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_252d_slope_v116_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_252d_slope_v117_signal(ebit):
    base = _safe_div(ebit.rolling(252).max() - ebit, ebit.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_504d_slope_v118_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_504d_slope_v119_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ebit
def gm_f38_biotech_f38_interest_coverage_capacity_dist_high_504d_slope_v120_signal(ebit):
    base = _safe_div(ebit.rolling(504).max() - ebit, ebit.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_21d_slope_v121_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_21d_slope_v122_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_21d_slope_v123_signal(ebit):
    base = _safe_div(_mean(ebit, 21) - _mean(ebit, 42), _mean(ebit, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_63d_slope_v124_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_63d_slope_v125_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_63d_slope_v126_signal(ebit):
    base = _safe_div(_mean(ebit, 63) - _mean(ebit, 126), _mean(ebit, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_126d_slope_v127_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_126d_slope_v128_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_126d_slope_v129_signal(ebit):
    base = _safe_div(_mean(ebit, 126) - _mean(ebit, 252), _mean(ebit, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_252d_slope_v130_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_252d_slope_v131_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_252d_slope_v132_signal(ebit):
    base = _safe_div(_mean(ebit, 252) - _mean(ebit, 504), _mean(ebit, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_504d_slope_v133_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_504d_slope_v134_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ebit
def gm_f38_biotech_f38_interest_coverage_capacity_mom_504d_slope_v135_signal(ebit):
    base = _safe_div(_mean(ebit, 504) - _mean(ebit, 1008), _mean(ebit, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_21d_slope_v136_signal(ebit):
    base = _std(ebit, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_21d_slope_v137_signal(ebit):
    base = _std(ebit, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_21d_slope_v138_signal(ebit):
    base = _std(ebit, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_63d_slope_v139_signal(ebit):
    base = _std(ebit, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_63d_slope_v140_signal(ebit):
    base = _std(ebit, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_63d_slope_v141_signal(ebit):
    base = _std(ebit, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_126d_slope_v142_signal(ebit):
    base = _std(ebit, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_126d_slope_v143_signal(ebit):
    base = _std(ebit, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_126d_slope_v144_signal(ebit):
    base = _std(ebit, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_252d_slope_v145_signal(ebit):
    base = _std(ebit, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_252d_slope_v146_signal(ebit):
    base = _std(ebit, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_252d_slope_v147_signal(ebit):
    base = _std(ebit, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_504d_slope_v148_signal(ebit):
    base = _std(ebit, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_504d_slope_v149_signal(ebit):
    base = _std(ebit, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ebit
def gm_f38_biotech_f38_interest_coverage_capacity_vol_504d_slope_v150_signal(ebit):
    base = _std(ebit, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

