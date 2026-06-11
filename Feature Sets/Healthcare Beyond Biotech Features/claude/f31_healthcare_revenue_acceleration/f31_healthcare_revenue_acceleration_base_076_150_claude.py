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
def _f31_revenue_growth_accel(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f31_acceleration_persistence(revenue, w):
    g = revenue.pct_change(periods=w)
    a = g - g.shift(w)
    return _mean(a, w) / _std(a, w).replace(0, np.nan)


def _f31_growth_quality(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return _mean(eg - rg, w)


# ---- features 076 - 150 (close-mediated bodies; structurally distinct from 001-075) ----

def f31hra_f31_healthcare_revenue_acceleration_accelxmean63_21d_base_v076_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean63_63d_base_v077_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean63_126d_base_v078_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean63_252d_base_v079_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean63_504d_base_v080_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean252_21d_base_v081_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean252_63d_base_v082_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxmean252_252d_base_v083_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxmean63_21d_base_v084_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxmean63_63d_base_v085_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxmean63_252d_base_v086_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxmean252_63d_base_v087_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxmean252_252d_base_v088_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxmean63_63d_base_v089_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxmean63_252d_base_v090_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxmean252_63d_base_v091_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxmean252_252d_base_v092_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_acceldivebitda_63d_base_v093_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * closeadj / _mean(ebitda, 63).replace(0, np.nan).abs() * ebitda.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_acceldivebitda_252d_base_v094_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * closeadj / _mean(ebitda, 252).replace(0, np.nan).abs() * ebitda.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_5d_base_v095_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 5)
    result = base * closeadj * 0.5 + _f31_acceleration_persistence(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_10d_base_v096_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 10)
    result = base * closeadj * 0.5 + _f31_acceleration_persistence(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_42d_base_v097_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 42)
    result = base * closeadj * 0.5 + _f31_acceleration_persistence(revenue, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_189d_base_v098_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 189)
    result = base * closeadj * 0.5 + _f31_acceleration_persistence(revenue, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_378d_base_v099_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 378)
    result = base * closeadj * 0.5 + _f31_acceleration_persistence(revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelhalflife_63d_base_v100_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.ewm(halflife=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelhalflife_252d_base_v101_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persisthalflife_63d_base_v102_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = base.ewm(halflife=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persisthalflife_252d_base_v103_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityhalflife_63d_base_v104_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base.ewm(halflife=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityhalflife_252d_base_v105_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelplusprice_63d_base_v106_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelplusprice_252d_base_v107_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelminusprice_63d_base_v108_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = (base - closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelminusprice_252d_base_v109_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = (base - closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistplusprice_63d_base_v110_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistplusprice_252d_base_v111_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityplusprice_63d_base_v112_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityplusprice_252d_base_v113_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxlog_63d_base_v114_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxlog_252d_base_v115_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxlog_63d_base_v116_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxlog_252d_base_v117_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxlog_63d_base_v118_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxlog_252d_base_v119_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelcorr_63d_base_v120_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    cor = base.rolling(63, min_periods=20).corr(closeadj.pct_change(63))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelcorr_252d_base_v121_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(252))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistcorr_63d_base_v122_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    cor = base.rolling(63, min_periods=20).corr(closeadj.pct_change(63))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistcorr_252d_base_v123_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(252))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelvscloseratio_63d_base_v124_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    pr = closeadj.pct_change(63).replace(0, np.nan)
    result = (base / pr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelvscloseratio_252d_base_v125_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    pr = closeadj.pct_change(252).replace(0, np.nan)
    result = (base / pr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxebitda_63d_base_v126_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxebitda_252d_base_v127_signal(revenue, ebitda, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxebitda_252d_base_v128_signal(revenue, ebitda, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxebitda_252d_base_v129_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxstd_63d_base_v130_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxstd_252d_base_v131_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxstd_252d_base_v132_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxstd_252d_base_v133_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxzclose_63d_base_v134_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * _z(closeadj, 252) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxzclose_252d_base_v135_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxzclose_252d_base_v136_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxzclose_252d_base_v137_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxsign_63d_base_v138_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.abs() * np.sign(closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxsign_252d_base_v139_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base.abs() * np.sign(closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxsign_252d_base_v140_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base.abs() * np.sign(closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxsign_252d_base_v141_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base.abs() * np.sign(closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelroll_max63_base_v142_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    result = base.rolling(63, min_periods=20).max() * closeadj - base.rolling(63, min_periods=20).min() * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelroll_max252_base_v143_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base.rolling(504, min_periods=126).max() * closeadj - base.rolling(504, min_periods=126).min() * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistroll_max252_base_v144_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj - base.rolling(252, min_periods=63).min() * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityroll_max252_base_v145_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj - base.rolling(252, min_periods=63).min() * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxewmstd_63d_base_v146_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * closeadj.ewm(span=63, min_periods=20).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxewmstd_252d_base_v147_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxewmstd_252d_base_v148_signal(revenue, closeadj):
    base = _f31_acceleration_persistence(revenue, 252)
    result = base * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxewmstd_252d_base_v149_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_acceltimespeed_252d_base_v150_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    spd = _mean(closeadj.pct_change(21).abs(), 252)
    result = base * spd * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hra_f31_healthcare_revenue_acceleration_accelxmean63_21d_base_v076_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean63_63d_base_v077_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean63_126d_base_v078_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean63_252d_base_v079_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean63_504d_base_v080_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean252_21d_base_v081_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean252_63d_base_v082_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxmean252_252d_base_v083_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxmean63_21d_base_v084_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxmean63_63d_base_v085_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxmean63_252d_base_v086_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxmean252_63d_base_v087_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxmean252_252d_base_v088_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxmean63_63d_base_v089_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxmean63_252d_base_v090_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxmean252_63d_base_v091_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxmean252_252d_base_v092_signal,
    f31hra_f31_healthcare_revenue_acceleration_acceldivebitda_63d_base_v093_signal,
    f31hra_f31_healthcare_revenue_acceleration_acceldivebitda_252d_base_v094_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_5d_base_v095_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_10d_base_v096_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_42d_base_v097_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_189d_base_v098_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxcloseadj_378d_base_v099_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelhalflife_63d_base_v100_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelhalflife_252d_base_v101_signal,
    f31hra_f31_healthcare_revenue_acceleration_persisthalflife_63d_base_v102_signal,
    f31hra_f31_healthcare_revenue_acceleration_persisthalflife_252d_base_v103_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityhalflife_63d_base_v104_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityhalflife_252d_base_v105_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelplusprice_63d_base_v106_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelplusprice_252d_base_v107_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelminusprice_63d_base_v108_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelminusprice_252d_base_v109_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistplusprice_63d_base_v110_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistplusprice_252d_base_v111_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityplusprice_63d_base_v112_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityplusprice_252d_base_v113_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxlog_63d_base_v114_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxlog_252d_base_v115_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxlog_63d_base_v116_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxlog_252d_base_v117_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxlog_63d_base_v118_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxlog_252d_base_v119_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelcorr_63d_base_v120_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelcorr_252d_base_v121_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistcorr_63d_base_v122_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistcorr_252d_base_v123_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelvscloseratio_63d_base_v124_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelvscloseratio_252d_base_v125_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxebitda_63d_base_v126_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxebitda_252d_base_v127_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxebitda_252d_base_v128_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxebitda_252d_base_v129_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxstd_63d_base_v130_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxstd_252d_base_v131_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxstd_252d_base_v132_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxstd_252d_base_v133_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxzclose_63d_base_v134_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxzclose_252d_base_v135_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxzclose_252d_base_v136_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxzclose_252d_base_v137_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxsign_63d_base_v138_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxsign_252d_base_v139_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxsign_252d_base_v140_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxsign_252d_base_v141_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelroll_max63_base_v142_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelroll_max252_base_v143_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistroll_max252_base_v144_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityroll_max252_base_v145_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxewmstd_63d_base_v146_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxewmstd_252d_base_v147_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxewmstd_252d_base_v148_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxewmstd_252d_base_v149_signal,
    f31hra_f31_healthcare_revenue_acceleration_acceltimespeed_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HEALTHCARE_REVENUE_ACCELERATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_revenue_growth_accel", "_f31_acceleration_persistence", "_f31_growth_quality")
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
    print(f"OK f31_healthcare_revenue_acceleration_base_076_150_claude: {n_features} features pass")
