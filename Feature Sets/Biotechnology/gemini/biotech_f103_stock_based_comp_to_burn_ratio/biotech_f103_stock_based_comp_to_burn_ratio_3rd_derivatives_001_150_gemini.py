
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(sbcomp, ncfo):
    return _safe_div(sbcomp, ncfo.abs())

# 5d accel of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_accel_v001_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_accel_v002_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_accel_v003_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_accel_v004_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_accel_v005_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_accel_v006_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_accel_v007_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_accel_v008_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_accel_v009_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_accel_v010_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_accel_v011_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_accel_v012_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_accel_v013_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_accel_v014_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_accel_v015_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_accel_v016_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_accel_v017_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_accel_v018_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_accel_v019_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_accel_v020_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_accel_v021_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_accel_v022_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_accel_v023_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_accel_v024_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_accel_v025_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_accel_v026_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_accel_v027_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_accel_v028_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_accel_v029_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_accel_v030_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_accel_v031_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_accel_v032_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_accel_v033_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_accel_v034_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_accel_v035_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_accel_v036_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_accel_v037_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_accel_v038_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_accel_v039_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_accel_v040_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_accel_v041_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_accel_v042_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_accel_v043_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_accel_v044_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_accel_v045_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_accel_v046_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_accel_v047_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_accel_v048_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_accel_v049_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_accel_v050_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_accel_v051_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_accel_v052_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_accel_v053_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_accel_v054_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_accel_v055_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_accel_v056_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_accel_v057_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_accel_v058_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_accel_v059_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_accel_v060_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_accel_v061_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_accel_v062_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_accel_v063_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_accel_v064_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_accel_v065_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_accel_v066_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_accel_v067_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_accel_v068_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_accel_v069_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_accel_v070_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_accel_v071_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_accel_v072_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_accel_v073_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_accel_v074_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_accel_v075_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_accel_v076_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_accel_v077_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_accel_v078_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_accel_v079_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_accel_v080_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_accel_v081_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_accel_v082_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_accel_v083_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_accel_v084_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_accel_v085_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_accel_v086_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_accel_v087_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_accel_v088_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_accel_v089_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_accel_v090_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_accel_v091_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_accel_v092_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_accel_v093_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_accel_v094_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_accel_v095_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_accel_v096_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_accel_v097_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_accel_v098_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_accel_v099_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_accel_v100_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_accel_v101_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_accel_v102_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_accel_v103_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_accel_v104_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_accel_v105_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_accel_v106_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_accel_v107_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_accel_v108_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_accel_v109_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_accel_v110_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_accel_v111_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_accel_v112_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_accel_v113_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_accel_v114_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_accel_v115_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_accel_v116_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_accel_v117_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_accel_v118_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_accel_v119_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_accel_v120_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_accel_v121_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_accel_v122_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_accel_v123_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_accel_v124_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_accel_v125_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_accel_v126_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_accel_v127_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_accel_v128_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_accel_v129_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_accel_v130_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_accel_v131_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_accel_v132_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_accel_v133_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_accel_v134_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_accel_v135_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_accel_v136_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_accel_v137_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_accel_v138_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_accel_v139_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_accel_v140_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_accel_v141_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_accel_v142_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_accel_v143_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_accel_v144_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_accel_v145_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_accel_v146_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_accel_v147_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d accel of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_accel_v148_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    slope = _slope(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_accel_v149_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    slope = _slope(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_accel_v150_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    slope = _slope(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)

