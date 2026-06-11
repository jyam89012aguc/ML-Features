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
def _f069_evs(ev, revenue):
    return ev / revenue.abs().replace(0, np.nan)


# 21d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slope_21d_2d_v001_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slope_63d_2d_v002_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slope_126d_2d_v003_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slope_252d_2d_v004_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slope_504d_2d_v005_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slope_21d_2d_v006_signal(ps, closeadj):
    base = ps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slope_63d_2d_v007_signal(ps, closeadj):
    base = ps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slope_126d_2d_v008_signal(ps, closeadj):
    base = ps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slope_252d_2d_v009_signal(ps, closeadj):
    base = ps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slope_504d_2d_v010_signal(ps, closeadj):
    base = ps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slope_21d_2d_v011_signal(ps1, closeadj):
    base = ps1
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slope_63d_2d_v012_signal(ps1, closeadj):
    base = ps1
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slope_126d_2d_v013_signal(ps1, closeadj):
    base = ps1
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slope_252d_2d_v014_signal(ps1, closeadj):
    base = ps1
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slope_504d_2d_v015_signal(ps1, closeadj):
    base = ps1
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slope_21d_2d_v016_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slope_63d_2d_v017_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slope_126d_2d_v018_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slope_252d_2d_v019_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slope_504d_2d_v020_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slope_21d_2d_v021_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slope_63d_2d_v022_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slope_126d_2d_v023_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slope_252d_2d_v024_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slope_504d_2d_v025_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slope_21d_2d_v026_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slope_63d_2d_v027_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slope_126d_2d_v028_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slope_252d_2d_v029_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slope_504d_2d_v030_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slope_21d_2d_v031_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slope_63d_2d_v032_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slope_126d_2d_v033_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slope_252d_2d_v034_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slope_504d_2d_v035_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slope_21d_2d_v036_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slope_63d_2d_v037_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slope_126d_2d_v038_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slope_252d_2d_v039_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slope_504d_2d_v040_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slope_21d_2d_v041_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slope_63d_2d_v042_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slope_126d_2d_v043_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slope_252d_2d_v044_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slope_504d_2d_v045_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slope_21d_2d_v046_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slope_63d_2d_v047_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slope_126d_2d_v048_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slope_252d_2d_v049_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slope_504d_2d_v050_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slope_21d_2d_v056_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slope_63d_2d_v057_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slope_126d_2d_v058_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slope_252d_2d_v059_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slope_504d_2d_v060_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slope_21d_2d_v061_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slope_63d_2d_v062_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slope_126d_2d_v063_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slope_252d_2d_v064_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slope_504d_2d_v065_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sm21_sl21_2d_v066_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sm63_sl21_2d_v067_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sm63_sl63_2d_v068_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sm252_sl63_2d_v069_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sm252_sl126_2d_v070_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sm21_sl21_2d_v071_signal(ps, closeadj):
    base = _mean(ps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sm63_sl21_2d_v072_signal(ps, closeadj):
    base = _mean(ps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sm63_sl63_2d_v073_signal(ps, closeadj):
    base = _mean(ps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sm252_sl63_2d_v074_signal(ps, closeadj):
    base = _mean(ps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sm252_sl126_2d_v075_signal(ps, closeadj):
    base = _mean(ps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sm21_sl21_2d_v076_signal(ps1, closeadj):
    base = _mean(ps1, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sm63_sl21_2d_v077_signal(ps1, closeadj):
    base = _mean(ps1, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sm63_sl63_2d_v078_signal(ps1, closeadj):
    base = _mean(ps1, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sm252_sl63_2d_v079_signal(ps1, closeadj):
    base = _mean(ps1, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sm252_sl126_2d_v080_signal(ps1, closeadj):
    base = _mean(ps1, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sm21_sl21_2d_v081_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sm63_sl21_2d_v082_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sm63_sl63_2d_v083_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sm252_sl63_2d_v084_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sm252_sl126_2d_v085_signal(marketcap, revenue, closeadj):
    base = _mean(marketcap / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sm21_sl21_2d_v086_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sm63_sl21_2d_v087_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sm63_sl63_2d_v088_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sm252_sl63_2d_v089_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sm252_sl126_2d_v090_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sm21_sl21_2d_v091_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sm63_sl21_2d_v092_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sm63_sl63_2d_v093_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sm252_sl63_2d_v094_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sm252_sl126_2d_v095_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sm21_sl21_2d_v096_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sm63_sl21_2d_v097_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sm63_sl63_2d_v098_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sm252_sl63_2d_v099_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sm252_sl126_2d_v100_signal(ev, revenue, closeadj):
    base = _mean(_f069_evs(ev, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sm21_sl21_2d_v101_signal(ev, revenue, evs_sector_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sm63_sl21_2d_v102_signal(ev, revenue, evs_sector_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sm63_sl63_2d_v103_signal(ev, revenue, evs_sector_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sm252_sl63_2d_v104_signal(ev, revenue, evs_sector_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sm252_sl126_2d_v105_signal(ev, revenue, evs_sector_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sm21_sl21_2d_v106_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sm63_sl21_2d_v107_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sm63_sl63_2d_v108_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sm252_sl63_2d_v109_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sm252_sl126_2d_v110_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sm21_sl21_2d_v111_signal(ev, revenue, evs_industry_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sm63_sl21_2d_v112_signal(ev, revenue, evs_industry_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sm63_sl63_2d_v113_signal(ev, revenue, evs_industry_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sm252_sl63_2d_v114_signal(ev, revenue, evs_industry_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sm252_sl126_2d_v115_signal(ev, revenue, evs_industry_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(ev, revenue, evs_mcap_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(ev, revenue, evs_mcap_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(ev, revenue, evs_mcap_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(ev, revenue, evs_mcap_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(ev, revenue, evs_mcap_med, closeadj):
    base = _mean((_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_sm21_sl21_2d_v121_signal(evs_sector_pctile, closeadj):
    base = _mean(evs_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_sm63_sl21_2d_v122_signal(evs_sector_pctile, closeadj):
    base = _mean(evs_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_sm63_sl63_2d_v123_signal(evs_sector_pctile, closeadj):
    base = _mean(evs_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_sm252_sl63_2d_v124_signal(evs_sector_pctile, closeadj):
    base = _mean(evs_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_sm252_sl126_2d_v125_signal(evs_sector_pctile, closeadj):
    base = _mean(evs_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_sm21_sl21_2d_v126_signal(evs_industry_pctile, closeadj):
    base = _mean(evs_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_sm63_sl21_2d_v127_signal(evs_industry_pctile, closeadj):
    base = _mean(evs_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_sm63_sl63_2d_v128_signal(evs_industry_pctile, closeadj):
    base = _mean(evs_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_sm252_sl63_2d_v129_signal(evs_industry_pctile, closeadj):
    base = _mean(evs_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_sm252_sl126_2d_v130_signal(evs_industry_pctile, closeadj):
    base = _mean(evs_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_pctslope_21d_2d_v131_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_pctslope_63d_2d_v132_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_pctslope_252d_2d_v133_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_pctslope_21d_2d_v134_signal(ps, closeadj):
    base = ps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_pctslope_63d_2d_v135_signal(ps, closeadj):
    base = ps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_pctslope_252d_2d_v136_signal(ps, closeadj):
    base = ps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_pctslope_21d_2d_v137_signal(ps1, closeadj):
    base = ps1
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_pctslope_63d_2d_v138_signal(ps1, closeadj):
    base = ps1
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_pctslope_252d_2d_v139_signal(ps1, closeadj):
    base = ps1
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_pctslope_21d_2d_v140_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_pctslope_63d_2d_v141_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_pctslope_252d_2d_v142_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_pctslope_21d_2d_v143_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_pctslope_63d_2d_v144_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_pctslope_252d_2d_v145_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_pctslope_21d_2d_v146_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_pctslope_63d_2d_v147_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_pctslope_252d_2d_v148_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_pctslope_21d_2d_v149_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_pctslope_63d_2d_v150_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_pctslope_252d_2d_v151_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_pctslope_21d_2d_v152_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_pctslope_63d_2d_v153_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_pctslope_252d_2d_v154_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_pctslope_21d_2d_v155_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_pctslope_63d_2d_v156_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_pctslope_252d_2d_v157_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_pctslope_21d_2d_v158_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_pctslope_63d_2d_v159_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_pctslope_252d_2d_v160_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_pctslope_21d_2d_v164_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_pctslope_63d_2d_v165_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_pctslope_252d_2d_v166_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_pctslope_21d_2d_v167_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_pctslope_63d_2d_v168_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_pctslope_252d_2d_v169_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sgnslope_21d_2d_v170_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sgnslope_63d_2d_v171_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_sgnslope_252d_2d_v172_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sgnslope_21d_2d_v173_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sgnslope_63d_2d_v174_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_sgnslope_252d_2d_v175_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sgnslope_21d_2d_v176_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sgnslope_63d_2d_v177_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_sgnslope_252d_2d_v178_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sgnslope_21d_2d_v179_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sgnslope_63d_2d_v180_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_sgnslope_252d_2d_v181_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sgnslope_21d_2d_v182_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sgnslope_63d_2d_v183_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_sgnslope_252d_2d_v184_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sgnslope_21d_2d_v185_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sgnslope_63d_2d_v186_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_sgnslope_252d_2d_v187_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sgnslope_21d_2d_v188_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sgnslope_63d_2d_v189_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_sgnslope_252d_2d_v190_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sgnslope_21d_2d_v191_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sgnslope_63d_2d_v192_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_sgnslope_252d_2d_v193_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sgnslope_21d_2d_v194_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sgnslope_63d_2d_v195_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_sgnslope_252d_2d_v196_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sgnslope_21d_2d_v197_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sgnslope_63d_2d_v198_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_sgnslope_252d_2d_v199_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

