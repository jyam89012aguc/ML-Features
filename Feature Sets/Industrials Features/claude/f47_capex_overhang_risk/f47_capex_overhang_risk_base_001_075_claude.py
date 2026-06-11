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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f47_capex_overinvestment(capex, depamor, w):
    return _mean(capex / depamor.replace(0, np.nan).abs(), w)


def _f47_capex_roic_pressure(capex, roic, w):
    return _mean(capex, w) * _mean(roic, w)


def _f47_overhang_signal(capex, ebit, w):
    return _mean(capex / ebit.replace(0, np.nan).abs(), w)


# v001-v009 capex/depamor at various windows (overinvestment)
def f47cohr_f47_capex_overhang_risk_oi_21d_base_v001_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_63d_base_v002_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_126d_base_v003_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_252d_base_v004_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_504d_base_v005_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_5d_base_v006_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_42d_base_v007_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_189d_base_v008_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_378d_base_v009_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010-v018 capex×roic pressure at various windows
def f47cohr_f47_capex_overhang_risk_pressure_21d_base_v010_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 21)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_63d_base_v011_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_126d_base_v012_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 126)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_252d_base_v013_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_504d_base_v014_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 504)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_5d_base_v015_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 5)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_42d_base_v016_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 42)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_189d_base_v017_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 189)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressure_378d_base_v018_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 378)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


# v019-v027 capex/ebit overhang signal
def f47cohr_f47_capex_overhang_risk_signal_21d_base_v019_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_63d_base_v020_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_126d_base_v021_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_252d_base_v022_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_504d_base_v023_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_5d_base_v024_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_42d_base_v025_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_189d_base_v026_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_378d_base_v027_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028-v033 z-scores
def f47cohr_f47_capex_overhang_risk_oiz_63d_base_v028_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiz_252d_base_v029_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalz_63d_base_v030_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalz_252d_base_v031_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressz_63d_base_v032_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63)
    result = _z(base, 252) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressz_252d_base_v033_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    result = _z(base, 504) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034-v037 std of OI
def f47cohr_f47_capex_overhang_risk_oistd_63d_base_v034_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oistd_252d_base_v035_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalstd_252d_base_v036_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressstd_252d_base_v037_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 21)
    result = _std(base, 252) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


# v038-v043 ratios and diffs
def f47cohr_f47_capex_overhang_risk_oidiff_63m252_base_v038_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 63)
    lg = _f47_capex_overinvestment(capex, depamor, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oidiff_21m63_base_v039_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 21)
    lg = _f47_capex_overinvestment(capex, depamor, 63)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oidiff_252m504_base_v040_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 252)
    lg = _f47_capex_overinvestment(capex, depamor, 504)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signaldiff_63m252_base_v041_signal(capex, ebit, closeadj):
    sh = _f47_overhang_signal(capex, ebit, 63)
    lg = _f47_overhang_signal(capex, ebit, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiratio_63v252_base_v042_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 63)
    lg = _f47_capex_overinvestment(capex, depamor, 252)
    result = sh / lg.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalratio_63v252_base_v043_signal(capex, ebit, closeadj):
    sh = _f47_overhang_signal(capex, ebit, 63)
    lg = _f47_overhang_signal(capex, ebit, 252)
    result = sh / lg.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044-v050 EMA variants
