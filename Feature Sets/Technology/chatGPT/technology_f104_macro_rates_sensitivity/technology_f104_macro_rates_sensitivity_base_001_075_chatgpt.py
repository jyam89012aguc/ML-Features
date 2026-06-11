import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_base_v001_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_base_v002_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_base_v003_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_base_v004_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_base_v005_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_base_v006_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_base_v007_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_base_v008_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_base_v009_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_base_v010_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_base_v011_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_base_v012_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_base_v013_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_base_v014_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_base_v015_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_base_v016_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_base_v017_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_base_v018_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_base_v019_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_base_v020_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_base_v021_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_base_v022_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_base_v023_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_base_v024_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_base_v025_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_base_v026_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_base_v027_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_base_v028_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_base_v029_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_base_v030_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_base_v031_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_base_v032_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_base_v033_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_base_v034_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_base_v035_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_base_v036_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_base_v037_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_base_v038_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_base_v039_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_base_v040_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_base_v041_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_base_v042_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_base_v043_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_base_v044_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_base_v045_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_base_v046_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_base_v047_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_base_v048_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_base_v049_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_base_v050_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_base_v051_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_base_v052_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_base_v053_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_base_v054_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_base_v055_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_base_v056_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_base_v057_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_base_v058_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_base_v059_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_base_v060_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    result = _mean(series, 252)
    return _clean(result)

# core00 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_base_v061_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    result = _mean(series, 5)
    return _clean(result)

# core01 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_base_v062_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    result = _mean(series, 21)
    return _clean(result)

# core02 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_base_v063_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    result = _mean(series, 63)
    return _clean(result)

# core03 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_base_v064_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    result = _mean(series, 126)
    return _clean(result)

# core04 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_base_v065_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    result = _mean(series, 252)
    return _clean(result)

# core05 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_base_v066_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    result = _mean(series, 5)
    return _clean(result)

# core06 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_base_v067_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    result = _mean(series, 21)
    return _clean(result)

# core07 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_base_v068_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    result = _mean(series, 63)
    return _clean(result)

# core08 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_base_v069_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    result = _mean(series, 126)
    return _clean(result)

# core09 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_base_v070_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    result = _mean(series, 252)
    return _clean(result)

# core10 mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_base_v071_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    result = _mean(series, 5)
    return _clean(result)

# core11 mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_base_v072_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    result = _mean(series, 21)
    return _clean(result)

# core12 mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_base_v073_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    result = _mean(series, 63)
    return _clean(result)

# core13 mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_base_v074_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    result = _mean(series, 126)
    return _clean(result)

# core14 mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_base_v075_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    result = _mean(series, 252)
    return _clean(result)

