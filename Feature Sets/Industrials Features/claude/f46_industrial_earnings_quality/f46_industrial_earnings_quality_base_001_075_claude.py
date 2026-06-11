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


# v001 21d accrual-to-cash gap scaled by close
def f46ieq_f46_industrial_earnings_quality_acgap_21d_base_v001_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002 63d accrual-to-cash gap scaled
def f46ieq_f46_industrial_earnings_quality_acgap_63d_base_v002_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003 126d gap
def f46ieq_f46_industrial_earnings_quality_acgap_126d_base_v003_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 126)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004 252d gap
def f46ieq_f46_industrial_earnings_quality_acgap_252d_base_v004_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005 504d gap
def f46ieq_f46_industrial_earnings_quality_acgap_504d_base_v005_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006 5d gap
def f46ieq_f46_industrial_earnings_quality_acgap_5d_base_v006_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 5)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007 42d gap
def f46ieq_f46_industrial_earnings_quality_acgap_42d_base_v007_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 42)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008 189d gap
def f46ieq_f46_industrial_earnings_quality_acgap_189d_base_v008_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 189)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009 378d gap
def f46ieq_f46_industrial_earnings_quality_acgap_378d_base_v009_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 378)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010 ratio gap/abs(netinc) scaled by close
def f46ieq_f46_industrial_earnings_quality_acgapratio_63d_base_v010_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    ratio = base / netinc.abs().replace(0, np.nan)
    result = ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011 252d gap ratio
def f46ieq_f46_industrial_earnings_quality_acgapratio_252d_base_v011_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    ratio = base / netinc.abs().replace(0, np.nan)
    result = ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012 504d gap ratio
def f46ieq_f46_industrial_earnings_quality_acgapratio_504d_base_v012_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504)
    ratio = base / netinc.abs().replace(0, np.nan)
    result = ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013 21d accrual quality (gap / assets)
def f46ieq_f46_industrial_earnings_quality_acq_21d_base_v013_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014 63d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_63d_base_v014_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015 126d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_126d_base_v015_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016 252d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_252d_base_v016_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017 504d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_504d_base_v017_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018 42d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_42d_base_v018_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019 189d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_189d_base_v019_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020 378d accrual quality
def f46ieq_f46_industrial_earnings_quality_acq_378d_base_v020_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021 21d cash earnings proxy (ncfo/ebitda)
def f46ieq_f46_industrial_earnings_quality_cep_21d_base_v021_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022 63d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_63d_base_v022_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023 126d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_126d_base_v023_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024 252d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_252d_base_v024_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025 504d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_504d_base_v025_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026 5d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_5d_base_v026_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027 42d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_42d_base_v027_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028 189d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_189d_base_v028_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029 378d cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cep_378d_base_v029_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030 63d gap z-score over 252d scaled
def f46ieq_f46_industrial_earnings_quality_acgapz_63d_base_v030_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031 252d gap z over 504d
def f46ieq_f46_industrial_earnings_quality_acgapz_252d_base_v031_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032 21d gap z over 126d
def f46ieq_f46_industrial_earnings_quality_acgapz_21d_base_v032_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033 63d accrual quality z
def f46ieq_f46_industrial_earnings_quality_acqz_63d_base_v033_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034 252d accrual quality z
def f46ieq_f46_industrial_earnings_quality_acqz_252d_base_v034_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035 63d cash earnings z
def f46ieq_f46_industrial_earnings_quality_cepz_63d_base_v035_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036 252d cash earnings z
def f46ieq_f46_industrial_earnings_quality_cepz_252d_base_v036_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037 std of 21d gap over 63d scaled
def f46ieq_f46_industrial_earnings_quality_acgapstd_63d_base_v037_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    result = _std(base, 63) / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038 std of 63d gap over 252d
def f46ieq_f46_industrial_earnings_quality_acgapstd_252d_base_v038_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = _std(base, 252) / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039 std of 252d gap over 504d
def f46ieq_f46_industrial_earnings_quality_acgapstd_504d_base_v039_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = _std(base, 504) / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040 gap divided by EBITDA scaled by close
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_63d_base_v040_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / ebitda.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041 252d gap / ebitda scaled
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_252d_base_v041_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = base / ebitda.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042 504d gap / ebitda scaled
def f46ieq_f46_industrial_earnings_quality_acgap_ebitda_504d_base_v042_signal(netinc, ncfo, ebitda, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504)
    result = base / ebitda.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043 ncfo/ebitda 63d minus 252d (cash earnings momentum)
