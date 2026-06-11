
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(taxassets, assets, marketcap):
    return _safe_div(taxassets, assets)

# 5d accel of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_accel_v001_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_accel_v002_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_21d_accel_v003_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_accel_v004_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_accel_v005_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_63d_accel_v006_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_accel_v007_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_accel_v008_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_126d_accel_v009_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_accel_v010_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_accel_v011_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_252d_accel_v012_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_accel_v013_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_accel_v014_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_raw_504d_accel_v015_signal(taxassets, assets, marketcap):
    base = _mean(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_accel_v016_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_accel_v017_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_21d_accel_v018_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_accel_v019_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_accel_v020_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_63d_accel_v021_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_accel_v022_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_accel_v023_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_126d_accel_v024_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_accel_v025_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_accel_v026_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_252d_accel_v027_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_accel_v028_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_accel_v029_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_log_504d_accel_v030_signal(taxassets, assets, marketcap):
    base = _mean(_log(_get_metric(taxassets, assets, marketcap).abs()), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_accel_v031_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_accel_v032_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_21d_accel_v033_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_accel_v034_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_accel_v035_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_63d_accel_v036_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_accel_v037_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_accel_v038_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_126d_accel_v039_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_accel_v040_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_accel_v041_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_252d_accel_v042_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_accel_v043_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_accel_v044_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_z_504d_accel_v045_signal(taxassets, assets, marketcap):
    base = _z(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_accel_v046_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_accel_v047_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_21d_accel_v048_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_accel_v049_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_accel_v050_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_63d_accel_v051_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_accel_v052_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_accel_v053_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_126d_accel_v054_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_accel_v055_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_accel_v056_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_252d_accel_v057_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_accel_v058_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_accel_v059_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d pct dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_pct_504d_accel_v060_signal(taxassets, assets, marketcap):
    base = _pct_change(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_accel_v061_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_accel_v062_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_21d_accel_v063_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_accel_v064_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_accel_v065_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_63d_accel_v066_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_accel_v067_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_accel_v068_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_126d_accel_v069_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_accel_v070_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_accel_v071_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_252d_accel_v072_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_accel_v073_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_accel_v074_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ps_504d_accel_v075_signal(taxassets, assets, marketcap, sharesbas):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_accel_v076_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_accel_v077_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_21d_accel_v078_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_accel_v079_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_accel_v080_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_63d_accel_v081_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_accel_v082_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_accel_v083_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_126d_accel_v084_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_accel_v085_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_accel_v086_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_252d_accel_v087_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_accel_v088_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_accel_v089_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_asset_scaled_504d_accel_v090_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_accel_v091_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_accel_v092_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_21d_accel_v093_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_accel_v094_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_accel_v095_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_63d_accel_v096_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_accel_v097_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_accel_v098_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_126d_accel_v099_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_accel_v100_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_accel_v101_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_252d_accel_v102_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_accel_v103_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_accel_v104_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_mcap_scaled_504d_accel_v105_signal(taxassets, assets, marketcap):
    base = _safe_div(_mean(_get_metric(taxassets, assets, marketcap), 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_accel_v106_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_accel_v107_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_21d_accel_v108_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_accel_v109_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_accel_v110_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_63d_accel_v111_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_accel_v112_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_accel_v113_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_126d_accel_v114_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_accel_v115_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_accel_v116_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_252d_accel_v117_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_accel_v118_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_accel_v119_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d rank dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_rank_504d_accel_v120_signal(taxassets, assets, marketcap):
    base = _rank(_get_metric(taxassets, assets, marketcap), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_accel_v121_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_accel_v122_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_21d_accel_v123_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=21).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_accel_v124_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_accel_v125_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_63d_accel_v126_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=63).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_accel_v127_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_accel_v128_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_126d_accel_v129_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=126).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_accel_v130_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_accel_v131_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_252d_accel_v132_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=252).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_accel_v133_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_accel_v134_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ewm dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_ewm_504d_accel_v135_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).ewm(span=504).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_accel_v136_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_accel_v137_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_21d_accel_v138_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(21).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_accel_v139_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_accel_v140_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_63d_accel_v141_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(63).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_accel_v142_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_accel_v143_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_126d_accel_v144_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(126).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_accel_v145_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_accel_v146_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_252d_accel_v147_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(252).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_accel_v148_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_accel_v149_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d med dta_to_valuation
def gm_f104_biotech_f104_deferred_tax_asset_to_valuation_med_504d_accel_v150_signal(taxassets, assets, marketcap):
    base = _get_metric(taxassets, assets, marketcap).rolling(504).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

