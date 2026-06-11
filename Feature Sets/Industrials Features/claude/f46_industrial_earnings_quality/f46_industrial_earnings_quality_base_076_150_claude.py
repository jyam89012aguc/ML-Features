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
def _f46_accrual_to_cash_gap(netinc, ncfo, w):
    return _mean(netinc - ncfo, w)


def _f46_accrual_quality(netinc, ncfo, assets, w):
    acc = (netinc - ncfo) / assets.replace(0, np.nan).abs()
    return _mean(acc, w)


def _f46_cash_earnings_proxy(ncfo, ebitda, w):
    return _mean(ncfo / ebitda.replace(0, np.nan).abs(), w)


# v076 gap × revenue scaling
def f46ieq_f46_industrial_earnings_quality_acgap_rev_63d_base_v076_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj * 1.1
    return result.replace([np.inf, -np.inf], np.nan)


# v077 EMA short of gap
def f46ieq_f46_industrial_earnings_quality_acgapema_21d_base_v077_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 5)
    ema = base.ewm(span=21, adjust=False).mean() / closeadj.abs().replace(0, np.nan)
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078 long EMA of gap
def f46ieq_f46_industrial_earnings_quality_acgapema_252d_base_v078_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    ema = base.ewm(span=252, adjust=False).mean() / closeadj.abs().replace(0, np.nan)
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079 EMA short of cep
def f46ieq_f46_industrial_earnings_quality_cepema_21d_base_v079_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 5)
    ema = base.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080 long EMA of cep
