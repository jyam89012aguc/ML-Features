import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f089_dv(volume, closeadj):
    return volume * closeadj


# 21d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slope_21d_2d_v001_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slope_63d_2d_v002_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slope_126d_2d_v003_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slope_252d_2d_v004_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slope_504d_2d_v005_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slope_21d_2d_v006_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slope_63d_2d_v007_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slope_126d_2d_v008_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slope_252d_2d_v009_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slope_504d_2d_v010_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slope_21d_2d_v011_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slope_63d_2d_v012_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slope_126d_2d_v013_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slope_252d_2d_v014_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slope_504d_2d_v015_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slope_21d_2d_v016_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slope_63d_2d_v017_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slope_126d_2d_v018_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slope_252d_2d_v019_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slope_504d_2d_v020_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slope_21d_2d_v021_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slope_63d_2d_v022_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slope_126d_2d_v023_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slope_252d_2d_v024_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slope_504d_2d_v025_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slope_21d_2d_v026_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slope_63d_2d_v027_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slope_126d_2d_v028_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slope_252d_2d_v029_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slope_504d_2d_v030_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slope_21d_2d_v031_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slope_63d_2d_v032_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slope_126d_2d_v033_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slope_252d_2d_v034_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slope_504d_2d_v035_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sm21_sl21_2d_v036_signal(volume, closeadj):
    base = _mean((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sm63_sl21_2d_v037_signal(volume, closeadj):
    base = _mean((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sm63_sl63_2d_v038_signal(volume, closeadj):
    base = _mean((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sm252_sl63_2d_v039_signal(volume, closeadj):
    base = _mean((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sm252_sl126_2d_v040_signal(volume, closeadj):
    base = _mean((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sm21_sl21_2d_v041_signal(closeadj, volume):
    base = _mean((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sm63_sl21_2d_v042_signal(closeadj, volume):
    base = _mean((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sm63_sl63_2d_v043_signal(closeadj, volume):
    base = _mean((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sm252_sl63_2d_v044_signal(closeadj, volume):
    base = _mean((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sm252_sl126_2d_v045_signal(closeadj, volume):
    base = _mean((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sm21_sl21_2d_v046_signal(volume, closeadj):
    base = _mean(volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sm63_sl21_2d_v047_signal(volume, closeadj):
    base = _mean(volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sm63_sl63_2d_v048_signal(volume, closeadj):
    base = _mean(volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sm252_sl63_2d_v049_signal(volume, closeadj):
    base = _mean(volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sm252_sl126_2d_v050_signal(volume, closeadj):
    base = _mean(volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sm21_sl21_2d_v051_signal(volume, closeadj):
    base = _mean((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sm63_sl21_2d_v052_signal(volume, closeadj):
    base = _mean((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sm63_sl63_2d_v053_signal(volume, closeadj):
    base = _mean((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sm252_sl63_2d_v054_signal(volume, closeadj):
    base = _mean((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sm252_sl126_2d_v055_signal(volume, closeadj):
    base = _mean((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sm21_sl21_2d_v056_signal(volume, closeadj):
    base = _mean((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sm63_sl21_2d_v057_signal(volume, closeadj):
    base = _mean((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sm63_sl63_2d_v058_signal(volume, closeadj):
    base = _mean((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sm252_sl63_2d_v059_signal(volume, closeadj):
    base = _mean((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sm252_sl126_2d_v060_signal(volume, closeadj):
    base = _mean((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sm21_sl21_2d_v061_signal(volume, closeadj):
    base = _mean((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sm63_sl21_2d_v062_signal(volume, closeadj):
    base = _mean((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sm63_sl63_2d_v063_signal(volume, closeadj):
    base = _mean((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sm252_sl63_2d_v064_signal(volume, closeadj):
    base = _mean((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sm252_sl126_2d_v065_signal(volume, closeadj):
    base = _mean((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sm21_sl21_2d_v066_signal(volume, closeadj):
    base = _mean(volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sm63_sl21_2d_v067_signal(volume, closeadj):
    base = _mean(volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sm63_sl63_2d_v068_signal(volume, closeadj):
    base = _mean(volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sm252_sl63_2d_v069_signal(volume, closeadj):
    base = _mean(volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sm252_sl126_2d_v070_signal(volume, closeadj):
    base = _mean(volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_pctslope_21d_2d_v071_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_pctslope_63d_2d_v072_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_pctslope_252d_2d_v073_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_pctslope_21d_2d_v074_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_pctslope_63d_2d_v075_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_pctslope_252d_2d_v076_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_pctslope_21d_2d_v077_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_pctslope_63d_2d_v078_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_pctslope_252d_2d_v079_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_pctslope_21d_2d_v080_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_pctslope_63d_2d_v081_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_pctslope_252d_2d_v082_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_pctslope_21d_2d_v083_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_pctslope_63d_2d_v084_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_pctslope_252d_2d_v085_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_pctslope_21d_2d_v086_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_pctslope_63d_2d_v087_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_pctslope_252d_2d_v088_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_pctslope_21d_2d_v089_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_pctslope_63d_2d_v090_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_pctslope_252d_2d_v091_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sgnslope_21d_2d_v092_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sgnslope_63d_2d_v093_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_sgnslope_252d_2d_v094_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sgnslope_21d_2d_v095_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sgnslope_63d_2d_v096_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_sgnslope_252d_2d_v097_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sgnslope_21d_2d_v098_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sgnslope_63d_2d_v099_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_sgnslope_252d_2d_v100_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sgnslope_21d_2d_v101_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sgnslope_63d_2d_v102_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_sgnslope_252d_2d_v103_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sgnslope_21d_2d_v104_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sgnslope_63d_2d_v105_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_sgnslope_252d_2d_v106_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sgnslope_21d_2d_v107_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sgnslope_63d_2d_v108_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_sgnslope_252d_2d_v109_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sgnslope_21d_2d_v110_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sgnslope_63d_2d_v111_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_sgnslope_252d_2d_v112_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_logmagslope_21d_2d_v113_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_logmagslope_63d_2d_v114_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_logmagslope_252d_2d_v115_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_logmagslope_21d_2d_v116_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_logmagslope_63d_2d_v117_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_logmagslope_252d_2d_v118_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_logmagslope_21d_2d_v119_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_logmagslope_63d_2d_v120_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_logmagslope_252d_2d_v121_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_logmagslope_21d_2d_v122_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_logmagslope_63d_2d_v123_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_logmagslope_252d_2d_v124_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_logmagslope_21d_2d_v125_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_logmagslope_63d_2d_v126_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_logmagslope_252d_2d_v127_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_logmagslope_21d_2d_v128_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_logmagslope_63d_2d_v129_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_logmagslope_252d_2d_v130_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_logmagslope_21d_2d_v131_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_logmagslope_63d_2d_v132_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_logmagslope_252d_2d_v133_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liquidity_dryup|
def f089vol_f089_volume_liquidity_context_liquidity_dryup_logslope_63d_2d_v134_signal(volume, closeadj):
    base = np.log(((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liquidity_dryup|
def f089vol_f089_volume_liquidity_context_liquidity_dryup_logslope_252d_2d_v135_signal(volume, closeadj):
    base = np.log(((volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|amihud_proxy|
def f089vol_f089_volume_liquidity_context_amihud_proxy_logslope_63d_2d_v136_signal(closeadj, volume):
    base = np.log(((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|amihud_proxy|
def f089vol_f089_volume_liquidity_context_amihud_proxy_logslope_252d_2d_v137_signal(closeadj, volume):
    base = np.log(((closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|vol_relative_252_63|
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_logslope_63d_2d_v138_signal(volume, closeadj):
    base = np.log((volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|vol_relative_252_63|
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_logslope_252d_2d_v139_signal(volume, closeadj):
    base = np.log((volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|vol_burst_flag|
def f089vol_f089_volume_liquidity_context_vol_burst_flag_logslope_63d_2d_v140_signal(volume, closeadj):
    base = np.log(((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|vol_burst_flag|
def f089vol_f089_volume_liquidity_context_vol_burst_flag_logslope_252d_2d_v141_signal(volume, closeadj):
    base = np.log(((volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|vol_drought_252|
def f089vol_f089_volume_liquidity_context_vol_drought_252_logslope_63d_2d_v142_signal(volume, closeadj):
    base = np.log(((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|vol_drought_252|
def f089vol_f089_volume_liquidity_context_vol_drought_252_logslope_252d_2d_v143_signal(volume, closeadj):
    base = np.log(((volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dv_zscore_252|
def f089vol_f089_volume_liquidity_context_dv_zscore_252_logslope_63d_2d_v144_signal(volume, closeadj):
    base = np.log(((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dv_zscore_252|
def f089vol_f089_volume_liquidity_context_dv_zscore_252_logslope_252d_2d_v145_signal(volume, closeadj):
    base = np.log(((_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|vol_skew_proxy|
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_logslope_63d_2d_v146_signal(volume, closeadj):
    base = np.log((volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|vol_skew_proxy|
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_logslope_252d_2d_v147_signal(volume, closeadj):
    base = np.log((volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

