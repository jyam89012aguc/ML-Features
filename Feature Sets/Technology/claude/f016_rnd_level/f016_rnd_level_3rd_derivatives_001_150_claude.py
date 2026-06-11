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
def _f016_rnd_log(rnd):
    return np.log(rnd.abs().replace(0, np.nan))


def _f016_rnd_per_share(rnd, sharesbas):
    return rnd / sharesbas.replace(0, np.nan).abs()


# 21d acceleration of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accel_21d_3d_v001_signal(rnd, closeadj):
    base = rnd
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accel_63d_3d_v002_signal(rnd, closeadj):
    base = rnd
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accel_126d_3d_v003_signal(rnd, closeadj):
    base = rnd
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accel_252d_3d_v004_signal(rnd, closeadj):
    base = rnd
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accel_21d_3d_v005_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accel_63d_3d_v006_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accel_126d_3d_v007_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accel_252d_3d_v008_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accel_21d_3d_v009_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accel_63d_3d_v010_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accel_126d_3d_v011_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accel_252d_3d_v012_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accel_21d_3d_v013_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accel_63d_3d_v014_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accel_126d_3d_v015_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accel_252d_3d_v016_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accel_21d_3d_v017_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accel_63d_3d_v018_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accel_126d_3d_v019_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accel_252d_3d_v020_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accel_21d_3d_v021_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accel_63d_3d_v022_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accel_126d_3d_v023_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accel_252d_3d_v024_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accel_21d_3d_v025_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accel_63d_3d_v026_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accel_126d_3d_v027_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accel_252d_3d_v028_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accel_21d_3d_v029_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accel_63d_3d_v030_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accel_126d_3d_v031_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accel_252d_3d_v032_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accel_21d_3d_v033_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accel_63d_3d_v034_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accel_126d_3d_v035_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accel_252d_3d_v036_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accel_21d_3d_v037_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accel_63d_3d_v038_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accel_126d_3d_v039_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accel_252d_3d_v040_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accel_21d_3d_v045_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accel_63d_3d_v046_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accel_126d_3d_v047_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accel_252d_3d_v048_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accel_21d_3d_v049_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accel_63d_3d_v050_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accel_126d_3d_v051_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accel_252d_3d_v052_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_slopez_21d_z126_3d_v053_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_slopez_63d_z252_3d_v054_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_slopez_126d_z252_3d_v055_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_slopez_252d_z504_3d_v056_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_slopez_21d_z126_3d_v057_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_slopez_63d_z252_3d_v058_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_slopez_126d_z252_3d_v059_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_slopez_252d_z504_3d_v060_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_slopez_21d_z126_3d_v061_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_slopez_63d_z252_3d_v062_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_slopez_126d_z252_3d_v063_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_slopez_252d_z504_3d_v064_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_slopez_21d_z126_3d_v065_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_slopez_63d_z252_3d_v066_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_slopez_126d_z252_3d_v067_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_slopez_252d_z504_3d_v068_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_slopez_21d_z126_3d_v069_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_slopez_63d_z252_3d_v070_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_slopez_126d_z252_3d_v071_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_slopez_252d_z504_3d_v072_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_slopez_21d_z126_3d_v073_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_slopez_63d_z252_3d_v074_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_slopez_126d_z252_3d_v075_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_slopez_252d_z504_3d_v076_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_slopez_21d_z126_3d_v077_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_slopez_63d_z252_3d_v078_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_slopez_126d_z252_3d_v079_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_slopez_252d_z504_3d_v080_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_slopez_21d_z126_3d_v081_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_slopez_63d_z252_3d_v082_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_slopez_126d_z252_3d_v083_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_slopez_252d_z504_3d_v084_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_slopez_21d_z126_3d_v085_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_slopez_63d_z252_3d_v086_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_slopez_126d_z252_3d_v087_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_slopez_252d_z504_3d_v088_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_slopez_21d_z126_3d_v089_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_slopez_63d_z252_3d_v090_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_slopez_126d_z252_3d_v091_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_slopez_252d_z504_3d_v092_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_jerk_21d_3d_v105_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_jerk_63d_3d_v106_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_jerk_126d_3d_v107_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_rnd
def f016rdl_f016_rnd_level_log_rnd_jerk_21d_3d_v108_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_rnd
def f016rdl_f016_rnd_level_log_rnd_jerk_63d_3d_v109_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_rnd
def f016rdl_f016_rnd_level_log_rnd_jerk_126d_3d_v110_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_jerk_21d_3d_v111_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_jerk_63d_3d_v112_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_jerk_126d_3d_v113_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_jerk_21d_3d_v114_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_jerk_63d_3d_v115_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_jerk_126d_3d_v116_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_jerk_21d_3d_v117_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_jerk_63d_3d_v118_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_jerk_126d_3d_v119_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_jerk_21d_3d_v120_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_jerk_63d_3d_v121_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_jerk_126d_3d_v122_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_jerk_21d_3d_v123_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_jerk_63d_3d_v124_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_jerk_126d_3d_v125_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_jerk_21d_3d_v126_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_jerk_63d_3d_v127_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_jerk_126d_3d_v128_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_jerk_21d_3d_v129_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_jerk_63d_3d_v130_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_jerk_126d_3d_v131_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_jerk_21d_3d_v132_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_jerk_63d_3d_v133_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_jerk_126d_3d_v134_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_jerk_21d_3d_v138_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_jerk_63d_3d_v139_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_jerk_126d_3d_v140_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_jerk_21d_3d_v141_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_jerk_63d_3d_v142_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_jerk_126d_3d_v143_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_lvl smoothed over 252d
def f016rdl_f016_rnd_level_rnd_lvl_smoothaccel_63d_sm252_3d_v144_signal(rnd, closeadj):
    base = rnd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_lvl smoothed over 504d
