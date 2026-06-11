import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f069_ev_sales_valuation_core00_mean_4q_v001_signal(ev, revenue, marketcap):
    return _clean(_mean(ev, 4))
def cg_f069_ev_sales_valuation_core01_mean_4q_v002_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue), 4))
def cg_f069_ev_sales_valuation_core02_mean_4q_v003_signal(ev, revenue, marketcap):
    return _clean(_mean(marketcap, 4))
def cg_f069_ev_sales_valuation_core03_mean_4q_v004_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(marketcap, revenue), 4))
def cg_f069_ev_sales_valuation_core04_mean_4q_v005_signal(ev, revenue, marketcap):
    return _clean(_mean(revenue, 4))
def cg_f069_ev_sales_valuation_core05_mean_4q_v006_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue.abs() + 1.0), 4))
def cg_f069_ev_sales_valuation_core06_mean_4q_v007_signal(ev, revenue, marketcap):
    return _clean(_mean(ev - marketcap, 4))
def cg_f069_ev_sales_valuation_core07_mean_4q_v008_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev - marketcap, revenue.abs() + 1.0), 4))
def cg_f069_ev_sales_valuation_core08_mean_4q_v009_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, marketcap.abs() + 1.0), 4))
def cg_f069_ev_sales_valuation_core09_mean_4q_v010_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue * 0.8 + 1.0), 4))

# core10-19: mean 8q
def cg_f069_ev_sales_valuation_core10_mean_8q_v011_signal(ev, revenue, marketcap):
    return _clean(_mean(ev, 8))
def cg_f069_ev_sales_valuation_core11_mean_8q_v012_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue), 8))
def cg_f069_ev_sales_valuation_core12_mean_8q_v013_signal(ev, revenue, marketcap):
    return _clean(_mean(marketcap, 8))
def cg_f069_ev_sales_valuation_core13_mean_8q_v014_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(marketcap, revenue), 8))
def cg_f069_ev_sales_valuation_core14_mean_8q_v015_signal(ev, revenue, marketcap):
    return _clean(_mean(revenue, 8))
def cg_f069_ev_sales_valuation_core15_mean_8q_v016_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core16_mean_8q_v017_signal(ev, revenue, marketcap):
    return _clean(_mean(ev - marketcap, 8))
def cg_f069_ev_sales_valuation_core17_mean_8q_v018_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev - marketcap, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core18_mean_8q_v019_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, marketcap.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core19_mean_8q_v020_signal(ev, revenue, marketcap):
    return _clean(_mean(_safe_div(ev, revenue * 0.8 + 1.0), 8))

# core20-29: z 8q
def cg_f069_ev_sales_valuation_core20_z_8q_v021_signal(ev, revenue, marketcap):
    return _clean(_z(ev, 8))
def cg_f069_ev_sales_valuation_core21_z_8q_v022_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue), 8))
def cg_f069_ev_sales_valuation_core22_z_8q_v023_signal(ev, revenue, marketcap):
    return _clean(_z(marketcap, 8))
def cg_f069_ev_sales_valuation_core23_z_8q_v024_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(marketcap, revenue), 8))
def cg_f069_ev_sales_valuation_core24_z_8q_v025_signal(ev, revenue, marketcap):
    return _clean(_z(revenue, 8))
def cg_f069_ev_sales_valuation_core25_z_8q_v026_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core26_z_8q_v027_signal(ev, revenue, marketcap):
    return _clean(_z(ev - marketcap, 8))
def cg_f069_ev_sales_valuation_core27_z_8q_v028_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev - marketcap, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core28_z_8q_v029_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, marketcap.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core29_z_8q_v030_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue * 0.8 + 1.0), 8))

# core30-39: z 20q
def cg_f069_ev_sales_valuation_core30_z_20q_v031_signal(ev, revenue, marketcap):
    return _clean(_z(ev, 20))
def cg_f069_ev_sales_valuation_core31_z_20q_v032_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue), 20))
def cg_f069_ev_sales_valuation_core32_z_20q_v033_signal(ev, revenue, marketcap):
    return _clean(_z(marketcap, 20))
def cg_f069_ev_sales_valuation_core33_z_20q_v034_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(marketcap, revenue), 20))
def cg_f069_ev_sales_valuation_core34_z_20q_v035_signal(ev, revenue, marketcap):
    return _clean(_z(revenue, 20))
def cg_f069_ev_sales_valuation_core35_z_20q_v036_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core36_z_20q_v037_signal(ev, revenue, marketcap):
    return _clean(_z(ev - marketcap, 20))
def cg_f069_ev_sales_valuation_core37_z_20q_v038_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev - marketcap, revenue.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core38_z_20q_v039_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, marketcap.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core39_z_20q_v040_signal(ev, revenue, marketcap):
    return _clean(_z(_safe_div(ev, revenue * 0.8 + 1.0), 20))

