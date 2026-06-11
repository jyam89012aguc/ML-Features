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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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


# 21d margin moat durability scaled by marketcap
def f43mt_f43_moat_trajectory_marginmoat_21d_base_v001_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin moat durability scaled by marketcap
def f43mt_f43_moat_trajectory_marginmoat_63d_base_v002_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d margin moat durability scaled by marketcap
def f43mt_f43_moat_trajectory_marginmoat_126d_base_v003_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat durability scaled by marketcap
def f43mt_f43_moat_trajectory_marginmoat_252d_base_v004_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin moat durability scaled by marketcap
def f43mt_f43_moat_trajectory_marginmoat_504d_base_v005_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roic moat durability scaled by ev
def f43mt_f43_moat_trajectory_roicmoat_21d_base_v006_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic moat durability scaled by ev
def f43mt_f43_moat_trajectory_roicmoat_63d_base_v007_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat durability scaled by ev
def f43mt_f43_moat_trajectory_roicmoat_252d_base_v008_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic moat durability scaled by ev
def f43mt_f43_moat_trajectory_roicmoat_504d_base_v009_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marginpersist_63d_base_v010_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_persistence(m, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marginpersist_252d_base_v011_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_persistence(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpersist_63d_base_v012_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_persistence(r, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpersist_252d_base_v013_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_persistence(r, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstability_21d_base_v014_signal(ev, marketcap):
    result = _f43_moat_traj_evstability(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstability_63d_base_v015_signal(ev, marketcap):
    result = _f43_moat_traj_evstability(ev, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstability_252d_base_v016_signal(ev, marketcap):
    result = _f43_moat_traj_evstability(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev stability × marketcap
def f43mt_f43_moat_trajectory_evstability_504d_base_v017_signal(ev, marketcap):
    result = _f43_moat_traj_evstability(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross margin proxy × marketcap (opinc/revenue)
def f43mt_f43_moat_trajectory_opmoat_63d_base_v018_signal(opinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = _f43_moat_traj_durability(m, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin moat × marketcap
def f43mt_f43_moat_trajectory_opmoat_252d_base_v019_signal(opinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating margin moat × marketcap
def f43mt_f43_moat_trajectory_opmoat_504d_base_v020_signal(opinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = _f43_moat_traj_durability(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_63d_base_v021_signal(ebitda, revenue, ev):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = _f43_moat_traj_durability(m, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_252d_base_v022_signal(ebitda, revenue, ev):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = _f43_moat_traj_durability(m, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda margin moat × ev
def f43mt_f43_moat_trajectory_ebmoat_504d_base_v023_signal(ebitda, revenue, ev):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = _f43_moat_traj_durability(m, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_63d_base_v024_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = _f43_moat_traj_durability(m, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_252d_base_v025_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = _f43_moat_traj_durability(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf margin moat × marketcap
def f43mt_f43_moat_trajectory_fcfmoat_504d_base_v026_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = _f43_moat_traj_durability(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitstable_21d_base_v027_signal(evebit, marketcap):
    result = _f43_moat_traj_evstability(evebit, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitstable_63d_base_v028_signal(evebit, marketcap):
    result = _f43_moat_traj_evstability(evebit, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit stability × marketcap
def f43mt_f43_moat_trajectory_evebitstable_252d_base_v029_signal(evebit, marketcap):
    result = _f43_moat_traj_evstability(evebit, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdastable_21d_base_v030_signal(evebitda, marketcap):
    result = _f43_moat_traj_evstability(evebitda, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdastable_252d_base_v031_signal(evebitda, marketcap):
    result = _f43_moat_traj_evstability(evebitda, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebitda stability × marketcap
def f43mt_f43_moat_trajectory_evebitdastable_504d_base_v032_signal(evebitda, marketcap):
    result = _f43_moat_traj_evstability(evebitda, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe stability × marketcap
def f43mt_f43_moat_trajectory_pestable_252d_base_v033_signal(pe, marketcap):
    result = _f43_moat_traj_evstability(pe, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pe stability × marketcap
def f43mt_f43_moat_trajectory_pestable_504d_base_v034_signal(pe, marketcap):
    result = _f43_moat_traj_evstability(pe, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pb stability × marketcap
def f43mt_f43_moat_trajectory_pbstable_252d_base_v035_signal(pb, marketcap):
    result = _f43_moat_traj_evstability(pb, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pb stability × marketcap
def f43mt_f43_moat_trajectory_pbstable_504d_base_v036_signal(pb, marketcap):
    result = _f43_moat_traj_evstability(pb, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ps stability × marketcap
def f43mt_f43_moat_trajectory_psstable_252d_base_v037_signal(ps, marketcap):
    result = _f43_moat_traj_evstability(ps, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ps stability × marketcap
def f43mt_f43_moat_trajectory_psstable_504d_base_v038_signal(ps, marketcap):
    result = _f43_moat_traj_evstability(ps, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcstable_21d_base_v039_signal(marketcap):
    result = _f43_moat_traj_evstability(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcstable_63d_base_v040_signal(marketcap):
    result = _f43_moat_traj_evstability(marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcstable_252d_base_v041_signal(marketcap):
    result = _f43_moat_traj_evstability(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap stability × marketcap
def f43mt_f43_moat_trajectory_mcstable_504d_base_v042_signal(marketcap):
    result = _f43_moat_traj_evstability(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sf3a institutional shares stability × marketcap
def f43mt_f43_moat_trajectory_sf3astable_63d_base_v043_signal(sf3a_shares, marketcap):
    result = _f43_moat_traj_evstability(sf3a_shares, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value stability × marketcap
def f43mt_f43_moat_trajectory_sf3avalstable_252d_base_v044_signal(sf3a_value, marketcap):
    result = _f43_moat_traj_evstability(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b shares stability × marketcap
def f43mt_f43_moat_trajectory_sf3bstable_252d_base_v045_signal(sf3b_shares, marketcap):
    result = _f43_moat_traj_evstability(sf3b_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value stability × marketcap
def f43mt_f43_moat_trajectory_sf3bvalstable_504d_base_v046_signal(sf3b_value, marketcap):
    result = _f43_moat_traj_evstability(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin × ev (durable margin × valuation footprint)
def f43mt_f43_moat_trajectory_marginxev_63d_base_v047_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _mean(m, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin × ev
def f43mt_f43_moat_trajectory_marginxev_252d_base_v048_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _mean(m, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic × ev
def f43mt_f43_moat_trajectory_roicxev_504d_base_v049_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _mean(r, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin × marketcap
def f43mt_f43_moat_trajectory_opxmc_252d_base_v050_signal(opinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = _mean(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin × ev
def f43mt_f43_moat_trajectory_ebmgxev_252d_base_v051_signal(ebitda, revenue, ev):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = _mean(m, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf margin × ev
def f43mt_f43_moat_trajectory_fcfxev_504d_base_v052_signal(fcf, revenue, ev):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = _mean(m, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# margin durability × evebit (cheap durable margin)
def f43mt_f43_moat_trajectory_marginxevebit_252d_base_v053_signal(netinc, revenue, evebit):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * evebit
    return result.replace([np.inf, -np.inf], np.nan)


# roic durability × evebitda
def f43mt_f43_moat_trajectory_roicxevebitda_252d_base_v054_signal(netinc, equity, debt, evebitda):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 252) * evebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap moving avg × roic durability
def f43mt_f43_moat_trajectory_mcxroic_63d_base_v055_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 63) * _mean(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap mean × margin moat
def f43mt_f43_moat_trajectory_mcxmargin_252d_base_v056_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * _mean(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev mean × margin moat (durable margin enterprise weighted)
def f43mt_f43_moat_trajectory_evxmargin_252d_base_v057_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * _mean(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value mean × margin moat
def f43mt_f43_moat_trajectory_sf3axmargin_252d_base_v058_signal(netinc, revenue, sf3a_value):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b value mean × roic moat
def f43mt_f43_moat_trajectory_sf3bxroic_252d_base_v059_signal(netinc, equity, debt, sf3b_value):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 252) * _mean(sf3b_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of months with positive margin × marketcap
def f43mt_f43_moat_trajectory_marginposcount_252d_base_v060_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = (m).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of months with positive roic × marketcap
def f43mt_f43_moat_trajectory_roicposcount_504d_base_v061_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = (r).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin EWM trend × ev
def f43mt_f43_moat_trajectory_marginema_252d_base_v062_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = m.ewm(span=252, adjust=False).mean() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin EWM × marketcap
def f43mt_f43_moat_trajectory_marginema_504d_base_v063_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = m.ewm(span=504, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic EWM × ev
def f43mt_f43_moat_trajectory_roicema_252d_base_v064_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = r.ewm(span=252, adjust=False).mean() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic EWM × marketcap
def f43mt_f43_moat_trajectory_roicema_504d_base_v065_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = r.ewm(span=504, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin z-score across 252d × ev
def f43mt_f43_moat_trajectory_marginz_252d_base_v066_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _z(m, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# margin z-score across 504d × marketcap
def f43mt_f43_moat_trajectory_marginz_504d_base_v067_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _z(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# roic z-score across 252d × ev
def f43mt_f43_moat_trajectory_roicz_252d_base_v068_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _z(r, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of margin moat to ev moat
def f43mt_f43_moat_trajectory_marginvev_252d_base_v069_signal(netinc, revenue, ev, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    a = _f43_moat_traj_durability(m, 252)
    b = _f43_moat_traj_evstability(ev, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of roic moat to marketcap stability
def f43mt_f43_moat_trajectory_roicvmc_252d_base_v070_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    a = _f43_moat_traj_durability(r, 252)
    b = _f43_moat_traj_evstability(marketcap, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin × roic combined moat × marketcap
def f43mt_f43_moat_trajectory_combinedmoat_252d_base_v071_signal(netinc, revenue, equity, debt, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(m, 252) * _f43_moat_traj_durability(r, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin × roic combined moat 504d × ev
def f43mt_f43_moat_trajectory_combinedmoat_504d_base_v072_signal(netinc, revenue, equity, debt, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(m, 504) * _f43_moat_traj_durability(r, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat × pb (durability × book value valuation)
def f43mt_f43_moat_trajectory_marginxpb_252d_base_v073_signal(netinc, revenue, pb):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * pb
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat × ps
def f43mt_f43_moat_trajectory_roicxps_252d_base_v074_signal(netinc, equity, debt, ps):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 252) * ps
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev moat × pe (composite cheap-durable)
def f43mt_f43_moat_trajectory_evxpe_252d_base_v075_signal(ev, pe, marketcap):
    result = _f43_moat_traj_evstability(ev, 252) * pe * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43mt_f43_moat_trajectory_marginmoat_21d_base_v001_signal,
    f43mt_f43_moat_trajectory_marginmoat_63d_base_v002_signal,
    f43mt_f43_moat_trajectory_marginmoat_126d_base_v003_signal,
    f43mt_f43_moat_trajectory_marginmoat_252d_base_v004_signal,
    f43mt_f43_moat_trajectory_marginmoat_504d_base_v005_signal,
    f43mt_f43_moat_trajectory_roicmoat_21d_base_v006_signal,
    f43mt_f43_moat_trajectory_roicmoat_63d_base_v007_signal,
    f43mt_f43_moat_trajectory_roicmoat_252d_base_v008_signal,
    f43mt_f43_moat_trajectory_roicmoat_504d_base_v009_signal,
    f43mt_f43_moat_trajectory_marginpersist_63d_base_v010_signal,
    f43mt_f43_moat_trajectory_marginpersist_252d_base_v011_signal,
    f43mt_f43_moat_trajectory_roicpersist_63d_base_v012_signal,
    f43mt_f43_moat_trajectory_roicpersist_252d_base_v013_signal,
    f43mt_f43_moat_trajectory_evstability_21d_base_v014_signal,
    f43mt_f43_moat_trajectory_evstability_63d_base_v015_signal,
    f43mt_f43_moat_trajectory_evstability_252d_base_v016_signal,
    f43mt_f43_moat_trajectory_evstability_504d_base_v017_signal,
    f43mt_f43_moat_trajectory_opmoat_63d_base_v018_signal,
    f43mt_f43_moat_trajectory_opmoat_252d_base_v019_signal,
    f43mt_f43_moat_trajectory_opmoat_504d_base_v020_signal,
    f43mt_f43_moat_trajectory_ebmoat_63d_base_v021_signal,
    f43mt_f43_moat_trajectory_ebmoat_252d_base_v022_signal,
    f43mt_f43_moat_trajectory_ebmoat_504d_base_v023_signal,
    f43mt_f43_moat_trajectory_fcfmoat_63d_base_v024_signal,
    f43mt_f43_moat_trajectory_fcfmoat_252d_base_v025_signal,
    f43mt_f43_moat_trajectory_fcfmoat_504d_base_v026_signal,
    f43mt_f43_moat_trajectory_evebitstable_21d_base_v027_signal,
    f43mt_f43_moat_trajectory_evebitstable_63d_base_v028_signal,
    f43mt_f43_moat_trajectory_evebitstable_252d_base_v029_signal,
    f43mt_f43_moat_trajectory_evebitdastable_21d_base_v030_signal,
    f43mt_f43_moat_trajectory_evebitdastable_252d_base_v031_signal,
    f43mt_f43_moat_trajectory_evebitdastable_504d_base_v032_signal,
    f43mt_f43_moat_trajectory_pestable_252d_base_v033_signal,
    f43mt_f43_moat_trajectory_pestable_504d_base_v034_signal,
    f43mt_f43_moat_trajectory_pbstable_252d_base_v035_signal,
    f43mt_f43_moat_trajectory_pbstable_504d_base_v036_signal,
    f43mt_f43_moat_trajectory_psstable_252d_base_v037_signal,
    f43mt_f43_moat_trajectory_psstable_504d_base_v038_signal,
    f43mt_f43_moat_trajectory_mcstable_21d_base_v039_signal,
    f43mt_f43_moat_trajectory_mcstable_63d_base_v040_signal,
    f43mt_f43_moat_trajectory_mcstable_252d_base_v041_signal,
    f43mt_f43_moat_trajectory_mcstable_504d_base_v042_signal,
    f43mt_f43_moat_trajectory_sf3astable_63d_base_v043_signal,
    f43mt_f43_moat_trajectory_sf3avalstable_252d_base_v044_signal,
    f43mt_f43_moat_trajectory_sf3bstable_252d_base_v045_signal,
    f43mt_f43_moat_trajectory_sf3bvalstable_504d_base_v046_signal,
    f43mt_f43_moat_trajectory_marginxev_63d_base_v047_signal,
    f43mt_f43_moat_trajectory_marginxev_252d_base_v048_signal,
    f43mt_f43_moat_trajectory_roicxev_504d_base_v049_signal,
    f43mt_f43_moat_trajectory_opxmc_252d_base_v050_signal,
    f43mt_f43_moat_trajectory_ebmgxev_252d_base_v051_signal,
    f43mt_f43_moat_trajectory_fcfxev_504d_base_v052_signal,
    f43mt_f43_moat_trajectory_marginxevebit_252d_base_v053_signal,
    f43mt_f43_moat_trajectory_roicxevebitda_252d_base_v054_signal,
    f43mt_f43_moat_trajectory_mcxroic_63d_base_v055_signal,
    f43mt_f43_moat_trajectory_mcxmargin_252d_base_v056_signal,
    f43mt_f43_moat_trajectory_evxmargin_252d_base_v057_signal,
    f43mt_f43_moat_trajectory_sf3axmargin_252d_base_v058_signal,
    f43mt_f43_moat_trajectory_sf3bxroic_252d_base_v059_signal,
    f43mt_f43_moat_trajectory_marginposcount_252d_base_v060_signal,
    f43mt_f43_moat_trajectory_roicposcount_504d_base_v061_signal,
    f43mt_f43_moat_trajectory_marginema_252d_base_v062_signal,
    f43mt_f43_moat_trajectory_marginema_504d_base_v063_signal,
    f43mt_f43_moat_trajectory_roicema_252d_base_v064_signal,
    f43mt_f43_moat_trajectory_roicema_504d_base_v065_signal,
    f43mt_f43_moat_trajectory_marginz_252d_base_v066_signal,
    f43mt_f43_moat_trajectory_marginz_504d_base_v067_signal,
    f43mt_f43_moat_trajectory_roicz_252d_base_v068_signal,
    f43mt_f43_moat_trajectory_marginvev_252d_base_v069_signal,
    f43mt_f43_moat_trajectory_roicvmc_252d_base_v070_signal,
    f43mt_f43_moat_trajectory_combinedmoat_252d_base_v071_signal,
    f43mt_f43_moat_trajectory_combinedmoat_504d_base_v072_signal,
    f43mt_f43_moat_trajectory_marginxpb_252d_base_v073_signal,
    f43mt_f43_moat_trajectory_roicxps_252d_base_v074_signal,
    f43mt_f43_moat_trajectory_evxpe_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_MOAT_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f43_moat_trajectory_base_001_075_claude: {n_features} features pass")
