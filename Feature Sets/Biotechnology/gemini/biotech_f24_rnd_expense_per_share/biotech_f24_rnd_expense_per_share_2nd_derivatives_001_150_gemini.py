
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_21d_slope_v001_signal(rnd):
    base = _mean(rnd, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_21d_slope_v002_signal(rnd):
    base = _mean(rnd, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_21d_slope_v003_signal(rnd):
    base = _mean(rnd, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_63d_slope_v004_signal(rnd):
    base = _mean(rnd, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_63d_slope_v005_signal(rnd):
    base = _mean(rnd, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_63d_slope_v006_signal(rnd):
    base = _mean(rnd, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_126d_slope_v007_signal(rnd):
    base = _mean(rnd, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_126d_slope_v008_signal(rnd):
    base = _mean(rnd, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_126d_slope_v009_signal(rnd):
    base = _mean(rnd, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_252d_slope_v010_signal(rnd):
    base = _mean(rnd, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_252d_slope_v011_signal(rnd):
    base = _mean(rnd, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_252d_slope_v012_signal(rnd):
    base = _mean(rnd, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_504d_slope_v013_signal(rnd):
    base = _mean(rnd, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_504d_slope_v014_signal(rnd):
    base = _mean(rnd, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw rnd
def gm_f24_biotech_f24_rnd_expense_per_share_raw_504d_slope_v015_signal(rnd):
    base = _mean(rnd, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_21d_slope_v016_signal(rnd):
    base = _mean(_log(rnd), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_21d_slope_v017_signal(rnd):
    base = _mean(_log(rnd), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_21d_slope_v018_signal(rnd):
    base = _mean(_log(rnd), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_63d_slope_v019_signal(rnd):
    base = _mean(_log(rnd), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_63d_slope_v020_signal(rnd):
    base = _mean(_log(rnd), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_63d_slope_v021_signal(rnd):
    base = _mean(_log(rnd), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_126d_slope_v022_signal(rnd):
    base = _mean(_log(rnd), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_126d_slope_v023_signal(rnd):
    base = _mean(_log(rnd), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_126d_slope_v024_signal(rnd):
    base = _mean(_log(rnd), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_252d_slope_v025_signal(rnd):
    base = _mean(_log(rnd), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_252d_slope_v026_signal(rnd):
    base = _mean(_log(rnd), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_252d_slope_v027_signal(rnd):
    base = _mean(_log(rnd), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_504d_slope_v028_signal(rnd):
    base = _mean(_log(rnd), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_504d_slope_v029_signal(rnd):
    base = _mean(_log(rnd), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log rnd
def gm_f24_biotech_f24_rnd_expense_per_share_log_504d_slope_v030_signal(rnd):
    base = _mean(_log(rnd), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_21d_slope_v031_signal(rnd):
    base = _z(rnd, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_21d_slope_v032_signal(rnd):
    base = _z(rnd, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_21d_slope_v033_signal(rnd):
    base = _z(rnd, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_63d_slope_v034_signal(rnd):
    base = _z(rnd, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_63d_slope_v035_signal(rnd):
    base = _z(rnd, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_63d_slope_v036_signal(rnd):
    base = _z(rnd, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_126d_slope_v037_signal(rnd):
    base = _z(rnd, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_126d_slope_v038_signal(rnd):
    base = _z(rnd, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_126d_slope_v039_signal(rnd):
    base = _z(rnd, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_252d_slope_v040_signal(rnd):
    base = _z(rnd, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_252d_slope_v041_signal(rnd):
    base = _z(rnd, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_252d_slope_v042_signal(rnd):
    base = _z(rnd, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_504d_slope_v043_signal(rnd):
    base = _z(rnd, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_504d_slope_v044_signal(rnd):
    base = _z(rnd, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z rnd
def gm_f24_biotech_f24_rnd_expense_per_share_z_504d_slope_v045_signal(rnd):
    base = _z(rnd, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_21d_slope_v046_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_21d_slope_v047_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_21d_slope_v048_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_63d_slope_v049_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_63d_slope_v050_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_63d_slope_v051_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_126d_slope_v052_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_126d_slope_v053_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_126d_slope_v054_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_252d_slope_v055_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_252d_slope_v056_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_252d_slope_v057_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_504d_slope_v058_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_504d_slope_v059_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps rnd
def gm_f24_biotech_f24_rnd_expense_per_share_ps_504d_slope_v060_signal(rnd, sharesbas):
    base = _safe_div(_mean(rnd, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_21d_slope_v061_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_21d_slope_v062_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_21d_slope_v063_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_63d_slope_v064_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_63d_slope_v065_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_63d_slope_v066_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_126d_slope_v067_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_126d_slope_v068_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_126d_slope_v069_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_252d_slope_v070_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_252d_slope_v071_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_252d_slope_v072_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_504d_slope_v073_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_504d_slope_v074_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_asset_scaled_504d_slope_v075_signal(rnd, assets):
    base = _safe_div(_mean(rnd, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_21d_slope_v076_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_21d_slope_v077_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_21d_slope_v078_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_63d_slope_v079_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_63d_slope_v080_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_63d_slope_v081_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_126d_slope_v082_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_126d_slope_v083_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_126d_slope_v084_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_252d_slope_v085_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_252d_slope_v086_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_252d_slope_v087_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_504d_slope_v088_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_504d_slope_v089_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mcap_scaled_504d_slope_v090_signal(rnd, marketcap):
    base = _safe_div(_mean(rnd, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_21d_slope_v091_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_21d_slope_v092_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_21d_slope_v093_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(21).min(), rnd.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_63d_slope_v094_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_63d_slope_v095_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_63d_slope_v096_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(63).min(), rnd.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_126d_slope_v097_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_126d_slope_v098_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_126d_slope_v099_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(126).min(), rnd.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_252d_slope_v100_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_252d_slope_v101_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_252d_slope_v102_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(252).min(), rnd.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_504d_slope_v103_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_504d_slope_v104_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_low_504d_slope_v105_signal(rnd):
    base = _safe_div(rnd - rnd.rolling(504).min(), rnd.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_21d_slope_v106_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_21d_slope_v107_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_21d_slope_v108_signal(rnd):
    base = _safe_div(rnd.rolling(21).max() - rnd, rnd.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_63d_slope_v109_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_63d_slope_v110_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_63d_slope_v111_signal(rnd):
    base = _safe_div(rnd.rolling(63).max() - rnd, rnd.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_126d_slope_v112_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_126d_slope_v113_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_126d_slope_v114_signal(rnd):
    base = _safe_div(rnd.rolling(126).max() - rnd, rnd.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_252d_slope_v115_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_252d_slope_v116_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_252d_slope_v117_signal(rnd):
    base = _safe_div(rnd.rolling(252).max() - rnd, rnd.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_504d_slope_v118_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_504d_slope_v119_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high rnd
def gm_f24_biotech_f24_rnd_expense_per_share_dist_high_504d_slope_v120_signal(rnd):
    base = _safe_div(rnd.rolling(504).max() - rnd, rnd.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_21d_slope_v121_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_21d_slope_v122_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_21d_slope_v123_signal(rnd):
    base = _safe_div(_mean(rnd, 21) - _mean(rnd, 42), _mean(rnd, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_63d_slope_v124_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_63d_slope_v125_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_63d_slope_v126_signal(rnd):
    base = _safe_div(_mean(rnd, 63) - _mean(rnd, 126), _mean(rnd, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_126d_slope_v127_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_126d_slope_v128_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_126d_slope_v129_signal(rnd):
    base = _safe_div(_mean(rnd, 126) - _mean(rnd, 252), _mean(rnd, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_252d_slope_v130_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_252d_slope_v131_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_252d_slope_v132_signal(rnd):
    base = _safe_div(_mean(rnd, 252) - _mean(rnd, 504), _mean(rnd, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_504d_slope_v133_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_504d_slope_v134_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom rnd
def gm_f24_biotech_f24_rnd_expense_per_share_mom_504d_slope_v135_signal(rnd):
    base = _safe_div(_mean(rnd, 504) - _mean(rnd, 1008), _mean(rnd, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_21d_slope_v136_signal(rnd):
    base = _std(rnd, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_21d_slope_v137_signal(rnd):
    base = _std(rnd, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_21d_slope_v138_signal(rnd):
    base = _std(rnd, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_63d_slope_v139_signal(rnd):
    base = _std(rnd, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_63d_slope_v140_signal(rnd):
    base = _std(rnd, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_63d_slope_v141_signal(rnd):
    base = _std(rnd, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_126d_slope_v142_signal(rnd):
    base = _std(rnd, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_126d_slope_v143_signal(rnd):
    base = _std(rnd, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_126d_slope_v144_signal(rnd):
    base = _std(rnd, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_252d_slope_v145_signal(rnd):
    base = _std(rnd, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_252d_slope_v146_signal(rnd):
    base = _std(rnd, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_252d_slope_v147_signal(rnd):
    base = _std(rnd, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_504d_slope_v148_signal(rnd):
    base = _std(rnd, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_504d_slope_v149_signal(rnd):
    base = _std(rnd, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol rnd
def gm_f24_biotech_f24_rnd_expense_per_share_vol_504d_slope_v150_signal(rnd):
    base = _std(rnd, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

