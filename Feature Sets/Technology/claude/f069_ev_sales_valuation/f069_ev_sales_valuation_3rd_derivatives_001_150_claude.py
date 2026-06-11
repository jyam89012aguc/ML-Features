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


# 21d acceleration of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accel_21d_3d_v001_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accel_63d_3d_v002_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accel_126d_3d_v003_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accel_252d_3d_v004_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accel_21d_3d_v005_signal(ps, closeadj):
    base = ps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accel_63d_3d_v006_signal(ps, closeadj):
    base = ps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accel_126d_3d_v007_signal(ps, closeadj):
    base = ps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accel_252d_3d_v008_signal(ps, closeadj):
    base = ps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accel_21d_3d_v009_signal(ps1, closeadj):
    base = ps1
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accel_63d_3d_v010_signal(ps1, closeadj):
    base = ps1
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accel_126d_3d_v011_signal(ps1, closeadj):
    base = ps1
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accel_252d_3d_v012_signal(ps1, closeadj):
    base = ps1
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accel_21d_3d_v013_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accel_63d_3d_v014_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accel_126d_3d_v015_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accel_252d_3d_v016_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accel_21d_3d_v017_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accel_63d_3d_v018_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accel_126d_3d_v019_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accel_252d_3d_v020_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accel_21d_3d_v021_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accel_63d_3d_v022_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accel_126d_3d_v023_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accel_252d_3d_v024_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accel_21d_3d_v025_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accel_63d_3d_v026_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accel_126d_3d_v027_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accel_252d_3d_v028_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accel_21d_3d_v029_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accel_63d_3d_v030_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accel_126d_3d_v031_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accel_252d_3d_v032_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accel_21d_3d_v033_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accel_63d_3d_v034_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accel_126d_3d_v035_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accel_252d_3d_v036_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accel_21d_3d_v037_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accel_63d_3d_v038_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accel_126d_3d_v039_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accel_252d_3d_v040_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accel_21d_3d_v045_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accel_63d_3d_v046_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accel_126d_3d_v047_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accel_252d_3d_v048_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accel_21d_3d_v049_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accel_63d_3d_v050_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accel_126d_3d_v051_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accel_252d_3d_v052_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slopez_21d_z126_3d_v053_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slopez_63d_z252_3d_v054_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slopez_126d_z252_3d_v055_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_slopez_252d_z504_3d_v056_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slopez_21d_z126_3d_v057_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slopez_63d_z252_3d_v058_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slopez_126d_z252_3d_v059_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_slopez_252d_z504_3d_v060_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slopez_21d_z126_3d_v061_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slopez_63d_z252_3d_v062_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slopez_126d_z252_3d_v063_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_slopez_252d_z504_3d_v064_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slopez_21d_z126_3d_v065_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slopez_63d_z252_3d_v066_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slopez_126d_z252_3d_v067_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_slopez_252d_z504_3d_v068_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slopez_21d_z126_3d_v069_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slopez_63d_z252_3d_v070_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slopez_126d_z252_3d_v071_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_slopez_252d_z504_3d_v072_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slopez_21d_z126_3d_v073_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slopez_63d_z252_3d_v074_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slopez_126d_z252_3d_v075_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_slopez_252d_z504_3d_v076_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slopez_21d_z126_3d_v077_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slopez_63d_z252_3d_v078_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slopez_126d_z252_3d_v079_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_slopez_252d_z504_3d_v080_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slopez_21d_z126_3d_v081_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slopez_63d_z252_3d_v082_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slopez_126d_z252_3d_v083_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_slopez_252d_z504_3d_v084_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slopez_21d_z126_3d_v085_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slopez_63d_z252_3d_v086_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slopez_126d_z252_3d_v087_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_slopez_252d_z504_3d_v088_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slopez_21d_z126_3d_v089_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slopez_63d_z252_3d_v090_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slopez_126d_z252_3d_v091_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_slopez_252d_z504_3d_v092_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_jerk_21d_3d_v105_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_jerk_63d_3d_v106_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_jerk_126d_3d_v107_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_jerk_21d_3d_v108_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_jerk_63d_3d_v109_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_jerk_126d_3d_v110_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_jerk_21d_3d_v111_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_jerk_63d_3d_v112_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_jerk_126d_3d_v113_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_jerk_21d_3d_v114_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_jerk_63d_3d_v115_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_jerk_126d_3d_v116_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_jerk_21d_3d_v117_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_jerk_63d_3d_v118_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_jerk_126d_3d_v119_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_jerk_21d_3d_v120_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_jerk_63d_3d_v121_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_jerk_126d_3d_v122_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_jerk_21d_3d_v123_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_jerk_63d_3d_v124_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_jerk_126d_3d_v125_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_jerk_21d_3d_v126_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_jerk_63d_3d_v127_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_jerk_126d_3d_v128_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_jerk_21d_3d_v129_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_jerk_63d_3d_v130_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_jerk_126d_3d_v131_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_jerk_21d_3d_v132_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_jerk_63d_3d_v133_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_jerk_126d_3d_v134_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_jerk_21d_3d_v138_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_jerk_63d_3d_v139_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_jerk_126d_3d_v140_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_jerk_21d_3d_v141_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_jerk_63d_3d_v142_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_jerk_126d_3d_v143_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_sales smoothed over 252d
def f069evs_f069_ev_sales_valuation_ev_sales_smoothaccel_63d_sm252_3d_v144_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_sales smoothed over 504d
def f069evs_f069_ev_sales_valuation_ev_sales_smoothaccel_252d_sm504_3d_v145_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ps_lvl smoothed over 252d
def f069evs_f069_ev_sales_valuation_ps_lvl_smoothaccel_63d_sm252_3d_v146_signal(ps, closeadj):
    base = ps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ps_lvl smoothed over 504d
