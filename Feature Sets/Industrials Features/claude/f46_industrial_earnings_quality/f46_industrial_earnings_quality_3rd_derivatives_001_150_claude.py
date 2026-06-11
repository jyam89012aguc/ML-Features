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
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f46_accrual_to_cash_gap(netinc, ncfo, w):
    return _mean(netinc - ncfo, w)


def _f46_accrual_quality(netinc, ncfo, assets, w):
    acc = (netinc - ncfo) / assets.replace(0, np.nan).abs()
    return _mean(acc, w)


def _f46_cash_earnings_proxy(ncfo, ebitda, w):
    return _mean(ncfo / ebitda.replace(0, np.nan).abs(), w)


# v001 5d jerk of 21d gap
def f46ieq_f46_industrial_earnings_quality_acgap_21d_jerk_v001_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002 21d jerk of 21d gap
def f46ieq_f46_industrial_earnings_quality_acgap_21d_jerk_v002_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003 21d jerk of 63d gap
def f46ieq_f46_industrial_earnings_quality_acgap_63d_jerk_v003_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v004 21d jerk of 126d gap
def f46ieq_f46_industrial_earnings_quality_acgap_126d_jerk_v004_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 126) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v005 63d jerk of 252d gap
def f46ieq_f46_industrial_earnings_quality_acgap_252d_jerk_v005_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v006 63d jerk of 504d gap
def f46ieq_f46_industrial_earnings_quality_acgap_504d_jerk_v006_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007 5d jerk of 5d gap
def f46ieq_f46_industrial_earnings_quality_acgap_5d_jerk_v007_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 5) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008 21d jerk of 42d gap
def f46ieq_f46_industrial_earnings_quality_acgap_42d_jerk_v008_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 42) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009 21d jerk of 189d gap
def f46ieq_f46_industrial_earnings_quality_acgap_189d_jerk_v009_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 189) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v010 63d jerk of 378d gap
def f46ieq_f46_industrial_earnings_quality_acgap_378d_jerk_v010_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 378) / netinc.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011 21d jerk of 63d cep
def f46ieq_f46_industrial_earnings_quality_cep_63d_jerk_v011_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012 63d jerk of 252d cep
def f46ieq_f46_industrial_earnings_quality_cep_252d_jerk_v012_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013 63d jerk of 504d cep
def f46ieq_f46_industrial_earnings_quality_cep_504d_jerk_v013_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v014 5d jerk of 21d cep
def f46ieq_f46_industrial_earnings_quality_cep_21d_jerk_v014_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v015 21d jerk of 126d cep
def f46ieq_f46_industrial_earnings_quality_cep_126d_jerk_v015_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v016 21d jerk of 63d acq
def f46ieq_f46_industrial_earnings_quality_acq_63d_jerk_v016_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v017 63d jerk of 252d acq
def f46ieq_f46_industrial_earnings_quality_acq_252d_jerk_v017_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v018 63d jerk of 504d acq
def f46ieq_f46_industrial_earnings_quality_acq_504d_jerk_v018_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019 5d jerk of 21d acq
def f46ieq_f46_industrial_earnings_quality_acq_21d_jerk_v019_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020 21d jerk of 126d acq
def f46ieq_f46_industrial_earnings_quality_acq_126d_jerk_v020_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021 21d jerk of gap z 63
def f46ieq_f46_industrial_earnings_quality_acgapz_63d_jerk_v021_signal(netinc, ncfo, closeadj):
    base = _z(_f46_accrual_to_cash_gap(netinc, ncfo, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v022 63d jerk of gap z 252
def f46ieq_f46_industrial_earnings_quality_acgapz_252d_jerk_v022_signal(netinc, ncfo, closeadj):
    base = _z(_f46_accrual_to_cash_gap(netinc, ncfo, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v023 21d jerk of cep z
def f46ieq_f46_industrial_earnings_quality_cepz_63d_jerk_v023_signal(ncfo, ebitda, closeadj):
    base = _z(_f46_cash_earnings_proxy(ncfo, ebitda, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024 63d jerk of cep z
def f46ieq_f46_industrial_earnings_quality_cepz_252d_jerk_v024_signal(ncfo, ebitda, closeadj):
    base = _z(_f46_cash_earnings_proxy(ncfo, ebitda, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025 21d jerk of acq z
def f46ieq_f46_industrial_earnings_quality_acqz_63d_jerk_v025_signal(netinc, ncfo, assets, closeadj):
    base = _z(_f46_accrual_quality(netinc, ncfo, assets, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v026 63d jerk of acq z
def f46ieq_f46_industrial_earnings_quality_acqz_252d_jerk_v026_signal(netinc, ncfo, assets, closeadj):
    base = _z(_f46_accrual_quality(netinc, ncfo, assets, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v027 63d jerk of gap std
def f46ieq_f46_industrial_earnings_quality_acgapstd_252d_jerk_v027_signal(netinc, ncfo, closeadj):
    base = _std(_f46_accrual_to_cash_gap(netinc, ncfo, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028 21d jerk of gap std
def f46ieq_f46_industrial_earnings_quality_acgapstd_63d_jerk_v028_signal(netinc, ncfo, closeadj):
    base = _std(_f46_accrual_to_cash_gap(netinc, ncfo, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v029 21d jerk of cep std
def f46ieq_f46_industrial_earnings_quality_cepstd_63d_jerk_v029_signal(ncfo, ebitda, closeadj):
    base = _std(_f46_cash_earnings_proxy(ncfo, ebitda, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030 63d jerk of cep std long
def f46ieq_f46_industrial_earnings_quality_cepstd_252d_jerk_v030_signal(ncfo, ebitda, closeadj):
    base = _std(_f46_cash_earnings_proxy(ncfo, ebitda, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031 63d jerk of acq std
def f46ieq_f46_industrial_earnings_quality_acqstd_252d_jerk_v031_signal(netinc, ncfo, assets, closeadj):
    base = _std(_f46_accrual_quality(netinc, ncfo, assets, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v032 21d jerk of acq std
def f46ieq_f46_industrial_earnings_quality_acqstd_63d_jerk_v032_signal(netinc, ncfo, assets, closeadj):
    base = _std(_f46_accrual_quality(netinc, ncfo, assets, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033 21d jerk of gap/ebitda
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_63d_jerk_v033_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / ebitda.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v034 63d jerk of gap/ebitda
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_252d_jerk_v034_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / ebitda.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v035 63d jerk of gap/ebitda 504
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_504d_jerk_v035_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / ebitda.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v036 63d jerk of cep diff (63 - 252)
def f46ieq_f46_industrial_earnings_quality_cepdiff_63m252_jerk_v036_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037 21d jerk of cep diff 21 vs 63
def f46ieq_f46_industrial_earnings_quality_cepdiff_21m63_jerk_v037_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v038 63d jerk of acq diff 63 vs 252
def f46ieq_f46_industrial_earnings_quality_acqdiff_63m252_jerk_v038_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 63)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v039 21d jerk of acq diff 21 vs 63
def f46ieq_f46_industrial_earnings_quality_acqdiff_21m63_jerk_v039_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 21)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v040 63d jerk of gap/assets
def f46ieq_f46_industrial_earnings_quality_acgap_assets_63d_jerk_v040_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / assets.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v041 63d jerk of gap/assets 252
def f46ieq_f46_industrial_earnings_quality_acgap_assets_252d_jerk_v041_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / assets.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v042 126d jerk of gap/assets 504
def f46ieq_f46_industrial_earnings_quality_acgap_assets_504d_jerk_v042_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / assets.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v043 63d jerk of composite quality 252
def f46ieq_f46_industrial_earnings_quality_qcomp_252d_jerk_v043_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = (cep - acq) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v044 21d jerk of composite 63d
def f46ieq_f46_industrial_earnings_quality_qcomp_63d_jerk_v044_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = (cep - acq) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045 63d jerk of composite 504
def f46ieq_f46_industrial_earnings_quality_qcomp_504d_jerk_v045_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    base = (cep - acq) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046 63d jerk of gap EMA 63
def f46ieq_f46_industrial_earnings_quality_acgapema_63d_jerk_v046_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v047 21d jerk of gap EMA 21
def f46ieq_f46_industrial_earnings_quality_acgapema_21d_jerk_v047_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 5) / netinc.abs().replace(0, np.nan)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048 126d jerk of gap EMA 252
def f46ieq_f46_industrial_earnings_quality_acgapema_252d_jerk_v048_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v049 21d jerk of cep EMA 21
def f46ieq_f46_industrial_earnings_quality_cepema_21d_jerk_v049_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v050 63d jerk of cep EMA 63
def f46ieq_f46_industrial_earnings_quality_cepema_63d_jerk_v050_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v051 63d jerk of cep EMA 252
def f46ieq_f46_industrial_earnings_quality_cepema_252d_jerk_v051_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052 21d jerk of acq EMA 21
def f46ieq_f46_industrial_earnings_quality_acqema_21d_jerk_v052_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v053 63d jerk of acq EMA 63
def f46ieq_f46_industrial_earnings_quality_acqema_63d_jerk_v053_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v054 63d jerk of acq EMA 252
def f46ieq_f46_industrial_earnings_quality_acqema_252d_jerk_v054_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055 63d jerk of inverse cep 252
def f46ieq_f46_industrial_earnings_quality_ebitcep_252d_jerk_v055_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = (1.0 / cep.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v056 21d jerk of inverse cep 63
def f46ieq_f46_industrial_earnings_quality_ebitcep_63d_jerk_v056_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = (1.0 / cep.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057 63d jerk of gap rank 252
def f46ieq_f46_industrial_earnings_quality_acgaprank_252d_jerk_v057_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058 63d jerk of cep rank
def f46ieq_f46_industrial_earnings_quality_ceprank_252d_jerk_v058_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v059 63d jerk of acq rank
def f46ieq_f46_industrial_earnings_quality_acqrank_252d_jerk_v059_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v060 63d jerk of gap × volume z
def f46ieq_f46_industrial_earnings_quality_acgapxvolz_63d_jerk_v060_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * _z(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061 21d jerk of gap × dv mean
def f46ieq_f46_industrial_earnings_quality_acgapxdv_63d_jerk_v061_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    dv = closeadj * volume
    base = g * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v062 63d jerk of cep × dv mean
def f46ieq_f46_industrial_earnings_quality_cepxdv_252d_jerk_v062_signal(ncfo, ebitda, volume, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v063 63d jerk of acq × volume z
def f46ieq_f46_industrial_earnings_quality_acqxvolz_63d_jerk_v063_signal(netinc, ncfo, assets, volume, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = g * _z(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064 63d jerk of acq × ebitda margin
def f46ieq_f46_industrial_earnings_quality_acqxebitda_252d_jerk_v064_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    em = ebitda / assets.replace(0, np.nan)
    base = acq * em * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v065 21d jerk of gap × cep
def f46ieq_f46_industrial_earnings_quality_gapxcep_63d_jerk_v065_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = g * cep * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066 63d jerk of gap × cep 252
def f46ieq_f46_industrial_earnings_quality_gapxcep_252d_jerk_v066_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = g * cep * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067 63d jerk of absolute gap
def f46ieq_f46_industrial_earnings_quality_absacgap_63d_jerk_v067_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63).abs() / netinc.abs().replace(0, np.nan)
    base = g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v068 21d jerk of squared gap
def f46ieq_f46_industrial_earnings_quality_sqacgap_63d_jerk_v068_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069 63d jerk of (cep - 1)
def f46ieq_f46_industrial_earnings_quality_cepminus1_252d_jerk_v069_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = (cep - 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070 21d jerk of (cep - 1) 63
def f46ieq_f46_industrial_earnings_quality_cepminus1_63d_jerk_v070_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = (cep - 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v071 21d jerk of gap × log close
def f46ieq_f46_industrial_earnings_quality_acgapxlogc_63d_jerk_v071_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072 63d jerk of cep × log close
def f46ieq_f46_industrial_earnings_quality_cepxlogprice_252d_jerk_v072_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = cep * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073 63d jerk of gap min
def f46ieq_f46_industrial_earnings_quality_acgapmin_63d_jerk_v073_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v074 63d jerk of gap max
def f46ieq_f46_industrial_earnings_quality_acgapmax_252d_jerk_v074_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v075 63d jerk of gap range
def f46ieq_f46_industrial_earnings_quality_acgaprange_252d_jerk_v075_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076 21d jerk of cep range
def f46ieq_f46_industrial_earnings_quality_ceprange_252d_jerk_v076_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v077 63d jerk of acq range
def f46ieq_f46_industrial_earnings_quality_acqrange_252d_jerk_v077_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v078 63d jerk of squared acq
def f46ieq_f46_industrial_earnings_quality_sqacq_252d_jerk_v078_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079 63d jerk of squared cep
def f46ieq_f46_industrial_earnings_quality_sqcep_252d_jerk_v079_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v080 63d jerk of cep skew
def f46ieq_f46_industrial_earnings_quality_cepskew_252d_jerk_v080_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v081 63d jerk of cep kurt
def f46ieq_f46_industrial_earnings_quality_cepkurt_252d_jerk_v081_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082 63d jerk of gap skew
def f46ieq_f46_industrial_earnings_quality_acgapskew_252d_jerk_v082_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v083 63d jerk of gap kurt
def f46ieq_f46_industrial_earnings_quality_acgapkurt_252d_jerk_v083_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v084 21d jerk of gap lag-diff
def f46ieq_f46_industrial_earnings_quality_acgaplagdiff_252d_jerk_v084_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = (g - g.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v085 63d jerk of cep lag diff
def f46ieq_f46_industrial_earnings_quality_ceplagdiff_252d_jerk_v085_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = (g - g.shift(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v086 21d jerk of acq lag diff
def f46ieq_f46_industrial_earnings_quality_acqlagdiff_252d_jerk_v086_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = (g - g.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087 21d jerk of gap × revenue z
def f46ieq_f46_industrial_earnings_quality_acgapxrevz_63d_jerk_v087_signal(netinc, ncfo, revenue, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * _z(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v088 63d jerk of cep × revenue z
def f46ieq_f46_industrial_earnings_quality_cepxrevz_252d_jerk_v088_signal(ncfo, ebitda, revenue, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = cep * _z(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v089 63d jerk of cep × revenue growth
def f46ieq_f46_industrial_earnings_quality_cepxrevgrowth_252d_jerk_v089_signal(ncfo, ebitda, revenue, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    rg = revenue.pct_change(252)
    base = cep * rg * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v090 63d jerk of gap × log NCFO
def f46ieq_f46_industrial_earnings_quality_acgapxlogncfo_63d_jerk_v090_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * np.log(ncfo.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091 21d jerk of cep × NCFO momentum
def f46ieq_f46_industrial_earnings_quality_cepxncfomomo_63d_jerk_v091_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    nm = ncfo.pct_change(63)
    base = cep * nm * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v092 63d jerk of long gap × ncfo momentum
def f46ieq_f46_industrial_earnings_quality_acgapxncfomomo_504d_jerk_v092_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan)
    nm = ncfo.pct_change(252)
    base = g * nm * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v093 63d jerk of gap × dv normed
def f46ieq_f46_industrial_earnings_quality_acgapxdvnorm_63d_jerk_v093_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    dv = closeadj * volume
    base = g * _z(dv, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094 63d jerk of cep min
def f46ieq_f46_industrial_earnings_quality_cepmin_63d_jerk_v094_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = g.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v095 63d jerk of cep max
def f46ieq_f46_industrial_earnings_quality_cepmax_252d_jerk_v095_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = g.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v096 63d jerk of acq min
def f46ieq_f46_industrial_earnings_quality_acqmin_252d_jerk_v096_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 21)
    base = g.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097 63d jerk of acq max
def f46ieq_f46_industrial_earnings_quality_acqmax_252d_jerk_v097_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 21)
    base = g.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v098 63d jerk of negative-gap (median-split)
def f46ieq_f46_industrial_earnings_quality_negacgap_252d_jerk_v098_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    med = g.rolling(252, min_periods=63).median()
    base = ((g < med).astype(float) * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v099 63d jerk of positive-gap (median-split)
def f46ieq_f46_industrial_earnings_quality_posacgap_252d_jerk_v099_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    med = g.rolling(252, min_periods=63).median()
    base = ((g > med).astype(float) * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100 21d jerk of gap z 21
def f46ieq_f46_industrial_earnings_quality_acgapz_21d_jerk_v100_signal(netinc, ncfo, closeadj):
    base = _z(_f46_accrual_to_cash_gap(netinc, ncfo, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v101 5d jerk of gap z 21
def f46ieq_f46_industrial_earnings_quality_acgapz_21d_jerk_v101_signal(netinc, ncfo, closeadj):
    base = _z(_f46_accrual_to_cash_gap(netinc, ncfo, 21), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v102 21d jerk of cep × log NCFO
def f46ieq_f46_industrial_earnings_quality_cepxncfo_63d_jerk_v102_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = cep * np.log(ncfo.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v103 63d jerk of acq × capex/depamor
def f46ieq_f46_industrial_earnings_quality_acqxcapex_252d_jerk_v103_signal(netinc, ncfo, assets, capex, depamor, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    ratio = capex / depamor.replace(0, np.nan).abs()
    base = acq * ratio * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v104 63d jerk of gap × log depamor
def f46ieq_f46_industrial_earnings_quality_acgapxdep_63d_jerk_v104_signal(netinc, ncfo, depamor, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * np.log(depamor.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v105 63d jerk of gap log scale
def f46ieq_f46_industrial_earnings_quality_acgaplog_252d_jerk_v105_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106 21d jerk of qcomp short 21
def f46ieq_f46_industrial_earnings_quality_qcomp_21d_jerk_v106_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 21)
    base = (cep - acq) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v107 5d jerk of qcomp short 5
def f46ieq_f46_industrial_earnings_quality_qcomp_5d_jerk_v107_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 5)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 5)
    base = (cep - acq) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v108 63d jerk of qcomp 504
def f46ieq_f46_industrial_earnings_quality_qcomp_504d_jerk_v108_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    base = (cep - acq) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109 21d jerk of gap × inverse close
def f46ieq_f46_industrial_earnings_quality_acgap_invc_63d_jerk_v109_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    base = g / closeadj.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v110 63d jerk of cep 252 raw
def f46ieq_f46_industrial_earnings_quality_cep_252d_jerk_v110_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v111 5d jerk of cep 21 raw
def f46ieq_f46_industrial_earnings_quality_cep_21d_jerk_v111_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v112 63d jerk of inverse cep 504
def f46ieq_f46_industrial_earnings_quality_ebitcep_504d_jerk_v112_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    base = (1.0 / cep.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v113 63d jerk of acq diff 252-504
def f46ieq_f46_industrial_earnings_quality_acqdiff_252m504_jerk_v113_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 252)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 504)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v114 63d jerk of cep diff 252-504
def f46ieq_f46_industrial_earnings_quality_cepdiff_252m504_jerk_v114_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115 21d jerk of cep ratio short/long
def f46ieq_f46_industrial_earnings_quality_cepratio_63v252_jerk_v115_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v116 21d jerk of acq ratio short/long
def f46ieq_f46_industrial_earnings_quality_acqratio_63v252_jerk_v116_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 63)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117 5d jerk of gap × volume scaled
def f46ieq_f46_industrial_earnings_quality_acgapxvolc_21d_jerk_v117_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g * closeadj * np.log(volume.abs().replace(0, np.nan))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v118 21d jerk of raw gap 21
def f46ieq_f46_industrial_earnings_quality_acgapraw_21d_jerk_v118_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    base = g * _mean(closeadj, 21) / closeadj.abs().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v119 63d jerk of long raw gap
def f46ieq_f46_industrial_earnings_quality_acgapraw_252d_jerk_v119_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    base = g * _mean(closeadj, 63) / closeadj.abs().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v120 21d jerk of gap × sign of netinc
def f46ieq_f46_industrial_earnings_quality_acgapxni_63d_jerk_v120_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    base = g * np.sign(netinc) / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v121 21d jerk of gap/assets 252
def f46ieq_f46_industrial_earnings_quality_acgap_invassets_252d_jerk_v121_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / assets.replace(0, np.nan).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v122 63d jerk of acq*revenue mix
def f46ieq_f46_industrial_earnings_quality_acqxrevmix_252d_jerk_v122_signal(netinc, ncfo, assets, revenue, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    rmix = revenue / assets.replace(0, np.nan)
    base = acq * rmix * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v123 21d jerk of gap × rev/ebitda
def f46ieq_f46_industrial_earnings_quality_acgap_revebitda_63d_jerk_v123_signal(netinc, ncfo, revenue, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    rmix = revenue / ebitda.replace(0, np.nan).abs()
    base = g * rmix * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v124 21d jerk of qcomp 63 alt
def f46ieq_f46_industrial_earnings_quality_qcomp63_alt_jerk_v124_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = (cep + acq) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v125 63d jerk of qcomp 252 alt
def f46ieq_f46_industrial_earnings_quality_qcomp252_alt_jerk_v125_signal(netinc, ncfo, assets, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = (cep + acq) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v126 63d jerk of gap × log close (21)
def f46ieq_f46_industrial_earnings_quality_acgapxlogprice_21d_jerk_v126_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    base = g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127 63d jerk of cep*log price 63
def f46ieq_f46_industrial_earnings_quality_cepxlogprice_63d_jerk_v127_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = cep * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v128 21d jerk of acq*log price
def f46ieq_f46_industrial_earnings_quality_acqxlogprice_63d_jerk_v128_signal(netinc, ncfo, assets, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    base = acq * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129 63d jerk of negative-gap event count
def f46ieq_f46_industrial_earnings_quality_acgapevent_neg_252d_jerk_v129_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    med = g.rolling(252, min_periods=63).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130 63d jerk of low-cep event count
def f46ieq_f46_industrial_earnings_quality_cepevent_low_252d_jerk_v130_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v131 63d jerk of high-acq event count
def f46ieq_f46_industrial_earnings_quality_acqevent_hi_252d_jerk_v131_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 1000.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v132 63d jerk of sign(gap) × cep
def f46ieq_f46_industrial_earnings_quality_signxcep_63d_jerk_v132_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = np.sign(g) * cep * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133 21d jerk of cep minus 1 21d
def f46ieq_f46_industrial_earnings_quality_cepminus1_21d_jerk_v133_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = (cep - 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v134 63d jerk of gap × acq 504
def f46ieq_f46_industrial_earnings_quality_gapxacq_504d_jerk_v134_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 504) / netinc.abs().replace(0, np.nan)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    base = g * acq * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v135 63d jerk of acq momentum 21 vs 252
def f46ieq_f46_industrial_earnings_quality_acqmomo_21v252_jerk_v135_signal(netinc, ncfo, assets, closeadj):
    sh = _f46_accrual_quality(netinc, ncfo, assets, 21)
    lg = _f46_accrual_quality(netinc, ncfo, assets, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136 21d jerk of gap × cep diff 252
def f46ieq_f46_industrial_earnings_quality_gapxcepdiff_252d_jerk_v136_signal(netinc, ncfo, ebitda, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    cs = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    cl = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = g * (cs - cl) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v137 63d jerk of acq × ebitda margin (long)
def f46ieq_f46_industrial_earnings_quality_acqxebitda_504d_jerk_v137_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    em = ebitda / assets.replace(0, np.nan)
    base = acq * em * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v138 21d jerk of cep × NCFO momentum 252
def f46ieq_f46_industrial_earnings_quality_cepxncfomomo_252d_jerk_v138_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    nm = ncfo.pct_change(126)
    base = cep * nm * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v139 63d jerk of gap × close × volume
def f46ieq_f46_industrial_earnings_quality_acgapxvolc_63d_jerk_v139_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    base = g * closeadj * np.log(volume.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v140 63d jerk of acq×cep long
def f46ieq_f46_industrial_earnings_quality_acqxcep_504d_jerk_v140_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    base = (cep - acq) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v141 21d jerk of acq×cep 63
def f46ieq_f46_industrial_earnings_quality_acqxcep_63d_jerk_v141_signal(netinc, ncfo, assets, ebitda, closeadj):
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = (cep - acq) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v142 21d jerk of cep std 21
def f46ieq_f46_industrial_earnings_quality_cepstd_21d_jerk_v142_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    base = _std(g, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v143 5d jerk of cep std 21
def f46ieq_f46_industrial_earnings_quality_cepstd_5d_jerk_v143_signal(ncfo, ebitda, closeadj):
    g = _f46_cash_earnings_proxy(ncfo, ebitda, 5)
    base = _std(g, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v144 21d jerk of acq std 21
def f46ieq_f46_industrial_earnings_quality_acqstd_21d_jerk_v144_signal(netinc, ncfo, assets, closeadj):
    g = _f46_accrual_quality(netinc, ncfo, assets, 5)
    base = _std(g, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v145 5d jerk of gap std
def f46ieq_f46_industrial_earnings_quality_acgapstd_21d_jerk_v145_signal(netinc, ncfo, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 5)
    base = _std(g, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146 63d jerk of cep × ebitda margin
def f46ieq_f46_industrial_earnings_quality_cepxem_252d_jerk_v146_signal(ncfo, ebitda, assets, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    em = ebitda / assets.replace(0, np.nan)
    base = cep * em * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v147 21d jerk of cep*revenue z 63
def f46ieq_f46_industrial_earnings_quality_cepxrevz_63d_jerk_v147_signal(ncfo, ebitda, revenue, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    base = cep * _z(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v148 63d jerk of inverse cep 252 with closeadj normalization
def f46ieq_f46_industrial_earnings_quality_ebitcepnorm_252d_jerk_v148_signal(ncfo, ebitda, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = (1.0 / cep.replace(0, np.nan)) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v149 21d jerk of cep diff 21 vs 252
def f46ieq_f46_industrial_earnings_quality_cepdiff_21m252_jerk_v149_signal(ncfo, ebitda, closeadj):
    sh = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    lg = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150 63d jerk of gap × dv long
def f46ieq_f46_industrial_earnings_quality_acgapxdv_252d_jerk_v150_signal(netinc, ncfo, volume, closeadj):
    g = _f46_accrual_to_cash_gap(netinc, ncfo, 252) / netinc.abs().replace(0, np.nan)
    dv = closeadj * volume
    base = g * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ieq_f46_industrial_earnings_quality_acgap_21d_jerk_v001_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_21d_jerk_v002_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_63d_jerk_v003_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_126d_jerk_v004_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_252d_jerk_v005_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_504d_jerk_v006_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_5d_jerk_v007_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_42d_jerk_v008_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_189d_jerk_v009_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_378d_jerk_v010_signal,
    f46ieq_f46_industrial_earnings_quality_cep_63d_jerk_v011_signal,
    f46ieq_f46_industrial_earnings_quality_cep_252d_jerk_v012_signal,
    f46ieq_f46_industrial_earnings_quality_cep_504d_jerk_v013_signal,
    f46ieq_f46_industrial_earnings_quality_cep_21d_jerk_v014_signal,
    f46ieq_f46_industrial_earnings_quality_cep_126d_jerk_v015_signal,
    f46ieq_f46_industrial_earnings_quality_acq_63d_jerk_v016_signal,
    f46ieq_f46_industrial_earnings_quality_acq_252d_jerk_v017_signal,
    f46ieq_f46_industrial_earnings_quality_acq_504d_jerk_v018_signal,
    f46ieq_f46_industrial_earnings_quality_acq_21d_jerk_v019_signal,
    f46ieq_f46_industrial_earnings_quality_acq_126d_jerk_v020_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_63d_jerk_v021_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_252d_jerk_v022_signal,
    f46ieq_f46_industrial_earnings_quality_cepz_63d_jerk_v023_signal,
    f46ieq_f46_industrial_earnings_quality_cepz_252d_jerk_v024_signal,
    f46ieq_f46_industrial_earnings_quality_acqz_63d_jerk_v025_signal,
    f46ieq_f46_industrial_earnings_quality_acqz_252d_jerk_v026_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_252d_jerk_v027_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_63d_jerk_v028_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_63d_jerk_v029_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_252d_jerk_v030_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_252d_jerk_v031_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_63d_jerk_v032_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_63d_jerk_v033_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_252d_jerk_v034_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_504d_jerk_v035_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_63m252_jerk_v036_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_21m63_jerk_v037_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_63m252_jerk_v038_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_21m63_jerk_v039_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_63d_jerk_v040_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_252d_jerk_v041_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_504d_jerk_v042_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_252d_jerk_v043_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_63d_jerk_v044_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_504d_jerk_v045_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_63d_jerk_v046_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_21d_jerk_v047_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_252d_jerk_v048_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_21d_jerk_v049_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_63d_jerk_v050_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_252d_jerk_v051_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_21d_jerk_v052_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_63d_jerk_v053_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_252d_jerk_v054_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_252d_jerk_v055_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_63d_jerk_v056_signal,
    f46ieq_f46_industrial_earnings_quality_acgaprank_252d_jerk_v057_signal,
    f46ieq_f46_industrial_earnings_quality_ceprank_252d_jerk_v058_signal,
    f46ieq_f46_industrial_earnings_quality_acqrank_252d_jerk_v059_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxvolz_63d_jerk_v060_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdv_63d_jerk_v061_signal,
    f46ieq_f46_industrial_earnings_quality_cepxdv_252d_jerk_v062_signal,
    f46ieq_f46_industrial_earnings_quality_acqxvolz_63d_jerk_v063_signal,
    f46ieq_f46_industrial_earnings_quality_acqxebitda_252d_jerk_v064_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcep_63d_jerk_v065_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcep_252d_jerk_v066_signal,
    f46ieq_f46_industrial_earnings_quality_absacgap_63d_jerk_v067_signal,
    f46ieq_f46_industrial_earnings_quality_sqacgap_63d_jerk_v068_signal,
    f46ieq_f46_industrial_earnings_quality_cepminus1_252d_jerk_v069_signal,
    f46ieq_f46_industrial_earnings_quality_cepminus1_63d_jerk_v070_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogc_63d_jerk_v071_signal,
    f46ieq_f46_industrial_earnings_quality_cepxlogprice_252d_jerk_v072_signal,
    f46ieq_f46_industrial_earnings_quality_acgapmin_63d_jerk_v073_signal,
    f46ieq_f46_industrial_earnings_quality_acgapmax_252d_jerk_v074_signal,
    f46ieq_f46_industrial_earnings_quality_acgaprange_252d_jerk_v075_signal,
    f46ieq_f46_industrial_earnings_quality_ceprange_252d_jerk_v076_signal,
    f46ieq_f46_industrial_earnings_quality_acqrange_252d_jerk_v077_signal,
    f46ieq_f46_industrial_earnings_quality_sqacq_252d_jerk_v078_signal,
    f46ieq_f46_industrial_earnings_quality_sqcep_252d_jerk_v079_signal,
    f46ieq_f46_industrial_earnings_quality_cepskew_252d_jerk_v080_signal,
    f46ieq_f46_industrial_earnings_quality_cepkurt_252d_jerk_v081_signal,
    f46ieq_f46_industrial_earnings_quality_acgapskew_252d_jerk_v082_signal,
    f46ieq_f46_industrial_earnings_quality_acgapkurt_252d_jerk_v083_signal,
    f46ieq_f46_industrial_earnings_quality_acgaplagdiff_252d_jerk_v084_signal,
    f46ieq_f46_industrial_earnings_quality_ceplagdiff_252d_jerk_v085_signal,
    f46ieq_f46_industrial_earnings_quality_acqlagdiff_252d_jerk_v086_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxrevz_63d_jerk_v087_signal,
    f46ieq_f46_industrial_earnings_quality_cepxrevz_252d_jerk_v088_signal,
    f46ieq_f46_industrial_earnings_quality_cepxrevgrowth_252d_jerk_v089_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogncfo_63d_jerk_v090_signal,
    f46ieq_f46_industrial_earnings_quality_cepxncfomomo_63d_jerk_v091_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxncfomomo_504d_jerk_v092_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdvnorm_63d_jerk_v093_signal,
    f46ieq_f46_industrial_earnings_quality_cepmin_63d_jerk_v094_signal,
    f46ieq_f46_industrial_earnings_quality_cepmax_252d_jerk_v095_signal,
    f46ieq_f46_industrial_earnings_quality_acqmin_252d_jerk_v096_signal,
    f46ieq_f46_industrial_earnings_quality_acqmax_252d_jerk_v097_signal,
    f46ieq_f46_industrial_earnings_quality_negacgap_252d_jerk_v098_signal,
    f46ieq_f46_industrial_earnings_quality_posacgap_252d_jerk_v099_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_21d_jerk_v100_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_21d_jerk_v101_signal,
    f46ieq_f46_industrial_earnings_quality_cepxncfo_63d_jerk_v102_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcapex_252d_jerk_v103_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdep_63d_jerk_v104_signal,
    f46ieq_f46_industrial_earnings_quality_acgaplog_252d_jerk_v105_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_21d_jerk_v106_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_5d_jerk_v107_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_504d_jerk_v108_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_invc_63d_jerk_v109_signal,
    f46ieq_f46_industrial_earnings_quality_cep_252d_jerk_v110_signal,
    f46ieq_f46_industrial_earnings_quality_cep_21d_jerk_v111_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcep_504d_jerk_v112_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_252m504_jerk_v113_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_252m504_jerk_v114_signal,
    f46ieq_f46_industrial_earnings_quality_cepratio_63v252_jerk_v115_signal,
    f46ieq_f46_industrial_earnings_quality_acqratio_63v252_jerk_v116_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxvolc_21d_jerk_v117_signal,
    f46ieq_f46_industrial_earnings_quality_acgapraw_21d_jerk_v118_signal,
    f46ieq_f46_industrial_earnings_quality_acgapraw_252d_jerk_v119_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxni_63d_jerk_v120_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_invassets_252d_jerk_v121_signal,
    f46ieq_f46_industrial_earnings_quality_acqxrevmix_252d_jerk_v122_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_revebitda_63d_jerk_v123_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp63_alt_jerk_v124_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp252_alt_jerk_v125_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogprice_21d_jerk_v126_signal,
    f46ieq_f46_industrial_earnings_quality_cepxlogprice_63d_jerk_v127_signal,
    f46ieq_f46_industrial_earnings_quality_acqxlogprice_63d_jerk_v128_signal,
    f46ieq_f46_industrial_earnings_quality_acgapevent_neg_252d_jerk_v129_signal,
    f46ieq_f46_industrial_earnings_quality_cepevent_low_252d_jerk_v130_signal,
    f46ieq_f46_industrial_earnings_quality_acqevent_hi_252d_jerk_v131_signal,
    f46ieq_f46_industrial_earnings_quality_signxcep_63d_jerk_v132_signal,
    f46ieq_f46_industrial_earnings_quality_cepminus1_21d_jerk_v133_signal,
    f46ieq_f46_industrial_earnings_quality_gapxacq_504d_jerk_v134_signal,
    f46ieq_f46_industrial_earnings_quality_acqmomo_21v252_jerk_v135_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcepdiff_252d_jerk_v136_signal,
    f46ieq_f46_industrial_earnings_quality_acqxebitda_504d_jerk_v137_signal,
    f46ieq_f46_industrial_earnings_quality_cepxncfomomo_252d_jerk_v138_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxvolc_63d_jerk_v139_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcep_504d_jerk_v140_signal,
    f46ieq_f46_industrial_earnings_quality_acqxcep_63d_jerk_v141_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_21d_jerk_v142_signal,
    f46ieq_f46_industrial_earnings_quality_cepstd_5d_jerk_v143_signal,
    f46ieq_f46_industrial_earnings_quality_acqstd_21d_jerk_v144_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_21d_jerk_v145_signal,
    f46ieq_f46_industrial_earnings_quality_cepxem_252d_jerk_v146_signal,
    f46ieq_f46_industrial_earnings_quality_cepxrevz_63d_jerk_v147_signal,
    f46ieq_f46_industrial_earnings_quality_ebitcepnorm_252d_jerk_v148_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_21m252_jerk_v149_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxdv_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_INDUSTRIAL_EARNINGS_QUALITY_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f46_industrial_earnings_quality_3rd_derivatives_001_150_claude: {n_features} features pass")
