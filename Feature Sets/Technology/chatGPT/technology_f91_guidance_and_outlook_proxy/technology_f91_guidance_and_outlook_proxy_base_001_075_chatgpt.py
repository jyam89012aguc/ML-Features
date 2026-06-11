import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_mean_5d_base_v001_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core01 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_mean_5d_base_v002_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core02 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_mean_5d_base_v003_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core03 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_mean_5d_base_v004_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core04 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_mean_5d_base_v005_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _mean(series,5)
    return _clean(result)

# core05 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_mean_5d_base_v006_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _mean(series,5)
    return _clean(result)

# core06 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_mean_5d_base_v007_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _mean(series,5)
    return _clean(result)

# core07 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_mean_5d_base_v008_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core08 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_mean_5d_base_v009_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _mean(series,5)
    return _clean(result)

# core09 mean_5d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_mean_5d_base_v010_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _mean(series,5)
    return _clean(result)

# core00 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_mean_21d_base_v011_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core01 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_mean_21d_base_v012_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core02 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_mean_21d_base_v013_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core03 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_mean_21d_base_v014_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core04 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_mean_21d_base_v015_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _mean(series,21)
    return _clean(result)

# core05 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_mean_21d_base_v016_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _mean(series,21)
    return _clean(result)

# core06 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_mean_21d_base_v017_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _mean(series,21)
    return _clean(result)

# core07 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_mean_21d_base_v018_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core08 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_mean_21d_base_v019_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _mean(series,21)
    return _clean(result)

# core09 mean_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_mean_21d_base_v020_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _mean(series,21)
    return _clean(result)

# core00 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_mean_63d_base_v021_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core01 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_mean_63d_base_v022_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core02 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_mean_63d_base_v023_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core03 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_mean_63d_base_v024_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core04 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_mean_63d_base_v025_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _mean(series,63) + 0.10*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core05 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_mean_63d_base_v026_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _mean(series,63)
    return _clean(result)

# core06 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_mean_63d_base_v027_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _mean(series,63)
    return _clean(result)

# core07 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_mean_63d_base_v028_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core08 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_mean_63d_base_v029_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _mean(series,63)
    return _clean(result)

# core09 mean_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_mean_63d_base_v030_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _mean(series,63)
    return _clean(result)

# core00 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_z_63d_base_v031_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core01 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_z_63d_base_v032_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core02 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_z_63d_base_v033_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core03 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_z_63d_base_v034_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core04 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_z_63d_base_v035_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _z(series,63)
    return _clean(result)

# core05 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_z_63d_base_v036_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _z(series,63)
    return _clean(result)

# core06 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_z_63d_base_v037_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _z(series,63)
    return _clean(result)

# core07 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_z_63d_base_v038_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core08 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_z_63d_base_v039_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _z(series,63)
    return _clean(result)

# core09 z_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_z_63d_base_v040_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _z(series,63)
    return _clean(result)

# core00 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_z_252d_base_v041_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core01 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_z_252d_base_v042_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core02 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_z_252d_base_v043_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core03 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_z_252d_base_v044_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core04 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_z_252d_base_v045_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _z(series,252)
    return _clean(result)

# core05 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_z_252d_base_v046_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _z(series,252)
    return _clean(result)

# core06 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_z_252d_base_v047_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _z(series,252)
    return _clean(result)

# core07 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_z_252d_base_v048_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core08 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_z_252d_base_v049_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _z(series,252)
    return _clean(result)

# core09 z_252d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_z_252d_base_v050_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _z(series,252)
    return _clean(result)

# core00 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_rank_126d_base_v051_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core01 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_rank_126d_base_v052_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core02 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_rank_126d_base_v053_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core03 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_rank_126d_base_v054_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core04 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_rank_126d_base_v055_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _rank(series,126)
    return _clean(result)

# core05 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_rank_126d_base_v056_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _rank(series,126)
    return _clean(result)

# core06 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_rank_126d_base_v057_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _rank(series,126)
    return _clean(result)

# core07 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_rank_126d_base_v058_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core08 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_rank_126d_base_v059_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _rank(series,126)
    return _clean(result)

# core09 rank_126d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_rank_126d_base_v060_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _rank(series,126)
    return _clean(result)

# core00 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_std_63d_base_v061_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core01 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_std_63d_base_v062_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core02 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_std_63d_base_v063_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core03 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_std_63d_base_v064_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core04 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_std_63d_base_v065_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _std(series,63) + 0.07*_rank(volume,126)
    return _clean(result)

# core05 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core05_std_63d_base_v066_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(eps_est,21),126)
    result = _std(series,63)
    return _clean(result)

# core06 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core06_std_63d_base_v067_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _corr(_pct_change(closeadj,21),_diff(rev_est,21),126)
    result = _std(series,63)
    return _clean(result)

# core07 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core07_std_63d_base_v068_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_pct_change(closeadj,63),_safe_div(eps_disp,eps_est.abs()+1e-9).abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core08 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core08_std_63d_base_v069_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(revenue,252),rev_est.abs()+1e-9)
    result = _std(series,63)
    return _clean(result)

# core09 std_63d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core09_std_63d_base_v070_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _event_rate(event_count,63)*_z(_pct_change(closeadj,21),126)+0.01*_z(volume,126)
    result = _std(series,63)
    return _clean(result)

# core00 delta_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core00_delta_21d_base_v071_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps-eps_est,eps_est.abs()+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core01 delta_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core01_delta_21d_base_v072_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(eps_est,63),eps_est.abs()+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core02 delta_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core02_delta_21d_base_v073_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(_diff(rev_est,63),rev_est.abs()+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core03 delta_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core03_delta_21d_base_v074_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(eps_disp,eps_est.abs()+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core04 delta_21d
def cg_f91_technology_f91_guidance_and_outlook_proxy_core04_delta_21d_base_v075_signal(eps, eps_est, eps_disp, rev_est, rev_disp, revenue, closeadj, volume, event_count):
    series = _safe_div(rev_disp,rev_est.abs()+1e-9) * (1.0 + 0.05*_z(_pct_change(closeadj,21),126))
    result = _diff(series,21)
    return _clean(result)

