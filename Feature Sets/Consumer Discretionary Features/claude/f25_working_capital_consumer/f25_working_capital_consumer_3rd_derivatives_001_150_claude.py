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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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

def f25wcc_f25_working_capital_consumer_wcr_5d_jw5_jerk_v001_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 5) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_10d_jw10_jerk_v002_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 10) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_21d_jw21_jerk_v003_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 21) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_42d_jw42_jerk_v004_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 42) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_63d_jw63_jerk_v005_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 63) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_84d_jw126_jerk_v006_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 84) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_126d_jw5_jerk_v007_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 126) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_168d_jw10_jerk_v008_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 168) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_189d_jw21_jerk_v009_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 189) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_252d_jw42_jerk_v010_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 252) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_315d_jw63_jerk_v011_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 315) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_378d_jw126_jerk_v012_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 378) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcr_504d_jw5_jerk_v013_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _mean(base, 504) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_5d_jw10_jerk_v014_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 5) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_10d_jw21_jerk_v015_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 10) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_21d_jw42_jerk_v016_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 21) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_42d_jw63_jerk_v017_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 42) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_63d_jw126_jerk_v018_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 63) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_84d_jw5_jerk_v019_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 84) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_126d_jw10_jerk_v020_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 126) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_168d_jw21_jerk_v021_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 168) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_189d_jw42_jerk_v022_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 189) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_252d_jw63_jerk_v023_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 252) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_315d_jw126_jerk_v024_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 315) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_378d_jw5_jerk_v025_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 378) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrstd_504d_jw10_jerk_v026_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _std(base, 504) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_5d_jw21_jerk_v027_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 5) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_10d_jw42_jerk_v028_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 10) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_21d_jw63_jerk_v029_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 21) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_42d_jw126_jerk_v030_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 42) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_63d_jw5_jerk_v031_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 63) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_84d_jw10_jerk_v032_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 84) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_126d_jw21_jerk_v033_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 126) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_168d_jw42_jerk_v034_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 168) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_189d_jw63_jerk_v035_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 189) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_252d_jw126_jerk_v036_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 252) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_315d_jw5_jerk_v037_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 315) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_378d_jw10_jerk_v038_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 378) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrema_504d_jw21_jerk_v039_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _ema(base, 504) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_5d_jw42_jerk_v040_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 5) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_10d_jw63_jerk_v041_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 10) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_21d_jw126_jerk_v042_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 21) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_42d_jw5_jerk_v043_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 42) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_63d_jw10_jerk_v044_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 63) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_84d_jw21_jerk_v045_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 84) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_126d_jw42_jerk_v046_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 126) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_168d_jw63_jerk_v047_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 168) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_189d_jw126_jerk_v048_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 189) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_252d_jw5_jerk_v049_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 252) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_315d_jw10_jerk_v050_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 315) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_378d_jw21_jerk_v051_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 378) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrz_504d_jw42_jerk_v052_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    result = _z(base, 504) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_5d_jw63_jerk_v053_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_10d_jw126_jerk_v054_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_21d_jw5_jerk_v055_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_42d_jw10_jerk_v056_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_63d_jw21_jerk_v057_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_84d_jw42_jerk_v058_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_126d_jw63_jerk_v059_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_168d_jw126_jerk_v060_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 168) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_189d_jw5_jerk_v061_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 189) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_252d_jw10_jerk_v062_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 252) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_315d_jw21_jerk_v063_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 315) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_378d_jw42_jerk_v064_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 378) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcyc_504d_jw63_jerk_v065_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 504) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_5d_jw126_jerk_v066_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_10d_jw5_jerk_v067_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_21d_jw10_jerk_v068_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_42d_jw21_jerk_v069_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_63d_jw42_jerk_v070_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_84d_jw63_jerk_v071_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_126d_jw126_jerk_v072_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_168d_jw5_jerk_v073_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 168) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_189d_jw10_jerk_v074_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 189) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_252d_jw21_jerk_v075_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 252) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_315d_jw42_jerk_v076_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 315) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_378d_jw63_jerk_v077_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 378) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycstd_504d_jw126_jerk_v078_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _std(base, 504) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_5d_jw5_jerk_v079_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 5) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_10d_jw10_jerk_v080_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 10) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_21d_jw21_jerk_v081_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 21) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_42d_jw42_jerk_v082_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 42) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_63d_jw63_jerk_v083_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 63) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_84d_jw126_jerk_v084_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 84) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_126d_jw5_jerk_v085_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 126) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_168d_jw10_jerk_v086_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 168) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_189d_jw21_jerk_v087_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 189) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_252d_jw42_jerk_v088_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 252) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_315d_jw63_jerk_v089_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 315) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_378d_jw126_jerk_v090_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 378) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycz_504d_jw5_jerk_v091_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _z(base, 504) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_5d_jw10_jerk_v092_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 5) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_10d_jw21_jerk_v093_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 10) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_21d_jw42_jerk_v094_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 21) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_42d_jw63_jerk_v095_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 42) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_63d_jw126_jerk_v096_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 63) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_84d_jw5_jerk_v097_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 84) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_126d_jw10_jerk_v098_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 126) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_168d_jw21_jerk_v099_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 168) * (closeadj / 100.0)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_189d_jw42_jerk_v100_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 189) * (closeadj / 100.0)
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_252d_jw63_jerk_v101_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 252) * (closeadj / 100.0)
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_315d_jw126_jerk_v102_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 315) * (closeadj / 100.0)
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_378d_jw5_jerk_v103_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 378) * (closeadj / 100.0)
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_opcycema_504d_jw10_jerk_v104_signal(inventory, receivables, payables, cor, closeadj):
    base = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _ema(base, 504) * (closeadj / 100.0)
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_5d_jw21_jerk_v105_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_10d_jw42_jerk_v106_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_21d_jw63_jerk_v107_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_42d_jw126_jerk_v108_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_63d_jw5_jerk_v109_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_84d_jw10_jerk_v110_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_126d_jw21_jerk_v111_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_168d_jw42_jerk_v112_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_189d_jw63_jerk_v113_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_252d_jw126_jerk_v114_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_315d_jw5_jerk_v115_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_378d_jw10_jerk_v116_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceff_504d_jw21_jerk_v117_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_5d_jw42_jerk_v118_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = _ema(base, 5) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_10d_jw63_jerk_v119_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = _ema(base, 10) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_21d_jw126_jerk_v120_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = _ema(base, 21) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_42d_jw5_jerk_v121_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = _ema(base, 42) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_63d_jw10_jerk_v122_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = _ema(base, 63) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_84d_jw21_jerk_v123_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = _ema(base, 84) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_126d_jw42_jerk_v124_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = _ema(base, 126) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_168d_jw63_jerk_v125_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = _ema(base, 168) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_189d_jw126_jerk_v126_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = _ema(base, 189) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_252d_jw5_jerk_v127_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = _ema(base, 252) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_315d_jw10_jerk_v128_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = _ema(base, 315) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_378d_jw21_jerk_v129_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = _ema(base, 378) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffema_504d_jw42_jerk_v130_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = _ema(base, 504) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_5d_jw63_jerk_v131_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 5)
    result = _std(base, 5) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_10d_jw126_jerk_v132_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 10)
    result = _std(base, 10) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_21d_jw5_jerk_v133_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 21)
    result = _std(base, 21) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_42d_jw10_jerk_v134_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 42)
    result = _std(base, 42) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_63d_jw21_jerk_v135_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 63)
    result = _std(base, 63) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_84d_jw42_jerk_v136_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 84)
    result = _std(base, 84) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_126d_jw63_jerk_v137_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 126)
    result = _std(base, 126) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_168d_jw126_jerk_v138_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 168)
    result = _std(base, 168) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_189d_jw5_jerk_v139_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 189)
    result = _std(base, 189) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_252d_jw10_jerk_v140_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 252)
    result = _std(base, 252) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_315d_jw21_jerk_v141_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 315)
    result = _std(base, 315) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_378d_jw42_jerk_v142_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 378)
    result = _std(base, 378) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wceffstd_504d_jw63_jerk_v143_signal(workingcapital, revenue, closeadj):
    base = _f25_wc_efficiency(workingcapital, revenue, 504)
    result = _std(base, 504) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_5d_jw126_jerk_v144_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 5) * _mean(oc, 5) / 365.0 * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_10d_jw5_jerk_v145_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 10) * _mean(oc, 10) / 365.0 * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_21d_jw10_jerk_v146_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 21) * _mean(oc, 21) / 365.0 * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_42d_jw21_jerk_v147_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 42) * _mean(oc, 42) / 365.0 * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_63d_jw42_jerk_v148_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 63) * _mean(oc, 63) / 365.0 * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_84d_jw63_jerk_v149_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 84) * _mean(oc, 84) / 365.0 * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f25wcc_f25_working_capital_consumer_wcrxopcyc_126d_jw126_jerk_v150_signal(inventory, receivables, payables, revenue, cor, closeadj):
    base = _f25_wc_ratio(inventory, receivables, payables, revenue)
    oc = _f25_operating_cycle(inventory, receivables, payables, cor)
    result = _mean(base, 126) * _mean(oc, 126) / 365.0 * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25wcc_f25_working_capital_consumer_wcr_5d_jw5_jerk_v001_signal,
    f25wcc_f25_working_capital_consumer_wcr_10d_jw10_jerk_v002_signal,
    f25wcc_f25_working_capital_consumer_wcr_21d_jw21_jerk_v003_signal,
    f25wcc_f25_working_capital_consumer_wcr_42d_jw42_jerk_v004_signal,
    f25wcc_f25_working_capital_consumer_wcr_63d_jw63_jerk_v005_signal,
    f25wcc_f25_working_capital_consumer_wcr_84d_jw126_jerk_v006_signal,
    f25wcc_f25_working_capital_consumer_wcr_126d_jw5_jerk_v007_signal,
    f25wcc_f25_working_capital_consumer_wcr_168d_jw10_jerk_v008_signal,
    f25wcc_f25_working_capital_consumer_wcr_189d_jw21_jerk_v009_signal,
    f25wcc_f25_working_capital_consumer_wcr_252d_jw42_jerk_v010_signal,
    f25wcc_f25_working_capital_consumer_wcr_315d_jw63_jerk_v011_signal,
    f25wcc_f25_working_capital_consumer_wcr_378d_jw126_jerk_v012_signal,
    f25wcc_f25_working_capital_consumer_wcr_504d_jw5_jerk_v013_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_5d_jw10_jerk_v014_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_10d_jw21_jerk_v015_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_21d_jw42_jerk_v016_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_42d_jw63_jerk_v017_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_63d_jw126_jerk_v018_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_84d_jw5_jerk_v019_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_126d_jw10_jerk_v020_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_168d_jw21_jerk_v021_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_189d_jw42_jerk_v022_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_252d_jw63_jerk_v023_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_315d_jw126_jerk_v024_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_378d_jw5_jerk_v025_signal,
    f25wcc_f25_working_capital_consumer_wcrstd_504d_jw10_jerk_v026_signal,
    f25wcc_f25_working_capital_consumer_wcrema_5d_jw21_jerk_v027_signal,
    f25wcc_f25_working_capital_consumer_wcrema_10d_jw42_jerk_v028_signal,
    f25wcc_f25_working_capital_consumer_wcrema_21d_jw63_jerk_v029_signal,
    f25wcc_f25_working_capital_consumer_wcrema_42d_jw126_jerk_v030_signal,
    f25wcc_f25_working_capital_consumer_wcrema_63d_jw5_jerk_v031_signal,
    f25wcc_f25_working_capital_consumer_wcrema_84d_jw10_jerk_v032_signal,
    f25wcc_f25_working_capital_consumer_wcrema_126d_jw21_jerk_v033_signal,
    f25wcc_f25_working_capital_consumer_wcrema_168d_jw42_jerk_v034_signal,
    f25wcc_f25_working_capital_consumer_wcrema_189d_jw63_jerk_v035_signal,
    f25wcc_f25_working_capital_consumer_wcrema_252d_jw126_jerk_v036_signal,
    f25wcc_f25_working_capital_consumer_wcrema_315d_jw5_jerk_v037_signal,
    f25wcc_f25_working_capital_consumer_wcrema_378d_jw10_jerk_v038_signal,
    f25wcc_f25_working_capital_consumer_wcrema_504d_jw21_jerk_v039_signal,
    f25wcc_f25_working_capital_consumer_wcrz_5d_jw42_jerk_v040_signal,
    f25wcc_f25_working_capital_consumer_wcrz_10d_jw63_jerk_v041_signal,
    f25wcc_f25_working_capital_consumer_wcrz_21d_jw126_jerk_v042_signal,
    f25wcc_f25_working_capital_consumer_wcrz_42d_jw5_jerk_v043_signal,
    f25wcc_f25_working_capital_consumer_wcrz_63d_jw10_jerk_v044_signal,
    f25wcc_f25_working_capital_consumer_wcrz_84d_jw21_jerk_v045_signal,
    f25wcc_f25_working_capital_consumer_wcrz_126d_jw42_jerk_v046_signal,
    f25wcc_f25_working_capital_consumer_wcrz_168d_jw63_jerk_v047_signal,
    f25wcc_f25_working_capital_consumer_wcrz_189d_jw126_jerk_v048_signal,
    f25wcc_f25_working_capital_consumer_wcrz_252d_jw5_jerk_v049_signal,
    f25wcc_f25_working_capital_consumer_wcrz_315d_jw10_jerk_v050_signal,
    f25wcc_f25_working_capital_consumer_wcrz_378d_jw21_jerk_v051_signal,
    f25wcc_f25_working_capital_consumer_wcrz_504d_jw42_jerk_v052_signal,
    f25wcc_f25_working_capital_consumer_opcyc_5d_jw63_jerk_v053_signal,
    f25wcc_f25_working_capital_consumer_opcyc_10d_jw126_jerk_v054_signal,
    f25wcc_f25_working_capital_consumer_opcyc_21d_jw5_jerk_v055_signal,
    f25wcc_f25_working_capital_consumer_opcyc_42d_jw10_jerk_v056_signal,
    f25wcc_f25_working_capital_consumer_opcyc_63d_jw21_jerk_v057_signal,
    f25wcc_f25_working_capital_consumer_opcyc_84d_jw42_jerk_v058_signal,
    f25wcc_f25_working_capital_consumer_opcyc_126d_jw63_jerk_v059_signal,
    f25wcc_f25_working_capital_consumer_opcyc_168d_jw126_jerk_v060_signal,
    f25wcc_f25_working_capital_consumer_opcyc_189d_jw5_jerk_v061_signal,
    f25wcc_f25_working_capital_consumer_opcyc_252d_jw10_jerk_v062_signal,
    f25wcc_f25_working_capital_consumer_opcyc_315d_jw21_jerk_v063_signal,
    f25wcc_f25_working_capital_consumer_opcyc_378d_jw42_jerk_v064_signal,
    f25wcc_f25_working_capital_consumer_opcyc_504d_jw63_jerk_v065_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_5d_jw126_jerk_v066_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_10d_jw5_jerk_v067_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_21d_jw10_jerk_v068_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_42d_jw21_jerk_v069_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_63d_jw42_jerk_v070_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_84d_jw63_jerk_v071_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_126d_jw126_jerk_v072_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_168d_jw5_jerk_v073_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_189d_jw10_jerk_v074_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_252d_jw21_jerk_v075_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_315d_jw42_jerk_v076_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_378d_jw63_jerk_v077_signal,
    f25wcc_f25_working_capital_consumer_opcycstd_504d_jw126_jerk_v078_signal,
    f25wcc_f25_working_capital_consumer_opcycz_5d_jw5_jerk_v079_signal,
    f25wcc_f25_working_capital_consumer_opcycz_10d_jw10_jerk_v080_signal,
    f25wcc_f25_working_capital_consumer_opcycz_21d_jw21_jerk_v081_signal,
    f25wcc_f25_working_capital_consumer_opcycz_42d_jw42_jerk_v082_signal,
    f25wcc_f25_working_capital_consumer_opcycz_63d_jw63_jerk_v083_signal,
    f25wcc_f25_working_capital_consumer_opcycz_84d_jw126_jerk_v084_signal,
    f25wcc_f25_working_capital_consumer_opcycz_126d_jw5_jerk_v085_signal,
    f25wcc_f25_working_capital_consumer_opcycz_168d_jw10_jerk_v086_signal,
    f25wcc_f25_working_capital_consumer_opcycz_189d_jw21_jerk_v087_signal,
    f25wcc_f25_working_capital_consumer_opcycz_252d_jw42_jerk_v088_signal,
    f25wcc_f25_working_capital_consumer_opcycz_315d_jw63_jerk_v089_signal,
    f25wcc_f25_working_capital_consumer_opcycz_378d_jw126_jerk_v090_signal,
    f25wcc_f25_working_capital_consumer_opcycz_504d_jw5_jerk_v091_signal,
    f25wcc_f25_working_capital_consumer_opcycema_5d_jw10_jerk_v092_signal,
    f25wcc_f25_working_capital_consumer_opcycema_10d_jw21_jerk_v093_signal,
    f25wcc_f25_working_capital_consumer_opcycema_21d_jw42_jerk_v094_signal,
    f25wcc_f25_working_capital_consumer_opcycema_42d_jw63_jerk_v095_signal,
    f25wcc_f25_working_capital_consumer_opcycema_63d_jw126_jerk_v096_signal,
    f25wcc_f25_working_capital_consumer_opcycema_84d_jw5_jerk_v097_signal,
    f25wcc_f25_working_capital_consumer_opcycema_126d_jw10_jerk_v098_signal,
    f25wcc_f25_working_capital_consumer_opcycema_168d_jw21_jerk_v099_signal,
    f25wcc_f25_working_capital_consumer_opcycema_189d_jw42_jerk_v100_signal,
    f25wcc_f25_working_capital_consumer_opcycema_252d_jw63_jerk_v101_signal,
    f25wcc_f25_working_capital_consumer_opcycema_315d_jw126_jerk_v102_signal,
    f25wcc_f25_working_capital_consumer_opcycema_378d_jw5_jerk_v103_signal,
    f25wcc_f25_working_capital_consumer_opcycema_504d_jw10_jerk_v104_signal,
    f25wcc_f25_working_capital_consumer_wceff_5d_jw21_jerk_v105_signal,
    f25wcc_f25_working_capital_consumer_wceff_10d_jw42_jerk_v106_signal,
    f25wcc_f25_working_capital_consumer_wceff_21d_jw63_jerk_v107_signal,
    f25wcc_f25_working_capital_consumer_wceff_42d_jw126_jerk_v108_signal,
    f25wcc_f25_working_capital_consumer_wceff_63d_jw5_jerk_v109_signal,
    f25wcc_f25_working_capital_consumer_wceff_84d_jw10_jerk_v110_signal,
    f25wcc_f25_working_capital_consumer_wceff_126d_jw21_jerk_v111_signal,
    f25wcc_f25_working_capital_consumer_wceff_168d_jw42_jerk_v112_signal,
    f25wcc_f25_working_capital_consumer_wceff_189d_jw63_jerk_v113_signal,
    f25wcc_f25_working_capital_consumer_wceff_252d_jw126_jerk_v114_signal,
    f25wcc_f25_working_capital_consumer_wceff_315d_jw5_jerk_v115_signal,
    f25wcc_f25_working_capital_consumer_wceff_378d_jw10_jerk_v116_signal,
    f25wcc_f25_working_capital_consumer_wceff_504d_jw21_jerk_v117_signal,
    f25wcc_f25_working_capital_consumer_wceffema_5d_jw42_jerk_v118_signal,
    f25wcc_f25_working_capital_consumer_wceffema_10d_jw63_jerk_v119_signal,
    f25wcc_f25_working_capital_consumer_wceffema_21d_jw126_jerk_v120_signal,
    f25wcc_f25_working_capital_consumer_wceffema_42d_jw5_jerk_v121_signal,
    f25wcc_f25_working_capital_consumer_wceffema_63d_jw10_jerk_v122_signal,
    f25wcc_f25_working_capital_consumer_wceffema_84d_jw21_jerk_v123_signal,
    f25wcc_f25_working_capital_consumer_wceffema_126d_jw42_jerk_v124_signal,
    f25wcc_f25_working_capital_consumer_wceffema_168d_jw63_jerk_v125_signal,
    f25wcc_f25_working_capital_consumer_wceffema_189d_jw126_jerk_v126_signal,
    f25wcc_f25_working_capital_consumer_wceffema_252d_jw5_jerk_v127_signal,
    f25wcc_f25_working_capital_consumer_wceffema_315d_jw10_jerk_v128_signal,
    f25wcc_f25_working_capital_consumer_wceffema_378d_jw21_jerk_v129_signal,
    f25wcc_f25_working_capital_consumer_wceffema_504d_jw42_jerk_v130_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_5d_jw63_jerk_v131_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_10d_jw126_jerk_v132_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_21d_jw5_jerk_v133_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_42d_jw10_jerk_v134_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_63d_jw21_jerk_v135_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_84d_jw42_jerk_v136_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_126d_jw63_jerk_v137_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_168d_jw126_jerk_v138_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_189d_jw5_jerk_v139_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_252d_jw10_jerk_v140_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_315d_jw21_jerk_v141_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_378d_jw42_jerk_v142_signal,
    f25wcc_f25_working_capital_consumer_wceffstd_504d_jw63_jerk_v143_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_5d_jw126_jerk_v144_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_10d_jw5_jerk_v145_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_21d_jw10_jerk_v146_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_42d_jw21_jerk_v147_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_63d_jw42_jerk_v148_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_84d_jw63_jerk_v149_signal,
    f25wcc_f25_working_capital_consumer_wcrxopcyc_126d_jw126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_WORKING_CAPITAL_CONSUMER_REGISTRY_JERK_001_150 = REGISTRY


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
        "workingcapital": workingcapital,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f25_working_capital_consumer_3rd_derivatives_001_150_claude: {n_features} features pass")
