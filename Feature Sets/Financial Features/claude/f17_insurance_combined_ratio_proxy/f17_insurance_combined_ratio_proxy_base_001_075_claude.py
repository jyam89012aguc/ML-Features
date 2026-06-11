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
def _f17_combined_ratio_proxy(opex, revenue):
    return opex / revenue.replace(0, np.nan)


def _f17_combined_ratio_trend(opex, revenue, w):
    cr = opex / revenue.replace(0, np.nan)
    return cr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_underwriting_efficiency(opex, sgna, revenue, w):
    cr = opex / revenue.replace(0, np.nan)
    sg = sgna / revenue.replace(0, np.nan)
    blend = cr + sg
    return blend.rolling(w, min_periods=max(1, w // 2)).mean()

def f17icr_f17_insurance_combined_ratio_proxy_crproxy_5d_base_v001_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(5, min_periods=max(1,5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_8d_base_v002_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(8, min_periods=max(1,8//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_10d_base_v003_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(10, min_periods=max(1,10//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_15d_base_v004_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(15, min_periods=max(1,15//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_21d_base_v005_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(21, min_periods=max(1,21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_30d_base_v006_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(30, min_periods=max(1,30//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_42d_base_v007_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(42, min_periods=max(1,42//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_63d_base_v008_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(63, min_periods=max(1,63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_90d_base_v009_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(90, min_periods=max(1,90//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_126d_base_v010_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(126, min_periods=max(1,126//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_150d_base_v011_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(150, min_periods=max(1,150//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_189d_base_v012_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(189, min_periods=max(1,189//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_252d_base_v013_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(252, min_periods=max(1,252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_378d_base_v014_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(378, min_periods=max(1,378//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_504d_base_v015_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = cr.rolling(504, min_periods=max(1,504//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_5d_base_v016_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_8d_base_v017_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_10d_base_v018_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_15d_base_v019_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_21d_base_v020_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_30d_base_v021_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_42d_base_v022_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_63d_base_v023_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_90d_base_v024_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_126d_base_v025_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_150d_base_v026_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_189d_base_v027_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_252d_base_v028_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_378d_base_v029_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_504d_base_v030_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    result = t * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_5d_base_v031_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_8d_base_v032_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_10d_base_v033_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_15d_base_v034_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_21d_base_v035_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_30d_base_v036_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_42d_base_v037_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_63d_base_v038_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_90d_base_v039_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_126d_base_v040_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_150d_base_v041_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_189d_base_v042_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_252d_base_v043_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_378d_base_v044_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_504d_base_v045_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _ema(cr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_5d_base_v046_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_8d_base_v047_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_10d_base_v048_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_15d_base_v049_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_21d_base_v050_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_30d_base_v051_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_42d_base_v052_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_63d_base_v053_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_90d_base_v054_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_126d_base_v055_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_150d_base_v056_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_189d_base_v057_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_252d_base_v058_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_378d_base_v059_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_504d_base_v060_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _z(cr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_5d_base_v061_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_8d_base_v062_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_10d_base_v063_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_15d_base_v064_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_21d_base_v065_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_30d_base_v066_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_42d_base_v067_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_63d_base_v068_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_90d_base_v069_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_126d_base_v070_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_150d_base_v071_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_189d_base_v072_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_252d_base_v073_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_378d_base_v074_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_504d_base_v075_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    result = _std(cr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_5d_base_v001_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_8d_base_v002_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_10d_base_v003_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_15d_base_v004_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_21d_base_v005_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_30d_base_v006_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_42d_base_v007_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_63d_base_v008_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_90d_base_v009_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_126d_base_v010_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_150d_base_v011_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_189d_base_v012_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_252d_base_v013_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_378d_base_v014_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_504d_base_v015_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_5d_base_v016_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_8d_base_v017_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_10d_base_v018_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_15d_base_v019_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_21d_base_v020_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_30d_base_v021_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_42d_base_v022_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_63d_base_v023_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_90d_base_v024_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_126d_base_v025_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_150d_base_v026_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_189d_base_v027_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_252d_base_v028_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_378d_base_v029_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_504d_base_v030_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_5d_base_v031_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_8d_base_v032_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_10d_base_v033_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_15d_base_v034_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_21d_base_v035_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_30d_base_v036_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_42d_base_v037_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_63d_base_v038_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_90d_base_v039_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_126d_base_v040_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_150d_base_v041_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_189d_base_v042_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_252d_base_v043_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_378d_base_v044_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_504d_base_v045_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_5d_base_v046_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_8d_base_v047_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_10d_base_v048_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_15d_base_v049_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_21d_base_v050_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_30d_base_v051_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_42d_base_v052_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_63d_base_v053_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_90d_base_v054_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_126d_base_v055_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_150d_base_v056_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_189d_base_v057_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_252d_base_v058_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_378d_base_v059_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_504d_base_v060_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_5d_base_v061_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_8d_base_v062_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_10d_base_v063_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_15d_base_v064_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_21d_base_v065_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_30d_base_v066_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_42d_base_v067_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_63d_base_v068_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_90d_base_v069_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_126d_base_v070_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_150d_base_v071_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_189d_base_v072_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_252d_base_v073_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_378d_base_v074_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_INSURANCE_COMBINED_RATIO_PROXY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f17_combined_ratio_proxy", "_f17_combined_ratio_trend", "_f17_underwriting_efficiency",)
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
    print(f"OK f17_insurance_combined_ratio_proxy_001_075_claude: {n_features} features pass")
