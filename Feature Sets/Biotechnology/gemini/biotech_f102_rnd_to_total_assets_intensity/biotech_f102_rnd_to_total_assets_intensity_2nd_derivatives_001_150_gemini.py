
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(rnd, assets):
    return _safe_div(rnd, assets)

# 5d slope of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_slope_v001_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_slope_v002_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_21d_slope_v003_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_slope_v004_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_slope_v005_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_63d_slope_v006_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_slope_v007_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_slope_v008_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_126d_slope_v009_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_slope_v010_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_slope_v011_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_252d_slope_v012_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_slope_v013_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_slope_v014_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_raw_504d_slope_v015_signal(rnd, assets):
    base = _mean(_get_metric(rnd, assets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_slope_v016_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_slope_v017_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_21d_slope_v018_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_slope_v019_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_slope_v020_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_63d_slope_v021_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_slope_v022_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_slope_v023_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_126d_slope_v024_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_slope_v025_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_slope_v026_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_252d_slope_v027_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_slope_v028_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_slope_v029_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_log_504d_slope_v030_signal(rnd, assets):
    base = _mean(_log(_get_metric(rnd, assets).abs()), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_slope_v031_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_slope_v032_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_21d_slope_v033_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_slope_v034_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_slope_v035_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_63d_slope_v036_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_slope_v037_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_slope_v038_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_126d_slope_v039_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_slope_v040_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_slope_v041_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_252d_slope_v042_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_slope_v043_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_slope_v044_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_z_504d_slope_v045_signal(rnd, assets):
    base = _z(_get_metric(rnd, assets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_slope_v046_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_slope_v047_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_21d_slope_v048_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_slope_v049_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_slope_v050_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_63d_slope_v051_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_slope_v052_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_slope_v053_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_126d_slope_v054_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_slope_v055_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_slope_v056_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_252d_slope_v057_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_slope_v058_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_slope_v059_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d pct rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_pct_504d_slope_v060_signal(rnd, assets):
    base = _pct_change(_get_metric(rnd, assets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_slope_v061_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_slope_v062_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_21d_slope_v063_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_slope_v064_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_slope_v065_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_63d_slope_v066_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_slope_v067_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_slope_v068_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_126d_slope_v069_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_slope_v070_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_slope_v071_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_252d_slope_v072_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_slope_v073_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_slope_v074_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ps_504d_slope_v075_signal(rnd, assets, sharesbas):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_slope_v076_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_slope_v077_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_21d_slope_v078_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_slope_v079_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_slope_v080_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_63d_slope_v081_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_slope_v082_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_slope_v083_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_126d_slope_v084_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_slope_v085_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_slope_v086_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_252d_slope_v087_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_slope_v088_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_slope_v089_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_asset_scaled_504d_slope_v090_signal(rnd, assets):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_slope_v091_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_slope_v092_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_21d_slope_v093_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_slope_v094_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_slope_v095_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_63d_slope_v096_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_slope_v097_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_slope_v098_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_126d_slope_v099_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_slope_v100_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_slope_v101_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_252d_slope_v102_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_slope_v103_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_slope_v104_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_mcap_scaled_504d_slope_v105_signal(rnd, assets, marketcap):
    base = _safe_div(_mean(_get_metric(rnd, assets), 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_slope_v106_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_slope_v107_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_21d_slope_v108_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_slope_v109_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_slope_v110_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_63d_slope_v111_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_slope_v112_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_slope_v113_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_126d_slope_v114_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_slope_v115_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_slope_v116_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_252d_slope_v117_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_slope_v118_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_slope_v119_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d rank rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_rank_504d_slope_v120_signal(rnd, assets):
    base = _rank(_get_metric(rnd, assets), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_slope_v121_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_slope_v122_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_21d_slope_v123_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=21).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_slope_v124_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_slope_v125_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_63d_slope_v126_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=63).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_slope_v127_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_slope_v128_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_126d_slope_v129_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=126).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_slope_v130_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_slope_v131_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_252d_slope_v132_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=252).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_slope_v133_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_slope_v134_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ewm rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_ewm_504d_slope_v135_signal(rnd, assets):
    base = _get_metric(rnd, assets).ewm(span=504).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_slope_v136_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_slope_v137_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_21d_slope_v138_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(21).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_slope_v139_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_slope_v140_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_63d_slope_v141_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(63).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_slope_v142_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_slope_v143_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_126d_slope_v144_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(126).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_slope_v145_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_slope_v146_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_252d_slope_v147_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(252).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_slope_v148_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_slope_v149_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d med rnd_intensity
def gm_f102_biotech_f102_rnd_to_total_assets_intensity_med_504d_slope_v150_signal(rnd, assets):
    base = _get_metric(rnd, assets).rolling(504).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

