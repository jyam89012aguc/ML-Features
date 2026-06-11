
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d slope of 21d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_21d_slope_v001_signal(debt):
    base = _mean(debt, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_21d_slope_v002_signal(debt):
    base = _mean(debt, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_21d_slope_v003_signal(debt):
    base = _mean(debt, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_63d_slope_v004_signal(debt):
    base = _mean(debt, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_63d_slope_v005_signal(debt):
    base = _mean(debt, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_63d_slope_v006_signal(debt):
    base = _mean(debt, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_126d_slope_v007_signal(debt):
    base = _mean(debt, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_126d_slope_v008_signal(debt):
    base = _mean(debt, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_126d_slope_v009_signal(debt):
    base = _mean(debt, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_252d_slope_v010_signal(debt):
    base = _mean(debt, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_252d_slope_v011_signal(debt):
    base = _mean(debt, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_252d_slope_v012_signal(debt):
    base = _mean(debt, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_504d_slope_v013_signal(debt):
    base = _mean(debt, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_504d_slope_v014_signal(debt):
    base = _mean(debt, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw debt
def gm_f36_biotech_f36_debt_to_equity_leverage_raw_504d_slope_v015_signal(debt):
    base = _mean(debt, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_21d_slope_v016_signal(debt):
    base = _mean(_log(debt), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_21d_slope_v017_signal(debt):
    base = _mean(_log(debt), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_21d_slope_v018_signal(debt):
    base = _mean(_log(debt), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_63d_slope_v019_signal(debt):
    base = _mean(_log(debt), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_63d_slope_v020_signal(debt):
    base = _mean(_log(debt), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_63d_slope_v021_signal(debt):
    base = _mean(_log(debt), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_126d_slope_v022_signal(debt):
    base = _mean(_log(debt), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_126d_slope_v023_signal(debt):
    base = _mean(_log(debt), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_126d_slope_v024_signal(debt):
    base = _mean(_log(debt), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_252d_slope_v025_signal(debt):
    base = _mean(_log(debt), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_252d_slope_v026_signal(debt):
    base = _mean(_log(debt), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_252d_slope_v027_signal(debt):
    base = _mean(_log(debt), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_504d_slope_v028_signal(debt):
    base = _mean(_log(debt), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_504d_slope_v029_signal(debt):
    base = _mean(_log(debt), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log debt
def gm_f36_biotech_f36_debt_to_equity_leverage_log_504d_slope_v030_signal(debt):
    base = _mean(_log(debt), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_21d_slope_v031_signal(debt):
    base = _z(debt, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_21d_slope_v032_signal(debt):
    base = _z(debt, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_21d_slope_v033_signal(debt):
    base = _z(debt, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_63d_slope_v034_signal(debt):
    base = _z(debt, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_63d_slope_v035_signal(debt):
    base = _z(debt, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_63d_slope_v036_signal(debt):
    base = _z(debt, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_126d_slope_v037_signal(debt):
    base = _z(debt, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_126d_slope_v038_signal(debt):
    base = _z(debt, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_126d_slope_v039_signal(debt):
    base = _z(debt, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_252d_slope_v040_signal(debt):
    base = _z(debt, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_252d_slope_v041_signal(debt):
    base = _z(debt, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_252d_slope_v042_signal(debt):
    base = _z(debt, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_504d_slope_v043_signal(debt):
    base = _z(debt, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_504d_slope_v044_signal(debt):
    base = _z(debt, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z debt
def gm_f36_biotech_f36_debt_to_equity_leverage_z_504d_slope_v045_signal(debt):
    base = _z(debt, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_21d_slope_v046_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_21d_slope_v047_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_21d_slope_v048_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_63d_slope_v049_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_63d_slope_v050_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_63d_slope_v051_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_126d_slope_v052_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_126d_slope_v053_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_126d_slope_v054_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_252d_slope_v055_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_252d_slope_v056_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_252d_slope_v057_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_504d_slope_v058_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_504d_slope_v059_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps debt
def gm_f36_biotech_f36_debt_to_equity_leverage_ps_504d_slope_v060_signal(debt, sharesbas):
    base = _safe_div(_mean(debt, 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_21d_slope_v061_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_21d_slope_v062_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_21d_slope_v063_signal(debt, assets):
    base = _safe_div(_mean(debt, 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_63d_slope_v064_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_63d_slope_v065_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_63d_slope_v066_signal(debt, assets):
    base = _safe_div(_mean(debt, 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_126d_slope_v067_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_126d_slope_v068_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_126d_slope_v069_signal(debt, assets):
    base = _safe_div(_mean(debt, 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_252d_slope_v070_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_252d_slope_v071_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_252d_slope_v072_signal(debt, assets):
    base = _safe_div(_mean(debt, 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_504d_slope_v073_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_504d_slope_v074_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_asset_scaled_504d_slope_v075_signal(debt, assets):
    base = _safe_div(_mean(debt, 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_21d_slope_v076_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_21d_slope_v077_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_21d_slope_v078_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_63d_slope_v079_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_63d_slope_v080_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_63d_slope_v081_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_126d_slope_v082_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_126d_slope_v083_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_126d_slope_v084_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_252d_slope_v085_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_252d_slope_v086_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_252d_slope_v087_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_504d_slope_v088_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_504d_slope_v089_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mcap_scaled_504d_slope_v090_signal(debt, marketcap):
    base = _safe_div(_mean(debt, 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_21d_slope_v091_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_21d_slope_v092_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_21d_slope_v093_signal(debt):
    base = _safe_div(debt - debt.rolling(21).min(), debt.rolling(21).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_63d_slope_v094_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_63d_slope_v095_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_63d_slope_v096_signal(debt):
    base = _safe_div(debt - debt.rolling(63).min(), debt.rolling(63).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_126d_slope_v097_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_126d_slope_v098_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_126d_slope_v099_signal(debt):
    base = _safe_div(debt - debt.rolling(126).min(), debt.rolling(126).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_252d_slope_v100_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_252d_slope_v101_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_252d_slope_v102_signal(debt):
    base = _safe_div(debt - debt.rolling(252).min(), debt.rolling(252).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_504d_slope_v103_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_504d_slope_v104_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_low debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_low_504d_slope_v105_signal(debt):
    base = _safe_div(debt - debt.rolling(504).min(), debt.rolling(504).min())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_21d_slope_v106_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_21d_slope_v107_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_21d_slope_v108_signal(debt):
    base = _safe_div(debt.rolling(21).max() - debt, debt.rolling(21).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_63d_slope_v109_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_63d_slope_v110_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_63d_slope_v111_signal(debt):
    base = _safe_div(debt.rolling(63).max() - debt, debt.rolling(63).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_126d_slope_v112_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_126d_slope_v113_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_126d_slope_v114_signal(debt):
    base = _safe_div(debt.rolling(126).max() - debt, debt.rolling(126).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_252d_slope_v115_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_252d_slope_v116_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_252d_slope_v117_signal(debt):
    base = _safe_div(debt.rolling(252).max() - debt, debt.rolling(252).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_504d_slope_v118_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_504d_slope_v119_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d dist_high debt
def gm_f36_biotech_f36_debt_to_equity_leverage_dist_high_504d_slope_v120_signal(debt):
    base = _safe_div(debt.rolling(504).max() - debt, debt.rolling(504).max())
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_21d_slope_v121_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_21d_slope_v122_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_21d_slope_v123_signal(debt):
    base = _safe_div(_mean(debt, 21) - _mean(debt, 42), _mean(debt, 42))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_63d_slope_v124_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_63d_slope_v125_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_63d_slope_v126_signal(debt):
    base = _safe_div(_mean(debt, 63) - _mean(debt, 126), _mean(debt, 126))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_126d_slope_v127_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_126d_slope_v128_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_126d_slope_v129_signal(debt):
    base = _safe_div(_mean(debt, 126) - _mean(debt, 252), _mean(debt, 252))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_252d_slope_v130_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_252d_slope_v131_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_252d_slope_v132_signal(debt):
    base = _safe_div(_mean(debt, 252) - _mean(debt, 504), _mean(debt, 504))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_504d_slope_v133_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_504d_slope_v134_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mom debt
def gm_f36_biotech_f36_debt_to_equity_leverage_mom_504d_slope_v135_signal(debt):
    base = _safe_div(_mean(debt, 504) - _mean(debt, 1008), _mean(debt, 1008))
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_21d_slope_v136_signal(debt):
    base = _std(debt, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_21d_slope_v137_signal(debt):
    base = _std(debt, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_21d_slope_v138_signal(debt):
    base = _std(debt, 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_63d_slope_v139_signal(debt):
    base = _std(debt, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_63d_slope_v140_signal(debt):
    base = _std(debt, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_63d_slope_v141_signal(debt):
    base = _std(debt, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_126d_slope_v142_signal(debt):
    base = _std(debt, 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_126d_slope_v143_signal(debt):
    base = _std(debt, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_126d_slope_v144_signal(debt):
    base = _std(debt, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_252d_slope_v145_signal(debt):
    base = _std(debt, 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_252d_slope_v146_signal(debt):
    base = _std(debt, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_252d_slope_v147_signal(debt):
    base = _std(debt, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_504d_slope_v148_signal(debt):
    base = _std(debt, 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_504d_slope_v149_signal(debt):
    base = _std(debt, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d vol debt
def gm_f36_biotech_f36_debt_to_equity_leverage_vol_504d_slope_v150_signal(debt):
    base = _std(debt, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

