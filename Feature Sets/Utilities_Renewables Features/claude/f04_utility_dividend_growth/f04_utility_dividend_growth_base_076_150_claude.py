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


def _f04_dps_growth(dps, w):
    return dps.pct_change(periods=w)


def _f04_dividend_compound(dps, w):
    sm = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return dps / sm.replace(0, np.nan)


def _f04_dividend_coverage(dps, eps, w):
    cov = eps / dps.replace(0, np.nan)
    return cov.rolling(w, min_periods=max(1, w // 2)).mean()


# Coverage × volume z × close
def f04udg_f04_utility_dividend_growth_coveragexvolz_252d_base_v076_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexvolz_63d_base_v077_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × volume z
def f04udg_f04_utility_dividend_growth_compoundxvolz_252d_base_v078_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 252)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxvolz_63d_base_v079_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 63)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage cross
def f04udg_f04_utility_dividend_growth_coveragecross_21_252_base_v080_signal(dps, eps, closeadj):
    short = _f04_dividend_coverage(dps, eps, 21)
    long = _f04_dividend_coverage(dps, eps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragecross_63_252_base_v081_signal(dps, eps, closeadj):
    short = _f04_dividend_coverage(dps, eps, 63)
    long = _f04_dividend_coverage(dps, eps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound cross
def f04udg_f04_utility_dividend_growth_compoundcross_21_252_base_v082_signal(dps, closeadj):
    short = _f04_dividend_compound(dps, 21)
    long = _f04_dividend_compound(dps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundcross_63_252_base_v083_signal(dps, closeadj):
    short = _f04_dividend_compound(dps, 63)
    long = _f04_dividend_compound(dps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS-growth cross
def f04udg_f04_utility_dividend_growth_dpsgrowthcross_21_252_base_v084_signal(dps, closeadj):
    short = _f04_dps_growth(dps, 21)
    long = _f04_dps_growth(dps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthcross_63_252_base_v085_signal(dps, closeadj):
    short = _f04_dps_growth(dps, 63)
    long = _f04_dps_growth(dps, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × inv close × scale
def f04udg_f04_utility_dividend_growth_coveragexinvprice_252d_base_v086_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × inv close × scale
def f04udg_f04_utility_dividend_growth_compoundxinvprice_252d_base_v087_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × inv close × scale
def f04udg_f04_utility_dividend_growth_dpsgrowthxinvprice_252d_base_v088_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × log eps × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxepssize_252d_base_v089_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 252)
    s = np.log(eps.abs().replace(0, np.nan))
    result = g * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × log eps × close
def f04udg_f04_utility_dividend_growth_coveragexepssize_252d_base_v090_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    s = np.log(eps.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × log dps × close
def f04udg_f04_utility_dividend_growth_compoundxdpssize_252d_base_v091_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    s = np.log(dps.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × payout × close
def f04udg_f04_utility_dividend_growth_coveragexpayout_252d_base_v092_signal(dps, eps, payoutratio, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * _mean(payoutratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × payout × close
def f04udg_f04_utility_dividend_growth_compoundxpayout_252d_base_v093_signal(dps, payoutratio, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base * _mean(payoutratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × payout × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxpayout_252d_base_v094_signal(dps, payoutratio, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * _mean(payoutratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth sign × volume × close
def f04udg_f04_utility_dividend_growth_dpsgrowthsign_252d_base_v095_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    result = np.sign(g) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage sign × volume × close
def f04udg_f04_utility_dividend_growth_coveragesign_252d_base_v096_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = np.sign(base - _mean(base, 504)) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth abs × close
def f04udg_f04_utility_dividend_growth_dpsgrowthabs_252d_base_v097_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252).abs()
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound abs × close
def f04udg_f04_utility_dividend_growth_compoundabs_252d_base_v098_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = (base - 1.0).abs() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage cube × close
def f04udg_f04_utility_dividend_growth_coveragecube_252d_base_v099_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth cube × close
def f04udg_f04_utility_dividend_growth_dpsgrowthcube_252d_base_v100_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × DPS growth × close × ATR
def f04udg_f04_utility_dividend_growth_combocovxret_252d_base_v101_signal(dps, eps, closeadj, high, low):
    co = _f04_dividend_coverage(dps, eps, 252)
    g = _f04_dps_growth(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = co * g * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × DPS growth × ATR
def f04udg_f04_utility_dividend_growth_combocompxret_252d_base_v102_signal(dps, closeadj, high, low):
    c = _f04_dividend_compound(dps, 252)
    g = _f04_dps_growth(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = c * g * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × dollar volume
def f04udg_f04_utility_dividend_growth_coveragexdv_63d_base_v103_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 63)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexdv_252d_base_v104_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × dollar volume
def f04udg_f04_utility_dividend_growth_compoundxdv_63d_base_v105_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 63)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxdv_252d_base_v106_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × dollar volume
def f04udg_f04_utility_dividend_growth_dpsgrowthxdv_63d_base_v107_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 63)
    dv = closeadj * volume
    result = g * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxdv_252d_base_v108_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    dv = closeadj * volume
    result = g * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS log gradient × close
def f04udg_f04_utility_dividend_growth_dpsloggrad_63d_base_v109_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 63)
    result = np.log(dps.abs().replace(0, np.nan)).diff(21) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsloggrad_252d_base_v110_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 252)
    result = np.log(dps.abs().replace(0, np.nan)).diff(63) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × eps growth × close
def f04udg_f04_utility_dividend_growth_coveragexepsgrowth_252d_base_v111_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    epsg = eps.pct_change(252)
    result = base * epsg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × eps growth × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxepsgrowth_252d_base_v112_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 252)
    epsg = eps.pct_change(252)
    result = g * epsg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × eps growth × close
def f04udg_f04_utility_dividend_growth_compoundxepsgrowth_252d_base_v113_signal(dps, eps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    epsg = eps.pct_change(252)
    result = c * epsg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × close ema × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxcloseema_252d_base_v114_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    cm = closeadj.ewm(span=63, min_periods=21).mean()
    result = g * cm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × close ema × close
def f04udg_f04_utility_dividend_growth_coveragexcloseema_252d_base_v115_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    cm = closeadj.ewm(span=63, min_periods=21).mean()
    result = base * cm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × volume × ATR
def f04udg_f04_utility_dividend_growth_dpsgrowthxvolxatr_252d_base_v116_signal(dps, closeadj, volume, high, low):
    g = _f04_dps_growth(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = g * _mean(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × volume × ATR
def f04udg_f04_utility_dividend_growth_coveragexvolxatr_252d_base_v117_signal(dps, eps, closeadj, volume, high, low):
    base = _f04_dividend_coverage(dps, eps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * _mean(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × volume × ATR
def f04udg_f04_utility_dividend_growth_compoundxvolxatr_252d_base_v118_signal(dps, closeadj, volume, high, low):
    base = _f04_dividend_compound(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * _mean(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth acceleration × close
def f04udg_f04_utility_dividend_growth_dpsgrowthaccel_63d_base_v119_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = (g - g.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthaccel_252d_base_v120_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = (g - g.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage accel × close
def f04udg_f04_utility_dividend_growth_coverageaccel_63d_base_v121_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageaccel_252d_base_v122_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound accel × close
def f04udg_f04_utility_dividend_growth_compoundaccel_63d_base_v123_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundaccel_252d_base_v124_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × inverse close × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxinv_63d_base_v125_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = g * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × payout × ATR
def f04udg_f04_utility_dividend_growth_dpsxpayoutxatr_252d_base_v126_signal(dps, payoutratio, closeadj, high, low):
    g = _f04_dps_growth(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = g * _mean(payoutratio, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × payout × close
def f04udg_f04_utility_dividend_growth_covxpayout_63d_base_v127_signal(dps, eps, payoutratio, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = base * _mean(payoutratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × DPS × close (raw dividend dollar)
def f04udg_f04_utility_dividend_growth_covxdps_252d_base_v128_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × DPS × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxdps_252d_base_v129_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × DPS × close
def f04udg_f04_utility_dividend_growth_compoundxdps_252d_base_v130_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage rolling sum × close
def f04udg_f04_utility_dividend_growth_coveragesum_252d_base_v131_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound rolling sum × close
def f04udg_f04_utility_dividend_growth_compoundsum_252d_base_v132_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × payoutratio gap × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxpayoutgap_252d_base_v133_signal(dps, payoutratio, closeadj):
    g = _f04_dps_growth(dps, 252)
    pg = payoutratio - _mean(payoutratio, 252)
    result = g * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × payoutratio gap × close
def f04udg_f04_utility_dividend_growth_coveragexpayoutgap_252d_base_v134_signal(dps, eps, payoutratio, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    pg = payoutratio - _mean(payoutratio, 252)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage spread vs target × close
def f04udg_f04_utility_dividend_growth_coveragespread_252d_base_v135_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = (base - 2.0) * closeadj * _mean(base, 252) / _mean(base, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth spread vs target × close
def f04udg_f04_utility_dividend_growth_dpsgrowthspread_252d_base_v136_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = (g - 0.05) * closeadj * _mean(g, 252) / _mean(g, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × eps × close (dividend × earnings level)
def f04udg_f04_utility_dividend_growth_dpsgrowthxeps_252d_base_v137_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxeps_63d_base_v138_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = g * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × eps × close
def f04udg_f04_utility_dividend_growth_compoundxepsraw_252d_base_v139_signal(dps, eps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxepsraw_63d_base_v140_signal(dps, eps, closeadj):
    base = _f04_dividend_compound(dps, 63)
    result = base * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × DPS × ATR
def f04udg_f04_utility_dividend_growth_covxdpsxatr_252d_base_v141_signal(dps, eps, closeadj, high, low):
    base = _f04_dividend_coverage(dps, eps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * dps * atr
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth EMA × close (short span)
def f04udg_f04_utility_dividend_growth_dpsgrowthema_63d_base_v142_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = g.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage EMA × close (short)
def f04udg_f04_utility_dividend_growth_coverageema_63d_base_v143_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound EMA short × close
def f04udg_f04_utility_dividend_growth_compoundema_63d_base_v144_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × DPS × close × volume
def f04udg_f04_utility_dividend_growth_coverxdpsxvol_252d_base_v145_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * dps * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × DPS × volume × close
def f04udg_f04_utility_dividend_growth_growthxdpsxvol_252d_base_v146_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    result = g * dps * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × DPS × volume × close
def f04udg_f04_utility_dividend_growth_compoundxdpsxvol_252d_base_v147_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 252)
    result = base * dps * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage rank short × close
def f04udg_f04_utility_dividend_growth_coveragerank_63d_base_v148_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound rank short × close
def f04udg_f04_utility_dividend_growth_compoundrank_63d_base_v149_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth rank short × close
def f04udg_f04_utility_dividend_growth_dpsgrowthrank_63d_base_v150_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04udg_f04_utility_dividend_growth_coveragexvolz_252d_base_v076_signal,
    f04udg_f04_utility_dividend_growth_coveragexvolz_63d_base_v077_signal,
    f04udg_f04_utility_dividend_growth_compoundxvolz_252d_base_v078_signal,
    f04udg_f04_utility_dividend_growth_compoundxvolz_63d_base_v079_signal,
    f04udg_f04_utility_dividend_growth_coveragecross_21_252_base_v080_signal,
    f04udg_f04_utility_dividend_growth_coveragecross_63_252_base_v081_signal,
    f04udg_f04_utility_dividend_growth_compoundcross_21_252_base_v082_signal,
    f04udg_f04_utility_dividend_growth_compoundcross_63_252_base_v083_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthcross_21_252_base_v084_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthcross_63_252_base_v085_signal,
    f04udg_f04_utility_dividend_growth_coveragexinvprice_252d_base_v086_signal,
    f04udg_f04_utility_dividend_growth_compoundxinvprice_252d_base_v087_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxinvprice_252d_base_v088_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxepssize_252d_base_v089_signal,
    f04udg_f04_utility_dividend_growth_coveragexepssize_252d_base_v090_signal,
    f04udg_f04_utility_dividend_growth_compoundxdpssize_252d_base_v091_signal,
    f04udg_f04_utility_dividend_growth_coveragexpayout_252d_base_v092_signal,
    f04udg_f04_utility_dividend_growth_compoundxpayout_252d_base_v093_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxpayout_252d_base_v094_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsign_252d_base_v095_signal,
    f04udg_f04_utility_dividend_growth_coveragesign_252d_base_v096_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthabs_252d_base_v097_signal,
    f04udg_f04_utility_dividend_growth_compoundabs_252d_base_v098_signal,
    f04udg_f04_utility_dividend_growth_coveragecube_252d_base_v099_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthcube_252d_base_v100_signal,
    f04udg_f04_utility_dividend_growth_combocovxret_252d_base_v101_signal,
    f04udg_f04_utility_dividend_growth_combocompxret_252d_base_v102_signal,
    f04udg_f04_utility_dividend_growth_coveragexdv_63d_base_v103_signal,
    f04udg_f04_utility_dividend_growth_coveragexdv_252d_base_v104_signal,
    f04udg_f04_utility_dividend_growth_compoundxdv_63d_base_v105_signal,
    f04udg_f04_utility_dividend_growth_compoundxdv_252d_base_v106_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxdv_63d_base_v107_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxdv_252d_base_v108_signal,
    f04udg_f04_utility_dividend_growth_dpsloggrad_63d_base_v109_signal,
    f04udg_f04_utility_dividend_growth_dpsloggrad_252d_base_v110_signal,
    f04udg_f04_utility_dividend_growth_coveragexepsgrowth_252d_base_v111_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxepsgrowth_252d_base_v112_signal,
    f04udg_f04_utility_dividend_growth_compoundxepsgrowth_252d_base_v113_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxcloseema_252d_base_v114_signal,
    f04udg_f04_utility_dividend_growth_coveragexcloseema_252d_base_v115_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvolxatr_252d_base_v116_signal,
    f04udg_f04_utility_dividend_growth_coveragexvolxatr_252d_base_v117_signal,
    f04udg_f04_utility_dividend_growth_compoundxvolxatr_252d_base_v118_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthaccel_63d_base_v119_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthaccel_252d_base_v120_signal,
    f04udg_f04_utility_dividend_growth_coverageaccel_63d_base_v121_signal,
    f04udg_f04_utility_dividend_growth_coverageaccel_252d_base_v122_signal,
    f04udg_f04_utility_dividend_growth_compoundaccel_63d_base_v123_signal,
    f04udg_f04_utility_dividend_growth_compoundaccel_252d_base_v124_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxinv_63d_base_v125_signal,
    f04udg_f04_utility_dividend_growth_dpsxpayoutxatr_252d_base_v126_signal,
    f04udg_f04_utility_dividend_growth_covxpayout_63d_base_v127_signal,
    f04udg_f04_utility_dividend_growth_covxdps_252d_base_v128_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxdps_252d_base_v129_signal,
    f04udg_f04_utility_dividend_growth_compoundxdps_252d_base_v130_signal,
    f04udg_f04_utility_dividend_growth_coveragesum_252d_base_v131_signal,
    f04udg_f04_utility_dividend_growth_compoundsum_252d_base_v132_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxpayoutgap_252d_base_v133_signal,
    f04udg_f04_utility_dividend_growth_coveragexpayoutgap_252d_base_v134_signal,
    f04udg_f04_utility_dividend_growth_coveragespread_252d_base_v135_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthspread_252d_base_v136_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxeps_252d_base_v137_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxeps_63d_base_v138_signal,
    f04udg_f04_utility_dividend_growth_compoundxepsraw_252d_base_v139_signal,
    f04udg_f04_utility_dividend_growth_compoundxepsraw_63d_base_v140_signal,
    f04udg_f04_utility_dividend_growth_covxdpsxatr_252d_base_v141_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthema_63d_base_v142_signal,
    f04udg_f04_utility_dividend_growth_coverageema_63d_base_v143_signal,
    f04udg_f04_utility_dividend_growth_compoundema_63d_base_v144_signal,
    f04udg_f04_utility_dividend_growth_coverxdpsxvol_252d_base_v145_signal,
    f04udg_f04_utility_dividend_growth_growthxdpsxvol_252d_base_v146_signal,
    f04udg_f04_utility_dividend_growth_compoundxdpsxvol_252d_base_v147_signal,
    f04udg_f04_utility_dividend_growth_coveragerank_63d_base_v148_signal,
    f04udg_f04_utility_dividend_growth_compoundrank_63d_base_v149_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthrank_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_UTILITY_DIVIDEND_GROWTH_REGISTRY_076_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "dps": dps, "eps": eps, "payoutratio": payoutratio,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_dps_growth", "_f04_dividend_compound", "_f04_dividend_coverage")
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
    print(f"OK f04_utility_dividend_growth_base_076_150_claude: {n_features} features pass")
