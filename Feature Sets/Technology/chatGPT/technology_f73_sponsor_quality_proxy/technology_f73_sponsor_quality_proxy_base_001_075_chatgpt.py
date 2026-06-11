import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_mean_5d_base_v001_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _mean(series,5)
    return _clean(result)

# core01 mean 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_mean_21d_base_v002_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _mean(series,21)
    return _clean(result)

# core02 mean 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_mean_63d_base_v003_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _mean(series,63)
    return _clean(result)

# core03 mean 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_mean_126d_base_v004_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _mean(series,126)
    return _clean(result)

# core04 mean 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_mean_252d_base_v005_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _mean(series,252)
    return _clean(result)

# core05 mean 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_mean_5d_base_v006_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core06 mean 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_mean_21d_base_v007_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core07 mean 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_mean_63d_base_v008_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core08 mean 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_mean_126d_base_v009_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _mean(series,126)
    return _clean(result)

# core09 mean 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_mean_252d_base_v010_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _mean(series,252)
    return _clean(result)

# core00 z 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_z_21d_base_v011_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _z(series,21)
    return _clean(result)

# core01 z 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_z_63d_base_v012_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _z(series,63)
    return _clean(result)

# core02 z 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_z_126d_base_v013_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _z(series,126)
    return _clean(result)

# core03 z 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_z_252d_base_v014_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core04 z 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_z_5d_base_v015_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _z(series,5)
    return _clean(result)

# core05 z 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_z_21d_base_v016_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _z(series,21)
    return _clean(result)

# core06 z 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_z_63d_base_v017_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core07 z 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_z_126d_base_v018_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _z(series,126)
    return _clean(result)

# core08 z 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_z_252d_base_v019_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _z(series,252)
    return _clean(result)

# core09 z 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_z_5d_base_v020_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _z(series,5)
    return _clean(result)

# core00 rank 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_rank_63d_base_v021_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _rank(series,63)
    return _clean(result)

# core01 rank 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_rank_126d_base_v022_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _rank(series,126)
    return _clean(result)

# core02 rank 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_rank_252d_base_v023_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _rank(series,252)
    return _clean(result)

# core03 rank 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_rank_5d_base_v024_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _rank(series,5)
    return _clean(result)

# core04 rank 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_rank_21d_base_v025_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _rank(series,21)
    return _clean(result)

# core05 rank 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_rank_63d_base_v026_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _rank(series,63)
    return _clean(result)

# core06 rank 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_rank_126d_base_v027_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core07 rank 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_rank_252d_base_v028_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _rank(series,252)
    return _clean(result)

# core08 rank 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_rank_5d_base_v029_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _rank(series,5)
    return _clean(result)

# core09 rank 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_rank_21d_base_v030_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _rank(series,21)
    return _clean(result)

# core00 std 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_std_126d_base_v031_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _std(series,126)
    return _clean(result)

# core01 std 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_std_252d_base_v032_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _std(series,252)
    return _clean(result)

# core02 std 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_std_5d_base_v033_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _std(series,5)
    return _clean(result)

# core03 std 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_std_21d_base_v034_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _std(series,21)
    return _clean(result)

# core04 std 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_std_63d_base_v035_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core05 std 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_std_126d_base_v036_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _std(series,126)
    return _clean(result)

# core06 std 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_std_252d_base_v037_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _std(series,252)
    return _clean(result)

# core07 std 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_std_5d_base_v038_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _std(series,5)
    return _clean(result)

# core08 std 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_std_21d_base_v039_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _std(series,21)
    return _clean(result)

# core09 std 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_std_63d_base_v040_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core00 delta 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_delta_252d_base_v041_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _diff(series,252)
    return _clean(result)

# core01 delta 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_delta_5d_base_v042_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _diff(series,5)
    return _clean(result)

# core02 delta 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_delta_21d_base_v043_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _diff(series,21)
    return _clean(result)

# core03 delta 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_delta_63d_base_v044_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _diff(series,63)
    return _clean(result)

# core04 delta 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_delta_126d_base_v045_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _diff(series,126)
    return _clean(result)

# core05 delta 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_delta_252d_base_v046_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _diff(series,252)
    return _clean(result)

