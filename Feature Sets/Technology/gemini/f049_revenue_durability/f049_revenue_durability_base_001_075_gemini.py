import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f049_revenue_durability_core00_mean_4q_v001_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_mean(down_mask, 4))
def cg_f049_revenue_durability_core01_mean_4q_v002_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_mean(yoy_decline, 4))
def cg_f049_revenue_durability_core02_mean_4q_v003_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    return _clean(_safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9))
def cg_f049_revenue_durability_core03_mean_4q_v004_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_mean(downside.abs(), 4))
def cg_f049_revenue_durability_core04_mean_4q_v005_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    return _clean(_safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9))
def cg_f049_revenue_durability_core05_mean_4q_v006_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_autocorr(revenue, 4), 4))
def cg_f049_revenue_durability_core06_mean_4q_v007_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_autocorr(_pct_change(revenue, 4), 4), 4))
def cg_f049_revenue_durability_core07_mean_4q_v008_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_mean(drawdown, 4))
def cg_f049_revenue_durability_core08_mean_4q_v009_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_kurt(revenue, 8), 4))
def cg_f049_revenue_durability_core09_mean_4q_v010_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_skew(revenue, 8), 4))

# core10-19: mean 8q
def cg_f049_revenue_durability_core10_mean_8q_v011_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_mean(down_mask, 8))
def cg_f049_revenue_durability_core11_mean_8q_v012_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_mean(yoy_decline, 8))
def cg_f049_revenue_durability_core12_mean_8q_v013_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    return _clean(_safe_div(_mean(yoy, 8), _std(yoy, 8).abs() + 1e-9))
def cg_f049_revenue_durability_core13_mean_8q_v014_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_mean(downside.abs(), 8))
def cg_f049_revenue_durability_core14_mean_8q_v015_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    return _clean(_safe_div(_mean(upside, 8), _mean(downside, 8) + 1e-9))
def cg_f049_revenue_durability_core15_mean_8q_v016_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_autocorr(revenue, 4), 8))
def cg_f049_revenue_durability_core16_mean_8q_v017_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_autocorr(_pct_change(revenue, 4), 4), 8))
def cg_f049_revenue_durability_core17_mean_8q_v018_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_mean(drawdown, 8))
def cg_f049_revenue_durability_core18_mean_8q_v019_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_kurt(revenue, 8), 8))
def cg_f049_revenue_durability_core19_mean_8q_v020_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_mean(_skew(revenue, 8), 8))

# core20-29: z 8q
def cg_f049_revenue_durability_core20_z_8q_v021_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_z(_mean(down_mask, 4), 8))
def cg_f049_revenue_durability_core21_z_8q_v022_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_z(_mean(yoy_decline, 4), 8))
def cg_f049_revenue_durability_core22_z_8q_v023_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_z(sr, 8))
def cg_f049_revenue_durability_core23_z_8q_v024_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_z(_mean(downside.abs(), 4), 8))
def cg_f049_revenue_durability_core24_z_8q_v025_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_z(omega, 8))
def cg_f049_revenue_durability_core25_z_8q_v026_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_autocorr(revenue, 4), 8))
def cg_f049_revenue_durability_core26_z_8q_v027_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_autocorr(_pct_change(revenue, 4), 4), 8))
def cg_f049_revenue_durability_core27_z_8q_v028_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_z(drawdown, 8))
def cg_f049_revenue_durability_core28_z_8q_v029_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_kurt(revenue, 8), 8))
def cg_f049_revenue_durability_core29_z_8q_v030_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_skew(revenue, 8), 8))

# core30-39: z 20q
def cg_f049_revenue_durability_core30_z_20q_v031_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_z(_mean(down_mask, 8), 20))
def cg_f049_revenue_durability_core31_z_20q_v032_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_z(_mean(yoy_decline, 8), 20))
def cg_f049_revenue_durability_core32_z_20q_v033_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 8), _std(yoy, 8).abs() + 1e-9)
    return _clean(_z(sr, 20))
def cg_f049_revenue_durability_core33_z_20q_v034_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_z(_mean(downside.abs(), 8), 20))
def cg_f049_revenue_durability_core34_z_20q_v035_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 8), _mean(downside, 8) + 1e-9)
    return _clean(_z(omega, 20))
