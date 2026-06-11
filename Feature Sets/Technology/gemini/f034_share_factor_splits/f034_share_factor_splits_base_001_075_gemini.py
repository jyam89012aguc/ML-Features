import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# Primary input is the Sharadar `sharefactor` adjustment field so split / reverse-split events are captured exactly rather than inferred from sharesbas (which would duplicate f031).

# core0-9: mean_4q
def cg_f034_share_factor_splits_core00_mean_4q_v001_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor, 4))
def cg_f034_share_factor_splits_core01_mean_4q_v002_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor.diff(), 4))
def cg_f034_share_factor_splits_core02_mean_4q_v003_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor.diff().abs(), 4))
def cg_f034_share_factor_splits_core03_mean_4q_v004_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor - 1.0, 4))
def cg_f034_share_factor_splits_core04_mean_4q_v005_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor - 1.0).abs(), 4))
def cg_f034_share_factor_splits_core05_mean_4q_v006_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_event_flag(sharefactor.diff().abs(), 0.01), 4))
def cg_f034_share_factor_splits_core06_mean_4q_v007_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor > 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core07_mean_4q_v008_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor < 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core08_mean_4q_v009_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_log(sharefactor.abs().clip(lower=0.01)), 4))
def cg_f034_share_factor_splits_core09_mean_4q_v010_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_pct_change(sharefactor, 1), 4))
# core10-19: mean_8q
def cg_f034_share_factor_splits_core10_mean_8q_v011_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor, 8))
def cg_f034_share_factor_splits_core11_mean_8q_v012_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor.diff(), 8))
def cg_f034_share_factor_splits_core12_mean_8q_v013_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor.diff().abs(), 8))
def cg_f034_share_factor_splits_core13_mean_8q_v014_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(sharefactor - 1.0, 8))
def cg_f034_share_factor_splits_core14_mean_8q_v015_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor - 1.0).abs(), 8))
def cg_f034_share_factor_splits_core15_mean_8q_v016_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_event_flag(sharefactor.diff().abs(), 0.01), 8))
def cg_f034_share_factor_splits_core16_mean_8q_v017_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor > 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core17_mean_8q_v018_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean((sharefactor < 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core18_mean_8q_v019_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_log(sharefactor.abs().clip(lower=0.01)), 8))
def cg_f034_share_factor_splits_core19_mean_8q_v020_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_mean(_pct_change(sharefactor, 1), 8))
# core20-29: z_8q
def cg_f034_share_factor_splits_core20_z_8q_v021_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor, 8))
def cg_f034_share_factor_splits_core21_z_8q_v022_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor.diff(), 8))
def cg_f034_share_factor_splits_core22_z_8q_v023_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor.diff().abs(), 8))
def cg_f034_share_factor_splits_core23_z_8q_v024_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor - 1.0, 8))
def cg_f034_share_factor_splits_core24_z_8q_v025_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor - 1.0).abs(), 8))
def cg_f034_share_factor_splits_core25_z_8q_v026_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_event_flag(sharefactor.diff().abs(), 0.01), 8))
def cg_f034_share_factor_splits_core26_z_8q_v027_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor > 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core27_z_8q_v028_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor < 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core28_z_8q_v029_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_log(sharefactor.abs().clip(lower=0.01)), 8))
def cg_f034_share_factor_splits_core29_z_8q_v030_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_pct_change(sharefactor, 1), 8))
# core30-39: z_20q
def cg_f034_share_factor_splits_core30_z_20q_v031_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor, 20))
def cg_f034_share_factor_splits_core31_z_20q_v032_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor.diff(), 20))
def cg_f034_share_factor_splits_core32_z_20q_v033_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor.diff().abs(), 20))
def cg_f034_share_factor_splits_core33_z_20q_v034_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(sharefactor - 1.0, 20))
def cg_f034_share_factor_splits_core34_z_20q_v035_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor - 1.0).abs(), 20))
def cg_f034_share_factor_splits_core35_z_20q_v036_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_event_flag(sharefactor.diff().abs(), 0.01), 20))
def cg_f034_share_factor_splits_core36_z_20q_v037_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor > 1.0).astype(float), 20))
def cg_f034_share_factor_splits_core37_z_20q_v038_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z((sharefactor < 1.0).astype(float), 20))
def cg_f034_share_factor_splits_core38_z_20q_v039_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_log(sharefactor.abs().clip(lower=0.01)), 20))
def cg_f034_share_factor_splits_core39_z_20q_v040_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_z(_pct_change(sharefactor, 1), 20))
# core40-49: rank_12q
def cg_f034_share_factor_splits_core40_rank_12q_v041_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor, 12))
def cg_f034_share_factor_splits_core41_rank_12q_v042_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor.diff(), 12))
def cg_f034_share_factor_splits_core42_rank_12q_v043_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor.diff().abs(), 12))
def cg_f034_share_factor_splits_core43_rank_12q_v044_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor - 1.0, 12))
def cg_f034_share_factor_splits_core44_rank_12q_v045_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor - 1.0).abs(), 12))
def cg_f034_share_factor_splits_core45_rank_12q_v046_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_event_flag(sharefactor.diff().abs(), 0.01), 12))
def cg_f034_share_factor_splits_core46_rank_12q_v047_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor > 1.0).astype(float), 12))
def cg_f034_share_factor_splits_core47_rank_12q_v048_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor < 1.0).astype(float), 12))
def cg_f034_share_factor_splits_core48_rank_12q_v049_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_log(sharefactor.abs().clip(lower=0.01)), 12))
def cg_f034_share_factor_splits_core49_rank_12q_v050_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_pct_change(sharefactor, 1), 12))
# core50-59: rank_20q
def cg_f034_share_factor_splits_core50_rank_20q_v051_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor, 20))
def cg_f034_share_factor_splits_core51_rank_20q_v052_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor.diff(), 20))
def cg_f034_share_factor_splits_core52_rank_20q_v053_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor.diff().abs(), 20))
def cg_f034_share_factor_splits_core53_rank_20q_v054_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(sharefactor - 1.0, 20))
def cg_f034_share_factor_splits_core54_rank_20q_v055_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor - 1.0).abs(), 20))
def cg_f034_share_factor_splits_core55_rank_20q_v056_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_event_flag(sharefactor.diff().abs(), 0.01), 20))
def cg_f034_share_factor_splits_core56_rank_20q_v057_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor > 1.0).astype(float), 20))
def cg_f034_share_factor_splits_core57_rank_20q_v058_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank((sharefactor < 1.0).astype(float), 20))
def cg_f034_share_factor_splits_core58_rank_20q_v059_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_log(sharefactor.abs().clip(lower=0.01)), 20))
def cg_f034_share_factor_splits_core59_rank_20q_v060_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_rank(_pct_change(sharefactor, 1), 20))
# core60-69: pct_1q
def cg_f034_share_factor_splits_core60_pct_1q_v061_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor, 1))
def cg_f034_share_factor_splits_core61_pct_1q_v062_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor.diff(), 1))
def cg_f034_share_factor_splits_core62_pct_1q_v063_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor.diff().abs(), 1))
def cg_f034_share_factor_splits_core63_pct_1q_v064_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor - 1.0, 1))
def cg_f034_share_factor_splits_core64_pct_1q_v065_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor - 1.0).abs(), 1))
def cg_f034_share_factor_splits_core65_pct_1q_v066_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_event_flag(sharefactor.diff().abs(), 0.01), 1))
def cg_f034_share_factor_splits_core66_pct_1q_v067_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor > 1.0).astype(float), 1))
def cg_f034_share_factor_splits_core67_pct_1q_v068_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor < 1.0).astype(float), 1))
def cg_f034_share_factor_splits_core68_pct_1q_v069_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_log(sharefactor.abs().clip(lower=0.01)), 1))
def cg_f034_share_factor_splits_core69_pct_1q_v070_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_pct_change(sharefactor, 1), 1))
# core70-74: pct_4q
def cg_f034_share_factor_splits_core70_pct_4q_v071_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor, 4))
def cg_f034_share_factor_splits_core71_pct_4q_v072_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor.diff(), 4))
def cg_f034_share_factor_splits_core72_pct_4q_v073_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor.diff().abs(), 4))
def cg_f034_share_factor_splits_core73_pct_4q_v074_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor - 1.0, 4))
def cg_f034_share_factor_splits_core74_pct_4q_v075_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor - 1.0).abs(), 4))
