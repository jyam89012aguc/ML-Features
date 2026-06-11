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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


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
def _f18_netinc_revenue_ratio(netinc, revenue):
    return netinc / revenue.replace(0, np.nan)


def _f18_investment_income_share(netinc, revenue, w):
    rev_sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    ni_sm = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return ni_sm / rev_sm.replace(0, np.nan)


def _f18_income_quality(netinc, revenue, w):
    ratio = netinc / revenue.replace(0, np.nan)
    m = ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)

def f18iii_f18_insurance_investment_income_nirratio_5d_jerk_5d_jerk_v001_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(5, min_periods=max(1,5//2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_8d_jerk_10d_jerk_v002_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(8, min_periods=max(1,8//2)).mean() * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_10d_jerk_21d_jerk_v003_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(10, min_periods=max(1,10//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_15d_jerk_42d_jerk_v004_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(15, min_periods=max(1,15//2)).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_21d_jerk_63d_jerk_v005_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(21, min_periods=max(1,21//2)).mean() * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_30d_jerk_5d_jerk_v006_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(30, min_periods=max(1,30//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_42d_jerk_10d_jerk_v007_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(42, min_periods=max(1,42//2)).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_63d_jerk_21d_jerk_v008_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(63, min_periods=max(1,63//2)).mean() * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_90d_jerk_42d_jerk_v009_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(90, min_periods=max(1,90//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_126d_jerk_63d_jerk_v010_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(126, min_periods=max(1,126//2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_150d_jerk_5d_jerk_v011_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(150, min_periods=max(1,150//2)).mean() * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_189d_jerk_10d_jerk_v012_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(189, min_periods=max(1,189//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_252d_jerk_21d_jerk_v013_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(252, min_periods=max(1,252//2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_378d_jerk_42d_jerk_v014_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(378, min_periods=max(1,378//2)).mean() * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_504d_jerk_63d_jerk_v015_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = r.rolling(504, min_periods=max(1,504//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_5d_jerk_5d_jerk_v016_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_8d_jerk_10d_jerk_v017_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_10d_jerk_21d_jerk_v018_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_15d_jerk_42d_jerk_v019_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_21d_jerk_63d_jerk_v020_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_30d_jerk_5d_jerk_v021_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_42d_jerk_10d_jerk_v022_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_63d_jerk_21d_jerk_v023_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_90d_jerk_42d_jerk_v024_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_126d_jerk_63d_jerk_v025_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_150d_jerk_5d_jerk_v026_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_189d_jerk_10d_jerk_v027_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_252d_jerk_21d_jerk_v028_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_378d_jerk_42d_jerk_v029_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_504d_jerk_63d_jerk_v030_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _ema(r, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_5d_jerk_5d_jerk_v031_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_8d_jerk_10d_jerk_v032_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_10d_jerk_21d_jerk_v033_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_15d_jerk_42d_jerk_v034_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_21d_jerk_63d_jerk_v035_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_30d_jerk_5d_jerk_v036_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_42d_jerk_10d_jerk_v037_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_63d_jerk_21d_jerk_v038_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_90d_jerk_42d_jerk_v039_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_126d_jerk_63d_jerk_v040_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_150d_jerk_5d_jerk_v041_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_189d_jerk_10d_jerk_v042_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_252d_jerk_21d_jerk_v043_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_378d_jerk_42d_jerk_v044_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_504d_jerk_63d_jerk_v045_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _std(r, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_5d_jerk_5d_jerk_v046_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_8d_jerk_10d_jerk_v047_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_10d_jerk_21d_jerk_v048_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_15d_jerk_42d_jerk_v049_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_21d_jerk_63d_jerk_v050_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_30d_jerk_5d_jerk_v051_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_42d_jerk_10d_jerk_v052_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_63d_jerk_21d_jerk_v053_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_90d_jerk_42d_jerk_v054_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_126d_jerk_63d_jerk_v055_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_150d_jerk_5d_jerk_v056_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_189d_jerk_10d_jerk_v057_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_252d_jerk_21d_jerk_v058_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_378d_jerk_42d_jerk_v059_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_504d_jerk_63d_jerk_v060_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    base = _z(r, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_5d_jerk_5d_jerk_v061_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    base = s * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_8d_jerk_10d_jerk_v062_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    base = s * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_10d_jerk_21d_jerk_v063_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    base = s * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_15d_jerk_42d_jerk_v064_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    base = s * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_21d_jerk_63d_jerk_v065_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    base = s * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_30d_jerk_5d_jerk_v066_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    base = s * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_42d_jerk_10d_jerk_v067_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    base = s * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_63d_jerk_21d_jerk_v068_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    base = s * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_90d_jerk_42d_jerk_v069_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    base = s * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_126d_jerk_63d_jerk_v070_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    base = s * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_150d_jerk_5d_jerk_v071_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    base = s * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_189d_jerk_10d_jerk_v072_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    base = s * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_252d_jerk_21d_jerk_v073_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    base = s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_378d_jerk_42d_jerk_v074_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    base = s * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_504d_jerk_63d_jerk_v075_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    base = s * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_5d_jerk_5d_jerk_v076_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    base = _ema(s, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_8d_jerk_10d_jerk_v077_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    base = _ema(s, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_10d_jerk_21d_jerk_v078_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    base = _ema(s, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_15d_jerk_42d_jerk_v079_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    base = _ema(s, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_21d_jerk_63d_jerk_v080_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    base = _ema(s, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_30d_jerk_5d_jerk_v081_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    base = _ema(s, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_42d_jerk_10d_jerk_v082_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    base = _ema(s, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_63d_jerk_21d_jerk_v083_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    base = _ema(s, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_90d_jerk_42d_jerk_v084_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    base = _ema(s, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_126d_jerk_63d_jerk_v085_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    base = _ema(s, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_150d_jerk_5d_jerk_v086_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    base = _ema(s, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_189d_jerk_10d_jerk_v087_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    base = _ema(s, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_252d_jerk_21d_jerk_v088_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    base = _ema(s, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_378d_jerk_42d_jerk_v089_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    base = _ema(s, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishareema_504d_jerk_63d_jerk_v090_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    base = _ema(s, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_5d_jerk_5d_jerk_v091_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    base = _z(s, 252) * closeadj * (0.0500)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_8d_jerk_10d_jerk_v092_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    base = _z(s, 252) * closeadj * (0.0800)
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_10d_jerk_21d_jerk_v093_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    base = _z(s, 252) * closeadj * (0.1000)
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_15d_jerk_42d_jerk_v094_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    base = _z(s, 252) * closeadj * (0.1500)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_21d_jerk_63d_jerk_v095_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    base = _z(s, 252) * closeadj * (0.2100)
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_30d_jerk_5d_jerk_v096_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    base = _z(s, 252) * closeadj * (0.3000)
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_42d_jerk_10d_jerk_v097_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    base = _z(s, 252) * closeadj * (0.4200)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_63d_jerk_21d_jerk_v098_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    base = _z(s, 252) * closeadj * (0.6300)
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_90d_jerk_42d_jerk_v099_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    base = _z(s, 252) * closeadj * (0.9000)
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_126d_jerk_63d_jerk_v100_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    base = _z(s, 252) * closeadj * (1.2600)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_150d_jerk_5d_jerk_v101_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    base = _z(s, 252) * closeadj * (1.5000)
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_189d_jerk_10d_jerk_v102_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    base = _z(s, 252) * closeadj * (1.8900)
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_252d_jerk_21d_jerk_v103_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    base = _z(s, 252) * closeadj * (2.5200)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_378d_jerk_42d_jerk_v104_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    base = _z(s, 252) * closeadj * (3.7800)
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharez_504d_jerk_63d_jerk_v105_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    base = _z(s, 252) * closeadj * (5.0400)
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_5d_jerk_5d_jerk_v106_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 5)
    base = q * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_8d_jerk_10d_jerk_v107_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 8)
    base = q * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_10d_jerk_21d_jerk_v108_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 10)
    base = q * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_15d_jerk_42d_jerk_v109_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 15)
    base = q * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_21d_jerk_63d_jerk_v110_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 21)
    base = q * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_30d_jerk_5d_jerk_v111_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 30)
    base = q * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_42d_jerk_10d_jerk_v112_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 42)
    base = q * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_63d_jerk_21d_jerk_v113_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 63)
    base = q * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_90d_jerk_42d_jerk_v114_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 90)
    base = q * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_126d_jerk_63d_jerk_v115_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 126)
    base = q * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_150d_jerk_5d_jerk_v116_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 150)
    base = q * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_189d_jerk_10d_jerk_v117_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 189)
    base = q * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_252d_jerk_21d_jerk_v118_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 252)
    base = q * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_378d_jerk_42d_jerk_v119_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 378)
    base = q * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iq_504d_jerk_63d_jerk_v120_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 504)
    base = q * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_5d_jerk_5d_jerk_v121_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 5)
    base = _ema(q, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_8d_jerk_10d_jerk_v122_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 8)
    base = _ema(q, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_10d_jerk_21d_jerk_v123_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 10)
    base = _ema(q, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_15d_jerk_42d_jerk_v124_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 15)
    base = _ema(q, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_21d_jerk_63d_jerk_v125_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 21)
    base = _ema(q, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_30d_jerk_5d_jerk_v126_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 30)
    base = _ema(q, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_42d_jerk_10d_jerk_v127_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 42)
    base = _ema(q, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_63d_jerk_21d_jerk_v128_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 63)
    base = _ema(q, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_90d_jerk_42d_jerk_v129_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 90)
    base = _ema(q, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_126d_jerk_63d_jerk_v130_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 126)
    base = _ema(q, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_150d_jerk_5d_jerk_v131_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 150)
    base = _ema(q, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_189d_jerk_10d_jerk_v132_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 189)
    base = _ema(q, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_252d_jerk_21d_jerk_v133_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 252)
    base = _ema(q, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_378d_jerk_42d_jerk_v134_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 378)
    base = _ema(q, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iqema_504d_jerk_63d_jerk_v135_signal(netinc, revenue, closeadj):
    q = _f18_income_quality(netinc, revenue, 504)
    base = _ema(q, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_5d_jerk_5d_jerk_v136_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    base = (s - s.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_8d_jerk_10d_jerk_v137_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    base = (s - s.shift(8)) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_10d_jerk_21d_jerk_v138_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    base = (s - s.shift(10)) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_15d_jerk_42d_jerk_v139_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    base = (s - s.shift(15)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_21d_jerk_63d_jerk_v140_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    base = (s - s.shift(21)) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_30d_jerk_5d_jerk_v141_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    base = (s - s.shift(30)) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_42d_jerk_10d_jerk_v142_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    base = (s - s.shift(42)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_63d_jerk_21d_jerk_v143_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    base = (s - s.shift(63)) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_90d_jerk_42d_jerk_v144_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    base = (s - s.shift(90)) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_126d_jerk_63d_jerk_v145_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    base = (s - s.shift(126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_150d_jerk_5d_jerk_v146_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    base = (s - s.shift(150)) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_189d_jerk_10d_jerk_v147_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    base = (s - s.shift(189)) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_252d_jerk_21d_jerk_v148_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    base = (s - s.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_378d_jerk_42d_jerk_v149_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    base = (s - s.shift(378)) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iisharediff_504d_jerk_63d_jerk_v150_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    base = (s - s.shift(504)) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18iii_f18_insurance_investment_income_nirratio_5d_jerk_5d_jerk_v001_signal,
    f18iii_f18_insurance_investment_income_nirratio_8d_jerk_10d_jerk_v002_signal,
    f18iii_f18_insurance_investment_income_nirratio_10d_jerk_21d_jerk_v003_signal,
    f18iii_f18_insurance_investment_income_nirratio_15d_jerk_42d_jerk_v004_signal,
    f18iii_f18_insurance_investment_income_nirratio_21d_jerk_63d_jerk_v005_signal,
    f18iii_f18_insurance_investment_income_nirratio_30d_jerk_5d_jerk_v006_signal,
    f18iii_f18_insurance_investment_income_nirratio_42d_jerk_10d_jerk_v007_signal,
    f18iii_f18_insurance_investment_income_nirratio_63d_jerk_21d_jerk_v008_signal,
    f18iii_f18_insurance_investment_income_nirratio_90d_jerk_42d_jerk_v009_signal,
    f18iii_f18_insurance_investment_income_nirratio_126d_jerk_63d_jerk_v010_signal,
    f18iii_f18_insurance_investment_income_nirratio_150d_jerk_5d_jerk_v011_signal,
    f18iii_f18_insurance_investment_income_nirratio_189d_jerk_10d_jerk_v012_signal,
    f18iii_f18_insurance_investment_income_nirratio_252d_jerk_21d_jerk_v013_signal,
    f18iii_f18_insurance_investment_income_nirratio_378d_jerk_42d_jerk_v014_signal,
    f18iii_f18_insurance_investment_income_nirratio_504d_jerk_63d_jerk_v015_signal,
    f18iii_f18_insurance_investment_income_nirratioema_5d_jerk_5d_jerk_v016_signal,
    f18iii_f18_insurance_investment_income_nirratioema_8d_jerk_10d_jerk_v017_signal,
    f18iii_f18_insurance_investment_income_nirratioema_10d_jerk_21d_jerk_v018_signal,
    f18iii_f18_insurance_investment_income_nirratioema_15d_jerk_42d_jerk_v019_signal,
    f18iii_f18_insurance_investment_income_nirratioema_21d_jerk_63d_jerk_v020_signal,
    f18iii_f18_insurance_investment_income_nirratioema_30d_jerk_5d_jerk_v021_signal,
    f18iii_f18_insurance_investment_income_nirratioema_42d_jerk_10d_jerk_v022_signal,
    f18iii_f18_insurance_investment_income_nirratioema_63d_jerk_21d_jerk_v023_signal,
    f18iii_f18_insurance_investment_income_nirratioema_90d_jerk_42d_jerk_v024_signal,
    f18iii_f18_insurance_investment_income_nirratioema_126d_jerk_63d_jerk_v025_signal,
    f18iii_f18_insurance_investment_income_nirratioema_150d_jerk_5d_jerk_v026_signal,
    f18iii_f18_insurance_investment_income_nirratioema_189d_jerk_10d_jerk_v027_signal,
    f18iii_f18_insurance_investment_income_nirratioema_252d_jerk_21d_jerk_v028_signal,
    f18iii_f18_insurance_investment_income_nirratioema_378d_jerk_42d_jerk_v029_signal,
    f18iii_f18_insurance_investment_income_nirratioema_504d_jerk_63d_jerk_v030_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_5d_jerk_5d_jerk_v031_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_8d_jerk_10d_jerk_v032_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_10d_jerk_21d_jerk_v033_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_15d_jerk_42d_jerk_v034_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_21d_jerk_63d_jerk_v035_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_30d_jerk_5d_jerk_v036_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_42d_jerk_10d_jerk_v037_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_63d_jerk_21d_jerk_v038_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_90d_jerk_42d_jerk_v039_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_126d_jerk_63d_jerk_v040_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_150d_jerk_5d_jerk_v041_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_189d_jerk_10d_jerk_v042_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_252d_jerk_21d_jerk_v043_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_378d_jerk_42d_jerk_v044_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_504d_jerk_63d_jerk_v045_signal,
    f18iii_f18_insurance_investment_income_nirratioz_5d_jerk_5d_jerk_v046_signal,
    f18iii_f18_insurance_investment_income_nirratioz_8d_jerk_10d_jerk_v047_signal,
    f18iii_f18_insurance_investment_income_nirratioz_10d_jerk_21d_jerk_v048_signal,
    f18iii_f18_insurance_investment_income_nirratioz_15d_jerk_42d_jerk_v049_signal,
    f18iii_f18_insurance_investment_income_nirratioz_21d_jerk_63d_jerk_v050_signal,
    f18iii_f18_insurance_investment_income_nirratioz_30d_jerk_5d_jerk_v051_signal,
    f18iii_f18_insurance_investment_income_nirratioz_42d_jerk_10d_jerk_v052_signal,
    f18iii_f18_insurance_investment_income_nirratioz_63d_jerk_21d_jerk_v053_signal,
    f18iii_f18_insurance_investment_income_nirratioz_90d_jerk_42d_jerk_v054_signal,
    f18iii_f18_insurance_investment_income_nirratioz_126d_jerk_63d_jerk_v055_signal,
    f18iii_f18_insurance_investment_income_nirratioz_150d_jerk_5d_jerk_v056_signal,
    f18iii_f18_insurance_investment_income_nirratioz_189d_jerk_10d_jerk_v057_signal,
    f18iii_f18_insurance_investment_income_nirratioz_252d_jerk_21d_jerk_v058_signal,
    f18iii_f18_insurance_investment_income_nirratioz_378d_jerk_42d_jerk_v059_signal,
    f18iii_f18_insurance_investment_income_nirratioz_504d_jerk_63d_jerk_v060_signal,
    f18iii_f18_insurance_investment_income_iishare_5d_jerk_5d_jerk_v061_signal,
    f18iii_f18_insurance_investment_income_iishare_8d_jerk_10d_jerk_v062_signal,
    f18iii_f18_insurance_investment_income_iishare_10d_jerk_21d_jerk_v063_signal,
    f18iii_f18_insurance_investment_income_iishare_15d_jerk_42d_jerk_v064_signal,
    f18iii_f18_insurance_investment_income_iishare_21d_jerk_63d_jerk_v065_signal,
    f18iii_f18_insurance_investment_income_iishare_30d_jerk_5d_jerk_v066_signal,
    f18iii_f18_insurance_investment_income_iishare_42d_jerk_10d_jerk_v067_signal,
    f18iii_f18_insurance_investment_income_iishare_63d_jerk_21d_jerk_v068_signal,
    f18iii_f18_insurance_investment_income_iishare_90d_jerk_42d_jerk_v069_signal,
    f18iii_f18_insurance_investment_income_iishare_126d_jerk_63d_jerk_v070_signal,
    f18iii_f18_insurance_investment_income_iishare_150d_jerk_5d_jerk_v071_signal,
    f18iii_f18_insurance_investment_income_iishare_189d_jerk_10d_jerk_v072_signal,
    f18iii_f18_insurance_investment_income_iishare_252d_jerk_21d_jerk_v073_signal,
    f18iii_f18_insurance_investment_income_iishare_378d_jerk_42d_jerk_v074_signal,
    f18iii_f18_insurance_investment_income_iishare_504d_jerk_63d_jerk_v075_signal,
    f18iii_f18_insurance_investment_income_iishareema_5d_jerk_5d_jerk_v076_signal,
    f18iii_f18_insurance_investment_income_iishareema_8d_jerk_10d_jerk_v077_signal,
    f18iii_f18_insurance_investment_income_iishareema_10d_jerk_21d_jerk_v078_signal,
    f18iii_f18_insurance_investment_income_iishareema_15d_jerk_42d_jerk_v079_signal,
    f18iii_f18_insurance_investment_income_iishareema_21d_jerk_63d_jerk_v080_signal,
    f18iii_f18_insurance_investment_income_iishareema_30d_jerk_5d_jerk_v081_signal,
    f18iii_f18_insurance_investment_income_iishareema_42d_jerk_10d_jerk_v082_signal,
    f18iii_f18_insurance_investment_income_iishareema_63d_jerk_21d_jerk_v083_signal,
    f18iii_f18_insurance_investment_income_iishareema_90d_jerk_42d_jerk_v084_signal,
    f18iii_f18_insurance_investment_income_iishareema_126d_jerk_63d_jerk_v085_signal,
    f18iii_f18_insurance_investment_income_iishareema_150d_jerk_5d_jerk_v086_signal,
    f18iii_f18_insurance_investment_income_iishareema_189d_jerk_10d_jerk_v087_signal,
    f18iii_f18_insurance_investment_income_iishareema_252d_jerk_21d_jerk_v088_signal,
    f18iii_f18_insurance_investment_income_iishareema_378d_jerk_42d_jerk_v089_signal,
    f18iii_f18_insurance_investment_income_iishareema_504d_jerk_63d_jerk_v090_signal,
    f18iii_f18_insurance_investment_income_iisharez_5d_jerk_5d_jerk_v091_signal,
    f18iii_f18_insurance_investment_income_iisharez_8d_jerk_10d_jerk_v092_signal,
    f18iii_f18_insurance_investment_income_iisharez_10d_jerk_21d_jerk_v093_signal,
    f18iii_f18_insurance_investment_income_iisharez_15d_jerk_42d_jerk_v094_signal,
    f18iii_f18_insurance_investment_income_iisharez_21d_jerk_63d_jerk_v095_signal,
    f18iii_f18_insurance_investment_income_iisharez_30d_jerk_5d_jerk_v096_signal,
    f18iii_f18_insurance_investment_income_iisharez_42d_jerk_10d_jerk_v097_signal,
    f18iii_f18_insurance_investment_income_iisharez_63d_jerk_21d_jerk_v098_signal,
    f18iii_f18_insurance_investment_income_iisharez_90d_jerk_42d_jerk_v099_signal,
    f18iii_f18_insurance_investment_income_iisharez_126d_jerk_63d_jerk_v100_signal,
    f18iii_f18_insurance_investment_income_iisharez_150d_jerk_5d_jerk_v101_signal,
    f18iii_f18_insurance_investment_income_iisharez_189d_jerk_10d_jerk_v102_signal,
    f18iii_f18_insurance_investment_income_iisharez_252d_jerk_21d_jerk_v103_signal,
    f18iii_f18_insurance_investment_income_iisharez_378d_jerk_42d_jerk_v104_signal,
    f18iii_f18_insurance_investment_income_iisharez_504d_jerk_63d_jerk_v105_signal,
    f18iii_f18_insurance_investment_income_iq_5d_jerk_5d_jerk_v106_signal,
    f18iii_f18_insurance_investment_income_iq_8d_jerk_10d_jerk_v107_signal,
    f18iii_f18_insurance_investment_income_iq_10d_jerk_21d_jerk_v108_signal,
    f18iii_f18_insurance_investment_income_iq_15d_jerk_42d_jerk_v109_signal,
    f18iii_f18_insurance_investment_income_iq_21d_jerk_63d_jerk_v110_signal,
    f18iii_f18_insurance_investment_income_iq_30d_jerk_5d_jerk_v111_signal,
    f18iii_f18_insurance_investment_income_iq_42d_jerk_10d_jerk_v112_signal,
    f18iii_f18_insurance_investment_income_iq_63d_jerk_21d_jerk_v113_signal,
    f18iii_f18_insurance_investment_income_iq_90d_jerk_42d_jerk_v114_signal,
    f18iii_f18_insurance_investment_income_iq_126d_jerk_63d_jerk_v115_signal,
    f18iii_f18_insurance_investment_income_iq_150d_jerk_5d_jerk_v116_signal,
    f18iii_f18_insurance_investment_income_iq_189d_jerk_10d_jerk_v117_signal,
    f18iii_f18_insurance_investment_income_iq_252d_jerk_21d_jerk_v118_signal,
    f18iii_f18_insurance_investment_income_iq_378d_jerk_42d_jerk_v119_signal,
    f18iii_f18_insurance_investment_income_iq_504d_jerk_63d_jerk_v120_signal,
    f18iii_f18_insurance_investment_income_iqema_5d_jerk_5d_jerk_v121_signal,
    f18iii_f18_insurance_investment_income_iqema_8d_jerk_10d_jerk_v122_signal,
    f18iii_f18_insurance_investment_income_iqema_10d_jerk_21d_jerk_v123_signal,
    f18iii_f18_insurance_investment_income_iqema_15d_jerk_42d_jerk_v124_signal,
    f18iii_f18_insurance_investment_income_iqema_21d_jerk_63d_jerk_v125_signal,
    f18iii_f18_insurance_investment_income_iqema_30d_jerk_5d_jerk_v126_signal,
    f18iii_f18_insurance_investment_income_iqema_42d_jerk_10d_jerk_v127_signal,
    f18iii_f18_insurance_investment_income_iqema_63d_jerk_21d_jerk_v128_signal,
    f18iii_f18_insurance_investment_income_iqema_90d_jerk_42d_jerk_v129_signal,
    f18iii_f18_insurance_investment_income_iqema_126d_jerk_63d_jerk_v130_signal,
    f18iii_f18_insurance_investment_income_iqema_150d_jerk_5d_jerk_v131_signal,
    f18iii_f18_insurance_investment_income_iqema_189d_jerk_10d_jerk_v132_signal,
    f18iii_f18_insurance_investment_income_iqema_252d_jerk_21d_jerk_v133_signal,
    f18iii_f18_insurance_investment_income_iqema_378d_jerk_42d_jerk_v134_signal,
    f18iii_f18_insurance_investment_income_iqema_504d_jerk_63d_jerk_v135_signal,
    f18iii_f18_insurance_investment_income_iisharediff_5d_jerk_5d_jerk_v136_signal,
    f18iii_f18_insurance_investment_income_iisharediff_8d_jerk_10d_jerk_v137_signal,
    f18iii_f18_insurance_investment_income_iisharediff_10d_jerk_21d_jerk_v138_signal,
    f18iii_f18_insurance_investment_income_iisharediff_15d_jerk_42d_jerk_v139_signal,
    f18iii_f18_insurance_investment_income_iisharediff_21d_jerk_63d_jerk_v140_signal,
    f18iii_f18_insurance_investment_income_iisharediff_30d_jerk_5d_jerk_v141_signal,
    f18iii_f18_insurance_investment_income_iisharediff_42d_jerk_10d_jerk_v142_signal,
    f18iii_f18_insurance_investment_income_iisharediff_63d_jerk_21d_jerk_v143_signal,
    f18iii_f18_insurance_investment_income_iisharediff_90d_jerk_42d_jerk_v144_signal,
    f18iii_f18_insurance_investment_income_iisharediff_126d_jerk_63d_jerk_v145_signal,
    f18iii_f18_insurance_investment_income_iisharediff_150d_jerk_5d_jerk_v146_signal,
    f18iii_f18_insurance_investment_income_iisharediff_189d_jerk_10d_jerk_v147_signal,
    f18iii_f18_insurance_investment_income_iisharediff_252d_jerk_21d_jerk_v148_signal,
    f18iii_f18_insurance_investment_income_iisharediff_378d_jerk_42d_jerk_v149_signal,
    f18iii_f18_insurance_investment_income_iisharediff_504d_jerk_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INSURANCE_INVESTMENT_INCOME_REGISTRY_JERK_001_150 = REGISTRY


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
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "liabilities": liabilities, "equity": equity,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f18_netinc_revenue_ratio", "_f18_investment_income_share", "_f18_income_quality",)
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
    print(f"OK f18_insurance_investment_income_jerk_001_150_claude: {n_features} features pass")
