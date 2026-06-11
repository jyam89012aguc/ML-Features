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


# 252d EWM of margin × ev
def f43mt_f43_moat_trajectory_marginewmev_252d_base_v076_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = m.ewm(span=126, adjust=False).mean() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWM of roic × marketcap
def f43mt_f43_moat_trajectory_roicewmmc_252d_base_v077_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = r.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin durability range (max-min over 252d) × ev
def f43mt_f43_moat_trajectory_marginrange_252d_base_v078_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    rng = md.rolling(252, min_periods=63).std()
    result = rng * ev
    return result.replace([np.inf, -np.inf], np.nan)


# roic durability range × marketcap
def f43mt_f43_moat_trajectory_roicrange_252d_base_v079_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    rng = rd.rolling(252, min_periods=63).std()
    result = rng * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat × log marketcap
def f43mt_f43_moat_trajectory_marginxlogmc_252d_base_v080_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat × log ev
def f43mt_f43_moat_trajectory_roicxlogev_252d_base_v081_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_durability(r, 252) * np.log(ev.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharpe-like margin: mean / std × marketcap
def f43mt_f43_moat_trajectory_marginsharpe_252d_base_v082_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    me = _mean(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    result = (me / sd) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharpe-like roic × marketcap
def f43mt_f43_moat_trajectory_roicsharpe_504d_base_v083_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    me = _mean(r, 504)
    sd = _std(r, 504).replace(0, np.nan)
    result = (me / sd) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin trend slope (diff vs std) × ev
def f43mt_f43_moat_trajectory_margintrend_252d_base_v084_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    sd = _std(m, 252).replace(0, np.nan)
    trend = _diff(m, 252)
    result = (trend / sd) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin trend × marketcap
def f43mt_f43_moat_trajectory_margintrend_504d_base_v085_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    sd = _std(m, 504).replace(0, np.nan)
    trend = _diff(m, 504)
    result = (trend / sd) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic trend × ev
def f43mt_f43_moat_trajectory_roictrend_252d_base_v086_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sd = _std(r, 252).replace(0, np.nan)
    trend = _diff(r, 252)
    result = (trend / sd) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic trend × marketcap
def f43mt_f43_moat_trajectory_roictrend_504d_base_v087_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sd = _std(r, 504).replace(0, np.nan)
    trend = _diff(r, 504)
    result = (trend / sd) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin moat × marketcap rolling mean (durable + size)
def f43mt_f43_moat_trajectory_marginxmc_252d_base_v088_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# roic moat × marketcap rolling mean
def f43mt_f43_moat_trajectory_roicxmc_252d_base_v089_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * _mean(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin moat × ev rolling mean
def f43mt_f43_moat_trajectory_marginxevmean_252d_base_v090_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# roic moat × ev rolling mean
def f43mt_f43_moat_trajectory_roicxevmean_252d_base_v091_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * _mean(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin × evebitda inverted (cheap-margin moat)
def f43mt_f43_moat_trajectory_cheapmargin_252d_base_v092_signal(netinc, revenue, evebitda, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    inv = 1.0 / evebitda.replace(0, np.nan).abs()
    result = md * inv * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# roic × evebit inverted × marketcap
def f43mt_f43_moat_trajectory_cheaproic_252d_base_v093_signal(netinc, equity, debt, evebit, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    inv = 1.0 / evebit.replace(0, np.nan).abs()
    result = rd * inv * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat × pe inverted
def f43mt_f43_moat_trajectory_marginxinvpe_252d_base_v094_signal(netinc, revenue, pe, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    inv = 1.0 / pe.replace(0, np.nan).abs()
    result = md * inv * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat × pb inverted
def f43mt_f43_moat_trajectory_roicxinvpb_252d_base_v095_signal(netinc, equity, debt, pb, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    inv = 1.0 / pb.replace(0, np.nan).abs()
    result = rd * inv * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat × ps inverted
def f43mt_f43_moat_trajectory_marginxinvps_252d_base_v096_signal(netinc, revenue, ps, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    inv = 1.0 / ps.replace(0, np.nan).abs()
    result = md * inv * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating-margin sharpe × ev
def f43mt_f43_moat_trajectory_opmgsharpe_252d_base_v097_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    me = _mean(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    result = (me / sd) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda margin sharpe × marketcap
def f43mt_f43_moat_trajectory_ebmgsharpe_504d_base_v098_signal(ebitda, revenue, marketcap):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    me = _mean(m, 504)
    sd = _std(m, 504).replace(0, np.nan)
    result = (me / sd) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf margin sharpe × ev
def f43mt_f43_moat_trajectory_fcfmgsharpe_252d_base_v099_signal(fcf, revenue, ev):
    m = _f43_moat_margin_proxy(fcf, revenue)
    me = _mean(m, 252)
    sd = _std(m, 252).replace(0, np.nan)
    result = (me / sd) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# margin moat - roic moat (gap) × marketcap
def f43mt_f43_moat_trajectory_marginroicgap_252d_base_v100_signal(netinc, revenue, equity, debt, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = (_f43_moat_traj_durability(m, 252) - _f43_moat_traj_durability(r, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin moat 63 vs margin moat 252 gap × ev
def f43mt_f43_moat_trajectory_marginshortvslong_base_v101_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    short = _f43_moat_traj_durability(m, 63)
    long = _f43_moat_traj_durability(m, 252)
    result = (short - long) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# roic moat 63 vs roic moat 252 gap × marketcap
def f43mt_f43_moat_trajectory_roicshortvslong_base_v102_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    short = _f43_moat_traj_durability(r, 63)
    long = _f43_moat_traj_durability(r, 252)
    result = (short - long) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev stability × pe (composite valuation moat)
def f43mt_f43_moat_trajectory_evxpe_252d_base_v103_signal(ev, pe, marketcap):
    result = _f43_moat_traj_evstability(ev, 252) * _mean(pe, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap stability × pb
def f43mt_f43_moat_trajectory_mcxpb_252d_base_v104_signal(marketcap, pb):
    result = _f43_moat_traj_evstability(marketcap, 252) * _mean(pb, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap stability × ps
def f43mt_f43_moat_trajectory_mcxps_504d_base_v105_signal(marketcap, ps):
    result = _f43_moat_traj_evstability(marketcap, 504) * _mean(ps, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev stability × evebit
def f43mt_f43_moat_trajectory_evxevebit_252d_base_v106_signal(ev, evebit, marketcap):
    result = _f43_moat_traj_evstability(ev, 252) * _mean(evebit, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev stability × evebitda
def f43mt_f43_moat_trajectory_evxevebitda_252d_base_v107_signal(ev, evebitda, marketcap):
    result = _f43_moat_traj_evstability(ev, 252) * _mean(evebitda, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value durability × marketcap (institutional persistence)
def f43mt_f43_moat_trajectory_sf3adur_252d_base_v108_signal(sf3a_value, marketcap):
    result = _f43_moat_traj_durability(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value durability × marketcap
def f43mt_f43_moat_trajectory_sf3bdur_504d_base_v109_signal(sf3b_value, marketcap):
    result = _f43_moat_traj_durability(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a shares mean × margin moat
def f43mt_f43_moat_trajectory_sf3ashxmargin_252d_base_v110_signal(netinc, revenue, sf3a_shares):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(sf3a_shares, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b shares mean × roic moat
def f43mt_f43_moat_trajectory_sf3bshxroic_252d_base_v111_signal(netinc, equity, debt, sf3b_shares):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * _mean(sf3b_shares, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin × roic combined averaged 504d × ev
def f43mt_f43_moat_trajectory_avgmoat_504d_base_v112_signal(netinc, revenue, equity, debt, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    avg = (_mean(m, 504) + _mean(r, 504)) / 2.0
    result = avg * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin durability × marketcap
def f43mt_f43_moat_trajectory_opmgdur_252d_base_v113_signal(opinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = _f43_moat_traj_durability(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating margin sharpe × ev
def f43mt_f43_moat_trajectory_opmgsharpe_504d_base_v114_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    me = _mean(m, 504)
    sd = _std(m, 504).replace(0, np.nan)
    result = (me / sd) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda margin durability × ev
def f43mt_f43_moat_trajectory_ebmgdur_504d_base_v115_signal(ebitda, revenue, ev):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = _f43_moat_traj_durability(m, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf margin durability × marketcap
def f43mt_f43_moat_trajectory_fcfmgdur_504d_base_v116_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = _f43_moat_traj_durability(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo margin durability × marketcap
def f43mt_f43_moat_trajectory_ncfomgdur_252d_base_v117_signal(ncfo, revenue, marketcap):
    m = _f43_moat_margin_proxy(ncfo, revenue)
    result = _f43_moat_traj_durability(m, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo margin durability × ev
def f43mt_f43_moat_trajectory_ncfomgdur_504d_base_v118_signal(ncfo, revenue, ev):
    m = _f43_moat_margin_proxy(ncfo, revenue)
    result = _f43_moat_traj_durability(m, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic on assets durability × marketcap
def f43mt_f43_moat_trajectory_roaadur_252d_base_v119_signal(netinc, assets, marketcap):
    r = _f43_moat_margin_proxy(netinc, assets)
    result = _f43_moat_traj_durability(r, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d return on equity durability × ev
def f43mt_f43_moat_trajectory_roeadur_504d_base_v120_signal(netinc, equity, ev):
    r = _f43_moat_margin_proxy(netinc, equity)
    result = _f43_moat_traj_durability(r, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda margin EWM × marketcap
def f43mt_f43_moat_trajectory_ebmgewm_252d_base_v121_signal(ebitda, revenue, marketcap):
    m = _f43_moat_margin_proxy(ebitda, revenue)
    result = m.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d operating margin EWM × ev
def f43mt_f43_moat_trajectory_opmgewm_504d_base_v122_signal(opinc, revenue, ev):
    m = _f43_moat_margin_proxy(opinc, revenue)
    result = m.ewm(span=252, adjust=False).mean() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf margin EWM × marketcap
def f43mt_f43_moat_trajectory_fcfmgewm_504d_base_v123_signal(fcf, revenue, marketcap):
    m = _f43_moat_margin_proxy(fcf, revenue)
    result = m.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin × marketcap × ev sandwich
def f43mt_f43_moat_trajectory_sandwich_252d_base_v124_signal(netinc, revenue, marketcap, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * np.sqrt(marketcap.abs() * ev.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic × marketcap × ev sandwich
def f43mt_f43_moat_trajectory_roicsand_252d_base_v125_signal(netinc, equity, debt, marketcap, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * np.sqrt(marketcap.abs() * ev.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat / pe (cheap-durable composite)
def f43mt_f43_moat_trajectory_marginvpe_252d_base_v126_signal(netinc, revenue, pe, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md / pe.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat / pb
def f43mt_f43_moat_trajectory_roicvpb_252d_base_v127_signal(netinc, equity, debt, pb, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd / pb.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin moat / ps
def f43mt_f43_moat_trajectory_marginvps_504d_base_v128_signal(netinc, revenue, ps, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 504)
    result = md / ps.replace(0, np.nan).abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev stability × roic moat (stable enterprise + durable returns)
def f43mt_f43_moat_trajectory_evxroic_252d_base_v129_signal(netinc, equity, debt, ev, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = _f43_moat_traj_evstability(ev, 252) * rd * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap stability × margin moat
def f43mt_f43_moat_trajectory_mcstxmargin_252d_base_v130_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = _f43_moat_traj_evstability(marketcap, 252) * md * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap stability × roic moat
def f43mt_f43_moat_trajectory_mcstxroic_504d_base_v131_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 504)
    result = _f43_moat_traj_evstability(marketcap, 504) * rd * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat times marketcap log diff (size growth × moat)
def f43mt_f43_moat_trajectory_marginxmcdiff_252d_base_v132_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    diff = _diff(np.log(marketcap.replace(0, np.nan)), 252)
    result = md * diff * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat times ev log diff
def f43mt_f43_moat_trajectory_roicxevdiff_252d_base_v133_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    diff = _diff(np.log(ev.replace(0, np.nan)), 252)
    result = rd * diff * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin durability vs 504d margin durability × marketcap
def f43mt_f43_moat_trajectory_margindur_2v5_base_v134_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    a = _f43_moat_traj_durability(m, 252)
    b = _f43_moat_traj_durability(m, 504).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic durability vs 504d roic durability × marketcap
def f43mt_f43_moat_trajectory_roicdur_2v5_base_v135_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    a = _f43_moat_traj_durability(r, 252)
    b = _f43_moat_traj_durability(r, 504).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margin durability × ebitda × ev composite moat
def f43mt_f43_moat_trajectory_marxebxev_252d_base_v136_signal(netinc, revenue, ebitda, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(ebitda, 252) * ev / ev.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat × opinc × marketcap
def f43mt_f43_moat_trajectory_roicxopxmc_252d_base_v137_signal(netinc, equity, debt, opinc, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * _mean(opinc, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d margin persistence × marketcap
def f43mt_f43_moat_trajectory_marginpersist_504d_base_v138_signal(netinc, revenue, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    result = _f43_moat_traj_persistence(m, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic persistence × ev
def f43mt_f43_moat_trajectory_roicpersist_504d_base_v139_signal(netinc, equity, debt, ev):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    result = _f43_moat_traj_persistence(r, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin × volume of sf3a value (smart-money confirmed durability)
def f43mt_f43_moat_trajectory_marginxsf3av_252d_base_v140_signal(netinc, revenue, sf3a_value):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic × sf3b value durability
def f43mt_f43_moat_trajectory_roicxsf3bv_252d_base_v141_signal(netinc, equity, debt, sf3b_value):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * _mean(sf3b_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite moat: margin sharpe × roic sharpe × marketcap
def f43mt_f43_moat_trajectory_compositesharpe_252d_base_v142_signal(netinc, revenue, equity, debt, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sm = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    sr = _mean(r, 252) / _std(r, 252).replace(0, np.nan)
    result = sm * sr * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite moat sharpe × ev
def f43mt_f43_moat_trajectory_compositesharpe_504d_base_v143_signal(netinc, revenue, equity, debt, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    sm = _mean(m, 504) / _std(m, 504).replace(0, np.nan)
    sr = _mean(r, 504) / _std(r, 504).replace(0, np.nan)
    result = sm * sr * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin floor (rolling min × ev) - persistent worst margin
def f43mt_f43_moat_trajectory_marginfloor_252d_base_v144_signal(netinc, revenue, ev):
    m = _f43_moat_margin_proxy(netinc, revenue)
    floor = _mean(m, 252) - _std(m, 252)
    result = floor * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic floor × marketcap
def f43mt_f43_moat_trajectory_roicfloor_504d_base_v145_signal(netinc, equity, debt, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    floor = _mean(r, 504) - _std(r, 504)
    result = floor * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin moat × log sf3a value
def f43mt_f43_moat_trajectory_marginxlogsf3a_252d_base_v146_signal(netinc, revenue, sf3a_value):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * np.log(sf3a_value.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic moat × log sf3b value
def f43mt_f43_moat_trajectory_roicxlogsf3b_252d_base_v147_signal(netinc, equity, debt, sf3b_value):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 252)
    result = rd * np.log(sf3b_value.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin × ebitda × ev sandwich (full durable moat)
def f43mt_f43_moat_trajectory_fullmoat_252d_base_v148_signal(netinc, revenue, ebitda, ev, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    md = _f43_moat_traj_durability(m, 252)
    result = md * _mean(ebitda, 252) * ev / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic × pb × marketcap (cheap-durable book composite)
def f43mt_f43_moat_trajectory_roicxpb_504d_base_v149_signal(netinc, equity, debt, pb, marketcap):
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    rd = _f43_moat_traj_durability(r, 504)
    result = rd * _mean(pb, 504) * marketcap / marketcap.replace(0, np.nan) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite triple moat (margin × roic × ev stability) × marketcap
def f43mt_f43_moat_trajectory_triplemoat_504d_base_v150_signal(netinc, revenue, equity, debt, ev, marketcap):
    m = _f43_moat_margin_proxy(netinc, revenue)
    r = _f43_moat_roic_proxy(netinc, equity, debt)
    md = _f43_moat_traj_durability(m, 504)
    rd = _f43_moat_traj_durability(r, 504)
    es = _f43_moat_traj_evstability(ev, 504)
    result = md * rd * es * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43mt_f43_moat_trajectory_marginewmev_252d_base_v076_signal,
    f43mt_f43_moat_trajectory_roicewmmc_252d_base_v077_signal,
    f43mt_f43_moat_trajectory_marginrange_252d_base_v078_signal,
    f43mt_f43_moat_trajectory_roicrange_252d_base_v079_signal,
    f43mt_f43_moat_trajectory_marginxlogmc_252d_base_v080_signal,
    f43mt_f43_moat_trajectory_roicxlogev_252d_base_v081_signal,
    f43mt_f43_moat_trajectory_marginsharpe_252d_base_v082_signal,
    f43mt_f43_moat_trajectory_roicsharpe_504d_base_v083_signal,
    f43mt_f43_moat_trajectory_margintrend_252d_base_v084_signal,
    f43mt_f43_moat_trajectory_margintrend_504d_base_v085_signal,
    f43mt_f43_moat_trajectory_roictrend_252d_base_v086_signal,
    f43mt_f43_moat_trajectory_roictrend_504d_base_v087_signal,
    f43mt_f43_moat_trajectory_marginxmc_252d_base_v088_signal,
    f43mt_f43_moat_trajectory_roicxmc_252d_base_v089_signal,
    f43mt_f43_moat_trajectory_marginxevmean_252d_base_v090_signal,
    f43mt_f43_moat_trajectory_roicxevmean_252d_base_v091_signal,
    f43mt_f43_moat_trajectory_cheapmargin_252d_base_v092_signal,
    f43mt_f43_moat_trajectory_cheaproic_252d_base_v093_signal,
    f43mt_f43_moat_trajectory_marginxinvpe_252d_base_v094_signal,
    f43mt_f43_moat_trajectory_roicxinvpb_252d_base_v095_signal,
    f43mt_f43_moat_trajectory_marginxinvps_252d_base_v096_signal,
    f43mt_f43_moat_trajectory_opmgsharpe_252d_base_v097_signal,
    f43mt_f43_moat_trajectory_ebmgsharpe_504d_base_v098_signal,
    f43mt_f43_moat_trajectory_fcfmgsharpe_252d_base_v099_signal,
    f43mt_f43_moat_trajectory_marginroicgap_252d_base_v100_signal,
    f43mt_f43_moat_trajectory_marginshortvslong_base_v101_signal,
    f43mt_f43_moat_trajectory_roicshortvslong_base_v102_signal,
    f43mt_f43_moat_trajectory_evxpe_252d_base_v103_signal,
    f43mt_f43_moat_trajectory_mcxpb_252d_base_v104_signal,
    f43mt_f43_moat_trajectory_mcxps_504d_base_v105_signal,
    f43mt_f43_moat_trajectory_evxevebit_252d_base_v106_signal,
    f43mt_f43_moat_trajectory_evxevebitda_252d_base_v107_signal,
    f43mt_f43_moat_trajectory_sf3adur_252d_base_v108_signal,
    f43mt_f43_moat_trajectory_sf3bdur_504d_base_v109_signal,
    f43mt_f43_moat_trajectory_sf3ashxmargin_252d_base_v110_signal,
    f43mt_f43_moat_trajectory_sf3bshxroic_252d_base_v111_signal,
    f43mt_f43_moat_trajectory_avgmoat_504d_base_v112_signal,
    f43mt_f43_moat_trajectory_opmgdur_252d_base_v113_signal,
    f43mt_f43_moat_trajectory_opmgsharpe_504d_base_v114_signal,
    f43mt_f43_moat_trajectory_ebmgdur_504d_base_v115_signal,
    f43mt_f43_moat_trajectory_fcfmgdur_504d_base_v116_signal,
    f43mt_f43_moat_trajectory_ncfomgdur_252d_base_v117_signal,
    f43mt_f43_moat_trajectory_ncfomgdur_504d_base_v118_signal,
    f43mt_f43_moat_trajectory_roaadur_252d_base_v119_signal,
    f43mt_f43_moat_trajectory_roeadur_504d_base_v120_signal,
    f43mt_f43_moat_trajectory_ebmgewm_252d_base_v121_signal,
    f43mt_f43_moat_trajectory_opmgewm_504d_base_v122_signal,
    f43mt_f43_moat_trajectory_fcfmgewm_504d_base_v123_signal,
    f43mt_f43_moat_trajectory_sandwich_252d_base_v124_signal,
    f43mt_f43_moat_trajectory_roicsand_252d_base_v125_signal,
    f43mt_f43_moat_trajectory_marginvpe_252d_base_v126_signal,
    f43mt_f43_moat_trajectory_roicvpb_252d_base_v127_signal,
    f43mt_f43_moat_trajectory_marginvps_504d_base_v128_signal,
    f43mt_f43_moat_trajectory_evxroic_252d_base_v129_signal,
    f43mt_f43_moat_trajectory_mcstxmargin_252d_base_v130_signal,
    f43mt_f43_moat_trajectory_mcstxroic_504d_base_v131_signal,
    f43mt_f43_moat_trajectory_marginxmcdiff_252d_base_v132_signal,
    f43mt_f43_moat_trajectory_roicxevdiff_252d_base_v133_signal,
    f43mt_f43_moat_trajectory_margindur_2v5_base_v134_signal,
    f43mt_f43_moat_trajectory_roicdur_2v5_base_v135_signal,
    f43mt_f43_moat_trajectory_marxebxev_252d_base_v136_signal,
    f43mt_f43_moat_trajectory_roicxopxmc_252d_base_v137_signal,
    f43mt_f43_moat_trajectory_marginpersist_504d_base_v138_signal,
    f43mt_f43_moat_trajectory_roicpersist_504d_base_v139_signal,
    f43mt_f43_moat_trajectory_marginxsf3av_252d_base_v140_signal,
    f43mt_f43_moat_trajectory_roicxsf3bv_252d_base_v141_signal,
    f43mt_f43_moat_trajectory_compositesharpe_252d_base_v142_signal,
    f43mt_f43_moat_trajectory_compositesharpe_504d_base_v143_signal,
    f43mt_f43_moat_trajectory_marginfloor_252d_base_v144_signal,
    f43mt_f43_moat_trajectory_roicfloor_504d_base_v145_signal,
    f43mt_f43_moat_trajectory_marginxlogsf3a_252d_base_v146_signal,
    f43mt_f43_moat_trajectory_roicxlogsf3b_252d_base_v147_signal,
    f43mt_f43_moat_trajectory_fullmoat_252d_base_v148_signal,
    f43mt_f43_moat_trajectory_roicxpb_504d_base_v149_signal,
    f43mt_f43_moat_trajectory_triplemoat_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_MOAT_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f43_moat_trajectory_base_076_150_claude: {n_features} features pass")