# core40-49: rank 8q
def cg_f069_ev_sales_valuation_core40_rank_8q_v041_signal(ev, revenue, marketcap):
    return _clean(_rank(ev, 8))
def cg_f069_ev_sales_valuation_core41_rank_8q_v042_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue), 8))
def cg_f069_ev_sales_valuation_core42_rank_8q_v043_signal(ev, revenue, marketcap):
    return _clean(_rank(marketcap, 8))
def cg_f069_ev_sales_valuation_core43_rank_8q_v044_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(marketcap, revenue), 8))
def cg_f069_ev_sales_valuation_core44_rank_8q_v045_signal(ev, revenue, marketcap):
    return _clean(_rank(revenue, 8))
def cg_f069_ev_sales_valuation_core45_rank_8q_v046_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core46_rank_8q_v047_signal(ev, revenue, marketcap):
    return _clean(_rank(ev - marketcap, 8))
def cg_f069_ev_sales_valuation_core47_rank_8q_v048_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev - marketcap, revenue.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core48_rank_8q_v049_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, marketcap.abs() + 1.0), 8))
def cg_f069_ev_sales_valuation_core49_rank_8q_v050_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue * 0.8 + 1.0), 8))

# core50-59: rank 20q
def cg_f069_ev_sales_valuation_core50_rank_20q_v051_signal(ev, revenue, marketcap):
    return _clean(_rank(ev, 20))
def cg_f069_ev_sales_valuation_core51_rank_20q_v052_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue), 20))
def cg_f069_ev_sales_valuation_core52_rank_20q_v053_signal(ev, revenue, marketcap):
    return _clean(_rank(marketcap, 20))
def cg_f069_ev_sales_valuation_core53_rank_20q_v054_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(marketcap, revenue), 20))
def cg_f069_ev_sales_valuation_core54_rank_20q_v055_signal(ev, revenue, marketcap):
    return _clean(_rank(revenue, 20))
def cg_f069_ev_sales_valuation_core55_rank_20q_v056_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core56_rank_20q_v057_signal(ev, revenue, marketcap):
    return _clean(_rank(ev - marketcap, 20))
def cg_f069_ev_sales_valuation_core57_rank_20q_v058_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev - marketcap, revenue.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core58_rank_20q_v059_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, marketcap.abs() + 1.0), 20))
def cg_f069_ev_sales_valuation_core59_rank_20q_v060_signal(ev, revenue, marketcap):
    return _clean(_rank(_safe_div(ev, revenue * 0.8 + 1.0), 20))

# core60-69: pct 1q
def cg_f069_ev_sales_valuation_core60_pct_1q_v061_signal(ev, revenue, marketcap):
    return _clean(_pct_change(ev, 1))
def cg_f069_ev_sales_valuation_core61_pct_1q_v062_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev, revenue), 1))
def cg_f069_ev_sales_valuation_core62_pct_1q_v063_signal(ev, revenue, marketcap):
    return _clean(_pct_change(marketcap, 1))
def cg_f069_ev_sales_valuation_core63_pct_1q_v064_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(marketcap, revenue), 1))
def cg_f069_ev_sales_valuation_core64_pct_1q_v065_signal(ev, revenue, marketcap):
    return _clean(_pct_change(revenue, 1))
def cg_f069_ev_sales_valuation_core65_pct_1q_v066_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev, revenue.abs() + 1.0), 1))
def cg_f069_ev_sales_valuation_core66_pct_1q_v067_signal(ev, revenue, marketcap):
    return _clean(_pct_change(ev - marketcap, 1))
def cg_f069_ev_sales_valuation_core67_pct_1q_v068_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev - marketcap, revenue.abs() + 1.0), 1))
def cg_f069_ev_sales_valuation_core68_pct_1q_v069_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev, marketcap.abs() + 1.0), 1))
def cg_f069_ev_sales_valuation_core69_pct_1q_v070_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev, revenue * 0.8 + 1.0), 1))

# core70-74: pct 4q
def cg_f069_ev_sales_valuation_core70_pct_4q_v071_signal(ev, revenue, marketcap):
    return _clean(_pct_change(ev, 4))
def cg_f069_ev_sales_valuation_core71_pct_4q_v072_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(ev, revenue), 4))
def cg_f069_ev_sales_valuation_core72_pct_4q_v073_signal(ev, revenue, marketcap):
    return _clean(_pct_change(marketcap, 4))
def cg_f069_ev_sales_valuation_core73_pct_4q_v074_signal(ev, revenue, marketcap):
    return _clean(_pct_change(_safe_div(marketcap, revenue), 4))
def cg_f069_ev_sales_valuation_core74_pct_4q_v075_signal(ev, revenue, marketcap):
    return _clean(_pct_change(revenue, 4))
