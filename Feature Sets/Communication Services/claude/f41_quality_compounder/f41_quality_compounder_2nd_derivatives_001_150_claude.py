import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (quality compounder) =====
def _f41_growth(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f41_dilution(sharesbas, w):
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f41_pos_frac(s, w):
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_stab(s, w):
    return _mean(s, w) / _std(s, w).replace(0, np.nan)


def _f41_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)



# slope d/dt[roicfcf] 15d plain
def f41qc_f41_quality_compounder_roicfcf_15d_slope_v001_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(15)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 63d z
def f41qc_f41_quality_compounder_roicfcf_63d_slope_v002_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(63)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 168d norm
def f41qc_f41_quality_compounder_roicfcf_168d_slope_v003_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(168)
    result = d / _std(base, 168).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 294d tanh
def f41qc_f41_quality_compounder_roicfcf_294d_slope_v004_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(294)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 42d tanh
def f41qc_f41_quality_compounder_roicfcf_42d_slope_v005_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(42)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 126d rank
def f41qc_f41_quality_compounder_roicfcf_126d_slope_v006_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(126)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 231d rank
def f41qc_f41_quality_compounder_roicfcf_231d_slope_v007_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(231)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 21d tanh
def f41qc_f41_quality_compounder_qmd_21d_slope_v008_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(21)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 84d tanh
def f41qc_f41_quality_compounder_qmd_84d_slope_v009_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(84)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 189d rank
def f41qc_f41_quality_compounder_qmd_189d_slope_v010_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(189)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 315d rank
def f41qc_f41_quality_compounder_qmd_315d_slope_v011_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(315)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 52d plain
def f41qc_f41_quality_compounder_qmd_52d_slope_v012_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(52)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 147d z
def f41qc_f41_quality_compounder_qmd_147d_slope_v013_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(147)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 252d norm
def f41qc_f41_quality_compounder_qmd_252d_slope_v014_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(252)
    result = d / _std(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 31d rank
def f41qc_f41_quality_compounder_roicpersist_31d_slope_v015_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(31)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 105d plain
def f41qc_f41_quality_compounder_roicpersist_105d_slope_v016_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 210d z
def f41qc_f41_quality_compounder_roicpersist_210d_slope_v017_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(210)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 15d norm
def f41qc_f41_quality_compounder_roicpersist_15d_slope_v018_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(15)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 63d tanh
def f41qc_f41_quality_compounder_roicpersist_63d_slope_v019_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(63)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 168d tanh
def f41qc_f41_quality_compounder_roicpersist_168d_slope_v020_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(168)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 294d rank
def f41qc_f41_quality_compounder_roicpersist_294d_slope_v021_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(294)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 42d norm
def f41qc_f41_quality_compounder_fcfgrow_42d_slope_v022_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(42)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 126d tanh
def f41qc_f41_quality_compounder_fcfgrow_126d_slope_v023_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(126)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 231d tanh
def f41qc_f41_quality_compounder_fcfgrow_231d_slope_v024_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(231)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 21d rank
def f41qc_f41_quality_compounder_fcfgrow_21d_slope_v025_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(21)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 84d rank
def f41qc_f41_quality_compounder_fcfgrow_84d_slope_v026_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(84)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 189d plain
def f41qc_f41_quality_compounder_fcfgrow_189d_slope_v027_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 315d z
def f41qc_f41_quality_compounder_fcfgrow_315d_slope_v028_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(315)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 52d rank
def f41qc_f41_quality_compounder_roicmargin_52d_slope_v029_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(52)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 147d rank
def f41qc_f41_quality_compounder_roicmargin_147d_slope_v030_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(147)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 252d plain
def f41qc_f41_quality_compounder_roicmargin_252d_slope_v031_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 31d z
def f41qc_f41_quality_compounder_roicmargin_31d_slope_v032_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(31)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 105d norm
def f41qc_f41_quality_compounder_roicmargin_105d_slope_v033_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(105)
    result = d / _std(base, 105).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 210d tanh
def f41qc_f41_quality_compounder_roicmargin_210d_slope_v034_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(210)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 15d tanh
def f41qc_f41_quality_compounder_roicmargin_15d_slope_v035_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(15)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 63d z
def f41qc_f41_quality_compounder_revgrow_63d_slope_v036_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(63)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 168d norm
def f41qc_f41_quality_compounder_revgrow_168d_slope_v037_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(168)
    result = d / _std(base, 168).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 294d tanh
def f41qc_f41_quality_compounder_revgrow_294d_slope_v038_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(294)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 42d tanh
def f41qc_f41_quality_compounder_revgrow_42d_slope_v039_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(42)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 126d rank
def f41qc_f41_quality_compounder_revgrow_126d_slope_v040_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(126)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 231d rank
def f41qc_f41_quality_compounder_revgrow_231d_slope_v041_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(231)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 21d plain
def f41qc_f41_quality_compounder_revgrow_21d_slope_v042_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 84d tanh
def f41qc_f41_quality_compounder_equitygrow_84d_slope_v043_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(84)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 189d rank
def f41qc_f41_quality_compounder_equitygrow_189d_slope_v044_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(189)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 315d rank
def f41qc_f41_quality_compounder_equitygrow_315d_slope_v045_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(315)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 52d plain
def f41qc_f41_quality_compounder_equitygrow_52d_slope_v046_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(52)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 147d z
def f41qc_f41_quality_compounder_equitygrow_147d_slope_v047_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(147)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 252d norm
def f41qc_f41_quality_compounder_equitygrow_252d_slope_v048_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(252)
    result = d / _std(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 31d tanh
def f41qc_f41_quality_compounder_equitygrow_31d_slope_v049_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(31)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 105d plain
def f41qc_f41_quality_compounder_persharegrow_105d_slope_v050_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(105)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 210d z
def f41qc_f41_quality_compounder_persharegrow_210d_slope_v051_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(210)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 15d norm
def f41qc_f41_quality_compounder_persharegrow_15d_slope_v052_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(15)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 63d tanh
def f41qc_f41_quality_compounder_persharegrow_63d_slope_v053_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(63)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 168d tanh
def f41qc_f41_quality_compounder_persharegrow_168d_slope_v054_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(168)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 294d rank
def f41qc_f41_quality_compounder_persharegrow_294d_slope_v055_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(294)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 42d rank
def f41qc_f41_quality_compounder_persharegrow_42d_slope_v056_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(42)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 126d tanh
def f41qc_f41_quality_compounder_twinprofit_126d_slope_v057_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(126)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 231d tanh
def f41qc_f41_quality_compounder_twinprofit_231d_slope_v058_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(231)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 21d rank
def f41qc_f41_quality_compounder_twinprofit_21d_slope_v059_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(21)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 84d rank
def f41qc_f41_quality_compounder_twinprofit_84d_slope_v060_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(84)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 189d plain
def f41qc_f41_quality_compounder_twinprofit_189d_slope_v061_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 315d z
def f41qc_f41_quality_compounder_twinprofit_315d_slope_v062_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(315)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 52d norm
def f41qc_f41_quality_compounder_twinprofit_52d_slope_v063_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(52)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 147d rank
def f41qc_f41_quality_compounder_zblend_147d_slope_v064_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(147)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 252d plain
def f41qc_f41_quality_compounder_zblend_252d_slope_v065_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 31d z
def f41qc_f41_quality_compounder_zblend_31d_slope_v066_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(31)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 105d norm
def f41qc_f41_quality_compounder_zblend_105d_slope_v067_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(105)
    result = d / _std(base, 105).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 210d tanh
def f41qc_f41_quality_compounder_zblend_210d_slope_v068_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(210)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 15d tanh
def f41qc_f41_quality_compounder_zblend_15d_slope_v069_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(15)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 63d rank
def f41qc_f41_quality_compounder_zblend_63d_slope_v070_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(63)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 168d norm
def f41qc_f41_quality_compounder_cashqmd_168d_slope_v071_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(168)
    result = d / _std(base, 168).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 294d tanh
def f41qc_f41_quality_compounder_cashqmd_294d_slope_v072_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(294)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 42d tanh
def f41qc_f41_quality_compounder_cashqmd_42d_slope_v073_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(42)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 126d rank
def f41qc_f41_quality_compounder_cashqmd_126d_slope_v074_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(126)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 231d rank
def f41qc_f41_quality_compounder_cashqmd_231d_slope_v075_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(231)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 21d plain
def f41qc_f41_quality_compounder_cashqmd_21d_slope_v076_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[cashqmd] 84d z
def f41qc_f41_quality_compounder_cashqmd_84d_slope_v077_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    base = _rank(cashret, 252) - _rank(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(84)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 189d rank
def f41qc_f41_quality_compounder_durindex_189d_slope_v078_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(189)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 315d rank
def f41qc_f41_quality_compounder_durindex_315d_slope_v079_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(315)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 52d plain
def f41qc_f41_quality_compounder_durindex_52d_slope_v080_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(52)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 147d z
def f41qc_f41_quality_compounder_durindex_147d_slope_v081_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(147)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 252d norm
def f41qc_f41_quality_compounder_durindex_252d_slope_v082_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(252)
    result = d / _std(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 31d tanh
def f41qc_f41_quality_compounder_durindex_31d_slope_v083_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(31)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[durindex] 105d tanh
def f41qc_f41_quality_compounder_durindex_105d_slope_v084_signal(roic, netmargin, fcf, equity):
    cashret = _safe_div(fcf, equity)
    base = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0
    d = base - base.shift(105)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 210d z
def f41qc_f41_quality_compounder_bvps_210d_slope_v085_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(210)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 15d norm
def f41qc_f41_quality_compounder_bvps_15d_slope_v086_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(15)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 63d tanh
def f41qc_f41_quality_compounder_bvps_63d_slope_v087_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(63)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 168d tanh
def f41qc_f41_quality_compounder_bvps_168d_slope_v088_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(168)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 294d rank
def f41qc_f41_quality_compounder_bvps_294d_slope_v089_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(294)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 42d rank
def f41qc_f41_quality_compounder_bvps_42d_slope_v090_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(42)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[bvps] 126d plain
def f41qc_f41_quality_compounder_bvps_126d_slope_v091_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    base = _z(bvps, 252)
    d = base - base.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 231d tanh
def f41qc_f41_quality_compounder_accrualgap_231d_slope_v092_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(231)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 21d rank
def f41qc_f41_quality_compounder_accrualgap_21d_slope_v093_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(21)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 84d rank
def f41qc_f41_quality_compounder_accrualgap_84d_slope_v094_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(84)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 189d plain
def f41qc_f41_quality_compounder_accrualgap_189d_slope_v095_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 315d z
def f41qc_f41_quality_compounder_accrualgap_315d_slope_v096_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(315)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 52d norm
def f41qc_f41_quality_compounder_accrualgap_52d_slope_v097_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(52)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[accrualgap] 147d tanh
def f41qc_f41_quality_compounder_accrualgap_147d_slope_v098_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 126) - _mean(netmargin, 126)
    d = base - base.shift(147)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 252d plain
def f41qc_f41_quality_compounder_turn_252d_slope_v099_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 31d z
def f41qc_f41_quality_compounder_turn_31d_slope_v100_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(31)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 105d norm
def f41qc_f41_quality_compounder_turn_105d_slope_v101_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(105)
    result = d / _std(base, 105).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 210d tanh
def f41qc_f41_quality_compounder_turn_210d_slope_v102_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(210)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 15d tanh
def f41qc_f41_quality_compounder_turn_15d_slope_v103_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(15)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 63d rank
def f41qc_f41_quality_compounder_turn_63d_slope_v104_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(63)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[turn] 168d rank
def f41qc_f41_quality_compounder_turn_168d_slope_v105_signal(revenue, equity, netmargin):
    turnp = _safe_div(revenue, equity)
    base = _z(turnp, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(168)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 294d tanh
def f41qc_f41_quality_compounder_roicminusmargin_294d_slope_v106_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(294)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 42d tanh
def f41qc_f41_quality_compounder_roicminusmargin_42d_slope_v107_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(42)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 126d rank
def f41qc_f41_quality_compounder_roicminusmargin_126d_slope_v108_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(126)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 231d rank
def f41qc_f41_quality_compounder_roicminusmargin_231d_slope_v109_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(231)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 21d plain
def f41qc_f41_quality_compounder_roicminusmargin_21d_slope_v110_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 84d z
def f41qc_f41_quality_compounder_roicminusmargin_84d_slope_v111_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(84)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicminusmargin] 189d norm
def f41qc_f41_quality_compounder_roicminusmargin_189d_slope_v112_signal(roic, netmargin):
    base = _mean(roic, 252) - _mean(netmargin, 252)
    d = base - base.shift(189)
    result = d / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 315d rank
def f41qc_f41_quality_compounder_fcfcover_315d_slope_v113_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(315)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 52d plain
def f41qc_f41_quality_compounder_fcfcover_52d_slope_v114_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(52)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 147d z
def f41qc_f41_quality_compounder_fcfcover_147d_slope_v115_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(147)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 252d norm
def f41qc_f41_quality_compounder_fcfcover_252d_slope_v116_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(252)
    result = d / _std(base, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 31d tanh
def f41qc_f41_quality_compounder_fcfcover_31d_slope_v117_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(31)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 105d tanh
def f41qc_f41_quality_compounder_fcfcover_105d_slope_v118_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(105)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfcover] 210d rank
def f41qc_f41_quality_compounder_fcfcover_210d_slope_v119_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    base = np.tanh(5.0 * (fcfm - _f41_growth(sharesbas, 126)))
    d = base - base.shift(210)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 15d norm
def f41qc_f41_quality_compounder_marginps_15d_slope_v120_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(15)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 63d tanh
def f41qc_f41_quality_compounder_marginps_63d_slope_v121_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(63)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 168d tanh
def f41qc_f41_quality_compounder_marginps_168d_slope_v122_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(168)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 294d rank
def f41qc_f41_quality_compounder_marginps_294d_slope_v123_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(294)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 42d rank
def f41qc_f41_quality_compounder_marginps_42d_slope_v124_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(42)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 126d plain
def f41qc_f41_quality_compounder_marginps_126d_slope_v125_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[marginps] 231d z
def f41qc_f41_quality_compounder_marginps_231d_slope_v126_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    d = base - base.shift(231)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 21d rank
def f41qc_f41_quality_compounder_fcfm_21d_slope_v127_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(21)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 84d rank
def f41qc_f41_quality_compounder_fcfm_84d_slope_v128_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(84)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 189d plain
def f41qc_f41_quality_compounder_fcfm_189d_slope_v129_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(189)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 315d z
def f41qc_f41_quality_compounder_fcfm_315d_slope_v130_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(315)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 52d norm
def f41qc_f41_quality_compounder_fcfm_52d_slope_v131_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(52)
    result = d / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 147d tanh
def f41qc_f41_quality_compounder_fcfm_147d_slope_v132_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(147)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfm] 252d tanh
def f41qc_f41_quality_compounder_fcfm_252d_slope_v133_signal(fcf, revenue):
    base = _mean(_f41_fcf_margin(fcf, revenue), 252)
    d = base - base.shift(252)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 31d z
def f41qc_f41_quality_compounder_master_31d_slope_v134_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(31)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 105d norm
def f41qc_f41_quality_compounder_master_105d_slope_v135_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(105)
    result = d / _std(base, 105).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 210d tanh
def f41qc_f41_quality_compounder_master_210d_slope_v136_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(210)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 15d tanh
def f41qc_f41_quality_compounder_master_15d_slope_v137_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(15)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 63d rank
def f41qc_f41_quality_compounder_master_63d_slope_v138_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(63)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 168d rank
def f41qc_f41_quality_compounder_master_168d_slope_v139_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(168)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[master] 294d plain
def f41qc_f41_quality_compounder_master_294d_slope_v140_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    base = rp + fp + np.tanh(5.0 * _mean(netmargin, 252)) - 5.0 * dil
    d = base - base.shift(294)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicfcf] 10d accel
def f41qc_f41_quality_compounder_roicfcf_10d_slope_v141_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _f41_pos_frac(roic, 252) * _f41_pos_frac(fcfm, 252) * _mean(roic, 252)
    d = base - base.shift(10)
    result = d - d.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[qmd] 273d tanh
def f41qc_f41_quality_compounder_qmd_273d_slope_v142_signal(roic, sharesbas):
    base = _rank(_mean(roic, 126), 252) - _z(_f41_dilution(sharesbas, 252), 252)
    d = base - base.shift(273)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicpersist] 357d rank
