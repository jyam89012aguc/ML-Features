
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_21d_accel_v001_signal(netinc):
    base = _mean(netinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_21d_accel_v002_signal(netinc):
    base = _mean(netinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_21d_accel_v003_signal(netinc):
    base = _mean(netinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_63d_accel_v004_signal(netinc):
    base = _mean(netinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_63d_accel_v005_signal(netinc):
    base = _mean(netinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_63d_accel_v006_signal(netinc):
    base = _mean(netinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_126d_accel_v007_signal(netinc):
    base = _mean(netinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_126d_accel_v008_signal(netinc):
    base = _mean(netinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_126d_accel_v009_signal(netinc):
    base = _mean(netinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_252d_accel_v010_signal(netinc):
    base = _mean(netinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_252d_accel_v011_signal(netinc):
    base = _mean(netinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_252d_accel_v012_signal(netinc):
    base = _mean(netinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_504d_accel_v013_signal(netinc):
    base = _mean(netinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_504d_accel_v014_signal(netinc):
    base = _mean(netinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw netinc
def gm_f46_biotech_f46_net_profit_margin_raw_504d_accel_v015_signal(netinc):
    base = _mean(netinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_21d_accel_v016_signal(netinc):
    base = _mean(_log(netinc), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_21d_accel_v017_signal(netinc):
    base = _mean(_log(netinc), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_21d_accel_v018_signal(netinc):
    base = _mean(_log(netinc), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_63d_accel_v019_signal(netinc):
    base = _mean(_log(netinc), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_63d_accel_v020_signal(netinc):
    base = _mean(_log(netinc), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_63d_accel_v021_signal(netinc):
    base = _mean(_log(netinc), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_126d_accel_v022_signal(netinc):
    base = _mean(_log(netinc), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_126d_accel_v023_signal(netinc):
    base = _mean(_log(netinc), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_126d_accel_v024_signal(netinc):
    base = _mean(_log(netinc), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_252d_accel_v025_signal(netinc):
    base = _mean(_log(netinc), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_252d_accel_v026_signal(netinc):
    base = _mean(_log(netinc), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_252d_accel_v027_signal(netinc):
    base = _mean(_log(netinc), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_504d_accel_v028_signal(netinc):
    base = _mean(_log(netinc), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_504d_accel_v029_signal(netinc):
    base = _mean(_log(netinc), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log netinc
def gm_f46_biotech_f46_net_profit_margin_log_504d_accel_v030_signal(netinc):
    base = _mean(_log(netinc), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_21d_accel_v031_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_21d_accel_v032_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_21d_accel_v033_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_63d_accel_v034_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_63d_accel_v035_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_63d_accel_v036_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_126d_accel_v037_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_126d_accel_v038_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_126d_accel_v039_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_252d_accel_v040_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_252d_accel_v041_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_252d_accel_v042_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_504d_accel_v043_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_504d_accel_v044_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z netinc
def gm_f46_biotech_f46_net_profit_margin_z_504d_accel_v045_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_21d_accel_v046_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_21d_accel_v047_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_21d_accel_v048_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_63d_accel_v049_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_63d_accel_v050_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_63d_accel_v051_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_126d_accel_v052_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_126d_accel_v053_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_126d_accel_v054_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_252d_accel_v055_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_252d_accel_v056_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_252d_accel_v057_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_504d_accel_v058_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_504d_accel_v059_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps netinc
def gm_f46_biotech_f46_net_profit_margin_ps_504d_accel_v060_signal(netinc, sharesbas):
    base = _safe_div(_mean(netinc, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_21d_accel_v061_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_21d_accel_v062_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_21d_accel_v063_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_63d_accel_v064_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_63d_accel_v065_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_63d_accel_v066_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_126d_accel_v067_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_126d_accel_v068_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_126d_accel_v069_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_252d_accel_v070_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_252d_accel_v071_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_252d_accel_v072_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_504d_accel_v073_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_504d_accel_v074_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_asset_scaled_504d_accel_v075_signal(netinc, assets):
    base = _safe_div(_mean(netinc, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_21d_accel_v076_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_21d_accel_v077_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_21d_accel_v078_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_63d_accel_v079_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_63d_accel_v080_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_63d_accel_v081_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_126d_accel_v082_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_126d_accel_v083_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_126d_accel_v084_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_252d_accel_v085_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_252d_accel_v086_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_252d_accel_v087_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_504d_accel_v088_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_504d_accel_v089_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled netinc
def gm_f46_biotech_f46_net_profit_margin_mcap_scaled_504d_accel_v090_signal(netinc, marketcap):
    base = _safe_div(_mean(netinc, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_21d_accel_v091_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_21d_accel_v092_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_21d_accel_v093_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(21).min(), netinc.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_63d_accel_v094_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_63d_accel_v095_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_63d_accel_v096_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(63).min(), netinc.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_126d_accel_v097_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_126d_accel_v098_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_126d_accel_v099_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(126).min(), netinc.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_252d_accel_v100_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_252d_accel_v101_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_252d_accel_v102_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(252).min(), netinc.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_504d_accel_v103_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_504d_accel_v104_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low netinc
def gm_f46_biotech_f46_net_profit_margin_dist_low_504d_accel_v105_signal(netinc):
    base = _safe_div(netinc - netinc.rolling(504).min(), netinc.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_21d_accel_v106_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_21d_accel_v107_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_21d_accel_v108_signal(netinc):
    base = _safe_div(netinc.rolling(21).max() - netinc, netinc.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_63d_accel_v109_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_63d_accel_v110_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_63d_accel_v111_signal(netinc):
    base = _safe_div(netinc.rolling(63).max() - netinc, netinc.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_126d_accel_v112_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_126d_accel_v113_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_126d_accel_v114_signal(netinc):
    base = _safe_div(netinc.rolling(126).max() - netinc, netinc.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_252d_accel_v115_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_252d_accel_v116_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_252d_accel_v117_signal(netinc):
    base = _safe_div(netinc.rolling(252).max() - netinc, netinc.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_504d_accel_v118_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_504d_accel_v119_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high netinc
def gm_f46_biotech_f46_net_profit_margin_dist_high_504d_accel_v120_signal(netinc):
    base = _safe_div(netinc.rolling(504).max() - netinc, netinc.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_21d_accel_v121_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_21d_accel_v122_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_21d_accel_v123_signal(netinc):
    base = _safe_div(_mean(netinc, 21) - _mean(netinc, 42), _mean(netinc, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_63d_accel_v124_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_63d_accel_v125_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_63d_accel_v126_signal(netinc):
    base = _safe_div(_mean(netinc, 63) - _mean(netinc, 126), _mean(netinc, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_126d_accel_v127_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_126d_accel_v128_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_126d_accel_v129_signal(netinc):
    base = _safe_div(_mean(netinc, 126) - _mean(netinc, 252), _mean(netinc, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_252d_accel_v130_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_252d_accel_v131_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_252d_accel_v132_signal(netinc):
    base = _safe_div(_mean(netinc, 252) - _mean(netinc, 504), _mean(netinc, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_504d_accel_v133_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_504d_accel_v134_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom netinc
def gm_f46_biotech_f46_net_profit_margin_mom_504d_accel_v135_signal(netinc):
    base = _safe_div(_mean(netinc, 504) - _mean(netinc, 1008), _mean(netinc, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_21d_accel_v136_signal(netinc):
    base = _std(netinc, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_21d_accel_v137_signal(netinc):
    base = _std(netinc, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_21d_accel_v138_signal(netinc):
    base = _std(netinc, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_63d_accel_v139_signal(netinc):
    base = _std(netinc, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_63d_accel_v140_signal(netinc):
    base = _std(netinc, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_63d_accel_v141_signal(netinc):
    base = _std(netinc, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_126d_accel_v142_signal(netinc):
    base = _std(netinc, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_126d_accel_v143_signal(netinc):
    base = _std(netinc, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_126d_accel_v144_signal(netinc):
    base = _std(netinc, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_252d_accel_v145_signal(netinc):
    base = _std(netinc, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_252d_accel_v146_signal(netinc):
    base = _std(netinc, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_252d_accel_v147_signal(netinc):
    base = _std(netinc, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_504d_accel_v148_signal(netinc):
    base = _std(netinc, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_504d_accel_v149_signal(netinc):
    base = _std(netinc, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol netinc
def gm_f46_biotech_f46_net_profit_margin_vol_504d_accel_v150_signal(netinc):
    base = _std(netinc, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

