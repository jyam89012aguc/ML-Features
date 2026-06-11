import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f047_revenue_growth_core00_mean_4q_v001_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core01_mean_4q_v002_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 1), 4))
def cg_f047_revenue_growth_core02_mean_4q_v003_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(_safe_div(revenue, assets), 4), 4))
def cg_f047_revenue_growth_core03_mean_4q_v004_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 4))
def cg_f047_revenue_growth_core04_mean_4q_v005_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4) - _pct_change(assets, 4), 4))
def cg_f047_revenue_growth_core05_mean_4q_v006_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4) - _pct_change(opex, 4), 4))
def cg_f047_revenue_growth_core07_mean_4q_v008_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core08_mean_4q_v009_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    # Log difference in revenue
    return _clean(_mean(_diff(_log(revenue.clip(lower=1.0)), 4), 4))
def cg_f047_revenue_growth_core09_mean_4q_v010_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    # Standardized revenue growth
    return _clean(_mean(_z(_pct_change(revenue, 4), 12), 4))

# core10-19: mean 8q
def cg_f047_revenue_growth_core10_mean_8q_v011_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4), 8))
def cg_f047_revenue_growth_core11_mean_8q_v012_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 1), 8))
def cg_f047_revenue_growth_core12_mean_8q_v013_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(_safe_div(revenue, assets), 4), 8))
def cg_f047_revenue_growth_core13_mean_8q_v014_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 8))
def cg_f047_revenue_growth_core14_mean_8q_v015_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4) - _pct_change(assets, 4), 8))
def cg_f047_revenue_growth_core15_mean_8q_v016_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_pct_change(revenue, 4) - _pct_change(opex, 4), 8))
def cg_f047_revenue_growth_core16_mean_8q_v017_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f047_revenue_growth_core17_mean_8q_v018_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core18_mean_8q_v019_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_diff(_log(revenue.clip(lower=1.0)), 4), 8))
def cg_f047_revenue_growth_core19_mean_8q_v020_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_mean(_z(_pct_change(revenue, 4), 12), 8))

# core20-29: z 8q
def cg_f047_revenue_growth_core20_z_8q_v021_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4), 8))
def cg_f047_revenue_growth_core21_z_8q_v022_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 1), 8))
def cg_f047_revenue_growth_core22_z_8q_v023_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(_safe_div(revenue, assets), 4), 8))
def cg_f047_revenue_growth_core23_z_8q_v024_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 8))
def cg_f047_revenue_growth_core24_z_8q_v025_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4) - _pct_change(assets, 4), 8))
def cg_f047_revenue_growth_core25_z_8q_v026_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4) - _pct_change(opex, 4), 8))
def cg_f047_revenue_growth_core26_z_8q_v027_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 1), 8))
def cg_f047_revenue_growth_core27_z_8q_v028_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core28_z_8q_v029_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_log(revenue.clip(lower=1.0)), 4), 8))
def cg_f047_revenue_growth_core29_z_8q_v030_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_z(_pct_change(revenue, 4), 12), 8))

# core30-39: z 20q
def cg_f047_revenue_growth_core30_z_20q_v031_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4), 20))
def cg_f047_revenue_growth_core31_z_20q_v032_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 1), 20))
def cg_f047_revenue_growth_core32_z_20q_v033_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(_safe_div(revenue, assets), 4), 20))
def cg_f047_revenue_growth_core33_z_20q_v034_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 20))
def cg_f047_revenue_growth_core34_z_20q_v035_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4) - _pct_change(assets, 4), 20))
def cg_f047_revenue_growth_core35_z_20q_v036_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_pct_change(revenue, 4) - _pct_change(opex, 4), 20))
def cg_f047_revenue_growth_core36_z_20q_v037_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 1), 20))
def cg_f047_revenue_growth_core37_z_20q_v038_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 20))
def cg_f047_revenue_growth_core38_z_20q_v039_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_diff(_log(revenue.clip(lower=1.0)), 4), 20))
def cg_f047_revenue_growth_core39_z_20q_v040_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_z(_z(_pct_change(revenue, 4), 12), 20))

