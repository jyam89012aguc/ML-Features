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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f089_dv(volume, closeadj):
    return volume * closeadj


# 21d mean of liquidity_dryup scaled by closeadj
def f089vol_f089_volume_liquidity_context_liquidity_dryup_mean_21d_base_v001_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liquidity_dryup scaled by closeadj
def f089vol_f089_volume_liquidity_context_liquidity_dryup_mean_63d_base_v002_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liquidity_dryup scaled by closeadj
def f089vol_f089_volume_liquidity_context_liquidity_dryup_mean_126d_base_v003_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liquidity_dryup scaled by closeadj
def f089vol_f089_volume_liquidity_context_liquidity_dryup_mean_252d_base_v004_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liquidity_dryup scaled by closeadj
def f089vol_f089_volume_liquidity_context_liquidity_dryup_mean_504d_base_v005_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of amihud_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_amihud_proxy_mean_21d_base_v006_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of amihud_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_amihud_proxy_mean_63d_base_v007_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of amihud_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_amihud_proxy_mean_126d_base_v008_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of amihud_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_amihud_proxy_mean_252d_base_v009_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of amihud_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_amihud_proxy_mean_504d_base_v010_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of vol_relative_252_63 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_mean_21d_base_v011_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of vol_relative_252_63 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_mean_63d_base_v012_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of vol_relative_252_63 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_mean_126d_base_v013_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of vol_relative_252_63 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_mean_252d_base_v014_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of vol_relative_252_63 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_mean_504d_base_v015_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of vol_burst_flag scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_burst_flag_mean_21d_base_v016_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of vol_burst_flag scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_burst_flag_mean_63d_base_v017_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of vol_burst_flag scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_burst_flag_mean_126d_base_v018_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of vol_burst_flag scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_burst_flag_mean_252d_base_v019_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of vol_burst_flag scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_burst_flag_mean_504d_base_v020_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of vol_drought_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_drought_252_mean_21d_base_v021_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of vol_drought_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_drought_252_mean_63d_base_v022_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of vol_drought_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_drought_252_mean_126d_base_v023_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of vol_drought_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_drought_252_mean_252d_base_v024_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of vol_drought_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_drought_252_mean_504d_base_v025_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dv_zscore_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_dv_zscore_252_mean_21d_base_v026_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dv_zscore_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_dv_zscore_252_mean_63d_base_v027_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dv_zscore_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_dv_zscore_252_mean_126d_base_v028_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dv_zscore_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_dv_zscore_252_mean_252d_base_v029_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dv_zscore_252 scaled by closeadj
def f089vol_f089_volume_liquidity_context_dv_zscore_252_mean_504d_base_v030_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of vol_skew_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_mean_21d_base_v031_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of vol_skew_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_mean_63d_base_v032_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of vol_skew_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_mean_126d_base_v033_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of vol_skew_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_mean_252d_base_v034_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of vol_skew_proxy scaled by closeadj
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_mean_504d_base_v035_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_median_63d_base_v036_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_median_252d_base_v037_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_median_504d_base_v038_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_median_63d_base_v039_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_median_252d_base_v040_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_median_504d_base_v041_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_median_63d_base_v042_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_median_252d_base_v043_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_median_504d_base_v044_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_median_63d_base_v045_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_median_252d_base_v046_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_median_504d_base_v047_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_median_63d_base_v048_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_median_252d_base_v049_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_median_504d_base_v050_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_median_63d_base_v051_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_median_252d_base_v052_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_median_504d_base_v053_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_median_63d_base_v054_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_median_252d_base_v055_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_median_504d_base_v056_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rmax_252d_base_v057_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rmax_504d_base_v058_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_rmax_252d_base_v059_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_rmax_504d_base_v060_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_rmax_252d_base_v061_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_rmax_504d_base_v062_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_rmax_252d_base_v063_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_rmax_504d_base_v064_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_rmax_252d_base_v065_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_rmax_504d_base_v066_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_rmax_252d_base_v067_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_rmax_504d_base_v068_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_rmax_252d_base_v069_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_rmax_504d_base_v070_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rmin_252d_base_v071_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rmin_504d_base_v072_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_rmin_252d_base_v073_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_rmin_504d_base_v074_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_rmin_252d_base_v075_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

