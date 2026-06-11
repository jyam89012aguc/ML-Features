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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f48_cycle_proxy(opex, revenue, w):
    r = opex / revenue.replace(0, np.nan).abs()
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f48_market_phase(netmargin, revenue, w):
    m = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    g = revenue.pct_change(periods=w)
    return m + g


def _f48_cycle_score(opex, revenue, w):
    r = opex / revenue.replace(0, np.nan).abs()
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    mu = r.rolling(w, min_periods=max(1, w // 2)).mean()
    return (r - mu) / sd.replace(0, np.nan)


def imc_f48_insurance_market_cycle_cp_close_raw_5d_jw5_jerk_v001_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 5)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_5d_jw21_jerk_v002_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 5)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_5d_jw63_jerk_v003_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 5)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_10d_jw5_jerk_v004_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 10)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_10d_jw21_jerk_v005_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 10)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_10d_jw63_jerk_v006_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 10)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_21d_jw5_jerk_v007_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 21)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_21d_jw21_jerk_v008_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 21)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_21d_jw63_jerk_v009_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 21)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_42d_jw5_jerk_v010_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 42)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_42d_jw21_jerk_v011_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 42)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_42d_jw63_jerk_v012_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 42)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_63d_jw5_jerk_v013_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 63)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_63d_jw21_jerk_v014_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 63)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_63d_jw63_jerk_v015_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 63)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_126d_jw5_jerk_v016_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 126)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_126d_jw21_jerk_v017_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 126)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_126d_jw63_jerk_v018_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 126)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_189d_jw5_jerk_v019_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 189)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_189d_jw21_jerk_v020_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 189)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_189d_jw63_jerk_v021_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 189)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_252d_jw5_jerk_v022_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 252)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_252d_jw21_jerk_v023_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 252)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_252d_jw63_jerk_v024_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 252)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_378d_jw5_jerk_v025_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 378)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_378d_jw21_jerk_v026_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 378)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_378d_jw63_jerk_v027_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 378)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_raw_504d_jw5_jerk_v028_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 504)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_raw_504d_jw21_jerk_v029_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 504)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_raw_504d_jw63_jerk_v030_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 504)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_5d_jw5_jerk_v031_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 5)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_5d_jw21_jerk_v032_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 5)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_5d_jw63_jerk_v033_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 5)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_10d_jw5_jerk_v034_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 10)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_10d_jw21_jerk_v035_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 10)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_10d_jw63_jerk_v036_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 10)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_21d_jw5_jerk_v037_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 21)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_21d_jw21_jerk_v038_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 21)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_21d_jw63_jerk_v039_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 21)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_42d_jw5_jerk_v040_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 42)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_42d_jw21_jerk_v041_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 42)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_42d_jw63_jerk_v042_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 42)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_63d_jw5_jerk_v043_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 63)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_63d_jw21_jerk_v044_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 63)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_63d_jw63_jerk_v045_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 63)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_126d_jw5_jerk_v046_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 126)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_126d_jw21_jerk_v047_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 126)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_126d_jw63_jerk_v048_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 126)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_189d_jw5_jerk_v049_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 189)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_189d_jw21_jerk_v050_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 189)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_189d_jw63_jerk_v051_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 189)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_252d_jw5_jerk_v052_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 252)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_252d_jw21_jerk_v053_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 252)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_252d_jw63_jerk_v054_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 252)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_378d_jw5_jerk_v055_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 378)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_378d_jw21_jerk_v056_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 378)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_378d_jw63_jerk_v057_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 378)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_sq_raw_504d_jw5_jerk_v058_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 504)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_sq_raw_504d_jw21_jerk_v059_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 504)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_sq_raw_504d_jw63_jerk_v060_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 504)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_5d_jw5_jerk_v061_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_5d_jw21_jerk_v062_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_5d_jw63_jerk_v063_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_10d_jw5_jerk_v064_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_10d_jw21_jerk_v065_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_10d_jw63_jerk_v066_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_21d_jw5_jerk_v067_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_21d_jw21_jerk_v068_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_21d_jw63_jerk_v069_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_42d_jw5_jerk_v070_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_42d_jw21_jerk_v071_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_42d_jw63_jerk_v072_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_63d_jw5_jerk_v073_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_63d_jw21_jerk_v074_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_63d_jw63_jerk_v075_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_126d_jw5_jerk_v076_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_126d_jw21_jerk_v077_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_126d_jw63_jerk_v078_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_189d_jw5_jerk_v079_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_189d_jw21_jerk_v080_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_189d_jw63_jerk_v081_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_252d_jw5_jerk_v082_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_252d_jw21_jerk_v083_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_252d_jw63_jerk_v084_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_378d_jw5_jerk_v085_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_378d_jw21_jerk_v086_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_378d_jw63_jerk_v087_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_log_raw_504d_jw5_jerk_v088_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_log_raw_504d_jw21_jerk_v089_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_log_raw_504d_jw63_jerk_v090_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_5d_jw5_jerk_v091_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_5d_jw21_jerk_v092_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_5d_jw63_jerk_v093_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_10d_jw5_jerk_v094_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_10d_jw21_jerk_v095_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_10d_jw63_jerk_v096_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_21d_jw5_jerk_v097_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_21d_jw21_jerk_v098_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_21d_jw63_jerk_v099_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_42d_jw5_jerk_v100_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_42d_jw21_jerk_v101_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_42d_jw63_jerk_v102_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_63d_jw5_jerk_v103_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_63d_jw21_jerk_v104_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_63d_jw63_jerk_v105_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_126d_jw5_jerk_v106_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_126d_jw21_jerk_v107_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_126d_jw63_jerk_v108_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_189d_jw5_jerk_v109_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_189d_jw21_jerk_v110_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_189d_jw63_jerk_v111_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_252d_jw5_jerk_v112_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_252d_jw21_jerk_v113_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_252d_jw63_jerk_v114_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_378d_jw5_jerk_v115_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_378d_jw21_jerk_v116_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_378d_jw63_jerk_v117_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean21_raw_504d_jw5_jerk_v118_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean21_raw_504d_jw21_jerk_v119_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean21_raw_504d_jw63_jerk_v120_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_5d_jw5_jerk_v121_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_5d_jw21_jerk_v122_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_5d_jw63_jerk_v123_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_10d_jw5_jerk_v124_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_10d_jw21_jerk_v125_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_10d_jw63_jerk_v126_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_21d_jw5_jerk_v127_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_21d_jw21_jerk_v128_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_21d_jw63_jerk_v129_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_42d_jw5_jerk_v130_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_42d_jw21_jerk_v131_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_42d_jw63_jerk_v132_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_63d_jw5_jerk_v133_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_63d_jw21_jerk_v134_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_63d_jw63_jerk_v135_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_126d_jw5_jerk_v136_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_126d_jw21_jerk_v137_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_126d_jw63_jerk_v138_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_189d_jw5_jerk_v139_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_189d_jw21_jerk_v140_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_189d_jw63_jerk_v141_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_252d_jw5_jerk_v142_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_252d_jw21_jerk_v143_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_252d_jw63_jerk_v144_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_378d_jw5_jerk_v145_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_378d_jw21_jerk_v146_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_378d_jw63_jerk_v147_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cp_close_mean63_raw_504d_jw5_jerk_v148_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_proxy(opex, revenue, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_mp_close_mean63_raw_504d_jw21_jerk_v149_signal(netmargin, revenue, closeadj):
    _b = (_f48_market_phase(netmargin, revenue, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def imc_f48_insurance_market_cycle_cs_close_mean63_raw_504d_jw63_jerk_v150_signal(opex, revenue, closeadj):
    _b = (_f48_cycle_score(opex, revenue, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    imc_f48_insurance_market_cycle_cp_close_raw_5d_jw5_jerk_v001_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_5d_jw21_jerk_v002_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_5d_jw63_jerk_v003_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_10d_jw5_jerk_v004_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_10d_jw21_jerk_v005_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_10d_jw63_jerk_v006_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_21d_jw5_jerk_v007_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_21d_jw21_jerk_v008_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_21d_jw63_jerk_v009_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_42d_jw5_jerk_v010_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_42d_jw21_jerk_v011_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_42d_jw63_jerk_v012_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_63d_jw5_jerk_v013_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_63d_jw21_jerk_v014_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_63d_jw63_jerk_v015_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_126d_jw5_jerk_v016_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_126d_jw21_jerk_v017_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_126d_jw63_jerk_v018_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_189d_jw5_jerk_v019_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_189d_jw21_jerk_v020_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_189d_jw63_jerk_v021_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_252d_jw5_jerk_v022_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_252d_jw21_jerk_v023_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_252d_jw63_jerk_v024_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_378d_jw5_jerk_v025_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_378d_jw21_jerk_v026_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_378d_jw63_jerk_v027_signal,
    imc_f48_insurance_market_cycle_cp_close_raw_504d_jw5_jerk_v028_signal,
    imc_f48_insurance_market_cycle_mp_close_raw_504d_jw21_jerk_v029_signal,
    imc_f48_insurance_market_cycle_cs_close_raw_504d_jw63_jerk_v030_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_5d_jw5_jerk_v031_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_5d_jw21_jerk_v032_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_5d_jw63_jerk_v033_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_10d_jw5_jerk_v034_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_10d_jw21_jerk_v035_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_10d_jw63_jerk_v036_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_21d_jw5_jerk_v037_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_21d_jw21_jerk_v038_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_21d_jw63_jerk_v039_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_42d_jw5_jerk_v040_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_42d_jw21_jerk_v041_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_42d_jw63_jerk_v042_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_63d_jw5_jerk_v043_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_63d_jw21_jerk_v044_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_63d_jw63_jerk_v045_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_126d_jw5_jerk_v046_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_126d_jw21_jerk_v047_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_126d_jw63_jerk_v048_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_189d_jw5_jerk_v049_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_189d_jw21_jerk_v050_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_189d_jw63_jerk_v051_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_252d_jw5_jerk_v052_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_252d_jw21_jerk_v053_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_252d_jw63_jerk_v054_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_378d_jw5_jerk_v055_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_378d_jw21_jerk_v056_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_378d_jw63_jerk_v057_signal,
    imc_f48_insurance_market_cycle_cp_close_sq_raw_504d_jw5_jerk_v058_signal,
    imc_f48_insurance_market_cycle_mp_close_sq_raw_504d_jw21_jerk_v059_signal,
    imc_f48_insurance_market_cycle_cs_close_sq_raw_504d_jw63_jerk_v060_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_5d_jw5_jerk_v061_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_5d_jw21_jerk_v062_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_5d_jw63_jerk_v063_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_10d_jw5_jerk_v064_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_10d_jw21_jerk_v065_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_10d_jw63_jerk_v066_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_21d_jw5_jerk_v067_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_21d_jw21_jerk_v068_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_21d_jw63_jerk_v069_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_42d_jw5_jerk_v070_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_42d_jw21_jerk_v071_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_42d_jw63_jerk_v072_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_63d_jw5_jerk_v073_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_63d_jw21_jerk_v074_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_63d_jw63_jerk_v075_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_126d_jw5_jerk_v076_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_126d_jw21_jerk_v077_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_126d_jw63_jerk_v078_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_189d_jw5_jerk_v079_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_189d_jw21_jerk_v080_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_189d_jw63_jerk_v081_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_252d_jw5_jerk_v082_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_252d_jw21_jerk_v083_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_252d_jw63_jerk_v084_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_378d_jw5_jerk_v085_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_378d_jw21_jerk_v086_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_378d_jw63_jerk_v087_signal,
    imc_f48_insurance_market_cycle_cp_close_log_raw_504d_jw5_jerk_v088_signal,
    imc_f48_insurance_market_cycle_mp_close_log_raw_504d_jw21_jerk_v089_signal,
    imc_f48_insurance_market_cycle_cs_close_log_raw_504d_jw63_jerk_v090_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_5d_jw5_jerk_v091_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_5d_jw21_jerk_v092_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_5d_jw63_jerk_v093_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_10d_jw5_jerk_v094_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_10d_jw21_jerk_v095_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_10d_jw63_jerk_v096_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_21d_jw5_jerk_v097_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_21d_jw21_jerk_v098_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_21d_jw63_jerk_v099_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_42d_jw5_jerk_v100_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_42d_jw21_jerk_v101_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_42d_jw63_jerk_v102_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_63d_jw5_jerk_v103_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_63d_jw21_jerk_v104_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_63d_jw63_jerk_v105_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_126d_jw5_jerk_v106_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_126d_jw21_jerk_v107_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_126d_jw63_jerk_v108_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_189d_jw5_jerk_v109_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_189d_jw21_jerk_v110_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_189d_jw63_jerk_v111_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_252d_jw5_jerk_v112_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_252d_jw21_jerk_v113_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_252d_jw63_jerk_v114_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_378d_jw5_jerk_v115_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_378d_jw21_jerk_v116_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_378d_jw63_jerk_v117_signal,
    imc_f48_insurance_market_cycle_cp_close_mean21_raw_504d_jw5_jerk_v118_signal,
    imc_f48_insurance_market_cycle_mp_close_mean21_raw_504d_jw21_jerk_v119_signal,
    imc_f48_insurance_market_cycle_cs_close_mean21_raw_504d_jw63_jerk_v120_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_5d_jw5_jerk_v121_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_5d_jw21_jerk_v122_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_5d_jw63_jerk_v123_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_10d_jw5_jerk_v124_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_10d_jw21_jerk_v125_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_10d_jw63_jerk_v126_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_21d_jw5_jerk_v127_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_21d_jw21_jerk_v128_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_21d_jw63_jerk_v129_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_42d_jw5_jerk_v130_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_42d_jw21_jerk_v131_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_42d_jw63_jerk_v132_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_63d_jw5_jerk_v133_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_63d_jw21_jerk_v134_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_63d_jw63_jerk_v135_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_126d_jw5_jerk_v136_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_126d_jw21_jerk_v137_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_126d_jw63_jerk_v138_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_189d_jw5_jerk_v139_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_189d_jw21_jerk_v140_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_189d_jw63_jerk_v141_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_252d_jw5_jerk_v142_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_252d_jw21_jerk_v143_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_252d_jw63_jerk_v144_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_378d_jw5_jerk_v145_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_378d_jw21_jerk_v146_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_378d_jw63_jerk_v147_signal,
    imc_f48_insurance_market_cycle_cp_close_mean63_raw_504d_jw5_jerk_v148_signal,
    imc_f48_insurance_market_cycle_mp_close_mean63_raw_504d_jw21_jerk_v149_signal,
    imc_f48_insurance_market_cycle_cs_close_mean63_raw_504d_jw63_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_INSURANCE_MARKET_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f48_cycle_proxy', '_f48_market_phase', '_f48_cycle_score')
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
    print(f"OK f48_insurance_market_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
