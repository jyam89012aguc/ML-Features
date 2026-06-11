import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 slope mean 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_mean_5d_slope_v001_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core01 slope mean 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_mean_21d_slope_v002_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series,21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core02 slope mean 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_mean_63d_slope_v003_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _mean(series,63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope mean 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_mean_126d_slope_v004_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _mean(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core04 slope mean 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_mean_252d_slope_v005_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _mean(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core05 slope mean 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_mean_5d_slope_v006_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope mean 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_mean_21d_slope_v007_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core07 slope mean 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_mean_63d_slope_v008_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _mean(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core08 slope mean 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_mean_126d_slope_v009_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _mean(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope mean 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_mean_252d_slope_v010_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _mean(series,252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core00 slope z 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_z_21d_slope_v011_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _z(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope z 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_z_63d_slope_v012_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core02 slope z 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_z_126d_slope_v013_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _z(series,126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core03 slope z 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_z_252d_slope_v014_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope z 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_z_5d_slope_v015_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _z(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core05 slope z 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_z_21d_slope_v016_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _z(series,21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core06 slope z 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_z_63d_slope_v017_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _z(series,63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope z 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_z_126d_slope_v018_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _z(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core08 slope z 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_z_252d_slope_v019_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core09 slope z 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_z_5d_slope_v020_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _z(series,5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope rank 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_rank_63d_slope_v021_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _rank(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core01 slope rank 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_rank_126d_slope_v022_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _rank(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope rank 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_rank_252d_slope_v023_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _rank(series,252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core03 slope rank 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_rank_5d_slope_v024_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _rank(series,5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core04 slope rank 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_rank_21d_slope_v025_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _rank(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope rank 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_rank_63d_slope_v026_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _rank(series,63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core06 slope rank 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_rank_126d_slope_v027_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _rank(series,126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core07 slope rank 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_rank_252d_slope_v028_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _rank(series,252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope rank 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_rank_5d_slope_v029_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _rank(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core09 slope rank 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_rank_21d_slope_v030_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _rank(series,21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core00 slope std 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_std_126d_slope_v031_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _std(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core01 slope std 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_std_252d_slope_v032_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _std(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core02 slope std 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_std_5d_slope_v033_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _std(series,5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope std 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_std_21d_slope_v034_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _std(series,21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core04 slope std 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_std_63d_slope_v035_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core05 slope std 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_std_126d_slope_v036_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _std(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope std 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_std_252d_slope_v037_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _std(series,252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core07 slope std 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_std_5d_slope_v038_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _std(series,5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core08 slope std 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_std_21d_slope_v039_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _std(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope std 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_std_63d_slope_v040_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core00 slope delta 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_delta_252d_slope_v041_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _diff(series,252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope delta 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_delta_5d_slope_v042_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _diff(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core02 slope delta 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_delta_21d_slope_v043_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _diff(series,21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core03 slope delta 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_delta_63d_slope_v044_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _diff(series,63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope delta 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_delta_126d_slope_v045_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _diff(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core05 slope delta 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_delta_252d_slope_v046_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _diff(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core06 slope delta 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_delta_5d_slope_v047_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _diff(series,5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope delta 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_delta_21d_slope_v048_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core08 slope delta 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_delta_63d_slope_v049_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _diff(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core09 slope delta 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_delta_126d_slope_v050_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _diff(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope pct 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_pct_5d_slope_v051_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _pct_change(series,5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core01 slope pct 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_pct_21d_slope_v052_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope pct 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_pct_63d_slope_v053_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _pct_change(series,63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core03 slope pct 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_pct_126d_slope_v054_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _pct_change(series,126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core04 slope pct 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_pct_252d_slope_v055_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _pct_change(series,252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope pct 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_pct_5d_slope_v056_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _pct_change(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core06 slope pct 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_pct_21d_slope_v057_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core07 slope pct 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_pct_63d_slope_v058_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _pct_change(series,63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope pct 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_pct_126d_slope_v059_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _pct_change(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core09 slope pct 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_pct_252d_slope_v060_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _pct_change(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core00 slope ewm 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_ewm_21d_slope_v061_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _ewm(series,21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core01 slope ewm 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_ewm_63d_slope_v062_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _ewm(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core02 slope ewm 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_ewm_126d_slope_v063_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _ewm(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope ewm 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_ewm_252d_slope_v064_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _ewm(series,252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core04 slope ewm 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_ewm_5d_slope_v065_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _ewm(series,5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core05 slope ewm 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_ewm_21d_slope_v066_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _ewm(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope ewm 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_ewm_63d_slope_v067_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _ewm(series,63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core07 slope ewm 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_ewm_126d_slope_v068_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _ewm(series,126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core08 slope ewm 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_ewm_252d_slope_v069_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _ewm(series,252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope ewm 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_ewm_5d_slope_v070_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _ewm(series,5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core00 slope slope 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_slope_63d_slope_v071_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _slope(series,63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope slope 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_slope_126d_slope_v072_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _slope(series,126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core02 slope slope 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_slope_252d_slope_v073_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _slope(series,252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core03 slope slope 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_slope_5d_slope_v074_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _slope(series,5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope slope 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_slope_21d_slope_v075_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _slope(series,21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core05 slope slope 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_slope_63d_slope_v076_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core06 slope slope 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_slope_126d_slope_v077_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _slope(series,126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope slope 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_slope_252d_slope_v078_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _slope(series,252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core08 slope slope 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_slope_5d_slope_v079_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _slope(series,5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core09 slope slope 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_slope_21d_slope_v080_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _slope(series,21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope abs_mean 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_abs_mean_126d_slope_v081_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core01 slope abs_mean 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_abs_mean_252d_slope_v082_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope abs_mean 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_abs_mean_5d_slope_v083_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core03 slope abs_mean 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_abs_mean_21d_slope_v084_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core04 slope abs_mean 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_abs_mean_63d_slope_v085_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope abs_mean 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_abs_mean_126d_slope_v086_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _mean(series.abs(),126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core06 slope abs_mean 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_abs_mean_252d_slope_v087_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _mean(series.abs(),252)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core07 slope abs_mean 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_abs_mean_5d_slope_v088_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _mean(series.abs(),5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope abs_mean 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_abs_mean_21d_slope_v089_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _mean(series.abs(),21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core09 slope abs_mean 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_abs_mean_63d_slope_v090_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _mean(series.abs(),63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core00 slope pos_mag 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_pos_mag_252d_slope_v091_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series.where(series>0,0),252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core01 slope pos_mag 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_pos_mag_5d_slope_v092_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _mean(series.where(series>0,0),5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core02 slope pos_mag 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_pos_mag_21d_slope_v093_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _mean(series.where(series>0,0),21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope pos_mag 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_pos_mag_63d_slope_v094_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _mean(series.where(series>0,0),63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core04 slope pos_mag 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_pos_mag_126d_slope_v095_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _mean(series.where(series>0,0),126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core05 slope pos_mag 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_pos_mag_252d_slope_v096_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _mean(series.where(series>0,0),252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope pos_mag 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_pos_mag_5d_slope_v097_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _mean(series.where(series>0,0),5)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core07 slope pos_mag 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_pos_mag_21d_slope_v098_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _mean(series.where(series>0,0),21)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core08 slope pos_mag 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_pos_mag_63d_slope_v099_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _mean(series.where(series>0,0),63)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope pos_mag 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_pos_mag_126d_slope_v100_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _mean(series.where(series>0,0),126)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core00 slope neg_mag2 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_neg_mag2_5d_slope_v101_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _mean((series.where(series<0,0).abs() ** 2),5)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope neg_mag2 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_neg_mag2_21d_slope_v102_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _mean((series.where(series<0,0).abs() ** 2),21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core02 slope neg_mag2 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_neg_mag2_63d_slope_v103_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _mean((series.where(series<0,0).abs() ** 2),63)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core03 slope neg_mag2 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_neg_mag2_126d_slope_v104_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),126)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope neg_mag2 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_neg_mag2_252d_slope_v105_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),252)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core05 slope neg_mag2 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_neg_mag2_5d_slope_v106_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),5)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core06 slope neg_mag2 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_neg_mag2_21d_slope_v107_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _mean((series.where(series<0,0).abs() ** 2),21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope neg_mag2 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_neg_mag2_63d_slope_v108_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _mean((series.where(series<0,0).abs() ** 2),63)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core08 slope neg_mag2 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_neg_mag2_126d_slope_v109_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),126)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core09 slope neg_mag2 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_neg_mag2_252d_slope_v110_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _mean((series.where(series<0,0).abs() ** 2),252)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope vol_ratio 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_vol_ratio_21d_slope_v111_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_std(series,21), _mean(series.abs(),21)+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core01 slope vol_ratio 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_vol_ratio_63d_slope_v112_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_std(series,63), _mean(series.abs(),63)+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope vol_ratio 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_vol_ratio_126d_slope_v113_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_std(series,126), _mean(series.abs(),126)+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core03 slope vol_ratio 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_vol_ratio_252d_slope_v114_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _safe_div(_std(series,252), _mean(series.abs(),252)+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core04 slope vol_ratio 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_vol_ratio_5d_slope_v115_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(_std(series,5), _mean(series.abs(),5)+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope vol_ratio 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_vol_ratio_21d_slope_v116_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _safe_div(_std(series,21), _mean(series.abs(),21)+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core06 slope vol_ratio 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_vol_ratio_63d_slope_v117_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _safe_div(_std(series,63), _mean(series.abs(),63)+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core07 slope vol_ratio 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_vol_ratio_126d_slope_v118_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _safe_div(_std(series,126), _mean(series.abs(),126)+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope vol_ratio 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_vol_ratio_252d_slope_v119_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _safe_div(_std(series,252), _mean(series.abs(),252)+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core09 slope vol_ratio 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_vol_ratio_5d_slope_v120_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(_std(series,5), _mean(series.abs(),5)+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core00 slope recent_vs_long 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_recent_vs_long_63d_slope_v121_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_mean(series,63), _mean(series,126)+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core01 slope recent_vs_long 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_recent_vs_long_126d_slope_v122_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_mean(series,126), _mean(series,252)+1e-9)-1.0
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core02 slope recent_vs_long 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_recent_vs_long_252d_slope_v123_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _safe_div(_mean(series,252), _mean(series,504)+1e-9)-1.0
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope recent_vs_long 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_recent_vs_long_5d_slope_v124_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _safe_div(_mean(series,5), _mean(series,10)+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core04 slope recent_vs_long 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_recent_vs_long_21d_slope_v125_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,42)+1e-9)-1.0
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core05 slope recent_vs_long 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_recent_vs_long_63d_slope_v126_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _safe_div(_mean(series,63), _mean(series,126)+1e-9)-1.0
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope recent_vs_long 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_recent_vs_long_126d_slope_v127_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _safe_div(_mean(series,126), _mean(series,252)+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core07 slope recent_vs_long 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_recent_vs_long_252d_slope_v128_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _safe_div(_mean(series,252), _mean(series,504)+1e-9)-1.0
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core08 slope recent_vs_long 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_recent_vs_long_5d_slope_v129_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _safe_div(_mean(series,5), _mean(series,10)+1e-9)-1.0
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope recent_vs_long 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_recent_vs_long_21d_slope_v130_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,42)+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core00 slope accel 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_accel_126d_slope_v131_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _diff(_diff(series,42),42)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope accel 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_accel_252d_slope_v132_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _diff(_diff(series,84),84)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core02 slope accel 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_accel_5d_slope_v133_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _diff(_diff(series,1),1)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core03 slope accel 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_accel_21d_slope_v134_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _diff(_diff(series,7),7)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope accel 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_accel_63d_slope_v135_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _diff(_diff(series,21),21)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core05 slope accel 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_accel_126d_slope_v136_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _diff(_diff(series,42),42)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core06 slope accel 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_accel_252d_slope_v137_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _diff(_diff(series,84),84)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope accel 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_accel_5d_slope_v138_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _diff(_diff(series,1),1)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core08 slope accel 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_accel_21d_slope_v139_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _diff(_diff(series,7),7)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core09 slope accel 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_accel_63d_slope_v140_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _diff(_diff(series,21),21)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope centered_range 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core00_centered_range_252d_slope_v141_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(revenue,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(series-_mean(series,252), (_max(series,252)-_min(series,252)).abs()+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core01 slope centered_range 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core01_centered_range_5d_slope_v142_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = action_count*_pct_change(fcf,252)+0.001*_pct_change(closeadj,21)
    base = _safe_div(series-_mean(series,5), (_max(series,5)-_min(series,5)).abs()+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope centered_range 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core02_centered_range_21d_slope_v143_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = event_count*_diff(roic,63)+0.001*_pct_change(closeadj,21)
    base = _safe_div(series-_mean(series,21), (_max(series,21)-_min(series,21)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core03 slope centered_range 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core03_centered_range_63d_slope_v144_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(revenue,63),_event_count(action_count,252)+1e-9)
    base = _safe_div(series-_mean(series,63), (_max(series,63)-_min(series,63)).abs()+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core04 slope centered_range 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core04_centered_range_126d_slope_v145_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(fcf,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope centered_range 252d
def cg_f88_technology_f88_action_fundamental_followthrough_core05_centered_range_252d_slope_v146_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(roic,63),_event_count(action_count+event_count,252)+1e-9)
    base = _safe_div(series-_mean(series,252), (_max(series,252)-_min(series,252)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core06 slope centered_range 5d
def cg_f88_technology_f88_action_fundamental_followthrough_core06_centered_range_5d_slope_v147_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(action_count,_pct_change(revenue,63),252)
    base = _safe_div(series-_mean(series,5), (_max(series,5)-_min(series,5)).abs()+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

# core07 slope centered_range 21d
def cg_f88_technology_f88_action_fundamental_followthrough_core07_centered_range_21d_slope_v148_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _corr(event_count,_pct_change(fcf,63),252)
    base = _safe_div(series-_mean(series,21), (_max(series,21)-_min(series,21)).abs()+1e-9)
    result = _safe_div(_diff(base,63), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope centered_range 63d
def cg_f88_technology_f88_action_fundamental_followthrough_core08_centered_range_63d_slope_v149_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_pct_change(closeadj,126),_event_count(action_count,252)+1e-9)
    base = _safe_div(series-_mean(series,63), (_max(series,63)-_min(series,63)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,21).abs()+1e-9)
    return _clean(result)

# core09 slope centered_range 126d
def cg_f88_technology_f88_action_fundamental_followthrough_core09_centered_range_126d_slope_v150_signal(action_count, event_count, revenue, fcf, roic, sharesbas, closeadj):
    series = _safe_div(_diff(sharesbas,63),_event_count(event_count,252)+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,5), _std(base,5).abs()+1e-9)
    return _clean(result)

