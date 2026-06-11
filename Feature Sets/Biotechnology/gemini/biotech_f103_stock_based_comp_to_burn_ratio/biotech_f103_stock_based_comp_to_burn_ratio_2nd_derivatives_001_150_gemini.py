
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

# Metric implementation
def _get_metric(sbcomp, ncfo):
    return _safe_div(sbcomp, ncfo.abs())

# 5d slope of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_slope_v001_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_slope_v002_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_21d_slope_v003_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_slope_v004_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_slope_v005_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_63d_slope_v006_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_slope_v007_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_slope_v008_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_126d_slope_v009_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_slope_v010_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_slope_v011_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_252d_slope_v012_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_slope_v013_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_slope_v014_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d raw sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_raw_504d_slope_v015_signal(sbcomp, ncfo):
    base = _mean(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_slope_v016_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_slope_v017_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_21d_slope_v018_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_slope_v019_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_slope_v020_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_63d_slope_v021_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_slope_v022_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_slope_v023_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_126d_slope_v024_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_slope_v025_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_slope_v026_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_252d_slope_v027_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_slope_v028_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_slope_v029_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d log sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_log_504d_slope_v030_signal(sbcomp, ncfo):
    base = _mean(_log(_get_metric(sbcomp, ncfo).abs()), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_slope_v031_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_slope_v032_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_21d_slope_v033_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_slope_v034_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_slope_v035_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_63d_slope_v036_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_slope_v037_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_slope_v038_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_126d_slope_v039_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_slope_v040_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_slope_v041_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_252d_slope_v042_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_slope_v043_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_slope_v044_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_z_504d_slope_v045_signal(sbcomp, ncfo):
    base = _z(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_slope_v046_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_slope_v047_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_21d_slope_v048_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_slope_v049_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_slope_v050_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_63d_slope_v051_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_slope_v052_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_slope_v053_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_126d_slope_v054_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_slope_v055_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_slope_v056_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_252d_slope_v057_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_slope_v058_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_slope_v059_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d pct sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_pct_504d_slope_v060_signal(sbcomp, ncfo):
    base = _pct_change(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_slope_v061_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_slope_v062_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_21d_slope_v063_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_slope_v064_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_slope_v065_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_63d_slope_v066_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_slope_v067_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_slope_v068_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_126d_slope_v069_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_slope_v070_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_slope_v071_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_252d_slope_v072_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_slope_v073_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_slope_v074_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ps sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ps_504d_slope_v075_signal(sbcomp, ncfo, sharesbas):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), sharesbas)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_slope_v076_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_slope_v077_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_21d_slope_v078_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_slope_v079_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_slope_v080_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_63d_slope_v081_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_slope_v082_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_slope_v083_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_126d_slope_v084_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_slope_v085_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_slope_v086_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_252d_slope_v087_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_slope_v088_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_slope_v089_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d asset_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_asset_scaled_504d_slope_v090_signal(sbcomp, ncfo, assets):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), assets)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_slope_v091_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_slope_v092_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_21d_slope_v093_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 21), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_slope_v094_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_slope_v095_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_63d_slope_v096_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 63), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_slope_v097_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_slope_v098_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_126d_slope_v099_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 126), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_slope_v100_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_slope_v101_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_252d_slope_v102_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 252), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_slope_v103_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_slope_v104_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d mcap_scaled sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_mcap_scaled_504d_slope_v105_signal(sbcomp, ncfo, marketcap):
    base = _safe_div(_mean(_get_metric(sbcomp, ncfo), 504), marketcap)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_slope_v106_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_slope_v107_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_21d_slope_v108_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 21)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_slope_v109_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_slope_v110_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_63d_slope_v111_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_slope_v112_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_slope_v113_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_126d_slope_v114_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_slope_v115_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_slope_v116_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_252d_slope_v117_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_slope_v118_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_slope_v119_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d rank sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_rank_504d_slope_v120_signal(sbcomp, ncfo):
    base = _rank(_get_metric(sbcomp, ncfo), 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_slope_v121_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_slope_v122_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_21d_slope_v123_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=21).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_slope_v124_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_slope_v125_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_63d_slope_v126_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=63).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_slope_v127_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_slope_v128_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_126d_slope_v129_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=126).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_slope_v130_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_slope_v131_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_252d_slope_v132_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=252).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_slope_v133_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_slope_v134_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d ewm sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_ewm_504d_slope_v135_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).ewm(span=504).mean()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_slope_v136_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_slope_v137_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_21d_slope_v138_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(21).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_slope_v139_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_slope_v140_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_63d_slope_v141_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(63).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_slope_v142_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_slope_v143_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_126d_slope_v144_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(126).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_slope_v145_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_slope_v146_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_252d_slope_v147_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(252).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_slope_v148_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_slope_v149_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d med sbc_to_burn
def gm_f103_biotech_f103_stock_based_comp_to_burn_ratio_med_504d_slope_v150_signal(sbcomp, ncfo):
    base = _get_metric(sbcomp, ncfo).rolling(504).median()
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

