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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    return s - s.shift(w)


def _f33_roic_level(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f33_fcf_roic(fcf, equity, w):
    r = fcf / equity.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_reinvest_rate(fcf, netinc, w):
    payout = fcf / netinc.replace(0, np.nan)
    reinv = 1.0 - payout
    return reinv.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_dilution(sharesbas, w):
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f33_revgrowth(revenue, w):
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


def _f33_fcf_margin(fcf, revenue, w):
    r = fcf / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f33_capital_turnover(revenue, equity, w):
    t = revenue / equity.replace(0, np.nan)
    return t.rolling(w, min_periods=max(1, w // 2)).mean()


def f33qc_f33_quality_compounder_qmd_252d_jerk_v001_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) - _f33_dilution(sharesbas, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_qmd_252d_jerk_v002_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) - _f33_dilution(sharesbas, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_qmd_252d_jerk_v003_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) - _f33_dilution(sharesbas, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicbb_252d_jerk_v004_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicbb_252d_jerk_v005_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicbb_252d_jerk_v006_signal(roic, sharesbas):
    b0 = _f33_roic_level(roic, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroic_252d_jerk_v007_signal(fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroic_252d_jerk_v008_signal(fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroic_252d_jerk_v009_signal(fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashconv_252d_jerk_v010_signal(roic, fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252) - _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashconv_252d_jerk_v011_signal(roic, fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252) - _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashconv_252d_jerk_v012_signal(roic, fcf, equity):
    b0 = _f33_fcf_roic(fcf, equity, 252) - _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_compound_252d_jerk_v013_signal(roic, fcf, netinc):
    b0 = _f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_compound_252d_jerk_v014_signal(roic, fcf, netinc):
    b0 = _f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_compound_252d_jerk_v015_signal(roic, fcf, netinc):
    b0 = _f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinveff_504d_jerk_v016_signal(roic, revenue):
    b0 = _z(_f33_revgrowth(revenue, 252), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinveff_504d_jerk_v017_signal(roic, revenue):
    b0 = _z(_f33_revgrowth(revenue, 252), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinveff_504d_jerk_v018_signal(roic, revenue):
    b0 = _z(_f33_revgrowth(revenue, 252), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v019_signal(fcf, revenue, roic):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v020_signal(fcf, revenue, roic):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v021_signal(fcf, revenue, roic):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_turnroic_252d_jerk_v022_signal(revenue, equity, roic):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_turnroic_252d_jerk_v023_signal(revenue, equity, roic):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_turnroic_252d_jerk_v024_signal(revenue, equity, roic):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durable_504d_jerk_v025_signal(roic, sharesbas):
    stab = _f33_roic_stability(roic, 252)
    bb = -_f33_dilution(sharesbas, 504)
    b0 = _rank(stab, 252) * np.sign(bb) + _rank(bb, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durable_504d_jerk_v026_signal(roic, sharesbas):
    stab = _f33_roic_stability(roic, 252)
    bb = -_f33_dilution(sharesbas, 504)
    b0 = _rank(stab, 252) * np.sign(bb) + _rank(bb, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durable_504d_jerk_v027_signal(roic, sharesbas):
    stab = _f33_roic_stability(roic, 252)
    bb = -_f33_dilution(sharesbas, 504)
    b0 = _rank(stab, 252) * np.sign(bb) + _rank(bb, 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_hurdle_252d_jerk_v028_signal(roic, fcf, netinc):
    b0 = _z((_f33_roic_level(roic, 126) - 0.08).clip(lower=0), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126).clip(lower=0), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_hurdle_252d_jerk_v029_signal(roic, fcf, netinc):
    b0 = _z((_f33_roic_level(roic, 126) - 0.08).clip(lower=0), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126).clip(lower=0), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_hurdle_252d_jerk_v030_signal(roic, fcf, netinc):
    b0 = _z((_f33_roic_level(roic, 126) - 0.08).clip(lower=0), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126).clip(lower=0), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_econprofit_504d_jerk_v031_signal(roic, equity):
    b0 = _z(_f33_roic_level(roic, 252) - 0.08, 252) * _z(_f33_revgrowth(equity, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_econprofit_504d_jerk_v032_signal(roic, equity):
    b0 = _z(_f33_roic_level(roic, 252) - 0.08, 252) * _z(_f33_revgrowth(equity, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_econprofit_504d_jerk_v033_signal(roic, equity):
    b0 = _z(_f33_roic_level(roic, 252) - 0.08, 252) * _z(_f33_revgrowth(equity, 252), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_moat_252d_jerk_v034_signal(roic, fcf, revenue):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_fcf_margin(fcf, revenue, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_moat_252d_jerk_v035_signal(roic, fcf, revenue):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_fcf_margin(fcf, revenue, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_moat_252d_jerk_v036_signal(roic, fcf, revenue):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_fcf_margin(fcf, revenue, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v037_signal(netinc, revenue, roic):
    b0 = (netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v038_signal(netinc, revenue, roic):
    b0 = (netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v039_signal(netinc, revenue, roic):
    b0 = (netinc / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roeroic_252d_jerk_v040_signal(netinc, equity, roic):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = roe - _f33_roic_level(roic, 126)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roeroic_252d_jerk_v041_signal(netinc, equity, roic):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = roe - _f33_roic_level(roic, 126)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roeroic_252d_jerk_v042_signal(netinc, equity, roic):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = roe - _f33_roic_level(roic, 126)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v043_signal(fcf, netinc, roic):
    b0 = (fcf / netinc.replace(0, np.nan)).clip(-3.0, 3.0).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v044_signal(fcf, netinc, roic):
    b0 = (fcf / netinc.replace(0, np.nan)).clip(-3.0, 3.0).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v045_signal(fcf, netinc, roic):
    b0 = (fcf / netinc.replace(0, np.nan)).clip(-3.0, 3.0).rolling(252, min_periods=126).mean() * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_revpsroic_504d_jerk_v046_signal(revenue, sharesbas, roic):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    b0 = g * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_revpsroic_504d_jerk_v047_signal(revenue, sharesbas, roic):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    b0 = g * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_revpsroic_504d_jerk_v048_signal(revenue, sharesbas, roic):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = _z(rps / rps.shift(504).replace(0, np.nan) - 1.0, 252)
    b0 = g * _z(_f33_roic_level(roic, 126), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v049_signal(equity, sharesbas, roic):
    bvps = equity / sharesbas.replace(0, np.nan)
    b0 = (bvps / bvps.shift(504).replace(0, np.nan) - 1.0).clip(-0.9, 3.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v050_signal(equity, sharesbas, roic):
    bvps = equity / sharesbas.replace(0, np.nan)
    b0 = (bvps / bvps.shift(504).replace(0, np.nan) - 1.0).clip(-0.9, 3.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v051_signal(equity, sharesbas, roic):
    bvps = equity / sharesbas.replace(0, np.nan)
    b0 = (bvps / bvps.shift(504).replace(0, np.nan) - 1.0).clip(-0.9, 3.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epsroic_504d_jerk_v052_signal(netinc, sharesbas, roic):
    eps = netinc / sharesbas.replace(0, np.nan)
    b0 = (eps / eps.shift(504).replace(0, np.nan) - 1.0).clip(-2.0, 5.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epsroic_504d_jerk_v053_signal(netinc, sharesbas, roic):
    eps = netinc / sharesbas.replace(0, np.nan)
    b0 = (eps / eps.shift(504).replace(0, np.nan) - 1.0).clip(-2.0, 5.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epsroic_504d_jerk_v054_signal(netinc, sharesbas, roic):
    eps = netinc / sharesbas.replace(0, np.nan)
    b0 = (eps / eps.shift(504).replace(0, np.nan) - 1.0).clip(-2.0, 5.0) * (1.0 + _f33_roic_level(roic, 252).clip(-0.5, 1.0))
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashdupont_252d_jerk_v055_signal(fcf, equity, revenue):
    b0 = _f33_fcf_roic(fcf, equity, 252) * _f33_capital_turnover(revenue, equity, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashdupont_252d_jerk_v056_signal(fcf, equity, revenue):
    b0 = _f33_fcf_roic(fcf, equity, 252) * _f33_capital_turnover(revenue, equity, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashdupont_252d_jerk_v057_signal(fcf, equity, revenue):
    b0 = _f33_fcf_roic(fcf, equity, 252) * _f33_capital_turnover(revenue, equity, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_sustgrow_252d_jerk_v058_signal(roic, fcf, netinc):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_sustgrow_252d_jerk_v059_signal(roic, fcf, netinc):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_sustgrow_252d_jerk_v060_signal(roic, fcf, netinc):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_reinvest_rate(fcf, netinc, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v061_signal(fcf, netinc, revenue):
    b0 = _f33_reinvest_rate(fcf, netinc, 252) * _f33_revgrowth(revenue, 504)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v062_signal(fcf, netinc, revenue):
    b0 = _f33_reinvest_rate(fcf, netinc, 252) * _f33_revgrowth(revenue, 504)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v063_signal(fcf, netinc, revenue):
    b0 = _f33_reinvest_rate(fcf, netinc, 252) * _f33_revgrowth(revenue, 504)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v064_signal(fcf, revenue):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 252), 252) * _z(_f33_revgrowth(revenue, 504), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v065_signal(fcf, revenue):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 252), 252) * _z(_f33_revgrowth(revenue, 504), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v066_signal(fcf, revenue):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 252), 252) * _z(_f33_revgrowth(revenue, 504), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_buybackcap_252d_jerk_v067_signal(fcf, revenue, sharesbas):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_buybackcap_252d_jerk_v068_signal(fcf, revenue, sharesbas):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_buybackcap_252d_jerk_v069_signal(fcf, revenue, sharesbas):
    b0 = _f33_fcf_margin(fcf, revenue, 252) * (1.0 + (-_f33_dilution(sharesbas, 252)))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_selffund_504d_jerk_v070_signal(roic, revenue, equity):
    needed = _f33_revgrowth(revenue, 504) / _f33_capital_turnover(revenue, equity, 252).replace(0, np.nan)
    b0 = _f33_roic_level(roic, 252) - needed.clip(-1.0, 1.0)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_selffund_504d_jerk_v071_signal(roic, revenue, equity):
    needed = _f33_revgrowth(revenue, 504) / _f33_capital_turnover(revenue, equity, 252).replace(0, np.nan)
    b0 = _f33_roic_level(roic, 252) - needed.clip(-1.0, 1.0)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_selffund_504d_jerk_v072_signal(roic, revenue, equity):
    needed = _f33_revgrowth(revenue, 504) / _f33_capital_turnover(revenue, equity, 252).replace(0, np.nan)
    b0 = _f33_roic_level(roic, 252) - needed.clip(-1.0, 1.0)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_index4_252d_jerk_v073_signal(roic, fcf, equity, netinc, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic, 252), 504), _z(_f33_fcf_roic(fcf, equity, 252), 504), _z(_f33_reinvest_rate(fcf, netinc, 252), 504), _z(-_f33_dilution(sharesbas, 252), 504)], axis=1)
    b0 = parts.max(axis=1) - parts.min(axis=1)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_index4_252d_jerk_v074_signal(roic, fcf, equity, netinc, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic, 252), 504), _z(_f33_fcf_roic(fcf, equity, 252), 504), _z(_f33_reinvest_rate(fcf, netinc, 252), 504), _z(-_f33_dilution(sharesbas, 252), 504)], axis=1)
    b0 = parts.max(axis=1) - parts.min(axis=1)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_index4_252d_jerk_v075_signal(roic, fcf, equity, netinc, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic, 252), 504), _z(_f33_fcf_roic(fcf, equity, 252), 504), _z(_f33_reinvest_rate(fcf, netinc, 252), 504), _z(-_f33_dilution(sharesbas, 252), 504)], axis=1)
    b0 = parts.max(axis=1) - parts.min(axis=1)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durtriple_252d_jerk_v076_signal(roic, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252), 252) + _rank(_f33_roic_stability(roic, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durtriple_252d_jerk_v077_signal(roic, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252), 252) + _rank(_f33_roic_stability(roic, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_durtriple_252d_jerk_v078_signal(roic, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252), 252) + _rank(_f33_roic_stability(roic, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v079_signal(fcf, equity, sharesbas):
    b0 = _z(_f33_fcf_roic(fcf, equity, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v080_signal(fcf, equity, sharesbas):
    b0 = _z(_f33_fcf_roic(fcf, equity, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v081_signal(fcf, equity, sharesbas):
    b0 = _z(_f33_fcf_roic(fcf, equity, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicpershare_504d_jerk_v082_signal(roic, sharesbas):
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(_f33_roic_level(roic, 252) / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicpershare_504d_jerk_v083_signal(roic, sharesbas):
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(_f33_roic_level(roic, 252) / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicpershare_504d_jerk_v084_signal(roic, sharesbas):
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(_f33_roic_level(roic, 252) / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v085_signal(fcf, revenue, equity):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 126), 252) * _z(_f33_capital_turnover(revenue, equity, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v086_signal(fcf, revenue, equity):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 126), 252) * _z(_f33_capital_turnover(revenue, equity, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v087_signal(fcf, revenue, equity):
    b0 = _z(_f33_fcf_margin(fcf, revenue, 126), 252) * _z(_f33_capital_turnover(revenue, equity, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_blendroic_252d_jerk_v088_signal(roic, fcf, equity):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_roic(fcf, equity, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_blendroic_252d_jerk_v089_signal(roic, fcf, equity):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_roic(fcf, equity, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_blendroic_252d_jerk_v090_signal(roic, fcf, equity):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_roic(fcf, equity, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvqual_252d_jerk_v091_signal(roic, fcf, netinc, sharesbas):
    b0 = _z(_f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _z(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvqual_252d_jerk_v092_signal(roic, fcf, netinc, sharesbas):
    b0 = _z(_f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _z(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_reinvqual_252d_jerk_v093_signal(roic, fcf, netinc, sharesbas):
    b0 = _z(_f33_roic_level(roic, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _z(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v094_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v095_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v096_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252) * _f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_triple_504d_jerk_v097_signal(revenue, fcf, equity, sharesbas):
    b0 = _f33_revgrowth(revenue, 504) * _f33_fcf_roic(fcf, equity, 252) - _f33_dilution(sharesbas, 504)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_triple_504d_jerk_v098_signal(revenue, fcf, equity, sharesbas):
    b0 = _f33_revgrowth(revenue, 504) * _f33_fcf_roic(fcf, equity, 252) - _f33_dilution(sharesbas, 504)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_triple_504d_jerk_v099_signal(revenue, fcf, equity, sharesbas):
    b0 = _f33_revgrowth(revenue, 504) * _f33_fcf_roic(fcf, equity, 252) - _f33_dilution(sharesbas, 504)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v100_signal(roic, equity):
    b0 = _f33_roic_level(roic, 252) * _f33_revgrowth(equity, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v101_signal(roic, equity):
    b0 = _f33_roic_level(roic, 252) * _f33_revgrowth(equity, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v102_signal(roic, equity):
    b0 = _f33_roic_level(roic, 252) * _f33_revgrowth(equity, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_harmret_252d_jerk_v103_signal(roic, fcf, equity, sharesbas):
    r = _f33_roic_level(roic, 252).clip(lower=0.001)
    cash = _f33_fcf_roic(fcf, equity, 252).clip(lower=0.001)
    harm = 2.0 / (1.0 / r + 1.0 / cash)
    b0 = _rank(harm, 252) * _rank(-_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_harmret_252d_jerk_v104_signal(roic, fcf, equity, sharesbas):
    r = _f33_roic_level(roic, 252).clip(lower=0.001)
    cash = _f33_fcf_roic(fcf, equity, 252).clip(lower=0.001)
    harm = 2.0 / (1.0 / r + 1.0 / cash)
    b0 = _rank(harm, 252) * _rank(-_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_harmret_252d_jerk_v105_signal(roic, fcf, equity, sharesbas):
    r = _f33_roic_level(roic, 252).clip(lower=0.001)
    cash = _f33_fcf_roic(fcf, equity, 252).clip(lower=0.001)
    harm = 2.0 / (1.0 / r + 1.0 / cash)
    b0 = _rank(harm, 252) * _rank(-_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v106_signal(fcf, revenue, equity):
    fm = _rank(_f33_fcf_margin(fcf, revenue, 126), 252)
    t = _rank(_f33_capital_turnover(revenue, equity, 126), 252)
    b0 = fm - t
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v107_signal(fcf, revenue, equity):
    fm = _rank(_f33_fcf_margin(fcf, revenue, 126), 252)
    t = _rank(_f33_capital_turnover(revenue, equity, 126), 252)
    b0 = fm - t
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v108_signal(fcf, revenue, equity):
    fm = _rank(_f33_fcf_margin(fcf, revenue, 126), 252)
    t = _rank(_f33_capital_turnover(revenue, equity, 126), 252)
    b0 = fm - t
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_ownerret_252d_jerk_v109_signal(fcf, revenue, sharesbas, roic):
    fm = _z(_f33_fcf_margin(fcf, revenue, 126), 252)
    d = _z(_f33_dilution(sharesbas, 126), 252)
    b0 = (fm - d) * np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_ownerret_252d_jerk_v110_signal(fcf, revenue, sharesbas, roic):
    fm = _z(_f33_fcf_margin(fcf, revenue, 126), 252)
    d = _z(_f33_dilution(sharesbas, 126), 252)
    b0 = (fm - d) * np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_ownerret_252d_jerk_v111_signal(fcf, revenue, sharesbas, roic):
    fm = _z(_f33_fcf_margin(fcf, revenue, 126), 252)
    d = _z(_f33_dilution(sharesbas, 126), 252)
    b0 = (fm - d) * np.tanh(_f33_roic_stability(roic, 252) / 5.0)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_valuecreate_252d_jerk_v112_signal(roic, fcf, netinc, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252) - 0.08, 252) * _f33_reinvest_rate(fcf, netinc, 252).clip(-1.0, 2.0) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_valuecreate_252d_jerk_v113_signal(roic, fcf, netinc, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252) - 0.08, 252) * _f33_reinvest_rate(fcf, netinc, 252).clip(-1.0, 2.0) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_valuecreate_252d_jerk_v114_signal(roic, fcf, netinc, sharesbas):
    b0 = _rank(_f33_roic_level(roic, 252) - 0.08, 252) * _f33_reinvest_rate(fcf, netinc, 252).clip(-1.0, 2.0) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roepershare_504d_jerk_v115_signal(netinc, equity, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(roe / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roepershare_504d_jerk_v116_signal(netinc, equity, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(roe / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roepershare_504d_jerk_v117_signal(netinc, equity, sharesbas):
    roe = (netinc / equity.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    sg = sharesbas / sharesbas.shift(252).replace(0, np.nan)
    b0 = _rank(roe / sg.replace(0, np.nan), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashqual_252d_jerk_v118_signal(fcf, netinc, revenue, sharesbas):
    fm = _f33_fcf_margin(fcf, revenue, 126)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = _z(fm - nm, 252) * _z(-_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashqual_252d_jerk_v119_signal(fcf, netinc, revenue, sharesbas):
    fm = _f33_fcf_margin(fcf, revenue, 126)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = _z(fm - nm, 252) * _z(-_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_cashqual_252d_jerk_v120_signal(fcf, netinc, revenue, sharesbas):
    fm = _f33_fcf_margin(fcf, revenue, 126)
    nm = (netinc / revenue.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b0 = _z(fm - nm, 252) * _z(-_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_regimereinv_252d_jerk_v121_signal(roic, fcf, netinc):
    med = _f33_roic_level(roic, 126).rolling(504, min_periods=126).median()
    b0 = (_f33_roic_level(roic, 126) - med) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_regimereinv_252d_jerk_v122_signal(roic, fcf, netinc):
    med = _f33_roic_level(roic, 126).rolling(504, min_periods=126).median()
    b0 = (_f33_roic_level(roic, 126) - med) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_regimereinv_252d_jerk_v123_signal(roic, fcf, netinc):
    med = _f33_roic_level(roic, 126).rolling(504, min_periods=126).median()
    b0 = (_f33_roic_level(roic, 126) - med) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epmargin_252d_jerk_v124_signal(roic, revenue, equity):
    spread = _f33_roic_level(roic, 252) - 0.08
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b0 = spread * (1.0 + np.tanh(t))
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epmargin_252d_jerk_v125_signal(roic, revenue, equity):
    spread = _f33_roic_level(roic, 252) - 0.08
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b0 = spread * (1.0 + np.tanh(t))
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_epmargin_252d_jerk_v126_signal(roic, revenue, equity):
    spread = _f33_roic_level(roic, 252) - 0.08
    t = _z(_f33_capital_turnover(revenue, equity, 252), 504)
    b0 = spread * (1.0 + np.tanh(t))
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_richnet_252d_jerk_v127_signal(roic, fcf, revenue, sharesbas):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_margin(fcf, revenue, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_richnet_252d_jerk_v128_signal(roic, fcf, revenue, sharesbas):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_margin(fcf, revenue, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_richnet_252d_jerk_v129_signal(roic, fcf, revenue, sharesbas):
    b0 = _z(_f33_roic_level(roic, 126), 252) * _z(_f33_fcf_margin(fcf, revenue, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_grandscore_504d_jerk_v130_signal(roic, fcf, equity, netinc, revenue, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic,252),504), _z(_f33_fcf_roic(fcf,equity,252),504), _z(_f33_reinvest_rate(fcf,netinc,252),504), _z(_f33_revgrowth(revenue,504),504), _z(-_f33_dilution(sharesbas,504),504)], axis=1)
    b0 = parts.min(axis=1) * parts.std(axis=1)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_grandscore_504d_jerk_v131_signal(roic, fcf, equity, netinc, revenue, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic,252),504), _z(_f33_fcf_roic(fcf,equity,252),504), _z(_f33_reinvest_rate(fcf,netinc,252),504), _z(_f33_revgrowth(revenue,504),504), _z(-_f33_dilution(sharesbas,504),504)], axis=1)
    b0 = parts.min(axis=1) * parts.std(axis=1)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_grandscore_504d_jerk_v132_signal(roic, fcf, equity, netinc, revenue, sharesbas):
    parts = pd.concat([_z(_f33_roic_level(roic,252),504), _z(_f33_fcf_roic(fcf,equity,252),504), _z(_f33_reinvest_rate(fcf,netinc,252),504), _z(_f33_revgrowth(revenue,504),504), _z(-_f33_dilution(sharesbas,504),504)], axis=1)
    b0 = parts.min(axis=1) * parts.std(axis=1)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_convexcomp_252d_jerk_v133_signal(roic, fcf, netinc):
    spread = _f33_roic_level(roic, 252) - 0.08
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b0 = np.sign(spread) * (reinv ** 2) * np.tanh(5.0 * spread.abs())
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_convexcomp_252d_jerk_v134_signal(roic, fcf, netinc):
    spread = _f33_roic_level(roic, 252) - 0.08
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b0 = np.sign(spread) * (reinv ** 2) * np.tanh(5.0 * spread.abs())
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_convexcomp_252d_jerk_v135_signal(roic, fcf, netinc):
    spread = _f33_roic_level(roic, 252) - 0.08
    reinv = _f33_reinvest_rate(fcf, netinc, 252)
    b0 = np.sign(spread) * (reinv ** 2) * np.tanh(5.0 * spread.abs())
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_intfund_252d_jerk_v136_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252), 252) * _rank(_f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_intfund_252d_jerk_v137_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252), 252) * _rank(_f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_intfund_252d_jerk_v138_signal(fcf, equity, netinc, sharesbas):
    b0 = _rank(_f33_fcf_roic(fcf, equity, 252), 252) * _rank(_f33_reinvest_rate(fcf, netinc, 252), 252) - _rank(_f33_dilution(sharesbas, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v139_signal(roic, fcf, netinc):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v140_signal(roic, fcf, netinc):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v141_signal(roic, fcf, netinc):
    b0 = np.tanh(_f33_roic_stability(roic, 252) / 5.0) * _f33_reinvest_rate(fcf, netinc, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v142_signal(fcf, revenue, roic):
    b0 = _rank(_f33_fcf_margin(fcf, revenue, 252), 252) + _rank(_f33_revgrowth(revenue, 504), 252) + _rank(_f33_roic_level(roic, 252), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v143_signal(fcf, revenue, roic):
    b0 = _rank(_f33_fcf_margin(fcf, revenue, 252), 252) + _rank(_f33_revgrowth(revenue, 504), 252) + _rank(_f33_roic_level(roic, 252), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v144_signal(fcf, revenue, roic):
    b0 = _rank(_f33_fcf_margin(fcf, revenue, 252), 252) + _rank(_f33_revgrowth(revenue, 504), 252) + _rank(_f33_roic_level(roic, 252), 252)
    d1 = b0 - b0.shift(252)
    dN = d1 - d1.shift(252)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicconv_252d_jerk_v145_signal(roic, fcf, netinc):
    conv = (fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(252, min_periods=126).mean()
    b0 = conv * _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicconv_252d_jerk_v146_signal(roic, fcf, netinc):
    conv = (fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(252, min_periods=126).mean()
    b0 = conv * _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_roicconv_252d_jerk_v147_signal(roic, fcf, netinc):
    conv = (fcf / netinc.replace(0, np.nan)).clip(-3, 3).rolling(252, min_periods=126).mean()
    b0 = conv * _f33_roic_level(roic, 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_capliteret_252d_jerk_v148_signal(revenue, equity, roic, sharesbas):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(21)
    dN = d1 - d1.shift(21)
    result = dN
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_capliteret_252d_jerk_v149_signal(revenue, equity, roic, sharesbas):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(63)
    dN = d1 - d1.shift(63)
    result = _z(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33qc_f33_quality_compounder_capliteret_252d_jerk_v150_signal(revenue, equity, roic, sharesbas):
    b0 = _z(_f33_capital_turnover(revenue, equity, 126), 252) * _z(_f33_roic_level(roic, 126), 252) - _z(_f33_dilution(sharesbas, 126), 252)
    d1 = b0 - b0.shift(126)
    dN = d1 - d1.shift(126)
    result = _rank(dN, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33qc_f33_quality_compounder_qmd_252d_jerk_v001_signal,
    f33qc_f33_quality_compounder_qmd_252d_jerk_v002_signal,
    f33qc_f33_quality_compounder_qmd_252d_jerk_v003_signal,
    f33qc_f33_quality_compounder_roicbb_252d_jerk_v004_signal,
    f33qc_f33_quality_compounder_roicbb_252d_jerk_v005_signal,
    f33qc_f33_quality_compounder_roicbb_252d_jerk_v006_signal,
    f33qc_f33_quality_compounder_fcfroic_252d_jerk_v007_signal,
    f33qc_f33_quality_compounder_fcfroic_252d_jerk_v008_signal,
    f33qc_f33_quality_compounder_fcfroic_252d_jerk_v009_signal,
    f33qc_f33_quality_compounder_cashconv_252d_jerk_v010_signal,
    f33qc_f33_quality_compounder_cashconv_252d_jerk_v011_signal,
    f33qc_f33_quality_compounder_cashconv_252d_jerk_v012_signal,
    f33qc_f33_quality_compounder_compound_252d_jerk_v013_signal,
    f33qc_f33_quality_compounder_compound_252d_jerk_v014_signal,
    f33qc_f33_quality_compounder_compound_252d_jerk_v015_signal,
    f33qc_f33_quality_compounder_reinveff_504d_jerk_v016_signal,
    f33qc_f33_quality_compounder_reinveff_504d_jerk_v017_signal,
    f33qc_f33_quality_compounder_reinveff_504d_jerk_v018_signal,
    f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v019_signal,
    f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v020_signal,
    f33qc_f33_quality_compounder_fcfmgnroic_252d_jerk_v021_signal,
    f33qc_f33_quality_compounder_turnroic_252d_jerk_v022_signal,
    f33qc_f33_quality_compounder_turnroic_252d_jerk_v023_signal,
    f33qc_f33_quality_compounder_turnroic_252d_jerk_v024_signal,
    f33qc_f33_quality_compounder_durable_504d_jerk_v025_signal,
    f33qc_f33_quality_compounder_durable_504d_jerk_v026_signal,
    f33qc_f33_quality_compounder_durable_504d_jerk_v027_signal,
    f33qc_f33_quality_compounder_hurdle_252d_jerk_v028_signal,
    f33qc_f33_quality_compounder_hurdle_252d_jerk_v029_signal,
    f33qc_f33_quality_compounder_hurdle_252d_jerk_v030_signal,
    f33qc_f33_quality_compounder_econprofit_504d_jerk_v031_signal,
    f33qc_f33_quality_compounder_econprofit_504d_jerk_v032_signal,
    f33qc_f33_quality_compounder_econprofit_504d_jerk_v033_signal,
    f33qc_f33_quality_compounder_moat_252d_jerk_v034_signal,
    f33qc_f33_quality_compounder_moat_252d_jerk_v035_signal,
    f33qc_f33_quality_compounder_moat_252d_jerk_v036_signal,
    f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v037_signal,
    f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v038_signal,
    f33qc_f33_quality_compounder_netmgnroic_252d_jerk_v039_signal,
    f33qc_f33_quality_compounder_roeroic_252d_jerk_v040_signal,
    f33qc_f33_quality_compounder_roeroic_252d_jerk_v041_signal,
    f33qc_f33_quality_compounder_roeroic_252d_jerk_v042_signal,
    f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v043_signal,
    f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v044_signal,
    f33qc_f33_quality_compounder_fcfconvroic_252d_jerk_v045_signal,
    f33qc_f33_quality_compounder_revpsroic_504d_jerk_v046_signal,
    f33qc_f33_quality_compounder_revpsroic_504d_jerk_v047_signal,
    f33qc_f33_quality_compounder_revpsroic_504d_jerk_v048_signal,
    f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v049_signal,
    f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v050_signal,
    f33qc_f33_quality_compounder_bvpsroic_504d_jerk_v051_signal,
    f33qc_f33_quality_compounder_epsroic_504d_jerk_v052_signal,
    f33qc_f33_quality_compounder_epsroic_504d_jerk_v053_signal,
    f33qc_f33_quality_compounder_epsroic_504d_jerk_v054_signal,
    f33qc_f33_quality_compounder_cashdupont_252d_jerk_v055_signal,
    f33qc_f33_quality_compounder_cashdupont_252d_jerk_v056_signal,
    f33qc_f33_quality_compounder_cashdupont_252d_jerk_v057_signal,
    f33qc_f33_quality_compounder_sustgrow_252d_jerk_v058_signal,
    f33qc_f33_quality_compounder_sustgrow_252d_jerk_v059_signal,
    f33qc_f33_quality_compounder_sustgrow_252d_jerk_v060_signal,
    f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v061_signal,
    f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v062_signal,
    f33qc_f33_quality_compounder_reinvgrow_504d_jerk_v063_signal,
    f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v064_signal,
    f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v065_signal,
    f33qc_f33_quality_compounder_fcfmgngrow_504d_jerk_v066_signal,
    f33qc_f33_quality_compounder_buybackcap_252d_jerk_v067_signal,
    f33qc_f33_quality_compounder_buybackcap_252d_jerk_v068_signal,
    f33qc_f33_quality_compounder_buybackcap_252d_jerk_v069_signal,
    f33qc_f33_quality_compounder_selffund_504d_jerk_v070_signal,
    f33qc_f33_quality_compounder_selffund_504d_jerk_v071_signal,
    f33qc_f33_quality_compounder_selffund_504d_jerk_v072_signal,
    f33qc_f33_quality_compounder_index4_252d_jerk_v073_signal,
    f33qc_f33_quality_compounder_index4_252d_jerk_v074_signal,
    f33qc_f33_quality_compounder_index4_252d_jerk_v075_signal,
    f33qc_f33_quality_compounder_durtriple_252d_jerk_v076_signal,
    f33qc_f33_quality_compounder_durtriple_252d_jerk_v077_signal,
    f33qc_f33_quality_compounder_durtriple_252d_jerk_v078_signal,
    f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v079_signal,
    f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v080_signal,
    f33qc_f33_quality_compounder_fcfroicdil_252d_jerk_v081_signal,
    f33qc_f33_quality_compounder_roicpershare_504d_jerk_v082_signal,
    f33qc_f33_quality_compounder_roicpershare_504d_jerk_v083_signal,
    f33qc_f33_quality_compounder_roicpershare_504d_jerk_v084_signal,
    f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v085_signal,
    f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v086_signal,
    f33qc_f33_quality_compounder_cashgenturn_252d_jerk_v087_signal,
    f33qc_f33_quality_compounder_blendroic_252d_jerk_v088_signal,
    f33qc_f33_quality_compounder_blendroic_252d_jerk_v089_signal,
    f33qc_f33_quality_compounder_blendroic_252d_jerk_v090_signal,
    f33qc_f33_quality_compounder_reinvqual_252d_jerk_v091_signal,
    f33qc_f33_quality_compounder_reinvqual_252d_jerk_v092_signal,
    f33qc_f33_quality_compounder_reinvqual_252d_jerk_v093_signal,
    f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v094_signal,
    f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v095_signal,
    f33qc_f33_quality_compounder_cashcompnet_252d_jerk_v096_signal,
    f33qc_f33_quality_compounder_triple_504d_jerk_v097_signal,
    f33qc_f33_quality_compounder_triple_504d_jerk_v098_signal,
    f33qc_f33_quality_compounder_triple_504d_jerk_v099_signal,
    f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v100_signal,
    f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v101_signal,
    f33qc_f33_quality_compounder_roiceqgrow_252d_jerk_v102_signal,
    f33qc_f33_quality_compounder_harmret_252d_jerk_v103_signal,
    f33qc_f33_quality_compounder_harmret_252d_jerk_v104_signal,
    f33qc_f33_quality_compounder_harmret_252d_jerk_v105_signal,
    f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v106_signal,
    f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v107_signal,
    f33qc_f33_quality_compounder_fcfeqturn_252d_jerk_v108_signal,
    f33qc_f33_quality_compounder_ownerret_252d_jerk_v109_signal,
    f33qc_f33_quality_compounder_ownerret_252d_jerk_v110_signal,
    f33qc_f33_quality_compounder_ownerret_252d_jerk_v111_signal,
    f33qc_f33_quality_compounder_valuecreate_252d_jerk_v112_signal,
    f33qc_f33_quality_compounder_valuecreate_252d_jerk_v113_signal,
    f33qc_f33_quality_compounder_valuecreate_252d_jerk_v114_signal,
    f33qc_f33_quality_compounder_roepershare_504d_jerk_v115_signal,
    f33qc_f33_quality_compounder_roepershare_504d_jerk_v116_signal,
    f33qc_f33_quality_compounder_roepershare_504d_jerk_v117_signal,
    f33qc_f33_quality_compounder_cashqual_252d_jerk_v118_signal,
    f33qc_f33_quality_compounder_cashqual_252d_jerk_v119_signal,
    f33qc_f33_quality_compounder_cashqual_252d_jerk_v120_signal,
    f33qc_f33_quality_compounder_regimereinv_252d_jerk_v121_signal,
    f33qc_f33_quality_compounder_regimereinv_252d_jerk_v122_signal,
    f33qc_f33_quality_compounder_regimereinv_252d_jerk_v123_signal,
    f33qc_f33_quality_compounder_epmargin_252d_jerk_v124_signal,
    f33qc_f33_quality_compounder_epmargin_252d_jerk_v125_signal,
    f33qc_f33_quality_compounder_epmargin_252d_jerk_v126_signal,
    f33qc_f33_quality_compounder_richnet_252d_jerk_v127_signal,
    f33qc_f33_quality_compounder_richnet_252d_jerk_v128_signal,
    f33qc_f33_quality_compounder_richnet_252d_jerk_v129_signal,
    f33qc_f33_quality_compounder_grandscore_504d_jerk_v130_signal,
    f33qc_f33_quality_compounder_grandscore_504d_jerk_v131_signal,
    f33qc_f33_quality_compounder_grandscore_504d_jerk_v132_signal,
    f33qc_f33_quality_compounder_convexcomp_252d_jerk_v133_signal,
    f33qc_f33_quality_compounder_convexcomp_252d_jerk_v134_signal,
    f33qc_f33_quality_compounder_convexcomp_252d_jerk_v135_signal,
    f33qc_f33_quality_compounder_intfund_252d_jerk_v136_signal,
    f33qc_f33_quality_compounder_intfund_252d_jerk_v137_signal,
    f33qc_f33_quality_compounder_intfund_252d_jerk_v138_signal,
    f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v139_signal,
    f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v140_signal,
    f33qc_f33_quality_compounder_steadyreinv_252d_jerk_v141_signal,
    f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v142_signal,
    f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v143_signal,
    f33qc_f33_quality_compounder_fcffundgrow_504d_jerk_v144_signal,
    f33qc_f33_quality_compounder_roicconv_252d_jerk_v145_signal,
    f33qc_f33_quality_compounder_roicconv_252d_jerk_v146_signal,
    f33qc_f33_quality_compounder_roicconv_252d_jerk_v147_signal,
    f33qc_f33_quality_compounder_capliteret_252d_jerk_v148_signal,
    f33qc_f33_quality_compounder_capliteret_252d_jerk_v149_signal,
    f33qc_f33_quality_compounder_capliteret_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_QUALITY_COMPOUNDER_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    n = 1500
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    roic = _fund(101, base=0.15, drift=0.01, vol=0.20, allow_neg=True).rename("roic")
    fcf = _fund(102, base=5e7, drift=0.02, vol=0.06, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=1e8, drift=0.005, vol=0.02).rename("sharesbas")
    revenue = _fund(104, base=5e8, drift=0.02, vol=0.04).rename("revenue")
    equity = _fund(105, base=4e8, drift=0.015, vol=0.04).rename("equity")
    netinc = _fund(106, base=6e7, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "revenue": revenue, "equity": equity, "netinc": netinc}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f33_quality_compounder_3rd_derivatives_001_150_claude: %d features pass" % n_features)
