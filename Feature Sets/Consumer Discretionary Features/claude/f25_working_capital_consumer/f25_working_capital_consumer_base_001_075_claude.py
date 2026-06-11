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
def _f25_wc_ratio(inventory, receivables, payables, revenue):
    wc = inventory + receivables - payables
    return wc / revenue.replace(0, np.nan)


def _f25_operating_cycle(inventory, receivables, payables, cor):
    dio = inventory / cor.replace(0, np.nan) * 365.0
    dso = receivables / cor.replace(0, np.nan) * 365.0
    dpo = payables / cor.replace(0, np.nan) * 365.0
    return dio + dso - dpo


def _f25_wc_efficiency(workingcapital, revenue, w):
    ratio = workingcapital / revenue.replace(0, np.nan)
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ratio.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return -((ratio - m) / sd)

# ===== features =====

def f25wcc_f25_working_capital_consumer_wcr_5d_base_v001_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_10d_base_v002_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_21d_base_v003_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_42d_base_v004_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_63d_base_v005_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_84d_base_v006_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_126d_base_v007_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_168d_base_v008_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_189d_base_v009_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_252d_base_v010_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_315d_base_v011_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_378d_base_v012_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_504d_base_v013_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_5d_base_v014_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_10d_base_v015_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_21d_base_v016_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_42d_base_v017_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_63d_base_v018_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_84d_base_v019_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_126d_base_v020_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_168d_base_v021_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_189d_base_v022_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_252d_base_v023_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_315d_base_v024_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_378d_base_v025_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_504d_base_v026_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_5d_base_v027_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_10d_base_v028_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_21d_base_v029_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_42d_base_v030_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_63d_base_v031_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_84d_base_v032_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_126d_base_v033_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_168d_base_v034_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_189d_base_v035_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_252d_base_v036_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_315d_base_v037_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_378d_base_v038_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_504d_base_v039_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_5d_base_v040_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_10d_base_v041_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_21d_base_v042_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_42d_base_v043_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_63d_base_v044_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_84d_base_v045_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_126d_base_v046_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_168d_base_v047_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_189d_base_v048_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_252d_base_v049_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_315d_base_v050_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 315) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_378d_base_v051_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_504d_base_v052_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_5d_base_v053_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 5) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_10d_base_v054_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 10) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_21d_base_v055_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 21) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_42d_base_v056_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 42) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_63d_base_v057_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 63) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_84d_base_v058_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 84) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_126d_base_v059_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 126) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_168d_base_v060_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 168) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_189d_base_v061_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 189) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_252d_base_v062_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 252) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_315d_base_v063_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 315) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_378d_base_v064_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 378) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_504d_base_v065_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 504) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_5d_base_v066_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 5) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_10d_base_v067_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 10) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_21d_base_v068_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 21) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_42d_base_v069_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 42) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_63d_base_v070_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 63) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_84d_base_v071_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 84) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_126d_base_v072_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 126) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_168d_base_v073_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 168) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_189d_base_v074_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 189) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_252d_base_v075_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 252) * (closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25wcc_f25_working_capital_consumer_wcr_5d_base_v001_signal,
    f25wcc_f25_working_capital_consumer_wcr_10d_base_v002_signal,
    f25wcc_f25_working_capital_consumer_wcr_21d_base_v003_signal,
    f25wcc_f25_working_capital_consumer_wcr_42d_base_v004_signal,
    f25wcc_f25_working_capital_consumer_wcr_63d_base_v005_signal,
    f25wcc_f25_working_capital_consumer_wcr_84d_base_v006_signal,
    f25wcc_f25_working_capital_consumer_wcr_126d_base_v007_signal,
    f25wcc_f25_working_capital_consumer_wcr_168d_base_v008_signal,
    f25wcc_f25_working_capital_consumer_wcr_189d_base_v009_signal,
    f25wcc_f25_working_capital_consumer_wcr_252d_base_v010_signal,
    f25wcc_f25_working_capital_consumer_wcr_315d_base_v011_signal,
    f25wcc_f25_working_capital_consumer_wcr_378d_base_v012_signal,
    f25wcc_f25_working_capital_consumer_wcr_504d_base_v013_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_5d_base_v014_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_10d_base_v015_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_21d_base_v016_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_42d_base_v017_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_63d_base_v018_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_84d_base_v019_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_126d_base_v020_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_168d_base_v021_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_189d_base_v022_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_252d_base_v023_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_315d_base_v024_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_378d_base_v025_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_504d_base_v026_signal,
    f25wcc_f25_working_capital_consumer_wcrema_5d_base_v027_signal,
    f25wcc_f25_working_capital_consumer_wcrema_10d_base_v028_signal,
    f25wcc_f25_working_capital_consumer_wcrema_21d_base_v029_signal,
    f25wcc_f25_working_capital_consumer_wcrema_42d_base_v030_signal,
    f25wcc_f25_working_capital_consumer_wcrema_63d_base_v031_signal,
    f25wcc_f25_working_capital_consumer_wcrema_84d_base_v032_signal,
    f25wcc_f25_working_capital_consumer_wcrema_126d_base_v033_signal,
    f25wcc_f25_working_capital_consumer_wcrema_168d_base_v034_signal,
    f25wcc_f25_working_capital_consumer_wcrema_189d_base_v035_signal,
    f25wcc_f25_working_capital_consumer_wcrema_252d_base_v036_signal,
    f25wcc_f25_working_capital_consumer_wcrema_315d_base_v037_signal,
    f25wcc_f25_working_capital_consumer_wcrema_378d_base_v038_signal,
    f25wcc_f25_working_capital_consumer_wcrema_504d_base_v039_signal,
    f25wcc_f25_working_capital_consumer_wcrz_5d_base_v040_signal,
    f25wcc_f25_working_capital_consumer_wcrz_10d_base_v041_signal,
    f25wcc_f25_working_capital_consumer_wcrz_21d_base_v042_signal,
    f25wcc_f25_working_capital_consumer_wcrz_42d_base_v043_signal,
    f25wcc_f25_working_capital_consumer_wcrz_63d_base_v044_signal,
    f25wcc_f25_working_capital_consumer_wcrz_84d_base_v045_signal,
    f25wcc_f25_working_capital_consumer_wcrz_126d_base_v046_signal,
    f25wcc_f25_working_capital_consumer_wcrz_168d_base_v047_signal,
    f25wcc_f25_working_capital_consumer_wcrz_189d_base_v048_signal,
    f25wcc_f25_working_capital_consumer_wcrz_252d_base_v049_signal,
    f25wcc_f25_working_capital_consumer_wcrz_315d_base_v050_signal,
    f25wcc_f25_working_capital_consumer_wcrz_378d_base_v051_signal,
    f25wcc_f25_working_capital_consumer_wcrz_504d_base_v052_signal,
    f25wcc_f25_working_capital_consumer_opcyc_5d_base_v053_signal,
    f25wcc_f25_working_capital_consumer_opcyc_10d_base_v054_signal,
    f25wcc_f25_working_capital_consumer_opcyc_21d_base_v055_signal,
    f25wcc_f25_working_capital_consumer_opcyc_42d_base_v056_signal,
    f25wcc_f25_working_capital_consumer_opcyc_63d_base_v057_signal,
    f25wcc_f25_working_capital_consumer_opcyc_84d_base_v058_signal,
    f25wcc_f25_working_capital_consumer_opcyc_126d_base_v059_signal,
    f25wcc_f25_working_capital_consumer_opcyc_168d_base_v060_signal,
    f25wcc_f25_working_capital_consumer_opcyc_189d_base_v061_signal,
    f25wcc_f25_working_capital_consumer_opcyc_252d_base_v062_signal,
    f25wcc_f25_working_capital_consumer_opcyc_315d_base_v063_signal,
    f25wcc_f25_working_capital_consumer_opcyc_378d_base_v064_signal,
    f25wcc_f25_working_capital_consumer_opcyc_504d_base_v065_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_5d_base_v066_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_10d_base_v067_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_21d_base_v068_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_42d_base_v069_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_63d_base_v070_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_84d_base_v071_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_126d_base_v072_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_168d_base_v073_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_189d_base_v074_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_WORKING_CAPITAL_CONSUMER_REGISTRY_001_075 = REGISTRY


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
        "inventory": inventory,
        "receivables": receivables,
        "payables": payables,
        "revenue": revenue,
        "closeadj": closeadj,
        "cor": cor,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_wc_ratio", "_f25_operating_cycle", "_f25_wc_efficiency",)
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
    print(f"OK f25_working_capital_consumer_base_001_075_claude: {n_features} features pass")
