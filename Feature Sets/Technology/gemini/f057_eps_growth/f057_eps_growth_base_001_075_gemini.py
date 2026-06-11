import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f057_eps_growth_core00_mean_4q_v001_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 4), 4))
def cg_f057_eps_growth_core01_mean_4q_v002_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 4), 4))
def cg_f057_eps_growth_core02_mean_4q_v003_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(eps, 4), 4))
def cg_f057_eps_growth_core03_mean_4q_v004_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(epsdil, 4), 4))
def cg_f057_eps_growth_core04_mean_4q_v005_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 1), 4))
def cg_f057_eps_growth_core05_mean_4q_v006_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 1), 4))
def cg_f057_eps_growth_core06_mean_4q_v007_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 4) - _pct_change(revenue, 4), 4))
def cg_f057_eps_growth_core07_mean_4q_v008_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 4))
def cg_f057_eps_growth_core08_mean_4q_v009_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(_pct_change(eps, 4), 1), 4))
def cg_f057_eps_growth_core09_mean_4q_v010_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(_pct_change(epsdil, 4), 1), 4))

# core10-19: mean 8q
def cg_f057_eps_growth_core10_mean_8q_v011_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 4), 8))
def cg_f057_eps_growth_core11_mean_8q_v012_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 4), 8))
def cg_f057_eps_growth_core12_mean_8q_v013_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(eps, 4), 8))
def cg_f057_eps_growth_core13_mean_8q_v014_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(epsdil, 4), 8))
def cg_f057_eps_growth_core14_mean_8q_v015_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 1), 8))
def cg_f057_eps_growth_core15_mean_8q_v016_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 1), 8))
def cg_f057_eps_growth_core16_mean_8q_v017_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(eps, 4) - _pct_change(revenue, 4), 8))
def cg_f057_eps_growth_core17_mean_8q_v018_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 8))
def cg_f057_eps_growth_core18_mean_8q_v019_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(_pct_change(eps, 4), 1), 8))
def cg_f057_eps_growth_core19_mean_8q_v020_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_mean(_diff(_pct_change(epsdil, 4), 1), 8))

# core20-29: z 8q
def cg_f057_eps_growth_core20_z_8q_v021_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 4), 8))
def cg_f057_eps_growth_core21_z_8q_v022_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 4), 8))
def cg_f057_eps_growth_core22_z_8q_v023_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(eps, 4), 8))
def cg_f057_eps_growth_core23_z_8q_v024_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(epsdil, 4), 8))
def cg_f057_eps_growth_core24_z_8q_v025_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 1), 8))
def cg_f057_eps_growth_core25_z_8q_v026_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 1), 8))
def cg_f057_eps_growth_core26_z_8q_v027_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 4) - _pct_change(revenue, 4), 8))
def cg_f057_eps_growth_core27_z_8q_v028_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 8))
def cg_f057_eps_growth_core28_z_8q_v029_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(_pct_change(eps, 4), 1), 8))
def cg_f057_eps_growth_core29_z_8q_v030_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(_pct_change(epsdil, 4), 1), 8))

# core30-39: z 20q
def cg_f057_eps_growth_core30_z_20q_v031_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 4), 20))
def cg_f057_eps_growth_core31_z_20q_v032_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 4), 20))
def cg_f057_eps_growth_core32_z_20q_v033_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(eps, 4), 20))
def cg_f057_eps_growth_core33_z_20q_v034_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(epsdil, 4), 20))
def cg_f057_eps_growth_core34_z_20q_v035_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 1), 20))
def cg_f057_eps_growth_core35_z_20q_v036_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 1), 20))
def cg_f057_eps_growth_core36_z_20q_v037_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(eps, 4) - _pct_change(revenue, 4), 20))
def cg_f057_eps_growth_core37_z_20q_v038_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 20))
def cg_f057_eps_growth_core38_z_20q_v039_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(_pct_change(eps, 4), 1), 20))
def cg_f057_eps_growth_core39_z_20q_v040_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_z(_diff(_pct_change(epsdil, 4), 1), 20))

