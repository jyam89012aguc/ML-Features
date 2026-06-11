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
def _f069_evs(ev, revenue):
    return ev / revenue.abs().replace(0, np.nan)


# 21d mean of ev_sales scaled by closeadj
def f069evs_f069_ev_sales_valuation_ev_sales_mean_21d_base_v001_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_sales scaled by closeadj
def f069evs_f069_ev_sales_valuation_ev_sales_mean_63d_base_v002_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_sales scaled by closeadj
def f069evs_f069_ev_sales_valuation_ev_sales_mean_126d_base_v003_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_sales scaled by closeadj
def f069evs_f069_ev_sales_valuation_ev_sales_mean_252d_base_v004_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_sales scaled by closeadj
def f069evs_f069_ev_sales_valuation_ev_sales_mean_504d_base_v005_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ps_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps_lvl_mean_21d_base_v006_signal(ps, closeadj):
    base = ps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ps_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps_lvl_mean_63d_base_v007_signal(ps, closeadj):
    base = ps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ps_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps_lvl_mean_126d_base_v008_signal(ps, closeadj):
    base = ps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ps_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps_lvl_mean_252d_base_v009_signal(ps, closeadj):
    base = ps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ps_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps_lvl_mean_504d_base_v010_signal(ps, closeadj):
    base = ps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ps1_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps1_lvl_mean_21d_base_v011_signal(ps1, closeadj):
    base = ps1
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ps1_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps1_lvl_mean_63d_base_v012_signal(ps1, closeadj):
    base = ps1
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ps1_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps1_lvl_mean_126d_base_v013_signal(ps1, closeadj):
    base = ps1
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ps1_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps1_lvl_mean_252d_base_v014_signal(ps1, closeadj):
    base = ps1
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ps1_lvl scaled by closeadj
def f069evs_f069_ev_sales_valuation_ps1_lvl_mean_504d_base_v015_signal(ps1, closeadj):
    base = ps1
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_to_rev scaled by closeadj
def f069evs_f069_ev_sales_valuation_mcap_to_rev_mean_21d_base_v016_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_to_rev scaled by closeadj
def f069evs_f069_ev_sales_valuation_mcap_to_rev_mean_63d_base_v017_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_to_rev scaled by closeadj
def f069evs_f069_ev_sales_valuation_mcap_to_rev_mean_126d_base_v018_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_to_rev scaled by closeadj
def f069evs_f069_ev_sales_valuation_mcap_to_rev_mean_252d_base_v019_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_to_rev scaled by closeadj
def f069evs_f069_ev_sales_valuation_mcap_to_rev_mean_504d_base_v020_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evsales_yoy_chg scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_mean_21d_base_v021_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evsales_yoy_chg scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_mean_63d_base_v022_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evsales_yoy_chg scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_mean_126d_base_v023_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evsales_yoy_chg scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_mean_252d_base_v024_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evsales_yoy_chg scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_mean_504d_base_v025_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sales_yield scaled by closeadj
def f069evs_f069_ev_sales_valuation_sales_yield_mean_21d_base_v026_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sales_yield scaled by closeadj
def f069evs_f069_ev_sales_valuation_sales_yield_mean_63d_base_v027_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sales_yield scaled by closeadj
def f069evs_f069_ev_sales_valuation_sales_yield_mean_126d_base_v028_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sales_yield scaled by closeadj
def f069evs_f069_ev_sales_valuation_sales_yield_mean_252d_base_v029_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sales_yield scaled by closeadj
def f069evs_f069_ev_sales_valuation_sales_yield_mean_504d_base_v030_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evsales_vol_252 scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_vol_252_mean_21d_base_v031_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evsales_vol_252 scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_vol_252_mean_63d_base_v032_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evsales_vol_252 scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_vol_252_mean_126d_base_v033_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evsales_vol_252 scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_vol_252_mean_252d_base_v034_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evsales_vol_252 scaled by closeadj
def f069evs_f069_ev_sales_valuation_evsales_vol_252_mean_504d_base_v035_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_sector_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_mean_21d_base_v036_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_sector_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_mean_63d_base_v037_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_sector_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_mean_126d_base_v038_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_sector_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_mean_252d_base_v039_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_sector_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_mean_504d_base_v040_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_sector_z scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_mean_21d_base_v041_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_sector_z scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_mean_63d_base_v042_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_sector_z scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_mean_126d_base_v043_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_sector_z scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_mean_252d_base_v044_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_sector_z scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_mean_504d_base_v045_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_industry_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_mean_21d_base_v046_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_industry_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_mean_63d_base_v047_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_industry_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_mean_126d_base_v048_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_industry_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_mean_252d_base_v049_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_industry_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_mean_504d_base_v050_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_mcap_bucket_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_mean_21d_base_v051_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_mcap_bucket_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_mean_63d_base_v052_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_mcap_bucket_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_mean_126d_base_v053_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_mcap_bucket_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_mean_252d_base_v054_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_mcap_bucket_dist scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_mean_504d_base_v055_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_sector_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_mean_21d_base_v056_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_sector_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_mean_63d_base_v057_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_sector_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_mean_126d_base_v058_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_sector_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_mean_252d_base_v059_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_sector_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_mean_504d_base_v060_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evs_peer_industry_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_mean_21d_base_v061_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evs_peer_industry_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_mean_63d_base_v062_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evs_peer_industry_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_mean_126d_base_v063_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evs_peer_industry_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_mean_252d_base_v064_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evs_peer_industry_pctile scaled by closeadj
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_mean_504d_base_v065_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_median_63d_base_v066_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_median_252d_base_v067_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_median_504d_base_v068_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_median_63d_base_v069_signal(ps, closeadj):
    base = ps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_median_252d_base_v070_signal(ps, closeadj):
    base = ps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_median_504d_base_v071_signal(ps, closeadj):
    base = ps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_median_63d_base_v072_signal(ps1, closeadj):
    base = ps1
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_median_252d_base_v073_signal(ps1, closeadj):
    base = ps1
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_median_504d_base_v074_signal(ps1, closeadj):
    base = ps1
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_median_63d_base_v075_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_median_252d_base_v076_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_median_504d_base_v077_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_median_63d_base_v078_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_median_252d_base_v079_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_median_504d_base_v080_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_median_63d_base_v081_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_median_252d_base_v082_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_median_504d_base_v083_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_median_63d_base_v084_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_median_252d_base_v085_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_median_504d_base_v086_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_median_63d_base_v087_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_median_252d_base_v088_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_median_504d_base_v089_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_median_63d_base_v090_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_median_252d_base_v091_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_median_504d_base_v092_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_median_63d_base_v093_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_median_252d_base_v094_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_median_504d_base_v095_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_median_63d_base_v096_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_median_252d_base_v097_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_median_504d_base_v098_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_median_63d_base_v099_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_median_252d_base_v100_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

