
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(rnd, assets):
    return _safe_div(rnd, assets)

# 5d accel of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_accel_v001_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_accel_v002_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_accel_v003_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_accel_v004_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_accel_v005_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_accel_v006_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_accel_v007_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_accel_v008_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_accel_v009_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_accel_v010_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_accel_v011_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_accel_v012_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_accel_v013_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_accel_v014_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_accel_v015_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_accel_v016_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_accel_v017_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_accel_v018_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_accel_v019_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_accel_v020_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_accel_v021_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_accel_v022_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_accel_v023_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_accel_v024_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_accel_v025_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_accel_v026_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_accel_v027_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_accel_v028_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_accel_v029_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_accel_v030_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_accel_v031_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_accel_v032_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_accel_v033_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_accel_v034_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_accel_v035_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_accel_v036_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_accel_v037_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_accel_v038_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_accel_v039_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_accel_v040_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_accel_v041_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_accel_v042_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_accel_v043_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_accel_v044_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_accel_v045_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_accel_v046_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_accel_v047_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_accel_v048_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_accel_v049_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_accel_v050_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_accel_v051_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_accel_v052_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_accel_v053_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_accel_v054_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_accel_v055_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_accel_v056_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_accel_v057_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_accel_v058_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_accel_v059_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_accel_v060_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_accel_v061_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_accel_v062_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_accel_v063_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_accel_v064_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_accel_v065_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_accel_v066_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_accel_v067_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_accel_v068_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_accel_v069_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_accel_v070_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_accel_v071_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_accel_v072_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_accel_v073_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_accel_v074_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_accel_v075_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_accel_v076_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_accel_v077_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_accel_v078_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_accel_v079_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_accel_v080_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_accel_v081_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_accel_v082_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_accel_v083_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_accel_v084_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_accel_v085_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_accel_v086_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_accel_v087_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_accel_v088_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_accel_v089_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_accel_v090_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_accel_v091_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_accel_v092_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_accel_v093_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_accel_v094_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_accel_v095_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_accel_v096_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_accel_v097_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_accel_v098_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_accel_v099_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_accel_v100_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_accel_v101_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_accel_v102_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_accel_v103_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_accel_v104_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_accel_v105_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_accel_v106_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_accel_v107_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_accel_v108_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_accel_v109_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_accel_v110_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_accel_v111_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_accel_v112_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_accel_v113_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_accel_v114_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_accel_v115_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_accel_v116_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_accel_v117_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_accel_v118_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_accel_v119_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_accel_v120_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_accel_v121_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_accel_v122_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_accel_v123_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_accel_v124_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_accel_v125_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_accel_v126_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_accel_v127_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_accel_v128_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_accel_v129_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_accel_v130_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_accel_v131_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_accel_v132_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_accel_v133_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_accel_v134_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_accel_v135_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_accel_v136_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_accel_v137_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_accel_v138_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_accel_v139_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_accel_v140_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_accel_v141_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_accel_v142_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_accel_v143_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_accel_v144_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_accel_v145_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_accel_v146_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_accel_v147_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_accel_v148_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_accel_v149_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_accel_v150_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