# core40-49: rank 12q
def cg_f057_eps_growth_core40_rank_12q_v041_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 4), 12))
def cg_f057_eps_growth_core41_rank_12q_v042_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 4), 12))
def cg_f057_eps_growth_core42_rank_12q_v043_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(eps, 4), 12))
def cg_f057_eps_growth_core43_rank_12q_v044_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(epsdil, 4), 12))
def cg_f057_eps_growth_core44_rank_12q_v045_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 1), 12))
def cg_f057_eps_growth_core45_rank_12q_v046_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 1), 12))
def cg_f057_eps_growth_core46_rank_12q_v047_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 4) - _pct_change(revenue, 4), 12))
def cg_f057_eps_growth_core47_rank_12q_v048_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 12))
def cg_f057_eps_growth_core48_rank_12q_v049_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(_pct_change(eps, 4), 1), 12))
def cg_f057_eps_growth_core49_rank_12q_v050_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(_pct_change(epsdil, 4), 1), 12))

# core50-59: rank 20q
def cg_f057_eps_growth_core50_rank_20q_v051_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 4), 20))
def cg_f057_eps_growth_core51_rank_20q_v052_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 4), 20))
def cg_f057_eps_growth_core52_rank_20q_v053_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(eps, 4), 20))
def cg_f057_eps_growth_core53_rank_20q_v054_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(epsdil, 4), 20))
def cg_f057_eps_growth_core54_rank_20q_v055_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 1), 20))
def cg_f057_eps_growth_core55_rank_20q_v056_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 1), 20))
def cg_f057_eps_growth_core56_rank_20q_v057_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(eps, 4) - _pct_change(revenue, 4), 20))
def cg_f057_eps_growth_core57_rank_20q_v058_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 20))
def cg_f057_eps_growth_core58_rank_20q_v059_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(_pct_change(eps, 4), 1), 20))
def cg_f057_eps_growth_core59_rank_20q_v060_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_rank(_diff(_pct_change(epsdil, 4), 1), 20))

# core60-69: pct 1q
def cg_f057_eps_growth_core60_pct_1q_v061_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(eps, 4), 1))
def cg_f057_eps_growth_core61_pct_1q_v062_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(epsdil, 4), 1))
def cg_f057_eps_growth_core62_pct_1q_v063_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(eps, 4), 1))
def cg_f057_eps_growth_core63_pct_1q_v064_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(epsdil, 4), 1))
def cg_f057_eps_growth_core64_pct_1q_v065_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(eps, 1), 1))
def cg_f057_eps_growth_core65_pct_1q_v066_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(epsdil, 1), 1))
def cg_f057_eps_growth_core66_pct_1q_v067_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(eps, 4) - _pct_change(revenue, 4), 1))
def cg_f057_eps_growth_core67_pct_1q_v068_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(epsdil, 4) - _pct_change(opinc, 4), 1))
def cg_f057_eps_growth_core68_pct_1q_v069_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(_pct_change(eps, 4), 1), 1))
def cg_f057_eps_growth_core69_pct_1q_v070_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(_pct_change(epsdil, 4), 1), 1))

# core70-74: pct 4q
def cg_f057_eps_growth_core70_pct_4q_v071_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(eps, 4), 4))
def cg_f057_eps_growth_core71_pct_4q_v072_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(epsdil, 4), 4))
def cg_f057_eps_growth_core72_pct_4q_v073_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(eps, 4), 4))
def cg_f057_eps_growth_core73_pct_4q_v074_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_diff(epsdil, 4), 4))
def cg_f057_eps_growth_core74_pct_4q_v075_signal(eps, epsdil, netinc, opinc, revenue, ebitda, assets, marketcap):
    return _clean(_pct_change(_pct_change(eps, 4) - _pct_change(revenue, 4), 4))