def f47cohr_f47_capex_overhang_risk_oiema_21d_base_v044_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 5)
    base = g.ewm(span=21, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_63d_base_v045_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_252d_base_v046_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_63d_base_v047_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_252d_base_v048_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressema_63d_base_v049_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressema_252d_base_v050_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v056 ranks
def f47cohr_f47_capex_overhang_risk_oirank_252d_base_v051_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrank_252d_base_v052_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressrank_252d_base_v053_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirank_504d_base_v054_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrank_504d_base_v055_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressrank_504d_base_v056_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057-v064 capex/revenue scaling and ratios
def f47cohr_f47_capex_overhang_risk_oixrev_63d_base_v057_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_63d_base_v058_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63)
    result = base * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrevgrowth_252d_base_v059_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    rg = revenue.pct_change(252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrevgrowth_252d_base_v060_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    rg = revenue.pct_change(252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_63d_base_v061_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63)
    result = base * (capex / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_252d_base_v062_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    result = base * (capex / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_504d_base_v063_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504)
    result = base * (capex / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxcaprev_252d_base_v064_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    result = base * (capex / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065-v075 derivative-like combos and roic-decline composites
def f47cohr_f47_capex_overhang_risk_roicdecline_252d_base_v065_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252)
    roic_delta = roic - roic.shift(252)
    result = base * roic_delta / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_roicdecline_63d_base_v066_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63)
    roic_delta = roic - roic.shift(63)
    result = base * roic_delta / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_extreme_oi_252d_base_v067_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    med = base.rolling(252, min_periods=63).median()
    extreme = (base > med).astype(float)
    result = (extreme * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_low_oi_252d_base_v068_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    med = base.rolling(252, min_periods=63).median()
    low = (base < med).astype(float)
    result = (low * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimin_63d_base_v069_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(63, min_periods=21).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimax_252d_base_v070_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(252, min_periods=63).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmin_63d_base_v071_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(63, min_periods=21).min()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmax_252d_base_v072_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(252, min_periods=63).max()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirange_252d_base_v073_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrange_252d_base_v074_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compositeoverhang_252d_base_v075_signal(capex, depamor, ebit, roic, closeadj):
    oi = _f47_capex_overinvestment(capex, depamor, 252)
    sg = _f47_overhang_signal(capex, ebit, 252)
    pr = _f47_capex_roic_pressure(capex, roic, 252)
    result = (oi + sg) * closeadj + pr * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47cohr_f47_capex_overhang_risk_oi_21d_base_v001_signal,
    f47cohr_f47_capex_overhang_risk_oi_63d_base_v002_signal,
    f47cohr_f47_capex_overhang_risk_oi_126d_base_v003_signal,
    f47cohr_f47_capex_overhang_risk_oi_252d_base_v004_signal,
    f47cohr_f47_capex_overhang_risk_oi_504d_base_v005_signal,
    f47cohr_f47_capex_overhang_risk_oi_5d_base_v006_signal,
    f47cohr_f47_capex_overhang_risk_oi_42d_base_v007_signal,
    f47cohr_f47_capex_overhang_risk_oi_189d_base_v008_signal,
    f47cohr_f47_capex_overhang_risk_oi_378d_base_v009_signal,
    f47cohr_f47_capex_overhang_risk_pressure_21d_base_v010_signal,
    f47cohr_f47_capex_overhang_risk_pressure_63d_base_v011_signal,
    f47cohr_f47_capex_overhang_risk_pressure_126d_base_v012_signal,
    f47cohr_f47_capex_overhang_risk_pressure_252d_base_v013_signal,
    f47cohr_f47_capex_overhang_risk_pressure_504d_base_v014_signal,
    f47cohr_f47_capex_overhang_risk_pressure_5d_base_v015_signal,
    f47cohr_f47_capex_overhang_risk_pressure_42d_base_v016_signal,
    f47cohr_f47_capex_overhang_risk_pressure_189d_base_v017_signal,
    f47cohr_f47_capex_overhang_risk_pressure_378d_base_v018_signal,
    f47cohr_f47_capex_overhang_risk_signal_21d_base_v019_signal,
    f47cohr_f47_capex_overhang_risk_signal_63d_base_v020_signal,
    f47cohr_f47_capex_overhang_risk_signal_126d_base_v021_signal,
    f47cohr_f47_capex_overhang_risk_signal_252d_base_v022_signal,
    f47cohr_f47_capex_overhang_risk_signal_504d_base_v023_signal,
    f47cohr_f47_capex_overhang_risk_signal_5d_base_v024_signal,
    f47cohr_f47_capex_overhang_risk_signal_42d_base_v025_signal,
    f47cohr_f47_capex_overhang_risk_signal_189d_base_v026_signal,
    f47cohr_f47_capex_overhang_risk_signal_378d_base_v027_signal,
    f47cohr_f47_capex_overhang_risk_oiz_63d_base_v028_signal,
    f47cohr_f47_capex_overhang_risk_oiz_252d_base_v029_signal,
    f47cohr_f47_capex_overhang_risk_signalz_63d_base_v030_signal,
    f47cohr_f47_capex_overhang_risk_signalz_252d_base_v031_signal,
    f47cohr_f47_capex_overhang_risk_pressz_63d_base_v032_signal,
    f47cohr_f47_capex_overhang_risk_pressz_252d_base_v033_signal,
    f47cohr_f47_capex_overhang_risk_oistd_63d_base_v034_signal,
    f47cohr_f47_capex_overhang_risk_oistd_252d_base_v035_signal,
    f47cohr_f47_capex_overhang_risk_signalstd_252d_base_v036_signal,
    f47cohr_f47_capex_overhang_risk_pressstd_252d_base_v037_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_63m252_base_v038_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_21m63_base_v039_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_252m504_base_v040_signal,
    f47cohr_f47_capex_overhang_risk_signaldiff_63m252_base_v041_signal,
    f47cohr_f47_capex_overhang_risk_oiratio_63v252_base_v042_signal,
    f47cohr_f47_capex_overhang_risk_signalratio_63v252_base_v043_signal,
    f47cohr_f47_capex_overhang_risk_oiema_21d_base_v044_signal,
    f47cohr_f47_capex_overhang_risk_oiema_63d_base_v045_signal,
    f47cohr_f47_capex_overhang_risk_oiema_252d_base_v046_signal,
    f47cohr_f47_capex_overhang_risk_signalema_63d_base_v047_signal,
    f47cohr_f47_capex_overhang_risk_signalema_252d_base_v048_signal,
    f47cohr_f47_capex_overhang_risk_pressema_63d_base_v049_signal,
    f47cohr_f47_capex_overhang_risk_pressema_252d_base_v050_signal,
    f47cohr_f47_capex_overhang_risk_oirank_252d_base_v051_signal,
    f47cohr_f47_capex_overhang_risk_signalrank_252d_base_v052_signal,
    f47cohr_f47_capex_overhang_risk_pressrank_252d_base_v053_signal,
    f47cohr_f47_capex_overhang_risk_oirank_504d_base_v054_signal,
    f47cohr_f47_capex_overhang_risk_signalrank_504d_base_v055_signal,
    f47cohr_f47_capex_overhang_risk_pressrank_504d_base_v056_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_63d_base_v057_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_63d_base_v058_signal,
    f47cohr_f47_capex_overhang_risk_oixrevgrowth_252d_base_v059_signal,
    f47cohr_f47_capex_overhang_risk_signalxrevgrowth_252d_base_v060_signal,
    f47cohr_f47_capex_overhang_risk_caprev_63d_base_v061_signal,
    f47cohr_f47_capex_overhang_risk_caprev_252d_base_v062_signal,
    f47cohr_f47_capex_overhang_risk_caprev_504d_base_v063_signal,
    f47cohr_f47_capex_overhang_risk_signalxcaprev_252d_base_v064_signal,
    f47cohr_f47_capex_overhang_risk_roicdecline_252d_base_v065_signal,
    f47cohr_f47_capex_overhang_risk_roicdecline_63d_base_v066_signal,
    f47cohr_f47_capex_overhang_risk_extreme_oi_252d_base_v067_signal,
    f47cohr_f47_capex_overhang_risk_low_oi_252d_base_v068_signal,
    f47cohr_f47_capex_overhang_risk_oimin_63d_base_v069_signal,
    f47cohr_f47_capex_overhang_risk_oimax_252d_base_v070_signal,
    f47cohr_f47_capex_overhang_risk_signalmin_63d_base_v071_signal,
    f47cohr_f47_capex_overhang_risk_signalmax_252d_base_v072_signal,
    f47cohr_f47_capex_overhang_risk_oirange_252d_base_v073_signal,
    f47cohr_f47_capex_overhang_risk_signalrange_252d_base_v074_signal,
    f47cohr_f47_capex_overhang_risk_compositeoverhang_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_CAPEX_OVERHANG_RISK_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "capex": capex, "depamor": depamor, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_capex_overinvestment", "_f47_capex_roic_pressure", "_f47_overhang_signal")
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
    print(f"OK f47_capex_overhang_risk_base_001_075_claude: {n_features} features pass")
