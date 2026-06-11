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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f24_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan) * 365.0


def _f24_receivables_growth_gap(receivables, revenue, w):
    rg = receivables.pct_change(periods=w)
    sg = revenue.pct_change(periods=w)
    return rg - sg


def _f24_collection_efficiency(receivables, revenue, w):
    dso = receivables / revenue.replace(0, np.nan) * 365.0
    m = dso.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = dso.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return -((dso - m) / sd)

# ===== features =====

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_315d_base_v076_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = _mean(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_378d_base_v077_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_504d_base_v078_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_5d_base_v079_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_10d_base_v080_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_21d_base_v081_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_42d_base_v082_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_63d_base_v083_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_84d_base_v084_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_126d_base_v085_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_168d_base_v086_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_189d_base_v087_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_252d_base_v088_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_315d_base_v089_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_378d_base_v090_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_504d_base_v091_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_5d_base_v092_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_10d_base_v093_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_21d_base_v094_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_42d_base_v095_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_63d_base_v096_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_84d_base_v097_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_126d_base_v098_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_168d_base_v099_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_189d_base_v100_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_252d_base_v101_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_315d_base_v102_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_378d_base_v103_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_504d_base_v104_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_5d_base_v105_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_10d_base_v106_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_21d_base_v107_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_42d_base_v108_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_63d_base_v109_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_84d_base_v110_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_126d_base_v111_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_168d_base_v112_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_189d_base_v113_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_252d_base_v114_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_315d_base_v115_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_378d_base_v116_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_504d_base_v117_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_5d_base_v118_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_10d_base_v119_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_21d_base_v120_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_42d_base_v121_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_63d_base_v122_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_84d_base_v123_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_126d_base_v124_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_168d_base_v125_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_189d_base_v126_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_252d_base_v127_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_315d_base_v128_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_378d_base_v129_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_504d_base_v130_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_5d_base_v131_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_10d_base_v132_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_21d_base_v133_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_42d_base_v134_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_63d_base_v135_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_84d_base_v136_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_126d_base_v137_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_168d_base_v138_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_189d_base_v139_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_252d_base_v140_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_315d_base_v141_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_378d_base_v142_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_504d_base_v143_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_5d_base_v144_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=5)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_10d_base_v145_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=10)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_21d_base_v146_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=21)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_42d_base_v147_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=42)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_63d_base_v148_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=63)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_84d_base_v149_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=84)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_126d_base_v150_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=126)
    result = base * rg * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_315d_base_v076_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_378d_base_v077_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_504d_base_v078_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_5d_base_v079_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_10d_base_v080_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_21d_base_v081_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_42d_base_v082_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_63d_base_v083_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_84d_base_v084_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_126d_base_v085_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_168d_base_v086_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_189d_base_v087_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_252d_base_v088_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_315d_base_v089_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_378d_base_v090_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_504d_base_v091_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_5d_base_v092_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_10d_base_v093_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_21d_base_v094_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_42d_base_v095_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_63d_base_v096_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_84d_base_v097_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_126d_base_v098_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_168d_base_v099_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_189d_base_v100_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_252d_base_v101_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_315d_base_v102_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_378d_base_v103_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_504d_base_v104_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_5d_base_v105_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_10d_base_v106_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_21d_base_v107_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_42d_base_v108_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_63d_base_v109_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_84d_base_v110_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_126d_base_v111_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_168d_base_v112_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_189d_base_v113_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_252d_base_v114_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_315d_base_v115_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_378d_base_v116_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_504d_base_v117_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_5d_base_v118_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_10d_base_v119_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_21d_base_v120_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_42d_base_v121_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_63d_base_v122_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_84d_base_v123_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_126d_base_v124_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_168d_base_v125_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_189d_base_v126_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_252d_base_v127_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_315d_base_v128_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_378d_base_v129_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_504d_base_v130_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_5d_base_v131_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_10d_base_v132_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_21d_base_v133_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_42d_base_v134_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_63d_base_v135_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_84d_base_v136_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_126d_base_v137_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_168d_base_v138_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_189d_base_v139_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_252d_base_v140_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_315d_base_v141_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_378d_base_v142_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_504d_base_v143_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_5d_base_v144_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_10d_base_v145_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_21d_base_v146_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_42d_base_v147_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_63d_base_v148_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_84d_base_v149_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_RECEIVABLES_QUALITY_CONSUMER_REGISTRY_076_150 = REGISTRY


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
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "receivables": receivables,
        "revenue": revenue,
        "closeadj": closeadj,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_dso", "_f24_receivables_growth_gap", "_f24_collection_efficiency",)
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
    print(f"OK f24_receivables_quality_consumer_base_076_150_claude: {n_features} features pass")
