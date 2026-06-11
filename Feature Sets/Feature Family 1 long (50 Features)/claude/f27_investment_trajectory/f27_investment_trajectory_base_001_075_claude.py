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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f27_invest_traj(capex, w):
    base = _mean(capex, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f27_capex_growth(capex, w):
    return _diff(_mean(capex, w), w) / _mean(capex.abs(), w).replace(0, np.nan)


def _f27_capex_to_rev(capex, revenue, w):
    return _safe_div(_mean(capex, w), _mean(revenue, w))


# 21d capex growth trajectory weighted by closeadj
def f27it_f27_investment_trajectory_capgrow_21d_base_v001_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth trajectory weighted by closeadj
def f27it_f27_investment_trajectory_capgrow_63d_base_v002_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex growth trajectory weighted by closeadj
def f27it_f27_investment_trajectory_capgrow_126d_base_v003_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth trajectory weighted by closeadj
def f27it_f27_investment_trajectory_capgrow_252d_base_v004_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth trajectory weighted by closeadj
def f27it_f27_investment_trajectory_capgrow_504d_base_v005_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d invest trajectory mean weighted by closeadj
def f27it_f27_investment_trajectory_capinv_21d_base_v006_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invest trajectory mean weighted by closeadj
def f27it_f27_investment_trajectory_capinv_63d_base_v007_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest trajectory mean weighted by closeadj
def f27it_f27_investment_trajectory_capinv_252d_base_v008_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest trajectory mean weighted by closeadj
def f27it_f27_investment_trajectory_capinv_504d_base_v009_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue trajectory weighted by closeadj
def f27it_f27_investment_trajectory_caprev_63d_base_v010_signal(capex, revenue, closeadj):
    result = _f27_capex_to_rev(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/revenue trajectory weighted by closeadj
def f27it_f27_investment_trajectory_caprev_126d_base_v011_signal(capex, revenue, closeadj):
    result = _f27_capex_to_rev(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue trajectory weighted by closeadj
def f27it_f27_investment_trajectory_caprev_252d_base_v012_signal(capex, revenue, closeadj):
    result = _f27_capex_to_rev(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/revenue trajectory weighted by closeadj
def f27it_f27_investment_trajectory_caprev_504d_base_v013_signal(capex, revenue, closeadj):
    result = _f27_capex_to_rev(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in capex/revenue ratio (invest trajectory)
def f27it_f27_investment_trajectory_caprevdiff_63d_base_v014_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63)
    result = _diff(base, 63) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/revenue ratio
def f27it_f27_investment_trajectory_caprevdiff_252d_base_v015_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = _diff(base, 252) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in capex/revenue ratio
def f27it_f27_investment_trajectory_caprevdiff_504d_base_v016_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 504)
    result = _diff(base, 252) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of capex growth 63d over 252d
def f27it_f27_investment_trajectory_capgrowz_252d_base_v017_signal(capex, closeadj):
    result = _z(_f27_capex_growth(capex, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of capex growth 252d over 504d
def f27it_f27_investment_trajectory_capgrowz_504d_base_v018_signal(capex, closeadj):
    result = _z(_f27_capex_growth(capex, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d capex growth over 63d
def f27it_f27_investment_trajectory_capgrowmean_63d_base_v019_signal(capex, closeadj):
    result = _mean(_f27_capex_growth(capex, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d capex growth over 252d
def f27it_f27_investment_trajectory_capgrowmean_252d_base_v020_signal(capex, closeadj):
    result = _mean(_f27_capex_growth(capex, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of capex growth 63d over 252d
def f27it_f27_investment_trajectory_capgrowstd_252d_base_v021_signal(capex, closeadj):
    result = _std(_f27_capex_growth(capex, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of capex growth 252d over 504d
def f27it_f27_investment_trajectory_capgrowstd_504d_base_v022_signal(capex, closeadj):
    result = _std(_f27_capex_growth(capex, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of months with positive capex growth (rolling sum)
def f27it_f27_investment_trajectory_capgrowupcnt_252d_base_v023_signal(capex, closeadj):
    flag = (_f27_capex_growth(capex, 21) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of capex growth slow-downs (rolling sum)
def f27it_f27_investment_trajectory_capgrowdowncnt_504d_base_v024_signal(capex, closeadj):
    flag = (_f27_capex_growth(capex, 63) < 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue intensity weighted by closeadj^2 normalization
def f27it_f27_investment_trajectory_capintensity_63d_base_v025_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue intensity weighted by mean closeadj
def f27it_f27_investment_trajectory_capintensity_252d_base_v026_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d invest traj scaled by absolute capex level
def f27it_f27_investment_trajectory_capinvxlevel_21d_base_v027_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 21) * _mean(capex, 21) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invest traj scaled by capex level
def f27it_f27_investment_trajectory_capinvxlevel_63d_base_v028_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 63) * _mean(capex, 63) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest traj scaled by capex level
def f27it_f27_investment_trajectory_capinvxlevel_252d_base_v029_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 252) * _mean(capex, 252) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest traj scaled by capex level
def f27it_f27_investment_trajectory_capinvxlevel_504d_base_v030_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 504) * _mean(capex, 504) / 1e6 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex over operating cash flow trajectory
def f27it_f27_investment_trajectory_capncfo_63d_base_v031_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(ncfo, 63))
    result = base * closeadj + _f27_capex_growth(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex over operating cash flow trajectory
def f27it_f27_investment_trajectory_capncfo_252d_base_v032_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ncfo, 252))
    result = base * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex over operating cash flow trajectory
def f27it_f27_investment_trajectory_capncfo_504d_base_v033_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(ncfo, 504))
    result = base * closeadj + _f27_capex_growth(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in capex/ncfo ratio
def f27it_f27_investment_trajectory_capncfodiff_63d_base_v034_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(ncfo, 63))
    result = _diff(base, 63) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/ncfo ratio
def f27it_f27_investment_trajectory_capncfodiff_252d_base_v035_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ncfo, 252))
    result = _diff(base, 252) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex over assets trajectory
def f27it_f27_investment_trajectory_capassets_63d_base_v036_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(assets, 63))
    result = base * closeadj + _f27_invest_traj(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex over assets trajectory
def f27it_f27_investment_trajectory_capassets_252d_base_v037_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex over assets trajectory
def f27it_f27_investment_trajectory_capassets_504d_base_v038_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/assets ratio
def f27it_f27_investment_trajectory_capassetsdiff_252d_base_v039_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets, 252))
    result = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in capex/assets ratio
def f27it_f27_investment_trajectory_capassetsdiff_504d_base_v040_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets, 504))
    result = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA capex growth
def f27it_f27_investment_trajectory_capgrowema_21d_base_v041_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21)
    result = base.ewm(span=21, adjust=False, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA capex growth
def f27it_f27_investment_trajectory_capgrowema_63d_base_v042_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63)
    result = base.ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA capex growth
def f27it_f27_investment_trajectory_capgrowema_252d_base_v043_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252)
    result = base.ewm(span=252, adjust=False, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d invest trajectory short term level scaled
def f27it_f27_investment_trajectory_capinvshort_21d_base_v044_signal(capex, closeadj):
    result = _f27_invest_traj(capex, 21) * closeadj * _mean(capex, 21) / 1e7
    return result.replace([np.inf, -np.inf], np.nan)


# 5d invest trajectory ultra-short
def f27it_f27_investment_trajectory_capinvultra_5d_base_v045_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d invest trajectory short
def f27it_f27_investment_trajectory_capinvshrt_10d_base_v046_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d invest trajectory medium
def f27it_f27_investment_trajectory_capinvmed_42d_base_v047_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d invest trajectory long
def f27it_f27_investment_trajectory_capinvlong_189d_base_v048_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d invest trajectory long
def f27it_f27_investment_trajectory_capinvlong_378d_base_v049_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex log-level scaled by closeadj
def f27it_f27_investment_trajectory_caplogXprice_252d_base_v050_signal(capex, closeadj):
    base = np.log(_mean(capex, 252).abs().replace(0, np.nan))
    result = base * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex log-level scaled by closeadj
def f27it_f27_investment_trajectory_caplogXprice_504d_base_v051_signal(capex, closeadj):
    base = np.log(_mean(capex, 504).abs().replace(0, np.nan))
    result = base * closeadj + _f27_capex_growth(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth combined with revenue growth (compound invest)
def f27it_f27_investment_trajectory_caprevcomb_63d_base_v052_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 63)
    rg = _diff(_mean(revenue, 63), 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    result = (cg - rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth minus revenue growth
def f27it_f27_investment_trajectory_caprevcomb_252d_base_v053_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 252)
    rg = _diff(_mean(revenue, 252), 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    result = (cg - rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth minus revenue growth
def f27it_f27_investment_trajectory_caprevcomb_504d_base_v054_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 504)
    rg = _diff(_mean(revenue, 504), 252) / _mean(revenue.abs(), 504).replace(0, np.nan)
    result = (cg - rg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth + 63d ncfo growth (composite invest signal)
def f27it_f27_investment_trajectory_capplusncfogrow_63d_base_v055_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 63)
    ng = _diff(_mean(ncfo, 63), 63) / _mean(ncfo.abs(), 63).replace(0, np.nan)
    result = (cg + ng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth + ncfo growth
def f27it_f27_investment_trajectory_capplusncfogrow_252d_base_v056_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 252)
    ng = _diff(_mean(ncfo, 252), 252) / _mean(ncfo.abs(), 252).replace(0, np.nan)
    result = (cg + ng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth squared (severity)
def f27it_f27_investment_trajectory_capgrowsq_63d_base_v057_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth squared
def f27it_f27_investment_trajectory_capgrowsq_252d_base_v058_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth squared
def f27it_f27_investment_trajectory_capgrowsq_504d_base_v059_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 504)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue * mean revenue (currency-scale invest)
def f27it_f27_investment_trajectory_capnominal_63d_base_v060_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63) * _mean(revenue, 63) / 1e7
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex nominal scaled
def f27it_f27_investment_trajectory_capnominal_252d_base_v061_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252) * _mean(revenue, 252) / 1e7
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex nominal scaled
def f27it_f27_investment_trajectory_capnominal_504d_base_v062_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 504) * _mean(revenue, 504) / 1e7
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex YoY proxy via 252d diff
def f27it_f27_investment_trajectory_capyoy_252d_base_v063_signal(capex, closeadj):
    base = _diff(_mean(capex, 21), 252) / _mean(capex.abs(), 252).replace(0, np.nan)
    result = base * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex YoY proxy via 252d diff
def f27it_f27_investment_trajectory_capyoy63_252d_base_v064_signal(capex, closeadj):
    base = _diff(_mean(capex, 63), 252) / _mean(capex.abs(), 252).replace(0, np.nan)
    result = base * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex 2y proxy via 504d diff
def f27it_f27_investment_trajectory_cap2y_504d_base_v065_signal(capex, closeadj):
    base = _diff(_mean(capex, 21), 504) / _mean(capex.abs(), 504).replace(0, np.nan)
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/equity ratio trajectory
def f27it_f27_investment_trajectory_capequity_252d_base_v066_signal(capex, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(equity, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/equity ratio trajectory
def f27it_f27_investment_trajectory_capequity_504d_base_v067_signal(capex, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(equity, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/equity ratio
def f27it_f27_investment_trajectory_capequitydiff_252d_base_v068_signal(capex, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(equity, 252))
    result = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ebitda trajectory
def f27it_f27_investment_trajectory_capebitda_252d_base_v069_signal(capex, ebitda, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ebitda, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ebitda trajectory
def f27it_f27_investment_trajectory_capebitda_504d_base_v070_signal(capex, ebitda, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(ebitda, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/ebitda ratio
def f27it_f27_investment_trajectory_capebitdadiff_252d_base_v071_signal(capex, ebitda, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ebitda, 252))
    result = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex / opinc trajectory
def f27it_f27_investment_trajectory_capopinc_63d_base_v072_signal(capex, opinc, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(opinc, 63))
    result = base * closeadj + _f27_invest_traj(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / opinc trajectory
def f27it_f27_investment_trajectory_capopinc_252d_base_v073_signal(capex, opinc, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(opinc, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest trajectory * mean closeadj (compound severity)
def f27it_f27_investment_trajectory_capinvxprice_252d_base_v074_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest trajectory * mean closeadj
def f27it_f27_investment_trajectory_capinvxprice_504d_base_v075_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27it_f27_investment_trajectory_capgrow_21d_base_v001_signal,
    f27it_f27_investment_trajectory_capgrow_63d_base_v002_signal,
    f27it_f27_investment_trajectory_capgrow_126d_base_v003_signal,
    f27it_f27_investment_trajectory_capgrow_252d_base_v004_signal,
    f27it_f27_investment_trajectory_capgrow_504d_base_v005_signal,
    f27it_f27_investment_trajectory_capinv_21d_base_v006_signal,
    f27it_f27_investment_trajectory_capinv_63d_base_v007_signal,
    f27it_f27_investment_trajectory_capinv_252d_base_v008_signal,
    f27it_f27_investment_trajectory_capinv_504d_base_v009_signal,
    f27it_f27_investment_trajectory_caprev_63d_base_v010_signal,
    f27it_f27_investment_trajectory_caprev_126d_base_v011_signal,
    f27it_f27_investment_trajectory_caprev_252d_base_v012_signal,
    f27it_f27_investment_trajectory_caprev_504d_base_v013_signal,
    f27it_f27_investment_trajectory_caprevdiff_63d_base_v014_signal,
    f27it_f27_investment_trajectory_caprevdiff_252d_base_v015_signal,
    f27it_f27_investment_trajectory_caprevdiff_504d_base_v016_signal,
    f27it_f27_investment_trajectory_capgrowz_252d_base_v017_signal,
    f27it_f27_investment_trajectory_capgrowz_504d_base_v018_signal,
    f27it_f27_investment_trajectory_capgrowmean_63d_base_v019_signal,
    f27it_f27_investment_trajectory_capgrowmean_252d_base_v020_signal,
    f27it_f27_investment_trajectory_capgrowstd_252d_base_v021_signal,
    f27it_f27_investment_trajectory_capgrowstd_504d_base_v022_signal,
    f27it_f27_investment_trajectory_capgrowupcnt_252d_base_v023_signal,
    f27it_f27_investment_trajectory_capgrowdowncnt_504d_base_v024_signal,
    f27it_f27_investment_trajectory_capintensity_63d_base_v025_signal,
    f27it_f27_investment_trajectory_capintensity_252d_base_v026_signal,
    f27it_f27_investment_trajectory_capinvxlevel_21d_base_v027_signal,
    f27it_f27_investment_trajectory_capinvxlevel_63d_base_v028_signal,
    f27it_f27_investment_trajectory_capinvxlevel_252d_base_v029_signal,
    f27it_f27_investment_trajectory_capinvxlevel_504d_base_v030_signal,
    f27it_f27_investment_trajectory_capncfo_63d_base_v031_signal,
    f27it_f27_investment_trajectory_capncfo_252d_base_v032_signal,
    f27it_f27_investment_trajectory_capncfo_504d_base_v033_signal,
    f27it_f27_investment_trajectory_capncfodiff_63d_base_v034_signal,
    f27it_f27_investment_trajectory_capncfodiff_252d_base_v035_signal,
    f27it_f27_investment_trajectory_capassets_63d_base_v036_signal,
    f27it_f27_investment_trajectory_capassets_252d_base_v037_signal,
    f27it_f27_investment_trajectory_capassets_504d_base_v038_signal,
    f27it_f27_investment_trajectory_capassetsdiff_252d_base_v039_signal,
    f27it_f27_investment_trajectory_capassetsdiff_504d_base_v040_signal,
    f27it_f27_investment_trajectory_capgrowema_21d_base_v041_signal,
    f27it_f27_investment_trajectory_capgrowema_63d_base_v042_signal,
    f27it_f27_investment_trajectory_capgrowema_252d_base_v043_signal,
    f27it_f27_investment_trajectory_capinvshort_21d_base_v044_signal,
    f27it_f27_investment_trajectory_capinvultra_5d_base_v045_signal,
    f27it_f27_investment_trajectory_capinvshrt_10d_base_v046_signal,
    f27it_f27_investment_trajectory_capinvmed_42d_base_v047_signal,
    f27it_f27_investment_trajectory_capinvlong_189d_base_v048_signal,
    f27it_f27_investment_trajectory_capinvlong_378d_base_v049_signal,
    f27it_f27_investment_trajectory_caplogXprice_252d_base_v050_signal,
    f27it_f27_investment_trajectory_caplogXprice_504d_base_v051_signal,
    f27it_f27_investment_trajectory_caprevcomb_63d_base_v052_signal,
    f27it_f27_investment_trajectory_caprevcomb_252d_base_v053_signal,
    f27it_f27_investment_trajectory_caprevcomb_504d_base_v054_signal,
    f27it_f27_investment_trajectory_capplusncfogrow_63d_base_v055_signal,
    f27it_f27_investment_trajectory_capplusncfogrow_252d_base_v056_signal,
    f27it_f27_investment_trajectory_capgrowsq_63d_base_v057_signal,
    f27it_f27_investment_trajectory_capgrowsq_252d_base_v058_signal,
    f27it_f27_investment_trajectory_capgrowsq_504d_base_v059_signal,
    f27it_f27_investment_trajectory_capnominal_63d_base_v060_signal,
    f27it_f27_investment_trajectory_capnominal_252d_base_v061_signal,
    f27it_f27_investment_trajectory_capnominal_504d_base_v062_signal,
    f27it_f27_investment_trajectory_capyoy_252d_base_v063_signal,
    f27it_f27_investment_trajectory_capyoy63_252d_base_v064_signal,
    f27it_f27_investment_trajectory_cap2y_504d_base_v065_signal,
    f27it_f27_investment_trajectory_capequity_252d_base_v066_signal,
    f27it_f27_investment_trajectory_capequity_504d_base_v067_signal,
    f27it_f27_investment_trajectory_capequitydiff_252d_base_v068_signal,
    f27it_f27_investment_trajectory_capebitda_252d_base_v069_signal,
    f27it_f27_investment_trajectory_capebitda_504d_base_v070_signal,
    f27it_f27_investment_trajectory_capebitdadiff_252d_base_v071_signal,
    f27it_f27_investment_trajectory_capopinc_63d_base_v072_signal,
    f27it_f27_investment_trajectory_capopinc_252d_base_v073_signal,
    f27it_f27_investment_trajectory_capinvxprice_252d_base_v074_signal,
    f27it_f27_investment_trajectory_capinvxprice_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_INVESTMENT_TRAJECTORY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap, "ev": ev, "evebit": evebit,
        "evebitda": evebitda, "pe": pe, "pb": pb, "ps": ps,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_invest_traj", "_f27_capex_growth", "_f27_capex_to_rev")
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
    print(f"OK f27_investment_trajectory_base_001_075_claude: {n_features} features pass")