# core40-49: rank 12q
def cg_f047_revenue_growth_core40_rank_12q_v041_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4), 12))
def cg_f047_revenue_growth_core41_rank_12q_v042_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 1), 12))
def cg_f047_revenue_growth_core42_rank_12q_v043_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(_safe_div(revenue, assets), 4), 12))
def cg_f047_revenue_growth_core43_rank_12q_v044_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 12))
def cg_f047_revenue_growth_core44_rank_12q_v045_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4) - _pct_change(assets, 4), 12))
def cg_f047_revenue_growth_core45_rank_12q_v046_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4) - _pct_change(opex, 4), 12))
def cg_f047_revenue_growth_core46_rank_12q_v047_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 1), 12))
def cg_f047_revenue_growth_core47_rank_12q_v048_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core48_rank_12q_v049_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_log(revenue.clip(lower=1.0)), 4), 12))
def cg_f047_revenue_growth_core49_rank_12q_v050_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_z(_pct_change(revenue, 4), 12), 12))

# core50-59: rank 20q
def cg_f047_revenue_growth_core50_rank_20q_v051_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4), 20))
def cg_f047_revenue_growth_core51_rank_20q_v052_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 1), 20))
def cg_f047_revenue_growth_core52_rank_20q_v053_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(_safe_div(revenue, assets), 4), 20))
def cg_f047_revenue_growth_core53_rank_20q_v054_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 20))
def cg_f047_revenue_growth_core54_rank_20q_v055_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4) - _pct_change(assets, 4), 20))
def cg_f047_revenue_growth_core55_rank_20q_v056_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_pct_change(revenue, 4) - _pct_change(opex, 4), 20))
def cg_f047_revenue_growth_core56_rank_20q_v057_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 1), 20))
def cg_f047_revenue_growth_core57_rank_20q_v058_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 20))
def cg_f047_revenue_growth_core58_rank_20q_v059_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_diff(_log(revenue.clip(lower=1.0)), 4), 20))
def cg_f047_revenue_growth_core59_rank_20q_v060_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_rank(_z(_pct_change(revenue, 4), 12), 20))

# core60-69: pct 1q
def cg_f047_revenue_growth_core60_pct_1q_v061_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4), 1))
def cg_f047_revenue_growth_core61_pct_1q_v062_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 1), 1))
def cg_f047_revenue_growth_core62_pct_1q_v063_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(_safe_div(revenue, assets), 4), 1))
def cg_f047_revenue_growth_core63_pct_1q_v064_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 1))
def cg_f047_revenue_growth_core64_pct_1q_v065_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4) - _pct_change(assets, 4), 1))
def cg_f047_revenue_growth_core65_pct_1q_v066_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4) - _pct_change(opex, 4), 1))
def cg_f047_revenue_growth_core66_pct_1q_v067_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 1), 1))
def cg_f047_revenue_growth_core67_pct_1q_v068_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_pct_change(revenue, 4), 4), 1))
def cg_f047_revenue_growth_core68_pct_1q_v069_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_diff(_log(revenue.clip(lower=1.0)), 4), 1))
def cg_f047_revenue_growth_core69_pct_1q_v070_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_z(_pct_change(revenue, 4), 12), 1))

# core70-74: pct 4q
def cg_f047_revenue_growth_core70_pct_4q_v071_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core71_pct_4q_v072_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 1), 4))
def cg_f047_revenue_growth_core72_pct_4q_v073_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(_safe_div(revenue, assets), 4), 4))
def cg_f047_revenue_growth_core73_pct_4q_v074_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(_safe_div(revenue, opex.abs() + 1.0), 4), 4))
def cg_f047_revenue_growth_core74_pct_4q_v075_signal(revenue, assets, marketcap, opex, equity, cor, netinc, ebitda):
    return _clean(_pct_change(_pct_change(revenue, 4) - _pct_change(assets, 4), 4))

def cg_f047_revenue_growth_rev_yoy_mean_63d_base_v007_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_5y_cagr_median_252d_base_v076_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_5y_cagr_median_504d_base_v077_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_slope_252d_median_63d_base_v078_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_slope_252d_median_252d_base_v079_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_slope_252d_median_504d_base_v080_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_q_streak_median_63d_base_v081_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_q_streak_median_252d_base_v082_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_q_streak_median_504d_base_v083_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_growth_z_252_median_63d_base_v084_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_growth_z_252_median_252d_base_v085_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_growth_z_252_median_504d_base_v086_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_63d_base_v087_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_252d_base_v088_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_504d_base_v089_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_z_median_63d_base_v090_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_z_median_252d_base_v091_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_z_median_504d_base_v092_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_63d_base_v093_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_252d_base_v094_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_504d_base_v095_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_63d_base_v096_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_252d_base_v097_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_504d_base_v098_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_pctile_median_63d_base_v099_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f047_revenue_growth_rev_yoy_peer_sector_pctile_median_252d_base_v100_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

