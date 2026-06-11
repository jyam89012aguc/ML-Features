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


# 63d z-score of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_z_63d_base_v076_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_z_126d_base_v077_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_z_252d_base_v078_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_z_504d_base_v079_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_z_63d_base_v080_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_z_126d_base_v081_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_z_252d_base_v082_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_z_504d_base_v083_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_z_63d_base_v084_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_z_126d_base_v085_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_z_252d_base_v086_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_z_504d_base_v087_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_z_63d_base_v088_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_z_126d_base_v089_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_z_252d_base_v090_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_z_504d_base_v091_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_z_63d_base_v092_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_z_126d_base_v093_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_z_252d_base_v094_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_z_504d_base_v095_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_z_63d_base_v096_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_z_126d_base_v097_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_z_252d_base_v098_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_z_504d_base_v099_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_z_63d_base_v100_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_z_126d_base_v101_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_z_252d_base_v102_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_z_504d_base_v103_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_distmax_252d_base_v104_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_distmax_504d_base_v105_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_distmax_252d_base_v106_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_distmax_504d_base_v107_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_distmax_252d_base_v108_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_distmax_504d_base_v109_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_distmax_252d_base_v110_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_distmax_504d_base_v111_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_distmax_252d_base_v112_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_distmax_504d_base_v113_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_distmax_252d_base_v114_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_distmax_504d_base_v115_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_distmax_252d_base_v116_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_distmax_504d_base_v117_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_distmed_126d_base_v118_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_distmed_252d_base_v119_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_distmed_504d_base_v120_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_distmed_126d_base_v121_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_distmed_252d_base_v122_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_distmed_504d_base_v123_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_distmed_126d_base_v124_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_distmed_252d_base_v125_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_distmed_504d_base_v126_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_distmed_126d_base_v127_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_distmed_252d_base_v128_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_distmed_504d_base_v129_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_distmed_126d_base_v130_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_distmed_252d_base_v131_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_distmed_504d_base_v132_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_distmed_126d_base_v133_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_distmed_252d_base_v134_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_distmed_504d_base_v135_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_distmed_126d_base_v136_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_distmed_252d_base_v137_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of vol_skew_proxy
def f089vol_f089_volume_liquidity_context_vol_skew_proxy_distmed_504d_base_v138_signal(volume, closeadj):
    base = volume.rolling(252, min_periods=63).max() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_chg_63d_base_v139_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liquidity_dryup
def f089vol_f089_volume_liquidity_context_liquidity_dryup_chg_252d_base_v140_signal(volume, closeadj):
    base = (volume.rolling(63, min_periods=21).mean() < 0.5 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_chg_63d_base_v141_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in amihud_proxy
def f089vol_f089_volume_liquidity_context_amihud_proxy_chg_252d_base_v142_signal(closeadj, volume):
    base = (closeadj.pct_change().abs()) / (_f089_dv(volume, closeadj).replace(0, np.nan))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_chg_63d_base_v143_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in vol_relative_252_63
def f089vol_f089_volume_liquidity_context_vol_relative_252_63_chg_252d_base_v144_signal(volume, closeadj):
    base = volume.rolling(63, min_periods=21).mean() / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_chg_63d_base_v145_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in vol_burst_flag
def f089vol_f089_volume_liquidity_context_vol_burst_flag_chg_252d_base_v146_signal(volume, closeadj):
    base = (volume > 3 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_chg_63d_base_v147_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in vol_drought_252
def f089vol_f089_volume_liquidity_context_vol_drought_252_chg_252d_base_v148_signal(volume, closeadj):
    base = (volume.rolling(252, min_periods=63).min() < 0.1 * volume.rolling(252, min_periods=63).mean()).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_chg_63d_base_v149_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dv_zscore_252
def f089vol_f089_volume_liquidity_context_dv_zscore_252_chg_252d_base_v150_signal(volume, closeadj):
    base = (_f089_dv(volume, closeadj) - _f089_dv(volume, closeadj).rolling(252, min_periods=63).mean()) / _f089_dv(volume, closeadj).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

