
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_21d_slope_v001_signal(netinc):
    base = _mean(netinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_21d_slope_v002_signal(netinc):
    base = _mean(netinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_21d_slope_v003_signal(netinc):
    base = _mean(netinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_63d_slope_v004_signal(netinc):
    base = _mean(netinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_63d_slope_v005_signal(netinc):
    base = _mean(netinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_63d_slope_v006_signal(netinc):
    base = _mean(netinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_126d_slope_v007_signal(netinc):
    base = _mean(netinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_126d_slope_v008_signal(netinc):
    base = _mean(netinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_126d_slope_v009_signal(netinc):
    base = _mean(netinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_252d_slope_v010_signal(netinc):
    base = _mean(netinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_252d_slope_v011_signal(netinc):
    base = _mean(netinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_252d_slope_v012_signal(netinc):
    base = _mean(netinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_504d_slope_v013_signal(netinc):
    base = _mean(netinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_504d_slope_v014_signal(netinc):
    base = _mean(netinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_raw_504d_slope_v015_signal(netinc):
    base = _mean(netinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_21d_slope_v016_signal(netinc):
    base = _mean(_log(netinc), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_21d_slope_v017_signal(netinc):
    base = _mean(_log(netinc), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_21d_slope_v018_signal(netinc):
    base = _mean(_log(netinc), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_63d_slope_v019_signal(netinc):
    base = _mean(_log(netinc), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_63d_slope_v020_signal(netinc):
    base = _mean(_log(netinc), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_63d_slope_v021_signal(netinc):
    base = _mean(_log(netinc), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_126d_slope_v022_signal(netinc):
    base = _mean(_log(netinc), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_126d_slope_v023_signal(netinc):
    base = _mean(_log(netinc), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_126d_slope_v024_signal(netinc):
    base = _mean(_log(netinc), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_252d_slope_v025_signal(netinc):
    base = _mean(_log(netinc), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_252d_slope_v026_signal(netinc):
    base = _mean(_log(netinc), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_252d_slope_v027_signal(netinc):
    base = _mean(_log(netinc), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_504d_slope_v028_signal(netinc):
    base = _mean(_log(netinc), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_504d_slope_v029_signal(netinc):
    base = _mean(_log(netinc), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_log_504d_slope_v030_signal(netinc):
    base = _mean(_log(netinc), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_21d_slope_v031_signal(netinc):
    base = _z(netinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_21d_slope_v032_signal(netinc):
    base = _z(netinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_21d_slope_v033_signal(netinc):
    base = _z(netinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_63d_slope_v034_signal(netinc):
    base = _z(netinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_63d_slope_v035_signal(netinc):
    base = _z(netinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_63d_slope_v036_signal(netinc):
    base = _z(netinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_126d_slope_v037_signal(netinc):
    base = _z(netinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_126d_slope_v038_signal(netinc):
    base = _z(netinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_126d_slope_v039_signal(netinc):
    base = _z(netinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_252d_slope_v040_signal(netinc):
    base = _z(netinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_252d_slope_v041_signal(netinc):
    base = _z(netinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_252d_slope_v042_signal(netinc):
    base = _z(netinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_504d_slope_v043_signal(netinc):
    base = _z(netinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_504d_slope_v044_signal(netinc):
    base = _z(netinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_z_504d_slope_v045_signal(netinc):
    base = _z(netinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_21d_slope_v046_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_21d_slope_v047_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_21d_slope_v048_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_63d_slope_v049_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_63d_slope_v050_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_63d_slope_v051_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_126d_slope_v052_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_126d_slope_v053_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_126d_slope_v054_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_252d_slope_v055_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_252d_slope_v056_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_252d_slope_v057_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_504d_slope_v058_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_504d_slope_v059_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_ps_504d_slope_v060_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_21d_slope_v061_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_21d_slope_v062_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_21d_slope_v063_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_63d_slope_v064_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_63d_slope_v065_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_63d_slope_v066_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_126d_slope_v067_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_126d_slope_v068_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_126d_slope_v069_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_252d_slope_v070_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_252d_slope_v071_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_252d_slope_v072_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_504d_slope_v073_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_504d_slope_v074_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_asset_scaled_504d_slope_v075_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_21d_slope_v076_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_21d_slope_v077_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_21d_slope_v078_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_63d_slope_v079_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_63d_slope_v080_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_63d_slope_v081_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_126d_slope_v082_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_126d_slope_v083_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_126d_slope_v084_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_252d_slope_v085_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_252d_slope_v086_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_252d_slope_v087_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_504d_slope_v088_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_504d_slope_v089_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mcap_scaled_504d_slope_v090_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_21d_slope_v091_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_21d_slope_v092_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_21d_slope_v093_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_63d_slope_v094_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_63d_slope_v095_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_63d_slope_v096_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_126d_slope_v097_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_126d_slope_v098_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_126d_slope_v099_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_252d_slope_v100_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_252d_slope_v101_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_252d_slope_v102_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_504d_slope_v103_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_504d_slope_v104_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_low_504d_slope_v105_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_21d_slope_v106_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_21d_slope_v107_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_21d_slope_v108_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_63d_slope_v109_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_63d_slope_v110_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_63d_slope_v111_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_126d_slope_v112_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_126d_slope_v113_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_126d_slope_v114_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_252d_slope_v115_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_252d_slope_v116_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_252d_slope_v117_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_504d_slope_v118_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_504d_slope_v119_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_dist_high_504d_slope_v120_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_21d_slope_v121_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_21d_slope_v122_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_21d_slope_v123_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_63d_slope_v124_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_63d_slope_v125_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_63d_slope_v126_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_126d_slope_v127_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_126d_slope_v128_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_126d_slope_v129_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_252d_slope_v130_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_252d_slope_v131_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_252d_slope_v132_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_504d_slope_v133_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_504d_slope_v134_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_mom_504d_slope_v135_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_21d_slope_v136_signal(netinc):
    base = _std(netinc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_21d_slope_v137_signal(netinc):
    base = _std(netinc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_21d_slope_v138_signal(netinc):
    base = _std(netinc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_63d_slope_v139_signal(netinc):
    base = _std(netinc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_63d_slope_v140_signal(netinc):
    base = _std(netinc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_63d_slope_v141_signal(netinc):
    base = _std(netinc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_126d_slope_v142_signal(netinc):
    base = _std(netinc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_126d_slope_v143_signal(netinc):
    base = _std(netinc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_126d_slope_v144_signal(netinc):
    base = _std(netinc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_252d_slope_v145_signal(netinc):
    base = _std(netinc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_252d_slope_v146_signal(netinc):
    base = _std(netinc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_252d_slope_v147_signal(netinc):
    base = _std(netinc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_504d_slope_v148_signal(netinc):
    base = _std(netinc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_504d_slope_v149_signal(netinc):
    base = _std(netinc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol netinc
def gm_f63_biotech_f63_earnings_accrual_volatility_vol_504d_slope_v150_signal(netinc):
    base = _std(netinc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

