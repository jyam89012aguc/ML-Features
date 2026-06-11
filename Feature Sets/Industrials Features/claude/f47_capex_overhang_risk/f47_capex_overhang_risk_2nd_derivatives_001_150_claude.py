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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f47_capex_overinvestment(capex, depamor, w):
    return _mean(capex / depamor.replace(0, np.nan).abs(), w)


def _f47_capex_roic_pressure(capex, roic, w):
    return _mean(capex, w) * _mean(roic, w)


def _f47_overhang_signal(capex, ebit, w):
    return _mean(capex / ebit.replace(0, np.nan).abs(), w)


# Slope features (we mix windows for diversity)

def f47cohr_f47_capex_overhang_risk_oi_21d_slope_v001_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_21d_slope_v002_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_63d_slope_v003_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_126d_slope_v004_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_252d_slope_v005_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_504d_slope_v006_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_5d_slope_v007_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_42d_slope_v008_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_189d_slope_v009_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_378d_slope_v010_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_21d_slope_v011_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_63d_slope_v012_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_252d_slope_v013_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_504d_slope_v014_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_126d_slope_v015_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_5d_slope_v016_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_42d_slope_v017_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_189d_slope_v018_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_378d_slope_v019_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_63d_slope_v020_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_252d_slope_v021_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_504d_slope_v022_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 504) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_21d_slope_v023_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 21) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_126d_slope_v024_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 126) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_5d_slope_v025_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 5) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiz_63d_slope_v026_signal(capex, depamor, closeadj):
    base = _z(_f47_capex_overinvestment(capex, depamor, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiz_252d_slope_v027_signal(capex, depamor, closeadj):
    base = _z(_f47_capex_overinvestment(capex, depamor, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalz_63d_slope_v028_signal(capex, ebit, closeadj):
    base = _z(_f47_overhang_signal(capex, ebit, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalz_252d_slope_v029_signal(capex, ebit, closeadj):
    base = _z(_f47_overhang_signal(capex, ebit, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oistd_252d_slope_v030_signal(capex, depamor, closeadj):
    base = _std(_f47_capex_overinvestment(capex, depamor, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalstd_252d_slope_v031_signal(capex, ebit, closeadj):
    base = _std(_f47_overhang_signal(capex, ebit, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oistd_63d_slope_v032_signal(capex, depamor, closeadj):
    base = _std(_f47_capex_overinvestment(capex, depamor, 5), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oidiff_63m252_slope_v033_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 63)
    lg = _f47_capex_overinvestment(capex, depamor, 252)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oidiff_21m63_slope_v034_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 21)
    lg = _f47_capex_overinvestment(capex, depamor, 63)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oidiff_252m504_slope_v035_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 252)
    lg = _f47_capex_overinvestment(capex, depamor, 504)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signaldiff_63m252_slope_v036_signal(capex, ebit, closeadj):
    sh = _f47_overhang_signal(capex, ebit, 63)
    lg = _f47_overhang_signal(capex, ebit, 252)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signaldiff_21m63_slope_v037_signal(capex, ebit, closeadj):
    sh = _f47_overhang_signal(capex, ebit, 21)
    lg = _f47_overhang_signal(capex, ebit, 63)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiratio_63v252_slope_v038_signal(capex, depamor, closeadj):
    sh = _f47_capex_overinvestment(capex, depamor, 63)
    lg = _f47_capex_overinvestment(capex, depamor, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalratio_63v252_slope_v039_signal(capex, ebit, closeadj):
    sh = _f47_overhang_signal(capex, ebit, 63)
    lg = _f47_overhang_signal(capex, ebit, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_63d_slope_v040_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_252d_slope_v041_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_63d_slope_v042_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_252d_slope_v043_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirank_252d_slope_v044_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrank_252d_slope_v045_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrevgrowth_252d_slope_v046_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrevgrowth_252d_slope_v047_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroic_252d_slope_v048_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * _z(roic, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxroic_252d_slope_v049_signal(capex, ebit, roic, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * _z(roic, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_252d_slope_v050_signal(capex, depamor, ebit, closeadj):
    base = (_f47_capex_overinvestment(capex, depamor, 252) * _f47_overhang_signal(capex, ebit, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_63d_slope_v051_signal(capex, depamor, ebit, closeadj):
    base = (_f47_capex_overinvestment(capex, depamor, 63) * _f47_overhang_signal(capex, ebit, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_504d_slope_v052_signal(capex, depamor, ebit, closeadj):
    base = (_f47_capex_overinvestment(capex, depamor, 504) * _f47_overhang_signal(capex, ebit, 504)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrev_63d_slope_v053_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_63d_slope_v054_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_volz_63d_slope_v055_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_volz_63d_slope_v056_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_dv_63d_slope_v057_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * _mean(closeadj * volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_dv_252d_slope_v058_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * _mean(closeadj * volume, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimin_63d_slope_v059_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimax_252d_slope_v060_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmin_63d_slope_v061_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmax_252d_slope_v062_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirange_252d_slope_v063_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrange_252d_slope_v064_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiskew_252d_slope_v065_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalskew_252d_slope_v066_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oikurt_252d_slope_v067_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalkurt_252d_slope_v068_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_sqoi_252d_slope_v069_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    base = g * g.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_sqsignal_252d_slope_v070_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    base = g * g.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oilog_252d_slope_v071_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signallog_252d_slope_v072_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oilagdiff_252d_slope_v073_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    base = (g - g.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signallagdiff_252d_slope_v074_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    base = (g - g.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oievent_hi_252d_slope_v075_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalevent_hi_252d_slope_v076_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimedsplit_252d_slope_v077_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmedsplit_252d_slope_v078_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiminus1_252d_slope_v079_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    base = (g - 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalminus1_252d_slope_v080_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    base = (g - 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compositesev_252d_slope_v081_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    rd = roic - roic.shift(252)
    base = ((a + b) * (1.0 - rd)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compositesev_504d_slope_v082_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 504)
    b = _f47_overhang_signal(capex, ebit, 504)
    rd = roic - roic.shift(252)
    base = ((a + b) * (1.0 - rd)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroicdelta_252d_slope_v083_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * (roic - roic.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxroicdelta_252d_slope_v084_signal(capex, ebit, roic, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * (roic - roic.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_5d_slope_v085_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_5d_slope_v086_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_5d_slope_v087_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 5) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_42d_slope_v088_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_42d_slope_v089_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_378d_slope_v090_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_378d_slope_v091_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_378d_slope_v092_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 378) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebit_63d_slope_v093_signal(capex, depamor, ebit, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * np.log(ebit.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxcap_63d_slope_v094_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixlogcap_252d_slope_v095_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxdep_252d_slope_v096_signal(capex, ebit, depamor, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * np.log(depamor.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oicapexshare_252d_slope_v097_signal(capex, depamor, ebitda, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * (capex / ebitda.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalcapexshare_252d_slope_v098_signal(capex, ebit, ebitda, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * (capex / ebitda.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oitrend_252d_slope_v099_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signaltrend_252d_slope_v100_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_63d_slope_v101_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * (capex / revenue.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_252d_slope_v102_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * (capex / revenue.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_caprev_504d_slope_v103_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504) * (capex / revenue.replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrev_252d_slope_v104_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * (revenue / capex.replace(0, np.nan).abs()) * closeadj * 1e-4
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_252d_slope_v105_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * (revenue / capex.replace(0, np.nan).abs()) * closeadj * 1e-4
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixroicrange_252d_slope_v106_signal(capex, depamor, roic, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * (roic.rolling(252, min_periods=63).max() - roic.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxroicrange_252d_slope_v107_signal(capex, ebit, roic, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * (roic.rolling(252, min_periods=63).max() - roic.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_21d_slope_v108_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_21d_slope_v109_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressema_252d_slope_v110_signal(capex, roic, closeadj):
    g = _f47_capex_roic_pressure(capex, roic, 21)
    base = g.ewm(span=252, adjust=False).mean() / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirank_504d_slope_v111_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrank_504d_slope_v112_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compxroic_252d_slope_v113_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    base = (a + b) * _z(roic, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compxneg_252d_slope_v114_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    rd = roic - roic.shift(252)
    med = rd.rolling(504, min_periods=126).median()
    mod = (rd < med).astype(float)
    base = ((a + b) * mod + (a + b) * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixneg_63d_slope_v115_signal(capex, depamor, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 63)
    rd = roic - roic.shift(63)
    med = rd.rolling(252, min_periods=63).median()
    mod = (rd < med).astype(float)
    base = (a * mod + a * 0.5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxneg_252d_slope_v116_signal(capex, ebit, roic, closeadj):
    b = _f47_overhang_signal(capex, ebit, 252)
    rd = roic - roic.shift(252)
    med = rd.rolling(504, min_periods=126).median()
    mod = (rd < med).astype(float)
    base = (b * mod + b * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixrev_63d_slope_v117_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * revenue.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxrev_63d_slope_v118_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * revenue.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebitgrowth_63d_slope_v119_signal(capex, depamor, ebit, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * ebit.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxebitgrowth_252d_slope_v120_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252) * ebit.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixvolc_21d_slope_v121_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 21) * closeadj * np.log(volume.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxvolc_21d_slope_v122_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 21) * closeadj * np.log(volume.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixdvnorm_63d_slope_v123_signal(capex, depamor, volume, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 63) * _z(closeadj * volume, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalxdvnorm_63d_slope_v124_signal(capex, ebit, volume, closeadj):
    base = _f47_overhang_signal(capex, ebit, 63) * _z(closeadj * volume, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oiema_short_slope_v125_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 21)
    base = g.ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalema_short_slope_v126_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 21)
    base = g.ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_5d_slopediff_v127_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_5d_slopediff_v128_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_42d_slopediff_v129_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_42d_slopediff_v130_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_42d_slope_v131_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 42) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_press_189d_slope_v132_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 189) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignalxroic_252d_slope_v133_signal(capex, depamor, ebit, roic, closeadj):
    base = (_f47_capex_overinvestment(capex, depamor, 252) + _f47_overhang_signal(capex, ebit, 252)) * roic * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixsignal_lograw_252d_slope_v134_signal(capex, depamor, ebit, closeadj):
    base = (_f47_capex_overinvestment(capex, depamor, 252) + _f47_overhang_signal(capex, ebit, 252)) * np.log(capex.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirevgrowth_504d_slope_v135_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 504) * revenue.pct_change(252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrevgrowth_504d_slope_v136_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 504) * revenue.pct_change(252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_presstrend_252d_slope_v137_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 21)
    trend = base.rolling(252, min_periods=63).mean() - base.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixebitgrowth_252d_slope_v138_signal(capex, depamor, ebit, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252) * ebit.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oirev_ratio_252d_slope_v139_signal(capex, depamor, revenue, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 252)
    cr = capex / revenue.replace(0, np.nan).abs()
    base2 = (base + cr * 10.0) * closeadj
    result = _slope_pct(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalrev_ratio_252d_slope_v140_signal(capex, ebit, revenue, closeadj):
    base = _f47_overhang_signal(capex, ebit, 252)
    cr = capex / revenue.replace(0, np.nan).abs()
    base2 = (base + cr * 10.0) * closeadj
    result = _slope_pct(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oimedsplit_504d_slope_v141_signal(capex, depamor, closeadj):
    g = _f47_capex_overinvestment(capex, depamor, 504)
    med = g.rolling(504, min_periods=126).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signalmedsplit_504d_slope_v142_signal(capex, ebit, closeadj):
    g = _f47_overhang_signal(capex, ebit, 504)
    med = g.rolling(504, min_periods=126).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_capxroic_63d_slope_v143_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 63) * roic / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_capxroic_252d_slope_v144_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252) * roic / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_pressxlogprice_252d_slope_v145_signal(capex, roic, closeadj):
    base = _f47_capex_roic_pressure(capex, roic, 252) * np.log(closeadj.abs().replace(0, np.nan)) / closeadj.abs().replace(0, np.nan) * closeadj * 1e-8
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixlong_pct_252d_slope_v146_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    base = ((a + b) * (1.0 - roic)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oixlong_pct_504d_slope_v147_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 504)
    b = _f47_overhang_signal(capex, ebit, 504)
    base = ((a + b) * (1.0 - roic)) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_oi_swap_42d_slope_v148_signal(capex, depamor, closeadj):
    base = _f47_capex_overinvestment(capex, depamor, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_signal_swap_42d_slope_v149_signal(capex, ebit, closeadj):
    base = _f47_overhang_signal(capex, ebit, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47cohr_f47_capex_overhang_risk_compositesev_alt_252d_slope_v150_signal(capex, depamor, ebit, roic, closeadj):
    a = _f47_capex_overinvestment(capex, depamor, 252)
    b = _f47_overhang_signal(capex, ebit, 252)
    base = (a * b * (1.0 - roic)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47cohr_f47_capex_overhang_risk_oi_21d_slope_v001_signal,
    f47cohr_f47_capex_overhang_risk_oi_21d_slope_v002_signal,
    f47cohr_f47_capex_overhang_risk_oi_63d_slope_v003_signal,
    f47cohr_f47_capex_overhang_risk_oi_126d_slope_v004_signal,
    f47cohr_f47_capex_overhang_risk_oi_252d_slope_v005_signal,
    f47cohr_f47_capex_overhang_risk_oi_504d_slope_v006_signal,
    f47cohr_f47_capex_overhang_risk_oi_5d_slope_v007_signal,
    f47cohr_f47_capex_overhang_risk_oi_42d_slope_v008_signal,
    f47cohr_f47_capex_overhang_risk_oi_189d_slope_v009_signal,
    f47cohr_f47_capex_overhang_risk_oi_378d_slope_v010_signal,
    f47cohr_f47_capex_overhang_risk_signal_21d_slope_v011_signal,
    f47cohr_f47_capex_overhang_risk_signal_63d_slope_v012_signal,
    f47cohr_f47_capex_overhang_risk_signal_252d_slope_v013_signal,
    f47cohr_f47_capex_overhang_risk_signal_504d_slope_v014_signal,
    f47cohr_f47_capex_overhang_risk_signal_126d_slope_v015_signal,
    f47cohr_f47_capex_overhang_risk_signal_5d_slope_v016_signal,
    f47cohr_f47_capex_overhang_risk_signal_42d_slope_v017_signal,
    f47cohr_f47_capex_overhang_risk_signal_189d_slope_v018_signal,
    f47cohr_f47_capex_overhang_risk_signal_378d_slope_v019_signal,
    f47cohr_f47_capex_overhang_risk_press_63d_slope_v020_signal,
    f47cohr_f47_capex_overhang_risk_press_252d_slope_v021_signal,
    f47cohr_f47_capex_overhang_risk_press_504d_slope_v022_signal,
    f47cohr_f47_capex_overhang_risk_press_21d_slope_v023_signal,
    f47cohr_f47_capex_overhang_risk_press_126d_slope_v024_signal,
    f47cohr_f47_capex_overhang_risk_press_5d_slope_v025_signal,
    f47cohr_f47_capex_overhang_risk_oiz_63d_slope_v026_signal,
    f47cohr_f47_capex_overhang_risk_oiz_252d_slope_v027_signal,
    f47cohr_f47_capex_overhang_risk_signalz_63d_slope_v028_signal,
    f47cohr_f47_capex_overhang_risk_signalz_252d_slope_v029_signal,
    f47cohr_f47_capex_overhang_risk_oistd_252d_slope_v030_signal,
    f47cohr_f47_capex_overhang_risk_signalstd_252d_slope_v031_signal,
    f47cohr_f47_capex_overhang_risk_oistd_63d_slope_v032_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_63m252_slope_v033_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_21m63_slope_v034_signal,
    f47cohr_f47_capex_overhang_risk_oidiff_252m504_slope_v035_signal,
    f47cohr_f47_capex_overhang_risk_signaldiff_63m252_slope_v036_signal,
    f47cohr_f47_capex_overhang_risk_signaldiff_21m63_slope_v037_signal,
    f47cohr_f47_capex_overhang_risk_oiratio_63v252_slope_v038_signal,
    f47cohr_f47_capex_overhang_risk_signalratio_63v252_slope_v039_signal,
    f47cohr_f47_capex_overhang_risk_oiema_63d_slope_v040_signal,
    f47cohr_f47_capex_overhang_risk_oiema_252d_slope_v041_signal,
    f47cohr_f47_capex_overhang_risk_signalema_63d_slope_v042_signal,
    f47cohr_f47_capex_overhang_risk_signalema_252d_slope_v043_signal,
    f47cohr_f47_capex_overhang_risk_oirank_252d_slope_v044_signal,
    f47cohr_f47_capex_overhang_risk_signalrank_252d_slope_v045_signal,
    f47cohr_f47_capex_overhang_risk_oixrevgrowth_252d_slope_v046_signal,
    f47cohr_f47_capex_overhang_risk_signalxrevgrowth_252d_slope_v047_signal,
    f47cohr_f47_capex_overhang_risk_oixroic_252d_slope_v048_signal,
    f47cohr_f47_capex_overhang_risk_signalxroic_252d_slope_v049_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_252d_slope_v050_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_63d_slope_v051_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_504d_slope_v052_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_63d_slope_v053_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_63d_slope_v054_signal,
    f47cohr_f47_capex_overhang_risk_oi_volz_63d_slope_v055_signal,
    f47cohr_f47_capex_overhang_risk_signal_volz_63d_slope_v056_signal,
    f47cohr_f47_capex_overhang_risk_oi_dv_63d_slope_v057_signal,
    f47cohr_f47_capex_overhang_risk_signal_dv_252d_slope_v058_signal,
    f47cohr_f47_capex_overhang_risk_oimin_63d_slope_v059_signal,
    f47cohr_f47_capex_overhang_risk_oimax_252d_slope_v060_signal,
    f47cohr_f47_capex_overhang_risk_signalmin_63d_slope_v061_signal,
    f47cohr_f47_capex_overhang_risk_signalmax_252d_slope_v062_signal,
    f47cohr_f47_capex_overhang_risk_oirange_252d_slope_v063_signal,
    f47cohr_f47_capex_overhang_risk_signalrange_252d_slope_v064_signal,
    f47cohr_f47_capex_overhang_risk_oiskew_252d_slope_v065_signal,
    f47cohr_f47_capex_overhang_risk_signalskew_252d_slope_v066_signal,
    f47cohr_f47_capex_overhang_risk_oikurt_252d_slope_v067_signal,
    f47cohr_f47_capex_overhang_risk_signalkurt_252d_slope_v068_signal,
    f47cohr_f47_capex_overhang_risk_sqoi_252d_slope_v069_signal,
    f47cohr_f47_capex_overhang_risk_sqsignal_252d_slope_v070_signal,
    f47cohr_f47_capex_overhang_risk_oilog_252d_slope_v071_signal,
    f47cohr_f47_capex_overhang_risk_signallog_252d_slope_v072_signal,
    f47cohr_f47_capex_overhang_risk_oilagdiff_252d_slope_v073_signal,
    f47cohr_f47_capex_overhang_risk_signallagdiff_252d_slope_v074_signal,
    f47cohr_f47_capex_overhang_risk_oievent_hi_252d_slope_v075_signal,
    f47cohr_f47_capex_overhang_risk_signalevent_hi_252d_slope_v076_signal,
    f47cohr_f47_capex_overhang_risk_oimedsplit_252d_slope_v077_signal,
    f47cohr_f47_capex_overhang_risk_signalmedsplit_252d_slope_v078_signal,
    f47cohr_f47_capex_overhang_risk_oiminus1_252d_slope_v079_signal,
    f47cohr_f47_capex_overhang_risk_signalminus1_252d_slope_v080_signal,
    f47cohr_f47_capex_overhang_risk_compositesev_252d_slope_v081_signal,
    f47cohr_f47_capex_overhang_risk_compositesev_504d_slope_v082_signal,
    f47cohr_f47_capex_overhang_risk_oixroicdelta_252d_slope_v083_signal,
    f47cohr_f47_capex_overhang_risk_signalxroicdelta_252d_slope_v084_signal,
    f47cohr_f47_capex_overhang_risk_oi_5d_slope_v085_signal,
    f47cohr_f47_capex_overhang_risk_signal_5d_slope_v086_signal,
    f47cohr_f47_capex_overhang_risk_press_5d_slope_v087_signal,
    f47cohr_f47_capex_overhang_risk_oi_42d_slope_v088_signal,
    f47cohr_f47_capex_overhang_risk_signal_42d_slope_v089_signal,
    f47cohr_f47_capex_overhang_risk_oi_378d_slope_v090_signal,
    f47cohr_f47_capex_overhang_risk_signal_378d_slope_v091_signal,
    f47cohr_f47_capex_overhang_risk_press_378d_slope_v092_signal,
    f47cohr_f47_capex_overhang_risk_oixebit_63d_slope_v093_signal,
    f47cohr_f47_capex_overhang_risk_signalxcap_63d_slope_v094_signal,
    f47cohr_f47_capex_overhang_risk_oixlogcap_252d_slope_v095_signal,
    f47cohr_f47_capex_overhang_risk_signalxdep_252d_slope_v096_signal,
    f47cohr_f47_capex_overhang_risk_oicapexshare_252d_slope_v097_signal,
    f47cohr_f47_capex_overhang_risk_signalcapexshare_252d_slope_v098_signal,
    f47cohr_f47_capex_overhang_risk_oitrend_252d_slope_v099_signal,
    f47cohr_f47_capex_overhang_risk_signaltrend_252d_slope_v100_signal,
    f47cohr_f47_capex_overhang_risk_caprev_63d_slope_v101_signal,
    f47cohr_f47_capex_overhang_risk_caprev_252d_slope_v102_signal,
    f47cohr_f47_capex_overhang_risk_caprev_504d_slope_v103_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_252d_slope_v104_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_252d_slope_v105_signal,
    f47cohr_f47_capex_overhang_risk_oixroicrange_252d_slope_v106_signal,
    f47cohr_f47_capex_overhang_risk_signalxroicrange_252d_slope_v107_signal,
    f47cohr_f47_capex_overhang_risk_oiema_21d_slope_v108_signal,
    f47cohr_f47_capex_overhang_risk_signalema_21d_slope_v109_signal,
    f47cohr_f47_capex_overhang_risk_pressema_252d_slope_v110_signal,
    f47cohr_f47_capex_overhang_risk_oirank_504d_slope_v111_signal,
    f47cohr_f47_capex_overhang_risk_signalrank_504d_slope_v112_signal,
    f47cohr_f47_capex_overhang_risk_compxroic_252d_slope_v113_signal,
    f47cohr_f47_capex_overhang_risk_compxneg_252d_slope_v114_signal,
    f47cohr_f47_capex_overhang_risk_oixneg_63d_slope_v115_signal,
    f47cohr_f47_capex_overhang_risk_signalxneg_252d_slope_v116_signal,
    f47cohr_f47_capex_overhang_risk_oixrev_63d_slope_v117_signal,
    f47cohr_f47_capex_overhang_risk_signalxrev_63d_slope_v118_signal,
    f47cohr_f47_capex_overhang_risk_oixebitgrowth_63d_slope_v119_signal,
    f47cohr_f47_capex_overhang_risk_signalxebitgrowth_252d_slope_v120_signal,
    f47cohr_f47_capex_overhang_risk_oixvolc_21d_slope_v121_signal,
    f47cohr_f47_capex_overhang_risk_signalxvolc_21d_slope_v122_signal,
    f47cohr_f47_capex_overhang_risk_oixdvnorm_63d_slope_v123_signal,
    f47cohr_f47_capex_overhang_risk_signalxdvnorm_63d_slope_v124_signal,
    f47cohr_f47_capex_overhang_risk_oiema_short_slope_v125_signal,
    f47cohr_f47_capex_overhang_risk_signalema_short_slope_v126_signal,
    f47cohr_f47_capex_overhang_risk_oi_5d_slopediff_v127_signal,
    f47cohr_f47_capex_overhang_risk_signal_5d_slopediff_v128_signal,
    f47cohr_f47_capex_overhang_risk_oi_42d_slopediff_v129_signal,
    f47cohr_f47_capex_overhang_risk_signal_42d_slopediff_v130_signal,
    f47cohr_f47_capex_overhang_risk_press_42d_slope_v131_signal,
    f47cohr_f47_capex_overhang_risk_press_189d_slope_v132_signal,
    f47cohr_f47_capex_overhang_risk_oixsignalxroic_252d_slope_v133_signal,
    f47cohr_f47_capex_overhang_risk_oixsignal_lograw_252d_slope_v134_signal,
    f47cohr_f47_capex_overhang_risk_oirevgrowth_504d_slope_v135_signal,
    f47cohr_f47_capex_overhang_risk_signalrevgrowth_504d_slope_v136_signal,
    f47cohr_f47_capex_overhang_risk_presstrend_252d_slope_v137_signal,
    f47cohr_f47_capex_overhang_risk_oixebitgrowth_252d_slope_v138_signal,
    f47cohr_f47_capex_overhang_risk_oirev_ratio_252d_slope_v139_signal,
    f47cohr_f47_capex_overhang_risk_signalrev_ratio_252d_slope_v140_signal,
    f47cohr_f47_capex_overhang_risk_oimedsplit_504d_slope_v141_signal,
    f47cohr_f47_capex_overhang_risk_signalmedsplit_504d_slope_v142_signal,
    f47cohr_f47_capex_overhang_risk_capxroic_63d_slope_v143_signal,
    f47cohr_f47_capex_overhang_risk_capxroic_252d_slope_v144_signal,
    f47cohr_f47_capex_overhang_risk_pressxlogprice_252d_slope_v145_signal,
    f47cohr_f47_capex_overhang_risk_oixlong_pct_252d_slope_v146_signal,
    f47cohr_f47_capex_overhang_risk_oixlong_pct_504d_slope_v147_signal,
    f47cohr_f47_capex_overhang_risk_oi_swap_42d_slope_v148_signal,
    f47cohr_f47_capex_overhang_risk_signal_swap_42d_slope_v149_signal,
    f47cohr_f47_capex_overhang_risk_compositesev_alt_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_CAPEX_OVERHANG_RISK_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f47_capex_overhang_risk_2nd_derivatives_001_150_claude: {n_features} features pass")
