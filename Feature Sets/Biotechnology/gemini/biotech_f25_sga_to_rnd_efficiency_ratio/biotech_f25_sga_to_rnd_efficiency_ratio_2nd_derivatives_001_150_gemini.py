
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_slope_v001_signal(sgna):
    base = _mean(sgna, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_slope_v002_signal(sgna):
    base = _mean(sgna, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_21d_slope_v003_signal(sgna):
    base = _mean(sgna, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_slope_v004_signal(sgna):
    base = _mean(sgna, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_slope_v005_signal(sgna):
    base = _mean(sgna, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_63d_slope_v006_signal(sgna):
    base = _mean(sgna, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_slope_v007_signal(sgna):
    base = _mean(sgna, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_slope_v008_signal(sgna):
    base = _mean(sgna, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_126d_slope_v009_signal(sgna):
    base = _mean(sgna, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_slope_v010_signal(sgna):
    base = _mean(sgna, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_slope_v011_signal(sgna):
    base = _mean(sgna, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_252d_slope_v012_signal(sgna):
    base = _mean(sgna, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_slope_v013_signal(sgna):
    base = _mean(sgna, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_slope_v014_signal(sgna):
    base = _mean(sgna, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_raw_504d_slope_v015_signal(sgna):
    base = _mean(sgna, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_slope_v016_signal(sgna):
    base = _mean(_log(sgna), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_slope_v017_signal(sgna):
    base = _mean(_log(sgna), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_21d_slope_v018_signal(sgna):
    base = _mean(_log(sgna), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_slope_v019_signal(sgna):
    base = _mean(_log(sgna), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_slope_v020_signal(sgna):
    base = _mean(_log(sgna), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_63d_slope_v021_signal(sgna):
    base = _mean(_log(sgna), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_slope_v022_signal(sgna):
    base = _mean(_log(sgna), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_slope_v023_signal(sgna):
    base = _mean(_log(sgna), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_126d_slope_v024_signal(sgna):
    base = _mean(_log(sgna), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_slope_v025_signal(sgna):
    base = _mean(_log(sgna), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_slope_v026_signal(sgna):
    base = _mean(_log(sgna), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_252d_slope_v027_signal(sgna):
    base = _mean(_log(sgna), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_slope_v028_signal(sgna):
    base = _mean(_log(sgna), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_slope_v029_signal(sgna):
    base = _mean(_log(sgna), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_log_504d_slope_v030_signal(sgna):
    base = _mean(_log(sgna), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_slope_v031_signal(sgna):
    base = _z(sgna, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_slope_v032_signal(sgna):
    base = _z(sgna, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_21d_slope_v033_signal(sgna):
    base = _z(sgna, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_slope_v034_signal(sgna):
    base = _z(sgna, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_slope_v035_signal(sgna):
    base = _z(sgna, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_63d_slope_v036_signal(sgna):
    base = _z(sgna, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_slope_v037_signal(sgna):
    base = _z(sgna, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_slope_v038_signal(sgna):
    base = _z(sgna, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_126d_slope_v039_signal(sgna):
    base = _z(sgna, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_slope_v040_signal(sgna):
    base = _z(sgna, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_slope_v041_signal(sgna):
    base = _z(sgna, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_252d_slope_v042_signal(sgna):
    base = _z(sgna, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_slope_v043_signal(sgna):
    base = _z(sgna, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_slope_v044_signal(sgna):
    base = _z(sgna, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_z_504d_slope_v045_signal(sgna):
    base = _z(sgna, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_slope_v046_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_slope_v047_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_21d_slope_v048_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_slope_v049_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_slope_v050_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_63d_slope_v051_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_slope_v052_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_slope_v053_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_126d_slope_v054_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_slope_v055_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_slope_v056_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_252d_slope_v057_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_slope_v058_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_slope_v059_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_ps_504d_slope_v060_signal(sgna, sharesbas):
    base = _safe_div(_mean(sgna, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_slope_v061_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_slope_v062_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_21d_slope_v063_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_slope_v064_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_slope_v065_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_63d_slope_v066_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_slope_v067_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_slope_v068_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_126d_slope_v069_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_slope_v070_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_slope_v071_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_252d_slope_v072_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_slope_v073_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_slope_v074_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_asset_scaled_504d_slope_v075_signal(sgna, assets):
    base = _safe_div(_mean(sgna, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_slope_v076_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_slope_v077_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_21d_slope_v078_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_slope_v079_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_slope_v080_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_63d_slope_v081_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_slope_v082_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_slope_v083_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_126d_slope_v084_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_slope_v085_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_slope_v086_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_252d_slope_v087_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_slope_v088_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_slope_v089_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mcap_scaled_504d_slope_v090_signal(sgna, marketcap):
    base = _safe_div(_mean(sgna, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_slope_v091_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_slope_v092_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_21d_slope_v093_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(21).min(), sgna.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_slope_v094_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_slope_v095_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_63d_slope_v096_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(63).min(), sgna.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_slope_v097_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_slope_v098_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_126d_slope_v099_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(126).min(), sgna.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_slope_v100_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_slope_v101_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_252d_slope_v102_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(252).min(), sgna.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_slope_v103_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_slope_v104_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_low_504d_slope_v105_signal(sgna):
    base = _safe_div(sgna - sgna.rolling(504).min(), sgna.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_slope_v106_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_slope_v107_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_21d_slope_v108_signal(sgna):
    base = _safe_div(sgna.rolling(21).max() - sgna, sgna.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_slope_v109_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_slope_v110_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_63d_slope_v111_signal(sgna):
    base = _safe_div(sgna.rolling(63).max() - sgna, sgna.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_slope_v112_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_slope_v113_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_126d_slope_v114_signal(sgna):
    base = _safe_div(sgna.rolling(126).max() - sgna, sgna.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_slope_v115_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_slope_v116_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_252d_slope_v117_signal(sgna):
    base = _safe_div(sgna.rolling(252).max() - sgna, sgna.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_slope_v118_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_slope_v119_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_dist_high_504d_slope_v120_signal(sgna):
    base = _safe_div(sgna.rolling(504).max() - sgna, sgna.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_slope_v121_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_slope_v122_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_21d_slope_v123_signal(sgna):
    base = _safe_div(_mean(sgna, 21) - _mean(sgna, 42), _mean(sgna, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_slope_v124_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_slope_v125_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_63d_slope_v126_signal(sgna):
    base = _safe_div(_mean(sgna, 63) - _mean(sgna, 126), _mean(sgna, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_slope_v127_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_slope_v128_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_126d_slope_v129_signal(sgna):
    base = _safe_div(_mean(sgna, 126) - _mean(sgna, 252), _mean(sgna, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_slope_v130_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_slope_v131_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_252d_slope_v132_signal(sgna):
    base = _safe_div(_mean(sgna, 252) - _mean(sgna, 504), _mean(sgna, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_slope_v133_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_slope_v134_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_mom_504d_slope_v135_signal(sgna):
    base = _safe_div(_mean(sgna, 504) - _mean(sgna, 1008), _mean(sgna, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_slope_v136_signal(sgna):
    base = _std(sgna, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_slope_v137_signal(sgna):
    base = _std(sgna, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_21d_slope_v138_signal(sgna):
    base = _std(sgna, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_slope_v139_signal(sgna):
    base = _std(sgna, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_slope_v140_signal(sgna):
    base = _std(sgna, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_63d_slope_v141_signal(sgna):
    base = _std(sgna, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_slope_v142_signal(sgna):
    base = _std(sgna, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_slope_v143_signal(sgna):
    base = _std(sgna, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_126d_slope_v144_signal(sgna):
    base = _std(sgna, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_slope_v145_signal(sgna):
    base = _std(sgna, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_slope_v146_signal(sgna):
    base = _std(sgna, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_252d_slope_v147_signal(sgna):
    base = _std(sgna, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_slope_v148_signal(sgna):
    base = _std(sgna, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_slope_v149_signal(sgna):
    base = _std(sgna, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol sgna
def gm_f25_biotech_f25_sga_to_rnd_efficiency_ratio_vol_504d_slope_v150_signal(sgna):
    base = _std(sgna, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

