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


# 21d acceleration of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accel_21d_3d_v001_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accel_63d_3d_v002_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accel_126d_3d_v003_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accel_252d_3d_v004_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accel_21d_3d_v005_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accel_63d_3d_v006_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accel_126d_3d_v007_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accel_252d_3d_v008_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accel_21d_3d_v009_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accel_63d_3d_v010_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accel_126d_3d_v011_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accel_252d_3d_v012_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accel_21d_3d_v013_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accel_63d_3d_v014_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accel_126d_3d_v015_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accel_252d_3d_v016_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accel_21d_3d_v017_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accel_63d_3d_v018_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accel_126d_3d_v019_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accel_252d_3d_v020_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accel_21d_3d_v021_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accel_63d_3d_v022_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accel_126d_3d_v023_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accel_252d_3d_v024_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accel_21d_3d_v025_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accel_63d_3d_v026_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accel_126d_3d_v027_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accel_252d_3d_v028_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slopez_21d_z126_3d_v029_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slopez_63d_z252_3d_v030_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slopez_126d_z252_3d_v031_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_slopez_252d_z504_3d_v032_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slopez_21d_z126_3d_v033_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slopez_63d_z252_3d_v034_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slopez_126d_z252_3d_v035_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_slopez_252d_z504_3d_v036_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slopez_21d_z126_3d_v037_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slopez_63d_z252_3d_v038_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slopez_126d_z252_3d_v039_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_slopez_252d_z504_3d_v040_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slopez_21d_z126_3d_v041_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slopez_63d_z252_3d_v042_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slopez_126d_z252_3d_v043_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_slopez_252d_z504_3d_v044_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slopez_21d_z126_3d_v045_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slopez_63d_z252_3d_v046_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slopez_126d_z252_3d_v047_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_slopez_252d_z504_3d_v048_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slopez_21d_z126_3d_v049_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slopez_63d_z252_3d_v050_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slopez_126d_z252_3d_v051_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_slopez_252d_z504_3d_v052_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slopez_21d_z126_3d_v053_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slopez_63d_z252_3d_v054_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slopez_126d_z252_3d_v055_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_slopez_252d_z504_3d_v056_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_jerk_21d_3d_v057_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_jerk_63d_3d_v058_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_jerk_126d_3d_v059_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_jerk_21d_3d_v060_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_jerk_63d_3d_v061_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_jerk_126d_3d_v062_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_jerk_21d_3d_v063_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_jerk_63d_3d_v064_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_jerk_126d_3d_v065_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_jerk_21d_3d_v066_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_jerk_63d_3d_v067_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_jerk_126d_3d_v068_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_jerk_21d_3d_v069_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_jerk_63d_3d_v070_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_jerk_126d_3d_v071_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_jerk_21d_3d_v072_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_jerk_63d_3d_v073_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_jerk_126d_3d_v074_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_jerk_21d_3d_v075_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_jerk_63d_3d_v076_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_jerk_126d_3d_v077_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_gp smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_smoothaccel_63d_sm252_3d_v078_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_gp smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_smoothaccel_252d_sm504_3d_v079_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_yield smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_gp_yield_smoothaccel_63d_sm252_3d_v080_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_yield smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_gp_yield_smoothaccel_252d_sm504_3d_v081_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of mcap_to_gp smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_smoothaccel_63d_sm252_3d_v082_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of mcap_to_gp smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_smoothaccel_252d_sm504_3d_v083_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_gp_adj_gm smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_smoothaccel_63d_sm252_3d_v084_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_gp_adj_gm smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_smoothaccel_252d_sm504_3d_v085_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ev_gp_yoy smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_smoothaccel_63d_sm252_3d_v086_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ev_gp_yoy smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_smoothaccel_252d_sm504_3d_v087_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_per_share smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_smoothaccel_63d_sm252_3d_v088_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_per_share smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_smoothaccel_252d_sm504_3d_v089_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_growth_pct smoothed over 252d
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_smoothaccel_63d_sm252_3d_v090_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_growth_pct smoothed over 504d
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_smoothaccel_252d_sm504_3d_v091_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accelz_21d_z252_3d_v092_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_accelz_63d_z504_3d_v093_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accelz_21d_z252_3d_v094_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_accelz_63d_z504_3d_v095_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accelz_21d_z252_3d_v096_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_accelz_63d_z504_3d_v097_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accelz_21d_z252_3d_v098_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_accelz_63d_z504_3d_v099_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accelz_21d_z252_3d_v100_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_accelz_63d_z504_3d_v101_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accelz_21d_z252_3d_v102_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_accelz_63d_z504_3d_v103_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accelz_21d_z252_3d_v104_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_accelz_63d_z504_3d_v105_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_gp (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_signflip_63d_3d_v106_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_gp (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_signflip_252d_3d_v107_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gp_yield (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_yield_signflip_63d_3d_v108_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gp_yield (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_yield_signflip_252d_3d_v109_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in mcap_to_gp (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_signflip_63d_3d_v110_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in mcap_to_gp (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_signflip_252d_3d_v111_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_gp_adj_gm (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_signflip_63d_3d_v112_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_gp_adj_gm (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_signflip_252d_3d_v113_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ev_gp_yoy (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_signflip_63d_3d_v114_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ev_gp_yoy (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_signflip_252d_3d_v115_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gp_per_share (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_signflip_63d_3d_v116_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gp_per_share (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_signflip_252d_3d_v117_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gp_growth_pct (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_signflip_63d_3d_v118_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gp_growth_pct (raw count, no price scaling)
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_signflip_252d_3d_v119_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rngaccel_63d_r252_3d_v120_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rngaccel_252d_r504_3d_v121_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_yield normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rngaccel_63d_r252_3d_v122_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_yield normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rngaccel_252d_r504_3d_v123_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of mcap_to_gp normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_rngaccel_63d_r252_3d_v124_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of mcap_to_gp normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_rngaccel_252d_r504_3d_v125_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp_adj_gm normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_rngaccel_63d_r252_3d_v126_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp_adj_gm normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_rngaccel_252d_r504_3d_v127_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ev_gp_yoy normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_rngaccel_63d_r252_3d_v128_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ev_gp_yoy normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_rngaccel_252d_r504_3d_v129_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_per_share normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_rngaccel_63d_r252_3d_v130_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_per_share normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_rngaccel_252d_r504_3d_v131_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_growth_pct normalized by 252d range
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_rngaccel_63d_r252_3d_v132_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_growth_pct normalized by 504d range
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_rngaccel_252d_r504_3d_v133_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_cumslope_21d_3d_v134_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_cumslope_63d_3d_v135_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_cumslope_252d_3d_v136_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_cumslope_21d_3d_v137_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_cumslope_63d_3d_v138_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_cumslope_252d_3d_v139_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_cumslope_21d_3d_v140_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_cumslope_63d_3d_v141_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_cumslope_252d_3d_v142_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_cumslope_21d_3d_v143_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_cumslope_63d_3d_v144_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_cumslope_252d_3d_v145_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_cumslope_21d_3d_v146_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_cumslope_63d_3d_v147_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_cumslope_252d_3d_v148_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_cumslope_21d_3d_v149_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_cumslope_63d_3d_v150_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

