
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_21d_slope_v001_signal(invcap):
    base = _mean(invcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_21d_slope_v002_signal(invcap):
    base = _mean(invcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_21d_slope_v003_signal(invcap):
    base = _mean(invcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_63d_slope_v004_signal(invcap):
    base = _mean(invcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_63d_slope_v005_signal(invcap):
    base = _mean(invcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_63d_slope_v006_signal(invcap):
    base = _mean(invcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_126d_slope_v007_signal(invcap):
    base = _mean(invcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_126d_slope_v008_signal(invcap):
    base = _mean(invcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_126d_slope_v009_signal(invcap):
    base = _mean(invcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_252d_slope_v010_signal(invcap):
    base = _mean(invcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_252d_slope_v011_signal(invcap):
    base = _mean(invcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_252d_slope_v012_signal(invcap):
    base = _mean(invcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_504d_slope_v013_signal(invcap):
    base = _mean(invcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_504d_slope_v014_signal(invcap):
    base = _mean(invcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_raw_504d_slope_v015_signal(invcap):
    base = _mean(invcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_21d_slope_v016_signal(invcap):
    base = _mean(_log(invcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_21d_slope_v017_signal(invcap):
    base = _mean(_log(invcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_21d_slope_v018_signal(invcap):
    base = _mean(_log(invcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_63d_slope_v019_signal(invcap):
    base = _mean(_log(invcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_63d_slope_v020_signal(invcap):
    base = _mean(_log(invcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_63d_slope_v021_signal(invcap):
    base = _mean(_log(invcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_126d_slope_v022_signal(invcap):
    base = _mean(_log(invcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_126d_slope_v023_signal(invcap):
    base = _mean(_log(invcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_126d_slope_v024_signal(invcap):
    base = _mean(_log(invcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_252d_slope_v025_signal(invcap):
    base = _mean(_log(invcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_252d_slope_v026_signal(invcap):
    base = _mean(_log(invcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_252d_slope_v027_signal(invcap):
    base = _mean(_log(invcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_504d_slope_v028_signal(invcap):
    base = _mean(_log(invcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_504d_slope_v029_signal(invcap):
    base = _mean(_log(invcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_log_504d_slope_v030_signal(invcap):
    base = _mean(_log(invcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_21d_slope_v031_signal(invcap):
    base = _z(invcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_21d_slope_v032_signal(invcap):
    base = _z(invcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_21d_slope_v033_signal(invcap):
    base = _z(invcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_63d_slope_v034_signal(invcap):
    base = _z(invcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_63d_slope_v035_signal(invcap):
    base = _z(invcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_63d_slope_v036_signal(invcap):
    base = _z(invcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_126d_slope_v037_signal(invcap):
    base = _z(invcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_126d_slope_v038_signal(invcap):
    base = _z(invcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_126d_slope_v039_signal(invcap):
    base = _z(invcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_252d_slope_v040_signal(invcap):
    base = _z(invcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_252d_slope_v041_signal(invcap):
    base = _z(invcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_252d_slope_v042_signal(invcap):
    base = _z(invcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_504d_slope_v043_signal(invcap):
    base = _z(invcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_504d_slope_v044_signal(invcap):
    base = _z(invcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_z_504d_slope_v045_signal(invcap):
    base = _z(invcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_21d_slope_v046_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_21d_slope_v047_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_21d_slope_v048_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_63d_slope_v049_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_63d_slope_v050_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_63d_slope_v051_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_126d_slope_v052_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_126d_slope_v053_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_126d_slope_v054_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_252d_slope_v055_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_252d_slope_v056_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_252d_slope_v057_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_504d_slope_v058_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_504d_slope_v059_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ps_504d_slope_v060_signal(invcap, sharesbas):
    base = _safe_div(_mean(invcap, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_21d_slope_v061_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_21d_slope_v062_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_21d_slope_v063_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_63d_slope_v064_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_63d_slope_v065_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_63d_slope_v066_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_126d_slope_v067_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_126d_slope_v068_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_126d_slope_v069_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_252d_slope_v070_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_252d_slope_v071_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_252d_slope_v072_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_504d_slope_v073_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_504d_slope_v074_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_asset_scaled_504d_slope_v075_signal(invcap, assets):
    base = _safe_div(_mean(invcap, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_21d_slope_v076_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_21d_slope_v077_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_21d_slope_v078_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_63d_slope_v079_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_63d_slope_v080_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_63d_slope_v081_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_126d_slope_v082_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_126d_slope_v083_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_126d_slope_v084_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_252d_slope_v085_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_252d_slope_v086_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_252d_slope_v087_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_504d_slope_v088_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_504d_slope_v089_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mcap_scaled_504d_slope_v090_signal(invcap, marketcap):
    base = _safe_div(_mean(invcap, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_21d_slope_v091_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(21).min(), invcap.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_21d_slope_v092_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(21).min(), invcap.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_21d_slope_v093_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(21).min(), invcap.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_63d_slope_v094_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(63).min(), invcap.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_63d_slope_v095_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(63).min(), invcap.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_63d_slope_v096_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(63).min(), invcap.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_126d_slope_v097_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(126).min(), invcap.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_126d_slope_v098_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(126).min(), invcap.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_126d_slope_v099_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(126).min(), invcap.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_252d_slope_v100_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(252).min(), invcap.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_252d_slope_v101_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(252).min(), invcap.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_252d_slope_v102_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(252).min(), invcap.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_504d_slope_v103_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(504).min(), invcap.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_504d_slope_v104_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(504).min(), invcap.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_low_504d_slope_v105_signal(invcap):
    base = _safe_div(invcap - invcap.rolling(504).min(), invcap.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_21d_slope_v106_signal(invcap):
    base = _safe_div(invcap.rolling(21).max() - invcap, invcap.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_21d_slope_v107_signal(invcap):
    base = _safe_div(invcap.rolling(21).max() - invcap, invcap.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_21d_slope_v108_signal(invcap):
    base = _safe_div(invcap.rolling(21).max() - invcap, invcap.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_63d_slope_v109_signal(invcap):
    base = _safe_div(invcap.rolling(63).max() - invcap, invcap.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_63d_slope_v110_signal(invcap):
    base = _safe_div(invcap.rolling(63).max() - invcap, invcap.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_63d_slope_v111_signal(invcap):
    base = _safe_div(invcap.rolling(63).max() - invcap, invcap.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_126d_slope_v112_signal(invcap):
    base = _safe_div(invcap.rolling(126).max() - invcap, invcap.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_126d_slope_v113_signal(invcap):
    base = _safe_div(invcap.rolling(126).max() - invcap, invcap.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_126d_slope_v114_signal(invcap):
    base = _safe_div(invcap.rolling(126).max() - invcap, invcap.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_252d_slope_v115_signal(invcap):
    base = _safe_div(invcap.rolling(252).max() - invcap, invcap.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_252d_slope_v116_signal(invcap):
    base = _safe_div(invcap.rolling(252).max() - invcap, invcap.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_252d_slope_v117_signal(invcap):
    base = _safe_div(invcap.rolling(252).max() - invcap, invcap.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_504d_slope_v118_signal(invcap):
    base = _safe_div(invcap.rolling(504).max() - invcap, invcap.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_504d_slope_v119_signal(invcap):
    base = _safe_div(invcap.rolling(504).max() - invcap, invcap.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_dist_high_504d_slope_v120_signal(invcap):
    base = _safe_div(invcap.rolling(504).max() - invcap, invcap.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_21d_slope_v121_signal(invcap):
    base = _safe_div(_mean(invcap, 21) - _mean(invcap, 42), _mean(invcap, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_21d_slope_v122_signal(invcap):
    base = _safe_div(_mean(invcap, 21) - _mean(invcap, 42), _mean(invcap, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_21d_slope_v123_signal(invcap):
    base = _safe_div(_mean(invcap, 21) - _mean(invcap, 42), _mean(invcap, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_63d_slope_v124_signal(invcap):
    base = _safe_div(_mean(invcap, 63) - _mean(invcap, 126), _mean(invcap, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_63d_slope_v125_signal(invcap):
    base = _safe_div(_mean(invcap, 63) - _mean(invcap, 126), _mean(invcap, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_63d_slope_v126_signal(invcap):
    base = _safe_div(_mean(invcap, 63) - _mean(invcap, 126), _mean(invcap, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_126d_slope_v127_signal(invcap):
    base = _safe_div(_mean(invcap, 126) - _mean(invcap, 252), _mean(invcap, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_126d_slope_v128_signal(invcap):
    base = _safe_div(_mean(invcap, 126) - _mean(invcap, 252), _mean(invcap, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_126d_slope_v129_signal(invcap):
    base = _safe_div(_mean(invcap, 126) - _mean(invcap, 252), _mean(invcap, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_252d_slope_v130_signal(invcap):
    base = _safe_div(_mean(invcap, 252) - _mean(invcap, 504), _mean(invcap, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_252d_slope_v131_signal(invcap):
    base = _safe_div(_mean(invcap, 252) - _mean(invcap, 504), _mean(invcap, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_252d_slope_v132_signal(invcap):
    base = _safe_div(_mean(invcap, 252) - _mean(invcap, 504), _mean(invcap, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_504d_slope_v133_signal(invcap):
    base = _safe_div(_mean(invcap, 504) - _mean(invcap, 1008), _mean(invcap, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_504d_slope_v134_signal(invcap):
    base = _safe_div(_mean(invcap, 504) - _mean(invcap, 1008), _mean(invcap, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mom_504d_slope_v135_signal(invcap):
    base = _safe_div(_mean(invcap, 504) - _mean(invcap, 1008), _mean(invcap, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_21d_slope_v136_signal(invcap):
    base = _std(invcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_21d_slope_v137_signal(invcap):
    base = _std(invcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_21d_slope_v138_signal(invcap):
    base = _std(invcap, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_63d_slope_v139_signal(invcap):
    base = _std(invcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_63d_slope_v140_signal(invcap):
    base = _std(invcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_63d_slope_v141_signal(invcap):
    base = _std(invcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_126d_slope_v142_signal(invcap):
    base = _std(invcap, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_126d_slope_v143_signal(invcap):
    base = _std(invcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_126d_slope_v144_signal(invcap):
    base = _std(invcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_252d_slope_v145_signal(invcap):
    base = _std(invcap, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_252d_slope_v146_signal(invcap):
    base = _std(invcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_252d_slope_v147_signal(invcap):
    base = _std(invcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_504d_slope_v148_signal(invcap):
    base = _std(invcap, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_504d_slope_v149_signal(invcap):
    base = _std(invcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_vol_504d_slope_v150_signal(invcap):
    base = _std(invcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

