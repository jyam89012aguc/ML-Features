
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_21d_slope_v001_signal(sbcomp):
    base = _mean(sbcomp, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_21d_slope_v002_signal(sbcomp):
    base = _mean(sbcomp, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_21d_slope_v003_signal(sbcomp):
    base = _mean(sbcomp, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_63d_slope_v004_signal(sbcomp):
    base = _mean(sbcomp, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_63d_slope_v005_signal(sbcomp):
    base = _mean(sbcomp, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_63d_slope_v006_signal(sbcomp):
    base = _mean(sbcomp, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_126d_slope_v007_signal(sbcomp):
    base = _mean(sbcomp, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_126d_slope_v008_signal(sbcomp):
    base = _mean(sbcomp, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_126d_slope_v009_signal(sbcomp):
    base = _mean(sbcomp, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_252d_slope_v010_signal(sbcomp):
    base = _mean(sbcomp, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_252d_slope_v011_signal(sbcomp):
    base = _mean(sbcomp, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_252d_slope_v012_signal(sbcomp):
    base = _mean(sbcomp, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_504d_slope_v013_signal(sbcomp):
    base = _mean(sbcomp, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_504d_slope_v014_signal(sbcomp):
    base = _mean(sbcomp, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_raw_504d_slope_v015_signal(sbcomp):
    base = _mean(sbcomp, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_21d_slope_v016_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_21d_slope_v017_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_21d_slope_v018_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_63d_slope_v019_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_63d_slope_v020_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_63d_slope_v021_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_126d_slope_v022_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_126d_slope_v023_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_126d_slope_v024_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_252d_slope_v025_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_252d_slope_v026_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_252d_slope_v027_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_504d_slope_v028_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_504d_slope_v029_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_log_504d_slope_v030_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_21d_slope_v031_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_21d_slope_v032_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_21d_slope_v033_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_63d_slope_v034_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_63d_slope_v035_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_63d_slope_v036_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_126d_slope_v037_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_126d_slope_v038_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_126d_slope_v039_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_252d_slope_v040_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_252d_slope_v041_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_252d_slope_v042_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_504d_slope_v043_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_504d_slope_v044_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_z_504d_slope_v045_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_21d_slope_v046_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_21d_slope_v047_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_21d_slope_v048_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_63d_slope_v049_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_63d_slope_v050_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_63d_slope_v051_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_126d_slope_v052_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_126d_slope_v053_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_126d_slope_v054_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_252d_slope_v055_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_252d_slope_v056_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_252d_slope_v057_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_504d_slope_v058_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_504d_slope_v059_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_ps_504d_slope_v060_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_21d_slope_v061_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_21d_slope_v062_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_21d_slope_v063_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_63d_slope_v064_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_63d_slope_v065_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_63d_slope_v066_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_126d_slope_v067_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_126d_slope_v068_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_126d_slope_v069_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_252d_slope_v070_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_252d_slope_v071_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_252d_slope_v072_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_504d_slope_v073_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_504d_slope_v074_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_asset_scaled_504d_slope_v075_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_21d_slope_v076_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_21d_slope_v077_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_21d_slope_v078_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_63d_slope_v079_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_63d_slope_v080_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_63d_slope_v081_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_126d_slope_v082_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_126d_slope_v083_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_126d_slope_v084_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_252d_slope_v085_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_252d_slope_v086_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_252d_slope_v087_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_504d_slope_v088_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_504d_slope_v089_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mcap_scaled_504d_slope_v090_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_21d_slope_v091_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_21d_slope_v092_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_21d_slope_v093_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_63d_slope_v094_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_63d_slope_v095_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_63d_slope_v096_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_126d_slope_v097_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_126d_slope_v098_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_126d_slope_v099_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_252d_slope_v100_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_252d_slope_v101_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_252d_slope_v102_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_504d_slope_v103_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_504d_slope_v104_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_low_504d_slope_v105_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_21d_slope_v106_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_21d_slope_v107_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_21d_slope_v108_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_63d_slope_v109_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_63d_slope_v110_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_63d_slope_v111_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_126d_slope_v112_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_126d_slope_v113_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_126d_slope_v114_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_252d_slope_v115_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_252d_slope_v116_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_252d_slope_v117_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_504d_slope_v118_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_504d_slope_v119_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_dist_high_504d_slope_v120_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_21d_slope_v121_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_21d_slope_v122_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_21d_slope_v123_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_63d_slope_v124_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_63d_slope_v125_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_63d_slope_v126_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_126d_slope_v127_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_126d_slope_v128_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_126d_slope_v129_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_252d_slope_v130_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_252d_slope_v131_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_252d_slope_v132_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_504d_slope_v133_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_504d_slope_v134_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_mom_504d_slope_v135_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_21d_slope_v136_signal(sbcomp):
    base = _std(sbcomp, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_21d_slope_v137_signal(sbcomp):
    base = _std(sbcomp, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_21d_slope_v138_signal(sbcomp):
    base = _std(sbcomp, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_63d_slope_v139_signal(sbcomp):
    base = _std(sbcomp, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_63d_slope_v140_signal(sbcomp):
    base = _std(sbcomp, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_63d_slope_v141_signal(sbcomp):
    base = _std(sbcomp, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_126d_slope_v142_signal(sbcomp):
    base = _std(sbcomp, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_126d_slope_v143_signal(sbcomp):
    base = _std(sbcomp, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_126d_slope_v144_signal(sbcomp):
    base = _std(sbcomp, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_252d_slope_v145_signal(sbcomp):
    base = _std(sbcomp, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_252d_slope_v146_signal(sbcomp):
    base = _std(sbcomp, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_252d_slope_v147_signal(sbcomp):
    base = _std(sbcomp, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_504d_slope_v148_signal(sbcomp):
    base = _std(sbcomp, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_504d_slope_v149_signal(sbcomp):
    base = _std(sbcomp, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol sbcomp
def gm_f30_biotech_f30_stock_based_compensation_expense_vol_504d_slope_v150_signal(sbcomp):
    base = _std(sbcomp, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

