
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_21d_slope_v001_signal(prefdivis):
    base = _mean(prefdivis, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_21d_slope_v002_signal(prefdivis):
    base = _mean(prefdivis, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_21d_slope_v003_signal(prefdivis):
    base = _mean(prefdivis, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_63d_slope_v004_signal(prefdivis):
    base = _mean(prefdivis, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_63d_slope_v005_signal(prefdivis):
    base = _mean(prefdivis, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_63d_slope_v006_signal(prefdivis):
    base = _mean(prefdivis, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_126d_slope_v007_signal(prefdivis):
    base = _mean(prefdivis, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_126d_slope_v008_signal(prefdivis):
    base = _mean(prefdivis, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_126d_slope_v009_signal(prefdivis):
    base = _mean(prefdivis, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_252d_slope_v010_signal(prefdivis):
    base = _mean(prefdivis, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_252d_slope_v011_signal(prefdivis):
    base = _mean(prefdivis, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_252d_slope_v012_signal(prefdivis):
    base = _mean(prefdivis, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_504d_slope_v013_signal(prefdivis):
    base = _mean(prefdivis, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_504d_slope_v014_signal(prefdivis):
    base = _mean(prefdivis, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_raw_504d_slope_v015_signal(prefdivis):
    base = _mean(prefdivis, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_21d_slope_v016_signal(prefdivis):
    base = _mean(_log(prefdivis), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_21d_slope_v017_signal(prefdivis):
    base = _mean(_log(prefdivis), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_21d_slope_v018_signal(prefdivis):
    base = _mean(_log(prefdivis), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_63d_slope_v019_signal(prefdivis):
    base = _mean(_log(prefdivis), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_63d_slope_v020_signal(prefdivis):
    base = _mean(_log(prefdivis), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_63d_slope_v021_signal(prefdivis):
    base = _mean(_log(prefdivis), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_126d_slope_v022_signal(prefdivis):
    base = _mean(_log(prefdivis), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_126d_slope_v023_signal(prefdivis):
    base = _mean(_log(prefdivis), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_126d_slope_v024_signal(prefdivis):
    base = _mean(_log(prefdivis), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_252d_slope_v025_signal(prefdivis):
    base = _mean(_log(prefdivis), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_252d_slope_v026_signal(prefdivis):
    base = _mean(_log(prefdivis), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_252d_slope_v027_signal(prefdivis):
    base = _mean(_log(prefdivis), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_504d_slope_v028_signal(prefdivis):
    base = _mean(_log(prefdivis), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_504d_slope_v029_signal(prefdivis):
    base = _mean(_log(prefdivis), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_log_504d_slope_v030_signal(prefdivis):
    base = _mean(_log(prefdivis), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_21d_slope_v031_signal(prefdivis):
    base = _z(prefdivis, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_21d_slope_v032_signal(prefdivis):
    base = _z(prefdivis, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_21d_slope_v033_signal(prefdivis):
    base = _z(prefdivis, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_63d_slope_v034_signal(prefdivis):
    base = _z(prefdivis, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_63d_slope_v035_signal(prefdivis):
    base = _z(prefdivis, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_63d_slope_v036_signal(prefdivis):
    base = _z(prefdivis, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_126d_slope_v037_signal(prefdivis):
    base = _z(prefdivis, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_126d_slope_v038_signal(prefdivis):
    base = _z(prefdivis, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_126d_slope_v039_signal(prefdivis):
    base = _z(prefdivis, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_252d_slope_v040_signal(prefdivis):
    base = _z(prefdivis, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_252d_slope_v041_signal(prefdivis):
    base = _z(prefdivis, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_252d_slope_v042_signal(prefdivis):
    base = _z(prefdivis, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_504d_slope_v043_signal(prefdivis):
    base = _z(prefdivis, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_504d_slope_v044_signal(prefdivis):
    base = _z(prefdivis, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_z_504d_slope_v045_signal(prefdivis):
    base = _z(prefdivis, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_21d_slope_v046_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_21d_slope_v047_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_21d_slope_v048_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_63d_slope_v049_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_63d_slope_v050_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_63d_slope_v051_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_126d_slope_v052_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_126d_slope_v053_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_126d_slope_v054_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_252d_slope_v055_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_252d_slope_v056_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_252d_slope_v057_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_504d_slope_v058_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_504d_slope_v059_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_ps_504d_slope_v060_signal(prefdivis, sharesbas):
    base = _safe_div(_mean(prefdivis, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_21d_slope_v061_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_21d_slope_v062_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_21d_slope_v063_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_63d_slope_v064_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_63d_slope_v065_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_63d_slope_v066_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_126d_slope_v067_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_126d_slope_v068_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_126d_slope_v069_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_252d_slope_v070_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_252d_slope_v071_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_252d_slope_v072_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_504d_slope_v073_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_504d_slope_v074_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_asset_scaled_504d_slope_v075_signal(prefdivis, assets):
    base = _safe_div(_mean(prefdivis, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_21d_slope_v076_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_21d_slope_v077_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_21d_slope_v078_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_63d_slope_v079_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_63d_slope_v080_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_63d_slope_v081_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_126d_slope_v082_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_126d_slope_v083_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_126d_slope_v084_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_252d_slope_v085_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_252d_slope_v086_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_252d_slope_v087_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_504d_slope_v088_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_504d_slope_v089_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mcap_scaled_504d_slope_v090_signal(prefdivis, marketcap):
    base = _safe_div(_mean(prefdivis, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_21d_slope_v091_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(21).min(), prefdivis.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_21d_slope_v092_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(21).min(), prefdivis.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_21d_slope_v093_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(21).min(), prefdivis.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_63d_slope_v094_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(63).min(), prefdivis.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_63d_slope_v095_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(63).min(), prefdivis.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_63d_slope_v096_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(63).min(), prefdivis.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_126d_slope_v097_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(126).min(), prefdivis.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_126d_slope_v098_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(126).min(), prefdivis.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_126d_slope_v099_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(126).min(), prefdivis.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_252d_slope_v100_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(252).min(), prefdivis.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_252d_slope_v101_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(252).min(), prefdivis.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_252d_slope_v102_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(252).min(), prefdivis.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_504d_slope_v103_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(504).min(), prefdivis.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_504d_slope_v104_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(504).min(), prefdivis.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_low_504d_slope_v105_signal(prefdivis):
    base = _safe_div(prefdivis - prefdivis.rolling(504).min(), prefdivis.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_21d_slope_v106_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(21).max() - prefdivis, prefdivis.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_21d_slope_v107_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(21).max() - prefdivis, prefdivis.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_21d_slope_v108_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(21).max() - prefdivis, prefdivis.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_63d_slope_v109_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(63).max() - prefdivis, prefdivis.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_63d_slope_v110_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(63).max() - prefdivis, prefdivis.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_63d_slope_v111_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(63).max() - prefdivis, prefdivis.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_126d_slope_v112_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(126).max() - prefdivis, prefdivis.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_126d_slope_v113_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(126).max() - prefdivis, prefdivis.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_126d_slope_v114_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(126).max() - prefdivis, prefdivis.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_252d_slope_v115_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(252).max() - prefdivis, prefdivis.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_252d_slope_v116_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(252).max() - prefdivis, prefdivis.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_252d_slope_v117_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(252).max() - prefdivis, prefdivis.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_504d_slope_v118_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(504).max() - prefdivis, prefdivis.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_504d_slope_v119_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(504).max() - prefdivis, prefdivis.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_dist_high_504d_slope_v120_signal(prefdivis):
    base = _safe_div(prefdivis.rolling(504).max() - prefdivis, prefdivis.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_21d_slope_v121_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 21) - _mean(prefdivis, 42), _mean(prefdivis, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_21d_slope_v122_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 21) - _mean(prefdivis, 42), _mean(prefdivis, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_21d_slope_v123_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 21) - _mean(prefdivis, 42), _mean(prefdivis, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_63d_slope_v124_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 63) - _mean(prefdivis, 126), _mean(prefdivis, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_63d_slope_v125_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 63) - _mean(prefdivis, 126), _mean(prefdivis, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_63d_slope_v126_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 63) - _mean(prefdivis, 126), _mean(prefdivis, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_126d_slope_v127_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 126) - _mean(prefdivis, 252), _mean(prefdivis, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_126d_slope_v128_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 126) - _mean(prefdivis, 252), _mean(prefdivis, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_126d_slope_v129_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 126) - _mean(prefdivis, 252), _mean(prefdivis, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_252d_slope_v130_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 252) - _mean(prefdivis, 504), _mean(prefdivis, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_252d_slope_v131_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 252) - _mean(prefdivis, 504), _mean(prefdivis, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_252d_slope_v132_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 252) - _mean(prefdivis, 504), _mean(prefdivis, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_504d_slope_v133_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 504) - _mean(prefdivis, 1008), _mean(prefdivis, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_504d_slope_v134_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 504) - _mean(prefdivis, 1008), _mean(prefdivis, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_mom_504d_slope_v135_signal(prefdivis):
    base = _safe_div(_mean(prefdivis, 504) - _mean(prefdivis, 1008), _mean(prefdivis, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_21d_slope_v136_signal(prefdivis):
    base = _std(prefdivis, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_21d_slope_v137_signal(prefdivis):
    base = _std(prefdivis, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_21d_slope_v138_signal(prefdivis):
    base = _std(prefdivis, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_63d_slope_v139_signal(prefdivis):
    base = _std(prefdivis, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_63d_slope_v140_signal(prefdivis):
    base = _std(prefdivis, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_63d_slope_v141_signal(prefdivis):
    base = _std(prefdivis, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_126d_slope_v142_signal(prefdivis):
    base = _std(prefdivis, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_126d_slope_v143_signal(prefdivis):
    base = _std(prefdivis, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_126d_slope_v144_signal(prefdivis):
    base = _std(prefdivis, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_252d_slope_v145_signal(prefdivis):
    base = _std(prefdivis, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_252d_slope_v146_signal(prefdivis):
    base = _std(prefdivis, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_252d_slope_v147_signal(prefdivis):
    base = _std(prefdivis, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_504d_slope_v148_signal(prefdivis):
    base = _std(prefdivis, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_504d_slope_v149_signal(prefdivis):
    base = _std(prefdivis, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol prefdivis
def gm_f34_biotech_f34_preferred_dividend_obligation_vol_504d_slope_v150_signal(prefdivis):
    base = _std(prefdivis, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

