import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f040_asset_base_core00_mean_4q_v001_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(assets, 4))
def cg_f040_asset_base_core01_mean_4q_v002_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assetsc, assets), 4))
def cg_f040_asset_base_core02_mean_4q_v003_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, revenue), 4))
def cg_f040_asset_base_core03_mean_4q_v004_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, marketcap), 4))
def cg_f040_asset_base_core04_mean_4q_v005_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, equity.abs() + 1.0), 4))
def cg_f040_asset_base_core05_mean_4q_v006_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets - liabilities, assets), 4))
def cg_f040_asset_base_core06_mean_4q_v007_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, sharesbas), 4))
def cg_f040_asset_base_core07_mean_4q_v008_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_pct_change(assets, 4), 4))
def cg_f040_asset_base_core08_mean_4q_v009_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, opex.abs() + 1.0), 4))
def cg_f040_asset_base_core09_mean_4q_v010_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_log(assets.clip(lower=1.0)), 4))

# core10-19: mean 8q
def cg_f040_asset_base_core10_mean_8q_v011_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(assets, 8))
def cg_f040_asset_base_core11_mean_8q_v012_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assetsc, assets), 8))
def cg_f040_asset_base_core12_mean_8q_v013_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, revenue), 8))
def cg_f040_asset_base_core13_mean_8q_v014_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, marketcap), 8))
def cg_f040_asset_base_core14_mean_8q_v015_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, equity.abs() + 1.0), 8))
def cg_f040_asset_base_core15_mean_8q_v016_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets - liabilities, assets), 8))
def cg_f040_asset_base_core16_mean_8q_v017_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, sharesbas), 8))
def cg_f040_asset_base_core17_mean_8q_v018_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_pct_change(assets, 4), 8))
def cg_f040_asset_base_core18_mean_8q_v019_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_safe_div(assets, opex.abs() + 1.0), 8))
def cg_f040_asset_base_core19_mean_8q_v020_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_mean(_log(assets.clip(lower=1.0)), 8))

# core20-29: z 8q
def cg_f040_asset_base_core20_z_8q_v021_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(assets, 8))
def cg_f040_asset_base_core21_z_8q_v022_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assetsc, assets), 8))
def cg_f040_asset_base_core22_z_8q_v023_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, revenue), 8))
def cg_f040_asset_base_core23_z_8q_v024_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, marketcap), 8))
def cg_f040_asset_base_core24_z_8q_v025_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, equity.abs() + 1.0), 8))
def cg_f040_asset_base_core25_z_8q_v026_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets - liabilities, assets), 8))
def cg_f040_asset_base_core26_z_8q_v027_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, sharesbas), 8))
def cg_f040_asset_base_core27_z_8q_v028_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_pct_change(assets, 4), 8))
def cg_f040_asset_base_core28_z_8q_v029_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, opex.abs() + 1.0), 8))
def cg_f040_asset_base_core29_z_8q_v030_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_log(assets.clip(lower=1.0)), 8))

# core30-39: z 20q
def cg_f040_asset_base_core30_z_20q_v031_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(assets, 20))
def cg_f040_asset_base_core31_z_20q_v032_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assetsc, assets), 20))
def cg_f040_asset_base_core32_z_20q_v033_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, revenue), 20))
def cg_f040_asset_base_core33_z_20q_v034_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, marketcap), 20))
def cg_f040_asset_base_core34_z_20q_v035_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, equity.abs() + 1.0), 20))
def cg_f040_asset_base_core35_z_20q_v036_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets - liabilities, assets), 20))
def cg_f040_asset_base_core36_z_20q_v037_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, sharesbas), 20))
def cg_f040_asset_base_core37_z_20q_v038_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_pct_change(assets, 4), 20))
def cg_f040_asset_base_core38_z_20q_v039_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_safe_div(assets, opex.abs() + 1.0), 20))
def cg_f040_asset_base_core39_z_20q_v040_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_z(_log(assets.clip(lower=1.0)), 20))

# core40-49: rank 12q
def cg_f040_asset_base_core40_rank_12q_v041_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(assets, 12))
def cg_f040_asset_base_core41_rank_12q_v042_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assetsc, assets), 12))
def cg_f040_asset_base_core42_rank_12q_v043_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, revenue), 12))
def cg_f040_asset_base_core43_rank_12q_v044_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, marketcap), 12))
def cg_f040_asset_base_core44_rank_12q_v045_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, equity.abs() + 1.0), 12))
def cg_f040_asset_base_core45_rank_12q_v046_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets - liabilities, assets), 12))
def cg_f040_asset_base_core46_rank_12q_v047_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, sharesbas), 12))
def cg_f040_asset_base_core47_rank_12q_v048_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_pct_change(assets, 4), 12))
def cg_f040_asset_base_core48_rank_12q_v049_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, opex.abs() + 1.0), 12))
def cg_f040_asset_base_core49_rank_12q_v050_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_log(assets.clip(lower=1.0)), 12))

# core50-59: rank 20q
def cg_f040_asset_base_core50_rank_20q_v051_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(assets, 20))
def cg_f040_asset_base_core51_rank_20q_v052_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assetsc, assets), 20))
def cg_f040_asset_base_core52_rank_20q_v053_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, revenue), 20))
def cg_f040_asset_base_core53_rank_20q_v054_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, marketcap), 20))
def cg_f040_asset_base_core54_rank_20q_v055_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, equity.abs() + 1.0), 20))
def cg_f040_asset_base_core55_rank_20q_v056_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets - liabilities, assets), 20))
def cg_f040_asset_base_core56_rank_20q_v057_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, sharesbas), 20))
def cg_f040_asset_base_core57_rank_20q_v058_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_pct_change(assets, 4), 20))
def cg_f040_asset_base_core58_rank_20q_v059_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_safe_div(assets, opex.abs() + 1.0), 20))
def cg_f040_asset_base_core59_rank_20q_v060_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_rank(_log(assets.clip(lower=1.0)), 20))

# core60-69: pct 1q
def cg_f040_asset_base_core60_pct_1q_v061_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(assets, 1))
def cg_f040_asset_base_core61_pct_1q_v062_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assetsc, assets), 1))
def cg_f040_asset_base_core62_pct_1q_v063_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, revenue), 1))
def cg_f040_asset_base_core63_pct_1q_v064_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, marketcap), 1))
def cg_f040_asset_base_core64_pct_1q_v065_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, equity.abs() + 1.0), 1))
def cg_f040_asset_base_core65_pct_1q_v066_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets - liabilities, assets), 1))
def cg_f040_asset_base_core66_pct_1q_v067_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, sharesbas), 1))
def cg_f040_asset_base_core67_pct_1q_v068_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_pct_change(assets, 4), 1))
def cg_f040_asset_base_core68_pct_1q_v069_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, opex.abs() + 1.0), 1))
def cg_f040_asset_base_core69_pct_1q_v070_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_log(assets.clip(lower=1.0)), 1))

# core70-74: pct 4q
def cg_f040_asset_base_core70_pct_4q_v071_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(assets, 4))
def cg_f040_asset_base_core71_pct_4q_v072_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assetsc, assets), 4))
def cg_f040_asset_base_core72_pct_4q_v073_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, revenue), 4))
def cg_f040_asset_base_core73_pct_4q_v074_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, marketcap), 4))
def cg_f040_asset_base_core74_pct_4q_v075_signal(assets, assetsc, revenue, marketcap, equity, liabilities, sharesbas, opex):
    return _clean(_pct_change(_safe_div(assets, equity.abs() + 1.0), 4))