def cg_f049_revenue_durability_core35_z_20q_v036_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_autocorr(revenue, 4), 20))
def cg_f049_revenue_durability_core36_z_20q_v037_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_autocorr(_pct_change(revenue, 4), 4), 20))
def cg_f049_revenue_durability_core37_z_20q_v038_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_z(drawdown, 20))
def cg_f049_revenue_durability_core38_z_20q_v039_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_kurt(revenue, 8), 20))
def cg_f049_revenue_durability_core39_z_20q_v040_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_z(_skew(revenue, 8), 20))

# core40-49: rank 12q
def cg_f049_revenue_durability_core40_rank_12q_v041_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_rank(_mean(down_mask, 4), 12))
def cg_f049_revenue_durability_core41_rank_12q_v042_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_rank(_mean(yoy_decline, 4), 12))
def cg_f049_revenue_durability_core42_rank_12q_v043_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_rank(sr, 12))
def cg_f049_revenue_durability_core43_rank_12q_v044_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_rank(_mean(downside.abs(), 4), 12))
def cg_f049_revenue_durability_core44_rank_12q_v045_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_rank(omega, 12))
def cg_f049_revenue_durability_core45_rank_12q_v046_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_autocorr(revenue, 4), 12))
def cg_f049_revenue_durability_core46_rank_12q_v047_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_autocorr(_pct_change(revenue, 4), 4), 12))
def cg_f049_revenue_durability_core47_rank_12q_v048_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_rank(drawdown, 12))
def cg_f049_revenue_durability_core48_rank_12q_v049_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_kurt(revenue, 8), 12))
def cg_f049_revenue_durability_core49_rank_12q_v050_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_skew(revenue, 8), 12))

# core50-59: rank 20q
def cg_f049_revenue_durability_core50_rank_20q_v051_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_rank(_mean(down_mask, 8), 20))
def cg_f049_revenue_durability_core51_rank_20q_v052_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_rank(_mean(yoy_decline, 8), 20))
def cg_f049_revenue_durability_core52_rank_20q_v053_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 8), _std(yoy, 8).abs() + 1e-9)
    return _clean(_rank(sr, 20))
def cg_f049_revenue_durability_core53_rank_20q_v054_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_rank(_mean(downside.abs(), 8), 20))
def cg_f049_revenue_durability_core54_rank_20q_v055_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 8), _mean(downside, 8) + 1e-9)
    return _clean(_rank(omega, 20))
def cg_f049_revenue_durability_core55_rank_20q_v056_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_autocorr(revenue, 4), 20))
def cg_f049_revenue_durability_core56_rank_20q_v057_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_autocorr(_pct_change(revenue, 4), 4), 20))
def cg_f049_revenue_durability_core57_rank_20q_v058_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_rank(drawdown, 20))
def cg_f049_revenue_durability_core58_rank_20q_v059_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_kurt(revenue, 8), 20))
def cg_f049_revenue_durability_core59_rank_20q_v060_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_rank(_skew(revenue, 8), 20))

# core60-69: pct 1q
def cg_f049_revenue_durability_core60_pct_1q_v061_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_pct_change(sr, 1))
def cg_f049_revenue_durability_core61_pct_1q_v062_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_pct_change(_mean(downside.abs(), 4), 1))
def cg_f049_revenue_durability_core62_pct_1q_v063_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_pct_change(omega, 1))
def cg_f049_revenue_durability_core63_pct_1q_v064_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_autocorr(revenue, 4), 1))
def cg_f049_revenue_durability_core64_pct_1q_v065_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_autocorr(_pct_change(revenue, 4), 4), 1))
def cg_f049_revenue_durability_core65_pct_1q_v066_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_pct_change(drawdown, 1))
def cg_f049_revenue_durability_core66_pct_1q_v067_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_kurt(revenue, 8), 1))
def cg_f049_revenue_durability_core67_pct_1q_v068_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_skew(revenue, 8), 1))
def cg_f049_revenue_durability_core68_pct_1q_v069_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_std(_pct_change(revenue, 4), 8), 1))
def cg_f049_revenue_durability_core69_pct_1q_v070_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_std(revenue, 8), 1))

# core70-74: pct 4q
def cg_f049_revenue_durability_core70_pct_4q_v071_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_pct_change(sr, 4))
def cg_f049_revenue_durability_core71_pct_4q_v072_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_pct_change(_mean(downside.abs(), 4), 4))
def cg_f049_revenue_durability_core72_pct_4q_v073_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_pct_change(omega, 4))
def cg_f049_revenue_durability_core73_pct_4q_v074_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_autocorr(revenue, 4), 4))
def cg_f049_revenue_durability_core74_pct_4q_v075_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_autocorr(_pct_change(revenue, 4), 4), 4))
