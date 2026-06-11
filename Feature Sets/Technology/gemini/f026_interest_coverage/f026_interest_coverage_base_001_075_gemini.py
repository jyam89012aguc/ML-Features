import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f026_interest_coverage_core00_mean_4q_v001_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(opinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core01_mean_4q_v002_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core02_mean_4q_v003_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core03_mean_4q_v004_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(fcf, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core04_mean_4q_v005_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(opinc + sbc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core05_mean_4q_v006_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(netinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core06_mean_4q_v007_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(revenue, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core07_mean_4q_v008_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core08_mean_4q_v009_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(debtt.abs(), intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core09_mean_4q_v010_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 4))

# core10-19: mean 8q
def cg_f026_interest_coverage_core10_mean_8q_v011_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(opinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core11_mean_8q_v012_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core12_mean_8q_v013_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core13_mean_8q_v014_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(fcf, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core14_mean_8q_v015_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(opinc + sbc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core15_mean_8q_v016_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(netinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core16_mean_8q_v017_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(revenue, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core17_mean_8q_v018_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core18_mean_8q_v019_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_safe_div(debtt.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core19_mean_8q_v020_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_mean(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 8))

# core20-29: z 8q
def cg_f026_interest_coverage_core20_z_8q_v021_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(opinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core21_z_8q_v022_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ebitda, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core22_z_8q_v023_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ncfo, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core23_z_8q_v024_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(fcf, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core24_z_8q_v025_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(opinc + sbc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core25_z_8q_v026_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(netinc, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core26_z_8q_v027_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(revenue, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core27_z_8q_v028_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core28_z_8q_v029_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(debtt.abs(), intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core29_z_8q_v030_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 8))

# core30-39: z 20q
def cg_f026_interest_coverage_core30_z_20q_v031_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(opinc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core31_z_20q_v032_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ebitda, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core32_z_20q_v033_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ncfo, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core33_z_20q_v034_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(fcf, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core34_z_20q_v035_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(opinc + sbc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core35_z_20q_v036_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(netinc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core36_z_20q_v037_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(revenue, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core37_z_20q_v038_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core38_z_20q_v039_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_safe_div(debtt.abs(), intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core39_z_20q_v040_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_z(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 20))

# core40-49: rank 12q
def cg_f026_interest_coverage_core40_rank_12q_v041_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(opinc, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core41_rank_12q_v042_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ebitda, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core42_rank_12q_v043_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ncfo, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core43_rank_12q_v044_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(fcf, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core44_rank_12q_v045_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(opinc + sbc, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core45_rank_12q_v046_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(netinc, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core46_rank_12q_v047_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(revenue, intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core47_rank_12q_v048_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core48_rank_12q_v049_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(debtt.abs(), intexp.abs() + 1.0), 12))
def cg_f026_interest_coverage_core49_rank_12q_v050_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 12))

# core50-59: rank 20q
def cg_f026_interest_coverage_core50_rank_20q_v051_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(opinc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core51_rank_20q_v052_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ebitda, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core52_rank_20q_v053_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ncfo, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core53_rank_20q_v054_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(fcf, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core54_rank_20q_v055_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(opinc + sbc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core55_rank_20q_v056_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(netinc, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core56_rank_20q_v057_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(revenue, intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core57_rank_20q_v058_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core58_rank_20q_v059_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_safe_div(debtt.abs(), intexp.abs() + 1.0), 20))
def cg_f026_interest_coverage_core59_rank_20q_v060_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_rank(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 20))

# core60-69: pct 1q
def cg_f026_interest_coverage_core60_pct_1q_v061_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(opinc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core61_pct_1q_v062_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ebitda, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core62_pct_1q_v063_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ncfo, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core63_pct_1q_v064_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(fcf, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core64_pct_1q_v065_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(opinc + sbc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core65_pct_1q_v066_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(netinc, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core66_pct_1q_v067_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(revenue, intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core67_pct_1q_v068_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ebitda - capex.abs(), intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core68_pct_1q_v069_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(debtt.abs(), intexp.abs() + 1.0), 1))
def cg_f026_interest_coverage_core69_pct_1q_v070_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_log(_safe_div(ebitda, intexp.abs() + 1.0).clip(lower=0.1)), 1))

# core70-74: pct 4q
def cg_f026_interest_coverage_core70_pct_4q_v071_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(opinc, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core71_pct_4q_v072_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ebitda, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core72_pct_4q_v073_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(ncfo, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core73_pct_4q_v074_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(fcf, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core74_pct_4q_v075_signal(opinc, intexp, ebitda, ncfo, fcf, sbc, netinc, revenue, debtt, debt, capex):
    return _clean(_pct_change(_safe_div(opinc + sbc, intexp.abs() + 1.0), 4))