def f46ieq_f46_industrial_earnings_quality_cepdiff_63m252_base_v043_signal(ncfo, ebitda, closeadj):
    short = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    long = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044 21d minus 63d cash earnings
def f46ieq_f46_industrial_earnings_quality_cepdiff_21m63_base_v044_signal(ncfo, ebitda, closeadj):
    short = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    long = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045 252d minus 504d cash earnings
def f46ieq_f46_industrial_earnings_quality_cepdiff_252m504_base_v045_signal(ncfo, ebitda, closeadj):
    short = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    long = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046 63d minus 252d accrual quality diff
def f46ieq_f46_industrial_earnings_quality_acqdiff_63m252_base_v046_signal(netinc, ncfo, assets, closeadj):
    short = _f46_accrual_quality(netinc, ncfo, assets, 63)
    long = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047 252d minus 504d accrual quality diff
def f46ieq_f46_industrial_earnings_quality_acqdiff_252m504_base_v047_signal(netinc, ncfo, assets, closeadj):
    short = _f46_accrual_quality(netinc, ncfo, assets, 252)
    long = _f46_accrual_quality(netinc, ncfo, assets, 504)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048 21d minus 63d accrual quality diff
def f46ieq_f46_industrial_earnings_quality_acqdiff_21m63_base_v048_signal(netinc, ncfo, assets, closeadj):
    short = _f46_accrual_quality(netinc, ncfo, assets, 21)
    long = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049 gap × volume
def f46ieq_f46_industrial_earnings_quality_acgapxvol_63d_base_v049_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050 gap weighted by netinc magnitude
def f46ieq_f46_industrial_earnings_quality_acgapxni_63d_base_v050_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base * np.sign(netinc) / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051 gap / assets ratio scaled
def f46ieq_f46_industrial_earnings_quality_acgap_assets_63d_base_v051_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / assets.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052 gap / assets 252d scaled
def f46ieq_f46_industrial_earnings_quality_acgap_assets_252d_base_v052_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = base / assets.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053 gap / assets 504d scaled
def f46ieq_f46_industrial_earnings_quality_acgap_assets_504d_base_v053_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 504)
    result = base / assets.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054 sign of gap × cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_signxcep_63d_base_v054_signal(netinc, ncfo, ebitda, closeadj):
    gap = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = np.sign(gap) * cep * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055 cash earnings × accrual quality (composite quality)
def f46ieq_f46_industrial_earnings_quality_qcomp_63d_base_v055_signal(netinc, ncfo, ebitda, assets, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 63)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056 252d composite quality
def f46ieq_f46_industrial_earnings_quality_qcomp_252d_base_v056_signal(netinc, ncfo, ebitda, assets, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057 504d composite quality
def f46ieq_f46_industrial_earnings_quality_qcomp_504d_base_v057_signal(netinc, ncfo, ebitda, assets, closeadj):
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 504)
    acq = _f46_accrual_quality(netinc, ncfo, assets, 504)
    result = (cep - acq) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058 raw netinc-ncfo / closeadj scaled (event-style)
def f46ieq_f46_industrial_earnings_quality_acgapraw_21d_base_v058_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    result = base * _mean(closeadj, 21) / closeadj.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v059 raw 252d gap × close-mean / close
def f46ieq_f46_industrial_earnings_quality_acgapraw_252d_base_v059_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = base * _mean(closeadj, 63) / closeadj.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v060 gap log magnitude
def f46ieq_f46_industrial_earnings_quality_acgaplog_252d_base_v060_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 252)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061 gap × log close
def f46ieq_f46_industrial_earnings_quality_acgapxlogc_63d_base_v061_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / netinc.abs().replace(0, np.nan) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062 EMA of gap
def f46ieq_f46_industrial_earnings_quality_acgapema_63d_base_v062_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    ema = base.ewm(span=63, adjust=False).mean()
    result = ema / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063 EMA of cash earnings proxy
