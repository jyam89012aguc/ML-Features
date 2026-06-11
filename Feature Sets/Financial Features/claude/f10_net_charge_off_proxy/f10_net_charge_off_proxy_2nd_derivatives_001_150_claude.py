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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f10_netinc_revenue_gap(netinc, revenue, w):
    gap = netinc - revenue * 0.1
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f10_chargeoff_proxy(netinc, revenue, w):
    dispersion = (netinc / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).std()
    return dispersion


def _f10_provision_signature(netinc, w):
    diff = netinc.diff()
    return diff.rolling(w, min_periods=max(1, w // 2)).std()


def f10nco_f10_net_charge_off_proxy_nirevgap_5d_slope_v001_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 5)
    base_series = base / _mean(revenue.abs(), 5).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_10d_slope_v002_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 10)
    base_series = base / _mean(revenue.abs(), 10).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_21d_slope_v003_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 21)
    base_series = base / _mean(revenue.abs(), 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_42d_slope_v004_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 42)
    base_series = base / _mean(revenue.abs(), 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_63d_slope_v005_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 63)
    base_series = base / _mean(revenue.abs(), 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_126d_slope_v006_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 126)
    base_series = base / _mean(revenue.abs(), 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_189d_slope_v007_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 189)
    base_series = base / _mean(revenue.abs(), 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_252d_slope_v008_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 252)
    base_series = base / _mean(revenue.abs(), 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_378d_slope_v009_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 378)
    base_series = base / _mean(revenue.abs(), 378).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgap_504d_slope_v010_signal(netinc, revenue, closeadj):
    base = _f10_netinc_revenue_gap(netinc, revenue, 504)
    base_series = base / _mean(revenue.abs(), 504).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_5d_slope_v011_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 5)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_10d_slope_v012_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 10)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_21d_slope_v013_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_42d_slope_v014_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 42)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_63d_slope_v015_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_126d_slope_v016_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_189d_slope_v017_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 189)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_252d_slope_v018_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_378d_slope_v019_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 378)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxy_504d_slope_v020_signal(netinc, revenue, closeadj):
    base = _f10_chargeoff_proxy(netinc, revenue, 504)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_5d_slope_v021_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 5)
    base_series = base / _mean(netinc.abs(), 5).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_10d_slope_v022_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 10)
    base_series = base / _mean(netinc.abs(), 10).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_21d_slope_v023_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 21)
    base_series = base / _mean(netinc.abs(), 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_42d_slope_v024_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 42)
    base_series = base / _mean(netinc.abs(), 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_63d_slope_v025_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 63)
    base_series = base / _mean(netinc.abs(), 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_126d_slope_v026_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 126)
    base_series = base / _mean(netinc.abs(), 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_189d_slope_v027_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 189)
    base_series = base / _mean(netinc.abs(), 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_252d_slope_v028_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 252)
    base_series = base / _mean(netinc.abs(), 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_378d_slope_v029_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 378)
    base_series = base / _mean(netinc.abs(), 378).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsig_504d_slope_v030_signal(netinc, closeadj):
    base = _f10_provision_signature(netinc, 504)
    base_series = base / _mean(netinc.abs(), 504).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_21d_slope_v031_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    base_series = _z(g, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_63d_slope_v032_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    base_series = _z(g, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_126d_slope_v033_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    base_series = _z(g, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapz_252d_slope_v034_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    base_series = _z(g, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_21d_slope_v035_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = _z(co, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_63d_slope_v036_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = _z(co, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_126d_slope_v037_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = _z(co, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyz_252d_slope_v038_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = _z(co, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_21d_slope_v039_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21)
    base_series = _z(ps, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_63d_slope_v040_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    base_series = _z(ps, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_126d_slope_v041_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126)
    base_series = _z(ps, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigz_252d_slope_v042_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    base_series = _z(ps, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_10d_slope_v043_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 10) / _mean(revenue.abs(), 10).replace(0, np.nan)
    base_series = _ema(g, 10) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_21d_slope_v044_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    base_series = _ema(g, 21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_63d_slope_v045_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    base_series = _ema(g, 63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_126d_slope_v046_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    base_series = _ema(g, 126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapema_252d_slope_v047_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    base_series = _ema(g, 252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_10d_slope_v048_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 10)
    base_series = _ema(co, 10) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_21d_slope_v049_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = _ema(co, 21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_63d_slope_v050_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = _ema(co, 63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_126d_slope_v051_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = _ema(co, 126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyema_252d_slope_v052_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = _ema(co, 252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_10d_slope_v053_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 10) / _mean(netinc.abs(), 10).replace(0, np.nan)
    base_series = _ema(ps, 10) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_21d_slope_v054_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = _ema(ps, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_63d_slope_v055_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = _ema(ps, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_126d_slope_v056_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = _ema(ps, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigema_252d_slope_v057_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = _ema(ps, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_5d_slope_v058_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 5)
    base_series = g.diff(periods=5) / _mean(revenue.abs(), 5).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_21d_slope_v059_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21)
    base_series = g.diff(periods=21) / _mean(revenue.abs(), 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_63d_slope_v060_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63)
    base_series = g.diff(periods=63) / _mean(revenue.abs(), 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_126d_slope_v061_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126)
    base_series = g.diff(periods=126) / _mean(revenue.abs(), 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgapchg_252d_slope_v062_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252)
    base_series = g.diff(periods=252) / _mean(revenue.abs(), 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_5d_slope_v063_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 5)
    base_series = co.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_21d_slope_v064_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = co.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_63d_slope_v065_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = co.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_126d_slope_v066_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = co.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxychg_252d_slope_v067_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = co.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_5d_slope_v068_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 5) / _mean(netinc.abs(), 5).replace(0, np.nan)
    base_series = ps.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_21d_slope_v069_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = ps.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_63d_slope_v070_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = ps.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_126d_slope_v071_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = ps.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigchg_252d_slope_v072_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = ps.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_63d_slope_v073_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63)
    rnk = g.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_126d_slope_v074_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126)
    rnk = g.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprank_252d_slope_v075_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252)
    rnk = g.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyrank_63d_slope_v076_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    rnk = co.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyrank_126d_slope_v077_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    rnk = co.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyrank_252d_slope_v078_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    rnk = co.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_63d_slope_v079_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    rnk = ps.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_126d_slope_v080_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126)
    rnk = ps.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigrank_252d_slope_v081_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    rnk = ps.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_21d_slope_v082_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21)
    base_series = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_63d_slope_v083_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63)
    base_series = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsiglog_252d_slope_v084_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252)
    base_series = np.log(ps.replace(0, np.nan).abs()) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_21d_slope_v085_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = co * ps * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_63d_slope_v086_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = co * ps * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_126d_slope_v087_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = co * ps * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprov_252d_slope_v088_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = co * ps * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_21d_slope_v089_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = g * co * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_63d_slope_v090_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = g * co * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_126d_slope_v091_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = g * co * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxco_252d_slope_v092_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = g * co * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_21v63_slope_v093_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 21)
    b = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_21v63_slope_v094_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 21)
    b = _f10_provision_signature(netinc, 63)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_63v252_slope_v095_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 63)
    b = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_63v252_slope_v096_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 63)
    b = _f10_provision_signature(netinc, 252)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_126v504_slope_v097_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 126)
    b = _f10_chargeoff_proxy(netinc, revenue, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_126v504_slope_v098_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 126)
    b = _f10_provision_signature(netinc, 504)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyratio_42v189_slope_v099_signal(netinc, revenue, closeadj):
    a = _f10_chargeoff_proxy(netinc, revenue, 42)
    b = _f10_chargeoff_proxy(netinc, revenue, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigratio_42v189_slope_v100_signal(netinc, closeadj):
    a = _f10_provision_signature(netinc, 42)
    b = _f10_provision_signature(netinc, 189)
    base_series = (a / b.replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_63d_slope_v101_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    rng = g.rolling(63, min_periods=max(1, 63//2)).max() - g.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_126d_slope_v102_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    rng = g.rolling(126, min_periods=max(1, 126//2)).max() - g.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_nirevgaprange_252d_slope_v103_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    rng = g.rolling(252, min_periods=max(1, 252//2)).max() - g.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_21d_slope_v104_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = _std(co, 21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_63d_slope_v105_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = _std(co, 63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_126d_slope_v106_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = _std(co, 126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxystd_252d_slope_v107_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = _std(co, 252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_21d_slope_v108_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = _std(ps, 21) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_63d_slope_v109_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = _std(ps, 63) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_126d_slope_v110_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    base_series = _std(ps, 126) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigstd_252d_slope_v111_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    base_series = _std(ps, 252) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_21d_slope_v112_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    rg = revenue.pct_change(periods=21)
    base_series = g * rg * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_63d_slope_v113_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    rg = revenue.pct_change(periods=63)
    base_series = g * rg * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_126d_slope_v114_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    rg = revenue.pct_change(periods=126)
    base_series = g * rg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxrevgrowth_252d_slope_v115_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    rg = revenue.pct_change(periods=252)
    base_series = g * rg * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_21d_slope_v116_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    rg = revenue.pct_change(periods=21)
    base_series = co * rg * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_63d_slope_v117_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    rg = revenue.pct_change(periods=63)
    base_series = co * rg * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_126d_slope_v118_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    rg = revenue.pct_change(periods=126)
    base_series = co * rg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxrev_252d_slope_v119_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    rg = revenue.pct_change(periods=252)
    base_series = co * rg * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_21d_slope_v120_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    rg = revenue.pct_change(periods=21)
    base_series = ps * rg * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_63d_slope_v121_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    rg = revenue.pct_change(periods=63)
    base_series = ps * rg * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_126d_slope_v122_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    rg = revenue.pct_change(periods=126)
    base_series = ps * rg * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxrev_252d_slope_v123_signal(netinc, revenue, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    rg = revenue.pct_change(periods=252)
    base_series = ps * rg * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_21d_slope_v124_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 21) / _mean(revenue.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_42d_slope_v125_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 42) / _mean(revenue.abs(), 42).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 42)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_63d_slope_v126_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 63) / _mean(revenue.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_126d_slope_v127_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 126) / _mean(revenue.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_189d_slope_v128_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 189) / _mean(revenue.abs(), 189).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 189)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_gapxprcvol_252d_slope_v129_signal(netinc, revenue, closeadj):
    g = _f10_netinc_revenue_gap(netinc, revenue, 252) / _mean(revenue.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    base_series = g * pv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_21d_slope_v130_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    pv = _std(closeadj.pct_change(), 21)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_42d_slope_v131_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 42)
    pv = _std(closeadj.pct_change(), 42)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_63d_slope_v132_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    pv = _std(closeadj.pct_change(), 63)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_126d_slope_v133_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    pv = _std(closeadj.pct_change(), 126)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_189d_slope_v134_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 189)
    pv = _std(closeadj.pct_change(), 189)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coxprcvol_252d_slope_v135_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    pv = _std(closeadj.pct_change(), 252)
    base_series = co * pv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_21d_slope_v136_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 21)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_42d_slope_v137_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 42)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_63d_slope_v138_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 63)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_126d_slope_v139_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 126) / _mean(netinc.abs(), 126).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 126)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_189d_slope_v140_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 189) / _mean(netinc.abs(), 189).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 189)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigxprcvol_252d_slope_v141_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 252) / _mean(netinc.abs(), 252).replace(0, np.nan)
    pv = _std(closeadj.pct_change(), 252)
    base_series = ps * pv * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_21d_slope_v142_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 21)
    base_series = co.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_42d_slope_v143_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 42)
    base_series = co.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_63d_slope_v144_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 63)
    base_series = co.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_126d_slope_v145_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 126)
    base_series = co.rolling(126, min_periods=max(1, 126//2)).sum() * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_189d_slope_v146_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 189)
    base_series = co.rolling(189, min_periods=max(1, 189//2)).sum() * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_coproxyacc_252d_slope_v147_signal(netinc, revenue, closeadj):
    co = _f10_chargeoff_proxy(netinc, revenue, 252)
    base_series = co.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_21d_slope_v148_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 21) / _mean(netinc.abs(), 21).replace(0, np.nan)
    base_series = ps.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_42d_slope_v149_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 42) / _mean(netinc.abs(), 42).replace(0, np.nan)
    base_series = ps.rolling(42, min_periods=max(1, 42//2)).sum() * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f10nco_f10_net_charge_off_proxy_provsigacc_63d_slope_v150_signal(netinc, closeadj):
    ps = _f10_provision_signature(netinc, 63) / _mean(netinc.abs(), 63).replace(0, np.nan)
    base_series = ps.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10nco_f10_net_charge_off_proxy_nirevgap_5d_slope_v001_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_10d_slope_v002_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_21d_slope_v003_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_42d_slope_v004_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_63d_slope_v005_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_126d_slope_v006_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_189d_slope_v007_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_252d_slope_v008_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_378d_slope_v009_signal,
    f10nco_f10_net_charge_off_proxy_nirevgap_504d_slope_v010_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_5d_slope_v011_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_10d_slope_v012_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_21d_slope_v013_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_42d_slope_v014_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_63d_slope_v015_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_126d_slope_v016_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_189d_slope_v017_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_252d_slope_v018_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_378d_slope_v019_signal,
    f10nco_f10_net_charge_off_proxy_coproxy_504d_slope_v020_signal,
    f10nco_f10_net_charge_off_proxy_provsig_5d_slope_v021_signal,
    f10nco_f10_net_charge_off_proxy_provsig_10d_slope_v022_signal,
    f10nco_f10_net_charge_off_proxy_provsig_21d_slope_v023_signal,
    f10nco_f10_net_charge_off_proxy_provsig_42d_slope_v024_signal,
    f10nco_f10_net_charge_off_proxy_provsig_63d_slope_v025_signal,
    f10nco_f10_net_charge_off_proxy_provsig_126d_slope_v026_signal,
    f10nco_f10_net_charge_off_proxy_provsig_189d_slope_v027_signal,
    f10nco_f10_net_charge_off_proxy_provsig_252d_slope_v028_signal,
    f10nco_f10_net_charge_off_proxy_provsig_378d_slope_v029_signal,
    f10nco_f10_net_charge_off_proxy_provsig_504d_slope_v030_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_21d_slope_v031_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_63d_slope_v032_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_126d_slope_v033_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapz_252d_slope_v034_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_21d_slope_v035_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_63d_slope_v036_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_126d_slope_v037_signal,
    f10nco_f10_net_charge_off_proxy_coproxyz_252d_slope_v038_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_21d_slope_v039_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_63d_slope_v040_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_126d_slope_v041_signal,
    f10nco_f10_net_charge_off_proxy_provsigz_252d_slope_v042_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_10d_slope_v043_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_21d_slope_v044_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_63d_slope_v045_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_126d_slope_v046_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapema_252d_slope_v047_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_10d_slope_v048_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_21d_slope_v049_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_63d_slope_v050_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_126d_slope_v051_signal,
    f10nco_f10_net_charge_off_proxy_coproxyema_252d_slope_v052_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_10d_slope_v053_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_21d_slope_v054_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_63d_slope_v055_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_126d_slope_v056_signal,
    f10nco_f10_net_charge_off_proxy_provsigema_252d_slope_v057_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_5d_slope_v058_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_21d_slope_v059_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_63d_slope_v060_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_126d_slope_v061_signal,
    f10nco_f10_net_charge_off_proxy_nirevgapchg_252d_slope_v062_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_5d_slope_v063_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_21d_slope_v064_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_63d_slope_v065_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_126d_slope_v066_signal,
    f10nco_f10_net_charge_off_proxy_coproxychg_252d_slope_v067_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_5d_slope_v068_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_21d_slope_v069_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_63d_slope_v070_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_126d_slope_v071_signal,
    f10nco_f10_net_charge_off_proxy_provsigchg_252d_slope_v072_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_63d_slope_v073_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_126d_slope_v074_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprank_252d_slope_v075_signal,
    f10nco_f10_net_charge_off_proxy_coproxyrank_63d_slope_v076_signal,
    f10nco_f10_net_charge_off_proxy_coproxyrank_126d_slope_v077_signal,
    f10nco_f10_net_charge_off_proxy_coproxyrank_252d_slope_v078_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_63d_slope_v079_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_126d_slope_v080_signal,
    f10nco_f10_net_charge_off_proxy_provsigrank_252d_slope_v081_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_21d_slope_v082_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_63d_slope_v083_signal,
    f10nco_f10_net_charge_off_proxy_provsiglog_252d_slope_v084_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_21d_slope_v085_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_63d_slope_v086_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_126d_slope_v087_signal,
    f10nco_f10_net_charge_off_proxy_coxprov_252d_slope_v088_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_21d_slope_v089_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_63d_slope_v090_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_126d_slope_v091_signal,
    f10nco_f10_net_charge_off_proxy_gapxco_252d_slope_v092_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_21v63_slope_v093_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_21v63_slope_v094_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_63v252_slope_v095_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_63v252_slope_v096_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_126v504_slope_v097_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_126v504_slope_v098_signal,
    f10nco_f10_net_charge_off_proxy_coproxyratio_42v189_slope_v099_signal,
    f10nco_f10_net_charge_off_proxy_provsigratio_42v189_slope_v100_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_63d_slope_v101_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_126d_slope_v102_signal,
    f10nco_f10_net_charge_off_proxy_nirevgaprange_252d_slope_v103_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_21d_slope_v104_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_63d_slope_v105_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_126d_slope_v106_signal,
    f10nco_f10_net_charge_off_proxy_coproxystd_252d_slope_v107_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_21d_slope_v108_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_63d_slope_v109_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_126d_slope_v110_signal,
    f10nco_f10_net_charge_off_proxy_provsigstd_252d_slope_v111_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_21d_slope_v112_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_63d_slope_v113_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_126d_slope_v114_signal,
    f10nco_f10_net_charge_off_proxy_gapxrevgrowth_252d_slope_v115_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_21d_slope_v116_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_63d_slope_v117_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_126d_slope_v118_signal,
    f10nco_f10_net_charge_off_proxy_coxrev_252d_slope_v119_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_21d_slope_v120_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_63d_slope_v121_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_126d_slope_v122_signal,
    f10nco_f10_net_charge_off_proxy_provsigxrev_252d_slope_v123_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_21d_slope_v124_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_42d_slope_v125_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_63d_slope_v126_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_126d_slope_v127_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_189d_slope_v128_signal,
    f10nco_f10_net_charge_off_proxy_gapxprcvol_252d_slope_v129_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_21d_slope_v130_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_42d_slope_v131_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_63d_slope_v132_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_126d_slope_v133_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_189d_slope_v134_signal,
    f10nco_f10_net_charge_off_proxy_coxprcvol_252d_slope_v135_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_21d_slope_v136_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_42d_slope_v137_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_63d_slope_v138_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_126d_slope_v139_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_189d_slope_v140_signal,
    f10nco_f10_net_charge_off_proxy_provsigxprcvol_252d_slope_v141_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_21d_slope_v142_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_42d_slope_v143_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_63d_slope_v144_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_126d_slope_v145_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_189d_slope_v146_signal,
    f10nco_f10_net_charge_off_proxy_coproxyacc_252d_slope_v147_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_21d_slope_v148_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_42d_slope_v149_signal,
    f10nco_f10_net_charge_off_proxy_provsigacc_63d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_NET_CHARGE_OFF_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f10_net_charge_off_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
