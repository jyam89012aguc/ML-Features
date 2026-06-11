
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 5d accel of 21d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_21d_accel_v001_signal(sbcomp):
    base = _mean(sbcomp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_21d_accel_v002_signal(sbcomp):
    base = _mean(sbcomp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_21d_accel_v003_signal(sbcomp):
    base = _mean(sbcomp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_63d_accel_v004_signal(sbcomp):
    base = _mean(sbcomp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_63d_accel_v005_signal(sbcomp):
    base = _mean(sbcomp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_63d_accel_v006_signal(sbcomp):
    base = _mean(sbcomp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_126d_accel_v007_signal(sbcomp):
    base = _mean(sbcomp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_126d_accel_v008_signal(sbcomp):
    base = _mean(sbcomp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_126d_accel_v009_signal(sbcomp):
    base = _mean(sbcomp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_252d_accel_v010_signal(sbcomp):
    base = _mean(sbcomp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_252d_accel_v011_signal(sbcomp):
    base = _mean(sbcomp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_252d_accel_v012_signal(sbcomp):
    base = _mean(sbcomp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_504d_accel_v013_signal(sbcomp):
    base = _mean(sbcomp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_504d_accel_v014_signal(sbcomp):
    base = _mean(sbcomp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_raw_504d_accel_v015_signal(sbcomp):
    base = _mean(sbcomp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_21d_accel_v016_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_21d_accel_v017_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_21d_accel_v018_signal(sbcomp):
    base = _mean(_log(sbcomp), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_63d_accel_v019_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_63d_accel_v020_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_63d_accel_v021_signal(sbcomp):
    base = _mean(_log(sbcomp), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_126d_accel_v022_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_126d_accel_v023_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_126d_accel_v024_signal(sbcomp):
    base = _mean(_log(sbcomp), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_252d_accel_v025_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_252d_accel_v026_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_252d_accel_v027_signal(sbcomp):
    base = _mean(_log(sbcomp), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_504d_accel_v028_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_504d_accel_v029_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_log_504d_accel_v030_signal(sbcomp):
    base = _mean(_log(sbcomp), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_21d_accel_v031_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_21d_accel_v032_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_21d_accel_v033_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_63d_accel_v034_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_63d_accel_v035_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_63d_accel_v036_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_126d_accel_v037_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_126d_accel_v038_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_126d_accel_v039_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_252d_accel_v040_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_252d_accel_v041_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_252d_accel_v042_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_504d_accel_v043_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_504d_accel_v044_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_z_504d_accel_v045_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_21d_accel_v046_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_21d_accel_v047_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_21d_accel_v048_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_63d_accel_v049_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_63d_accel_v050_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_63d_accel_v051_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_126d_accel_v052_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_126d_accel_v053_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_126d_accel_v054_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_252d_accel_v055_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_252d_accel_v056_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_252d_accel_v057_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_504d_accel_v058_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_504d_accel_v059_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_ps_504d_accel_v060_signal(sbcomp, sharesbas):
    base = _safe_div(_mean(sbcomp, 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_21d_accel_v061_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_21d_accel_v062_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_21d_accel_v063_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_63d_accel_v064_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_63d_accel_v065_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_63d_accel_v066_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_126d_accel_v067_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_126d_accel_v068_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_126d_accel_v069_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_252d_accel_v070_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_252d_accel_v071_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_252d_accel_v072_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_504d_accel_v073_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_504d_accel_v074_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_asset_scaled_504d_accel_v075_signal(sbcomp, assets):
    base = _safe_div(_mean(sbcomp, 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_21d_accel_v076_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_21d_accel_v077_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_21d_accel_v078_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_63d_accel_v079_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_63d_accel_v080_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_63d_accel_v081_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_126d_accel_v082_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_126d_accel_v083_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_126d_accel_v084_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_252d_accel_v085_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_252d_accel_v086_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_252d_accel_v087_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_504d_accel_v088_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_504d_accel_v089_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mcap_scaled_504d_accel_v090_signal(sbcomp, marketcap):
    base = _safe_div(_mean(sbcomp, 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_21d_accel_v091_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_21d_accel_v092_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_21d_accel_v093_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(21).min(), sbcomp.rolling(21).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_63d_accel_v094_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_63d_accel_v095_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_63d_accel_v096_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(63).min(), sbcomp.rolling(63).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_126d_accel_v097_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_126d_accel_v098_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_126d_accel_v099_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(126).min(), sbcomp.rolling(126).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_252d_accel_v100_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_252d_accel_v101_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_252d_accel_v102_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(252).min(), sbcomp.rolling(252).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_504d_accel_v103_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_504d_accel_v104_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_low sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_low_504d_accel_v105_signal(sbcomp):
    base = _safe_div(sbcomp - sbcomp.rolling(504).min(), sbcomp.rolling(504).min())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_21d_accel_v106_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_21d_accel_v107_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_21d_accel_v108_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(21).max() - sbcomp, sbcomp.rolling(21).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_63d_accel_v109_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_63d_accel_v110_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_63d_accel_v111_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(63).max() - sbcomp, sbcomp.rolling(63).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_126d_accel_v112_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_126d_accel_v113_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_126d_accel_v114_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(126).max() - sbcomp, sbcomp.rolling(126).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_252d_accel_v115_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_252d_accel_v116_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_252d_accel_v117_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(252).max() - sbcomp, sbcomp.rolling(252).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_504d_accel_v118_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_504d_accel_v119_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d dist_high sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_dist_high_504d_accel_v120_signal(sbcomp):
    base = _safe_div(sbcomp.rolling(504).max() - sbcomp, sbcomp.rolling(504).max())
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_21d_accel_v121_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_21d_accel_v122_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_21d_accel_v123_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 21) - _mean(sbcomp, 42), _mean(sbcomp, 42))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_63d_accel_v124_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_63d_accel_v125_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_63d_accel_v126_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 63) - _mean(sbcomp, 126), _mean(sbcomp, 126))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_126d_accel_v127_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_126d_accel_v128_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_126d_accel_v129_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 126) - _mean(sbcomp, 252), _mean(sbcomp, 252))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_252d_accel_v130_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_252d_accel_v131_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_252d_accel_v132_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 252) - _mean(sbcomp, 504), _mean(sbcomp, 504))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_504d_accel_v133_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_504d_accel_v134_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mom sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_mom_504d_accel_v135_signal(sbcomp):
    base = _safe_div(_mean(sbcomp, 504) - _mean(sbcomp, 1008), _mean(sbcomp, 1008))
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_21d_accel_v136_signal(sbcomp):
    base = _std(sbcomp, 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_21d_accel_v137_signal(sbcomp):
    base = _std(sbcomp, 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_21d_accel_v138_signal(sbcomp):
    base = _std(sbcomp, 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_63d_accel_v139_signal(sbcomp):
    base = _std(sbcomp, 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_63d_accel_v140_signal(sbcomp):
    base = _std(sbcomp, 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_63d_accel_v141_signal(sbcomp):
    base = _std(sbcomp, 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_126d_accel_v142_signal(sbcomp):
    base = _std(sbcomp, 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_126d_accel_v143_signal(sbcomp):
    base = _std(sbcomp, 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_126d_accel_v144_signal(sbcomp):
    base = _std(sbcomp, 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_252d_accel_v145_signal(sbcomp):
    base = _std(sbcomp, 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_252d_accel_v146_signal(sbcomp):
    base = _std(sbcomp, 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_252d_accel_v147_signal(sbcomp):
    base = _std(sbcomp, 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_504d_accel_v148_signal(sbcomp):
    base = _std(sbcomp, 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_504d_accel_v149_signal(sbcomp):
    base = _std(sbcomp, 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d vol sbcomp
def gm_f31_biotech_f31_sbc_to_revenue_intensity_vol_504d_accel_v150_signal(sbcomp):
    base = _std(sbcomp, 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