def f46ieq_f46_industrial_earnings_quality_cepema_63d_base_v063_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 21)
    ema = base.ewm(span=63, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064 EMA 252d of accrual quality
def f46ieq_f46_industrial_earnings_quality_acqema_252d_base_v064_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 63)
    ema = base.ewm(span=252, adjust=False).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065 gap / sqrt(assets) scaled
def f46ieq_f46_industrial_earnings_quality_acgap_sqrtassets_63d_base_v065_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base / np.sqrt(assets.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066 abs gap × close
def f46ieq_f46_industrial_earnings_quality_absacgap_63d_base_v066_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    result = base.abs() / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067 squared gap × close
def f46ieq_f46_industrial_earnings_quality_sqacgap_63d_base_v067_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068 sign of cash earnings minus 1
def f46ieq_f46_industrial_earnings_quality_cepminus1_63d_base_v068_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069 cep level minus 1 252d
def f46ieq_f46_industrial_earnings_quality_cepminus1_252d_base_v069_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = (base - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070 product gap×cep
def f46ieq_f46_industrial_earnings_quality_gapxcep_63d_base_v070_signal(netinc, ncfo, ebitda, closeadj):
    gap = _f46_accrual_to_cash_gap(netinc, ncfo, 63) / netinc.abs().replace(0, np.nan)
    cep = _f46_cash_earnings_proxy(ncfo, ebitda, 63)
    result = gap * cep * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071 21d gap × volume scaled
def f46ieq_f46_industrial_earnings_quality_acgapxlogprice_21d_base_v071_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21) / netinc.abs().replace(0, np.nan)
    result = base * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072 252d cash earnings × log close
def f46ieq_f46_industrial_earnings_quality_cepxlogprice_252d_base_v072_signal(ncfo, ebitda, closeadj):
    base = _f46_cash_earnings_proxy(ncfo, ebitda, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073 accrual quality minus 0 scaled
def f46ieq_f46_industrial_earnings_quality_acqlevel_252d_base_v073_signal(netinc, ncfo, assets, closeadj):
    base = _f46_accrual_quality(netinc, ncfo, assets, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074 gap rolling-min over 63d scaled
def f46ieq_f46_industrial_earnings_quality_acgapmin_63d_base_v074_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 21)
    mn = base.rolling(63, min_periods=21).min() / closeadj.abs().replace(0, np.nan)
    result = mn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075 gap rolling-max over 252d scaled
def f46ieq_f46_industrial_earnings_quality_acgapmax_252d_base_v075_signal(netinc, ncfo, closeadj):
    base = _f46_accrual_to_cash_gap(netinc, ncfo, 63)
    mx = base.rolling(252, min_periods=63).max() / closeadj.abs().replace(0, np.nan)
    result = mx * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ieq_f46_industrial_earnings_quality_acgap_21d_base_v001_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_63d_base_v002_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_126d_base_v003_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_252d_base_v004_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_504d_base_v005_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_5d_base_v006_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_42d_base_v007_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_189d_base_v008_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_378d_base_v009_signal,
    f46ieq_f46_industrial_earnings_quality_acgapratio_63d_base_v010_signal,
    f46ieq_f46_industrial_earnings_quality_acgapratio_252d_base_v011_signal,
    f46ieq_f46_industrial_earnings_quality_acgapratio_504d_base_v012_signal,
    f46ieq_f46_industrial_earnings_quality_acq_21d_base_v013_signal,
    f46ieq_f46_industrial_earnings_quality_acq_63d_base_v014_signal,
    f46ieq_f46_industrial_earnings_quality_acq_126d_base_v015_signal,
    f46ieq_f46_industrial_earnings_quality_acq_252d_base_v016_signal,
    f46ieq_f46_industrial_earnings_quality_acq_504d_base_v017_signal,
    f46ieq_f46_industrial_earnings_quality_acq_42d_base_v018_signal,
    f46ieq_f46_industrial_earnings_quality_acq_189d_base_v019_signal,
    f46ieq_f46_industrial_earnings_quality_acq_378d_base_v020_signal,
    f46ieq_f46_industrial_earnings_quality_cep_21d_base_v021_signal,
    f46ieq_f46_industrial_earnings_quality_cep_63d_base_v022_signal,
    f46ieq_f46_industrial_earnings_quality_cep_126d_base_v023_signal,
    f46ieq_f46_industrial_earnings_quality_cep_252d_base_v024_signal,
    f46ieq_f46_industrial_earnings_quality_cep_504d_base_v025_signal,
    f46ieq_f46_industrial_earnings_quality_cep_5d_base_v026_signal,
    f46ieq_f46_industrial_earnings_quality_cep_42d_base_v027_signal,
    f46ieq_f46_industrial_earnings_quality_cep_189d_base_v028_signal,
    f46ieq_f46_industrial_earnings_quality_cep_378d_base_v029_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_63d_base_v030_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_252d_base_v031_signal,
    f46ieq_f46_industrial_earnings_quality_acgapz_21d_base_v032_signal,
    f46ieq_f46_industrial_earnings_quality_acqz_63d_base_v033_signal,
    f46ieq_f46_industrial_earnings_quality_acqz_252d_base_v034_signal,
    f46ieq_f46_industrial_earnings_quality_cepz_63d_base_v035_signal,
    f46ieq_f46_industrial_earnings_quality_cepz_252d_base_v036_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_63d_base_v037_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_252d_base_v038_signal,
    f46ieq_f46_industrial_earnings_quality_acgapstd_504d_base_v039_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_63d_base_v040_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_252d_base_v041_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_ebitda_504d_base_v042_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_63m252_base_v043_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_21m63_base_v044_signal,
    f46ieq_f46_industrial_earnings_quality_cepdiff_252m504_base_v045_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_63m252_base_v046_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_252m504_base_v047_signal,
    f46ieq_f46_industrial_earnings_quality_acqdiff_21m63_base_v048_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxvol_63d_base_v049_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxni_63d_base_v050_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_63d_base_v051_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_252d_base_v052_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_assets_504d_base_v053_signal,
    f46ieq_f46_industrial_earnings_quality_signxcep_63d_base_v054_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_63d_base_v055_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_252d_base_v056_signal,
    f46ieq_f46_industrial_earnings_quality_qcomp_504d_base_v057_signal,
    f46ieq_f46_industrial_earnings_quality_acgapraw_21d_base_v058_signal,
    f46ieq_f46_industrial_earnings_quality_acgapraw_252d_base_v059_signal,
    f46ieq_f46_industrial_earnings_quality_acgaplog_252d_base_v060_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogc_63d_base_v061_signal,
    f46ieq_f46_industrial_earnings_quality_acgapema_63d_base_v062_signal,
    f46ieq_f46_industrial_earnings_quality_cepema_63d_base_v063_signal,
    f46ieq_f46_industrial_earnings_quality_acqema_252d_base_v064_signal,
    f46ieq_f46_industrial_earnings_quality_acgap_sqrtassets_63d_base_v065_signal,
    f46ieq_f46_industrial_earnings_quality_absacgap_63d_base_v066_signal,
    f46ieq_f46_industrial_earnings_quality_sqacgap_63d_base_v067_signal,
    f46ieq_f46_industrial_earnings_quality_cepminus1_63d_base_v068_signal,
    f46ieq_f46_industrial_earnings_quality_cepminus1_252d_base_v069_signal,
    f46ieq_f46_industrial_earnings_quality_gapxcep_63d_base_v070_signal,
    f46ieq_f46_industrial_earnings_quality_acgapxlogprice_21d_base_v071_signal,
    f46ieq_f46_industrial_earnings_quality_cepxlogprice_252d_base_v072_signal,
    f46ieq_f46_industrial_earnings_quality_acqlevel_252d_base_v073_signal,
    f46ieq_f46_industrial_earnings_quality_acgapmin_63d_base_v074_signal,
    f46ieq_f46_industrial_earnings_quality_acgapmax_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_INDUSTRIAL_EARNINGS_QUALITY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f46_industrial_earnings_quality_base_001_075_claude: {n_features} features pass")
