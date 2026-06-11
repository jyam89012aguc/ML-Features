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


# 63d z-score of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_z_63d_base_v076_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_z_126d_base_v077_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_z_252d_base_v078_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_z_504d_base_v079_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_z_63d_base_v080_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_z_126d_base_v081_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_z_252d_base_v082_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_z_504d_base_v083_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_z_63d_base_v084_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_z_126d_base_v085_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_z_252d_base_v086_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_z_504d_base_v087_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_z_63d_base_v088_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_z_126d_base_v089_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_z_252d_base_v090_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_z_504d_base_v091_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_z_63d_base_v092_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_z_126d_base_v093_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_z_252d_base_v094_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_z_504d_base_v095_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_z_63d_base_v096_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_z_126d_base_v097_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_z_252d_base_v098_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_z_504d_base_v099_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_z_63d_base_v100_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_z_126d_base_v101_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_z_252d_base_v102_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_z_504d_base_v103_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_distmax_252d_base_v104_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_distmax_504d_base_v105_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_distmax_252d_base_v106_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_distmax_504d_base_v107_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_distmax_252d_base_v108_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_distmax_504d_base_v109_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_distmax_252d_base_v110_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_distmax_504d_base_v111_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_distmax_252d_base_v112_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_distmax_504d_base_v113_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_distmax_252d_base_v114_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_distmax_504d_base_v115_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_distmax_252d_base_v116_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_distmax_504d_base_v117_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_distmed_126d_base_v118_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_distmed_252d_base_v119_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_distmed_504d_base_v120_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_distmed_126d_base_v121_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_distmed_252d_base_v122_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_distmed_504d_base_v123_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_distmed_126d_base_v124_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_distmed_252d_base_v125_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_distmed_504d_base_v126_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_distmed_126d_base_v127_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_distmed_252d_base_v128_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_distmed_504d_base_v129_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_distmed_126d_base_v130_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_distmed_252d_base_v131_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_distmed_504d_base_v132_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_distmed_126d_base_v133_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_distmed_252d_base_v134_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_distmed_504d_base_v135_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_distmed_126d_base_v136_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_distmed_252d_base_v137_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_growth_pct
def f070egp_f070_ev_gross_profit_valuation_gp_growth_pct_distmed_504d_base_v138_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_chg_63d_base_v139_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ev_gp
def f070egp_f070_ev_gross_profit_valuation_ev_gp_chg_252d_base_v140_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_chg_63d_base_v141_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in gp_yield
def f070egp_f070_ev_gross_profit_valuation_gp_yield_chg_252d_base_v142_signal(gp, ev, closeadj):
    base = gp / ev.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_chg_63d_base_v143_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in mcap_to_gp
def f070egp_f070_ev_gross_profit_valuation_mcap_to_gp_chg_252d_base_v144_signal(marketcap, gp, closeadj):
    base = marketcap / gp.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_chg_63d_base_v145_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ev_gp_adj_gm
def f070egp_f070_ev_gross_profit_valuation_ev_gp_adj_gm_chg_252d_base_v146_signal(ev, gp, revenue, closeadj):
    base = _f070_evgp(ev, gp) / (gp / revenue.abs().replace(0, np.nan)).replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_chg_63d_base_v147_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ev_gp_yoy
def f070egp_f070_ev_gross_profit_valuation_ev_gp_yoy_chg_252d_base_v148_signal(ev, gp, closeadj):
    base = _f070_evgp(ev, gp).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_chg_63d_base_v149_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in gp_per_share
def f070egp_f070_ev_gross_profit_valuation_gp_per_share_chg_252d_base_v150_signal(gp, sharesbas, closeadj):
    base = gp / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

