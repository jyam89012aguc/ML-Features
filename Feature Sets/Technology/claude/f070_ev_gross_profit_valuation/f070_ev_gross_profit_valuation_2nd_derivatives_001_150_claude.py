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
def _f070_evgp(ev, gp):
    return ev / gp.abs().replace(0, np.nan)


# 21d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slope_21d_2d_v001_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slope_63d_2d_v002_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slope_126d_2d_v003_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slope_252d_2d_v004_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slope_504d_2d_v005_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slope_21d_2d_v006_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slope_63d_2d_v007_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slope_126d_2d_v008_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slope_252d_2d_v009_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slope_504d_2d_v010_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slope_21d_2d_v011_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slope_63d_2d_v012_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slope_126d_2d_v013_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slope_252d_2d_v014_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slope_504d_2d_v015_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slope_21d_2d_v016_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slope_63d_2d_v017_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slope_126d_2d_v018_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slope_252d_2d_v019_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slope_504d_2d_v020_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slope_21d_2d_v021_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slope_63d_2d_v022_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slope_126d_2d_v023_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slope_252d_2d_v024_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slope_504d_2d_v025_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slope_21d_2d_v026_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slope_63d_2d_v027_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slope_126d_2d_v028_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slope_252d_2d_v029_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slope_504d_2d_v030_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slope_21d_2d_v031_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slope_63d_2d_v032_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slope_126d_2d_v033_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slope_252d_2d_v034_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slope_504d_2d_v035_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sm21_sl21_2d_v036_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sm63_sl21_2d_v037_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sm63_sl63_2d_v038_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sm252_sl63_2d_v039_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sm252_sl126_2d_v040_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sm21_sl21_2d_v041_signal(gp, ev, closeadj):
    base = _mean(gp / ev.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sm63_sl21_2d_v042_signal(gp, ev, closeadj):
    base = _mean(gp / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sm63_sl63_2d_v043_signal(gp, ev, closeadj):
    base = _mean(gp / ev.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sm252_sl63_2d_v044_signal(gp, ev, closeadj):
    base = _mean(gp / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sm252_sl126_2d_v045_signal(gp, ev, closeadj):
    base = _mean(gp / ev.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sm21_sl21_2d_v046_signal(marketcap, gp, closeadj):
    base = _mean(marketcap / gp.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sm63_sl21_2d_v047_signal(marketcap, gp, closeadj):
    base = _mean(marketcap / gp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sm63_sl63_2d_v048_signal(marketcap, gp, closeadj):
    base = _mean(marketcap / gp.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sm252_sl63_2d_v049_signal(marketcap, gp, closeadj):
    base = _mean(marketcap / gp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sm252_sl126_2d_v050_signal(marketcap, gp, closeadj):
    base = _mean(marketcap / gp.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sm21_sl21_2d_v051_signal(ev, gp, revenue, closeadj):
    base = _mean(_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sm63_sl21_2d_v052_signal(ev, gp, revenue, closeadj):
    base = _mean(_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sm63_sl63_2d_v053_signal(ev, gp, revenue, closeadj):
    base = _mean(_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sm252_sl63_2d_v054_signal(ev, gp, revenue, closeadj):
    base = _mean(_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sm252_sl126_2d_v055_signal(ev, gp, revenue, closeadj):
    base = _mean(_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sm21_sl21_2d_v056_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sm63_sl21_2d_v057_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sm63_sl63_2d_v058_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sm252_sl63_2d_v059_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sm252_sl126_2d_v060_signal(ev, gp, closeadj):
    base = _mean(_f070_evgp(ev, gp).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sm21_sl21_2d_v061_signal(gp, sharesbas, closeadj):
    base = _mean(gp / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sm63_sl21_2d_v062_signal(gp, sharesbas, closeadj):
    base = _mean(gp / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sm63_sl63_2d_v063_signal(gp, sharesbas, closeadj):
    base = _mean(gp / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sm252_sl63_2d_v064_signal(gp, sharesbas, closeadj):
    base = _mean(gp / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sm252_sl126_2d_v065_signal(gp, sharesbas, closeadj):
    base = _mean(gp / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sm21_sl21_2d_v066_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sm63_sl21_2d_v067_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sm63_sl63_2d_v068_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sm252_sl63_2d_v069_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sm252_sl126_2d_v070_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_pctslope_21d_2d_v071_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_pctslope_63d_2d_v072_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_pctslope_252d_2d_v073_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_pctslope_21d_2d_v074_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_pctslope_63d_2d_v075_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_pctslope_252d_2d_v076_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_pctslope_21d_2d_v077_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_pctslope_63d_2d_v078_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_pctslope_252d_2d_v079_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_pctslope_21d_2d_v080_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_pctslope_63d_2d_v081_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_pctslope_252d_2d_v082_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_pctslope_21d_2d_v083_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_pctslope_63d_2d_v084_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_pctslope_252d_2d_v085_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_pctslope_21d_2d_v086_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_pctslope_63d_2d_v087_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_pctslope_252d_2d_v088_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_pctslope_21d_2d_v089_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_pctslope_63d_2d_v090_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_pctslope_252d_2d_v091_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sgnslope_21d_2d_v092_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sgnslope_63d_2d_v093_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_sgnslope_252d_2d_v094_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sgnslope_21d_2d_v095_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sgnslope_63d_2d_v096_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_sgnslope_252d_2d_v097_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sgnslope_21d_2d_v098_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sgnslope_63d_2d_v099_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_sgnslope_252d_2d_v100_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sgnslope_21d_2d_v101_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sgnslope_63d_2d_v102_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_sgnslope_252d_2d_v103_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sgnslope_21d_2d_v104_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sgnslope_63d_2d_v105_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_sgnslope_252d_2d_v106_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sgnslope_21d_2d_v107_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sgnslope_63d_2d_v108_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_sgnslope_252d_2d_v109_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sgnslope_21d_2d_v110_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sgnslope_63d_2d_v111_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_sgnslope_252d_2d_v112_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_logmagslope_21d_2d_v113_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_logmagslope_63d_2d_v114_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_logmagslope_252d_2d_v115_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_logmagslope_21d_2d_v116_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_logmagslope_63d_2d_v117_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_logmagslope_252d_2d_v118_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_logmagslope_21d_2d_v119_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_logmagslope_63d_2d_v120_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_logmagslope_252d_2d_v121_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_logmagslope_21d_2d_v122_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_logmagslope_63d_2d_v123_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_logmagslope_252d_2d_v124_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_logmagslope_21d_2d_v125_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_logmagslope_63d_2d_v126_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_logmagslope_252d_2d_v127_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_logmagslope_21d_2d_v128_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_logmagslope_63d_2d_v129_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_logmagslope_252d_2d_v130_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_logmagslope_21d_2d_v131_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_logmagslope_63d_2d_v132_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_logmagslope_252d_2d_v133_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_gp|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_logslope_63d_2d_v134_signal(ev, gp, closeadj):
    base = np.log((_f070_evgp(ev, gp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_gp|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_logslope_252d_2d_v135_signal(ev, gp, closeadj):
    base = np.log((_f070_evgp(ev, gp)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gp_yield|
def f070egp_f070_ev_gross_profit_valuation_gp_yield_logslope_63d_2d_v136_signal(gp, ev, closeadj):
    base = np.log((gp / ev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gp_yield|
def f070egp_f070_ev_gross_profit_valuation_gp_yield_logslope_252d_2d_v137_signal(gp, ev, closeadj):
    base = np.log((gp / ev.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|mcap_to_gp|
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_logslope_63d_2d_v138_signal(marketcap, gp, closeadj):
    base = np.log((marketcap / gp.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|mcap_to_gp|
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_logslope_252d_2d_v139_signal(marketcap, gp, closeadj):
    base = np.log((marketcap / gp.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_gp_adj_gm|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_logslope_63d_2d_v140_signal(ev, gp, revenue, closeadj):
    base = np.log((_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_gp_adj_gm|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_logslope_252d_2d_v141_signal(ev, gp, revenue, closeadj):
    base = np.log((_f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_gp_yoy|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_logslope_63d_2d_v142_signal(ev, gp, closeadj):
    base = np.log((_f070_evgp(ev, gp).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_gp_yoy|
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_logslope_252d_2d_v143_signal(ev, gp, closeadj):
    base = np.log((_f070_evgp(ev, gp).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gp_per_share|
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_logslope_63d_2d_v144_signal(gp, sharesbas, closeadj):
    base = np.log((gp / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gp_per_share|
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_logslope_252d_2d_v145_signal(gp, sharesbas, closeadj):
    base = np.log((gp / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gp_growth_pct|
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_logslope_63d_2d_v146_signal(gp, closeadj):
    base = np.log((gp.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gp_growth_pct|
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_logslope_252d_2d_v147_signal(gp, closeadj):
    base = np.log((gp.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

