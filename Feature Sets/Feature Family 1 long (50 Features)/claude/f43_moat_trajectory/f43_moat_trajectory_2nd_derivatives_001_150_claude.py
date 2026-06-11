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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff(s, w):
    return s.diff(periods=w) / (s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


# ===== folder domain primitives =====
def _f43_moat_margin_proxy(netinc, revenue):
    return netinc / revenue.replace(0, np.nan).abs()


def _f43_moat_roic_proxy(netinc, equity, debt):
    cap = (equity.abs() + debt.abs()).replace(0, np.nan)
    return netinc / cap


def _f43_moat_traj_durability(metric, w):
    m = metric.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = metric.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def _f43_moat_traj_persistence(metric, w):
    base_ = metric.rolling(w, min_periods=max(1, w // 2)).mean()
    return base_ - metric.rolling(w * 2, min_periods=max(1, w)).mean()


def _f43_moat_traj_evstability(ev, w):
    m = ev.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ev.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


# 5d slope of 21d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_21d_slope_v001_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_21d_slope_v002_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 21) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_63d_slope_v003_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 63) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_63d_slope_v004_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_126d_slope_v005_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 126) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_126d_slope_v006_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 126) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_252d_slope_v007_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_252d_slope_v008_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_504d_slope_v009_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margin moat × marketcap
def f43mt_f43_moat_trajectory_marginmoat_504d_slope_v010_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d roic moat × ev
def f43mt_f43_moat_trajectory_roicmoat_21d_slope_v011_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 21) * ev
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d roic moat × ev
def f43mt_f43_moat_trajectory_roicmoat_63d_slope_v012_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 63) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d roic moat × ev
def f43mt_f43_moat_trajectory_roicmoat_252d_slope_v013_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic moat × ev
def f43mt_f43_moat_trajectory_roicmoat_252d_slope_v014_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d roic moat × ev
def f43mt_f43_moat_trajectory_roicmoat_504d_slope_v015_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 504) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marginpersist_63d_slope_v016_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_persistence(_f43_moat_margin_proxy(netinc, revenue), 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marginpersist_252d_slope_v017_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_persistence(_f43_moat_margin_proxy(netinc, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpersist_63d_slope_v018_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_persistence(_f43_moat_roic_proxy(netinc, equity, debt), 63) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpersist_252d_slope_v019_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_persistence(_f43_moat_roic_proxy(netinc, equity, debt), 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstable_21d_slope_v020_signal(ev, marketcap):
    base = _f43_moat_traj_evstability(ev, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstable_63d_slope_v021_signal(ev, marketcap):
    base = _f43_moat_traj_evstability(ev, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstable_252d_slope_v022_signal(ev, marketcap):
    base = _f43_moat_traj_evstability(ev, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstable_504d_slope_v023_signal(ev, marketcap):
    base = _f43_moat_traj_evstability(ev, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d operating margin moat × marketcap
def f43mt_f43_moat_trajectory_opmoat_63d_slope_v024_signal(opinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(opinc, revenue), 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d op margin moat × marketcap
def f43mt_f43_moat_trajectory_opmoat_252d_slope_v025_signal(opinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(opinc, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d op margin moat × marketcap
def f43mt_f43_moat_trajectory_opmoat_504d_slope_v026_signal(opinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(opinc, revenue), 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_63d_slope_v027_signal(ebitda, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ebitda, revenue), 63) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_252d_slope_v028_signal(ebitda, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ebitda, revenue), 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_504d_slope_v029_signal(ebitda, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ebitda, revenue), 504) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_63d_slope_v030_signal(fcf, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(fcf, revenue), 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_252d_slope_v031_signal(fcf, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(fcf, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_504d_slope_v032_signal(fcf, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(fcf, revenue), 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitst_21d_slope_v033_signal(evebit, marketcap):
    base = _f43_moat_traj_evstability(evebit, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitst_63d_slope_v034_signal(evebit, marketcap):
    base = _f43_moat_traj_evstability(evebit, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitst_252d_slope_v035_signal(evebit, marketcap):
    base = _f43_moat_traj_evstability(evebit, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdast_21d_slope_v036_signal(evebitda, marketcap):
    base = _f43_moat_traj_evstability(evebitda, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdast_252d_slope_v037_signal(evebitda, marketcap):
    base = _f43_moat_traj_evstability(evebitda, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdast_504d_slope_v038_signal(evebitda, marketcap):
    base = _f43_moat_traj_evstability(evebitda, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pe stability × marketcap
def f43mt_f43_moat_trajectory_pest_252d_slope_v039_signal(pe, marketcap):
    base = _f43_moat_traj_evstability(pe, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pe stability × marketcap
def f43mt_f43_moat_trajectory_pest_504d_slope_v040_signal(pe, marketcap):
    base = _f43_moat_traj_evstability(pe, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pb stability × marketcap
def f43mt_f43_moat_trajectory_pbst_252d_slope_v041_signal(pb, marketcap):
    base = _f43_moat_traj_evstability(pb, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pb stability × marketcap
def f43mt_f43_moat_trajectory_pbst_504d_slope_v042_signal(pb, marketcap):
    base = _f43_moat_traj_evstability(pb, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ps stability × marketcap
def f43mt_f43_moat_trajectory_psst_252d_slope_v043_signal(ps, marketcap):
    base = _f43_moat_traj_evstability(ps, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ps stability × marketcap
def f43mt_f43_moat_trajectory_psst_504d_slope_v044_signal(ps, marketcap):
    base = _f43_moat_traj_evstability(ps, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcst_21d_slope_v045_signal(marketcap):
    base = _f43_moat_traj_evstability(marketcap, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcst_63d_slope_v046_signal(marketcap):
    base = _f43_moat_traj_evstability(marketcap, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcst_252d_slope_v047_signal(marketcap):
    base = _f43_moat_traj_evstability(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcst_504d_slope_v048_signal(marketcap):
    base = _f43_moat_traj_evstability(marketcap, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sf3a shares stability × marketcap
def f43mt_f43_moat_trajectory_sf3ast_63d_slope_v049_signal(sf3a_shares, marketcap):
    base = _f43_moat_traj_evstability(sf3a_shares, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a value stability × marketcap
def f43mt_f43_moat_trajectory_sf3avst_252d_slope_v050_signal(sf3a_value, marketcap):
    base = _f43_moat_traj_evstability(sf3a_value, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3b shares stability × marketcap
def f43mt_f43_moat_trajectory_sf3bst_252d_slope_v051_signal(sf3b_shares, marketcap):
    base = _f43_moat_traj_evstability(sf3b_shares, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sf3b value stability × marketcap
def f43mt_f43_moat_trajectory_sf3bvst_504d_slope_v052_signal(sf3b_value, marketcap):
    base = _f43_moat_traj_evstability(sf3b_value, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d margin × ev
def f43mt_f43_moat_trajectory_marxev_63d_slope_v053_signal(netinc, revenue, ev):
    base = _mean(_f43_moat_margin_proxy(netinc, revenue), 63) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin × ev
def f43mt_f43_moat_trajectory_marxev_252d_slope_v054_signal(netinc, revenue, ev):
    base = _mean(_f43_moat_margin_proxy(netinc, revenue), 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d roic × ev
def f43mt_f43_moat_trajectory_roicxev_504d_slope_v055_signal(netinc, equity, debt, ev):
    base = _mean(_f43_moat_roic_proxy(netinc, equity, debt), 504) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d op margin × marketcap
def f43mt_f43_moat_trajectory_opxmc_252d_slope_v056_signal(opinc, revenue, marketcap):
    base = _mean(_f43_moat_margin_proxy(opinc, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda margin × ev
def f43mt_f43_moat_trajectory_ebxev_252d_slope_v057_signal(ebitda, revenue, ev):
    base = _mean(_f43_moat_margin_proxy(ebitda, revenue), 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fcf margin × ev
def f43mt_f43_moat_trajectory_fcfxev_504d_slope_v058_signal(fcf, revenue, ev):
    base = _mean(_f43_moat_margin_proxy(fcf, revenue), 504) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin moat × evebit
def f43mt_f43_moat_trajectory_marxevebit_252d_slope_v059_signal(netinc, revenue, evebit):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * evebit
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic moat × evebitda
def f43mt_f43_moat_trajectory_roicxevebitda_252d_slope_v060_signal(netinc, equity, debt, evebitda):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * evebitda
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap mean × roic
def f43mt_f43_moat_trajectory_mcxroic_63d_slope_v061_signal(netinc, equity, debt, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 63) * _mean(marketcap, 63)
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap mean × margin
def f43mt_f43_moat_trajectory_mcxmar_252d_slope_v062_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * _mean(marketcap, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ev mean × margin
def f43mt_f43_moat_trajectory_evxmar_252d_slope_v063_signal(netinc, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * _mean(ev, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a value mean × margin
def f43mt_f43_moat_trajectory_sf3axmar_252d_slope_v064_signal(netinc, revenue, sf3a_value):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * _mean(sf3a_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3b value mean × roic
def f43mt_f43_moat_trajectory_sf3bxroic_252d_slope_v065_signal(netinc, equity, debt, sf3b_value):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * _mean(sf3b_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d count of positive margins × marketcap
def f43mt_f43_moat_trajectory_marposc_252d_slope_v066_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (m).rolling(252, min_periods=63).mean() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d count of positive roic × marketcap
def f43mt_f43_moat_trajectory_roicposc_504d_slope_v067_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (r).rolling(504, min_periods=126).mean() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin EWM × ev
def f43mt_f43_moat_trajectory_marewm_252d_slope_v068_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = m.ewm(span=252, adjust=False).mean() * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margin EWM × marketcap
def f43mt_f43_moat_trajectory_marewm_504d_slope_v069_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = m.ewm(span=504, adjust=False).mean() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic EWM × ev
def f43mt_f43_moat_trajectory_roicewm_252d_slope_v070_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = r.ewm(span=252, adjust=False).mean() * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d roic EWM × marketcap
def f43mt_f43_moat_trajectory_roicewm_504d_slope_v071_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = r.ewm(span=504, adjust=False).mean() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin z × ev
def f43mt_f43_moat_trajectory_marz_252d_slope_v072_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = _z(m, 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margin z × marketcap
def f43mt_f43_moat_trajectory_marz_504d_slope_v073_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = _z(m, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic z × ev
def f43mt_f43_moat_trajectory_roicz_252d_slope_v074_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = _z(r, 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin sharpe × marketcap
def f43mt_f43_moat_trajectory_marsharpe_252d_slope_v075_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (_mean(m, 252) / _std(m, 252).replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d roic sharpe × marketcap
def f43mt_f43_moat_trajectory_roicsharpe_504d_slope_v076_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (_mean(r, 504) / _std(r, 504).replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d margin trend × ev
def f43mt_f43_moat_trajectory_martrend_252d_slope_v077_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (_diff(m, 252) / _std(m, 252).replace(0, np.nan)) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margin trend × marketcap
def f43mt_f43_moat_trajectory_martrend_504d_slope_v078_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (_diff(m, 504) / _std(m, 504).replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d roic trend × ev
def f43mt_f43_moat_trajectory_roictrend_252d_slope_v079_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (_diff(r, 252) / _std(r, 252).replace(0, np.nan)) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d roic trend × marketcap
def f43mt_f43_moat_trajectory_roictrend_504d_slope_v080_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (_diff(r, 504) / _std(r, 504).replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin moat × marketcap rolling mean
def f43mt_f43_moat_trajectory_marxmcmean_252d_slope_v081_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * _mean(marketcap, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic moat × marketcap rolling mean
def f43mt_f43_moat_trajectory_roicxmcmean_252d_slope_v082_signal(netinc, equity, debt, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * _mean(marketcap, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cheap-margin moat 252d
def f43mt_f43_moat_trajectory_cheapmar_252d_slope_v083_signal(netinc, revenue, evebitda, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * (1.0 / evebitda.replace(0, np.nan).abs()) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cheap-roic moat 252d
def f43mt_f43_moat_trajectory_cheaproic_252d_slope_v084_signal(netinc, equity, debt, evebit, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * (1.0 / evebit.replace(0, np.nan).abs()) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin / pe × marketcap
def f43mt_f43_moat_trajectory_marvpe_252d_slope_v085_signal(netinc, revenue, pe, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md / pe.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic / pb × marketcap
def f43mt_f43_moat_trajectory_roicvpb_252d_slope_v086_signal(netinc, equity, debt, pb, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd / pb.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin / ps × marketcap
def f43mt_f43_moat_trajectory_marvps_252d_slope_v087_signal(netinc, revenue, ps, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md / ps.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin sharpe 252d × ev
def f43mt_f43_moat_trajectory_opsharpe_252d_slope_v088_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    base = (_mean(m, 252) / _std(m, 252).replace(0, np.nan)) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ebitda sharpe 504d × marketcap
def f43mt_f43_moat_trajectory_ebsharpe_504d_slope_v089_signal(ebitda, revenue, marketcap):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    base = (_mean(m, 504) / _std(m, 504).replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fcf margin sharpe 252d × ev
def f43mt_f43_moat_trajectory_fcfsharpe_252d_slope_v090_signal(fcf, revenue, ev):
    m = _f43_moat_margin_proxy(fcf, revenue)
    base = (_mean(m, 252) / _std(m, 252).replace(0, np.nan)) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin-roic gap × marketcap
def f43mt_f43_moat_trajectory_margingap_252d_slope_v091_signal(netinc, revenue, equity, debt, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = (md - rd) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of margin short-vs-long × ev
def f43mt_f43_moat_trajectory_marshortlong_slope_v092_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (_f43_moat_traj_durability(m, 63) - _f43_moat_traj_durability(m, 252)) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of roic short-vs-long × marketcap
def f43mt_f43_moat_trajectory_roicshortlong_slope_v093_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (_f43_moat_traj_durability(r, 63) - _f43_moat_traj_durability(r, 252)) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev stab × pe × marketcap
def f43mt_f43_moat_trajectory_evxpe_252d_slope_v094_signal(ev, pe, marketcap):
    base = _f43_moat_traj_evstability(ev, 252) * _mean(pe, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mc stab × pb × marketcap
def f43mt_f43_moat_trajectory_mcxpb_252d_slope_v095_signal(marketcap, pb):
    base = _f43_moat_traj_evstability(marketcap, 252) * _mean(pb, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mc stab × ps × marketcap
def f43mt_f43_moat_trajectory_mcxps_504d_slope_v096_signal(marketcap, ps):
    base = _f43_moat_traj_evstability(marketcap, 504) * _mean(ps, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev stab × evebit × marketcap
def f43mt_f43_moat_trajectory_evxevebit_252d_slope_v097_signal(ev, evebit, marketcap):
    base = _f43_moat_traj_evstability(ev, 252) * _mean(evebit, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev stab × evebitda × marketcap
def f43mt_f43_moat_trajectory_evxevebitda_252d_slope_v098_signal(ev, evebitda, marketcap):
    base = _f43_moat_traj_evstability(ev, 252) * _mean(evebitda, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3a value durability × marketcap
def f43mt_f43_moat_trajectory_sf3adur_252d_slope_v099_signal(sf3a_value, marketcap):
    base = _f43_moat_traj_durability(sf3a_value, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of sf3b value durability × marketcap
def f43mt_f43_moat_trajectory_sf3bdur_504d_slope_v100_signal(sf3b_value, marketcap):
    base = _f43_moat_traj_durability(sf3b_value, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3a sh × margin moat
def f43mt_f43_moat_trajectory_sf3ashxmar_252d_slope_v101_signal(netinc, revenue, sf3a_shares):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252) * _mean(sf3a_shares, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3b sh × roic moat
def f43mt_f43_moat_trajectory_sf3bshxroic_252d_slope_v102_signal(netinc, equity, debt, sf3b_shares):
    base = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252) * _mean(sf3b_shares, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of avg moat 504d × ev
def f43mt_f43_moat_trajectory_avgmoat_504d_slope_v103_signal(netinc, revenue, equity, debt, ev):
    avg = (_mean(_f43_moat_margin_proxy(netinc, revenue), 504) + _mean(_f43_moat_roic_proxy(netinc, equity, debt), 504)) / 2.0
    base = avg * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of op margin durability × marketcap
def f43mt_f43_moat_trajectory_opdur_252d_slope_v104_signal(opinc, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(opinc, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of op margin sharpe 504d × ev
def f43mt_f43_moat_trajectory_opsharpe_504d_slope_v105_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    base = (_mean(m, 504) / _std(m, 504).replace(0, np.nan)) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ebitda margin durability × ev
def f43mt_f43_moat_trajectory_ebdur_504d_slope_v106_signal(ebitda, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ebitda, revenue), 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of fcf margin durability × marketcap
def f43mt_f43_moat_trajectory_fcfdur_504d_slope_v107_signal(fcf, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(fcf, revenue), 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncfo margin durability × marketcap
def f43mt_f43_moat_trajectory_ncfodur_252d_slope_v108_signal(ncfo, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ncfo, revenue), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ncfo margin durability × ev
def f43mt_f43_moat_trajectory_ncfodur_504d_slope_v109_signal(ncfo, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ncfo, revenue), 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ROA durability × marketcap
def f43mt_f43_moat_trajectory_roadur_252d_slope_v110_signal(netinc, assets, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, assets), 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ROE durability × ev
def f43mt_f43_moat_trajectory_roedur_504d_slope_v111_signal(netinc, equity, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, equity), 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ebitda margin EWM × marketcap
def f43mt_f43_moat_trajectory_ebewm_252d_slope_v112_signal(ebitda, revenue, marketcap):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    base = m.ewm(span=126, adjust=False).mean() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of op margin EWM × ev
def f43mt_f43_moat_trajectory_opewm_504d_slope_v113_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    base = m.ewm(span=252, adjust=False).mean() * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of fcf margin EWM × marketcap
def f43mt_f43_moat_trajectory_fcfewm_504d_slope_v114_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    base = m.ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin × sqrt(mc * ev) sandwich
def f43mt_f43_moat_trajectory_marsand_252d_slope_v115_signal(netinc, revenue, marketcap, ev):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * np.sqrt(marketcap.abs() * ev.abs())
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic × sqrt(mc * ev) sandwich
def f43mt_f43_moat_trajectory_roicsand_252d_slope_v116_signal(netinc, equity, debt, marketcap, ev):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * np.sqrt(marketcap.abs() * ev.abs())
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of margin / pe × marketcap (504d)
def f43mt_f43_moat_trajectory_marvpe_504d_slope_v117_signal(netinc, revenue, pe, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 504)
    base = md / pe.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of roic / pb × marketcap (504d)
def f43mt_f43_moat_trajectory_roicvpb_504d_slope_v118_signal(netinc, equity, debt, pb, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 504)
    base = rd / pb.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of margin / ps × marketcap (504d)
def f43mt_f43_moat_trajectory_marvps_504d_slope_v119_signal(netinc, revenue, ps, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 504)
    base = md / ps.replace(0, np.nan).abs() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev stab × roic × marketcap
def f43mt_f43_moat_trajectory_evxroic_252d_slope_v120_signal(netinc, equity, debt, ev, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = _f43_moat_traj_evstability(ev, 252) * rd * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mc stab × margin × marketcap
def f43mt_f43_moat_trajectory_mcstxmar_252d_slope_v121_signal(netinc, revenue, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = _f43_moat_traj_evstability(marketcap, 252) * md * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mc stab × roic × marketcap
def f43mt_f43_moat_trajectory_mcstxroic_504d_slope_v122_signal(netinc, equity, debt, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 504)
    base = _f43_moat_traj_evstability(marketcap, 504) * rd * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin × log(mc) diff
def f43mt_f43_moat_trajectory_marxmcdiff_252d_slope_v123_signal(netinc, revenue, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    diff = _diff(np.log(marketcap.replace(0, np.nan)), 252)
    base = md * diff * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic × log(ev) diff
def f43mt_f43_moat_trajectory_roicxevdiff_252d_slope_v124_signal(netinc, equity, debt, ev):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    diff = _diff(np.log(ev.replace(0, np.nan)), 252)
    base = rd * diff * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin durability ratio 252v504 × marketcap
def f43mt_f43_moat_trajectory_marratio_2v5_slope_v125_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    a = _f43_moat_traj_durability(m, 252)
    b = _f43_moat_traj_durability(m, 504).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic durability ratio 252v504 × marketcap
def f43mt_f43_moat_trajectory_roicratio_2v5_slope_v126_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    a = _f43_moat_traj_durability(r, 252)
    b = _f43_moat_traj_durability(r, 504).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin × ebitda × ev composite
def f43mt_f43_moat_trajectory_marxebxev_252d_slope_v127_signal(netinc, revenue, ebitda, ev):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * _mean(ebitda, 252) * ev / ev.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic × opinc × marketcap composite
def f43mt_f43_moat_trajectory_roicxopxmc_252d_slope_v128_signal(netinc, equity, debt, opinc, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * _mean(opinc, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marpers_504d_slope_v129_signal(netinc, revenue, marketcap):
    base = _f43_moat_traj_persistence(_f43_moat_margin_proxy(netinc, revenue), 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpers_504d_slope_v130_signal(netinc, equity, debt, ev):
    base = _f43_moat_traj_persistence(_f43_moat_roic_proxy(netinc, equity, debt), 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin × sf3a value × durability
def f43mt_f43_moat_trajectory_marxsf3av_252d_slope_v131_signal(netinc, revenue, sf3a_value):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * _mean(sf3a_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic × sf3b value × durability
def f43mt_f43_moat_trajectory_roicxsf3bv_252d_slope_v132_signal(netinc, equity, debt, sf3b_value):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * _mean(sf3b_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite sharpe 252d × marketcap
def f43mt_f43_moat_trajectory_compsharpe_252d_slope_v133_signal(netinc, revenue, equity, debt, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sm = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    sr = _mean(r, 252) / _std(r, 252).replace(0, np.nan)
    base = sm * sr * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of composite sharpe 504d × ev
def f43mt_f43_moat_trajectory_compsharpe_504d_slope_v134_signal(netinc, revenue, equity, debt, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sm = _mean(m, 504) / _std(m, 504).replace(0, np.nan)
    sr = _mean(r, 504) / _std(r, 504).replace(0, np.nan)
    base = sm * sr * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin floor 252d × ev
def f43mt_f43_moat_trajectory_marfloor_252d_slope_v135_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    base = (_mean(m, 252) - _std(m, 252)) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of roic floor 504d × marketcap
def f43mt_f43_moat_trajectory_roicfloor_504d_slope_v136_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    base = (_mean(r, 504) - _std(r, 504)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin × log sf3a value
def f43mt_f43_moat_trajectory_marxlogsf3a_252d_slope_v137_signal(netinc, revenue, sf3a_value):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * np.log(sf3a_value.replace(0, np.nan))
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic × log sf3b value
def f43mt_f43_moat_trajectory_roicxlogsf3b_252d_slope_v138_signal(netinc, equity, debt, sf3b_value):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * np.log(sf3b_value.replace(0, np.nan))
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of full moat composite 252d
def f43mt_f43_moat_trajectory_fullmoat_252d_slope_v139_signal(netinc, revenue, ebitda, ev, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * _mean(ebitda, 252) * ev / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of roic × pb × marketcap composite
def f43mt_f43_moat_trajectory_roicxpb_504d_slope_v140_signal(netinc, equity, debt, pb, marketcap):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 504)
    base = rd * _mean(pb, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of triple moat composite 504d × marketcap
def f43mt_f43_moat_trajectory_triplemoat_504d_slope_v141_signal(netinc, revenue, equity, debt, ev, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 504)
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 504)
    es = _f43_moat_traj_evstability(ev, 504)
    base = md * rd * es * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d marketcap stability × marketcap (intra-month moat shift)
def f43mt_f43_moat_trajectory_mcst_21d_slope_v142_signal(marketcap):
    base = _f43_moat_traj_evstability(marketcap, 21) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ev stability × marketcap
def f43mt_f43_moat_trajectory_evst_21d_slope_v143_signal(ev, marketcap):
    base = _f43_moat_traj_evstability(ev, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sf3a value durability × marketcap
def f43mt_f43_moat_trajectory_sf3aval_63d_slope_v144_signal(sf3a_value, marketcap):
    base = _f43_moat_traj_durability(sf3a_value, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sf3b value durability × marketcap
def f43mt_f43_moat_trajectory_sf3bval_63d_slope_v145_signal(sf3b_value, marketcap):
    base = _f43_moat_traj_durability(sf3b_value, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fcf margin × ev × marketcap composite
def f43mt_f43_moat_trajectory_fcfxevmc_252d_slope_v146_signal(fcf, revenue, ev, marketcap):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(fcf, revenue), 252)
    base = md * ev * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of margin moat × evebitda inverse × ev composite
def f43mt_f43_moat_trajectory_cheapmar_evcomp_slope_v147_signal(netinc, revenue, evebitda, ev):
    md = _f43_moat_traj_durability(_f43_moat_margin_proxy(netinc, revenue), 252)
    base = md * (1.0 / evebitda.replace(0, np.nan).abs()) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of roic moat × evebit inverse × ev composite
def f43mt_f43_moat_trajectory_cheaproic_evcomp_slope_v148_signal(netinc, equity, debt, evebit, ev):
    rd = _f43_moat_traj_durability(_f43_moat_roic_proxy(netinc, equity, debt), 252)
    base = rd * (1.0 / evebit.replace(0, np.nan).abs()) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of operating margin durability × ev (504d)
def f43mt_f43_moat_trajectory_opdur_504d_slope_v149_signal(opinc, revenue, ev):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(opinc, revenue), 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ebitda margin durability × marketcap (504d)
def f43mt_f43_moat_trajectory_ebdur_mc_504d_slope_v150_signal(ebitda, revenue, marketcap):
    base = _f43_moat_traj_durability(_f43_moat_margin_proxy(ebitda, revenue), 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43mt_f43_moat_trajectory_marginmoat_21d_slope_v001_signal,
    f43mt_f43_moat_trajectory_marginmoat_21d_slope_v002_signal,
    f43mt_f43_moat_trajectory_marginmoat_63d_slope_v003_signal,
    f43mt_f43_moat_trajectory_marginmoat_63d_slope_v004_signal,
    f43mt_f43_moat_trajectory_marginmoat_126d_slope_v005_signal,
    f43mt_f43_moat_trajectory_marginmoat_126d_slope_v006_signal,
    f43mt_f43_moat_trajectory_marginmoat_252d_slope_v007_signal,
    f43mt_f43_moat_trajectory_marginmoat_252d_slope_v008_signal,
    f43mt_f43_moat_trajectory_marginmoat_504d_slope_v009_signal,
    f43mt_f43_moat_trajectory_marginmoat_504d_slope_v010_signal,
    f43mt_f43_moat_trajectory_roicmoat_21d_slope_v011_signal,
    f43mt_f43_moat_trajectory_roicmoat_63d_slope_v012_signal,
    f43mt_f43_moat_trajectory_roicmoat_252d_slope_v013_signal,
    f43mt_f43_moat_trajectory_roicmoat_252d_slope_v014_signal,
    f43mt_f43_moat_trajectory_roicmoat_504d_slope_v015_signal,
    f43mt_f43_moat_trajectory_marginpersist_63d_slope_v016_signal,
    f43mt_f43_moat_trajectory_marginpersist_252d_slope_v017_signal,
    f43mt_f43_moat_trajectory_roicpersist_63d_slope_v018_signal,
    f43mt_f43_moat_trajectory_roicpersist_252d_slope_v019_signal,
    f43mt_f43_moat_trajectory_evstable_21d_slope_v020_signal,
    f43mt_f43_moat_trajectory_evstable_63d_slope_v021_signal,
    f43mt_f43_moat_trajectory_evstable_252d_slope_v022_signal,
    f43mt_f43_moat_trajectory_evstable_504d_slope_v023_signal,
    f43mt_f43_moat_trajectory_opmoat_63d_slope_v024_signal,
    f43mt_f43_moat_trajectory_opmoat_252d_slope_v025_signal,
    f43mt_f43_moat_trajectory_opmoat_504d_slope_v026_signal,
    f43mt_f43_moat_trajectory_ebmoat_63d_slope_v027_signal,
    f43mt_f43_moat_trajectory_ebmoat_252d_slope_v028_signal,
    f43mt_f43_moat_trajectory_ebmoat_504d_slope_v029_signal,
    f43mt_f43_moat_trajectory_fcfmoat_63d_slope_v030_signal,
    f43mt_f43_moat_trajectory_fcfmoat_252d_slope_v031_signal,
    f43mt_f43_moat_trajectory_fcfmoat_504d_slope_v032_signal,
    f43mt_f43_moat_trajectory_evebitst_21d_slope_v033_signal,
    f43mt_f43_moat_trajectory_evebitst_63d_slope_v034_signal,
    f43mt_f43_moat_trajectory_evebitst_252d_slope_v035_signal,
    f43mt_f43_moat_trajectory_evebitdast_21d_slope_v036_signal,
    f43mt_f43_moat_trajectory_evebitdast_252d_slope_v037_signal,
    f43mt_f43_moat_trajectory_evebitdast_504d_slope_v038_signal,
    f43mt_f43_moat_trajectory_pest_252d_slope_v039_signal,
    f43mt_f43_moat_trajectory_pest_504d_slope_v040_signal,
    f43mt_f43_moat_trajectory_pbst_252d_slope_v041_signal,
    f43mt_f43_moat_trajectory_pbst_504d_slope_v042_signal,
    f43mt_f43_moat_trajectory_psst_252d_slope_v043_signal,
    f43mt_f43_moat_trajectory_psst_504d_slope_v044_signal,
    f43mt_f43_moat_trajectory_mcst_21d_slope_v045_signal,
    f43mt_f43_moat_trajectory_mcst_63d_slope_v046_signal,
    f43mt_f43_moat_trajectory_mcst_252d_slope_v047_signal,
    f43mt_f43_moat_trajectory_mcst_504d_slope_v048_signal,
    f43mt_f43_moat_trajectory_sf3ast_63d_slope_v049_signal,
    f43mt_f43_moat_trajectory_sf3avst_252d_slope_v050_signal,
    f43mt_f43_moat_trajectory_sf3bst_252d_slope_v051_signal,
    f43mt_f43_moat_trajectory_sf3bvst_504d_slope_v052_signal,
    f43mt_f43_moat_trajectory_marxev_63d_slope_v053_signal,
    f43mt_f43_moat_trajectory_marxev_252d_slope_v054_signal,
    f43mt_f43_moat_trajectory_roicxev_504d_slope_v055_signal,
    f43mt_f43_moat_trajectory_opxmc_252d_slope_v056_signal,
    f43mt_f43_moat_trajectory_ebxev_252d_slope_v057_signal,
    f43mt_f43_moat_trajectory_fcfxev_504d_slope_v058_signal,
    f43mt_f43_moat_trajectory_marxevebit_252d_slope_v059_signal,
    f43mt_f43_moat_trajectory_roicxevebitda_252d_slope_v060_signal,
    f43mt_f43_moat_trajectory_mcxroic_63d_slope_v061_signal,
    f43mt_f43_moat_trajectory_mcxmar_252d_slope_v062_signal,
    f43mt_f43_moat_trajectory_evxmar_252d_slope_v063_signal,
    f43mt_f43_moat_trajectory_sf3axmar_252d_slope_v064_signal,
    f43mt_f43_moat_trajectory_sf3bxroic_252d_slope_v065_signal,
    f43mt_f43_moat_trajectory_marposc_252d_slope_v066_signal,
    f43mt_f43_moat_trajectory_roicposc_504d_slope_v067_signal,
    f43mt_f43_moat_trajectory_marewm_252d_slope_v068_signal,
    f43mt_f43_moat_trajectory_marewm_504d_slope_v069_signal,
    f43mt_f43_moat_trajectory_roicewm_252d_slope_v070_signal,
    f43mt_f43_moat_trajectory_roicewm_504d_slope_v071_signal,
    f43mt_f43_moat_trajectory_marz_252d_slope_v072_signal,
    f43mt_f43_moat_trajectory_marz_504d_slope_v073_signal,
    f43mt_f43_moat_trajectory_roicz_252d_slope_v074_signal,
    f43mt_f43_moat_trajectory_marsharpe_252d_slope_v075_signal,
    f43mt_f43_moat_trajectory_roicsharpe_504d_slope_v076_signal,
    f43mt_f43_moat_trajectory_martrend_252d_slope_v077_signal,
    f43mt_f43_moat_trajectory_martrend_504d_slope_v078_signal,
    f43mt_f43_moat_trajectory_roictrend_252d_slope_v079_signal,
    f43mt_f43_moat_trajectory_roictrend_504d_slope_v080_signal,
    f43mt_f43_moat_trajectory_marxmcmean_252d_slope_v081_signal,
    f43mt_f43_moat_trajectory_roicxmcmean_252d_slope_v082_signal,
    f43mt_f43_moat_trajectory_cheapmar_252d_slope_v083_signal,
    f43mt_f43_moat_trajectory_cheaproic_252d_slope_v084_signal,
    f43mt_f43_moat_trajectory_marvpe_252d_slope_v085_signal,
    f43mt_f43_moat_trajectory_roicvpb_252d_slope_v086_signal,
    f43mt_f43_moat_trajectory_marvps_252d_slope_v087_signal,
    f43mt_f43_moat_trajectory_opsharpe_252d_slope_v088_signal,
    f43mt_f43_moat_trajectory_ebsharpe_504d_slope_v089_signal,
    f43mt_f43_moat_trajectory_fcfsharpe_252d_slope_v090_signal,
    f43mt_f43_moat_trajectory_margingap_252d_slope_v091_signal,
    f43mt_f43_moat_trajectory_marshortlong_slope_v092_signal,
    f43mt_f43_moat_trajectory_roicshortlong_slope_v093_signal,
    f43mt_f43_moat_trajectory_evxpe_252d_slope_v094_signal,
    f43mt_f43_moat_trajectory_mcxpb_252d_slope_v095_signal,
    f43mt_f43_moat_trajectory_mcxps_504d_slope_v096_signal,
    f43mt_f43_moat_trajectory_evxevebit_252d_slope_v097_signal,
    f43mt_f43_moat_trajectory_evxevebitda_252d_slope_v098_signal,
    f43mt_f43_moat_trajectory_sf3adur_252d_slope_v099_signal,
    f43mt_f43_moat_trajectory_sf3bdur_504d_slope_v100_signal,
    f43mt_f43_moat_trajectory_sf3ashxmar_252d_slope_v101_signal,
    f43mt_f43_moat_trajectory_sf3bshxroic_252d_slope_v102_signal,
    f43mt_f43_moat_trajectory_avgmoat_504d_slope_v103_signal,
    f43mt_f43_moat_trajectory_opdur_252d_slope_v104_signal,
    f43mt_f43_moat_trajectory_opsharpe_504d_slope_v105_signal,
    f43mt_f43_moat_trajectory_ebdur_504d_slope_v106_signal,
    f43mt_f43_moat_trajectory_fcfdur_504d_slope_v107_signal,
    f43mt_f43_moat_trajectory_ncfodur_252d_slope_v108_signal,
    f43mt_f43_moat_trajectory_ncfodur_504d_slope_v109_signal,
    f43mt_f43_moat_trajectory_roadur_252d_slope_v110_signal,
    f43mt_f43_moat_trajectory_roedur_504d_slope_v111_signal,
    f43mt_f43_moat_trajectory_ebewm_252d_slope_v112_signal,
    f43mt_f43_moat_trajectory_opewm_504d_slope_v113_signal,
    f43mt_f43_moat_trajectory_fcfewm_504d_slope_v114_signal,
    f43mt_f43_moat_trajectory_marsand_252d_slope_v115_signal,
    f43mt_f43_moat_trajectory_roicsand_252d_slope_v116_signal,
    f43mt_f43_moat_trajectory_marvpe_504d_slope_v117_signal,
    f43mt_f43_moat_trajectory_roicvpb_504d_slope_v118_signal,
    f43mt_f43_moat_trajectory_marvps_504d_slope_v119_signal,
    f43mt_f43_moat_trajectory_evxroic_252d_slope_v120_signal,
    f43mt_f43_moat_trajectory_mcstxmar_252d_slope_v121_signal,
    f43mt_f43_moat_trajectory_mcstxroic_504d_slope_v122_signal,
    f43mt_f43_moat_trajectory_marxmcdiff_252d_slope_v123_signal,
    f43mt_f43_moat_trajectory_roicxevdiff_252d_slope_v124_signal,
    f43mt_f43_moat_trajectory_marratio_2v5_slope_v125_signal,
    f43mt_f43_moat_trajectory_roicratio_2v5_slope_v126_signal,
    f43mt_f43_moat_trajectory_marxebxev_252d_slope_v127_signal,
    f43mt_f43_moat_trajectory_roicxopxmc_252d_slope_v128_signal,
    f43mt_f43_moat_trajectory_marpers_504d_slope_v129_signal,
    f43mt_f43_moat_trajectory_roicpers_504d_slope_v130_signal,
    f43mt_f43_moat_trajectory_marxsf3av_252d_slope_v131_signal,
    f43mt_f43_moat_trajectory_roicxsf3bv_252d_slope_v132_signal,
    f43mt_f43_moat_trajectory_compsharpe_252d_slope_v133_signal,
    f43mt_f43_moat_trajectory_compsharpe_504d_slope_v134_signal,
    f43mt_f43_moat_trajectory_marfloor_252d_slope_v135_signal,
    f43mt_f43_moat_trajectory_roicfloor_504d_slope_v136_signal,
    f43mt_f43_moat_trajectory_marxlogsf3a_252d_slope_v137_signal,
    f43mt_f43_moat_trajectory_roicxlogsf3b_252d_slope_v138_signal,
    f43mt_f43_moat_trajectory_fullmoat_252d_slope_v139_signal,
    f43mt_f43_moat_trajectory_roicxpb_504d_slope_v140_signal,
    f43mt_f43_moat_trajectory_triplemoat_504d_slope_v141_signal,
    f43mt_f43_moat_trajectory_mcst_21d_slope_v142_signal,
    f43mt_f43_moat_trajectory_evst_21d_slope_v143_signal,
    f43mt_f43_moat_trajectory_sf3aval_63d_slope_v144_signal,
    f43mt_f43_moat_trajectory_sf3bval_63d_slope_v145_signal,
    f43mt_f43_moat_trajectory_fcfxevmc_252d_slope_v146_signal,
    f43mt_f43_moat_trajectory_cheapmar_evcomp_slope_v147_signal,
    f43mt_f43_moat_trajectory_cheaproic_evcomp_slope_v148_signal,
    f43mt_f43_moat_trajectory_opdur_504d_slope_v149_signal,
    f43mt_f43_moat_trajectory_ebdur_mc_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_MOAT_TRAJECTORY_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")
    sf3a_shares = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="sf3a_shares")
    sf3a_value = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0005, 0.012, n))), name="sf3a_value")
    sf3b_shares = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.006, n))), name="sf3b_shares")
    sf3b_value = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0004, 0.013, n))), name="sf3b_value")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "revenue": revenue,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "equity": equity,
        "debt": debt, "assets": assets, "ebitda": ebitda, "opinc": opinc,
        "sharesbas": sharesbas, "ev": ev, "evebit": evebit, "evebitda": evebitda,
        "pe": pe, "pb": pb, "ps": ps,
        "sf3a_shares": sf3a_shares, "sf3a_value": sf3a_value,
        "sf3b_shares": sf3b_shares, "sf3b_value": sf3b_value,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f43_moat_margin_proxy", "_f43_moat_roic_proxy",
                         "_f43_moat_traj_durability", "_f43_moat_traj_persistence",
                         "_f43_moat_traj_evstability")
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
    print(f"OK f43_moat_trajectory_2nd_derivatives_001_150_claude: {n_features} features pass")
