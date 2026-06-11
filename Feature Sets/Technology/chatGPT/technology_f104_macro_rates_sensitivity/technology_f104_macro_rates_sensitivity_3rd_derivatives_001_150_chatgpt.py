import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_accel_v001_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_accel_v002_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_accel_v003_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_accel_v004_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_accel_v005_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_accel_v006_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_accel_v007_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_accel_v008_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_accel_v009_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_accel_v010_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_accel_v011_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_accel_v012_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_accel_v013_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_accel_v014_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_accel_v015_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_accel_v016_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_accel_v017_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_accel_v018_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_accel_v019_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_accel_v020_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_accel_v021_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_accel_v022_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_accel_v023_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_accel_v024_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_accel_v025_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_accel_v026_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_accel_v027_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_accel_v028_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_accel_v029_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_accel_v030_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_accel_v031_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_accel_v032_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_accel_v033_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_accel_v034_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_accel_v035_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_accel_v036_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_accel_v037_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_accel_v038_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_accel_v039_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_accel_v040_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_accel_v041_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_accel_v042_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_accel_v043_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_accel_v044_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_accel_v045_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_accel_v046_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_accel_v047_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_accel_v048_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_accel_v049_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_accel_v050_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_accel_v051_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_accel_v052_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_accel_v053_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_accel_v054_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_accel_v055_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_accel_v056_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_accel_v057_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_accel_v058_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_accel_v059_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_accel_v060_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_accel_v061_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_accel_v062_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_accel_v063_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_accel_v064_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_accel_v065_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_accel_v066_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_accel_v067_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_accel_v068_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_accel_v069_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_accel_v070_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_accel_v071_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_accel_v072_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_accel_v073_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_accel_v074_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_accel_v075_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_accel_v076_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_accel_v077_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_accel_v078_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_accel_v079_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_accel_v080_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_accel_v081_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_accel_v082_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_accel_v083_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_accel_v084_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_accel_v085_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_accel_v086_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_accel_v087_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_accel_v088_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_accel_v089_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_accel_v090_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_accel_v091_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_accel_v092_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_accel_v093_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_accel_v094_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_accel_v095_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_accel_v096_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_accel_v097_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_accel_v098_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_accel_v099_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_accel_v100_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_accel_v101_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_accel_v102_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_accel_v103_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_accel_v104_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_accel_v105_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_accel_v106_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_accel_v107_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_accel_v108_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_accel_v109_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_accel_v110_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_accel_v111_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_accel_v112_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_accel_v113_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_accel_v114_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_accel_v115_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_accel_v116_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_accel_v117_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_accel_v118_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_accel_v119_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_accel_v120_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_accel_v121_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core01 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_accel_v122_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core02 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_accel_v123_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core03 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_accel_v124_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core04 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_accel_v125_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_accel_v126_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core06 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_accel_v127_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core07 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_accel_v128_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core08 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_accel_v129_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core09 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_accel_v130_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_accel_v131_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core11 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_accel_v132_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core12 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_accel_v133_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core13 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_accel_v134_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core14 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_accel_v135_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core00 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_accel_v136_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core01 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_accel_v137_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core02 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_accel_v138_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core03 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_accel_v139_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core04 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_accel_v140_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core05 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_accel_v141_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core06 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_accel_v142_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core07 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_accel_v143_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core08 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_accel_v144_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core09 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_accel_v145_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

# core10 accel ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_accel_v146_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 5)
    d2 = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core11 accel ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_accel_v147_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 21)
    d2 = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    result = _diff(d2, 21)
    return _clean(result)

# core12 accel ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_accel_v148_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 63)
    d2 = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    result = _diff(d2, 5)
    return _clean(result)

# core13 accel ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_accel_v149_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 126)
    d2 = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    result = _diff(d2, 1)
    return _clean(result)

# core14 accel ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_accel_v150_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 252)
    d2 = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    result = _diff(d2, 63)
    return _clean(result)

