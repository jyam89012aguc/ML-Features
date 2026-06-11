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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f15_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f15_pricing_dynamics(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan).abs()
    return rpa.pct_change(periods=w)


def _f15_pricing_uplift(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan).abs()
    return rpp.pct_change(periods=w)

def f15dpd_f15_diagnostics_pricing_dynamics_pdz_126d_base_v076_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdz_189d_base_v077_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 189)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdz_252d_base_v078_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdz_378d_base_v079_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdz_504d_base_v080_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_5d_base_v081_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_10d_base_v082_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 10)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_21d_base_v083_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_42d_base_v084_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_63d_base_v085_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_126d_base_v086_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_189d_base_v087_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 189)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_252d_base_v088_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_378d_base_v089_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puz_504d_base_v090_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_5d_base_v091_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 5)
    as_w = _mean(assets, 5)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_10d_base_v092_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 10)
    as_w = _mean(assets, 10)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_21d_base_v093_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 21)
    as_w = _mean(assets, 21)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_42d_base_v094_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 42)
    as_w = _mean(assets, 42)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_63d_base_v095_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 63)
    as_w = _mean(assets, 63)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_126d_base_v096_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 126)
    as_w = _mean(assets, 126)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_189d_base_v097_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 189)
    as_w = _mean(assets, 189)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_252d_base_v098_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 252)
    as_w = _mean(assets, 252)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_378d_base_v099_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 378)
    as_w = _mean(assets, 378)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpamean_504d_base_v100_signal(revenue, assets, closeadj):
    rev_w = _mean(revenue, 504)
    as_w = _mean(assets, 504)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    result = _mean(rpa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_5d_base_v101_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_10d_base_v102_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_21d_base_v103_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_42d_base_v104_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_63d_base_v105_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_126d_base_v106_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_189d_base_v107_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 189)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_252d_base_v108_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 252)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_378d_base_v109_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 378)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdema_504d_base_v110_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 504)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_5d_base_v111_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_10d_base_v112_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_21d_base_v113_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_42d_base_v114_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_63d_base_v115_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_126d_base_v116_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_189d_base_v117_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 189)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_252d_base_v118_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 252)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_378d_base_v119_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 378)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_puema_504d_base_v120_signal(revenue, ppnenet, closeadj):
    base = _f15_pricing_uplift(revenue, ppnenet, 504)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_5d_base_v121_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 5)
    b = _f15_pricing_uplift(revenue, ppnenet, 5)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_10d_base_v122_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 10)
    b = _f15_pricing_uplift(revenue, ppnenet, 10)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_21d_base_v123_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 21)
    b = _f15_pricing_uplift(revenue, ppnenet, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_42d_base_v124_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 42)
    b = _f15_pricing_uplift(revenue, ppnenet, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_63d_base_v125_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 63)
    b = _f15_pricing_uplift(revenue, ppnenet, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_126d_base_v126_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 126)
    b = _f15_pricing_uplift(revenue, ppnenet, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_189d_base_v127_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 189)
    b = _f15_pricing_uplift(revenue, ppnenet, 189)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_252d_base_v128_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 252)
    b = _f15_pricing_uplift(revenue, ppnenet, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_378d_base_v129_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 378)
    b = _f15_pricing_uplift(revenue, ppnenet, 378)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_504d_base_v130_signal(revenue, assets, ppnenet, closeadj):
    a = _f15_pricing_dynamics(revenue, assets, 504)
    b = _f15_pricing_uplift(revenue, ppnenet, 504)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_5d_base_v131_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 5)
    as_w = _mean(assets, 5)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=5)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_10d_base_v132_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 10)
    as_w = _mean(assets, 10)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=10)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_21d_base_v133_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 21)
    as_w = _mean(assets, 21)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=21)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_42d_base_v134_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 42)
    as_w = _mean(assets, 42)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=42)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_63d_base_v135_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 63)
    as_w = _mean(assets, 63)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=63)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_126d_base_v136_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 126)
    as_w = _mean(assets, 126)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=126)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_189d_base_v137_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 189)
    as_w = _mean(assets, 189)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=189)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_252d_base_v138_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 252)
    as_w = _mean(assets, 252)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=252)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_378d_base_v139_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 378)
    as_w = _mean(assets, 378)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=378)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_504d_base_v140_signal(revenue, assets, ppnenet, closeadj):
    rev_w = _mean(revenue, 504)
    as_w = _mean(assets, 504)
    rpa = _f15_revenue_per_asset(rev_w, as_w)
    ppe_g = ppnenet.pct_change(periods=504)
    result = rpa * ppe_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_5d_base_v141_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 5)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_10d_base_v142_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 10)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_21d_base_v143_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_42d_base_v144_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 42)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_63d_base_v145_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_126d_base_v146_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 126)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_189d_base_v147_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 189)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_252d_base_v148_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_378d_base_v149_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 378)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15dpd_f15_diagnostics_pricing_dynamics_pdstd_504d_base_v150_signal(revenue, assets, closeadj):
    base = _f15_pricing_dynamics(revenue, assets, 504)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15dpd_f15_diagnostics_pricing_dynamics_pdz_126d_base_v076_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdz_189d_base_v077_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdz_252d_base_v078_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdz_378d_base_v079_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdz_504d_base_v080_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_5d_base_v081_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_10d_base_v082_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_21d_base_v083_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_42d_base_v084_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_63d_base_v085_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_126d_base_v086_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_189d_base_v087_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_252d_base_v088_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_378d_base_v089_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puz_504d_base_v090_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_5d_base_v091_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_10d_base_v092_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_21d_base_v093_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_42d_base_v094_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_63d_base_v095_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_126d_base_v096_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_189d_base_v097_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_252d_base_v098_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_378d_base_v099_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpamean_504d_base_v100_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_5d_base_v101_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_10d_base_v102_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_21d_base_v103_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_42d_base_v104_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_63d_base_v105_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_126d_base_v106_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_189d_base_v107_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_252d_base_v108_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_378d_base_v109_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdema_504d_base_v110_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_5d_base_v111_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_10d_base_v112_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_21d_base_v113_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_42d_base_v114_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_63d_base_v115_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_126d_base_v116_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_189d_base_v117_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_252d_base_v118_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_378d_base_v119_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_puema_504d_base_v120_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_5d_base_v121_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_10d_base_v122_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_21d_base_v123_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_42d_base_v124_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_63d_base_v125_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_126d_base_v126_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_189d_base_v127_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_252d_base_v128_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_378d_base_v129_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdxpu_504d_base_v130_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_5d_base_v131_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_10d_base_v132_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_21d_base_v133_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_42d_base_v134_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_63d_base_v135_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_126d_base_v136_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_189d_base_v137_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_252d_base_v138_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_378d_base_v139_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_rpaxppe_504d_base_v140_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_5d_base_v141_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_10d_base_v142_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_21d_base_v143_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_42d_base_v144_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_63d_base_v145_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_126d_base_v146_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_189d_base_v147_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_252d_base_v148_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_378d_base_v149_signal,
    f15dpd_f15_diagnostics_pricing_dynamics_pdstd_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_DIAGNOSTICS_PRICING_DYNAMICS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_revenue_per_asset", "_f15_pricing_dynamics", "_f15_pricing_uplift",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f15_diagnostics_pricing_dynamics_base_076_150_claude: {n_features} features pass")
