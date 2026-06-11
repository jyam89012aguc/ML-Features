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
def _f016_rnd_log(rnd):
    return np.log(rnd.abs().replace(0, np.nan))


def _f016_rnd_per_share(rnd, sharesbas):
    return rnd / sharesbas.replace(0, np.nan).abs()


# 21d mean of rnd_lvl scaled by closeadj
def f016rdl_f016_rnd_level_rnd_lvl_mean_21d_base_v001_signal(rnd, closeadj):
    base = rnd
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_lvl scaled by closeadj
def f016rdl_f016_rnd_level_rnd_lvl_mean_63d_base_v002_signal(rnd, closeadj):
    base = rnd
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_lvl scaled by closeadj
def f016rdl_f016_rnd_level_rnd_lvl_mean_126d_base_v003_signal(rnd, closeadj):
    base = rnd
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_lvl scaled by closeadj
def f016rdl_f016_rnd_level_rnd_lvl_mean_252d_base_v004_signal(rnd, closeadj):
    base = rnd
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_lvl scaled by closeadj
def f016rdl_f016_rnd_level_rnd_lvl_mean_504d_base_v005_signal(rnd, closeadj):
    base = rnd
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_rnd scaled by closeadj
def f016rdl_f016_rnd_level_log_rnd_mean_21d_base_v006_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_rnd scaled by closeadj
def f016rdl_f016_rnd_level_log_rnd_mean_63d_base_v007_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_rnd scaled by closeadj
def f016rdl_f016_rnd_level_log_rnd_mean_126d_base_v008_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_rnd scaled by closeadj
def f016rdl_f016_rnd_level_log_rnd_mean_252d_base_v009_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_rnd scaled by closeadj
def f016rdl_f016_rnd_level_log_rnd_mean_504d_base_v010_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_per_share scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_share_mean_21d_base_v011_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_per_share scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_share_mean_63d_base_v012_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_per_share scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_share_mean_126d_base_v013_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_per_share scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_share_mean_252d_base_v014_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_per_share scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_share_mean_504d_base_v015_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_per_dilshare scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_dilshare_mean_21d_base_v016_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_per_dilshare scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_dilshare_mean_63d_base_v017_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_per_dilshare scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_dilshare_mean_126d_base_v018_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_per_dilshare scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_dilshare_mean_252d_base_v019_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_per_dilshare scaled by closeadj
def f016rdl_f016_rnd_level_rnd_per_dilshare_mean_504d_base_v020_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_log_expand scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_expand_mean_21d_base_v021_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_log_expand scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_expand_mean_63d_base_v022_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_log_expand scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_expand_mean_126d_base_v023_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_log_expand scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_expand_mean_252d_base_v024_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_log_expand scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_expand_mean_504d_base_v025_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_log_minus_5y scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_minus_5y_mean_21d_base_v026_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_log_minus_5y scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_minus_5y_mean_63d_base_v027_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_log_minus_5y scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_minus_5y_mean_126d_base_v028_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_log_minus_5y scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_minus_5y_mean_252d_base_v029_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_log_minus_5y scaled by closeadj
def f016rdl_f016_rnd_level_rnd_log_minus_5y_mean_504d_base_v030_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_yoy_log scaled by closeadj
def f016rdl_f016_rnd_level_rnd_yoy_log_mean_21d_base_v031_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_yoy_log scaled by closeadj
def f016rdl_f016_rnd_level_rnd_yoy_log_mean_63d_base_v032_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_yoy_log scaled by closeadj
def f016rdl_f016_rnd_level_rnd_yoy_log_mean_126d_base_v033_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_yoy_log scaled by closeadj
def f016rdl_f016_rnd_level_rnd_yoy_log_mean_252d_base_v034_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_yoy_log scaled by closeadj
def f016rdl_f016_rnd_level_rnd_yoy_log_mean_504d_base_v035_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_sector_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_mean_21d_base_v036_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_sector_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_mean_63d_base_v037_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_sector_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_mean_126d_base_v038_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_sector_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_mean_252d_base_v039_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_sector_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_mean_504d_base_v040_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_sector_z scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_z_mean_21d_base_v041_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_sector_z scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_z_mean_63d_base_v042_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_sector_z scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_z_mean_126d_base_v043_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_sector_z scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_z_mean_252d_base_v044_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_sector_z scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_z_mean_504d_base_v045_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_industry_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_mean_21d_base_v046_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_industry_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_mean_63d_base_v047_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_industry_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_mean_126d_base_v048_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_industry_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_mean_252d_base_v049_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_industry_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_mean_504d_base_v050_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_mcap_bucket_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_mean_21d_base_v051_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_mcap_bucket_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_mean_63d_base_v052_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_mcap_bucket_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_mean_126d_base_v053_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_mcap_bucket_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_mean_252d_base_v054_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_mcap_bucket_dist scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_mean_504d_base_v055_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_sector_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_mean_21d_base_v056_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_sector_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_mean_63d_base_v057_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_sector_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_mean_126d_base_v058_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_sector_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_mean_252d_base_v059_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_sector_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_mean_504d_base_v060_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_peer_industry_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_mean_21d_base_v061_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_peer_industry_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_mean_63d_base_v062_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_peer_industry_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_mean_126d_base_v063_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_peer_industry_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_mean_252d_base_v064_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_peer_industry_pctile scaled by closeadj
def f016rdl_f016_rnd_level_rnd_peer_industry_pctile_mean_504d_base_v065_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_median_63d_base_v066_signal(rnd, closeadj):
    base = rnd
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_median_252d_base_v067_signal(rnd, closeadj):
    base = rnd
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_lvl
def f016rdl_f016_rnd_level_rnd_lvl_median_504d_base_v068_signal(rnd, closeadj):
    base = rnd
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_rnd
def f016rdl_f016_rnd_level_log_rnd_median_63d_base_v069_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_rnd
def f016rdl_f016_rnd_level_log_rnd_median_252d_base_v070_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_rnd
def f016rdl_f016_rnd_level_log_rnd_median_504d_base_v071_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_median_63d_base_v072_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_median_252d_base_v073_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_per_share
def f016rdl_f016_rnd_level_rnd_per_share_median_504d_base_v074_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_median_63d_base_v075_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_median_252d_base_v076_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_per_dilshare
def f016rdl_f016_rnd_level_rnd_per_dilshare_median_504d_base_v077_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_median_63d_base_v078_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_median_252d_base_v079_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_log_expand
def f016rdl_f016_rnd_level_rnd_log_expand_median_504d_base_v080_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_median_63d_base_v081_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_median_252d_base_v082_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_log_minus_5y
def f016rdl_f016_rnd_level_rnd_log_minus_5y_median_504d_base_v083_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_median_63d_base_v084_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_median_252d_base_v085_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_yoy_log
def f016rdl_f016_rnd_level_rnd_yoy_log_median_504d_base_v086_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_median_63d_base_v087_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_median_252d_base_v088_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_peer_sector_dist
def f016rdl_f016_rnd_level_rnd_peer_sector_dist_median_504d_base_v089_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_median_63d_base_v090_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_median_252d_base_v091_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_peer_sector_z
def f016rdl_f016_rnd_level_rnd_peer_sector_z_median_504d_base_v092_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_median_63d_base_v093_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_median_252d_base_v094_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_peer_industry_dist
def f016rdl_f016_rnd_level_rnd_peer_industry_dist_median_504d_base_v095_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_median_63d_base_v096_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_median_252d_base_v097_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_peer_mcap_bucket_dist
def f016rdl_f016_rnd_level_rnd_peer_mcap_bucket_dist_median_504d_base_v098_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_median_63d_base_v099_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_peer_sector_pctile
def f016rdl_f016_rnd_level_rnd_peer_sector_pctile_median_252d_base_v100_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