def f016rdl_f016_rnd_level_rnd_lvl_smoothaccel_252d_sm504_3d_v145_signal(rnd, closeadj):
    base = rnd
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_rnd smoothed over 252d
def f016rdl_f016_rnd_level_log_rnd_smoothaccel_63d_sm252_3d_v146_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_rnd smoothed over 504d
def f016rdl_f016_rnd_level_log_rnd_smoothaccel_252d_sm504_3d_v147_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_per_share smoothed over 252d
def f016rdl_f016_rnd_level_rnd_per_share_smoothaccel_63d_sm252_3d_v148_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_per_share smoothed over 504d
def f016rdl_f016_rnd_level_rnd_per_share_smoothaccel_252d_sm504_3d_v149_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_per_dilshare smoothed over 252d
def f016rdl_f016_rnd_level_rnd_per_dilshare_smoothaccel_63d_sm252_3d_v150_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_per_dilshare smoothed over 504d
def f016rdl_f016_rnd_level_rnd_per_dilshare_smoothaccel_252d_sm504_3d_v151_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_log_expand smoothed over 252d
def f016rdl_f016_rnd_level_rnd_log_expand_smoothaccel_63d_sm252_3d_v152_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_log_expand smoothed over 504d
def f016rdl_f016_rnd_level_rnd_log_expand_smoothaccel_252d_sm504_3d_v153_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_log_minus_5y smoothed over 252d
def f016rdl_f016_rnd_level_rnd_log_minus_5y_smoothaccel_63d_sm252_3d_v154_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_log_minus_5y smoothed over 504d
def f016rdl_f016_rnd_level_rnd_log_minus_5y_smoothaccel_252d_sm504_3d_v155_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_yoy_log smoothed over 252d
def f016rdl_f016_rnd_level_rnd_yoy_log_smoothaccel_63d_sm252_3d_v156_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_yoy_log smoothed over 504d
def f016rdl_f016_rnd_level_rnd_yoy_log_smoothaccel_252d_sm504_3d_v157_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_sector_dist smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_sector_dist smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_sector_z smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_sector_z smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_industry_dist smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_industry_dist smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_mcap_bucket_dist smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_mcap_bucket_dist smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_sector_pctile smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_sector_pctile smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_peer_industry_pctile smoothed over 252d
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_peer_industry_pctile smoothed over 504d
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accelz_21d_z252_3d_v170_signal(rnd, closeadj):
    base = rnd
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_accelz_63d_z504_3d_v171_signal(rnd, closeadj):
    base = rnd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accelz_21d_z252_3d_v172_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_rnd
def f016rdl_f016_rnd_level_log_rnd_accelz_63d_z504_3d_v173_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accelz_21d_z252_3d_v174_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_accelz_63d_z504_3d_v175_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accelz_21d_z252_3d_v176_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_accelz_63d_z504_3d_v177_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accelz_21d_z252_3d_v178_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_accelz_63d_z504_3d_v179_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accelz_21d_z252_3d_v180_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_accelz_63d_z504_3d_v181_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accelz_21d_z252_3d_v182_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_accelz_63d_z504_3d_v183_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accelz_21d_z252_3d_v184_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_accelz_63d_z504_3d_v185_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accelz_21d_z252_3d_v186_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_accelz_63d_z504_3d_v187_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accelz_21d_z252_3d_v188_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_accelz_63d_z504_3d_v189_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_peer_industry_pctile
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_lvl (raw count, no price scaling)
def f016rdl_f016_rnd_level_rnd_lvl_signflip_63d_3d_v196_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_lvl (raw count, no price scaling)
def f016rdl_f016_rnd_level_rnd_lvl_signflip_252d_3d_v197_signal(rnd, closeadj):
    base = rnd
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_rnd (raw count, no price scaling)
def f016rdl_f016_rnd_level_log_rnd_signflip_63d_3d_v198_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_rnd (raw count, no price scaling)
def f016rdl_f016_rnd_level_log_rnd_signflip_252d_3d_v199_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_per_share (raw count, no price scaling)
def f016rdl_f016_rnd_level_rnd_per_share_signflip_63d_3d_v200_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

