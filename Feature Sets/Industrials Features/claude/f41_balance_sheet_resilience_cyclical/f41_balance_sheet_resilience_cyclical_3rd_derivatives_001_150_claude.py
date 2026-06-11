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
def _f41_net_debt_to_ebitda(debt, cashneq, ebitda):
    nd = debt - cashneq
    return nd / ebitda.replace(0, np.nan)


def _f41_leverage_position(debt, equity, w):
    lev = debt / equity.replace(0, np.nan).abs()
    return lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_debt_capacity(debt, cashneq, fcf, w):
    nd = debt - cashneq
    cap = fcf.rolling(w, min_periods=max(1, w // 2)).sum() / nd.replace(0, np.nan).abs()
    return cap

# jerk feature 1: ndebt_ebitda_smooth5d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xc_21d_jerk_v001_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 2: ndebt_ebitda_smooth5d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xclog_42d_jerk_v002_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 3: ndebt_ebitda_smooth5d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xcm21_63d_jerk_v003_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 4: ndebt_ebitda_smooth10d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xc_126d_jerk_v004_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 10)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 5: ndebt_ebitda_smooth10d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xclog_21d_jerk_v005_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 10)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 6: ndebt_ebitda_smooth10d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xcm21_42d_jerk_v006_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 10)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 7: ndebt_ebitda_smooth21d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xc_63d_jerk_v007_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 8: ndebt_ebitda_smooth21d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xclog_126d_jerk_v008_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 9: ndebt_ebitda_smooth21d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xcm21_21d_jerk_v009_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 10: ndebt_ebitda_smooth42d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xc_42d_jerk_v010_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 42)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 11: ndebt_ebitda_smooth42d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xclog_63d_jerk_v011_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 42)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 12: ndebt_ebitda_smooth42d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xcm21_126d_jerk_v012_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 42)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 13: ndebt_ebitda_smooth63d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xc_21d_jerk_v013_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 14: ndebt_ebitda_smooth63d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xclog_42d_jerk_v014_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 15: ndebt_ebitda_smooth63d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xcm21_63d_jerk_v015_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 16: ndebt_ebitda_smooth126d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xc_126d_jerk_v016_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 17: ndebt_ebitda_smooth126d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xclog_21d_jerk_v017_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 18: ndebt_ebitda_smooth126d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xcm21_42d_jerk_v018_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 19: ndebt_ebitda_smooth189d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xc_63d_jerk_v019_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 189)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 20: ndebt_ebitda_smooth189d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xclog_126d_jerk_v020_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 189)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 21: ndebt_ebitda_smooth189d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xcm21_21d_jerk_v021_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 189)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 22: ndebt_ebitda_smooth252d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xc_42d_jerk_v022_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 23: ndebt_ebitda_smooth252d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xclog_63d_jerk_v023_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 24: ndebt_ebitda_smooth252d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xcm21_126d_jerk_v024_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 25: ndebt_ebitda_smooth378d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xc_21d_jerk_v025_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 26: ndebt_ebitda_smooth378d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xclog_42d_jerk_v026_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 378)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 27: ndebt_ebitda_smooth378d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xcm21_63d_jerk_v027_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 28: ndebt_ebitda_smooth504d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xc_126d_jerk_v028_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 29: ndebt_ebitda_smooth504d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xclog_21d_jerk_v029_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 30: ndebt_ebitda_smooth504d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xcm21_42d_jerk_v030_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 504)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 31: ndebt_ebitda_z21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z21d_63d_jerk_v031_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 32: ndebt_ebitda_z42d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z42d_126d_jerk_v032_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 33: ndebt_ebitda_z63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z63d_21d_jerk_v033_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 34: ndebt_ebitda_z126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z126d_42d_jerk_v034_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 35: ndebt_ebitda_z189d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z189d_63d_jerk_v035_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 36: ndebt_ebitda_z252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z252d_126d_jerk_v036_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 37: ndebt_ebitda_z378d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z378d_21d_jerk_v037_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 38: ndebt_ebitda_z504d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z504d_42d_jerk_v038_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 39: lev_pos_5d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xc_63d_jerk_v039_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 40: lev_pos_5d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xclog_126d_jerk_v040_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 5)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 41: lev_pos_5d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xcm21_21d_jerk_v041_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 42: lev_pos_10d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xc_42d_jerk_v042_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 10)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 43: lev_pos_10d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xclog_63d_jerk_v043_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 10)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 44: lev_pos_10d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xcm21_126d_jerk_v044_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 10)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 45: lev_pos_21d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xc_21d_jerk_v045_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 46: lev_pos_21d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xclog_42d_jerk_v046_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 47: lev_pos_21d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xcm21_63d_jerk_v047_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 48: lev_pos_42d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xc_126d_jerk_v048_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 42)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 49: lev_pos_42d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xclog_21d_jerk_v049_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 42)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 50: lev_pos_42d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xcm21_42d_jerk_v050_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 42)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 51: lev_pos_63d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xc_63d_jerk_v051_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 52: lev_pos_63d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xclog_126d_jerk_v052_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 53: lev_pos_63d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xcm21_21d_jerk_v053_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 54: lev_pos_126d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xc_42d_jerk_v054_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 55: lev_pos_126d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xclog_63d_jerk_v055_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 56: lev_pos_126d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xcm21_126d_jerk_v056_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 57: lev_pos_189d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xc_21d_jerk_v057_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 189)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 58: lev_pos_189d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xclog_42d_jerk_v058_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 189)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 59: lev_pos_189d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xcm21_63d_jerk_v059_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 189)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 60: lev_pos_252d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xc_126d_jerk_v060_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 61: lev_pos_252d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xclog_21d_jerk_v061_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 62: lev_pos_252d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xcm21_42d_jerk_v062_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 63: lev_pos_378d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xc_63d_jerk_v063_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 64: lev_pos_378d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xclog_126d_jerk_v064_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 65: lev_pos_378d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xcm21_21d_jerk_v065_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 66: lev_pos_504d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xc_42d_jerk_v066_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 504)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 67: lev_pos_504d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xclog_63d_jerk_v067_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 68: lev_pos_504d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xcm21_126d_jerk_v068_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 69: debt_cap_5d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xc_21d_jerk_v069_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 5)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 70: debt_cap_5d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xclog_42d_jerk_v070_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 5)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 71: debt_cap_5d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xcm21_63d_jerk_v071_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 5)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 72: debt_cap_10d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xc_126d_jerk_v072_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 10)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 73: debt_cap_10d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xclog_21d_jerk_v073_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 10)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 74: debt_cap_10d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xcm21_42d_jerk_v074_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 10)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 75: debt_cap_21d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xc_63d_jerk_v075_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 76: debt_cap_21d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xclog_126d_jerk_v076_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 77: debt_cap_21d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xcm21_21d_jerk_v077_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 78: debt_cap_42d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xc_42d_jerk_v078_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 79: debt_cap_42d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xclog_63d_jerk_v079_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 80: debt_cap_42d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xcm21_126d_jerk_v080_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 81: debt_cap_63d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xc_21d_jerk_v081_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 82: debt_cap_63d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xclog_42d_jerk_v082_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 83: debt_cap_63d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xcm21_63d_jerk_v083_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 84: debt_cap_126d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xc_126d_jerk_v084_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 85: debt_cap_126d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xclog_21d_jerk_v085_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 86: debt_cap_126d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xcm21_42d_jerk_v086_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 87: debt_cap_189d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xc_63d_jerk_v087_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 88: debt_cap_189d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xclog_126d_jerk_v088_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 89: debt_cap_189d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xcm21_21d_jerk_v089_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 90: debt_cap_252d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xc_42d_jerk_v090_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 91: debt_cap_252d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xclog_63d_jerk_v091_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 92: debt_cap_252d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xcm21_126d_jerk_v092_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 93: debt_cap_378d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xc_21d_jerk_v093_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 94: debt_cap_378d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xclog_42d_jerk_v094_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 95: debt_cap_378d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xcm21_63d_jerk_v095_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 96: debt_cap_504d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xc_126d_jerk_v096_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 97: debt_cap_504d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xclog_21d_jerk_v097_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 98: debt_cap_504d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xcm21_42d_jerk_v098_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 99: levxcap_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_21d_63d_jerk_v099_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 21)
    b = _f41_debt_capacity(debt, cashneq, fcf, 21)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 100: ndebtxlev_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_21d_126d_jerk_v100_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 21)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 101: ndebt_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_21d_21d_jerk_v101_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 102: lev_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_21d_42d_jerk_v102_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 103: cap_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_21d_63d_jerk_v103_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 104: levxcap_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_63d_126d_jerk_v104_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 63)
    b = _f41_debt_capacity(debt, cashneq, fcf, 63)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 105: ndebtxlev_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_63d_21d_jerk_v105_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 63)
    base = (a * b)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 106: ndebt_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_63d_42d_jerk_v106_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 107: lev_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_63d_63d_jerk_v107_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 108: cap_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_63d_126d_jerk_v108_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 109: levxcap_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_126d_21d_jerk_v109_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 126)
    b = _f41_debt_capacity(debt, cashneq, fcf, 126)
    base = (a * b)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 110: ndebtxlev_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_126d_42d_jerk_v110_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 126)
    base = (a * b)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 111: ndebt_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_126d_63d_jerk_v111_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 112: lev_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_126d_126d_jerk_v112_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 113: cap_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_126d_21d_jerk_v113_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 114: levxcap_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_252d_42d_jerk_v114_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 252)
    b = _f41_debt_capacity(debt, cashneq, fcf, 252)
    base = (a * b)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 115: ndebtxlev_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_252d_63d_jerk_v115_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 252)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 116: ndebt_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_252d_126d_jerk_v116_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 117: lev_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_252d_21d_jerk_v117_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 118: cap_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_252d_42d_jerk_v118_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 119: levxcap_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_504d_63d_jerk_v119_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 504)
    b = _f41_debt_capacity(debt, cashneq, fcf, 504)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 120: ndebtxlev_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_504d_126d_jerk_v120_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 504)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 121: ndebt_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_504d_21d_jerk_v121_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 122: lev_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_504d_42d_jerk_v122_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 504)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 123: cap_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_504d_63d_jerk_v123_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 124: ndebt_sq_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_21d_126d_jerk_v124_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 125: lev_z_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_21d_21d_jerk_v125_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 126: cap_z_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_21d_42d_jerk_v126_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 127: ndebt_sq_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_42d_63d_jerk_v127_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 42)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 128: lev_z_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_42d_126d_jerk_v128_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 42)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 129: cap_z_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_42d_21d_jerk_v129_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 130: ndebt_sq_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_63d_42d_jerk_v130_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 131: lev_z_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_63d_63d_jerk_v131_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 132: cap_z_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_63d_126d_jerk_v132_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 133: ndebt_sq_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_126d_21d_jerk_v133_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 134: lev_z_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_126d_42d_jerk_v134_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 135: cap_z_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_126d_63d_jerk_v135_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 136: ndebt_sq_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_252d_126d_jerk_v136_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 137: lev_z_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_252d_21d_jerk_v137_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 138: cap_z_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_252d_42d_jerk_v138_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 139: capxlev_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_21d_63d_jerk_v139_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 21)
    b = _f41_leverage_position(debt, equity, 21)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 140: ndebtxcap_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_21d_126d_jerk_v140_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 21)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 141: capxlev_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_42d_21d_jerk_v141_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 42)
    b = _f41_leverage_position(debt, equity, 42)
    base = (a * b)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 142: ndebtxcap_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_42d_42d_jerk_v142_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 42)
    base = (a * b)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 143: capxlev_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_63d_63d_jerk_v143_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 63)
    b = _f41_leverage_position(debt, equity, 63)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 144: ndebtxcap_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_63d_126d_jerk_v144_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 63)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 145: capxlev_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_126d_21d_jerk_v145_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 126)
    b = _f41_leverage_position(debt, equity, 126)
    base = (a * b)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 146: ndebtxcap_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_126d_42d_jerk_v146_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 126)
    base = (a * b)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 147: capxlev_189d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_189d_63d_jerk_v147_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 189)
    b = _f41_leverage_position(debt, equity, 189)
    base = (a * b)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 148: ndebtxcap_189d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_189d_126d_jerk_v148_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 189)
    base = (a * b)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 149: capxlev_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_252d_21d_jerk_v149_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 252)
    b = _f41_leverage_position(debt, equity, 252)
    base = (a * b)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# jerk feature 150: ndebtxcap_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_252d_42d_jerk_v150_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 252)
    base = (a * b)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xc_21d_jerk_v001_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xclog_42d_jerk_v002_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth5d_xcm21_63d_jerk_v003_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xc_126d_jerk_v004_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xclog_21d_jerk_v005_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth10d_xcm21_42d_jerk_v006_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xc_63d_jerk_v007_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xclog_126d_jerk_v008_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth21d_xcm21_21d_jerk_v009_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xc_42d_jerk_v010_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xclog_63d_jerk_v011_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth42d_xcm21_126d_jerk_v012_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xc_21d_jerk_v013_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xclog_42d_jerk_v014_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth63d_xcm21_63d_jerk_v015_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xc_126d_jerk_v016_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xclog_21d_jerk_v017_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth126d_xcm21_42d_jerk_v018_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xc_63d_jerk_v019_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xclog_126d_jerk_v020_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth189d_xcm21_21d_jerk_v021_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xc_42d_jerk_v022_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xclog_63d_jerk_v023_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth252d_xcm21_126d_jerk_v024_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xc_21d_jerk_v025_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xclog_42d_jerk_v026_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth378d_xcm21_63d_jerk_v027_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xc_126d_jerk_v028_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xclog_21d_jerk_v029_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_smooth504d_xcm21_42d_jerk_v030_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z21d_63d_jerk_v031_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z42d_126d_jerk_v032_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z63d_21d_jerk_v033_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z126d_42d_jerk_v034_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z189d_63d_jerk_v035_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z252d_126d_jerk_v036_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z378d_21d_jerk_v037_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ebitda_z504d_42d_jerk_v038_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xc_63d_jerk_v039_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xclog_126d_jerk_v040_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_5d_xcm21_21d_jerk_v041_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xc_42d_jerk_v042_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xclog_63d_jerk_v043_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_10d_xcm21_126d_jerk_v044_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xc_21d_jerk_v045_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xclog_42d_jerk_v046_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_21d_xcm21_63d_jerk_v047_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xc_126d_jerk_v048_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xclog_21d_jerk_v049_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_42d_xcm21_42d_jerk_v050_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xc_63d_jerk_v051_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xclog_126d_jerk_v052_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_63d_xcm21_21d_jerk_v053_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xc_42d_jerk_v054_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xclog_63d_jerk_v055_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_126d_xcm21_126d_jerk_v056_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xc_21d_jerk_v057_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xclog_42d_jerk_v058_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_189d_xcm21_63d_jerk_v059_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xc_126d_jerk_v060_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xclog_21d_jerk_v061_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_252d_xcm21_42d_jerk_v062_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xc_63d_jerk_v063_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xclog_126d_jerk_v064_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_378d_xcm21_21d_jerk_v065_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xc_42d_jerk_v066_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xclog_63d_jerk_v067_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_pos_504d_xcm21_126d_jerk_v068_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xc_21d_jerk_v069_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xclog_42d_jerk_v070_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_5d_xcm21_63d_jerk_v071_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xc_126d_jerk_v072_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xclog_21d_jerk_v073_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_10d_xcm21_42d_jerk_v074_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xc_63d_jerk_v075_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xclog_126d_jerk_v076_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xcm21_21d_jerk_v077_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xc_42d_jerk_v078_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xclog_63d_jerk_v079_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xcm21_126d_jerk_v080_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xc_21d_jerk_v081_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xclog_42d_jerk_v082_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xcm21_63d_jerk_v083_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xc_126d_jerk_v084_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xclog_21d_jerk_v085_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xcm21_42d_jerk_v086_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xc_63d_jerk_v087_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xclog_126d_jerk_v088_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xcm21_21d_jerk_v089_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xc_42d_jerk_v090_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xclog_63d_jerk_v091_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xcm21_126d_jerk_v092_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xc_21d_jerk_v093_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xclog_42d_jerk_v094_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xcm21_63d_jerk_v095_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xc_126d_jerk_v096_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xclog_21d_jerk_v097_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xcm21_42d_jerk_v098_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_21d_63d_jerk_v099_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_21d_126d_jerk_v100_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_21d_21d_jerk_v101_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_21d_42d_jerk_v102_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_21d_63d_jerk_v103_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_63d_126d_jerk_v104_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_63d_21d_jerk_v105_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_63d_42d_jerk_v106_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_63d_63d_jerk_v107_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_63d_126d_jerk_v108_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_126d_21d_jerk_v109_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_126d_42d_jerk_v110_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_126d_63d_jerk_v111_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_126d_126d_jerk_v112_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_126d_21d_jerk_v113_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_252d_42d_jerk_v114_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_252d_63d_jerk_v115_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_252d_126d_jerk_v116_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_252d_21d_jerk_v117_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_252d_42d_jerk_v118_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_504d_63d_jerk_v119_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_504d_126d_jerk_v120_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_504d_21d_jerk_v121_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_504d_42d_jerk_v122_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_504d_63d_jerk_v123_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_21d_126d_jerk_v124_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_21d_21d_jerk_v125_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_21d_42d_jerk_v126_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_42d_63d_jerk_v127_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_42d_126d_jerk_v128_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_42d_21d_jerk_v129_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_63d_42d_jerk_v130_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_63d_63d_jerk_v131_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_63d_126d_jerk_v132_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_126d_21d_jerk_v133_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_126d_42d_jerk_v134_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_126d_63d_jerk_v135_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_252d_126d_jerk_v136_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_252d_21d_jerk_v137_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_252d_42d_jerk_v138_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_21d_63d_jerk_v139_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_21d_126d_jerk_v140_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_42d_21d_jerk_v141_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_42d_42d_jerk_v142_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_63d_63d_jerk_v143_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_63d_126d_jerk_v144_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_126d_21d_jerk_v145_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_126d_42d_jerk_v146_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_189d_63d_jerk_v147_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_189d_126d_jerk_v148_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_252d_21d_jerk_v149_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_252d_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_BALANCE_SHEET_RESILIENCE_CYCLICAL_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ('_f41_net_debt_to_ebitda', '_f41_leverage_position', '_f41_debt_capacity')
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
    print(f"OK f41_balance_sheet_resilience_cyclical_3rd_derivatives_001_150_claude: {n_features} features pass")
