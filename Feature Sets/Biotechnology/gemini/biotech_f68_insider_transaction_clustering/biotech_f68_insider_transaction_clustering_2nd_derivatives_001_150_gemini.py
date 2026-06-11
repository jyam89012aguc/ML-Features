
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_21d_slope_v001_signal(ownername):
    base = _mean(ownername, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_21d_slope_v002_signal(ownername):
    base = _mean(ownername, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_21d_slope_v003_signal(ownername):
    base = _mean(ownername, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_63d_slope_v004_signal(ownername):
    base = _mean(ownername, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_63d_slope_v005_signal(ownername):
    base = _mean(ownername, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_63d_slope_v006_signal(ownername):
    base = _mean(ownername, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_126d_slope_v007_signal(ownername):
    base = _mean(ownername, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_126d_slope_v008_signal(ownername):
    base = _mean(ownername, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_126d_slope_v009_signal(ownername):
    base = _mean(ownername, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_252d_slope_v010_signal(ownername):
    base = _mean(ownername, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_252d_slope_v011_signal(ownername):
    base = _mean(ownername, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_252d_slope_v012_signal(ownername):
    base = _mean(ownername, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_504d_slope_v013_signal(ownername):
    base = _mean(ownername, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_504d_slope_v014_signal(ownername):
    base = _mean(ownername, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw ownername
def gm_f68_biotech_f68_insider_transaction_clustering_raw_504d_slope_v015_signal(ownername):
    base = _mean(ownername, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_21d_slope_v016_signal(ownername):
    base = _mean(_log(ownername), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_21d_slope_v017_signal(ownername):
    base = _mean(_log(ownername), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_21d_slope_v018_signal(ownername):
    base = _mean(_log(ownername), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_63d_slope_v019_signal(ownername):
    base = _mean(_log(ownername), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_63d_slope_v020_signal(ownername):
    base = _mean(_log(ownername), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_63d_slope_v021_signal(ownername):
    base = _mean(_log(ownername), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_126d_slope_v022_signal(ownername):
    base = _mean(_log(ownername), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_126d_slope_v023_signal(ownername):
    base = _mean(_log(ownername), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_126d_slope_v024_signal(ownername):
    base = _mean(_log(ownername), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_252d_slope_v025_signal(ownername):
    base = _mean(_log(ownername), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_252d_slope_v026_signal(ownername):
    base = _mean(_log(ownername), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_252d_slope_v027_signal(ownername):
    base = _mean(_log(ownername), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_504d_slope_v028_signal(ownername):
    base = _mean(_log(ownername), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_504d_slope_v029_signal(ownername):
    base = _mean(_log(ownername), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log ownername
def gm_f68_biotech_f68_insider_transaction_clustering_log_504d_slope_v030_signal(ownername):
    base = _mean(_log(ownername), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_21d_slope_v031_signal(ownername):
    base = _z(ownername, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_21d_slope_v032_signal(ownername):
    base = _z(ownername, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_21d_slope_v033_signal(ownername):
    base = _z(ownername, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_63d_slope_v034_signal(ownername):
    base = _z(ownername, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_63d_slope_v035_signal(ownername):
    base = _z(ownername, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_63d_slope_v036_signal(ownername):
    base = _z(ownername, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_126d_slope_v037_signal(ownername):
    base = _z(ownername, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_126d_slope_v038_signal(ownername):
    base = _z(ownername, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_126d_slope_v039_signal(ownername):
    base = _z(ownername, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_252d_slope_v040_signal(ownername):
    base = _z(ownername, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_252d_slope_v041_signal(ownername):
    base = _z(ownername, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_252d_slope_v042_signal(ownername):
    base = _z(ownername, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_504d_slope_v043_signal(ownername):
    base = _z(ownername, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_504d_slope_v044_signal(ownername):
    base = _z(ownername, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z ownername
def gm_f68_biotech_f68_insider_transaction_clustering_z_504d_slope_v045_signal(ownername):
    base = _z(ownername, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_21d_slope_v046_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_21d_slope_v047_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_21d_slope_v048_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_63d_slope_v049_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_63d_slope_v050_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_63d_slope_v051_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_126d_slope_v052_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_126d_slope_v053_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_126d_slope_v054_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_252d_slope_v055_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_252d_slope_v056_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_252d_slope_v057_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_504d_slope_v058_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_504d_slope_v059_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ps_504d_slope_v060_signal(ownername, sharesbas):
    base = _safe_div(_mean(ownername, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_21d_slope_v061_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_21d_slope_v062_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_21d_slope_v063_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_63d_slope_v064_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_63d_slope_v065_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_63d_slope_v066_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_126d_slope_v067_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_126d_slope_v068_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_126d_slope_v069_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_252d_slope_v070_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_252d_slope_v071_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_252d_slope_v072_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_504d_slope_v073_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_504d_slope_v074_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_asset_scaled_504d_slope_v075_signal(ownername, assets):
    base = _safe_div(_mean(ownername, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_21d_slope_v076_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_21d_slope_v077_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_21d_slope_v078_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_63d_slope_v079_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_63d_slope_v080_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_63d_slope_v081_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_126d_slope_v082_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_126d_slope_v083_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_126d_slope_v084_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_252d_slope_v085_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_252d_slope_v086_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_252d_slope_v087_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_504d_slope_v088_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_504d_slope_v089_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mcap_scaled_504d_slope_v090_signal(ownername, marketcap):
    base = _safe_div(_mean(ownername, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_21d_slope_v091_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(21).min(), ownername.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_21d_slope_v092_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(21).min(), ownername.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_21d_slope_v093_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(21).min(), ownername.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_63d_slope_v094_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(63).min(), ownername.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_63d_slope_v095_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(63).min(), ownername.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_63d_slope_v096_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(63).min(), ownername.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_126d_slope_v097_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(126).min(), ownername.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_126d_slope_v098_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(126).min(), ownername.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_126d_slope_v099_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(126).min(), ownername.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_252d_slope_v100_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(252).min(), ownername.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_252d_slope_v101_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(252).min(), ownername.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_252d_slope_v102_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(252).min(), ownername.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_504d_slope_v103_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(504).min(), ownername.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_504d_slope_v104_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(504).min(), ownername.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_low_504d_slope_v105_signal(ownername):
    base = _safe_div(ownername - ownername.rolling(504).min(), ownername.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_21d_slope_v106_signal(ownername):
    base = _safe_div(ownername.rolling(21).max() - ownername, ownername.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_21d_slope_v107_signal(ownername):
    base = _safe_div(ownername.rolling(21).max() - ownername, ownername.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_21d_slope_v108_signal(ownername):
    base = _safe_div(ownername.rolling(21).max() - ownername, ownername.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_63d_slope_v109_signal(ownername):
    base = _safe_div(ownername.rolling(63).max() - ownername, ownername.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_63d_slope_v110_signal(ownername):
    base = _safe_div(ownername.rolling(63).max() - ownername, ownername.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_63d_slope_v111_signal(ownername):
    base = _safe_div(ownername.rolling(63).max() - ownername, ownername.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_126d_slope_v112_signal(ownername):
    base = _safe_div(ownername.rolling(126).max() - ownername, ownername.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_126d_slope_v113_signal(ownername):
    base = _safe_div(ownername.rolling(126).max() - ownername, ownername.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_126d_slope_v114_signal(ownername):
    base = _safe_div(ownername.rolling(126).max() - ownername, ownername.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_252d_slope_v115_signal(ownername):
    base = _safe_div(ownername.rolling(252).max() - ownername, ownername.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_252d_slope_v116_signal(ownername):
    base = _safe_div(ownername.rolling(252).max() - ownername, ownername.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_252d_slope_v117_signal(ownername):
    base = _safe_div(ownername.rolling(252).max() - ownername, ownername.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_504d_slope_v118_signal(ownername):
    base = _safe_div(ownername.rolling(504).max() - ownername, ownername.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_504d_slope_v119_signal(ownername):
    base = _safe_div(ownername.rolling(504).max() - ownername, ownername.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high ownername
def gm_f68_biotech_f68_insider_transaction_clustering_dist_high_504d_slope_v120_signal(ownername):
    base = _safe_div(ownername.rolling(504).max() - ownername, ownername.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_21d_slope_v121_signal(ownername):
    base = _safe_div(_mean(ownername, 21) - _mean(ownername, 42), _mean(ownername, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_21d_slope_v122_signal(ownername):
    base = _safe_div(_mean(ownername, 21) - _mean(ownername, 42), _mean(ownername, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_21d_slope_v123_signal(ownername):
    base = _safe_div(_mean(ownername, 21) - _mean(ownername, 42), _mean(ownername, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_63d_slope_v124_signal(ownername):
    base = _safe_div(_mean(ownername, 63) - _mean(ownername, 126), _mean(ownername, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_63d_slope_v125_signal(ownername):
    base = _safe_div(_mean(ownername, 63) - _mean(ownername, 126), _mean(ownername, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_63d_slope_v126_signal(ownername):
    base = _safe_div(_mean(ownername, 63) - _mean(ownername, 126), _mean(ownername, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_126d_slope_v127_signal(ownername):
    base = _safe_div(_mean(ownername, 126) - _mean(ownername, 252), _mean(ownername, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_126d_slope_v128_signal(ownername):
    base = _safe_div(_mean(ownername, 126) - _mean(ownername, 252), _mean(ownername, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_126d_slope_v129_signal(ownername):
    base = _safe_div(_mean(ownername, 126) - _mean(ownername, 252), _mean(ownername, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_252d_slope_v130_signal(ownername):
    base = _safe_div(_mean(ownername, 252) - _mean(ownername, 504), _mean(ownername, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_252d_slope_v131_signal(ownername):
    base = _safe_div(_mean(ownername, 252) - _mean(ownername, 504), _mean(ownername, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_252d_slope_v132_signal(ownername):
    base = _safe_div(_mean(ownername, 252) - _mean(ownername, 504), _mean(ownername, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_504d_slope_v133_signal(ownername):
    base = _safe_div(_mean(ownername, 504) - _mean(ownername, 1008), _mean(ownername, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_504d_slope_v134_signal(ownername):
    base = _safe_div(_mean(ownername, 504) - _mean(ownername, 1008), _mean(ownername, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mom_504d_slope_v135_signal(ownername):
    base = _safe_div(_mean(ownername, 504) - _mean(ownername, 1008), _mean(ownername, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_21d_slope_v136_signal(ownername):
    base = _std(ownername, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_21d_slope_v137_signal(ownername):
    base = _std(ownername, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_21d_slope_v138_signal(ownername):
    base = _std(ownername, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_63d_slope_v139_signal(ownername):
    base = _std(ownername, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_63d_slope_v140_signal(ownername):
    base = _std(ownername, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_63d_slope_v141_signal(ownername):
    base = _std(ownername, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_126d_slope_v142_signal(ownername):
    base = _std(ownername, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_126d_slope_v143_signal(ownername):
    base = _std(ownername, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_126d_slope_v144_signal(ownername):
    base = _std(ownername, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_252d_slope_v145_signal(ownername):
    base = _std(ownername, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_252d_slope_v146_signal(ownername):
    base = _std(ownername, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_252d_slope_v147_signal(ownername):
    base = _std(ownername, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_504d_slope_v148_signal(ownername):
    base = _std(ownername, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_504d_slope_v149_signal(ownername):
    base = _std(ownername, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol ownername
def gm_f68_biotech_f68_insider_transaction_clustering_vol_504d_slope_v150_signal(ownername):
    base = _std(ownername, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

