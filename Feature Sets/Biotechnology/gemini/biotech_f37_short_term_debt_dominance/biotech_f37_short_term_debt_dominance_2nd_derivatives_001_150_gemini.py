
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_slope_v001_signal(debtc):
    base = _mean(debtc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_slope_v002_signal(debtc):
    base = _mean(debtc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_21d_slope_v003_signal(debtc):
    base = _mean(debtc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_slope_v004_signal(debtc):
    base = _mean(debtc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_slope_v005_signal(debtc):
    base = _mean(debtc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_63d_slope_v006_signal(debtc):
    base = _mean(debtc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_slope_v007_signal(debtc):
    base = _mean(debtc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_slope_v008_signal(debtc):
    base = _mean(debtc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_126d_slope_v009_signal(debtc):
    base = _mean(debtc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_slope_v010_signal(debtc):
    base = _mean(debtc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_slope_v011_signal(debtc):
    base = _mean(debtc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_252d_slope_v012_signal(debtc):
    base = _mean(debtc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_slope_v013_signal(debtc):
    base = _mean(debtc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_slope_v014_signal(debtc):
    base = _mean(debtc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw debtc
def gm_f37_biotech_f37_short_term_debt_dominance_raw_504d_slope_v015_signal(debtc):
    base = _mean(debtc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_slope_v016_signal(debtc):
    base = _mean(_log(debtc), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_slope_v017_signal(debtc):
    base = _mean(_log(debtc), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_21d_slope_v018_signal(debtc):
    base = _mean(_log(debtc), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_slope_v019_signal(debtc):
    base = _mean(_log(debtc), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_slope_v020_signal(debtc):
    base = _mean(_log(debtc), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_63d_slope_v021_signal(debtc):
    base = _mean(_log(debtc), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_slope_v022_signal(debtc):
    base = _mean(_log(debtc), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_slope_v023_signal(debtc):
    base = _mean(_log(debtc), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_126d_slope_v024_signal(debtc):
    base = _mean(_log(debtc), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_slope_v025_signal(debtc):
    base = _mean(_log(debtc), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_slope_v026_signal(debtc):
    base = _mean(_log(debtc), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_252d_slope_v027_signal(debtc):
    base = _mean(_log(debtc), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_slope_v028_signal(debtc):
    base = _mean(_log(debtc), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_slope_v029_signal(debtc):
    base = _mean(_log(debtc), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log debtc
def gm_f37_biotech_f37_short_term_debt_dominance_log_504d_slope_v030_signal(debtc):
    base = _mean(_log(debtc), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_slope_v031_signal(debtc):
    base = _z(debtc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_slope_v032_signal(debtc):
    base = _z(debtc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_21d_slope_v033_signal(debtc):
    base = _z(debtc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_slope_v034_signal(debtc):
    base = _z(debtc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_slope_v035_signal(debtc):
    base = _z(debtc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_63d_slope_v036_signal(debtc):
    base = _z(debtc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_slope_v037_signal(debtc):
    base = _z(debtc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_slope_v038_signal(debtc):
    base = _z(debtc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_126d_slope_v039_signal(debtc):
    base = _z(debtc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_slope_v040_signal(debtc):
    base = _z(debtc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_slope_v041_signal(debtc):
    base = _z(debtc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_252d_slope_v042_signal(debtc):
    base = _z(debtc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_slope_v043_signal(debtc):
    base = _z(debtc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_slope_v044_signal(debtc):
    base = _z(debtc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z debtc
def gm_f37_biotech_f37_short_term_debt_dominance_z_504d_slope_v045_signal(debtc):
    base = _z(debtc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_slope_v046_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_slope_v047_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_21d_slope_v048_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_slope_v049_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_slope_v050_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_63d_slope_v051_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_slope_v052_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_slope_v053_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_126d_slope_v054_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_slope_v055_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_slope_v056_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_252d_slope_v057_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_slope_v058_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_slope_v059_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps debtc
def gm_f37_biotech_f37_short_term_debt_dominance_ps_504d_slope_v060_signal(debtc, sharesbas):
    base = _safe_div(_mean(debtc, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_slope_v061_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_slope_v062_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_21d_slope_v063_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_slope_v064_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_slope_v065_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_63d_slope_v066_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_slope_v067_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_slope_v068_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_126d_slope_v069_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_slope_v070_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_slope_v071_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_252d_slope_v072_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_slope_v073_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_slope_v074_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_asset_scaled_504d_slope_v075_signal(debtc, assets):
    base = _safe_div(_mean(debtc, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_slope_v076_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_slope_v077_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_21d_slope_v078_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_slope_v079_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_slope_v080_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_63d_slope_v081_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_slope_v082_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_slope_v083_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_126d_slope_v084_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_slope_v085_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_slope_v086_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_252d_slope_v087_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_slope_v088_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_slope_v089_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mcap_scaled_504d_slope_v090_signal(debtc, marketcap):
    base = _safe_div(_mean(debtc, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_slope_v091_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_slope_v092_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_21d_slope_v093_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(21).min(), debtc.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_slope_v094_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_slope_v095_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_63d_slope_v096_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(63).min(), debtc.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_slope_v097_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_slope_v098_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_126d_slope_v099_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(126).min(), debtc.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_slope_v100_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_slope_v101_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_252d_slope_v102_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(252).min(), debtc.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_slope_v103_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_slope_v104_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_low_504d_slope_v105_signal(debtc):
    base = _safe_div(debtc - debtc.rolling(504).min(), debtc.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_slope_v106_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_slope_v107_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_21d_slope_v108_signal(debtc):
    base = _safe_div(debtc.rolling(21).max() - debtc, debtc.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_slope_v109_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_slope_v110_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_63d_slope_v111_signal(debtc):
    base = _safe_div(debtc.rolling(63).max() - debtc, debtc.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_slope_v112_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_slope_v113_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_126d_slope_v114_signal(debtc):
    base = _safe_div(debtc.rolling(126).max() - debtc, debtc.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_slope_v115_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_slope_v116_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_252d_slope_v117_signal(debtc):
    base = _safe_div(debtc.rolling(252).max() - debtc, debtc.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_slope_v118_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_slope_v119_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high debtc
def gm_f37_biotech_f37_short_term_debt_dominance_dist_high_504d_slope_v120_signal(debtc):
    base = _safe_div(debtc.rolling(504).max() - debtc, debtc.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_slope_v121_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_slope_v122_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_21d_slope_v123_signal(debtc):
    base = _safe_div(_mean(debtc, 21) - _mean(debtc, 42), _mean(debtc, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_slope_v124_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_slope_v125_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_63d_slope_v126_signal(debtc):
    base = _safe_div(_mean(debtc, 63) - _mean(debtc, 126), _mean(debtc, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_slope_v127_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_slope_v128_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_126d_slope_v129_signal(debtc):
    base = _safe_div(_mean(debtc, 126) - _mean(debtc, 252), _mean(debtc, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_slope_v130_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_slope_v131_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_252d_slope_v132_signal(debtc):
    base = _safe_div(_mean(debtc, 252) - _mean(debtc, 504), _mean(debtc, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_slope_v133_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_slope_v134_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom debtc
def gm_f37_biotech_f37_short_term_debt_dominance_mom_504d_slope_v135_signal(debtc):
    base = _safe_div(_mean(debtc, 504) - _mean(debtc, 1008), _mean(debtc, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_slope_v136_signal(debtc):
    base = _std(debtc, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_slope_v137_signal(debtc):
    base = _std(debtc, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_21d_slope_v138_signal(debtc):
    base = _std(debtc, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_slope_v139_signal(debtc):
    base = _std(debtc, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_slope_v140_signal(debtc):
    base = _std(debtc, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_63d_slope_v141_signal(debtc):
    base = _std(debtc, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_slope_v142_signal(debtc):
    base = _std(debtc, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_slope_v143_signal(debtc):
    base = _std(debtc, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_126d_slope_v144_signal(debtc):
    base = _std(debtc, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_slope_v145_signal(debtc):
    base = _std(debtc, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_slope_v146_signal(debtc):
    base = _std(debtc, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_252d_slope_v147_signal(debtc):
    base = _std(debtc, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_slope_v148_signal(debtc):
    base = _std(debtc, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_slope_v149_signal(debtc):
    base = _std(debtc, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol debtc
def gm_f37_biotech_f37_short_term_debt_dominance_vol_504d_slope_v150_signal(debtc):
    base = _std(debtc, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

