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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f42_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f42_property_capex_burn(capex, revenue, w):
    r = capex / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f42_capex_quality(capex, depamor, w):
    r = capex / depamor.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f42rci_f42_resort_casino_capex_intensity_c2pdiff_63m252_base_v076_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 63) - _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiff_252m504_base_v077_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 252) - _mean(r, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiff_21m252_base_v078_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 21) - _mean(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prat_63v252_base_v079_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 63) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prat_21v63_base_v080_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 21) / _mean(r, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prat_252v504_base_v081_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 252) / _mean(r, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prat_126v252_base_v082_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 126) / _mean(r, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burndiff_21m63_base_v083_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 21)
    l = _f42_property_capex_burn(capex, revenue, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burndiff_63m252_base_v084_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 63)
    l = _f42_property_capex_burn(capex, revenue, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burndiff_252m504_base_v085_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 252)
    l = _f42_property_capex_burn(capex, revenue, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrat_63v252_base_v086_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 63)
    l = _f42_property_capex_burn(capex, revenue, 252).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrat_21v63_base_v087_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 21)
    l = _f42_property_capex_burn(capex, revenue, 63).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrat_252v504_base_v088_signal(capex, revenue, closeadj):
    s = _f42_property_capex_burn(capex, revenue, 252)
    l = _f42_property_capex_burn(capex, revenue, 504).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnz_63o252_base_v089_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = _z(b, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnz_252o504_base_v090_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252)
    result = _z(b, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnz_21o126_base_v091_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 21)
    result = _z(b, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualdiff_21m63_base_v092_signal(capex, depamor, closeadj):
    s = _f42_capex_quality(capex, depamor, 21)
    l = _f42_capex_quality(capex, depamor, 63)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualdiff_63m252_base_v093_signal(capex, depamor, closeadj):
    s = _f42_capex_quality(capex, depamor, 63)
    l = _f42_capex_quality(capex, depamor, 252)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualdiff_252m504_base_v094_signal(capex, depamor, closeadj):
    s = _f42_capex_quality(capex, depamor, 252)
    l = _f42_capex_quality(capex, depamor, 504)
    result = (s - l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualrat_63v252_base_v095_signal(capex, depamor, closeadj):
    s = _f42_capex_quality(capex, depamor, 63)
    l = _f42_capex_quality(capex, depamor, 252).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualrat_21v63_base_v096_signal(capex, depamor, closeadj):
    s = _f42_capex_quality(capex, depamor, 21)
    l = _f42_capex_quality(capex, depamor, 63).replace(0, np.nan)
    result = (s / l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxburn_21d_base_v097_signal(capex, ppnenet, revenue, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 21)
    result = _mean(r, 21) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxburn_63d_base_v098_signal(capex, ppnenet, revenue, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = _mean(r, 63) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxburn_126d_base_v099_signal(capex, ppnenet, revenue, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 126)
    result = _mean(r, 126) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxburn_252d_base_v100_signal(capex, ppnenet, revenue, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 252)
    result = _mean(r, 252) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxqual_21d_base_v101_signal(capex, ppnenet, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    q = _f42_capex_quality(capex, depamor, 21)
    result = _mean(r, 21) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxqual_63d_base_v102_signal(capex, ppnenet, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    q = _f42_capex_quality(capex, depamor, 63)
    result = _mean(r, 63) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxqual_252d_base_v103_signal(capex, ppnenet, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    q = _f42_capex_quality(capex, depamor, 252)
    result = _mean(r, 252) * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxdv_21d_base_v104_signal(capex, ppnenet, closeadj, volume):
    r = _f42_capex_to_ppe(capex, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxdv_63d_base_v105_signal(capex, ppnenet, closeadj, volume):
    r = _f42_capex_to_ppe(capex, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxdv_252d_base_v106_signal(capex, ppnenet, closeadj, volume):
    r = _f42_capex_to_ppe(capex, ppnenet)
    dv = closeadj * volume
    result = _mean(r, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2plogdiff_21d_base_v107_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet).abs().replace(0, np.nan)
    result = np.log(r).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2plogdiff_63d_base_v108_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet).abs().replace(0, np.nan)
    result = np.log(r).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2plogdiff_252d_base_v109_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet).abs().replace(0, np.nan)
    result = np.log(r).diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnlogdiff_21d_base_v110_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 21).abs().replace(0, np.nan)
    result = np.log(b).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnlogdiff_63d_base_v111_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63).abs().replace(0, np.nan)
    result = np.log(b).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnlogdiff_252d_base_v112_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252).abs().replace(0, np.nan)
    result = np.log(b).diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_composite_63d_base_v113_signal(capex, ppnenet, revenue, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 63)
    q = _f42_capex_quality(capex, depamor, 63)
    result = (_mean(r, 63) + b + q) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_composite_126d_base_v114_signal(capex, ppnenet, revenue, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 126)
    q = _f42_capex_quality(capex, depamor, 126)
    result = (_mean(r, 126) + b + q) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_composite_252d_base_v115_signal(capex, ppnenet, revenue, depamor, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    b = _f42_property_capex_burn(capex, revenue, 252)
    q = _f42_capex_quality(capex, depamor, 252)
    result = (_mean(r, 252) + b + q) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnsq_63d_base_v116_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    m = _mean(b, 63)
    result = ((b - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnsq_252d_base_v117_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252)
    m = _mean(b, 252)
    result = ((b - m) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualstd_63d_base_v118_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 63)
    result = _std(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualstd_252d_base_v119_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 252)
    result = _std(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualstd_504d_base_v120_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 504)
    result = _std(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_42d_base_v121_signal(capex, revenue, volume, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 42)
    result = b * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_126d_base_v122_signal(capex, revenue, volume, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 126)
    result = b * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_378d_base_v123_signal(capex, revenue, volume, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 378)
    result = b * volume * (closeadj / closeadj.mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prank_63d_base_v124_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = r.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prank_126d_base_v125_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = r.rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prank_252d_base_v126_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = r.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2prank_504d_base_v127_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = r.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrank_63d_base_v128_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = b.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrank_252d_base_v129_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252)
    result = b.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnrank_504d_base_v130_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 504)
    result = b.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualrank_63d_base_v131_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 63)
    result = q.rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualrank_252d_base_v132_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 252)
    result = q.rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualrank_504d_base_v133_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 504)
    result = q.rolling(504, min_periods=max(1, 504//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pemadiff_21m63_base_v134_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_ema(r, 21) - _ema(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pemadiff_63m252_base_v135_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_ema(r, 63) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pemadiff_126m252_base_v136_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_ema(r, 126) - _ema(r, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnemadiff_21m63_base_v137_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = (_ema(b, 21) - _ema(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnemadiff_63m252_base_v138_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = (_ema(b, 63) - _ema(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pminmax_63d_base_v139_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    hi = r.rolling(63, min_periods=max(1, 63//2)).max()
    lo = r.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pminmax_252d_base_v140_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    hi = r.rolling(252, min_periods=max(1, 252//2)).max()
    lo = r.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((r - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnminmax_63d_base_v141_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    hi = b.rolling(63, min_periods=max(1, 63//2)).max()
    lo = b.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((b - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnminmax_252d_base_v142_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252)
    hi = b.rolling(252, min_periods=max(1, 252//2)).max()
    lo = b.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((b - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualminmax_63d_base_v143_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 63)
    hi = q.rolling(63, min_periods=max(1, 63//2)).max()
    lo = q.rolling(63, min_periods=max(1, 63//2)).min()
    result = ((q - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualminmax_252d_base_v144_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 252)
    hi = q.rolling(252, min_periods=max(1, 252//2)).max()
    lo = q.rolling(252, min_periods=max(1, 252//2)).min()
    result = ((q - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxhlr_21d_base_v145_signal(capex, ppnenet, high, low):
    r = _f42_capex_to_ppe(capex, ppnenet)
    rng = (high - low).rolling(21, min_periods=max(1, 21//2)).mean()
    result = _mean(r, 21) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxhlr_63d_base_v146_signal(capex, ppnenet, high, low):
    r = _f42_capex_to_ppe(capex, ppnenet)
    rng = (high - low).rolling(63, min_periods=max(1, 63//2)).mean()
    result = _mean(r, 63) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pxhlr_252d_base_v147_signal(capex, ppnenet, high, low):
    r = _f42_capex_to_ppe(capex, ppnenet)
    rng = (high - low).rolling(252, min_periods=max(1, 252//2)).mean()
    result = _mean(r, 252) * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_21d_base_v148_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = np.sign(r.diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_63d_base_v149_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = np.sign(r.diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_252d_base_v150_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = np.sign(r.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42rci_f42_resort_casino_capex_intensity_c2pdiff_63m252_base_v076_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiff_252m504_base_v077_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiff_21m252_base_v078_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prat_63v252_base_v079_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prat_21v63_base_v080_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prat_252v504_base_v081_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prat_126v252_base_v082_signal,
    f42rci_f42_resort_casino_capex_intensity_burndiff_21m63_base_v083_signal,
    f42rci_f42_resort_casino_capex_intensity_burndiff_63m252_base_v084_signal,
    f42rci_f42_resort_casino_capex_intensity_burndiff_252m504_base_v085_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrat_63v252_base_v086_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrat_21v63_base_v087_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrat_252v504_base_v088_signal,
    f42rci_f42_resort_casino_capex_intensity_burnz_63o252_base_v089_signal,
    f42rci_f42_resort_casino_capex_intensity_burnz_252o504_base_v090_signal,
    f42rci_f42_resort_casino_capex_intensity_burnz_21o126_base_v091_signal,
    f42rci_f42_resort_casino_capex_intensity_qualdiff_21m63_base_v092_signal,
    f42rci_f42_resort_casino_capex_intensity_qualdiff_63m252_base_v093_signal,
    f42rci_f42_resort_casino_capex_intensity_qualdiff_252m504_base_v094_signal,
    f42rci_f42_resort_casino_capex_intensity_qualrat_63v252_base_v095_signal,
    f42rci_f42_resort_casino_capex_intensity_qualrat_21v63_base_v096_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxburn_21d_base_v097_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxburn_63d_base_v098_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxburn_126d_base_v099_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxburn_252d_base_v100_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxqual_21d_base_v101_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxqual_63d_base_v102_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxqual_252d_base_v103_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxdv_21d_base_v104_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxdv_63d_base_v105_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxdv_252d_base_v106_signal,
    f42rci_f42_resort_casino_capex_intensity_c2plogdiff_21d_base_v107_signal,
    f42rci_f42_resort_casino_capex_intensity_c2plogdiff_63d_base_v108_signal,
    f42rci_f42_resort_casino_capex_intensity_c2plogdiff_252d_base_v109_signal,
    f42rci_f42_resort_casino_capex_intensity_burnlogdiff_21d_base_v110_signal,
    f42rci_f42_resort_casino_capex_intensity_burnlogdiff_63d_base_v111_signal,
    f42rci_f42_resort_casino_capex_intensity_burnlogdiff_252d_base_v112_signal,
    f42rci_f42_resort_casino_capex_intensity_composite_63d_base_v113_signal,
    f42rci_f42_resort_casino_capex_intensity_composite_126d_base_v114_signal,
    f42rci_f42_resort_casino_capex_intensity_composite_252d_base_v115_signal,
    f42rci_f42_resort_casino_capex_intensity_burnsq_63d_base_v116_signal,
    f42rci_f42_resort_casino_capex_intensity_burnsq_252d_base_v117_signal,
    f42rci_f42_resort_casino_capex_intensity_qualstd_63d_base_v118_signal,
    f42rci_f42_resort_casino_capex_intensity_qualstd_252d_base_v119_signal,
    f42rci_f42_resort_casino_capex_intensity_qualstd_504d_base_v120_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_42d_base_v121_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_126d_base_v122_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvolnorm_378d_base_v123_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prank_63d_base_v124_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prank_126d_base_v125_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prank_252d_base_v126_signal,
    f42rci_f42_resort_casino_capex_intensity_c2prank_504d_base_v127_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrank_63d_base_v128_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrank_252d_base_v129_signal,
    f42rci_f42_resort_casino_capex_intensity_burnrank_504d_base_v130_signal,
    f42rci_f42_resort_casino_capex_intensity_qualrank_63d_base_v131_signal,
    f42rci_f42_resort_casino_capex_intensity_qualrank_252d_base_v132_signal,
    f42rci_f42_resort_casino_capex_intensity_qualrank_504d_base_v133_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pemadiff_21m63_base_v134_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pemadiff_63m252_base_v135_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pemadiff_126m252_base_v136_signal,
    f42rci_f42_resort_casino_capex_intensity_burnemadiff_21m63_base_v137_signal,
    f42rci_f42_resort_casino_capex_intensity_burnemadiff_63m252_base_v138_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pminmax_63d_base_v139_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pminmax_252d_base_v140_signal,
    f42rci_f42_resort_casino_capex_intensity_burnminmax_63d_base_v141_signal,
    f42rci_f42_resort_casino_capex_intensity_burnminmax_252d_base_v142_signal,
    f42rci_f42_resort_casino_capex_intensity_qualminmax_63d_base_v143_signal,
    f42rci_f42_resort_casino_capex_intensity_qualminmax_252d_base_v144_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxhlr_21d_base_v145_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxhlr_63d_base_v146_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pxhlr_252d_base_v147_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_21d_base_v148_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_63d_base_v149_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiffsign_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_RESORT_CASINO_CAPEX_INTENSITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "capex": capex, "ppnenet": ppnenet, "revenue": revenue, "depamor": depamor }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f42_capex_to_ppe", "_f42_property_capex_burn", "_f42_capex_quality")
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
    print(f"OK resort_casino_capex_intensity_base_076_150_claude: {n_features} features pass")