def f41qc_f41_quality_compounder_roicpersist_357d_slope_v143_signal(roic):
    base = _f41_pos_frac(roic, 252) - 0.5
    d = base - base.shift(357)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[fcfgrow] 25d accel
def f41qc_f41_quality_compounder_fcfgrow_25d_slope_v144_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(fcfm, 252) * _f41_growth(revenue, 252)
    d = base - base.shift(25)
    result = d - d.shift(12)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[roicmargin] 200d tanh
def f41qc_f41_quality_compounder_roicmargin_200d_slope_v145_signal(roic, netmargin):
    base = _z(roic, 126) * _z(netmargin, 126)
    d = base - base.shift(200)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[revgrow] 140d rank
def f41qc_f41_quality_compounder_revgrow_140d_slope_v146_signal(revenue):
    base = _f41_growth(revenue, 252)
    d = base - base.shift(140)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[equitygrow] 95d accel
def f41qc_f41_quality_compounder_equitygrow_95d_slope_v147_signal(equity):
    base = _f41_growth(equity, 252)
    d = base - base.shift(95)
    result = d - d.shift(47)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[persharegrow] 175d tanh
def f41qc_f41_quality_compounder_persharegrow_175d_slope_v148_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    base = _z(rps, 252)
    d = base - base.shift(175)
    sc = _std(d, 252).replace(0, np.nan)
    result = np.tanh(d / sc)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[twinprofit] 285d rank
