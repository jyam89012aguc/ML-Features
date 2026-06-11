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
def _f47_fake_growth(revenue, marketcap, w):
    rev_g = revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    mcap_g = marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return rev_g - mcap_g


def _f47_fakegrowth_valgap(netinc, marketcap, w):
    ni_g = netinc.diff(w) / netinc.shift(w).abs().replace(0, np.nan)
    mcap_g = marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return mcap_g - ni_g


def _f47_fakegrowth_psgap(revenue, ps, w):
    rev_g = revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    ps_g = ps.diff(w) / ps.shift(w).abs().replace(0, np.nan)
    return ps_g - rev_g


# 21d fake-growth gap: revenue growth minus marketcap growth
def f47fgd_f47_fake_growth_detector_revmcapgap_21d_base_v001_signal(revenue, marketcap):
    result = _f47_fake_growth(revenue, marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fake-growth gap: revenue growth minus marketcap growth
def f47fgd_f47_fake_growth_detector_revmcapgap_63d_base_v002_signal(revenue, marketcap):
    result = _f47_fake_growth(revenue, marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fake-growth gap
def f47fgd_f47_fake_growth_detector_revmcapgap_126d_base_v003_signal(revenue, marketcap):
    result = _f47_fake_growth(revenue, marketcap, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fake-growth gap
def f47fgd_f47_fake_growth_detector_revmcapgap_252d_base_v004_signal(revenue, marketcap):
    result = _f47_fake_growth(revenue, marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fake-growth gap
def f47fgd_f47_fake_growth_detector_revmcapgap_504d_base_v005_signal(revenue, marketcap):
    result = _f47_fake_growth(revenue, marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of 63d fake-growth gap
def f47fgd_f47_fake_growth_detector_fakemean_21d_base_v006_signal(revenue, marketcap):
    result = _mean(_f47_fake_growth(revenue, marketcap, 63), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of 252d fake-growth gap
def f47fgd_f47_fake_growth_detector_fakemean_63d_base_v007_signal(revenue, marketcap):
    result = _mean(_f47_fake_growth(revenue, marketcap, 252), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of fake-growth gap
def f47fgd_f47_fake_growth_detector_fakestd_63d_base_v008_signal(revenue, marketcap):
    result = _std(_f47_fake_growth(revenue, marketcap, 63), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of fake-growth gap
def f47fgd_f47_fake_growth_detector_fakestd_252d_base_v009_signal(revenue, marketcap):
    result = _std(_f47_fake_growth(revenue, marketcap, 252), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d fake-growth gap over 252d
def f47fgd_f47_fake_growth_detector_fakez_252d_base_v010_signal(revenue, marketcap):
    result = _z(_f47_fake_growth(revenue, marketcap, 63), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d fake-growth gap over 504d
def f47fgd_f47_fake_growth_detector_fakez_504d_base_v011_signal(revenue, marketcap):
    result = _z(_f47_fake_growth(revenue, marketcap, 252), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-income vs marketcap valuation-gap
def f47fgd_f47_fake_growth_detector_nimcapgap_63d_base_v012_signal(netinc, marketcap):
    result = _f47_fakegrowth_valgap(netinc, marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net-income vs marketcap valuation-gap
def f47fgd_f47_fake_growth_detector_nimcapgap_126d_base_v013_signal(netinc, marketcap):
    result = _f47_fakegrowth_valgap(netinc, marketcap, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-income vs marketcap valuation-gap
def f47fgd_f47_fake_growth_detector_nimcapgap_252d_base_v014_signal(netinc, marketcap):
    result = _f47_fakegrowth_valgap(netinc, marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net-income vs marketcap valuation-gap
def f47fgd_f47_fake_growth_detector_nimcapgap_504d_base_v015_signal(netinc, marketcap):
    result = _f47_fakegrowth_valgap(netinc, marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ps-vs-revenue gap (pricing premium against revenue acceleration)
def f47fgd_f47_fake_growth_detector_psrevgap_63d_base_v016_signal(revenue, ps, marketcap):
    result = _f47_fakegrowth_psgap(revenue, ps, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ps-vs-revenue gap
def f47fgd_f47_fake_growth_detector_psrevgap_252d_base_v017_signal(revenue, ps, marketcap):
    result = _f47_fakegrowth_psgap(revenue, ps, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ps-vs-revenue gap
def f47fgd_f47_fake_growth_detector_psrevgap_504d_base_v018_signal(revenue, ps, marketcap):
    result = _f47_fakegrowth_psgap(revenue, ps, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# revenue divided by marketcap (organic-vs-priced ratio)
def f47fgd_f47_fake_growth_detector_revovermcap_21d_base_v019_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 21)
    result = (revenue / marketcap.replace(0, np.nan)) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean of revenue/marketcap with fake-growth coupling
def f47fgd_f47_fake_growth_detector_revovermcapmean_63d_base_v020_signal(revenue, marketcap):
    rm = revenue / marketcap.replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = _mean(rm, 63) + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue growth times 21d marketcap (priced-revenue gap weighted)
def f47fgd_f47_fake_growth_detector_revgxmcap_21d_base_v021_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 21)
    result = g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# squared revenue-marketcap gap at 63d (severity of decoupling)
def f47fgd_f47_fake_growth_detector_revmcapgapsq_63d_base_v022_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# squared revenue-marketcap gap at 252d
def f47fgd_f47_fake_growth_detector_revmcapgapsq_252d_base_v023_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days revenue growth lagged marketcap by >5%
def f47fgd_f47_fake_growth_detector_lagcount5_252d_base_v024_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = (g).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days revenue growth lagged marketcap by >15%
def f47fgd_f47_fake_growth_detector_lagcount15_504d_base_v025_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = (g).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst (most-negative) fake-growth gap
def f47fgd_f47_fake_growth_detector_worstgap_63d_base_v026_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g.rolling(63, min_periods=21).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst fake-growth gap
def f47fgd_f47_fake_growth_detector_worstgap_252d_base_v027_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g.rolling(252, min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst fake-growth gap
def f47fgd_f47_fake_growth_detector_worstgap_504d_base_v028_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504)
    result = g.rolling(504, min_periods=126).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-income vs marketcap squared gap (overvaluation severity)
def f47fgd_f47_fake_growth_detector_nimcapsq_63d_base_v029_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-income vs marketcap squared gap
def f47fgd_f47_fake_growth_detector_nimcapsq_252d_base_v030_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of net-income vs marketcap gap
def f47fgd_f47_fake_growth_detector_nimcapstd_63d_base_v031_signal(netinc, marketcap):
    result = _std(_f47_fakegrowth_valgap(netinc, marketcap, 63), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of net-income vs marketcap gap
def f47fgd_f47_fake_growth_detector_nimcapstd_252d_base_v032_signal(netinc, marketcap):
    result = _std(_f47_fakegrowth_valgap(netinc, marketcap, 252), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d net-income gap over 252d
def f47fgd_f47_fake_growth_detector_nimcapz_252d_base_v033_signal(netinc, marketcap):
    result = _z(_f47_fakegrowth_valgap(netinc, marketcap, 63), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d net-income gap over 504d
def f47fgd_f47_fake_growth_detector_nimcapz_504d_base_v034_signal(netinc, marketcap):
    result = _z(_f47_fakegrowth_valgap(netinc, marketcap, 252), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ps-vs-revenue squared gap (inflated multiple severity)
def f47fgd_f47_fake_growth_detector_psrevsq_63d_base_v035_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ps-vs-revenue squared gap
def f47fgd_f47_fake_growth_detector_psrevsq_252d_base_v036_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst ps-vs-revenue gap (peak fake-growth premium)
def f47fgd_f47_fake_growth_detector_worstpsgap_252d_base_v037_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = g.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst ps-vs-revenue gap
def f47fgd_f47_fake_growth_detector_worstpsgap_504d_base_v038_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 504)
    result = g.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ps-vs-revenue gap over 252d
def f47fgd_f47_fake_growth_detector_psrevz_252d_base_v039_signal(revenue, ps, marketcap):
    result = _z(_f47_fakegrowth_psgap(revenue, ps, 63), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ps-vs-revenue gap over 504d
def f47fgd_f47_fake_growth_detector_psrevz_504d_base_v040_signal(revenue, ps, marketcap):
    result = _z(_f47_fakegrowth_psgap(revenue, ps, 252), 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days where ps-vs-revenue gap exceeded 10%
def f47fgd_f47_fake_growth_detector_psrevcount10_252d_base_v041_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    result = (g).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean ps-gap (continuous version) scaled by marketcap
def f47fgd_f47_fake_growth_detector_psrevcount30_504d_base_v042_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = g.rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite fake-growth: revenue gap plus ps gap
def f47fgd_f47_fake_growth_detector_combogap_63d_base_v043_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_psgap(revenue, ps, 63)
    result = (a + b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite fake-growth
def f47fgd_f47_fake_growth_detector_combogap_252d_base_v044_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = (a + b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite fake-growth
def f47fgd_f47_fake_growth_detector_combogap_504d_base_v045_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 504)
    b = _f47_fakegrowth_psgap(revenue, ps, 504)
    result = (a + b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-gap area (sum of magnitudes)
def f47fgd_f47_fake_growth_detector_gaparea_63d_base_v046_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63).abs()
    result = g.rolling(63, min_periods=21).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-gap area
def f47fgd_f47_fake_growth_detector_gaparea_252d_base_v047_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252).abs()
    result = g.rolling(252, min_periods=63).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue-gap area
def f47fgd_f47_fake_growth_detector_gaparea_504d_base_v048_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504).abs()
    result = g.rolling(504, min_periods=126).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap growth alone weighted by revenue gap
def f47fgd_f47_fake_growth_detector_mcapgxgap_63d_base_v049_signal(revenue, marketcap):
    mg = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = mg * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap growth alone weighted by revenue gap
def f47fgd_f47_fake_growth_detector_mcapgxgap_252d_base_v050_signal(revenue, marketcap):
    mg = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = mg * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev premium fake-growth (ev growth vs revenue growth)
def f47fgd_f47_fake_growth_detector_evrevgap_21d_base_v051_signal(revenue, ev, marketcap):
    eg = ev.diff(21) / ev.shift(21).abs().replace(0, np.nan)
    rg = revenue.diff(21) / revenue.shift(21).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 21)
    result = (eg - rg) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev premium fake-growth
def f47fgd_f47_fake_growth_detector_evrevgap_63d_base_v052_signal(revenue, ev, marketcap):
    eg = ev.diff(63) / ev.shift(63).abs().replace(0, np.nan)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = (eg - rg) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev premium fake-growth
def f47fgd_f47_fake_growth_detector_evrevgap_252d_base_v053_signal(revenue, ev, marketcap):
    eg = ev.diff(252) / ev.shift(252).abs().replace(0, np.nan)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 252)
    result = (eg - rg) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pe-vs-netinc decoupling
def f47fgd_f47_fake_growth_detector_pegap_63d_base_v054_signal(netinc, pe, marketcap):
    pg = pe.diff(63) / pe.shift(63).abs().replace(0, np.nan)
    ng = netinc.diff(63) / netinc.shift(63).abs().replace(0, np.nan)
    base = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = (pg - ng) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pe-vs-netinc decoupling
def f47fgd_f47_fake_growth_detector_pegap_252d_base_v055_signal(netinc, pe, marketcap):
    pg = pe.diff(252) / pe.shift(252).abs().replace(0, np.nan)
    ng = netinc.diff(252) / netinc.shift(252).abs().replace(0, np.nan)
    base = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = (pg - ng) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap minus 252d revenue-mcap gap (fakeness acceleration)
def f47fgd_f47_fake_growth_detector_gapdiff_63m252_base_v056_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fake_growth(revenue, marketcap, 252)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-mcap gap minus 63d revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapdiff_21m63_base_v057_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 21)
    b = _f47_fake_growth(revenue, marketcap, 63)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap minus 504d revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapdiff_252m504_base_v058_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fake_growth(revenue, marketcap, 504)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap divided by 252d revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapratio_63v252_base_v059_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fake_growth(revenue, marketcap, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue-mcap gap divided by 63d revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapratio_21v63_base_v060_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 21)
    b = _f47_fake_growth(revenue, marketcap, 63).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapema_63d_base_v061_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapema_252d_base_v062_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of net-income vs marketcap gap
def f47fgd_f47_fake_growth_detector_nimcapema_63d_base_v063_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = g.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of net-income vs marketcap gap
def f47fgd_f47_fake_growth_detector_nimcapema_252d_base_v064_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = g.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap times pe (priced-fake interaction)
def f47fgd_f47_fake_growth_detector_gapxpe_63d_base_v065_signal(revenue, marketcap, pe):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap times pe
def f47fgd_f47_fake_growth_detector_gapxpe_252d_base_v066_signal(revenue, marketcap, pe):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap times ps
def f47fgd_f47_fake_growth_detector_gapxps_63d_base_v067_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap times ps
def f47fgd_f47_fake_growth_detector_gapxps_252d_base_v068_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding-min revenue-mcap gap (worst-ever fake)
def f47fgd_f47_fake_growth_detector_gapworstever_base_v069_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g.expanding(min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap minus expanding worst-ever (gap-vs-history)
def f47fgd_f47_fake_growth_detector_gapvsever_63d_base_v070_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    worst = g.expanding(min_periods=63).min()
    result = (g - worst) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap minus expanding worst-ever
def f47fgd_f47_fake_growth_detector_gapvsever_252d_base_v071_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    worst = g.expanding(min_periods=63).min()
    result = (g - worst) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap times marketcap growth (fake-growth with mcap inflating)
def f47fgd_f47_fake_growth_detector_gapxmcapg_63d_base_v072_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    mg = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    result = g * mg.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap times marketcap growth
def f47fgd_f47_fake_growth_detector_gapxmcapg_252d_base_v073_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    mg = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    result = g * mg.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite severity: |gap| * |valgap| * marketcap
def f47fgd_f47_fake_growth_detector_combosev_63d_base_v074_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63).abs()
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity: |gap| * |valgap| * marketcap
def f47fgd_f47_fake_growth_detector_combosev_252d_base_v075_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252).abs()
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47fgd_f47_fake_growth_detector_revmcapgap_21d_base_v001_signal,
    f47fgd_f47_fake_growth_detector_revmcapgap_63d_base_v002_signal,
    f47fgd_f47_fake_growth_detector_revmcapgap_126d_base_v003_signal,
    f47fgd_f47_fake_growth_detector_revmcapgap_252d_base_v004_signal,
    f47fgd_f47_fake_growth_detector_revmcapgap_504d_base_v005_signal,
    f47fgd_f47_fake_growth_detector_fakemean_21d_base_v006_signal,
    f47fgd_f47_fake_growth_detector_fakemean_63d_base_v007_signal,
    f47fgd_f47_fake_growth_detector_fakestd_63d_base_v008_signal,
    f47fgd_f47_fake_growth_detector_fakestd_252d_base_v009_signal,
    f47fgd_f47_fake_growth_detector_fakez_252d_base_v010_signal,
    f47fgd_f47_fake_growth_detector_fakez_504d_base_v011_signal,
    f47fgd_f47_fake_growth_detector_nimcapgap_63d_base_v012_signal,
    f47fgd_f47_fake_growth_detector_nimcapgap_126d_base_v013_signal,
    f47fgd_f47_fake_growth_detector_nimcapgap_252d_base_v014_signal,
    f47fgd_f47_fake_growth_detector_nimcapgap_504d_base_v015_signal,
    f47fgd_f47_fake_growth_detector_psrevgap_63d_base_v016_signal,
    f47fgd_f47_fake_growth_detector_psrevgap_252d_base_v017_signal,
    f47fgd_f47_fake_growth_detector_psrevgap_504d_base_v018_signal,
    f47fgd_f47_fake_growth_detector_revovermcap_21d_base_v019_signal,
    f47fgd_f47_fake_growth_detector_revovermcapmean_63d_base_v020_signal,
    f47fgd_f47_fake_growth_detector_revgxmcap_21d_base_v021_signal,
    f47fgd_f47_fake_growth_detector_revmcapgapsq_63d_base_v022_signal,
    f47fgd_f47_fake_growth_detector_revmcapgapsq_252d_base_v023_signal,
    f47fgd_f47_fake_growth_detector_lagcount5_252d_base_v024_signal,
    f47fgd_f47_fake_growth_detector_lagcount15_504d_base_v025_signal,
    f47fgd_f47_fake_growth_detector_worstgap_63d_base_v026_signal,
    f47fgd_f47_fake_growth_detector_worstgap_252d_base_v027_signal,
    f47fgd_f47_fake_growth_detector_worstgap_504d_base_v028_signal,
    f47fgd_f47_fake_growth_detector_nimcapsq_63d_base_v029_signal,
    f47fgd_f47_fake_growth_detector_nimcapsq_252d_base_v030_signal,
    f47fgd_f47_fake_growth_detector_nimcapstd_63d_base_v031_signal,
    f47fgd_f47_fake_growth_detector_nimcapstd_252d_base_v032_signal,
    f47fgd_f47_fake_growth_detector_nimcapz_252d_base_v033_signal,
    f47fgd_f47_fake_growth_detector_nimcapz_504d_base_v034_signal,
    f47fgd_f47_fake_growth_detector_psrevsq_63d_base_v035_signal,
    f47fgd_f47_fake_growth_detector_psrevsq_252d_base_v036_signal,
    f47fgd_f47_fake_growth_detector_worstpsgap_252d_base_v037_signal,
    f47fgd_f47_fake_growth_detector_worstpsgap_504d_base_v038_signal,
    f47fgd_f47_fake_growth_detector_psrevz_252d_base_v039_signal,
    f47fgd_f47_fake_growth_detector_psrevz_504d_base_v040_signal,
    f47fgd_f47_fake_growth_detector_psrevcount10_252d_base_v041_signal,
    f47fgd_f47_fake_growth_detector_psrevcount30_504d_base_v042_signal,
    f47fgd_f47_fake_growth_detector_combogap_63d_base_v043_signal,
    f47fgd_f47_fake_growth_detector_combogap_252d_base_v044_signal,
    f47fgd_f47_fake_growth_detector_combogap_504d_base_v045_signal,
    f47fgd_f47_fake_growth_detector_gaparea_63d_base_v046_signal,
    f47fgd_f47_fake_growth_detector_gaparea_252d_base_v047_signal,
    f47fgd_f47_fake_growth_detector_gaparea_504d_base_v048_signal,
    f47fgd_f47_fake_growth_detector_mcapgxgap_63d_base_v049_signal,
    f47fgd_f47_fake_growth_detector_mcapgxgap_252d_base_v050_signal,
    f47fgd_f47_fake_growth_detector_evrevgap_21d_base_v051_signal,
    f47fgd_f47_fake_growth_detector_evrevgap_63d_base_v052_signal,
    f47fgd_f47_fake_growth_detector_evrevgap_252d_base_v053_signal,
    f47fgd_f47_fake_growth_detector_pegap_63d_base_v054_signal,
    f47fgd_f47_fake_growth_detector_pegap_252d_base_v055_signal,
    f47fgd_f47_fake_growth_detector_gapdiff_63m252_base_v056_signal,
    f47fgd_f47_fake_growth_detector_gapdiff_21m63_base_v057_signal,
    f47fgd_f47_fake_growth_detector_gapdiff_252m504_base_v058_signal,
    f47fgd_f47_fake_growth_detector_gapratio_63v252_base_v059_signal,
    f47fgd_f47_fake_growth_detector_gapratio_21v63_base_v060_signal,
    f47fgd_f47_fake_growth_detector_gapema_63d_base_v061_signal,
    f47fgd_f47_fake_growth_detector_gapema_252d_base_v062_signal,
    f47fgd_f47_fake_growth_detector_nimcapema_63d_base_v063_signal,
    f47fgd_f47_fake_growth_detector_nimcapema_252d_base_v064_signal,
    f47fgd_f47_fake_growth_detector_gapxpe_63d_base_v065_signal,
    f47fgd_f47_fake_growth_detector_gapxpe_252d_base_v066_signal,
    f47fgd_f47_fake_growth_detector_gapxps_63d_base_v067_signal,
    f47fgd_f47_fake_growth_detector_gapxps_252d_base_v068_signal,
    f47fgd_f47_fake_growth_detector_gapworstever_base_v069_signal,
    f47fgd_f47_fake_growth_detector_gapvsever_63d_base_v070_signal,
    f47fgd_f47_fake_growth_detector_gapvsever_252d_base_v071_signal,
    f47fgd_f47_fake_growth_detector_gapxmcapg_63d_base_v072_signal,
    f47fgd_f47_fake_growth_detector_gapxmcapg_252d_base_v073_signal,
    f47fgd_f47_fake_growth_detector_combosev_63d_base_v074_signal,
    f47fgd_f47_fake_growth_detector_combosev_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_FAKE_GROWTH_DETECTOR_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    ev = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.014, n))), name="ev")
    ps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="ps")
    pe = pd.Series(20.0 * np.exp(np.cumsum(np.random.normal(0.0001, 0.013, n))), name="pe")

    cols = {
        "marketcap": marketcap, "revenue": revenue, "netinc": netinc,
        "ev": ev, "ps": ps, "pe": pe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_fake_growth", "_f47_fakegrowth_valgap", "_f47_fakegrowth_psgap")
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
    print(f"OK f47_fake_growth_detector_base_001_075_claude: {n_features} features pass")
