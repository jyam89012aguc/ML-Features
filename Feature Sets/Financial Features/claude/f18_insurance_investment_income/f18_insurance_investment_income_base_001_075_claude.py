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

def f18iii_f18_insurance_investment_income_nirratio_5d_base_v001_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(5, min_periods=max(1,5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_8d_base_v002_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(8, min_periods=max(1,8//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_10d_base_v003_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(10, min_periods=max(1,10//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_15d_base_v004_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(15, min_periods=max(1,15//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_21d_base_v005_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(21, min_periods=max(1,21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_30d_base_v006_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(30, min_periods=max(1,30//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_42d_base_v007_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(42, min_periods=max(1,42//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_63d_base_v008_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(63, min_periods=max(1,63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_90d_base_v009_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(90, min_periods=max(1,90//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_126d_base_v010_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(126, min_periods=max(1,126//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_150d_base_v011_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(150, min_periods=max(1,150//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_189d_base_v012_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(189, min_periods=max(1,189//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_252d_base_v013_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(252, min_periods=max(1,252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_378d_base_v014_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(378, min_periods=max(1,378//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratio_504d_base_v015_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = r.rolling(504, min_periods=max(1,504//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_5d_base_v016_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_8d_base_v017_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_10d_base_v018_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_15d_base_v019_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_21d_base_v020_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_30d_base_v021_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_42d_base_v022_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_63d_base_v023_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_90d_base_v024_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_126d_base_v025_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_150d_base_v026_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_189d_base_v027_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_252d_base_v028_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_378d_base_v029_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioema_504d_base_v030_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_5d_base_v031_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_8d_base_v032_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_10d_base_v033_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_15d_base_v034_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_21d_base_v035_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_30d_base_v036_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_42d_base_v037_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_63d_base_v038_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_90d_base_v039_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_126d_base_v040_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_150d_base_v041_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_189d_base_v042_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_252d_base_v043_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_378d_base_v044_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratiostd_504d_base_v045_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _std(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_5d_base_v046_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_8d_base_v047_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_10d_base_v048_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_15d_base_v049_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_21d_base_v050_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_30d_base_v051_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_42d_base_v052_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_63d_base_v053_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_90d_base_v054_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_126d_base_v055_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_150d_base_v056_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_189d_base_v057_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_252d_base_v058_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_378d_base_v059_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_nirratioz_504d_base_v060_signal(netinc, revenue, closeadj):
    r = _f18_netinc_revenue_ratio(netinc, revenue)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_5d_base_v061_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_8d_base_v062_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 8)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_10d_base_v063_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_15d_base_v064_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 15)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_21d_base_v065_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_30d_base_v066_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 30)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_42d_base_v067_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_63d_base_v068_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_90d_base_v069_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 90)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_126d_base_v070_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_150d_base_v071_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 150)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_189d_base_v072_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_252d_base_v073_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_378d_base_v074_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18iii_f18_insurance_investment_income_iishare_504d_base_v075_signal(netinc, revenue, closeadj):
    s = _f18_investment_income_share(netinc, revenue, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18iii_f18_insurance_investment_income_nirratio_5d_base_v001_signal,
    f18iii_f18_insurance_investment_income_nirratio_8d_base_v002_signal,
    f18iii_f18_insurance_investment_income_nirratio_10d_base_v003_signal,
    f18iii_f18_insurance_investment_income_nirratio_15d_base_v004_signal,
    f18iii_f18_insurance_investment_income_nirratio_21d_base_v005_signal,
    f18iii_f18_insurance_investment_income_nirratio_30d_base_v006_signal,
    f18iii_f18_insurance_investment_income_nirratio_42d_base_v007_signal,
    f18iii_f18_insurance_investment_income_nirratio_63d_base_v008_signal,
    f18iii_f18_insurance_investment_income_nirratio_90d_base_v009_signal,
    f18iii_f18_insurance_investment_income_nirratio_126d_base_v010_signal,
    f18iii_f18_insurance_investment_income_nirratio_150d_base_v011_signal,
    f18iii_f18_insurance_investment_income_nirratio_189d_base_v012_signal,
    f18iii_f18_insurance_investment_income_nirratio_252d_base_v013_signal,
    f18iii_f18_insurance_investment_income_nirratio_378d_base_v014_signal,
    f18iii_f18_insurance_investment_income_nirratio_504d_base_v015_signal,
    f18iii_f18_insurance_investment_income_nirratioema_5d_base_v016_signal,
    f18iii_f18_insurance_investment_income_nirratioema_8d_base_v017_signal,
    f18iii_f18_insurance_investment_income_nirratioema_10d_base_v018_signal,
    f18iii_f18_insurance_investment_income_nirratioema_15d_base_v019_signal,
    f18iii_f18_insurance_investment_income_nirratioema_21d_base_v020_signal,
    f18iii_f18_insurance_investment_income_nirratioema_30d_base_v021_signal,
    f18iii_f18_insurance_investment_income_nirratioema_42d_base_v022_signal,
    f18iii_f18_insurance_investment_income_nirratioema_63d_base_v023_signal,
    f18iii_f18_insurance_investment_income_nirratioema_90d_base_v024_signal,
    f18iii_f18_insurance_investment_income_nirratioema_126d_base_v025_signal,
    f18iii_f18_insurance_investment_income_nirratioema_150d_base_v026_signal,
    f18iii_f18_insurance_investment_income_nirratioema_189d_base_v027_signal,
    f18iii_f18_insurance_investment_income_nirratioema_252d_base_v028_signal,
    f18iii_f18_insurance_investment_income_nirratioema_378d_base_v029_signal,
    f18iii_f18_insurance_investment_income_nirratioema_504d_base_v030_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_5d_base_v031_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_8d_base_v032_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_10d_base_v033_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_15d_base_v034_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_21d_base_v035_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_30d_base_v036_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_42d_base_v037_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_63d_base_v038_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_90d_base_v039_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_126d_base_v040_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_150d_base_v041_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_189d_base_v042_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_252d_base_v043_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_378d_base_v044_signal,
    f18iii_f18_insurance_investment_income_nirratiostd_504d_base_v045_signal,
    f18iii_f18_insurance_investment_income_nirratioz_5d_base_v046_signal,
    f18iii_f18_insurance_investment_income_nirratioz_8d_base_v047_signal,
    f18iii_f18_insurance_investment_income_nirratioz_10d_base_v048_signal,
    f18iii_f18_insurance_investment_income_nirratioz_15d_base_v049_signal,
    f18iii_f18_insurance_investment_income_nirratioz_21d_base_v050_signal,
    f18iii_f18_insurance_investment_income_nirratioz_30d_base_v051_signal,
    f18iii_f18_insurance_investment_income_nirratioz_42d_base_v052_signal,
    f18iii_f18_insurance_investment_income_nirratioz_63d_base_v053_signal,
    f18iii_f18_insurance_investment_income_nirratioz_90d_base_v054_signal,
    f18iii_f18_insurance_investment_income_nirratioz_126d_base_v055_signal,
    f18iii_f18_insurance_investment_income_nirratioz_150d_base_v056_signal,
    f18iii_f18_insurance_investment_income_nirratioz_189d_base_v057_signal,
    f18iii_f18_insurance_investment_income_nirratioz_252d_base_v058_signal,
    f18iii_f18_insurance_investment_income_nirratioz_378d_base_v059_signal,
    f18iii_f18_insurance_investment_income_nirratioz_504d_base_v060_signal,
    f18iii_f18_insurance_investment_income_iishare_5d_base_v061_signal,
    f18iii_f18_insurance_investment_income_iishare_8d_base_v062_signal,
    f18iii_f18_insurance_investment_income_iishare_10d_base_v063_signal,
    f18iii_f18_insurance_investment_income_iishare_15d_base_v064_signal,
    f18iii_f18_insurance_investment_income_iishare_21d_base_v065_signal,
    f18iii_f18_insurance_investment_income_iishare_30d_base_v066_signal,
    f18iii_f18_insurance_investment_income_iishare_42d_base_v067_signal,
    f18iii_f18_insurance_investment_income_iishare_63d_base_v068_signal,
    f18iii_f18_insurance_investment_income_iishare_90d_base_v069_signal,
    f18iii_f18_insurance_investment_income_iishare_126d_base_v070_signal,
    f18iii_f18_insurance_investment_income_iishare_150d_base_v071_signal,
    f18iii_f18_insurance_investment_income_iishare_189d_base_v072_signal,
    f18iii_f18_insurance_investment_income_iishare_252d_base_v073_signal,
    f18iii_f18_insurance_investment_income_iishare_378d_base_v074_signal,
    f18iii_f18_insurance_investment_income_iishare_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_INSURANCE_INVESTMENT_INCOME_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_insurance_investment_income_001_075_claude: {n_features} features pass")
