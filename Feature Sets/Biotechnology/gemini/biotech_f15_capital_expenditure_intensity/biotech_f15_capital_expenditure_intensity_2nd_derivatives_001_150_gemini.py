
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_21d_slope_v001_signal(capex):
    base = _mean(capex, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_21d_slope_v002_signal(capex):
    base = _mean(capex, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_21d_slope_v003_signal(capex):
    base = _mean(capex, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_63d_slope_v004_signal(capex):
    base = _mean(capex, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_63d_slope_v005_signal(capex):
    base = _mean(capex, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_63d_slope_v006_signal(capex):
    base = _mean(capex, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_126d_slope_v007_signal(capex):
    base = _mean(capex, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_126d_slope_v008_signal(capex):
    base = _mean(capex, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_126d_slope_v009_signal(capex):
    base = _mean(capex, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_252d_slope_v010_signal(capex):
    base = _mean(capex, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_252d_slope_v011_signal(capex):
    base = _mean(capex, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_252d_slope_v012_signal(capex):
    base = _mean(capex, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_504d_slope_v013_signal(capex):
    base = _mean(capex, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_504d_slope_v014_signal(capex):
    base = _mean(capex, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw capex
def gm_f15_biotech_f15_capital_expenditure_intensity_raw_504d_slope_v015_signal(capex):
    base = _mean(capex, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_21d_slope_v016_signal(capex):
    base = _mean(_log(capex), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_21d_slope_v017_signal(capex):
    base = _mean(_log(capex), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_21d_slope_v018_signal(capex):
    base = _mean(_log(capex), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_63d_slope_v019_signal(capex):
    base = _mean(_log(capex), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_63d_slope_v020_signal(capex):
    base = _mean(_log(capex), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_63d_slope_v021_signal(capex):
    base = _mean(_log(capex), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_126d_slope_v022_signal(capex):
    base = _mean(_log(capex), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_126d_slope_v023_signal(capex):
    base = _mean(_log(capex), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_126d_slope_v024_signal(capex):
    base = _mean(_log(capex), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_252d_slope_v025_signal(capex):
    base = _mean(_log(capex), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_252d_slope_v026_signal(capex):
    base = _mean(_log(capex), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_252d_slope_v027_signal(capex):
    base = _mean(_log(capex), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_504d_slope_v028_signal(capex):
    base = _mean(_log(capex), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_504d_slope_v029_signal(capex):
    base = _mean(_log(capex), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log capex
def gm_f15_biotech_f15_capital_expenditure_intensity_log_504d_slope_v030_signal(capex):
    base = _mean(_log(capex), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_21d_slope_v031_signal(capex):
    base = _z(capex, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_21d_slope_v032_signal(capex):
    base = _z(capex, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_21d_slope_v033_signal(capex):
    base = _z(capex, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_63d_slope_v034_signal(capex):
    base = _z(capex, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_63d_slope_v035_signal(capex):
    base = _z(capex, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_63d_slope_v036_signal(capex):
    base = _z(capex, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_126d_slope_v037_signal(capex):
    base = _z(capex, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_126d_slope_v038_signal(capex):
    base = _z(capex, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_126d_slope_v039_signal(capex):
    base = _z(capex, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_252d_slope_v040_signal(capex):
    base = _z(capex, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_252d_slope_v041_signal(capex):
    base = _z(capex, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_252d_slope_v042_signal(capex):
    base = _z(capex, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_504d_slope_v043_signal(capex):
    base = _z(capex, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_504d_slope_v044_signal(capex):
    base = _z(capex, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z capex
def gm_f15_biotech_f15_capital_expenditure_intensity_z_504d_slope_v045_signal(capex):
    base = _z(capex, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_21d_slope_v046_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_21d_slope_v047_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_21d_slope_v048_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_63d_slope_v049_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_63d_slope_v050_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_63d_slope_v051_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_126d_slope_v052_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_126d_slope_v053_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_126d_slope_v054_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_252d_slope_v055_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_252d_slope_v056_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_252d_slope_v057_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_504d_slope_v058_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_504d_slope_v059_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps capex
def gm_f15_biotech_f15_capital_expenditure_intensity_ps_504d_slope_v060_signal(capex, sharesbas):
    base = _safe_div(_mean(capex, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_21d_slope_v061_signal(capex, assets):
    base = _safe_div(_mean(capex, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_21d_slope_v062_signal(capex, assets):
    base = _safe_div(_mean(capex, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_21d_slope_v063_signal(capex, assets):
    base = _safe_div(_mean(capex, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_63d_slope_v064_signal(capex, assets):
    base = _safe_div(_mean(capex, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_63d_slope_v065_signal(capex, assets):
    base = _safe_div(_mean(capex, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_63d_slope_v066_signal(capex, assets):
    base = _safe_div(_mean(capex, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_126d_slope_v067_signal(capex, assets):
    base = _safe_div(_mean(capex, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_126d_slope_v068_signal(capex, assets):
    base = _safe_div(_mean(capex, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_126d_slope_v069_signal(capex, assets):
    base = _safe_div(_mean(capex, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_252d_slope_v070_signal(capex, assets):
    base = _safe_div(_mean(capex, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_252d_slope_v071_signal(capex, assets):
    base = _safe_div(_mean(capex, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_252d_slope_v072_signal(capex, assets):
    base = _safe_div(_mean(capex, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_504d_slope_v073_signal(capex, assets):
    base = _safe_div(_mean(capex, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_504d_slope_v074_signal(capex, assets):
    base = _safe_div(_mean(capex, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_asset_scaled_504d_slope_v075_signal(capex, assets):
    base = _safe_div(_mean(capex, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_21d_slope_v076_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_21d_slope_v077_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_21d_slope_v078_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_63d_slope_v079_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_63d_slope_v080_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_63d_slope_v081_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_126d_slope_v082_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_126d_slope_v083_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_126d_slope_v084_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_252d_slope_v085_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_252d_slope_v086_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_252d_slope_v087_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_504d_slope_v088_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_504d_slope_v089_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mcap_scaled_504d_slope_v090_signal(capex, marketcap):
    base = _safe_div(_mean(capex, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_21d_slope_v091_signal(capex):
    base = _safe_div(capex - capex.rolling(21).min(), capex.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_21d_slope_v092_signal(capex):
    base = _safe_div(capex - capex.rolling(21).min(), capex.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_21d_slope_v093_signal(capex):
    base = _safe_div(capex - capex.rolling(21).min(), capex.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_63d_slope_v094_signal(capex):
    base = _safe_div(capex - capex.rolling(63).min(), capex.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_63d_slope_v095_signal(capex):
    base = _safe_div(capex - capex.rolling(63).min(), capex.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_63d_slope_v096_signal(capex):
    base = _safe_div(capex - capex.rolling(63).min(), capex.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_126d_slope_v097_signal(capex):
    base = _safe_div(capex - capex.rolling(126).min(), capex.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_126d_slope_v098_signal(capex):
    base = _safe_div(capex - capex.rolling(126).min(), capex.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_126d_slope_v099_signal(capex):
    base = _safe_div(capex - capex.rolling(126).min(), capex.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_252d_slope_v100_signal(capex):
    base = _safe_div(capex - capex.rolling(252).min(), capex.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_252d_slope_v101_signal(capex):
    base = _safe_div(capex - capex.rolling(252).min(), capex.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_252d_slope_v102_signal(capex):
    base = _safe_div(capex - capex.rolling(252).min(), capex.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_504d_slope_v103_signal(capex):
    base = _safe_div(capex - capex.rolling(504).min(), capex.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_504d_slope_v104_signal(capex):
    base = _safe_div(capex - capex.rolling(504).min(), capex.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_low_504d_slope_v105_signal(capex):
    base = _safe_div(capex - capex.rolling(504).min(), capex.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_21d_slope_v106_signal(capex):
    base = _safe_div(capex.rolling(21).max() - capex, capex.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_21d_slope_v107_signal(capex):
    base = _safe_div(capex.rolling(21).max() - capex, capex.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_21d_slope_v108_signal(capex):
    base = _safe_div(capex.rolling(21).max() - capex, capex.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_63d_slope_v109_signal(capex):
    base = _safe_div(capex.rolling(63).max() - capex, capex.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_63d_slope_v110_signal(capex):
    base = _safe_div(capex.rolling(63).max() - capex, capex.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_63d_slope_v111_signal(capex):
    base = _safe_div(capex.rolling(63).max() - capex, capex.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_126d_slope_v112_signal(capex):
    base = _safe_div(capex.rolling(126).max() - capex, capex.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_126d_slope_v113_signal(capex):
    base = _safe_div(capex.rolling(126).max() - capex, capex.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_126d_slope_v114_signal(capex):
    base = _safe_div(capex.rolling(126).max() - capex, capex.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_252d_slope_v115_signal(capex):
    base = _safe_div(capex.rolling(252).max() - capex, capex.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_252d_slope_v116_signal(capex):
    base = _safe_div(capex.rolling(252).max() - capex, capex.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_252d_slope_v117_signal(capex):
    base = _safe_div(capex.rolling(252).max() - capex, capex.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_504d_slope_v118_signal(capex):
    base = _safe_div(capex.rolling(504).max() - capex, capex.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_504d_slope_v119_signal(capex):
    base = _safe_div(capex.rolling(504).max() - capex, capex.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high capex
def gm_f15_biotech_f15_capital_expenditure_intensity_dist_high_504d_slope_v120_signal(capex):
    base = _safe_div(capex.rolling(504).max() - capex, capex.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_21d_slope_v121_signal(capex):
    base = _safe_div(_mean(capex, 21) - _mean(capex, 42), _mean(capex, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_21d_slope_v122_signal(capex):
    base = _safe_div(_mean(capex, 21) - _mean(capex, 42), _mean(capex, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_21d_slope_v123_signal(capex):
    base = _safe_div(_mean(capex, 21) - _mean(capex, 42), _mean(capex, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_63d_slope_v124_signal(capex):
    base = _safe_div(_mean(capex, 63) - _mean(capex, 126), _mean(capex, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_63d_slope_v125_signal(capex):
    base = _safe_div(_mean(capex, 63) - _mean(capex, 126), _mean(capex, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_63d_slope_v126_signal(capex):
    base = _safe_div(_mean(capex, 63) - _mean(capex, 126), _mean(capex, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_126d_slope_v127_signal(capex):
    base = _safe_div(_mean(capex, 126) - _mean(capex, 252), _mean(capex, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_126d_slope_v128_signal(capex):
    base = _safe_div(_mean(capex, 126) - _mean(capex, 252), _mean(capex, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_126d_slope_v129_signal(capex):
    base = _safe_div(_mean(capex, 126) - _mean(capex, 252), _mean(capex, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_252d_slope_v130_signal(capex):
    base = _safe_div(_mean(capex, 252) - _mean(capex, 504), _mean(capex, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_252d_slope_v131_signal(capex):
    base = _safe_div(_mean(capex, 252) - _mean(capex, 504), _mean(capex, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_252d_slope_v132_signal(capex):
    base = _safe_div(_mean(capex, 252) - _mean(capex, 504), _mean(capex, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_504d_slope_v133_signal(capex):
    base = _safe_div(_mean(capex, 504) - _mean(capex, 1008), _mean(capex, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_504d_slope_v134_signal(capex):
    base = _safe_div(_mean(capex, 504) - _mean(capex, 1008), _mean(capex, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom capex
def gm_f15_biotech_f15_capital_expenditure_intensity_mom_504d_slope_v135_signal(capex):
    base = _safe_div(_mean(capex, 504) - _mean(capex, 1008), _mean(capex, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_21d_slope_v136_signal(capex):
    base = _std(capex, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_21d_slope_v137_signal(capex):
    base = _std(capex, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_21d_slope_v138_signal(capex):
    base = _std(capex, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_63d_slope_v139_signal(capex):
    base = _std(capex, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_63d_slope_v140_signal(capex):
    base = _std(capex, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_63d_slope_v141_signal(capex):
    base = _std(capex, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_126d_slope_v142_signal(capex):
    base = _std(capex, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_126d_slope_v143_signal(capex):
    base = _std(capex, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_126d_slope_v144_signal(capex):
    base = _std(capex, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_252d_slope_v145_signal(capex):
    base = _std(capex, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_252d_slope_v146_signal(capex):
    base = _std(capex, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_252d_slope_v147_signal(capex):
    base = _std(capex, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_504d_slope_v148_signal(capex):
    base = _std(capex, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_504d_slope_v149_signal(capex):
    base = _std(capex, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol capex
def gm_f15_biotech_f15_capital_expenditure_intensity_vol_504d_slope_v150_signal(capex):
    base = _std(capex, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