def f069evs_f069_ev_sales_valuation_ps_lvl_smoothaccel_252d_sm504_3d_v147_signal(ps, closeadj):
    base = ps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ps1_lvl smoothed over 252d
def f069evs_f069_ev_sales_valuation_ps1_lvl_smoothaccel_63d_sm252_3d_v148_signal(ps1, closeadj):
    base = ps1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ps1_lvl smoothed over 504d
def f069evs_f069_ev_sales_valuation_ps1_lvl_smoothaccel_252d_sm504_3d_v149_signal(ps1, closeadj):
    base = ps1
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_to_rev smoothed over 252d
def f069evs_f069_ev_sales_valuation_mcap_to_rev_smoothaccel_63d_sm252_3d_v150_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_to_rev smoothed over 504d
def f069evs_f069_ev_sales_valuation_mcap_to_rev_smoothaccel_252d_sm504_3d_v151_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evsales_yoy_chg smoothed over 252d
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_smoothaccel_63d_sm252_3d_v152_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evsales_yoy_chg smoothed over 504d
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_smoothaccel_252d_sm504_3d_v153_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sales_yield smoothed over 252d
def f069evs_f069_ev_sales_valuation_sales_yield_smoothaccel_63d_sm252_3d_v154_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sales_yield smoothed over 504d
def f069evs_f069_ev_sales_valuation_sales_yield_smoothaccel_252d_sm504_3d_v155_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evsales_vol_252 smoothed over 252d
def f069evs_f069_ev_sales_valuation_evsales_vol_252_smoothaccel_63d_sm252_3d_v156_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evsales_vol_252 smoothed over 504d
def f069evs_f069_ev_sales_valuation_evsales_vol_252_smoothaccel_252d_sm504_3d_v157_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_sector_dist smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_sector_dist smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_sector_z smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_sector_z smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_industry_dist smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_industry_dist smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_mcap_bucket_dist smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_mcap_bucket_dist smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_sector_pctile smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_sector_pctile smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of evs_peer_industry_pctile smoothed over 252d
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of evs_peer_industry_pctile smoothed over 504d
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accelz_21d_z252_3d_v170_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_sales
def f069evs_f069_ev_sales_valuation_ev_sales_accelz_63d_z504_3d_v171_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accelz_21d_z252_3d_v172_signal(ps, closeadj):
    base = ps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ps_lvl
def f069evs_f069_ev_sales_valuation_ps_lvl_accelz_63d_z504_3d_v173_signal(ps, closeadj):
    base = ps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accelz_21d_z252_3d_v174_signal(ps1, closeadj):
    base = ps1
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ps1_lvl
def f069evs_f069_ev_sales_valuation_ps1_lvl_accelz_63d_z504_3d_v175_signal(ps1, closeadj):
    base = ps1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accelz_21d_z252_3d_v176_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_to_rev
def f069evs_f069_ev_sales_valuation_mcap_to_rev_accelz_63d_z504_3d_v177_signal(marketcap, revenue, closeadj):
    base = marketcap / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accelz_21d_z252_3d_v178_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evsales_yoy_chg
def f069evs_f069_ev_sales_valuation_evsales_yoy_chg_accelz_63d_z504_3d_v179_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accelz_21d_z252_3d_v180_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sales_yield
def f069evs_f069_ev_sales_valuation_sales_yield_accelz_63d_z504_3d_v181_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accelz_21d_z252_3d_v182_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evsales_vol_252
def f069evs_f069_ev_sales_valuation_evsales_vol_252_accelz_63d_z504_3d_v183_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accelz_21d_z252_3d_v184_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_sector_dist
def f069evs_f069_ev_sales_valuation_evs_peer_sector_dist_accelz_63d_z504_3d_v185_signal(ev, revenue, evs_sector_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accelz_21d_z252_3d_v186_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_sector_z
def f069evs_f069_ev_sales_valuation_evs_peer_sector_z_accelz_63d_z504_3d_v187_signal(ev, revenue, evs_sector_med, evs_sector_std, closeadj):
    base = (_f069_evs(ev, revenue) - evs_sector_med) / evs_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accelz_21d_z252_3d_v188_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_industry_dist
def f069evs_f069_ev_sales_valuation_evs_peer_industry_dist_accelz_63d_z504_3d_v189_signal(ev, revenue, evs_industry_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_industry_med) / evs_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_mcap_bucket_dist
def f069evs_f069_ev_sales_valuation_evs_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(ev, revenue, evs_mcap_med, closeadj):
    base = (_f069_evs(ev, revenue) - evs_mcap_med) / evs_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_sector_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(evs_sector_pctile, closeadj):
    base = evs_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of evs_peer_industry_pctile
def f069evs_f069_ev_sales_valuation_evs_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(evs_industry_pctile, closeadj):
    base = evs_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_sales (raw count, no price scaling)
def f069evs_f069_ev_sales_valuation_ev_sales_signflip_63d_3d_v196_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_sales (raw count, no price scaling)
def f069evs_f069_ev_sales_valuation_ev_sales_signflip_252d_3d_v197_signal(ev, revenue, closeadj):
    base = _f069_evs(ev, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ps_lvl (raw count, no price scaling)
def f069evs_f069_ev_sales_valuation_ps_lvl_signflip_63d_3d_v198_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ps_lvl (raw count, no price scaling)
def f069evs_f069_ev_sales_valuation_ps_lvl_signflip_252d_3d_v199_signal(ps, closeadj):
    base = ps
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ps1_lvl (raw count, no price scaling)
def f069evs_f069_ev_sales_valuation_ps1_lvl_signflip_63d_3d_v200_signal(ps1, closeadj):
    base = ps1
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

