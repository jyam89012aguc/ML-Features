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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _f10_netinc_revenue_gap(netinc, revenue, w):
    gap = netinc - revenue * 0.1
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f10_chargeoff_proxy(netinc, revenue, w):
    dispersion = (netinc / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).std()
    return dispersion


def _f10_provision_signature(netinc, w):
    diff = netinc.diff()
    return diff.rolling(w, min_periods=max(1, w // 2)).std()


def f10nco_f10_net_charge_off_proxy_coproxyrank_63d_base_v076_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    rnk = co.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyrank_126d_base_v077_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    rnk = co.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyrank_252d_base_v078_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    rnk = co.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_63d_base_v079_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    rnk = ps.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_126d_base_v080_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126)
    rnk = ps.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_252d_base_v081_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    rnk = ps.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_21d_base_v082_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21)
    result = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_63d_base_v083_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    result = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_252d_base_v084_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    result = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_21d_base_v085_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = co * ps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_63d_base_v086_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = co * ps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_126d_base_v087_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = co * ps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_252d_base_v088_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = co * ps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_21d_base_v089_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = g * co * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_63d_base_v090_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = g * co * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_126d_base_v091_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = g * co * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_252d_base_v092_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = g * co * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_21v63_base_v093_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 21)
    b = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_21v63_base_v094_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 21)
    b = _f10_provision_signature(netinc, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_63v252_base_v095_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 63)
    b = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_63v252_base_v096_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 63)
    b = _f10_provision_signature(netinc, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_126v504_base_v097_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 126)
    b = _f10_chargeoff_proxy(netinc, revenue, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_126v504_base_v098_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 126)
    b = _f10_provision_signature(netinc, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_42v189_base_v099_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 42)
    b = _f10_chargeoff_proxy(netinc, revenue, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_42v189_base_v100_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 42)
    b = _f10_provision_signature(netinc, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_63d_base_v101_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    rng = g.rolling(63, min_periods=max(1, 63//2)).max() - g.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_126d_base_v102_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    rng = g.rolling(126, min_periods=max(1, 126//2)).max() - g.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_252d_base_v103_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    rng = g.rolling(252, min_periods=max(1, 252//2)).max() - g.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_21d_base_v104_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = _std(co, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_63d_base_v105_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = _std(co, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_126d_base_v106_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = _std(co, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_252d_base_v107_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = _std(co, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_21d_base_v108_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = _std(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_63d_base_v109_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = _std(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_126d_base_v110_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = _std(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_252d_base_v111_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = _std(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_21d_base_v112_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    rg = revenue.pct_change(periods=21)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_63d_base_v113_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    rg = revenue.pct_change(periods=63)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_126d_base_v114_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    rg = revenue.pct_change(periods=126)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_252d_base_v115_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    rg = revenue.pct_change(periods=252)
    result = g * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_21d_base_v116_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    rg = revenue.pct_change(periods=21)
    result = co * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_63d_base_v117_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    rg = revenue.pct_change(periods=63)
    result = co * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_126d_base_v118_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    rg = revenue.pct_change(periods=126)
    result = co * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_252d_base_v119_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    rg = revenue.pct_change(periods=252)
    result = co * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_21d_base_v120_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    rg = revenue.pct_change(periods=21)
    result = ps * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_63d_base_v121_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    rg = revenue.pct_change(periods=63)
    result = ps * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_126d_base_v122_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    rg = revenue.pct_change(periods=126)
    result = ps * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_252d_base_v123_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    rg = revenue.pct_change(periods=252)
    result = ps * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_21d_base_v124_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_42d_base_v125_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 42) / _mean(revenue.abs(), 42).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 42)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_63d_base_v126_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_126d_base_v127_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_189d_base_v128_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 189) / _mean(revenue.abs(), 189).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 189)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_252d_base_v129_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    result = g * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_21d_base_v130_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    pv = _std(closeadj.pct_change(), 21)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_42d_base_v131_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 42)
    pv = _std(closeadj.pct_change(), 42)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_63d_base_v132_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    pv = _std(closeadj.pct_change(), 63)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_126d_base_v133_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    pv = _std(closeadj.pct_change(), 126)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_189d_base_v134_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 189)
    pv = _std(closeadj.pct_change(), 189)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_252d_base_v135_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    pv = _std(closeadj.pct_change(), 252)
    result = co * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_21d_base_v136_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_42d_base_v137_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 42)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_63d_base_v138_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_126d_base_v139_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_189d_base_v140_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 189) / _mean(netinc.abs(), 189).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 189)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_252d_base_v141_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    result = ps * pv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_21d_base_v142_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = co.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_42d_base_v143_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 42)
    result = co.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_63d_base_v144_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = co.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_126d_base_v145_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = co.rolling(126, min_periods=max(1, 126//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_189d_base_v146_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 189)
    result = co.rolling(189, min_periods=max(1, 189//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_252d_base_v147_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = co.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_21d_base_v148_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = ps.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_42d_base_v149_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    result = ps.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_63d_base_v150_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = ps.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10nco_f10_net_charge_off_proxy_coproxyrank_63d_base_v076_signal,
    f10nco_f10_net_charge_off_proxy_coproxyrank_126d_base_v077_signal,
    f10nco_f10_net_charge_off_proxy_coproxyrank_252d_base_v078_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_63d_base_v079_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_126d_base_v080_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_252d_base_v081_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_21d_base_v082_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_63d_base_v083_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_252d_base_v084_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_21d_base_v085_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_63d_base_v086_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_126d_base_v087_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_252d_base_v088_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_21d_base_v089_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_63d_base_v090_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_126d_base_v091_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_252d_base_v092_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_21v63_base_v093_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_21v63_base_v094_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_63v252_base_v095_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_63v252_base_v096_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_126v504_base_v097_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_126v504_base_v098_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_42v189_base_v099_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_42v189_base_v100_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_63d_base_v101_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_126d_base_v102_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_252d_base_v103_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_21d_base_v104_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_63d_base_v105_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_126d_base_v106_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_252d_base_v107_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_21d_base_v108_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_63d_base_v109_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_126d_base_v110_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_252d_base_v111_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_21d_base_v112_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_63d_base_v113_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_126d_base_v114_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_252d_base_v115_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_21d_base_v116_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_63d_base_v117_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_126d_base_v118_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_252d_base_v119_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_21d_base_v120_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_63d_base_v121_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_126d_base_v122_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_252d_base_v123_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_21d_base_v124_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_42d_base_v125_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_63d_base_v126_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_126d_base_v127_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_189d_base_v128_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_252d_base_v129_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_21d_base_v130_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_42d_base_v131_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_63d_base_v132_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_126d_base_v133_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_189d_base_v134_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_252d_base_v135_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_21d_base_v136_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_42d_base_v137_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_63d_base_v138_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_126d_base_v139_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_189d_base_v140_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_252d_base_v141_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_21d_base_v142_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_42d_base_v143_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_63d_base_v144_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_126d_base_v145_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_189d_base_v146_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_252d_base_v147_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_21d_base_v148_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_42d_base_v149_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_63d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_NET_CHARGE_OFF_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f10_netinc_revenue_gap', '_f10_chargeoff_proxy', '_f10_provision_signature')
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
    print(f"OK f10_net_charge_off_proxy_base_076_150_claude: {n_features} features pass")