# core06 delta 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_delta_5d_base_v047_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _diff(series,5)
    return _clean(result)

# core07 delta 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_delta_21d_base_v048_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core08 delta 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_delta_63d_base_v049_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _diff(series,63)
    return _clean(result)

# core09 delta 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_delta_126d_base_v050_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _diff(series,126)
    return _clean(result)

# core00 pct 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_pct_5d_base_v051_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _pct_change(series,5)
    return _clean(result)

# core01 pct 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_pct_21d_base_v052_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _pct_change(series,21)
    return _clean(result)

# core02 pct 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_pct_63d_base_v053_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _pct_change(series,63)
    return _clean(result)

# core03 pct 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_pct_126d_base_v054_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _pct_change(series,126)
    return _clean(result)

# core04 pct 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_pct_252d_base_v055_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _pct_change(series,252)
    return _clean(result)

# core05 pct 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_pct_5d_base_v056_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _pct_change(series,5)
    return _clean(result)

# core06 pct 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_pct_21d_base_v057_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _pct_change(series,21)
    return _clean(result)

# core07 pct 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_pct_63d_base_v058_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _pct_change(series,63)
    return _clean(result)

# core08 pct 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_pct_126d_base_v059_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _pct_change(series,126)
    return _clean(result)

# core09 pct 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_pct_252d_base_v060_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _pct_change(series,252)
    return _clean(result)

# core00 ewm 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_ewm_21d_base_v061_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _ewm(series,21)
    return _clean(result)

# core01 ewm 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_ewm_63d_base_v062_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _ewm(series,63)
    return _clean(result)

# core02 ewm 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_ewm_126d_base_v063_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _ewm(series,126)
    return _clean(result)

# core03 ewm 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_ewm_252d_base_v064_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _ewm(series,252)
    return _clean(result)

# core04 ewm 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_ewm_5d_base_v065_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _ewm(series,5)
    return _clean(result)

# core05 ewm 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core05_ewm_21d_base_v066_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(mf_holders,inst_holders.abs()+1e-9)
    result = _ewm(series,21)
    return _clean(result)

# core06 ewm 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core06_ewm_63d_base_v067_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(pension_holders,inst_holders.abs()+1e-9)
    result = _ewm(series,63)
    return _clean(result)

# core07 ewm 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core07_ewm_126d_base_v068_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = -_safe_div(inst_top10_share,inst_share.abs()+1e-9)
    result = _ewm(series,126)
    return _clean(result)

# core08 ewm 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core08_ewm_252d_base_v069_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _corr(inst_holders,_pct_change(closeadj,21),252)
    result = _ewm(series,252)
    return _clean(result)

# core09 ewm 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core09_ewm_5d_base_v070_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_avg_position_size,63),_std(inst_avg_position_size,252).abs()+1e-9)
    result = _ewm(series,5)
    return _clean(result)

# core00 slope 63d
def cg_f73_technology_f73_sponsor_quality_proxy_core00_slope_63d_base_v071_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_holders
    result = _slope(series,63)
    return _clean(result)

# core01 slope 126d
def cg_f73_technology_f73_sponsor_quality_proxy_core01_slope_126d_base_v072_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_avg_position_size
    result = _slope(series,126)
    return _clean(result)

# core02 slope 252d
def cg_f73_technology_f73_sponsor_quality_proxy_core02_slope_252d_base_v073_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = inst_share
    result = _slope(series,252)
    return _clean(result)

# core03 slope 5d
def cg_f73_technology_f73_sponsor_quality_proxy_core03_slope_5d_base_v074_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(_diff(inst_value,63), _diff(inst_holders,63).abs()+1e-9)
    result = _slope(series,5)
    return _clean(result)

# core04 slope 21d
def cg_f73_technology_f73_sponsor_quality_proxy_core04_slope_21d_base_v075_signal(inst_holders, inst_value, inst_share, inst_avg_position_size, inst_top10_share, hf_holders, mf_holders, pension_holders, closeadj):
    series = _safe_div(hf_holders,inst_holders.abs()+1e-9)
    result = _slope(series,21)
    return _clean(result)

