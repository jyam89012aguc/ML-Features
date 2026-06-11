import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_slope_v001_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_slope_v002_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_slope_v003_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_slope_v004_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_slope_v005_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_slope_v006_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_slope_v007_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_slope_v008_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_slope_v009_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_slope_v010_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_slope_v011_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_slope_v012_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_slope_v013_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_slope_v014_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_slope_v015_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_slope_v016_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_slope_v017_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_slope_v018_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_slope_v019_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_slope_v020_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(dxy, 5), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_slope_v021_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_slope_v022_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_slope_v023_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_slope_v024_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_slope_v025_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_slope_v026_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_slope_v027_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_slope_v028_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_slope_v029_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_slope_v030_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_slope_v031_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_slope_v032_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_slope_v033_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_slope_v034_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_slope_v035_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_slope_v036_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_slope_v037_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_slope_v038_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_slope_v039_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_slope_v040_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 5), _pct_change(sox, 5), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_slope_v041_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_slope_v042_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_slope_v043_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_slope_v044_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_slope_v045_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _diff(rate_10y, 21), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_slope_v046_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_slope_v047_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_slope_v048_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_slope_v049_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_slope_v050_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _corr(_pct_change(closeadj, 21), _pct_change(dxy, 21), 252)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_slope_v051_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_slope_v052_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_slope_v053_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_slope_v054_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_slope_v055_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(ixic, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_slope_v056_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_slope_v057_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_slope_v058_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_slope_v059_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_slope_v060_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(ixic, 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_mean_5d_slope_v061_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_mean_21d_slope_v062_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_mean_63d_slope_v063_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_mean_126d_slope_v064_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_mean_252d_slope_v065_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21) - _pct_change(sox, 21)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_mean_5d_slope_v066_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_mean_21d_slope_v067_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_mean_63d_slope_v068_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_mean_126d_slope_v069_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_mean_252d_slope_v070_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 63) - _pct_change(sox, 63)
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope mean 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_mean_5d_slope_v071_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope mean 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_mean_21d_slope_v072_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope mean 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_mean_63d_slope_v073_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope mean 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_mean_126d_slope_v074_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope mean 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_mean_252d_slope_v075_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta1y
    base = _mean(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_slope_v076_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_slope_v077_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_slope_v078_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_slope_v079_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_slope_v080_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_slope_v081_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_slope_v082_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_slope_v083_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_slope_v084_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_slope_v085_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_slope_v086_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_slope_v087_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_slope_v088_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_slope_v089_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_slope_v090_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_slope_v091_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_slope_v092_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_slope_v093_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_slope_v094_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_slope_v095_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_slope_v096_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_slope_v097_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_slope_v098_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_slope_v099_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_slope_v100_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_slope_v101_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_slope_v102_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_slope_v103_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_slope_v104_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_slope_v105_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_slope_v106_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_slope_v107_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_slope_v108_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_slope_v109_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_slope_v110_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_slope_v111_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_slope_v112_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_slope_v113_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_slope_v114_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_slope_v115_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_slope_v116_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_slope_v117_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_slope_v118_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_slope_v119_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_slope_v120_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_slope_v121_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_slope_v122_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_slope_v123_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_slope_v124_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_slope_v125_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_slope_v126_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_slope_v127_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_slope_v128_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_slope_v129_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_slope_v130_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_slope_v131_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_slope_v132_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_slope_v133_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_slope_v134_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_slope_v135_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core00 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_slope_v136_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core01 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_slope_v137_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core02 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_slope_v138_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core03 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_slope_v139_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core04 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_slope_v140_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core05 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_slope_v141_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core06 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_slope_v142_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core07 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_slope_v143_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core08 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_slope_v144_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core09 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_slope_v145_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

# core10 slope ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_slope_v146_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 5)
    result = _safe_div(_diff(base, 5), _std(base, 5).abs() + 1e-9)
    return _clean(result)

# core11 slope ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_slope_v147_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 21)
    result = _safe_div(_diff(base, 63), _std(base, 63).abs() + 1e-9)
    return _clean(result)

# core12 slope ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_slope_v148_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 63)
    result = _safe_div(_diff(base, 126), _std(base, 126).abs() + 1e-9)
    return _clean(result)

# core13 slope ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_slope_v149_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 126)
    result = _safe_div(_diff(base, 252), _std(base, 252).abs() + 1e-9)
    return _clean(result)

# core14 slope ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_slope_v150_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    base = _ewm(series, 252)
    result = _safe_div(_diff(base, 21), _std(base, 21).abs() + 1e-9)
    return _clean(result)

