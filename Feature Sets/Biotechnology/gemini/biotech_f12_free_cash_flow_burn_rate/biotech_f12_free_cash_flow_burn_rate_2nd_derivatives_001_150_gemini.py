
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_slope_v001_signal(fcf):
    base = _mean(fcf, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_slope_v002_signal(fcf):
    base = _mean(fcf, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_21d_slope_v003_signal(fcf):
    base = _mean(fcf, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_slope_v004_signal(fcf):
    base = _mean(fcf, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_slope_v005_signal(fcf):
    base = _mean(fcf, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_63d_slope_v006_signal(fcf):
    base = _mean(fcf, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_slope_v007_signal(fcf):
    base = _mean(fcf, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_slope_v008_signal(fcf):
    base = _mean(fcf, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_126d_slope_v009_signal(fcf):
    base = _mean(fcf, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_slope_v010_signal(fcf):
    base = _mean(fcf, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_slope_v011_signal(fcf):
    base = _mean(fcf, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_252d_slope_v012_signal(fcf):
    base = _mean(fcf, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_slope_v013_signal(fcf):
    base = _mean(fcf, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_slope_v014_signal(fcf):
    base = _mean(fcf, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_raw_504d_slope_v015_signal(fcf):
    base = _mean(fcf, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_slope_v016_signal(fcf):
    base = _mean(_log(fcf), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_slope_v017_signal(fcf):
    base = _mean(_log(fcf), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_21d_slope_v018_signal(fcf):
    base = _mean(_log(fcf), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_slope_v019_signal(fcf):
    base = _mean(_log(fcf), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_slope_v020_signal(fcf):
    base = _mean(_log(fcf), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_63d_slope_v021_signal(fcf):
    base = _mean(_log(fcf), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_slope_v022_signal(fcf):
    base = _mean(_log(fcf), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_slope_v023_signal(fcf):
    base = _mean(_log(fcf), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_126d_slope_v024_signal(fcf):
    base = _mean(_log(fcf), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_slope_v025_signal(fcf):
    base = _mean(_log(fcf), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_slope_v026_signal(fcf):
    base = _mean(_log(fcf), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_252d_slope_v027_signal(fcf):
    base = _mean(_log(fcf), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_slope_v028_signal(fcf):
    base = _mean(_log(fcf), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_slope_v029_signal(fcf):
    base = _mean(_log(fcf), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_log_504d_slope_v030_signal(fcf):
    base = _mean(_log(fcf), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_slope_v031_signal(fcf):
    base = _z(fcf, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_slope_v032_signal(fcf):
    base = _z(fcf, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_21d_slope_v033_signal(fcf):
    base = _z(fcf, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_slope_v034_signal(fcf):
    base = _z(fcf, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_slope_v035_signal(fcf):
    base = _z(fcf, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_63d_slope_v036_signal(fcf):
    base = _z(fcf, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_slope_v037_signal(fcf):
    base = _z(fcf, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_slope_v038_signal(fcf):
    base = _z(fcf, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_126d_slope_v039_signal(fcf):
    base = _z(fcf, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_slope_v040_signal(fcf):
    base = _z(fcf, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_slope_v041_signal(fcf):
    base = _z(fcf, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_252d_slope_v042_signal(fcf):
    base = _z(fcf, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_slope_v043_signal(fcf):
    base = _z(fcf, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_slope_v044_signal(fcf):
    base = _z(fcf, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_z_504d_slope_v045_signal(fcf):
    base = _z(fcf, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_slope_v046_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_slope_v047_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_21d_slope_v048_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_slope_v049_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_slope_v050_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_63d_slope_v051_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_slope_v052_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_slope_v053_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_126d_slope_v054_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_slope_v055_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_slope_v056_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_252d_slope_v057_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_slope_v058_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_slope_v059_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ps_504d_slope_v060_signal(fcf, sharesbas):
    base = _safe_div(_mean(fcf, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_slope_v061_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_slope_v062_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_21d_slope_v063_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_slope_v064_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_slope_v065_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_63d_slope_v066_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_slope_v067_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_slope_v068_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_126d_slope_v069_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_slope_v070_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_slope_v071_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_252d_slope_v072_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_slope_v073_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_slope_v074_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_asset_scaled_504d_slope_v075_signal(fcf, assets):
    base = _safe_div(_mean(fcf, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_slope_v076_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_slope_v077_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_21d_slope_v078_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_slope_v079_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_slope_v080_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_63d_slope_v081_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_slope_v082_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_slope_v083_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_126d_slope_v084_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_slope_v085_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_slope_v086_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_252d_slope_v087_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_slope_v088_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_slope_v089_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mcap_scaled_504d_slope_v090_signal(fcf, marketcap):
    base = _safe_div(_mean(fcf, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_slope_v091_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_slope_v092_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_21d_slope_v093_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(21).min(), fcf.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_slope_v094_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_slope_v095_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_63d_slope_v096_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(63).min(), fcf.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_slope_v097_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_slope_v098_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_126d_slope_v099_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(126).min(), fcf.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_slope_v100_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_slope_v101_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_252d_slope_v102_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(252).min(), fcf.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_slope_v103_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_slope_v104_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_low_504d_slope_v105_signal(fcf):
    base = _safe_div(fcf - fcf.rolling(504).min(), fcf.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_slope_v106_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_slope_v107_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_21d_slope_v108_signal(fcf):
    base = _safe_div(fcf.rolling(21).max() - fcf, fcf.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_slope_v109_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_slope_v110_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_63d_slope_v111_signal(fcf):
    base = _safe_div(fcf.rolling(63).max() - fcf, fcf.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_slope_v112_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_slope_v113_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_126d_slope_v114_signal(fcf):
    base = _safe_div(fcf.rolling(126).max() - fcf, fcf.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_slope_v115_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_slope_v116_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_252d_slope_v117_signal(fcf):
    base = _safe_div(fcf.rolling(252).max() - fcf, fcf.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_slope_v118_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_slope_v119_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_dist_high_504d_slope_v120_signal(fcf):
    base = _safe_div(fcf.rolling(504).max() - fcf, fcf.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_slope_v121_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_slope_v122_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_21d_slope_v123_signal(fcf):
    base = _safe_div(_mean(fcf, 21) - _mean(fcf, 42), _mean(fcf, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_slope_v124_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_slope_v125_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_63d_slope_v126_signal(fcf):
    base = _safe_div(_mean(fcf, 63) - _mean(fcf, 126), _mean(fcf, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_slope_v127_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_slope_v128_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_126d_slope_v129_signal(fcf):
    base = _safe_div(_mean(fcf, 126) - _mean(fcf, 252), _mean(fcf, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_slope_v130_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_slope_v131_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_252d_slope_v132_signal(fcf):
    base = _safe_div(_mean(fcf, 252) - _mean(fcf, 504), _mean(fcf, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_slope_v133_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_slope_v134_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mom_504d_slope_v135_signal(fcf):
    base = _safe_div(_mean(fcf, 504) - _mean(fcf, 1008), _mean(fcf, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_slope_v136_signal(fcf):
    base = _std(fcf, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_slope_v137_signal(fcf):
    base = _std(fcf, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_21d_slope_v138_signal(fcf):
    base = _std(fcf, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_slope_v139_signal(fcf):
    base = _std(fcf, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_slope_v140_signal(fcf):
    base = _std(fcf, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_63d_slope_v141_signal(fcf):
    base = _std(fcf, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_slope_v142_signal(fcf):
    base = _std(fcf, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_slope_v143_signal(fcf):
    base = _std(fcf, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_126d_slope_v144_signal(fcf):
    base = _std(fcf, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_slope_v145_signal(fcf):
    base = _std(fcf, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_slope_v146_signal(fcf):
    base = _std(fcf, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_252d_slope_v147_signal(fcf):
    base = _std(fcf, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_slope_v148_signal(fcf):
    base = _std(fcf, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_slope_v149_signal(fcf):
    base = _std(fcf, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_vol_504d_slope_v150_signal(fcf):
    base = _std(fcf, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

