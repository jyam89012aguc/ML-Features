
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(taxassets, assets, marketcap):
    return _safe_div(taxassets, assets)

# 5d slope of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_slope_v001_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_slope_v002_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_slope_v003_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_slope_v004_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_slope_v005_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_slope_v006_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_slope_v007_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_slope_v008_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_slope_v009_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_slope_v010_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_slope_v011_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_slope_v012_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_slope_v013_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_slope_v014_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_slope_v015_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_slope_v016_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_slope_v017_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_slope_v018_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_slope_v019_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_slope_v020_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_slope_v021_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_slope_v022_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_slope_v023_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_slope_v024_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_slope_v025_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_slope_v026_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_slope_v027_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_slope_v028_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_slope_v029_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_slope_v030_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_slope_v031_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_slope_v032_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_slope_v033_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_slope_v034_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_slope_v035_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_slope_v036_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_slope_v037_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_slope_v038_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_slope_v039_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_slope_v040_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_slope_v041_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_slope_v042_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_slope_v043_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_slope_v044_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_slope_v045_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_slope_v046_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_slope_v047_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_slope_v048_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_slope_v049_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_slope_v050_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_slope_v051_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_slope_v052_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_slope_v053_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_slope_v054_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_slope_v055_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_slope_v056_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_slope_v057_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_slope_v058_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_slope_v059_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_slope_v060_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_slope_v061_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_slope_v062_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_slope_v063_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_slope_v064_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_slope_v065_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_slope_v066_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_slope_v067_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_slope_v068_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_slope_v069_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_slope_v070_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_slope_v071_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_slope_v072_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_slope_v073_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_slope_v074_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_slope_v075_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_slope_v076_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_slope_v077_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_slope_v078_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_slope_v079_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_slope_v080_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_slope_v081_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_slope_v082_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_slope_v083_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_slope_v084_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_slope_v085_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_slope_v086_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_slope_v087_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_slope_v088_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_slope_v089_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_slope_v090_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_slope_v091_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_slope_v092_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_slope_v093_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_slope_v094_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_slope_v095_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_slope_v096_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_slope_v097_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_slope_v098_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_slope_v099_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_slope_v100_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_slope_v101_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_slope_v102_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_slope_v103_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_slope_v104_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_slope_v105_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_slope_v106_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_slope_v107_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_slope_v108_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_slope_v109_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_slope_v110_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_slope_v111_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_slope_v112_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_slope_v113_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_slope_v114_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_slope_v115_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_slope_v116_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_slope_v117_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_slope_v118_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_slope_v119_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_slope_v120_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_slope_v121_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_slope_v122_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_slope_v123_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_slope_v124_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_slope_v125_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_slope_v126_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_slope_v127_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_slope_v128_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_slope_v129_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_slope_v130_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_slope_v131_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_slope_v132_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_slope_v133_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_slope_v134_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_slope_v135_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_slope_v136_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_slope_v137_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_slope_v138_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_slope_v139_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_slope_v140_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_slope_v141_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_slope_v142_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_slope_v143_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_slope_v144_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_slope_v145_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_slope_v146_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_slope_v147_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_slope_v148_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_slope_v149_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_slope_v150_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