def f41qc_f41_quality_compounder_twinprofit_285d_slope_v149_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    base = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    d = base - base.shift(285)
    result = _rank(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope d/dt[zblend] 230d accel
def f41qc_f41_quality_compounder_zblend_230d_slope_v150_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    base = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    d = base - base.shift(230)
    result = d - d.shift(115)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41qc_f41_quality_compounder_roicfcf_15d_slope_v001_signal,
    f41qc_f41_quality_compounder_roicfcf_63d_slope_v002_signal,
    f41qc_f41_quality_compounder_roicfcf_168d_slope_v003_signal,
    f41qc_f41_quality_compounder_roicfcf_294d_slope_v004_signal,
    f41qc_f41_quality_compounder_roicfcf_42d_slope_v005_signal,
    f41qc_f41_quality_compounder_roicfcf_126d_slope_v006_signal,
    f41qc_f41_quality_compounder_roicfcf_231d_slope_v007_signal,
    f41qc_f41_quality_compounder_qmd_21d_slope_v008_signal,
    f41qc_f41_quality_compounder_qmd_84d_slope_v009_signal,
    f41qc_f41_quality_compounder_qmd_189d_slope_v010_signal,
    f41qc_f41_quality_compounder_qmd_315d_slope_v011_signal,
    f41qc_f41_quality_compounder_qmd_52d_slope_v012_signal,
    f41qc_f41_quality_compounder_qmd_147d_slope_v013_signal,
    f41qc_f41_quality_compounder_qmd_252d_slope_v014_signal,
    f41qc_f41_quality_compounder_roicpersist_31d_slope_v015_signal,
    f41qc_f41_quality_compounder_roicpersist_105d_slope_v016_signal,
    f41qc_f41_quality_compounder_roicpersist_210d_slope_v017_signal,
    f41qc_f41_quality_compounder_roicpersist_15d_slope_v018_signal,
    f41qc_f41_quality_compounder_roicpersist_63d_slope_v019_signal,
    f41qc_f41_quality_compounder_roicpersist_168d_slope_v020_signal,
    f41qc_f41_quality_compounder_roicpersist_294d_slope_v021_signal,
    f41qc_f41_quality_compounder_fcfgrow_42d_slope_v022_signal,
    f41qc_f41_quality_compounder_fcfgrow_126d_slope_v023_signal,
    f41qc_f41_quality_compounder_fcfgrow_231d_slope_v024_signal,
    f41qc_f41_quality_compounder_fcfgrow_21d_slope_v025_signal,
    f41qc_f41_quality_compounder_fcfgrow_84d_slope_v026_signal,
    f41qc_f41_quality_compounder_fcfgrow_189d_slope_v027_signal,
    f41qc_f41_quality_compounder_fcfgrow_315d_slope_v028_signal,
    f41qc_f41_quality_compounder_roicmargin_52d_slope_v029_signal,
    f41qc_f41_quality_compounder_roicmargin_147d_slope_v030_signal,
    f41qc_f41_quality_compounder_roicmargin_252d_slope_v031_signal,
    f41qc_f41_quality_compounder_roicmargin_31d_slope_v032_signal,
    f41qc_f41_quality_compounder_roicmargin_105d_slope_v033_signal,
    f41qc_f41_quality_compounder_roicmargin_210d_slope_v034_signal,
    f41qc_f41_quality_compounder_roicmargin_15d_slope_v035_signal,
    f41qc_f41_quality_compounder_revgrow_63d_slope_v036_signal,
    f41qc_f41_quality_compounder_revgrow_168d_slope_v037_signal,
    f41qc_f41_quality_compounder_revgrow_294d_slope_v038_signal,
    f41qc_f41_quality_compounder_revgrow_42d_slope_v039_signal,
    f41qc_f41_quality_compounder_revgrow_126d_slope_v040_signal,
    f41qc_f41_quality_compounder_revgrow_231d_slope_v041_signal,
    f41qc_f41_quality_compounder_revgrow_21d_slope_v042_signal,
    f41qc_f41_quality_compounder_equitygrow_84d_slope_v043_signal,
    f41qc_f41_quality_compounder_equitygrow_189d_slope_v044_signal,
    f41qc_f41_quality_compounder_equitygrow_315d_slope_v045_signal,
    f41qc_f41_quality_compounder_equitygrow_52d_slope_v046_signal,
    f41qc_f41_quality_compounder_equitygrow_147d_slope_v047_signal,
    f41qc_f41_quality_compounder_equitygrow_252d_slope_v048_signal,
    f41qc_f41_quality_compounder_equitygrow_31d_slope_v049_signal,
    f41qc_f41_quality_compounder_persharegrow_105d_slope_v050_signal,
    f41qc_f41_quality_compounder_persharegrow_210d_slope_v051_signal,
    f41qc_f41_quality_compounder_persharegrow_15d_slope_v052_signal,
    f41qc_f41_quality_compounder_persharegrow_63d_slope_v053_signal,
    f41qc_f41_quality_compounder_persharegrow_168d_slope_v054_signal,
    f41qc_f41_quality_compounder_persharegrow_294d_slope_v055_signal,
    f41qc_f41_quality_compounder_persharegrow_42d_slope_v056_signal,
    f41qc_f41_quality_compounder_twinprofit_126d_slope_v057_signal,
    f41qc_f41_quality_compounder_twinprofit_231d_slope_v058_signal,
    f41qc_f41_quality_compounder_twinprofit_21d_slope_v059_signal,
    f41qc_f41_quality_compounder_twinprofit_84d_slope_v060_signal,
    f41qc_f41_quality_compounder_twinprofit_189d_slope_v061_signal,
    f41qc_f41_quality_compounder_twinprofit_315d_slope_v062_signal,
    f41qc_f41_quality_compounder_twinprofit_52d_slope_v063_signal,
    f41qc_f41_quality_compounder_zblend_147d_slope_v064_signal,
    f41qc_f41_quality_compounder_zblend_252d_slope_v065_signal,
    f41qc_f41_quality_compounder_zblend_31d_slope_v066_signal,
    f41qc_f41_quality_compounder_zblend_105d_slope_v067_signal,
    f41qc_f41_quality_compounder_zblend_210d_slope_v068_signal,
    f41qc_f41_quality_compounder_zblend_15d_slope_v069_signal,
    f41qc_f41_quality_compounder_zblend_63d_slope_v070_signal,
    f41qc_f41_quality_compounder_cashqmd_168d_slope_v071_signal,
    f41qc_f41_quality_compounder_cashqmd_294d_slope_v072_signal,
    f41qc_f41_quality_compounder_cashqmd_42d_slope_v073_signal,
    f41qc_f41_quality_compounder_cashqmd_126d_slope_v074_signal,
    f41qc_f41_quality_compounder_cashqmd_231d_slope_v075_signal,
    f41qc_f41_quality_compounder_cashqmd_21d_slope_v076_signal,
    f41qc_f41_quality_compounder_cashqmd_84d_slope_v077_signal,
    f41qc_f41_quality_compounder_durindex_189d_slope_v078_signal,
    f41qc_f41_quality_compounder_durindex_315d_slope_v079_signal,
    f41qc_f41_quality_compounder_durindex_52d_slope_v080_signal,
    f41qc_f41_quality_compounder_durindex_147d_slope_v081_signal,
    f41qc_f41_quality_compounder_durindex_252d_slope_v082_signal,
    f41qc_f41_quality_compounder_durindex_31d_slope_v083_signal,
    f41qc_f41_quality_compounder_durindex_105d_slope_v084_signal,
    f41qc_f41_quality_compounder_bvps_210d_slope_v085_signal,
    f41qc_f41_quality_compounder_bvps_15d_slope_v086_signal,
    f41qc_f41_quality_compounder_bvps_63d_slope_v087_signal,
    f41qc_f41_quality_compounder_bvps_168d_slope_v088_signal,
    f41qc_f41_quality_compounder_bvps_294d_slope_v089_signal,
    f41qc_f41_quality_compounder_bvps_42d_slope_v090_signal,
    f41qc_f41_quality_compounder_bvps_126d_slope_v091_signal,
    f41qc_f41_quality_compounder_accrualgap_231d_slope_v092_signal,
    f41qc_f41_quality_compounder_accrualgap_21d_slope_v093_signal,
    f41qc_f41_quality_compounder_accrualgap_84d_slope_v094_signal,
    f41qc_f41_quality_compounder_accrualgap_189d_slope_v095_signal,
    f41qc_f41_quality_compounder_accrualgap_315d_slope_v096_signal,
    f41qc_f41_quality_compounder_accrualgap_52d_slope_v097_signal,
    f41qc_f41_quality_compounder_accrualgap_147d_slope_v098_signal,
    f41qc_f41_quality_compounder_turn_252d_slope_v099_signal,
    f41qc_f41_quality_compounder_turn_31d_slope_v100_signal,
    f41qc_f41_quality_compounder_turn_105d_slope_v101_signal,
    f41qc_f41_quality_compounder_turn_210d_slope_v102_signal,
    f41qc_f41_quality_compounder_turn_15d_slope_v103_signal,
    f41qc_f41_quality_compounder_turn_63d_slope_v104_signal,
    f41qc_f41_quality_compounder_turn_168d_slope_v105_signal,
    f41qc_f41_quality_compounder_roicminusmargin_294d_slope_v106_signal,
    f41qc_f41_quality_compounder_roicminusmargin_42d_slope_v107_signal,
    f41qc_f41_quality_compounder_roicminusmargin_126d_slope_v108_signal,
    f41qc_f41_quality_compounder_roicminusmargin_231d_slope_v109_signal,
    f41qc_f41_quality_compounder_roicminusmargin_21d_slope_v110_signal,
    f41qc_f41_quality_compounder_roicminusmargin_84d_slope_v111_signal,
    f41qc_f41_quality_compounder_roicminusmargin_189d_slope_v112_signal,
    f41qc_f41_quality_compounder_fcfcover_315d_slope_v113_signal,
    f41qc_f41_quality_compounder_fcfcover_52d_slope_v114_signal,
    f41qc_f41_quality_compounder_fcfcover_147d_slope_v115_signal,
    f41qc_f41_quality_compounder_fcfcover_252d_slope_v116_signal,
    f41qc_f41_quality_compounder_fcfcover_31d_slope_v117_signal,
    f41qc_f41_quality_compounder_fcfcover_105d_slope_v118_signal,
    f41qc_f41_quality_compounder_fcfcover_210d_slope_v119_signal,
    f41qc_f41_quality_compounder_marginps_15d_slope_v120_signal,
    f41qc_f41_quality_compounder_marginps_63d_slope_v121_signal,
    f41qc_f41_quality_compounder_marginps_168d_slope_v122_signal,
    f41qc_f41_quality_compounder_marginps_294d_slope_v123_signal,
    f41qc_f41_quality_compounder_marginps_42d_slope_v124_signal,
    f41qc_f41_quality_compounder_marginps_126d_slope_v125_signal,
    f41qc_f41_quality_compounder_marginps_231d_slope_v126_signal,
    f41qc_f41_quality_compounder_fcfm_21d_slope_v127_signal,
    f41qc_f41_quality_compounder_fcfm_84d_slope_v128_signal,
    f41qc_f41_quality_compounder_fcfm_189d_slope_v129_signal,
    f41qc_f41_quality_compounder_fcfm_315d_slope_v130_signal,
    f41qc_f41_quality_compounder_fcfm_52d_slope_v131_signal,
    f41qc_f41_quality_compounder_fcfm_147d_slope_v132_signal,
    f41qc_f41_quality_compounder_fcfm_252d_slope_v133_signal,
    f41qc_f41_quality_compounder_master_31d_slope_v134_signal,
    f41qc_f41_quality_compounder_master_105d_slope_v135_signal,
    f41qc_f41_quality_compounder_master_210d_slope_v136_signal,
    f41qc_f41_quality_compounder_master_15d_slope_v137_signal,
    f41qc_f41_quality_compounder_master_63d_slope_v138_signal,
    f41qc_f41_quality_compounder_master_168d_slope_v139_signal,
    f41qc_f41_quality_compounder_master_294d_slope_v140_signal,
    f41qc_f41_quality_compounder_roicfcf_10d_slope_v141_signal,
    f41qc_f41_quality_compounder_qmd_273d_slope_v142_signal,
    f41qc_f41_quality_compounder_roicpersist_357d_slope_v143_signal,
    f41qc_f41_quality_compounder_fcfgrow_25d_slope_v144_signal,
    f41qc_f41_quality_compounder_roicmargin_200d_slope_v145_signal,
    f41qc_f41_quality_compounder_revgrow_140d_slope_v146_signal,
    f41qc_f41_quality_compounder_equitygrow_95d_slope_v147_signal,
    f41qc_f41_quality_compounder_persharegrow_175d_slope_v148_signal,
    f41qc_f41_quality_compounder_twinprofit_285d_slope_v149_signal,
    f41qc_f41_quality_compounder_zblend_230d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_QUALITY_COMPOUNDER_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False, noise=0.0,
              cycle=0.0, cyc_period=378):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if cycle > 0:
            phase = g.uniform(0, 2 * np.pi)
            s = s + base * cycle * np.sin(2 * np.pi * np.arange(n) / cyc_period + phase)
        if noise > 0:
            s = s * (1.0 + g.normal(0.0, noise, n))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    roic = _fund(101, base=0.18, drift=0.0, vol=0.14, allow_neg=True, noise=0.04,
                 cycle=0.9, cyc_period=340).rename("roic")
    fcf = _fund(102, base=1.2e8, drift=0.0, vol=0.16, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=470).rename("fcf")
    netmargin = _fund(103, base=0.22, drift=0.0, vol=0.14, allow_neg=True, noise=0.04,
                      cycle=0.9, cyc_period=410).rename("netmargin")
    sharesbas = _fund(104, base=8e7, drift=0.0, vol=0.05, noise=0.015).rename("sharesbas")
    revenue = _fund(105, base=6e8, drift=0.03, vol=0.06, noise=0.02).rename("revenue")
    equity = _fund(106, base=9e8, drift=0.025, vol=0.05, noise=0.02).rename("equity")

    cols = {"roic": roic, "fcf": fcf, "netmargin": netmargin,
            "sharesbas": sharesbas, "revenue": revenue, "equity": equity}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f41_quality_compounder_2nd_derivatives_001_150_claude: %d features pass" % n_features)