def f46ieq_f46_industrial_earnings_quality_cepema_252d_base_v080_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    ema = base.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081 EMA short of acq
def f46ieq_f46_industrial_earnings_quality_acqema_21d_base_v081_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 5)
    ema = base.ewm(span=21, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082 EMA 63d of acq
def f46ieq_f46_industrial_earnings_quality_acqema_63d_base_v082_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    ema = base.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083 quality ratio EBITDA-to-NCFO
def f46ieq_f46_industrial_earnings_quality_ebitcep_63d_base_v083_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = (1.0 / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084 252d EBITDA/NCFO
def f46ieq_f46_industrial_earnings_quality_ebitcep_252d_base_v084_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = (1.0 / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085 504d EBITDA/NCFO
def f46ieq_f46_industrial_earnings_quality_ebitcep_504d_base_v085_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    result = (1.0 / base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086 quartile rank of gap (63d) over 252
def f46ieq_f46_industrial_earnings_quality_acgaprank_63d_base_v086_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087 252d rank gap pct over 504
def f46ieq_f46_industrial_earnings_quality_acgaprank_252d_base_v087_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088 cash earnings proxy rank
def f46ieq_f46_industrial_earnings_quality_ceprank_252d_base_v088_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089 acq rank
def f46ieq_f46_industrial_earnings_quality_acqrank_252d_base_v089_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090 252d gap × cep diff
def f46ieq_f46_industrial_earnings_quality_gapxcepdiff_252d_base_v090_signal(netinc, ncfo, ebitda, closeadj):
    gap = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    cepshort = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    ceplong = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = gap * (cepshort - ceplong) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091 504d gap × acq composite
def f46ieq_f46_industrial_earnings_quality_gapxacq_504d_base_v091_signal(netinc, ncfo, assets, closeadj):
    gap = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    result = gap * acq * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092 acq × ebitda margin proxy
def f46ieq_f46_industrial_earnings_quality_acqxebitda_252d_base_v092_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    em = ebitda / assets.replace(0, np.nan)
    result = acq * em * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093 acq momentum (21 vs 252)
def f46ieq_f46_industrial_earnings_quality_acqmomo_21v252_base_v093_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 21)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094 ratio short/long acq
def f46ieq_f46_industrial_earnings_quality_acqratio_63v252_base_v094_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 63)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = sh / lg.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095 ratio short/long cep
def f46ieq_f46_industrial_earnings_quality_cepratio_63v252_base_v095_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = sh / lg.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096 cep × NCFO scaling
def f46ieq_f46_industrial_earnings_quality_cepxncfo_63d_base_v096_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = base * np.log(ncfo.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097 acgap × NCFO log
def f46ieq_f46_industrial_earnings_quality_acgapxlogncfo_63d_base_v097_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    result = base * np.log(ncfo.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098 acgap × revenue z
def f46ieq_f46_industrial_earnings_quality_acgapxrevz_63d_base_v098_signal(netinc, ncfo, revenue, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    result = base * _z(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099 cep × revenue z
def f46ieq_f46_industrial_earnings_quality_cepxrevz_252d_base_v099_signal(ncfo, ebitda, revenue, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = base * _z(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100 acq × volume z
def f46ieq_f46_industrial_earnings_quality_acqxvolz_63d_base_v100_signal(netinc, ncfo, assets, volume, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101 acgap × dollar volume mean
def f46ieq_f46_industrial_earnings_quality_acgapxdv_63d_base_v101_signal(netinc, ncfo, volume, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102 cep × dollar volume mean
def f46ieq_f46_industrial_earnings_quality_cepxdv_252d_base_v102_signal(ncfo, ebitda, volume, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103 gap × close × volume
def f46ieq_f46_industrial_earnings_quality_acgapxvolc_21d_base_v103_signal(netinc, ncfo, volume, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    result = base * closeadj * np.log(volume.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v104 acgap × inverse assets * close
def f46ieq_f46_industrial_earnings_quality_acgap_invassets_252d_base_v104_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = base / assets.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105 gap sign change frequency (counter-cyclical) ×close
def f46ieq_f46_industrial_earnings_quality_acgapsign_63d_base_v105_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    sign = np.sign(base)
    chg = sign.diff().abs()
    cnt = chg.rolling(63, min_periods=21).sum()
    result = (cnt + base.abs() / netinc.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106 252d sign change count
def f46ieq_f46_industrial_earnings_quality_acgapsign_252d_base_v106_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    sign = np.sign(base)
    chg = sign.diff().abs()
    cnt = chg.rolling(252, min_periods=63).sum()
    result = (cnt + base.abs() / netinc.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107 cep × NCFO trend
def f46ieq_f46_industrial_earnings_quality_cepxncfomomo_63d_base_v107_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    ncfo_mom = ncfo.pct_change(63)
    result = base * ncfo_mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108 acgap × revenue/ebitda
def f46ieq_f46_industrial_earnings_quality_acgap_revebitda_63d_base_v108_signal(netinc, ncfo, revenue, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    rmix = revenue / ebitda.replace(0, np.nan).abs()
    result = base * rmix * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109 acq × revenue mix
def f46ieq_f46_industrial_earnings_quality_acqxrevmix_252d_base_v109_signal(netinc, ncfo, assets, revenue, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    rmix = revenue / assets.replace(0, np.nan)
    result = base * rmix * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110 21d cash earnings volatility
def f46ieq_f46_industrial_earnings_quality_cepstd_63d_base_v110_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111 252d cep volatility
def f46ieq_f46_industrial_earnings_quality_cepstd_252d_base_v111_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112 504d cep volatility
def f46ieq_f46_industrial_earnings_quality_cepstd_504d_base_v112_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113 63d acq volatility
def f46ieq_f46_industrial_earnings_quality_acqstd_63d_base_v113_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114 252d acq vol
def f46ieq_f46_industrial_earnings_quality_acqstd_252d_base_v114_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115 504d acq vol
def f46ieq_f46_industrial_earnings_quality_acqstd_504d_base_v115_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116 mean(gap)*mean(cep) interaction
def f46ieq_f46_industrial_earnings_quality_gapxcepint_252d_base_v116_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    c = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117 504d gap×cep
def f46ieq_f46_industrial_earnings_quality_gapxcepint_504d_base_v117_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan)
    c = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118 acq×cep composite quality
def f46ieq_f46_industrial_earnings_quality_acqxcep_63d_base_v118_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119 252d acq×cep
def f46ieq_f46_industrial_earnings_quality_acqxcep_252d_base_v119_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120 504d acq×cep
def f46ieq_f46_industrial_earnings_quality_acqxcep_504d_base_v120_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121 below-median gap indicator scaled
def f46ieq_f46_industrial_earnings_quality_negacgap_252d_base_v121_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=63).median()
    neg = (base < med).astype(float)
    result = (neg * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122 above-median gap indicator scaled
def f46ieq_f46_industrial_earnings_quality_posacgap_252d_base_v122_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=63).median()
    pos = (base > med).astype(float)
    result = (pos * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123 gap kurtosis 252
def f46ieq_f46_industrial_earnings_quality_acgapkurt_252d_base_v123_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124 gap skewness 252
def f46ieq_f46_industrial_earnings_quality_acgapskew_252d_base_v124_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125 cep kurtosis 252
def f46ieq_f46_industrial_earnings_quality_cepkurt_252d_base_v125_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126 cep skewness 252
def f46ieq_f46_industrial_earnings_quality_cepskew_252d_base_v126_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127 acq squared × close
def f46ieq_f46_industrial_earnings_quality_sqacq_252d_base_v127_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128 cep squared
def f46ieq_f46_industrial_earnings_quality_sqcep_252d_base_v128_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129 gap normed by sgna proxy (use ebitda for safety)
def f46ieq_f46_industrial_earnings_quality_acgap_lograw_252d_base_v129_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130 lagged gap diff (gap_now minus gap_252_ago) scaled
def f46ieq_f46_industrial_earnings_quality_acgaplagdiff_252d_base_v130_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131 lagged cep diff
def f46ieq_f46_industrial_earnings_quality_ceplagdiff_252d_base_v131_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132 lagged acq diff
def f46ieq_f46_industrial_earnings_quality_acqlagdiff_252d_base_v132_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133 gap below rolling median count + level
def f46ieq_f46_industrial_earnings_quality_acgapevent_neg_252d_base_v133_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + base * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134 cep below rolling median count + level
def f46ieq_f46_industrial_earnings_quality_cepevent_low_252d_base_v134_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    med = base.rolling(252, min_periods=63).median()
    flag = (base < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + base * 10.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135 acq above rolling median count + level
def f46ieq_f46_industrial_earnings_quality_acqevent_hi_252d_base_v135_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    med = base.rolling(252, min_periods=63).median()
    flag = (base > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    result = (cnt + base * 1000.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136 gap × depamor proxy of capex
def f46ieq_f46_industrial_earnings_quality_acgapxdep_63d_base_v136_signal(netinc, ncfo, depamor, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    result = base * np.log(depamor.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137 acq × capex/depamor
def f46ieq_f46_industrial_earnings_quality_acqxcapex_252d_base_v137_signal(netinc, ncfo, assets, capex, depamor, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    ratio = capex / depamor.replace(0, np.nan).abs()
    result = acq * ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138 cep × revenue growth
def f46ieq_f46_industrial_earnings_quality_cepxrevgrowth_252d_base_v138_signal(ncfo, ebitda, revenue, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    rg = revenue.pct_change(252)
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139 long acgap × NCFO trend
def f46ieq_f46_industrial_earnings_quality_acgapxncfomomo_504d_base_v139_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan)
    ncfo_mom = ncfo.pct_change(252)
    result = base * ncfo_mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140 gap × dollar volume normed
def f46ieq_f46_industrial_earnings_quality_acgapxdvnorm_63d_base_v140_signal(netinc, ncfo, volume, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    dv = closeadj * volume
    result = base * (_z(dv, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141 cep min over 63d (bad cash quality streaks)
def f46ieq_f46_industrial_earnings_quality_cepmin_63d_base_v141_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    mn = base.rolling(63, min_periods=21).min()
    result = mn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142 cep max
def f46ieq_f46_industrial_earnings_quality_cepmax_252d_base_v142_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    mx = base.rolling(252, min_periods=63).max()
    result = mx * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143 acq min
def f46ieq_f46_industrial_earnings_quality_acqmin_252d_base_v143_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    mn = base.rolling(252, min_periods=63).min()
    result = mn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144 acq max
def f46ieq_f46_industrial_earnings_quality_acqmax_252d_base_v144_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    mx = base.rolling(252, min_periods=63).max()
    result = mx * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145 gap range over 252d
def f46ieq_f46_industrial_earnings_quality_acgaprange_252d_base_v145_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146 cep range
def f46ieq_f46_industrial_earnings_quality_ceprange_252d_base_v146_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147 acq range
def f46ieq_f46_industrial_earnings_quality_acqrange_252d_base_v147_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148 gap × inverse current ratio proxy
def f46ieq_f46_industrial_earnings_quality_acgapxinvassets_504d_base_v148_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504)
    result = base / assets.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149 high cep regime indicator (median split)
def f46ieq_f46_industrial_earnings_quality_hicep_252d_base_v149_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    med = base.rolling(252, min_periods=63).median()
    hi = (base > med).astype(float)
    result = (hi * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150 low acq regime indicator (median split)
def f46ieq_f46_industrial_earnings_quality_lowacq_252d_base_v150_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    med = base.rolling(252, min_periods=63).median()
    lo = (base < med).astype(float)
    result = (lo * base + base * 0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ieq_f46_industrial_earnings_quality_acgap_rev_63d_base_v076_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_21d_base_v077_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_252d_base_v078_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_21d_base_v079_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_252d_base_v080_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_21d_base_v081_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_63d_base_v082_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_63d_base_v083_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_252d_base_v084_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_504d_base_v085_signal,
    f46ieq_f46_industrial_earnings_quality_acgaprank_63d_base_v086_signal,
    f46ieq_f46_industrial_earnings_quality_acgaprank_252d_base_v087_signal,
    f46ieq_f46_industrial_earnings_quality_ceprank_252d_base_v088_signal,
    f46ieq_f46_industrial_earnings_quality_acqrank_252d_base_v089_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcepdiff_252d_base_v090_signal,
    f46ieq_f46_industrial_earnings_quality_gapxacq_504d_base_v091_signal,
    f46ieq_f46_industrial_earnings_quality_acqxebitda_252d_base_v092_signal,
    f46ieq_f46_industrial_earnings_quality_acqmomo_21v252_base_v093_signal,
    f46ieq_f46_industrial_earnings_quality_acqratio_63v252_base_v094_signal,
    f46ieq_f46_industrial_earnings_quality_cepratio_63v252_base_v095_signal,
    f46ieq_f46_industrial_earnings_quality_cepxncfo_63d_base_v096_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogncfo_63d_base_v097_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxrevz_63d_base_v098_signal,
    f46ieq_f46_industrial_earnings_quality_cepxrevz_252d_base_v099_signal,
    f46ieq_f46_industrial_earnings_quality_acqxvolz_63d_base_v100_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdv_63d_base_v101_signal,
    f46ieq_f46_industrial_earnings_quality_cepxdv_252d_base_v102_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxvolc_21d_base_v103_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_invassets_252d_base_v104_signal,
    f46ieq_f46_industrial_earnings_quality_acgapsign_63d_base_v105_signal,
    f46ieq_f46_industrial_earnings_quality_acgapsign_252d_base_v106_signal,
    f46ieq_f46_industrial_earnings_quality_cepxncfomomo_63d_base_v107_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_revebitda_63d_base_v108_signal,
    f46ieq_f46_industrial_earnings_quality_acqxrevmix_252d_base_v109_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_63d_base_v110_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_252d_base_v111_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_504d_base_v112_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_63d_base_v113_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_252d_base_v114_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_504d_base_v115_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcepint_252d_base_v116_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcepint_504d_base_v117_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcep_63d_base_v118_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcep_252d_base_v119_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcep_504d_base_v120_signal,
    f46ieq_f46_industrial_earnings_quality_negacgap_252d_base_v121_signal,
    f46ieq_f46_industrial_earnings_quality_posacgap_252d_base_v122_signal,
    f46ieq_f46_industrial_earnings_quality_acgapkurt_252d_base_v123_signal,
    f46ieq_f46_industrial_earnings_quality_acgapskew_252d_base_v124_signal,
    f46ieq_f46_industrial_earnings_quality_cepkurt_252d_base_v125_signal,
    f46ieq_f46_industrial_earnings_quality_cepskew_252d_base_v126_signal,
    f46ieq_f46_industrial_earnings_quality_sqacq_252d_base_v127_signal,
    f46ieq_f46_industrial_earnings_quality_sqcep_252d_base_v128_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_lograw_252d_base_v129_signal,
    f46ieq_f46_industrial_earnings_quality_acgaplagdiff_252d_base_v130_signal,
    f46ieq_f46_industrial_earnings_quality_ceplagdiff_252d_base_v131_signal,
    f46ieq_f46_industrial_earnings_quality_acqlagdiff_252d_base_v132_signal,
    f46ieq_f46_industrial_earnings_quality_acgapevent_neg_252d_base_v133_signal,
    f46ieq_f46_industrial_earnings_quality_cepevent_low_252d_base_v134_signal,
    f46ieq_f46_industrial_earnings_quality_acqevent_hi_252d_base_v135_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdep_63d_base_v136_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcapex_252d_base_v137_signal,
    f46ieq_f46_industrial_earnings_quality_cepxrevgrowth_252d_base_v138_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxncfomomo_504d_base_v139_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdvnorm_63d_base_v140_signal,
    f46ieq_f46_industrial_earnings_quality_cepmin_63d_base_v141_signal,
    f46ieq_f46_industrial_earnings_quality_cepmax_252d_base_v142_signal,
    f46ieq_f46_industrial_earnings_quality_acqmin_252d_base_v143_signal,
    f46ieq_f46_industrial_earnings_quality_acqmax_252d_base_v144_signal,
    f46ieq_f46_industrial_earnings_quality_acgaprange_252d_base_v145_signal,
    f46ieq_f46_industrial_earnings_quality_ceprange_252d_base_v146_signal,
    f46ieq_f46_industrial_earnings_quality_acqrange_252d_base_v147_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxinvassets_504d_base_v148_signal,
    f46ieq_f46_industrial_earnings_quality_hicep_252d_base_v149_signal,
    f46ieq_f46_industrial_earnings_quality_lowacq_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_INDUSTRIAL_EARNINGS_QUALITY_REGISTRY_076_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "assets": assets,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_accrual_to_cash_gap", "_f46_accrual_quality", "_f46_cash_earnings_proxy")
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
    print(f"OK f46_industrial_earnings_quality_base_076_150_claude: {n_features} features pass")
