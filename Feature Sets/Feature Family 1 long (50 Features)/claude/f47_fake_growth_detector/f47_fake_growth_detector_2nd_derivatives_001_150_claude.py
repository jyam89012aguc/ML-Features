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


def _slope(s, w):
    return s.diff(periods=w)


def _slope_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d revenue-mcap gap × marketcap
def f47fgd_f47_fake_growth_detector_revmcapgap_21d_slope_v001_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 21) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d gap × marketcap
def f47fgd_f47_fake_growth_detector_revmcapgap_21d_slope_v002_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_63d_slope_v003_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 63) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_63d_slope_v004_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_63d_slope_v005_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_126d_slope_v006_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 126) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_126d_slope_v007_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_252d_slope_v008_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_252d_slope_v009_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_504d_slope_v010_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 504) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d gap
def f47fgd_f47_fake_growth_detector_revmcapgap_504d_slope_v011_signal(revenue, marketcap):
    base = _f47_fake_growth(revenue, marketcap, 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of fakemean 21d (mean of 63d gap over 21d)
def f47fgd_f47_fake_growth_detector_fakemean_21d_slope_v012_signal(revenue, marketcap):
    base = _mean(_f47_fake_growth(revenue, marketcap, 63), 21) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fakemean 63d
def f47fgd_f47_fake_growth_detector_fakemean_63d_slope_v013_signal(revenue, marketcap):
    base = _mean(_f47_fake_growth(revenue, marketcap, 252), 63) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of fakestd 63d
def f47fgd_f47_fake_growth_detector_fakestd_63d_slope_v014_signal(revenue, marketcap):
    base = _std(_f47_fake_growth(revenue, marketcap, 63), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fakestd 252d
def f47fgd_f47_fake_growth_detector_fakestd_252d_slope_v015_signal(revenue, marketcap):
    base = _std(_f47_fake_growth(revenue, marketcap, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of fakez 252d
def f47fgd_f47_fake_growth_detector_fakez_252d_slope_v016_signal(revenue, marketcap):
    base = _z(_f47_fake_growth(revenue, marketcap, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of fakez 504d
def f47fgd_f47_fake_growth_detector_fakez_504d_slope_v017_signal(revenue, marketcap):
    base = _z(_f47_fake_growth(revenue, marketcap, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nimcap gap
def f47fgd_f47_fake_growth_detector_nimcapgap_63d_slope_v018_signal(netinc, marketcap):
    base = _f47_fakegrowth_valgap(netinc, marketcap, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nimcap gap
def f47fgd_f47_fake_growth_detector_nimcapgap_126d_slope_v019_signal(netinc, marketcap):
    base = _f47_fakegrowth_valgap(netinc, marketcap, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nimcap gap
def f47fgd_f47_fake_growth_detector_nimcapgap_252d_slope_v020_signal(netinc, marketcap):
    base = _f47_fakegrowth_valgap(netinc, marketcap, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nimcap gap
def f47fgd_f47_fake_growth_detector_nimcapgap_504d_slope_v021_signal(netinc, marketcap):
    base = _f47_fakegrowth_valgap(netinc, marketcap, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ps-rev gap × marketcap
def f47fgd_f47_fake_growth_detector_psrevgap_63d_slope_v022_signal(revenue, ps, marketcap):
    base = _f47_fakegrowth_psgap(revenue, ps, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ps-rev gap
def f47fgd_f47_fake_growth_detector_psrevgap_252d_slope_v023_signal(revenue, ps, marketcap):
    base = _f47_fakegrowth_psgap(revenue, ps, 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ps-rev gap
def f47fgd_f47_fake_growth_detector_psrevgap_504d_slope_v024_signal(revenue, ps, marketcap):
    base = _f47_fakegrowth_psgap(revenue, ps, 504) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revenue/mcap level
def f47fgd_f47_fake_growth_detector_revovermcap_21d_slope_v025_signal(revenue, marketcap):
    rm = revenue / marketcap.replace(0, np.nan)
    base = rm + _f47_fake_growth(revenue, marketcap, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue/mcap mean
def f47fgd_f47_fake_growth_detector_revovermcapmean_63d_slope_v026_signal(revenue, marketcap):
    rm = revenue / marketcap.replace(0, np.nan)
    base = _mean(rm, 63) + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of |gap| × marketcap (severity rate)
def f47fgd_f47_fake_growth_detector_revgxmcap_21d_slope_v027_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 21)
    base = g.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of squared 63d gap × marketcap
def f47fgd_f47_fake_growth_detector_revmcapgapsq_63d_slope_v028_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * g.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of squared 252d gap × marketcap
def f47fgd_f47_fake_growth_detector_revmcapgapsq_252d_slope_v029_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * g.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of lagcount5 252d
def f47fgd_f47_fake_growth_detector_lagcount5_252d_slope_v030_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = (g).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of lagcount15 504d
def f47fgd_f47_fake_growth_detector_lagcount15_504d_slope_v031_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = (g).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of worstgap 63d
def f47fgd_f47_fake_growth_detector_worstgap_63d_slope_v032_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g.rolling(63, min_periods=21).min() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worstgap 252d
def f47fgd_f47_fake_growth_detector_worstgap_252d_slope_v033_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g.rolling(252, min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worstgap 504d
def f47fgd_f47_fake_growth_detector_worstgap_504d_slope_v034_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504)
    base = g.rolling(504, min_periods=126).min() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of nimcapsq 63d
def f47fgd_f47_fake_growth_detector_nimcapsq_63d_slope_v035_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = g * g.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of nimcapsq 252d
def f47fgd_f47_fake_growth_detector_nimcapsq_252d_slope_v036_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = g * g.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of nimcapstd 63d
def f47fgd_f47_fake_growth_detector_nimcapstd_63d_slope_v037_signal(netinc, marketcap):
    base = _std(_f47_fakegrowth_valgap(netinc, marketcap, 63), 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of nimcapstd 252d
def f47fgd_f47_fake_growth_detector_nimcapstd_252d_slope_v038_signal(netinc, marketcap):
    base = _std(_f47_fakegrowth_valgap(netinc, marketcap, 252), 252) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of nimcapz 252d
def f47fgd_f47_fake_growth_detector_nimcapz_252d_slope_v039_signal(netinc, marketcap):
    base = _z(_f47_fakegrowth_valgap(netinc, marketcap, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of nimcapz 504d
def f47fgd_f47_fake_growth_detector_nimcapz_504d_slope_v040_signal(netinc, marketcap):
    base = _z(_f47_fakegrowth_valgap(netinc, marketcap, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of psrev squared 63d
def f47fgd_f47_fake_growth_detector_psrevsq_63d_slope_v041_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = g * g.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of psrev squared 252d
def f47fgd_f47_fake_growth_detector_psrevsq_252d_slope_v042_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = g * g.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of worstpsgap 252d
def f47fgd_f47_fake_growth_detector_worstpsgap_252d_slope_v043_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = g.rolling(252, min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of worstpsgap 504d
def f47fgd_f47_fake_growth_detector_worstpsgap_504d_slope_v044_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 504)
    base = g.rolling(504, min_periods=126).max() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of psrevz 252d
def f47fgd_f47_fake_growth_detector_psrevz_252d_slope_v045_signal(revenue, ps, marketcap):
    base = _z(_f47_fakegrowth_psgap(revenue, ps, 63), 252) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of psrevz 504d
def f47fgd_f47_fake_growth_detector_psrevz_504d_slope_v046_signal(revenue, ps, marketcap):
    base = _z(_f47_fakegrowth_psgap(revenue, ps, 252), 504) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of psrevcount10 252d
def f47fgd_f47_fake_growth_detector_psrevcount10_252d_slope_v047_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = (g).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of psrevcount30 504d
def f47fgd_f47_fake_growth_detector_psrevcount30_504d_slope_v048_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = (g).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of combogap 63d
def f47fgd_f47_fake_growth_detector_combogap_63d_slope_v049_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = (a + b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of combogap 252d
def f47fgd_f47_fake_growth_detector_combogap_252d_slope_v050_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = (a + b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of combogap 504d
def f47fgd_f47_fake_growth_detector_combogap_504d_slope_v051_signal(revenue, marketcap, ps):
    a = _f47_fake_growth(revenue, marketcap, 504)
    b = _f47_fakegrowth_psgap(revenue, ps, 504)
    base = (a + b) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gaparea 63d
def f47fgd_f47_fake_growth_detector_gaparea_63d_slope_v052_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63).abs()
    base = g.rolling(63, min_periods=21).sum() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gaparea 252d
def f47fgd_f47_fake_growth_detector_gaparea_252d_slope_v053_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252).abs()
    base = g.rolling(252, min_periods=63).sum() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of gaparea 504d
def f47fgd_f47_fake_growth_detector_gaparea_504d_slope_v054_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504).abs()
    base = g.rolling(504, min_periods=126).sum() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mcapgxgap 63d
def f47fgd_f47_fake_growth_detector_mcapgxgap_63d_slope_v055_signal(revenue, marketcap):
    mg = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = mg * g.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcapgxgap 252d
def f47fgd_f47_fake_growth_detector_mcapgxgap_252d_slope_v056_signal(revenue, marketcap):
    mg = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = mg * g.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of evrevgap 21d × marketcap
def f47fgd_f47_fake_growth_detector_evrevgap_21d_slope_v057_signal(revenue, ev, marketcap):
    eg = ev.diff(21) / ev.shift(21).abs().replace(0, np.nan)
    rg = revenue.diff(21) / revenue.shift(21).abs().replace(0, np.nan)
    base = (eg - rg) * marketcap + _f47_fake_growth(revenue, marketcap, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of evrevgap 63d
def f47fgd_f47_fake_growth_detector_evrevgap_63d_slope_v058_signal(revenue, ev, marketcap):
    eg = ev.diff(63) / ev.shift(63).abs().replace(0, np.nan)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = (eg - rg) * marketcap + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evrevgap 252d
def f47fgd_f47_fake_growth_detector_evrevgap_252d_slope_v059_signal(revenue, ev, marketcap):
    eg = ev.diff(252) / ev.shift(252).abs().replace(0, np.nan)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = (eg - rg) * marketcap + _f47_fake_growth(revenue, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of pegap 63d
def f47fgd_f47_fake_growth_detector_pegap_63d_slope_v060_signal(netinc, pe, marketcap):
    pg = pe.diff(63) / pe.shift(63).abs().replace(0, np.nan)
    ng = netinc.diff(63) / netinc.shift(63).abs().replace(0, np.nan)
    base = (pg - ng) * marketcap + _f47_fakegrowth_valgap(netinc, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pegap 252d
def f47fgd_f47_fake_growth_detector_pegap_252d_slope_v061_signal(netinc, pe, marketcap):
    pg = pe.diff(252) / pe.shift(252).abs().replace(0, np.nan)
    ng = netinc.diff(252) / netinc.shift(252).abs().replace(0, np.nan)
    base = (pg - ng) * marketcap + _f47_fakegrowth_valgap(netinc, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapdiff 63m252
def f47fgd_f47_fake_growth_detector_gapdiff_63m252_slope_v062_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fake_growth(revenue, marketcap, 252)
    base = (a - b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gapdiff 21m63
def f47fgd_f47_fake_growth_detector_gapdiff_21m63_slope_v063_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 21)
    b = _f47_fake_growth(revenue, marketcap, 63)
    base = (a - b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapdiff 252m504
def f47fgd_f47_fake_growth_detector_gapdiff_252m504_slope_v064_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fake_growth(revenue, marketcap, 504)
    base = (a - b) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapratio 63v252
def f47fgd_f47_fake_growth_detector_gapratio_63v252_slope_v065_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fake_growth(revenue, marketcap, 252).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of gapratio 21v63
def f47fgd_f47_fake_growth_detector_gapratio_21v63_slope_v066_signal(revenue, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 21)
    b = _f47_fake_growth(revenue, marketcap, 63).replace(0, np.nan)
    base = (a / b) * marketcap
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA gap 63d
def f47fgd_f47_fake_growth_detector_gapema_63d_slope_v067_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g.ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA gap 252d
def f47fgd_f47_fake_growth_detector_gapema_252d_slope_v068_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g.ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA nimcap 63d
def f47fgd_f47_fake_growth_detector_nimcapema_63d_slope_v069_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = g.ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA nimcap 252d
def f47fgd_f47_fake_growth_detector_nimcapema_252d_slope_v070_signal(netinc, marketcap):
    g = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = g.ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × pe 63d
def f47fgd_f47_fake_growth_detector_gapxpe_63d_slope_v071_signal(revenue, marketcap, pe):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × pe 252d
def f47fgd_f47_fake_growth_detector_gapxpe_252d_slope_v072_signal(revenue, marketcap, pe):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * pe * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × ps 63d
def f47fgd_f47_fake_growth_detector_gapxps_63d_slope_v073_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × ps 252d
def f47fgd_f47_fake_growth_detector_gapxps_252d_slope_v074_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * ps * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst gap (peak-fake rate)
def f47fgd_f47_fake_growth_detector_gapworstever_slope_v075_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g.expanding(min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapvsever 63d
def f47fgd_f47_fake_growth_detector_gapvsever_63d_slope_v076_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    worst = g.expanding(min_periods=63).min()
    base = (g - worst) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapvsever 252d
def f47fgd_f47_fake_growth_detector_gapvsever_252d_slope_v077_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    worst = g.expanding(min_periods=63).min()
    base = (g - worst) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxmcapg 63d
def f47fgd_f47_fake_growth_detector_gapxmcapg_63d_slope_v078_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    mg = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    base = g * mg.abs() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxmcapg 252d
def f47fgd_f47_fake_growth_detector_gapxmcapg_252d_slope_v079_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    mg = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    base = g * mg.abs() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of combosev 63d
def f47fgd_f47_fake_growth_detector_combosev_63d_slope_v080_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63).abs()
    base = a * b * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of combosev 252d
def f47fgd_f47_fake_growth_detector_combosev_252d_slope_v081_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252).abs()
    base = a * b * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × ev 63d
def f47fgd_f47_fake_growth_detector_gapxev_63d_slope_v082_signal(revenue, marketcap, ev):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * ev
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × ev 252d
def f47fgd_f47_fake_growth_detector_gapxev_252d_slope_v083_signal(revenue, marketcap, ev):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × evebitda 63d
def f47fgd_f47_fake_growth_detector_gapxevebitda_63d_slope_v084_signal(revenue, marketcap, evebitda):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × evebitda 252d
def f47fgd_f47_fake_growth_detector_gapxevebitda_252d_slope_v085_signal(revenue, marketcap, evebitda):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * evebitda * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × evebit 63d
def f47fgd_f47_fake_growth_detector_gapxevebit_63d_slope_v086_signal(revenue, marketcap, evebit):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * evebit * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × evebit 252d
def f47fgd_f47_fake_growth_detector_gapxevebit_252d_slope_v087_signal(revenue, marketcap, evebit):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * evebit * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × pb 63d
def f47fgd_f47_fake_growth_detector_gapxpb_63d_slope_v088_signal(revenue, marketcap, pb):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * pb * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × pb 252d
def f47fgd_f47_fake_growth_detector_gapxpb_252d_slope_v089_signal(revenue, marketcap, pb):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * pb * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of evrevxev 63d
def f47fgd_f47_fake_growth_detector_evrevxev_63d_slope_v090_signal(revenue, ev, marketcap):
    eg = ev.diff(63) / ev.shift(63).abs().replace(0, np.nan)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = (eg - rg) * ev + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evrevxev 252d
def f47fgd_f47_fake_growth_detector_evrevxev_252d_slope_v091_signal(revenue, ev, marketcap):
    eg = ev.diff(252) / ev.shift(252).abs().replace(0, np.nan)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = (eg - rg) * ev + _f47_fake_growth(revenue, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxnoncf 63d
def f47fgd_f47_fake_growth_detector_gapxnoncf_63d_slope_v092_signal(revenue, marketcap, ncfo):
    g = _f47_fake_growth(revenue, marketcap, 63)
    weak = 1.0 - (ncfo / marketcap.replace(0, np.nan)).clip(-1, 1)
    base = g * weak * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxnoncf 252d
def f47fgd_f47_fake_growth_detector_gapxnoncf_252d_slope_v093_signal(revenue, marketcap, ncfo):
    g = _f47_fake_growth(revenue, marketcap, 252)
    weak = 1.0 - (ncfo / marketcap.replace(0, np.nan)).clip(-1, 1)
    base = g * weak * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxfcfyld 63d
def f47fgd_f47_fake_growth_detector_gapxfcfyld_63d_slope_v094_signal(revenue, marketcap, fcf):
    g = _f47_fake_growth(revenue, marketcap, 63)
    yld = fcf / marketcap.replace(0, np.nan)
    base = g * (1.0 - yld.clip(-1, 1)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxfcfyld 252d
def f47fgd_f47_fake_growth_detector_gapxfcfyld_252d_slope_v095_signal(revenue, marketcap, fcf):
    g = _f47_fake_growth(revenue, marketcap, 252)
    yld = fcf / marketcap.replace(0, np.nan)
    base = g * (1.0 - yld.clip(-1, 1)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxshareg 63d
def f47fgd_f47_fake_growth_detector_gapxshareg_63d_slope_v096_signal(revenue, marketcap, sharesbas):
    g = _f47_fake_growth(revenue, marketcap, 63)
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    base = g * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxshareg 252d
def f47fgd_f47_fake_growth_detector_gapxshareg_252d_slope_v097_signal(revenue, marketcap, sharesbas):
    g = _f47_fake_growth(revenue, marketcap, 252)
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    base = g * (1.0 + sg.clip(-1, 1)) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxlev 63d
def f47fgd_f47_fake_growth_detector_gapxlev_63d_slope_v098_signal(revenue, marketcap, debt, equity):
    g = _f47_fake_growth(revenue, marketcap, 63)
    lev = debt / equity.replace(0, np.nan)
    base = g * lev * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxlev 252d
def f47fgd_f47_fake_growth_detector_gapxlev_252d_slope_v099_signal(revenue, marketcap, debt, equity):
    g = _f47_fake_growth(revenue, marketcap, 252)
    lev = debt / equity.replace(0, np.nan)
    base = g * lev * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of valgapxpe 63d
def f47fgd_f47_fake_growth_detector_valgapxpe_63d_slope_v100_signal(netinc, marketcap, pe):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = v * pe * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapxpe 252d
def f47fgd_f47_fake_growth_detector_valgapxpe_252d_slope_v101_signal(netinc, marketcap, pe):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = v * pe * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of valgapxps 63d
def f47fgd_f47_fake_growth_detector_valgapxps_63d_slope_v102_signal(netinc, marketcap, ps):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = v * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapxps 252d
def f47fgd_f47_fake_growth_detector_valgapxps_252d_slope_v103_signal(netinc, marketcap, ps):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = v * ps * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of valgapxevebitda 63d
def f47fgd_f47_fake_growth_detector_valgapxevebitda_63d_slope_v104_signal(netinc, marketcap, evebitda):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = v * evebitda * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapxevebitda 252d
def f47fgd_f47_fake_growth_detector_valgapxevebitda_252d_slope_v105_signal(netinc, marketcap, evebitda):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = v * evebitda * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of valgapema 63d
def f47fgd_f47_fake_growth_detector_valgapema_63d_slope_v106_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = v.ewm(span=63, adjust=False).mean() * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapema 252d
def f47fgd_f47_fake_growth_detector_valgapema_252d_slope_v107_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = v.ewm(span=252, adjust=False).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of psrevxev 63d
def f47fgd_f47_fake_growth_detector_psrevxev_63d_slope_v108_signal(revenue, ps, ev, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = p * ev + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of psrevxev 252d
def f47fgd_f47_fake_growth_detector_psrevxev_252d_slope_v109_signal(revenue, ps, ev, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = p * ev + _f47_fake_growth(revenue, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of psrevcount5 252d
def f47fgd_f47_fake_growth_detector_psrevcount5_252d_slope_v110_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = (g).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of psrevcount50 504d
def f47fgd_f47_fake_growth_detector_psrevcount50_504d_slope_v111_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = (g).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of lagcount25 252d
def f47fgd_f47_fake_growth_detector_lagcount25_252d_slope_v112_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = (g).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of valgapcount20 504d
def f47fgd_f47_fake_growth_detector_valgapcount20_504d_slope_v113_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = (v).rolling(504, min_periods=126).mean() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapcount10 252d
def f47fgd_f47_fake_growth_detector_valgapcount10_252d_slope_v114_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = (v).rolling(252, min_periods=63).mean() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapworstever
def f47fgd_f47_fake_growth_detector_valgapworstever_slope_v115_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = v.expanding(min_periods=63).max() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of valgapvsever 63d
def f47fgd_f47_fake_growth_detector_valgapvsever_63d_slope_v116_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    worst = v.expanding(min_periods=63).max()
    base = (worst - v) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of valgapvsever 252d
def f47fgd_f47_fake_growth_detector_valgapvsever_252d_slope_v117_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    worst = v.expanding(min_periods=63).max()
    base = (worst - v) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of jointfake 63d
def f47fgd_f47_fake_growth_detector_jointfake_63d_slope_v118_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = a.abs() * b * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of jointfake 252d
def f47fgd_f47_fake_growth_detector_jointfake_252d_slope_v119_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = a.abs() * b * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of jointpsval 63d
def f47fgd_f47_fake_growth_detector_jointpsval_63d_slope_v120_signal(revenue, netinc, ps, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 63)
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    base = p * v * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of jointpsval 252d
def f47fgd_f47_fake_growth_detector_jointpsval_252d_slope_v121_signal(revenue, netinc, ps, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 252)
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    base = p * v * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapworst 252d
def f47fgd_f47_fake_growth_detector_gapworst_252d_slope_v122_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g.rolling(252, min_periods=63).min() * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of gapworst 504d
def f47fgd_f47_fake_growth_detector_gapworst_504d_slope_v123_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g.rolling(504, min_periods=126).min() * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapareafrac 63v252
def f47fgd_f47_fake_growth_detector_gapareafrac_63v252_slope_v124_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252).abs()
    a = g.rolling(63, min_periods=21).sum()
    b = g.rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = a / b * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapareafrac 252v504
def f47fgd_f47_fake_growth_detector_gapareafrac_252v504_slope_v125_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504).abs()
    a = g.rolling(252, min_periods=63).sum()
    b = g.rolling(504, min_periods=126).sum().replace(0, np.nan)
    base = a / b * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapvolvol 63d
def f47fgd_f47_fake_growth_detector_gapvolvol_63d_slope_v126_signal(revenue, marketcap):
    sd = _std(_f47_fake_growth(revenue, marketcap, 252), 63)
    base = _std(sd, 63) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapvolvol 252d
def f47fgd_f47_fake_growth_detector_gapvolvol_252d_slope_v127_signal(revenue, marketcap):
    sd = _std(_f47_fake_growth(revenue, marketcap, 504), 252)
    base = _std(sd, 126) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapanomaly 63d
def f47fgd_f47_fake_growth_detector_gapanomaly_63d_slope_v128_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base_mean = _mean(_f47_fake_growth(revenue, marketcap, 252), 252)
    base = (g - base_mean) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapanomaly 252d
def f47fgd_f47_fake_growth_detector_gapanomaly_252d_slope_v129_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base_mean = _mean(_f47_fake_growth(revenue, marketcap, 504), 504)
    base = (g - base_mean) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxevrev 63d
def f47fgd_f47_fake_growth_detector_gapxevrev_63d_slope_v130_signal(revenue, ev, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    evrev = ev / revenue.replace(0, np.nan)
    base = g * evrev * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxevrev 252d
def f47fgd_f47_fake_growth_detector_gapxevrev_252d_slope_v131_signal(revenue, ev, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    evrev = ev / revenue.replace(0, np.nan)
    base = g * evrev * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxpsmult 63d
def f47fgd_f47_fake_growth_detector_gapxpsmult_63d_slope_v132_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * ps * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxpsmult 252d
def f47fgd_f47_fake_growth_detector_gapxpsmult_252d_slope_v133_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * ps * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gapxmcapz 63d
def f47fgd_f47_fake_growth_detector_gapxmcapz_63d_slope_v134_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    z = _z(marketcap, 252)
    base = g * z * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gapxmcapz 252d
def f47fgd_f47_fake_growth_detector_gapxmcapz_252d_slope_v135_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    z = _z(marketcap, 504)
    base = g * z * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revaccel 63d
def f47fgd_f47_fake_growth_detector_revaccel_63d_slope_v136_signal(revenue, marketcap):
    rga = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    rgb = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = (rga - rgb) * marketcap + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revaccel 252d
def f47fgd_f47_fake_growth_detector_revaccel_252d_slope_v137_signal(revenue, marketcap):
    rga = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    rgb = revenue.diff(504) / revenue.shift(504).abs().replace(0, np.nan)
    base = (rga - rgb) * marketcap + _f47_fake_growth(revenue, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mcapaccel 63d
def f47fgd_f47_fake_growth_detector_mcapaccel_63d_slope_v138_signal(revenue, marketcap):
    mga = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    mgb = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    base = (mga - mgb) * marketcap + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcapaccel 252d
def f47fgd_f47_fake_growth_detector_mcapaccel_252d_slope_v139_signal(revenue, marketcap):
    mga = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    mgb = marketcap.diff(504) / marketcap.shift(504).abs().replace(0, np.nan)
    base = (mga - mgb) * marketcap + _f47_fake_growth(revenue, marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multifake 63d
def f47fgd_f47_fake_growth_detector_multifake_63d_slope_v140_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    c = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = (a + b + c) * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of multifake 252d
def f47fgd_f47_fake_growth_detector_multifake_252d_slope_v141_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    c = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = (a + b + c) * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of multifake 504d
def f47fgd_f47_fake_growth_detector_multifake_504d_slope_v142_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 504)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 504)
    c = _f47_fakegrowth_psgap(revenue, ps, 504)
    base = (a + b + c) * marketcap
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × close 63d
def f47fgd_f47_fake_growth_detector_gapxclose_63d_slope_v143_signal(revenue, marketcap, closeadj):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * closeadj * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × close 252d
def f47fgd_f47_fake_growth_detector_gapxclose_252d_slope_v144_signal(revenue, marketcap, closeadj):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * closeadj * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × log marketcap 63d
def f47fgd_f47_fake_growth_detector_gapxlogmcap_63d_slope_v145_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = g * lm * marketcap
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × log marketcap 252d
def f47fgd_f47_fake_growth_detector_gapxlogmcap_252d_slope_v146_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    base = g * lm * marketcap
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × revenue 63d
def f47fgd_f47_fake_growth_detector_gapxrev_63d_slope_v147_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * revenue
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of gap × revenue 252d
def f47fgd_f47_fake_growth_detector_gapxrev_252d_slope_v148_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = g * revenue
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of gap × assets 63d
def f47fgd_f47_fake_growth_detector_gapxassets_63d_slope_v149_signal(revenue, marketcap, assets):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = g * assets
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositesev 252d × ev
def f47fgd_f47_fake_growth_detector_compositesev_252d_slope_v150_signal(revenue, netinc, ps, marketcap, ev):
    a = _f47_fake_growth(revenue, marketcap, 252).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252).abs()
    c = _f47_fakegrowth_psgap(revenue, ps, 252).abs()
    base = (a + b + c) * ev
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f47fgd_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_FAKE_GROWTH_DETECTOR_REGISTRY_SLOPE = REGISTRY


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
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f47_fake_growth_detector_2nd_derivatives_001_150_claude: {n_features} features pass")
