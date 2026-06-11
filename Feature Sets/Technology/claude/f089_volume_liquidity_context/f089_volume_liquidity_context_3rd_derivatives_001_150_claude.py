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


# 21d acceleration of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accel_21d_3d_v001_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accel_63d_3d_v002_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accel_126d_3d_v003_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accel_252d_3d_v004_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accel_21d_3d_v005_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accel_63d_3d_v006_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accel_126d_3d_v007_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accel_252d_3d_v008_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accel_21d_3d_v009_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accel_63d_3d_v010_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accel_126d_3d_v011_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accel_252d_3d_v012_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accel_21d_3d_v013_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accel_63d_3d_v014_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accel_126d_3d_v015_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accel_252d_3d_v016_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accel_21d_3d_v017_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accel_63d_3d_v018_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accel_126d_3d_v019_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accel_252d_3d_v020_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accel_21d_3d_v021_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accel_63d_3d_v022_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accel_126d_3d_v023_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accel_252d_3d_v024_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accel_21d_3d_v025_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accel_63d_3d_v026_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accel_126d_3d_v027_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accel_252d_3d_v028_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slopez_21d_z126_3d_v029_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slopez_63d_z252_3d_v030_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slopez_126d_z252_3d_v031_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_slopez_252d_z504_3d_v032_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slopez_21d_z126_3d_v033_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slopez_63d_z252_3d_v034_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slopez_126d_z252_3d_v035_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_slopez_252d_z504_3d_v036_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slopez_21d_z126_3d_v037_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slopez_63d_z252_3d_v038_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slopez_126d_z252_3d_v039_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_slopez_252d_z504_3d_v040_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slopez_21d_z126_3d_v041_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slopez_63d_z252_3d_v042_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slopez_126d_z252_3d_v043_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_slopez_252d_z504_3d_v044_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slopez_21d_z126_3d_v045_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slopez_63d_z252_3d_v046_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slopez_126d_z252_3d_v047_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_slopez_252d_z504_3d_v048_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slopez_21d_z126_3d_v049_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slopez_63d_z252_3d_v050_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slopez_126d_z252_3d_v051_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_slopez_252d_z504_3d_v052_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slopez_21d_z126_3d_v053_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slopez_63d_z252_3d_v054_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slopez_126d_z252_3d_v055_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_slopez_252d_z504_3d_v056_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_jerk_21d_3d_v057_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_jerk_63d_3d_v058_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_jerk_126d_3d_v059_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_jerk_21d_3d_v060_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_jerk_63d_3d_v061_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_jerk_126d_3d_v062_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_jerk_21d_3d_v063_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_jerk_63d_3d_v064_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_jerk_126d_3d_v065_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_jerk_21d_3d_v066_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_jerk_63d_3d_v067_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_jerk_126d_3d_v068_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_jerk_21d_3d_v069_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_jerk_63d_3d_v070_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_jerk_126d_3d_v071_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_jerk_21d_3d_v072_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_jerk_63d_3d_v073_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_jerk_126d_3d_v074_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_jerk_21d_3d_v075_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_jerk_63d_3d_v076_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_jerk_126d_3d_v077_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liquidity_dryup smoothed over 252d
def f089vol_f089_volume_liquidity_context_liquidity_dryup_smoothaccel_63d_sm252_3d_v078_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liquidity_dryup smoothed over 504d
def f089vol_f089_volume_liquidity_context_liquidity_dryup_smoothaccel_252d_sm504_3d_v079_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of amihud_proxy smoothed over 252d
def f089vol_f089_volume_liquidity_context_amihud_proxy_smoothaccel_63d_sm252_3d_v080_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of amihud_proxy smoothed over 504d
def f089vol_f089_volume_liquidity_context_amihud_proxy_smoothaccel_252d_sm504_3d_v081_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of vol_relative_252_63 smoothed over 252d
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_smoothaccel_63d_sm252_3d_v082_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of vol_relative_252_63 smoothed over 504d
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_smoothaccel_252d_sm504_3d_v083_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of vol_burst_flag smoothed over 252d
def f089vol_f089_volume_liquidity_context_vol_burst_flag_smoothaccel_63d_sm252_3d_v084_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of vol_burst_flag smoothed over 504d
def f089vol_f089_volume_liquidity_context_vol_burst_flag_smoothaccel_252d_sm504_3d_v085_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of vol_drought_252 smoothed over 252d
def f089vol_f089_volume_liquidity_context_vol_drought_252_smoothaccel_63d_sm252_3d_v086_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of vol_drought_252 smoothed over 504d
def f089vol_f089_volume_liquidity_context_vol_drought_252_smoothaccel_252d_sm504_3d_v087_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dv_zscore_252 smoothed over 252d
def f089vol_f089_volume_liquidity_context_dv_zscore_252_smoothaccel_63d_sm252_3d_v088_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dv_zscore_252 smoothed over 504d
def f089vol_f089_volume_liquidity_context_dv_zscore_252_smoothaccel_252d_sm504_3d_v089_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of vol_skew_proxy smoothed over 252d
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_smoothaccel_63d_sm252_3d_v090_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of vol_skew_proxy smoothed over 504d
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_smoothaccel_252d_sm504_3d_v091_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accelz_21d_z252_3d_v092_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_accelz_63d_z504_3d_v093_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accelz_21d_z252_3d_v094_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_accelz_63d_z504_3d_v095_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accelz_21d_z252_3d_v096_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_accelz_63d_z504_3d_v097_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accelz_21d_z252_3d_v098_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_accelz_63d_z504_3d_v099_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accelz_21d_z252_3d_v100_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_accelz_63d_z504_3d_v101_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accelz_21d_z252_3d_v102_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_accelz_63d_z504_3d_v103_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accelz_21d_z252_3d_v104_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_accelz_63d_z504_3d_v105_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liquidity_dryup (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_liquidity_dryup_signflip_63d_3d_v106_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liquidity_dryup (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_liquidity_dryup_signflip_252d_3d_v107_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in amihud_proxy (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_amihud_proxy_signflip_63d_3d_v108_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in amihud_proxy (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_amihud_proxy_signflip_252d_3d_v109_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in vol_relative_252_63 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_signflip_63d_3d_v110_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in vol_relative_252_63 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_signflip_252d_3d_v111_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in vol_burst_flag (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_burst_flag_signflip_63d_3d_v112_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in vol_burst_flag (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_burst_flag_signflip_252d_3d_v113_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in vol_drought_252 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_drought_252_signflip_63d_3d_v114_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in vol_drought_252 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_drought_252_signflip_252d_3d_v115_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dv_zscore_252 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_dv_zscore_252_signflip_63d_3d_v116_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dv_zscore_252 (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_dv_zscore_252_signflip_252d_3d_v117_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in vol_skew_proxy (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_signflip_63d_3d_v118_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in vol_skew_proxy (raw count, no price scaling)
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_signflip_252d_3d_v119_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liquidity_dryup normalized by 252d range
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rngaccel_63d_r252_3d_v120_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liquidity_dryup normalized by 504d range
def f089vol_f089_volume_liquidity_context_liquidity_dryup_rngaccel_252d_r504_3d_v121_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amihud_proxy normalized by 252d range
def f089vol_f089_volume_liquidity_context_amihud_proxy_rngaccel_63d_r252_3d_v122_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amihud_proxy normalized by 504d range
def f089vol_f089_volume_liquidity_context_amihud_proxy_rngaccel_252d_r504_3d_v123_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_relative_252_63 normalized by 252d range
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_rngaccel_63d_r252_3d_v124_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_relative_252_63 normalized by 504d range
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_rngaccel_252d_r504_3d_v125_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_burst_flag normalized by 252d range
def f089vol_f089_volume_liquidity_context_vol_burst_flag_rngaccel_63d_r252_3d_v126_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_burst_flag normalized by 504d range
def f089vol_f089_volume_liquidity_context_vol_burst_flag_rngaccel_252d_r504_3d_v127_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_drought_252 normalized by 252d range
def f089vol_f089_volume_liquidity_context_vol_drought_252_rngaccel_63d_r252_3d_v128_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_drought_252 normalized by 504d range
def f089vol_f089_volume_liquidity_context_vol_drought_252_rngaccel_252d_r504_3d_v129_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_zscore_252 normalized by 252d range
def f089vol_f089_volume_liquidity_context_dv_zscore_252_rngaccel_63d_r252_3d_v130_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_zscore_252 normalized by 504d range
def f089vol_f089_volume_liquidity_context_dv_zscore_252_rngaccel_252d_r504_3d_v131_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_skew_proxy normalized by 252d range
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_rngaccel_63d_r252_3d_v132_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_skew_proxy normalized by 504d range
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_rngaccel_252d_r504_3d_v133_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_cumslope_21d_3d_v134_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_cumslope_63d_3d_v135_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_cumslope_252d_3d_v136_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_cumslope_21d_3d_v137_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_cumslope_63d_3d_v138_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_cumslope_252d_3d_v139_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_cumslope_21d_3d_v140_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_cumslope_63d_3d_v141_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_cumslope_252d_3d_v142_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_cumslope_21d_3d_v143_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_cumslope_63d_3d_v144_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_cumslope_252d_3d_v145_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_cumslope_21d_3d_v146_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_cumslope_63d_3d_v147_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_cumslope_252d_3d_v148_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_cumslope_21d_3d_v149_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_cumslope_63d_3d_v150_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

