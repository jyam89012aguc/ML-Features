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
def _f053_ebm(ebitda, revenue):
    return ebitda / revenue.abs().replace(0, np.nan)


# 21d mean of ebitda_margin_calc scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_mean_21d_base_v001_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_margin_calc scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_mean_63d_base_v002_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_margin_calc scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_mean_126d_base_v003_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_margin_calc scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_mean_252d_base_v004_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_margin_calc scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_mean_504d_base_v005_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitdamargin scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitdamargin_mean_21d_base_v006_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitdamargin scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitdamargin_mean_63d_base_v007_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitdamargin scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitdamargin_mean_126d_base_v008_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitdamargin scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitdamargin_mean_252d_base_v009_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitdamargin scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitdamargin_mean_504d_base_v010_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_lvl scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_lvl_mean_21d_base_v011_signal(ebitda, closeadj):
    base = ebitda
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_lvl scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_lvl_mean_63d_base_v012_signal(ebitda, closeadj):
    base = ebitda
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_lvl scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_lvl_mean_126d_base_v013_signal(ebitda, closeadj):
    base = ebitda
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_lvl scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_lvl_mean_252d_base_v014_signal(ebitda, closeadj):
    base = ebitda
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_lvl scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_lvl_mean_504d_base_v015_signal(ebitda, closeadj):
    base = ebitda
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_growth scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_growth_mean_21d_base_v016_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_growth scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_growth_mean_63d_base_v017_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_growth scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_growth_mean_126d_base_v018_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_growth scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_growth_mean_252d_base_v019_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_growth scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_growth_mean_504d_base_v020_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_to_fcf scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_mean_21d_base_v021_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_to_fcf scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_mean_63d_base_v022_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_to_fcf scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_mean_126d_base_v023_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_to_fcf scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_mean_252d_base_v024_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_to_fcf scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_mean_504d_base_v025_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_to_asset scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_asset_mean_21d_base_v026_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_to_asset scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_asset_mean_63d_base_v027_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_to_asset scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_asset_mean_126d_base_v028_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_to_asset scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_asset_mean_252d_base_v029_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_to_asset scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_to_asset_mean_504d_base_v030_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebitda_yoy_chg scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_mean_21d_base_v031_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebitda_yoy_chg scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_mean_63d_base_v032_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebitda_yoy_chg scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_mean_126d_base_v033_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebitda_yoy_chg scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_mean_252d_base_v034_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebitda_yoy_chg scaled by closeadj
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_mean_504d_base_v035_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_sector_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_mean_21d_base_v036_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_sector_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_mean_63d_base_v037_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_sector_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_mean_126d_base_v038_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_sector_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_mean_252d_base_v039_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_sector_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_mean_504d_base_v040_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_sector_z scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_mean_21d_base_v041_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_sector_z scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_mean_63d_base_v042_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_sector_z scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_mean_126d_base_v043_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_sector_z scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_mean_252d_base_v044_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_sector_z scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_mean_504d_base_v045_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_industry_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_mean_21d_base_v046_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_industry_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_mean_63d_base_v047_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_industry_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_mean_126d_base_v048_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_industry_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_mean_252d_base_v049_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_industry_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_mean_504d_base_v050_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_mcap_bucket_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_mean_21d_base_v051_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_mcap_bucket_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_mean_63d_base_v052_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_mcap_bucket_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_mean_126d_base_v053_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_mcap_bucket_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_mean_252d_base_v054_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_mcap_bucket_dist scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_mean_504d_base_v055_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_sector_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_mean_21d_base_v056_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_sector_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_mean_63d_base_v057_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_sector_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_mean_126d_base_v058_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_sector_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_mean_252d_base_v059_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_sector_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_mean_504d_base_v060_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ebm_peer_industry_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_mean_21d_base_v061_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ebm_peer_industry_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_mean_63d_base_v062_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ebm_peer_industry_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_mean_126d_base_v063_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ebm_peer_industry_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_mean_252d_base_v064_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ebm_peer_industry_pctile scaled by closeadj
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_mean_504d_base_v065_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_median_63d_base_v066_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_median_252d_base_v067_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_median_504d_base_v068_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_median_63d_base_v069_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_median_252d_base_v070_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_median_504d_base_v071_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_median_63d_base_v072_signal(ebitda, closeadj):
    base = ebitda
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_median_252d_base_v073_signal(ebitda, closeadj):
    base = ebitda
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_median_504d_base_v074_signal(ebitda, closeadj):
    base = ebitda
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_median_63d_base_v075_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_median_252d_base_v076_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_median_504d_base_v077_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_median_63d_base_v078_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_median_252d_base_v079_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_median_504d_base_v080_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_median_63d_base_v081_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_median_252d_base_v082_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_median_504d_base_v083_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_median_63d_base_v084_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_median_252d_base_v085_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_median_504d_base_v086_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_median_63d_base_v087_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_median_252d_base_v088_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_median_504d_base_v089_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_median_63d_base_v090_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_median_252d_base_v091_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_median_504d_base_v092_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_median_63d_base_v093_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_median_252d_base_v094_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_median_504d_base_v095_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_median_63d_base_v096_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_median_252d_base_v097_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_median_504d_base_v098_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_median_63d_base_v099_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_median_252d_base_v100_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

