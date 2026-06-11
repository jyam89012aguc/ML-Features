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


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan).shift(w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f27_invest_traj(capex, w):
    base = _mean(capex, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f27_capex_growth(capex, w):
    return _diff(_mean(capex, w), w) / _mean(capex.abs(), w).replace(0, np.nan)


def _f27_capex_to_rev(capex, revenue, w):
    return _safe_div(_mean(capex, w), _mean(revenue, w))


# 5d jerk of 21d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_21d_jerk_v001_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_21d_jerk_v002_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_63d_jerk_v003_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_63d_jerk_v004_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_63d_jerk_v005_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_126d_jerk_v006_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_126d_jerk_v007_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_252d_jerk_v008_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_252d_jerk_v009_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_504d_jerk_v010_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d capex growth × closeadj
def f27it_f27_investment_trajectory_capgrow_504d_jerk_v011_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d invest trajectory × closeadj
def f27it_f27_investment_trajectory_capinv_21d_jerk_v012_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d invest trajectory × closeadj
def f27it_f27_investment_trajectory_capinv_63d_jerk_v013_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d invest trajectory × closeadj
def f27it_f27_investment_trajectory_capinv_252d_jerk_v014_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d invest trajectory × closeadj
def f27it_f27_investment_trajectory_capinv_504d_jerk_v015_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d capex/rev × closeadj
def f27it_f27_investment_trajectory_caprev_63d_jerk_v016_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d capex/rev × closeadj
def f27it_f27_investment_trajectory_caprev_126d_jerk_v017_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d capex/rev × closeadj
def f27it_f27_investment_trajectory_caprev_252d_jerk_v018_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d capex/rev × closeadj
def f27it_f27_investment_trajectory_caprev_504d_jerk_v019_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of zscore capex growth 252d × closeadj
def f27it_f27_investment_trajectory_capgrowz_252d_jerk_v020_signal(capex, closeadj):
    base = _z(_f27_capex_growth(capex, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of zscore capex growth long × closeadj
def f27it_f27_investment_trajectory_capgrowz_504d_jerk_v021_signal(capex, closeadj):
    base = _z(_f27_capex_growth(capex, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of mean capex growth × closeadj
def f27it_f27_investment_trajectory_capgrowmean_63d_jerk_v022_signal(capex, closeadj):
    base = _mean(_f27_capex_growth(capex, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of mean capex growth long × closeadj
def f27it_f27_investment_trajectory_capgrowmean_252d_jerk_v023_signal(capex, closeadj):
    base = _mean(_f27_capex_growth(capex, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of std capex growth × closeadj
def f27it_f27_investment_trajectory_capgrowstd_252d_jerk_v024_signal(capex, closeadj):
    base = _std(_f27_capex_growth(capex, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of std capex growth long × closeadj
def f27it_f27_investment_trajectory_capgrowstd_504d_jerk_v025_signal(capex, closeadj):
    base = _std(_f27_capex_growth(capex, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow upcount × closeadj
def f27it_f27_investment_trajectory_capgrowupcnt_252d_jerk_v026_signal(capex, closeadj):
    flag = (_f27_capex_growth(capex, 21) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow downcount × closeadj
def f27it_f27_investment_trajectory_capgrowdowncnt_504d_jerk_v027_signal(capex, closeadj):
    flag = (_f27_capex_growth(capex, 63) < 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capex/rev intensity short × closeadj
def f27it_f27_investment_trajectory_capintensity_63d_jerk_v028_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/rev intensity long × closeadj
def f27it_f27_investment_trajectory_capintensity_252d_jerk_v029_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of invest at level 21d × closeadj
def f27it_f27_investment_trajectory_capinvxlevel_21d_jerk_v030_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 21) * _mean(capex, 21) / 1e6 * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of invest at level 63d × closeadj
def f27it_f27_investment_trajectory_capinvxlevel_63d_jerk_v031_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 63) * _mean(capex, 63) / 1e6 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of invest at level 252d × closeadj
def f27it_f27_investment_trajectory_capinvxlevel_252d_jerk_v032_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252) * _mean(capex, 252) / 1e6 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of invest at level 504d × closeadj
def f27it_f27_investment_trajectory_capinvxlevel_504d_jerk_v033_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504) * _mean(capex, 504) / 1e6 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capex/ncfo 63d × closeadj
def f27it_f27_investment_trajectory_capncfo_63d_jerk_v034_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(ncfo, 63)) * closeadj + _f27_capex_growth(capex, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ncfo 252d × closeadj
def f27it_f27_investment_trajectory_capncfo_252d_jerk_v035_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ncfo, 252)) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ncfo 504d × closeadj
def f27it_f27_investment_trajectory_capncfo_504d_jerk_v036_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(ncfo, 504)) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/assets 63d × closeadj
def f27it_f27_investment_trajectory_capassets_63d_jerk_v037_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(assets, 63)) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/assets 252d × closeadj
def f27it_f27_investment_trajectory_capassets_252d_jerk_v038_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/assets 504d × closeadj
def f27it_f27_investment_trajectory_capassets_504d_jerk_v039_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EMA capex growth 21d × closeadj
def f27it_f27_investment_trajectory_capgrowema_21d_jerk_v040_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21).ewm(span=21, adjust=False, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EMA capex growth 63d × closeadj
def f27it_f27_investment_trajectory_capgrowema_63d_jerk_v041_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EMA capex growth 252d × closeadj
def f27it_f27_investment_trajectory_capgrowema_252d_jerk_v042_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252).ewm(span=252, adjust=False, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of invest ultra-short × closeadj
def f27it_f27_investment_trajectory_capinvultra_5d_jerk_v043_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of invest 10d × closeadj
def f27it_f27_investment_trajectory_capinvshrt_10d_jerk_v044_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of invest 42d × closeadj
def f27it_f27_investment_trajectory_capinvmed_42d_jerk_v045_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of invest 189d × closeadj
def f27it_f27_investment_trajectory_capinvlong_189d_jerk_v046_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of invest 378d × closeadj
def f27it_f27_investment_trajectory_capinvlong_378d_jerk_v047_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex log-level 252d × closeadj
def f27it_f27_investment_trajectory_caplogXprice_252d_jerk_v048_signal(capex, closeadj):
    base = np.log(_mean(capex, 252).abs().replace(0, np.nan)) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex log-level 504d × closeadj
def f27it_f27_investment_trajectory_caplogXprice_504d_jerk_v049_signal(capex, closeadj):
    base = np.log(_mean(capex, 504).abs().replace(0, np.nan)) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (capgrow - revgrow) 63d × closeadj
def f27it_f27_investment_trajectory_caprevcomb_63d_jerk_v050_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 63)
    rg = _diff(_mean(revenue, 63), 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    base = (cg - rg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (capgrow - revgrow) 252d × closeadj
def f27it_f27_investment_trajectory_caprevcomb_252d_jerk_v051_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 252)
    rg = _diff(_mean(revenue, 252), 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    base = (cg - rg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of (capgrow - revgrow) 504d × closeadj
def f27it_f27_investment_trajectory_caprevcomb_504d_jerk_v052_signal(capex, revenue, closeadj):
    cg = _f27_capex_growth(capex, 504)
    rg = _diff(_mean(revenue, 504), 252) / _mean(revenue.abs(), 504).replace(0, np.nan)
    base = (cg - rg) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow+ncfogrow 63d × closeadj
def f27it_f27_investment_trajectory_capplusncfogrow_63d_jerk_v053_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 63)
    ng = _diff(_mean(ncfo, 63), 63) / _mean(ncfo.abs(), 63).replace(0, np.nan)
    base = (cg + ng) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow+ncfogrow 252d × closeadj
def f27it_f27_investment_trajectory_capplusncfogrow_252d_jerk_v054_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 252)
    ng = _diff(_mean(ncfo, 252), 252) / _mean(ncfo.abs(), 252).replace(0, np.nan)
    base = (cg + ng) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow squared 63d × closeadj
def f27it_f27_investment_trajectory_capgrowsq_63d_jerk_v055_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    base = g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow squared 252d × closeadj
def f27it_f27_investment_trajectory_capgrowsq_252d_jerk_v056_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow squared 504d × closeadj
def f27it_f27_investment_trajectory_capgrowsq_504d_jerk_v057_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 504)
    base = g * g.abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capnominal 63d × closeadj
def f27it_f27_investment_trajectory_capnominal_63d_jerk_v058_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63) * _mean(revenue, 63) / 1e7 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capnominal 252d × closeadj
def f27it_f27_investment_trajectory_capnominal_252d_jerk_v059_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252) * _mean(revenue, 252) / 1e7 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capnominal 504d × closeadj
def f27it_f27_investment_trajectory_capnominal_504d_jerk_v060_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 504) * _mean(revenue, 504) / 1e7 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capYoY 252d × closeadj
def f27it_f27_investment_trajectory_capyoy_252d_jerk_v061_signal(capex, closeadj):
    base = _diff(_mean(capex, 21), 252) / _mean(capex.abs(), 252).replace(0, np.nan) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capYoY63 252d × closeadj
def f27it_f27_investment_trajectory_capyoy63_252d_jerk_v062_signal(capex, closeadj):
    base = _diff(_mean(capex, 63), 252) / _mean(capex.abs(), 252).replace(0, np.nan) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cap2y 504d × closeadj
def f27it_f27_investment_trajectory_cap2y_504d_jerk_v063_signal(capex, closeadj):
    base = _diff(_mean(capex, 21), 504) / _mean(capex.abs(), 504).replace(0, np.nan) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/equity 252d × closeadj
def f27it_f27_investment_trajectory_capequity_252d_jerk_v064_signal(capex, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(equity, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/equity 504d × closeadj
def f27it_f27_investment_trajectory_capequity_504d_jerk_v065_signal(capex, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(equity, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/ebitda 252d × closeadj
def f27it_f27_investment_trajectory_capebitda_252d_jerk_v066_signal(capex, ebitda, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ebitda, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/ebitda 504d × closeadj
def f27it_f27_investment_trajectory_capebitda_504d_jerk_v067_signal(capex, ebitda, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(ebitda, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capex/opinc 63d × closeadj
def f27it_f27_investment_trajectory_capopinc_63d_jerk_v068_signal(capex, opinc, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(opinc, 63)) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/opinc 252d × closeadj
def f27it_f27_investment_trajectory_capopinc_252d_jerk_v069_signal(capex, opinc, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(opinc, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of invest×price 252d × closeadj
def f27it_f27_investment_trajectory_capinvxprice_252d_jerk_v070_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of invest×price 504d × closeadj
def f27it_f27_investment_trajectory_capinvxprice_504d_jerk_v071_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504) * _mean(closeadj, 504)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow×mom 21d × closeadj
def f27it_f27_investment_trajectory_capgrowxmom_21d_jerk_v072_signal(capex, closeadj):
    mom = closeadj.pct_change(21)
    base = _f27_capex_growth(capex, 21) * (1.0 + mom) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow×mom 63d × closeadj
def f27it_f27_investment_trajectory_capgrowxmom_63d_jerk_v073_signal(capex, closeadj):
    mom = closeadj.pct_change(63)
    base = _f27_capex_growth(capex, 63) * (1.0 + mom) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow×mom 252d × closeadj
def f27it_f27_investment_trajectory_capgrowxmom_252d_jerk_v074_signal(capex, closeadj):
    mom = closeadj.pct_change(252)
    base = _f27_capex_growth(capex, 252) * (1.0 + mom) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/rev z 252d × closeadj
def f27it_f27_investment_trajectory_capreviz_252d_jerk_v075_signal(capex, revenue, closeadj):
    base = _z(_f27_capex_to_rev(capex, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/rev z 504d × closeadj
def f27it_f27_investment_trajectory_capreviz_504d_jerk_v076_signal(capex, revenue, closeadj):
    base = _z(_f27_capex_to_rev(capex, revenue, 252), 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrowabs 63d × closeadj
def f27it_f27_investment_trajectory_capgrowabs_63d_jerk_v077_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrowabs 252d × closeadj
def f27it_f27_investment_trajectory_capgrowabs_252d_jerk_v078_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrowabs 504d × closeadj
def f27it_f27_investment_trajectory_capgrowabs_504d_jerk_v079_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 504).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow CV 252d × closeadj
def f27it_f27_investment_trajectory_capgrowcv_252d_jerk_v080_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    base = _safe_div(_std(g, 252), _mean(g, 252).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow CV 504d × closeadj
def f27it_f27_investment_trajectory_capgrowcv_504d_jerk_v081_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 252)
    base = _safe_div(_std(g, 504), _mean(g, 504).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/fcf 252d × closeadj
def f27it_f27_investment_trajectory_capfcf_252d_jerk_v082_signal(capex, fcf, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(fcf, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/fcf 504d × closeadj
def f27it_f27_investment_trajectory_capfcf_504d_jerk_v083_signal(capex, fcf, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(fcf, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/netinc 252d × closeadj
def f27it_f27_investment_trajectory_capnetinc_252d_jerk_v084_signal(capex, netinc, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(netinc, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capex/netinc 504d × closeadj
def f27it_f27_investment_trajectory_capnetinc_504d_jerk_v085_signal(capex, netinc, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(netinc, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capex/gp 63d × closeadj
def f27it_f27_investment_trajectory_capgp_63d_jerk_v086_signal(capex, gp, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(gp, 63)) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex/gp 252d × closeadj
def f27it_f27_investment_trajectory_capgp_252d_jerk_v087_signal(capex, gp, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(gp, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow accel 252 × closeadj
def f27it_f27_investment_trajectory_capgrowaccel_252d_jerk_v088_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    base = _diff(g, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow accel 504 × closeadj
def f27it_f27_investment_trajectory_capgrowaccel_504d_jerk_v089_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 252)
    base = _diff(g, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow ratio 63v252 × closeadj
def f27it_f27_investment_trajectory_capgrowratio_63v252_jerk_v090_signal(capex, closeadj):
    sg = _f27_capex_growth(capex, 63)
    lg = _f27_capex_growth(capex, 252).replace(0, np.nan)
    base = (sg / lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow ratio 21v63 × closeadj
def f27it_f27_investment_trajectory_capgrowratio_21v63_jerk_v091_signal(capex, closeadj):
    sg = _f27_capex_growth(capex, 21)
    lg = _f27_capex_growth(capex, 63).replace(0, np.nan)
    base = (sg / lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow+ratio 63d × closeadj
def f27it_f27_investment_trajectory_capgrowplusratio_63d_jerk_v092_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 63)
    r = _f27_capex_to_rev(capex, revenue, 63)
    base = (g + r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow+ratio 252d × closeadj
def f27it_f27_investment_trajectory_capgrowplusratio_252d_jerk_v093_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    r = _f27_capex_to_rev(capex, revenue, 252)
    base = (g + r) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow+ratio 504d × closeadj
def f27it_f27_investment_trajectory_capgrowplusratio_504d_jerk_v094_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 504)
    r = _f27_capex_to_rev(capex, revenue, 504)
    base = (g + r) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxmcap 252d
def f27it_f27_investment_trajectory_capxmcap_252d_jerk_v095_signal(capex, revenue, marketcap):
    base = _f27_capex_to_rev(capex, revenue, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxmcap 504d
def f27it_f27_investment_trajectory_capxmcap_504d_jerk_v096_signal(capex, revenue, marketcap):
    base = _f27_capex_to_rev(capex, revenue, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow ema short × closeadj
def f27it_f27_investment_trajectory_capgrowemashrt_21d_jerk_v097_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21).ewm(span=10, adjust=False, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow ema long × closeadj
def f27it_f27_investment_trajectory_capgrowemalong_252d_jerk_v098_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63).ewm(span=252, adjust=False, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow skew 252d × closeadj
def f27it_f27_investment_trajectory_capgrowskew_252d_jerk_v099_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21).rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow skew 504d × closeadj
def f27it_f27_investment_trajectory_capgrowskew_504d_jerk_v100_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63).rolling(504, min_periods=126).skew() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow kurt 252d × closeadj
def f27it_f27_investment_trajectory_capgrowkurt_252d_jerk_v101_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21).rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow kurt 504d × closeadj
def f27it_f27_investment_trajectory_capgrowkurt_504d_jerk_v102_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63).rolling(504, min_periods=126).kurt() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capex composite 252d × closeadj
def f27it_f27_investment_trajectory_capcomposite_252d_jerk_v103_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    r = _f27_capex_to_rev(capex, revenue, 252)
    base = (g + r * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capinv×rev 63d × closeadj
def f27it_f27_investment_trajectory_capinvxrev_63d_jerk_v104_signal(capex, revenue, closeadj):
    base = _f27_invest_traj(capex, 63) * _mean(revenue, 63) / 1e8 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capinv×rev 252d × closeadj
def f27it_f27_investment_trajectory_capinvxrev_252d_jerk_v105_signal(capex, revenue, closeadj):
    base = _f27_invest_traj(capex, 252) * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxrevassets 252d
def f27it_f27_investment_trajectory_capxrevassets_252d_jerk_v106_signal(capex, revenue, assets):
    base = _f27_capex_to_rev(capex, revenue, 252) * _safe_div(_mean(revenue, 252), _mean(assets, 252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxrevassets 504d
def f27it_f27_investment_trajectory_capxrevassets_504d_jerk_v107_signal(capex, revenue, assets):
    base = _f27_capex_to_rev(capex, revenue, 504) * _safe_div(_mean(revenue, 504), _mean(assets, 504))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capgrow×std 21d × closeadj
def f27it_f27_investment_trajectory_capgrowxstd_21d_jerk_v108_signal(capex, closeadj):
    sd = _std(closeadj.pct_change(), 21)
    base = _f27_capex_growth(capex, 21) * (1.0 + sd) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow×std 252d × closeadj
def f27it_f27_investment_trajectory_capgrowxstd_252d_jerk_v109_signal(capex, closeadj):
    sd = _std(closeadj.pct_change(), 252)
    base = _f27_capex_growth(capex, 252) * (1.0 + sd) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capvsncfogrow 252d × closeadj
def f27it_f27_investment_trajectory_capvsncfogrow_252d_jerk_v110_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 252)
    ng = _diff(_mean(ncfo, 252), 252) / _mean(ncfo.abs(), 252).replace(0, np.nan)
    base = (cg / ng.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capvsncfogrow 504d × closeadj
def f27it_f27_investment_trajectory_capvsncfogrow_504d_jerk_v111_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 504)
    ng = _diff(_mean(ncfo, 504), 252) / _mean(ncfo.abs(), 504).replace(0, np.nan)
    base = (cg / ng.replace(0, np.nan)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capinvmom 252d × closeadj
def f27it_f27_investment_trajectory_capinvmom_252d_jerk_v112_signal(capex, closeadj):
    ret = closeadj.pct_change(252)
    base = _f27_invest_traj(capex, 252) * (1.0 + ret) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capinvmom 504d × closeadj
def f27it_f27_investment_trajectory_capinvmom_504d_jerk_v113_signal(capex, closeadj):
    ret = closeadj.pct_change(504)
    base = _f27_invest_traj(capex, 504) * (1.0 + ret) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxrevcfo 252d × closeadj
def f27it_f27_investment_trajectory_capxrevcfo_252d_jerk_v114_signal(capex, revenue, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(revenue + ncfo, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxrevcfo 504d × closeadj
def f27it_f27_investment_trajectory_capxrevcfo_504d_jerk_v115_signal(capex, revenue, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(revenue + ncfo, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxassetseq 252d × closeadj
def f27it_f27_investment_trajectory_capxassetseq_252d_jerk_v116_signal(capex, assets, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets + equity, 252)) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxassetseq 504d × closeadj
def f27it_f27_investment_trajectory_capxassetseq_504d_jerk_v117_signal(capex, assets, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets + equity, 504)) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capyoyraw 252d × closeadj
def f27it_f27_investment_trajectory_capyoyraw_252d_jerk_v118_signal(capex, closeadj):
    base = _diff(capex, 252) / _mean(capex.abs(), 252).replace(0, np.nan) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cap2yraw 504d × closeadj
def f27it_f27_investment_trajectory_cap2yraw_504d_jerk_v119_signal(capex, closeadj):
    base = _diff(capex, 504) / _mean(capex.abs(), 504).replace(0, np.nan) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cap1mraw 21d × closeadj
def f27it_f27_investment_trajectory_cap1mraw_21d_jerk_v120_signal(capex, closeadj):
    base = _diff(capex, 21) / _mean(capex.abs(), 21).replace(0, np.nan) * closeadj + _f27_capex_growth(capex, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cap1qraw 63d × closeadj
def f27it_f27_investment_trajectory_cap1qraw_63d_jerk_v121_signal(capex, closeadj):
    base = _diff(capex, 63) / _mean(capex.abs(), 63).replace(0, np.nan) * closeadj + _f27_capex_growth(capex, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capshare 252d × closeadj
def f27it_f27_investment_trajectory_capshare_252d_jerk_v122_signal(capex, sharesbas, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(sharesbas, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capshare 504d × closeadj
def f27it_f27_investment_trajectory_capshare_504d_jerk_v123_signal(capex, sharesbas, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(sharesbas, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxcap 252d × closeadj
def f27it_f27_investment_trajectory_capxcap_252d_jerk_v124_signal(capex, debt, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(debt + equity, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxcap 504d × closeadj
def f27it_f27_investment_trajectory_capxcap_504d_jerk_v125_signal(capex, debt, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(debt + equity, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capnet 63d × closeadj
def f27it_f27_investment_trajectory_capnet_63d_jerk_v126_signal(capex, ncfo, closeadj):
    invflow = _mean(capex, 63) - 0.5 * _mean(ncfo, 63)
    base = invflow * _f27_capex_growth(capex, 63).fillna(0).abs() * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capnet 252d × closeadj
def f27it_f27_investment_trajectory_capnet_252d_jerk_v127_signal(capex, ncfo, closeadj):
    invflow = _mean(capex, 252) - 0.5 * _mean(ncfo, 252)
    base = invflow * _f27_capex_growth(capex, 252).fillna(0).abs() * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrowinstability 252d × closeadj
def f27it_f27_investment_trajectory_capgrowinstability_252d_jerk_v128_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    base = _safe_div(_std(g, 252), _mean(g.abs(), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrowinstability 504d × closeadj
def f27it_f27_investment_trajectory_capgrowinstability_504d_jerk_v129_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    base = _safe_div(_std(g, 504), _mean(g.abs(), 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capaccelcnt 252d × closeadj
def f27it_f27_investment_trajectory_capaccelcnt_252d_jerk_v130_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    flag = (g.diff(21) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capaccelcnt 504d × closeadj
def f27it_f27_investment_trajectory_capaccelcnt_504d_jerk_v131_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    flag = (g.diff(63) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capsignsum 252d × closeadj
def f27it_f27_investment_trajectory_capsignsum_252d_jerk_v132_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capsignsum 504d × closeadj
def f27it_f27_investment_trajectory_capsignsum_504d_jerk_v133_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of caprev vs mean 252d × closeadj
def f27it_f27_investment_trajectory_caprevvsmean_252d_jerk_v134_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of caprev vs mean 504d × closeadj
def f27it_f27_investment_trajectory_caprevvsmean_504d_jerk_v135_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252)
    base = (base - _mean(base, 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capinv expanded 252d × closeadj
def f27it_f27_investment_trajectory_capinvexp_252d_jerk_v136_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252)
    base = base * base.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capinv expanded 504d × closeadj
def f27it_f27_investment_trajectory_capinvexp_504d_jerk_v137_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504)
    base = base * base.abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxretcum 252d × closeadj
def f27it_f27_investment_trajectory_capxretcum_252d_jerk_v138_signal(capex, closeadj):
    cret = closeadj / closeadj.shift(252).replace(0, np.nan)
    base = _f27_invest_traj(capex, 252) * cret * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxretcum 504d × closeadj
def f27it_f27_investment_trajectory_capxretcum_504d_jerk_v139_signal(capex, closeadj):
    cret = closeadj / closeadj.shift(504).replace(0, np.nan)
    base = _f27_invest_traj(capex, 504) * cret * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow×rev 252d × closeadj
def f27it_f27_investment_trajectory_capgrowxrev_252d_jerk_v140_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    base = g * _mean(revenue, 252) / 1e8 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow×rev 504d × closeadj
def f27it_f27_investment_trajectory_capgrowxrev_504d_jerk_v141_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 504)
    base = g * _mean(revenue, 504) / 1e8 * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capxopncfo 252d × closeadj
def f27it_f27_investment_trajectory_capxopncfo_252d_jerk_v142_signal(capex, opinc, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(opinc + ncfo, 252)) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capxopncfo 504d × closeadj
def f27it_f27_investment_trajectory_capxopncfo_504d_jerk_v143_signal(capex, opinc, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(opinc + ncfo, 504)) * closeadj + _f27_invest_traj(capex, 504) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capgrow area 252d × closeadj
def f27it_f27_investment_trajectory_capgrowarea_252d_jerk_v144_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21).abs()
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of capgrow area 504d × closeadj
def f27it_f27_investment_trajectory_capgrowarea_504d_jerk_v145_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63).abs()
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capyoyraw 504d × closeadj
def f27it_f27_investment_trajectory_capyoyraw_504d_jerk_v146_signal(capex, closeadj):
    base = _diff(capex, 252) / _mean(capex.abs(), 252).replace(0, np.nan) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capassetsdiff 252d × closeadj
def f27it_f27_investment_trajectory_capassetsdiff_252d_jerk_v147_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets, 252))
    base = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capassetsdiff 504d × closeadj
def f27it_f27_investment_trajectory_capassetsdiff_504d_jerk_v148_signal(capex, assets, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets, 504))
    base = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 504) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of capncfodiff 63d × closeadj
def f27it_f27_investment_trajectory_capncfodiff_63d_jerk_v149_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(ncfo, 63))
    base = _diff(base, 63) * closeadj + _f27_invest_traj(capex, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of capncfodiff 252d × closeadj
def f27it_f27_investment_trajectory_capncfodiff_252d_jerk_v150_signal(capex, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(ncfo, 252))
    base = _diff(base, 252) * closeadj + _f27_invest_traj(capex, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27it_f27_investment_trajectory_capgrow_21d_jerk_v001_signal,
    f27it_f27_investment_trajectory_capgrow_21d_jerk_v002_signal,
    f27it_f27_investment_trajectory_capgrow_63d_jerk_v003_signal,
    f27it_f27_investment_trajectory_capgrow_63d_jerk_v004_signal,
    f27it_f27_investment_trajectory_capgrow_63d_jerk_v005_signal,
    f27it_f27_investment_trajectory_capgrow_126d_jerk_v006_signal,
    f27it_f27_investment_trajectory_capgrow_126d_jerk_v007_signal,
    f27it_f27_investment_trajectory_capgrow_252d_jerk_v008_signal,
    f27it_f27_investment_trajectory_capgrow_252d_jerk_v009_signal,
    f27it_f27_investment_trajectory_capgrow_504d_jerk_v010_signal,
    f27it_f27_investment_trajectory_capgrow_504d_jerk_v011_signal,
    f27it_f27_investment_trajectory_capinv_21d_jerk_v012_signal,
    f27it_f27_investment_trajectory_capinv_63d_jerk_v013_signal,
    f27it_f27_investment_trajectory_capinv_252d_jerk_v014_signal,
    f27it_f27_investment_trajectory_capinv_504d_jerk_v015_signal,
    f27it_f27_investment_trajectory_caprev_63d_jerk_v016_signal,
    f27it_f27_investment_trajectory_caprev_126d_jerk_v017_signal,
    f27it_f27_investment_trajectory_caprev_252d_jerk_v018_signal,
    f27it_f27_investment_trajectory_caprev_504d_jerk_v019_signal,
    f27it_f27_investment_trajectory_capgrowz_252d_jerk_v020_signal,
    f27it_f27_investment_trajectory_capgrowz_504d_jerk_v021_signal,
    f27it_f27_investment_trajectory_capgrowmean_63d_jerk_v022_signal,
    f27it_f27_investment_trajectory_capgrowmean_252d_jerk_v023_signal,
    f27it_f27_investment_trajectory_capgrowstd_252d_jerk_v024_signal,
    f27it_f27_investment_trajectory_capgrowstd_504d_jerk_v025_signal,
    f27it_f27_investment_trajectory_capgrowupcnt_252d_jerk_v026_signal,
    f27it_f27_investment_trajectory_capgrowdowncnt_504d_jerk_v027_signal,
    f27it_f27_investment_trajectory_capintensity_63d_jerk_v028_signal,
    f27it_f27_investment_trajectory_capintensity_252d_jerk_v029_signal,
    f27it_f27_investment_trajectory_capinvxlevel_21d_jerk_v030_signal,
    f27it_f27_investment_trajectory_capinvxlevel_63d_jerk_v031_signal,
    f27it_f27_investment_trajectory_capinvxlevel_252d_jerk_v032_signal,
    f27it_f27_investment_trajectory_capinvxlevel_504d_jerk_v033_signal,
    f27it_f27_investment_trajectory_capncfo_63d_jerk_v034_signal,
    f27it_f27_investment_trajectory_capncfo_252d_jerk_v035_signal,
    f27it_f27_investment_trajectory_capncfo_504d_jerk_v036_signal,
    f27it_f27_investment_trajectory_capassets_63d_jerk_v037_signal,
    f27it_f27_investment_trajectory_capassets_252d_jerk_v038_signal,
    f27it_f27_investment_trajectory_capassets_504d_jerk_v039_signal,
    f27it_f27_investment_trajectory_capgrowema_21d_jerk_v040_signal,
    f27it_f27_investment_trajectory_capgrowema_63d_jerk_v041_signal,
    f27it_f27_investment_trajectory_capgrowema_252d_jerk_v042_signal,
    f27it_f27_investment_trajectory_capinvultra_5d_jerk_v043_signal,
    f27it_f27_investment_trajectory_capinvshrt_10d_jerk_v044_signal,
    f27it_f27_investment_trajectory_capinvmed_42d_jerk_v045_signal,
    f27it_f27_investment_trajectory_capinvlong_189d_jerk_v046_signal,
    f27it_f27_investment_trajectory_capinvlong_378d_jerk_v047_signal,
    f27it_f27_investment_trajectory_caplogXprice_252d_jerk_v048_signal,
    f27it_f27_investment_trajectory_caplogXprice_504d_jerk_v049_signal,
    f27it_f27_investment_trajectory_caprevcomb_63d_jerk_v050_signal,
    f27it_f27_investment_trajectory_caprevcomb_252d_jerk_v051_signal,
    f27it_f27_investment_trajectory_caprevcomb_504d_jerk_v052_signal,
    f27it_f27_investment_trajectory_capplusncfogrow_63d_jerk_v053_signal,
    f27it_f27_investment_trajectory_capplusncfogrow_252d_jerk_v054_signal,
    f27it_f27_investment_trajectory_capgrowsq_63d_jerk_v055_signal,
    f27it_f27_investment_trajectory_capgrowsq_252d_jerk_v056_signal,
    f27it_f27_investment_trajectory_capgrowsq_504d_jerk_v057_signal,
    f27it_f27_investment_trajectory_capnominal_63d_jerk_v058_signal,
    f27it_f27_investment_trajectory_capnominal_252d_jerk_v059_signal,
    f27it_f27_investment_trajectory_capnominal_504d_jerk_v060_signal,
    f27it_f27_investment_trajectory_capyoy_252d_jerk_v061_signal,
    f27it_f27_investment_trajectory_capyoy63_252d_jerk_v062_signal,
    f27it_f27_investment_trajectory_cap2y_504d_jerk_v063_signal,
    f27it_f27_investment_trajectory_capequity_252d_jerk_v064_signal,
    f27it_f27_investment_trajectory_capequity_504d_jerk_v065_signal,
    f27it_f27_investment_trajectory_capebitda_252d_jerk_v066_signal,
    f27it_f27_investment_trajectory_capebitda_504d_jerk_v067_signal,
    f27it_f27_investment_trajectory_capopinc_63d_jerk_v068_signal,
    f27it_f27_investment_trajectory_capopinc_252d_jerk_v069_signal,
    f27it_f27_investment_trajectory_capinvxprice_252d_jerk_v070_signal,
    f27it_f27_investment_trajectory_capinvxprice_504d_jerk_v071_signal,
    f27it_f27_investment_trajectory_capgrowxmom_21d_jerk_v072_signal,
    f27it_f27_investment_trajectory_capgrowxmom_63d_jerk_v073_signal,
    f27it_f27_investment_trajectory_capgrowxmom_252d_jerk_v074_signal,
    f27it_f27_investment_trajectory_capreviz_252d_jerk_v075_signal,
    f27it_f27_investment_trajectory_capreviz_504d_jerk_v076_signal,
    f27it_f27_investment_trajectory_capgrowabs_63d_jerk_v077_signal,
    f27it_f27_investment_trajectory_capgrowabs_252d_jerk_v078_signal,
    f27it_f27_investment_trajectory_capgrowabs_504d_jerk_v079_signal,
    f27it_f27_investment_trajectory_capgrowcv_252d_jerk_v080_signal,
    f27it_f27_investment_trajectory_capgrowcv_504d_jerk_v081_signal,
    f27it_f27_investment_trajectory_capfcf_252d_jerk_v082_signal,
    f27it_f27_investment_trajectory_capfcf_504d_jerk_v083_signal,
    f27it_f27_investment_trajectory_capnetinc_252d_jerk_v084_signal,
    f27it_f27_investment_trajectory_capnetinc_504d_jerk_v085_signal,
    f27it_f27_investment_trajectory_capgp_63d_jerk_v086_signal,
    f27it_f27_investment_trajectory_capgp_252d_jerk_v087_signal,
    f27it_f27_investment_trajectory_capgrowaccel_252d_jerk_v088_signal,
    f27it_f27_investment_trajectory_capgrowaccel_504d_jerk_v089_signal,
    f27it_f27_investment_trajectory_capgrowratio_63v252_jerk_v090_signal,
    f27it_f27_investment_trajectory_capgrowratio_21v63_jerk_v091_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_63d_jerk_v092_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_252d_jerk_v093_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_504d_jerk_v094_signal,
    f27it_f27_investment_trajectory_capxmcap_252d_jerk_v095_signal,
    f27it_f27_investment_trajectory_capxmcap_504d_jerk_v096_signal,
    f27it_f27_investment_trajectory_capgrowemashrt_21d_jerk_v097_signal,
    f27it_f27_investment_trajectory_capgrowemalong_252d_jerk_v098_signal,
    f27it_f27_investment_trajectory_capgrowskew_252d_jerk_v099_signal,
    f27it_f27_investment_trajectory_capgrowskew_504d_jerk_v100_signal,
    f27it_f27_investment_trajectory_capgrowkurt_252d_jerk_v101_signal,
    f27it_f27_investment_trajectory_capgrowkurt_504d_jerk_v102_signal,
    f27it_f27_investment_trajectory_capcomposite_252d_jerk_v103_signal,
    f27it_f27_investment_trajectory_capinvxrev_63d_jerk_v104_signal,
    f27it_f27_investment_trajectory_capinvxrev_252d_jerk_v105_signal,
    f27it_f27_investment_trajectory_capxrevassets_252d_jerk_v106_signal,
    f27it_f27_investment_trajectory_capxrevassets_504d_jerk_v107_signal,
    f27it_f27_investment_trajectory_capgrowxstd_21d_jerk_v108_signal,
    f27it_f27_investment_trajectory_capgrowxstd_252d_jerk_v109_signal,
    f27it_f27_investment_trajectory_capvsncfogrow_252d_jerk_v110_signal,
    f27it_f27_investment_trajectory_capvsncfogrow_504d_jerk_v111_signal,
    f27it_f27_investment_trajectory_capinvmom_252d_jerk_v112_signal,
    f27it_f27_investment_trajectory_capinvmom_504d_jerk_v113_signal,
    f27it_f27_investment_trajectory_capxrevcfo_252d_jerk_v114_signal,
    f27it_f27_investment_trajectory_capxrevcfo_504d_jerk_v115_signal,
    f27it_f27_investment_trajectory_capxassetseq_252d_jerk_v116_signal,
    f27it_f27_investment_trajectory_capxassetseq_504d_jerk_v117_signal,
    f27it_f27_investment_trajectory_capyoyraw_252d_jerk_v118_signal,
    f27it_f27_investment_trajectory_cap2yraw_504d_jerk_v119_signal,
    f27it_f27_investment_trajectory_cap1mraw_21d_jerk_v120_signal,
    f27it_f27_investment_trajectory_cap1qraw_63d_jerk_v121_signal,
    f27it_f27_investment_trajectory_capshare_252d_jerk_v122_signal,
    f27it_f27_investment_trajectory_capshare_504d_jerk_v123_signal,
    f27it_f27_investment_trajectory_capxcap_252d_jerk_v124_signal,
    f27it_f27_investment_trajectory_capxcap_504d_jerk_v125_signal,
    f27it_f27_investment_trajectory_capnet_63d_jerk_v126_signal,
    f27it_f27_investment_trajectory_capnet_252d_jerk_v127_signal,
    f27it_f27_investment_trajectory_capgrowinstability_252d_jerk_v128_signal,
    f27it_f27_investment_trajectory_capgrowinstability_504d_jerk_v129_signal,
    f27it_f27_investment_trajectory_capaccelcnt_252d_jerk_v130_signal,
    f27it_f27_investment_trajectory_capaccelcnt_504d_jerk_v131_signal,
    f27it_f27_investment_trajectory_capsignsum_252d_jerk_v132_signal,
    f27it_f27_investment_trajectory_capsignsum_504d_jerk_v133_signal,
    f27it_f27_investment_trajectory_caprevvsmean_252d_jerk_v134_signal,
    f27it_f27_investment_trajectory_caprevvsmean_504d_jerk_v135_signal,
    f27it_f27_investment_trajectory_capinvexp_252d_jerk_v136_signal,
    f27it_f27_investment_trajectory_capinvexp_504d_jerk_v137_signal,
    f27it_f27_investment_trajectory_capxretcum_252d_jerk_v138_signal,
    f27it_f27_investment_trajectory_capxretcum_504d_jerk_v139_signal,
    f27it_f27_investment_trajectory_capgrowxrev_252d_jerk_v140_signal,
    f27it_f27_investment_trajectory_capgrowxrev_504d_jerk_v141_signal,
    f27it_f27_investment_trajectory_capxopncfo_252d_jerk_v142_signal,
    f27it_f27_investment_trajectory_capxopncfo_504d_jerk_v143_signal,
    f27it_f27_investment_trajectory_capgrowarea_252d_jerk_v144_signal,
    f27it_f27_investment_trajectory_capgrowarea_504d_jerk_v145_signal,
    f27it_f27_investment_trajectory_capyoyraw_504d_jerk_v146_signal,
    f27it_f27_investment_trajectory_capassetsdiff_252d_jerk_v147_signal,
    f27it_f27_investment_trajectory_capassetsdiff_504d_jerk_v148_signal,
    f27it_f27_investment_trajectory_capncfodiff_63d_jerk_v149_signal,
    f27it_f27_investment_trajectory_capncfodiff_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_INVESTMENT_TRAJECTORY_REGISTRY_JERK = REGISTRY


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

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f27_investment_trajectory_3rd_derivatives_001_150_claude: {n_features} features pass")
