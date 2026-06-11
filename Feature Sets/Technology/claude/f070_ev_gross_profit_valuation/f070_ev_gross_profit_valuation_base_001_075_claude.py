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
def _f070_evgp(ev, gp):
    return ev / gp.abs().replace(0, np.nan)


# 21d mean of ev_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_mean_21d_base_v001_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_mean_63d_base_v002_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_mean_126d_base_v003_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_mean_252d_base_v004_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_mean_504d_base_v005_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_yield scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_yield_mean_21d_base_v006_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_yield scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_yield_mean_63d_base_v007_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_yield scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_yield_mean_126d_base_v008_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_yield scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_yield_mean_252d_base_v009_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_yield scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_yield_mean_504d_base_v010_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of mcap_to_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_mean_21d_base_v011_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of mcap_to_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_mean_63d_base_v012_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of mcap_to_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_mean_126d_base_v013_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of mcap_to_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_mean_252d_base_v014_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of mcap_to_gp scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_mean_504d_base_v015_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_gp_adj_gm scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_mean_21d_base_v016_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_gp_adj_gm scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_mean_63d_base_v017_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_gp_adj_gm scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_mean_126d_base_v018_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_gp_adj_gm scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_mean_252d_base_v019_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_gp_adj_gm scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_mean_504d_base_v020_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_gp_yoy scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_mean_21d_base_v021_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_gp_yoy scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_mean_63d_base_v022_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_gp_yoy scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_mean_126d_base_v023_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_gp_yoy scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_mean_252d_base_v024_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_gp_yoy scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_mean_504d_base_v025_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_per_share scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_mean_21d_base_v026_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_per_share scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_mean_63d_base_v027_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_per_share scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_mean_126d_base_v028_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_per_share scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_mean_252d_base_v029_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_per_share scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_mean_504d_base_v030_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_growth_pct scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_mean_21d_base_v031_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_growth_pct scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_mean_63d_base_v032_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_growth_pct scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_mean_126d_base_v033_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_growth_pct scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_mean_252d_base_v034_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_growth_pct scaled by closeadj
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_mean_504d_base_v035_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_median_63d_base_v036_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_median_252d_base_v037_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_median_504d_base_v038_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_median_63d_base_v039_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_median_252d_base_v040_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_median_504d_base_v041_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_median_63d_base_v042_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_median_252d_base_v043_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_median_504d_base_v044_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_median_63d_base_v045_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_median_252d_base_v046_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_median_504d_base_v047_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_median_63d_base_v048_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_median_252d_base_v049_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_median_504d_base_v050_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_median_63d_base_v051_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_median_252d_base_v052_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_median_504d_base_v053_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_median_63d_base_v054_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_median_252d_base_v055_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_median_504d_base_v056_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rmax_252d_base_v057_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rmax_504d_base_v058_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rmax_252d_base_v059_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rmax_504d_base_v060_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_rmax_252d_base_v061_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_rmax_504d_base_v062_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_rmax_252d_base_v063_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_rmax_504d_base_v064_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_rmax_252d_base_v065_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_rmax_504d_base_v066_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_rmax_252d_base_v067_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_rmax_504d_base_v068_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_rmax_252d_base_v069_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_rmax_504d_base_v070_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rmin_252d_base_v071_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_rmin_504d_base_v072_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rmin_252d_base_v073_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_rmin_504d_base_v074_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_rmin_252d_base_v075_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

