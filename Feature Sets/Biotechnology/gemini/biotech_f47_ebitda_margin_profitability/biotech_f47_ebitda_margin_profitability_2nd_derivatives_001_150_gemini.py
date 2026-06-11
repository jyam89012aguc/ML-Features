
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_slope_v001_signal(ebitda):
    base = _mean(ebitda, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_slope_v002_signal(ebitda):
    base = _mean(ebitda, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_21d_slope_v003_signal(ebitda):
    base = _mean(ebitda, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_slope_v004_signal(ebitda):
    base = _mean(ebitda, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_slope_v005_signal(ebitda):
    base = _mean(ebitda, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_63d_slope_v006_signal(ebitda):
    base = _mean(ebitda, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_slope_v007_signal(ebitda):
    base = _mean(ebitda, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_slope_v008_signal(ebitda):
    base = _mean(ebitda, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_126d_slope_v009_signal(ebitda):
    base = _mean(ebitda, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_slope_v010_signal(ebitda):
    base = _mean(ebitda, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_slope_v011_signal(ebitda):
    base = _mean(ebitda, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_252d_slope_v012_signal(ebitda):
    base = _mean(ebitda, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_slope_v013_signal(ebitda):
    base = _mean(ebitda, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_slope_v014_signal(ebitda):
    base = _mean(ebitda, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_raw_504d_slope_v015_signal(ebitda):
    base = _mean(ebitda, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_slope_v016_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_slope_v017_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_21d_slope_v018_signal(ebitda):
    base = _mean(_log(ebitda), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_slope_v019_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_slope_v020_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_63d_slope_v021_signal(ebitda):
    base = _mean(_log(ebitda), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_slope_v022_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_slope_v023_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_126d_slope_v024_signal(ebitda):
    base = _mean(_log(ebitda), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_slope_v025_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_slope_v026_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_252d_slope_v027_signal(ebitda):
    base = _mean(_log(ebitda), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_slope_v028_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_slope_v029_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_log_504d_slope_v030_signal(ebitda):
    base = _mean(_log(ebitda), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_slope_v031_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_slope_v032_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_21d_slope_v033_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_slope_v034_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_slope_v035_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_63d_slope_v036_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_slope_v037_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_slope_v038_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_126d_slope_v039_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_slope_v040_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_slope_v041_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_252d_slope_v042_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_slope_v043_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_slope_v044_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_z_504d_slope_v045_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_slope_v046_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_slope_v047_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_21d_slope_v048_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_slope_v049_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_slope_v050_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_63d_slope_v051_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_slope_v052_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_slope_v053_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_126d_slope_v054_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_slope_v055_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_slope_v056_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_252d_slope_v057_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_slope_v058_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_slope_v059_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_ps_504d_slope_v060_signal(ebitda, sharesbas):
    base = _safe_div(_mean(ebitda, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_slope_v061_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_slope_v062_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_21d_slope_v063_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_slope_v064_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_slope_v065_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_63d_slope_v066_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_slope_v067_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_slope_v068_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_126d_slope_v069_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_slope_v070_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_slope_v071_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_252d_slope_v072_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_slope_v073_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_slope_v074_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_asset_scaled_504d_slope_v075_signal(ebitda, assets):
    base = _safe_div(_mean(ebitda, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_slope_v076_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_slope_v077_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_21d_slope_v078_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_slope_v079_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_slope_v080_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_63d_slope_v081_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_slope_v082_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_slope_v083_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_126d_slope_v084_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_slope_v085_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_slope_v086_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_252d_slope_v087_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_slope_v088_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_slope_v089_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mcap_scaled_504d_slope_v090_signal(ebitda, marketcap):
    base = _safe_div(_mean(ebitda, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_slope_v091_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_slope_v092_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_21d_slope_v093_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(21).min(), ebitda.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_slope_v094_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_slope_v095_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_63d_slope_v096_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(63).min(), ebitda.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_slope_v097_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_slope_v098_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_126d_slope_v099_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(126).min(), ebitda.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_slope_v100_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_slope_v101_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_252d_slope_v102_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(252).min(), ebitda.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_slope_v103_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_slope_v104_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_low_504d_slope_v105_signal(ebitda):
    base = _safe_div(ebitda - ebitda.rolling(504).min(), ebitda.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_slope_v106_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_slope_v107_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_21d_slope_v108_signal(ebitda):
    base = _safe_div(ebitda.rolling(21).max() - ebitda, ebitda.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_slope_v109_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_slope_v110_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_63d_slope_v111_signal(ebitda):
    base = _safe_div(ebitda.rolling(63).max() - ebitda, ebitda.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_slope_v112_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_slope_v113_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_126d_slope_v114_signal(ebitda):
    base = _safe_div(ebitda.rolling(126).max() - ebitda, ebitda.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_slope_v115_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_slope_v116_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_252d_slope_v117_signal(ebitda):
    base = _safe_div(ebitda.rolling(252).max() - ebitda, ebitda.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_slope_v118_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_slope_v119_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_dist_high_504d_slope_v120_signal(ebitda):
    base = _safe_div(ebitda.rolling(504).max() - ebitda, ebitda.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_slope_v121_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_slope_v122_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_21d_slope_v123_signal(ebitda):
    base = _safe_div(_mean(ebitda, 21) - _mean(ebitda, 42), _mean(ebitda, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_slope_v124_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_slope_v125_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_63d_slope_v126_signal(ebitda):
    base = _safe_div(_mean(ebitda, 63) - _mean(ebitda, 126), _mean(ebitda, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_slope_v127_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_slope_v128_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_126d_slope_v129_signal(ebitda):
    base = _safe_div(_mean(ebitda, 126) - _mean(ebitda, 252), _mean(ebitda, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_slope_v130_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_slope_v131_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_252d_slope_v132_signal(ebitda):
    base = _safe_div(_mean(ebitda, 252) - _mean(ebitda, 504), _mean(ebitda, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_slope_v133_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_slope_v134_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_mom_504d_slope_v135_signal(ebitda):
    base = _safe_div(_mean(ebitda, 504) - _mean(ebitda, 1008), _mean(ebitda, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_slope_v136_signal(ebitda):
    base = _std(ebitda, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_slope_v137_signal(ebitda):
    base = _std(ebitda, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_21d_slope_v138_signal(ebitda):
    base = _std(ebitda, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_slope_v139_signal(ebitda):
    base = _std(ebitda, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_slope_v140_signal(ebitda):
    base = _std(ebitda, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_63d_slope_v141_signal(ebitda):
    base = _std(ebitda, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_slope_v142_signal(ebitda):
    base = _std(ebitda, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_slope_v143_signal(ebitda):
    base = _std(ebitda, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_126d_slope_v144_signal(ebitda):
    base = _std(ebitda, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_slope_v145_signal(ebitda):
    base = _std(ebitda, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_slope_v146_signal(ebitda):
    base = _std(ebitda, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_252d_slope_v147_signal(ebitda):
    base = _std(ebitda, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_slope_v148_signal(ebitda):
    base = _std(ebitda, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_slope_v149_signal(ebitda):
    base = _std(ebitda, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ebitda
def gm_f47_biotech_f47_ebitda_margin_profitability_vol_504d_slope_v150_signal(ebitda):
    base = _std(ebitda, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

