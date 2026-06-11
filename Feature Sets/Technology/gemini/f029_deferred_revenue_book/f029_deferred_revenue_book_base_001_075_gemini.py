import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f029_deferred_revenue_book_core00_mean_4q_v001_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, revenue), 4))
def cg_f029_deferred_revenue_book_core01_mean_4q_v002_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core02_mean_4q_v003_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, assets), 4))
def cg_f029_deferred_revenue_book_core03_mean_4q_v004_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, marketcap), 4))
def cg_f029_deferred_revenue_book_core04_mean_4q_v005_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, sharesbas), 4))
def cg_f029_deferred_revenue_book_core05_mean_4q_v006_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(revenue + _diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core06_mean_4q_v007_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, opex.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core07_mean_4q_v008_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, fcf.abs() + 1.0), 4))
def cg_f029_deferred_revenue_book_core08_mean_4q_v009_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(deferredrev, 4))
def cg_f029_deferred_revenue_book_core09_mean_4q_v010_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_log(deferredrev.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f029_deferred_revenue_book_core10_mean_8q_v011_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, revenue), 8))
def cg_f029_deferred_revenue_book_core11_mean_8q_v012_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core12_mean_8q_v013_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, assets), 8))
def cg_f029_deferred_revenue_book_core13_mean_8q_v014_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, marketcap), 8))
def cg_f029_deferred_revenue_book_core14_mean_8q_v015_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, sharesbas), 8))
def cg_f029_deferred_revenue_book_core15_mean_8q_v016_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(revenue + _diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core16_mean_8q_v017_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, opex.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core17_mean_8q_v018_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_safe_div(deferredrev, fcf.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core18_mean_8q_v019_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(deferredrev, 8))
def cg_f029_deferred_revenue_book_core19_mean_8q_v020_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_mean(_log(deferredrev.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f029_deferred_revenue_book_core20_z_8q_v021_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, revenue), 8))
def cg_f029_deferred_revenue_book_core21_z_8q_v022_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(_diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core22_z_8q_v023_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, assets), 8))
def cg_f029_deferred_revenue_book_core23_z_8q_v024_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, marketcap), 8))
def cg_f029_deferred_revenue_book_core24_z_8q_v025_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, sharesbas), 8))
def cg_f029_deferred_revenue_book_core25_z_8q_v026_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(revenue + _diff(deferredrev, 4), revenue), 8))
def cg_f029_deferred_revenue_book_core26_z_8q_v027_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, opex.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core27_z_8q_v028_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, fcf.abs() + 1.0), 8))
def cg_f029_deferred_revenue_book_core28_z_8q_v029_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(deferredrev, 8))
def cg_f029_deferred_revenue_book_core29_z_8q_v030_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_log(deferredrev.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f029_deferred_revenue_book_core30_z_20q_v031_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, revenue), 20))
def cg_f029_deferred_revenue_book_core31_z_20q_v032_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(_diff(deferredrev, 4), revenue), 20))
def cg_f029_deferred_revenue_book_core32_z_20q_v033_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, assets), 20))
def cg_f029_deferred_revenue_book_core33_z_20q_v034_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, marketcap), 20))
def cg_f029_deferred_revenue_book_core34_z_20q_v035_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, sharesbas), 20))
def cg_f029_deferred_revenue_book_core35_z_20q_v036_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(revenue + _diff(deferredrev, 4), revenue), 20))
def cg_f029_deferred_revenue_book_core36_z_20q_v037_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, opex.abs() + 1.0), 20))
def cg_f029_deferred_revenue_book_core37_z_20q_v038_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_safe_div(deferredrev, fcf.abs() + 1.0), 20))
def cg_f029_deferred_revenue_book_core38_z_20q_v039_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(deferredrev, 20))
def cg_f029_deferred_revenue_book_core39_z_20q_v040_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_z(_log(deferredrev.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f029_deferred_revenue_book_core40_rank_12q_v041_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, revenue), 12))
def cg_f029_deferred_revenue_book_core41_rank_12q_v042_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(_diff(deferredrev, 4), revenue), 12))
def cg_f029_deferred_revenue_book_core42_rank_12q_v043_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, assets), 12))
def cg_f029_deferred_revenue_book_core43_rank_12q_v044_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, marketcap), 12))
def cg_f029_deferred_revenue_book_core44_rank_12q_v045_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, sharesbas), 12))
def cg_f029_deferred_revenue_book_core45_rank_12q_v046_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(revenue + _diff(deferredrev, 4), revenue), 12))
def cg_f029_deferred_revenue_book_core46_rank_12q_v047_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, opex.abs() + 1.0), 12))
def cg_f029_deferred_revenue_book_core47_rank_12q_v048_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, fcf.abs() + 1.0), 12))
def cg_f029_deferred_revenue_book_core48_rank_12q_v049_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(deferredrev, 12))
def cg_f029_deferred_revenue_book_core49_rank_12q_v050_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_log(deferredrev.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f029_deferred_revenue_book_core50_rank_20q_v051_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, revenue), 20))
def cg_f029_deferred_revenue_book_core51_rank_20q_v052_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(_diff(deferredrev, 4), revenue), 20))
def cg_f029_deferred_revenue_book_core52_rank_20q_v053_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, assets), 20))
def cg_f029_deferred_revenue_book_core53_rank_20q_v054_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, marketcap), 20))
def cg_f029_deferred_revenue_book_core54_rank_20q_v055_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, sharesbas), 20))
def cg_f029_deferred_revenue_book_core55_rank_20q_v056_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(revenue + _diff(deferredrev, 4), revenue), 20))
def cg_f029_deferred_revenue_book_core56_rank_20q_v057_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, opex.abs() + 1.0), 20))
def cg_f029_deferred_revenue_book_core57_rank_20q_v058_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_safe_div(deferredrev, fcf.abs() + 1.0), 20))
def cg_f029_deferred_revenue_book_core58_rank_20q_v059_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(deferredrev, 20))
def cg_f029_deferred_revenue_book_core59_rank_20q_v060_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_rank(_log(deferredrev.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f029_deferred_revenue_book_core60_pct_1q_v061_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(deferredrev, 1))
def cg_f029_deferred_revenue_book_core61_pct_1q_v062_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, revenue), 1))
def cg_f029_deferred_revenue_book_core62_pct_1q_v063_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(_diff(deferredrev, 4), revenue), 1))
def cg_f029_deferred_revenue_book_core63_pct_1q_v064_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, assets), 1))
def cg_f029_deferred_revenue_book_core64_pct_1q_v065_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, marketcap), 1))
def cg_f029_deferred_revenue_book_core65_pct_1q_v066_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, sharesbas), 1))
def cg_f029_deferred_revenue_book_core66_pct_1q_v067_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(revenue + _diff(deferredrev, 4), revenue), 1))
def cg_f029_deferred_revenue_book_core67_pct_1q_v068_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, opex.abs() + 1.0), 1))
def cg_f029_deferred_revenue_book_core68_pct_1q_v069_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, fcf.abs() + 1.0), 1))
def cg_f029_deferred_revenue_book_core69_pct_1q_v070_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_log(deferredrev.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f029_deferred_revenue_book_core70_pct_4q_v071_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(deferredrev, 4))
def cg_f029_deferred_revenue_book_core71_pct_4q_v072_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, revenue), 4))
def cg_f029_deferred_revenue_book_core72_pct_4q_v073_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(_diff(deferredrev, 4), revenue), 4))
def cg_f029_deferred_revenue_book_core73_pct_4q_v074_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, assets), 4))
def cg_f029_deferred_revenue_book_core74_pct_4q_v075_signal(deferredrev, revenue, assets, marketcap, sharesbas, opex, fcf, netinc):
    return _clean(_pct_change(_safe_div(deferredrev, marketcap), 4))
