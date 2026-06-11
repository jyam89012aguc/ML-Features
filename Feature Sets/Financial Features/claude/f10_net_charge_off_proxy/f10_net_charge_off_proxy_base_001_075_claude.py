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


def f10nco_f10_net_charge_off_proxy_nirevgap_5d_base_v001_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 5)
    result = base / _mean(revenue.abs(), 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_10d_base_v002_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 10)
    result = base / _mean(revenue.abs(), 10).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_21d_base_v003_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 21)
    result = base / _mean(revenue.abs(), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_42d_base_v004_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 42)
    result = base / _mean(revenue.abs(), 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_63d_base_v005_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 63)
    result = base / _mean(revenue.abs(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_126d_base_v006_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 126)
    result = base / _mean(revenue.abs(), 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_189d_base_v007_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 189)
    result = base / _mean(revenue.abs(), 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_252d_base_v008_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 252)
    result = base / _mean(revenue.abs(), 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_378d_base_v009_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 378)
    result = base / _mean(revenue.abs(), 378).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_504d_base_v010_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 504)
    result = base / _mean(revenue.abs(), 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_5d_base_v011_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_10d_base_v012_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_21d_base_v013_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_42d_base_v014_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_63d_base_v015_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_126d_base_v016_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_189d_base_v017_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_252d_base_v018_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_378d_base_v019_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_504d_base_v020_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_5d_base_v021_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 5)
    result = base / _mean(netinc.abs(), 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_10d_base_v022_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 10)
    result = base / _mean(netinc.abs(), 10).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_21d_base_v023_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 21)
    result = base / _mean(netinc.abs(), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_42d_base_v024_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 42)
    result = base / _mean(netinc.abs(), 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_63d_base_v025_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 63)
    result = base / _mean(netinc.abs(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_126d_base_v026_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 126)
    result = base / _mean(netinc.abs(), 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_189d_base_v027_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 189)
    result = base / _mean(netinc.abs(), 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_252d_base_v028_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 252)
    result = base / _mean(netinc.abs(), 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_378d_base_v029_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 378)
    result = base / _mean(netinc.abs(), 378).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_504d_base_v030_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 504)
    result = base / _mean(netinc.abs(), 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_21d_base_v031_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    result = _z(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_63d_base_v032_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_126d_base_v033_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_252d_base_v034_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_21d_base_v035_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = _z(co, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_63d_base_v036_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = _z(co, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_126d_base_v037_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = _z(co, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_252d_base_v038_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = _z(co, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_21d_base_v039_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21)
    result = _z(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_63d_base_v040_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    result = _z(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_126d_base_v041_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126)
    result = _z(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_252d_base_v042_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    result = _z(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_10d_base_v043_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 10) / _mean(revenue.abs(), 10).replace(0, np.nan)
    result = _ema(g, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_21d_base_v044_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_63d_base_v045_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    result = _ema(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_126d_base_v046_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    result = _ema(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_252d_base_v047_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    result = _ema(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_10d_base_v048_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 10)
    result = _ema(co, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_21d_base_v049_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = _ema(co, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_63d_base_v050_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = _ema(co, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_126d_base_v051_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = _ema(co, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_252d_base_v052_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = _ema(co, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_10d_base_v053_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 10) / _mean(netinc.abs(), 10).replace(0, np.nan)
    result = _ema(ps, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_21d_base_v054_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = _ema(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_63d_base_v055_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = _ema(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_126d_base_v056_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = _ema(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_252d_base_v057_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = _ema(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_5d_base_v058_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 5)
    result = g.diff(periods=5) / _mean(revenue.abs(), 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_21d_base_v059_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21)
    result = g.diff(periods=21) / _mean(revenue.abs(), 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_63d_base_v060_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63)
    result = g.diff(periods=63) / _mean(revenue.abs(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_126d_base_v061_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126)
    result = g.diff(periods=126) / _mean(revenue.abs(), 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_252d_base_v062_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252)
    result = g.diff(periods=252) / _mean(revenue.abs(), 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_5d_base_v063_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 5)
    result = co.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_21d_base_v064_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    result = co.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_63d_base_v065_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    result = co.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_126d_base_v066_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    result = co.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_252d_base_v067_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    result = co.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_5d_base_v068_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 5) / _mean(netinc.abs(), 5).replace(0, np.nan)
    result = ps.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_21d_base_v069_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    result = ps.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_63d_base_v070_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    result = ps.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_126d_base_v071_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    result = ps.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_252d_base_v072_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = ps.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_63d_base_v073_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63)
    rnk = g.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_126d_base_v074_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126)
    rnk = g.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_252d_base_v075_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252)
    rnk = g.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10nco_f10_net_charge_off_proxy_nirevgap_5d_base_v001_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_10d_base_v002_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_21d_base_v003_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_42d_base_v004_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_63d_base_v005_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_126d_base_v006_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_189d_base_v007_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_252d_base_v008_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_378d_base_v009_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_504d_base_v010_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_5d_base_v011_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_10d_base_v012_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_21d_base_v013_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_42d_base_v014_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_63d_base_v015_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_126d_base_v016_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_189d_base_v017_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_252d_base_v018_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_378d_base_v019_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_504d_base_v020_signal,
    f10nco_f10_net_charge_off_proxy_provsig_5d_base_v021_signal,
    f10nco_f10_net_charge_off_proxy_provsig_10d_base_v022_signal,
    f10nco_f10_net_charge_off_proxy_provsig_21d_base_v023_signal,
    f10nco_f10_net_charge_off_proxy_provsig_42d_base_v024_signal,
    f10nco_f10_net_charge_off_proxy_provsig_63d_base_v025_signal,
    f10nco_f10_net_charge_off_proxy_provsig_126d_base_v026_signal,
    f10nco_f10_net_charge_off_proxy_provsig_189d_base_v027_signal,
    f10nco_f10_net_charge_off_proxy_provsig_252d_base_v028_signal,
    f10nco_f10_net_charge_off_proxy_provsig_378d_base_v029_signal,
    f10nco_f10_net_charge_off_proxy_provsig_504d_base_v030_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_21d_base_v031_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_63d_base_v032_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_126d_base_v033_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_252d_base_v034_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_21d_base_v035_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_63d_base_v036_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_126d_base_v037_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_252d_base_v038_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_21d_base_v039_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_63d_base_v040_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_126d_base_v041_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_252d_base_v042_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_10d_base_v043_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_21d_base_v044_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_63d_base_v045_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_126d_base_v046_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_252d_base_v047_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_10d_base_v048_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_21d_base_v049_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_63d_base_v050_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_126d_base_v051_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_252d_base_v052_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_10d_base_v053_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_21d_base_v054_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_63d_base_v055_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_126d_base_v056_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_252d_base_v057_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_5d_base_v058_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_21d_base_v059_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_63d_base_v060_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_126d_base_v061_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_252d_base_v062_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_5d_base_v063_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_21d_base_v064_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_63d_base_v065_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_126d_base_v066_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_252d_base_v067_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_5d_base_v068_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_21d_base_v069_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_63d_base_v070_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_126d_base_v071_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_252d_base_v072_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_63d_base_v073_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_126d_base_v074_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_252d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_NET_CHARGE_OFF_PROXY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f10_net_charge_off_proxy_base_001_075_claude: {n_features} features pass")
