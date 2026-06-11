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

def f17icr_f17_insurance_combined_ratio_proxy_crproxy_5d_jerk_5d_jerk_v001_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(5, min_periods=max(1,5//2)).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_8d_jerk_10d_jerk_v002_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(8, min_periods=max(1,8//2)).mean() * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_10d_jerk_21d_jerk_v003_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(10, min_periods=max(1,10//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_15d_jerk_42d_jerk_v004_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(15, min_periods=max(1,15//2)).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_21d_jerk_63d_jerk_v005_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(21, min_periods=max(1,21//2)).mean() * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_30d_jerk_5d_jerk_v006_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(30, min_periods=max(1,30//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_42d_jerk_10d_jerk_v007_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(42, min_periods=max(1,42//2)).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_63d_jerk_21d_jerk_v008_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(63, min_periods=max(1,63//2)).mean() * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_90d_jerk_42d_jerk_v009_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(90, min_periods=max(1,90//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_126d_jerk_63d_jerk_v010_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(126, min_periods=max(1,126//2)).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_150d_jerk_5d_jerk_v011_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(150, min_periods=max(1,150//2)).mean() * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_189d_jerk_10d_jerk_v012_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(189, min_periods=max(1,189//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_252d_jerk_21d_jerk_v013_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(252, min_periods=max(1,252//2)).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_378d_jerk_42d_jerk_v014_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(378, min_periods=max(1,378//2)).mean() * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxy_504d_jerk_63d_jerk_v015_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = cr.rolling(504, min_periods=max(1,504//2)).mean() * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_5d_jerk_5d_jerk_v016_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_8d_jerk_10d_jerk_v017_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    base = t * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_10d_jerk_21d_jerk_v018_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    base = t * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_15d_jerk_42d_jerk_v019_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    base = t * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_21d_jerk_63d_jerk_v020_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    base = t * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_30d_jerk_5d_jerk_v021_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    base = t * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_42d_jerk_10d_jerk_v022_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    base = t * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_63d_jerk_21d_jerk_v023_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    base = t * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_90d_jerk_42d_jerk_v024_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    base = t * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_126d_jerk_63d_jerk_v025_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    base = t * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_150d_jerk_5d_jerk_v026_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    base = t * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_189d_jerk_10d_jerk_v027_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    base = t * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_252d_jerk_21d_jerk_v028_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    base = t * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_378d_jerk_42d_jerk_v029_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    base = t * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrend_504d_jerk_63d_jerk_v030_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    base = t * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_5d_jerk_5d_jerk_v031_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_8d_jerk_10d_jerk_v032_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_10d_jerk_21d_jerk_v033_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_15d_jerk_42d_jerk_v034_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_21d_jerk_63d_jerk_v035_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_30d_jerk_5d_jerk_v036_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_42d_jerk_10d_jerk_v037_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_63d_jerk_21d_jerk_v038_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_90d_jerk_42d_jerk_v039_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_126d_jerk_63d_jerk_v040_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_150d_jerk_5d_jerk_v041_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_189d_jerk_10d_jerk_v042_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_252d_jerk_21d_jerk_v043_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_378d_jerk_42d_jerk_v044_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyema_504d_jerk_63d_jerk_v045_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _ema(cr, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_5d_jerk_5d_jerk_v046_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_8d_jerk_10d_jerk_v047_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_10d_jerk_21d_jerk_v048_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_15d_jerk_42d_jerk_v049_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_21d_jerk_63d_jerk_v050_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_30d_jerk_5d_jerk_v051_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_42d_jerk_10d_jerk_v052_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_63d_jerk_21d_jerk_v053_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_90d_jerk_42d_jerk_v054_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_126d_jerk_63d_jerk_v055_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_150d_jerk_5d_jerk_v056_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_189d_jerk_10d_jerk_v057_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_252d_jerk_21d_jerk_v058_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_378d_jerk_42d_jerk_v059_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxyz_504d_jerk_63d_jerk_v060_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _z(cr, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_5d_jerk_5d_jerk_v061_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_8d_jerk_10d_jerk_v062_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_10d_jerk_21d_jerk_v063_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_15d_jerk_42d_jerk_v064_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_21d_jerk_63d_jerk_v065_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_30d_jerk_5d_jerk_v066_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_42d_jerk_10d_jerk_v067_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_63d_jerk_21d_jerk_v068_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_90d_jerk_42d_jerk_v069_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_126d_jerk_63d_jerk_v070_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_150d_jerk_5d_jerk_v071_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_189d_jerk_10d_jerk_v072_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_252d_jerk_21d_jerk_v073_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_378d_jerk_42d_jerk_v074_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crproxystd_504d_jerk_63d_jerk_v075_signal(opex, revenue, closeadj):
    cr = _f17_combined_ratio_proxy(opex, revenue)
    base = _std(cr, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_5d_jerk_5d_jerk_v076_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    base = _z(t, 252) * closeadj * (0.0500)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_8d_jerk_10d_jerk_v077_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    base = _z(t, 252) * closeadj * (0.0800)
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_10d_jerk_21d_jerk_v078_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    base = _z(t, 252) * closeadj * (0.1000)
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_15d_jerk_42d_jerk_v079_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    base = _z(t, 252) * closeadj * (0.1500)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_21d_jerk_63d_jerk_v080_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    base = _z(t, 252) * closeadj * (0.2100)
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_30d_jerk_5d_jerk_v081_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    base = _z(t, 252) * closeadj * (0.3000)
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_42d_jerk_10d_jerk_v082_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    base = _z(t, 252) * closeadj * (0.4200)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_63d_jerk_21d_jerk_v083_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    base = _z(t, 252) * closeadj * (0.6300)
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_90d_jerk_42d_jerk_v084_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    base = _z(t, 252) * closeadj * (0.9000)
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_126d_jerk_63d_jerk_v085_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    base = _z(t, 252) * closeadj * (1.2600)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_150d_jerk_5d_jerk_v086_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    base = _z(t, 252) * closeadj * (1.5000)
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_189d_jerk_10d_jerk_v087_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    base = _z(t, 252) * closeadj * (1.8900)
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_252d_jerk_21d_jerk_v088_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    base = _z(t, 252) * closeadj * (2.5200)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_378d_jerk_42d_jerk_v089_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    base = _z(t, 252) * closeadj * (3.7800)
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrendz_504d_jerk_63d_jerk_v090_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    base = _z(t, 252) * closeadj * (5.0400)
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_5d_jerk_5d_jerk_v091_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    base = ue * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_8d_jerk_10d_jerk_v092_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    base = ue * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_10d_jerk_21d_jerk_v093_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    base = ue * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_15d_jerk_42d_jerk_v094_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    base = ue * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_21d_jerk_63d_jerk_v095_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    base = ue * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_30d_jerk_5d_jerk_v096_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    base = ue * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_42d_jerk_10d_jerk_v097_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    base = ue * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_63d_jerk_21d_jerk_v098_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    base = ue * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_90d_jerk_42d_jerk_v099_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    base = ue * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_126d_jerk_63d_jerk_v100_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    base = ue * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_150d_jerk_5d_jerk_v101_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    base = ue * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_189d_jerk_10d_jerk_v102_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    base = ue * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_252d_jerk_21d_jerk_v103_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    base = ue * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_378d_jerk_42d_jerk_v104_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    base = ue * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweff_504d_jerk_63d_jerk_v105_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    base = ue * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_5d_jerk_5d_jerk_v106_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    base = _ema(ue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_8d_jerk_10d_jerk_v107_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    base = _ema(ue, 8) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_10d_jerk_21d_jerk_v108_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    base = _ema(ue, 10) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_15d_jerk_42d_jerk_v109_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    base = _ema(ue, 15) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_21d_jerk_63d_jerk_v110_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    base = _ema(ue, 21) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_30d_jerk_5d_jerk_v111_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    base = _ema(ue, 30) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_42d_jerk_10d_jerk_v112_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    base = _ema(ue, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_63d_jerk_21d_jerk_v113_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    base = _ema(ue, 63) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_90d_jerk_42d_jerk_v114_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    base = _ema(ue, 90) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_126d_jerk_63d_jerk_v115_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    base = _ema(ue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_150d_jerk_5d_jerk_v116_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    base = _ema(ue, 150) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_189d_jerk_10d_jerk_v117_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    base = _ema(ue, 189) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_252d_jerk_21d_jerk_v118_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    base = _ema(ue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_378d_jerk_42d_jerk_v119_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    base = _ema(ue, 378) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffema_504d_jerk_63d_jerk_v120_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    base = _ema(ue, 504) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_5d_jerk_5d_jerk_v121_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 5)
    base = _z(ue, 252) * closeadj * (0.0500)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_8d_jerk_10d_jerk_v122_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 8)
    base = _z(ue, 252) * closeadj * (0.0800)
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_10d_jerk_21d_jerk_v123_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 10)
    base = _z(ue, 252) * closeadj * (0.1000)
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_15d_jerk_42d_jerk_v124_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 15)
    base = _z(ue, 252) * closeadj * (0.1500)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_21d_jerk_63d_jerk_v125_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 21)
    base = _z(ue, 252) * closeadj * (0.2100)
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_30d_jerk_5d_jerk_v126_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 30)
    base = _z(ue, 252) * closeadj * (0.3000)
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_42d_jerk_10d_jerk_v127_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 42)
    base = _z(ue, 252) * closeadj * (0.4200)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_63d_jerk_21d_jerk_v128_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 63)
    base = _z(ue, 252) * closeadj * (0.6300)
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_90d_jerk_42d_jerk_v129_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 90)
    base = _z(ue, 252) * closeadj * (0.9000)
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_126d_jerk_63d_jerk_v130_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 126)
    base = _z(ue, 252) * closeadj * (1.2600)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_150d_jerk_5d_jerk_v131_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 150)
    base = _z(ue, 252) * closeadj * (1.5000)
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_189d_jerk_10d_jerk_v132_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 189)
    base = _z(ue, 252) * closeadj * (1.8900)
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_252d_jerk_21d_jerk_v133_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 252)
    base = _z(ue, 252) * closeadj * (2.5200)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_378d_jerk_42d_jerk_v134_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 378)
    base = _z(ue, 252) * closeadj * (3.7800)
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_uweffz_504d_jerk_63d_jerk_v135_signal(opex, sgna, revenue, closeadj):
    ue = _f17_underwriting_efficiency(opex, sgna, revenue, 504)
    base = _z(ue, 252) * closeadj * (5.0400)
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_5d_jerk_5d_jerk_v136_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 5)
    base = (t - t.shift(5)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_8d_jerk_10d_jerk_v137_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 8)
    base = (t - t.shift(8)) * closeadj
    sl = _slope_pct(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_10d_jerk_21d_jerk_v138_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 10)
    base = (t - t.shift(10)) * closeadj
    sl = _slope_diff_norm(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_15d_jerk_42d_jerk_v139_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 15)
    base = (t - t.shift(15)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_21d_jerk_63d_jerk_v140_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 21)
    base = (t - t.shift(21)) * closeadj
    sl = _slope_pct(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_30d_jerk_5d_jerk_v141_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 30)
    base = (t - t.shift(30)) * closeadj
    sl = _slope_diff_norm(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_42d_jerk_10d_jerk_v142_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 42)
    base = (t - t.shift(42)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_63d_jerk_21d_jerk_v143_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 63)
    base = (t - t.shift(63)) * closeadj
    sl = _slope_pct(base, 21)
    result = sl.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_90d_jerk_42d_jerk_v144_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 90)
    base = (t - t.shift(90)) * closeadj
    sl = _slope_diff_norm(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_126d_jerk_63d_jerk_v145_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 126)
    base = (t - t.shift(126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_150d_jerk_5d_jerk_v146_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 150)
    base = (t - t.shift(150)) * closeadj
    sl = _slope_pct(base, 5)
    result = sl.diff(periods=5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_189d_jerk_10d_jerk_v147_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 189)
    base = (t - t.shift(189)) * closeadj
    sl = _slope_diff_norm(base, 10)
    result = sl.diff(periods=10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_252d_jerk_21d_jerk_v148_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 252)
    base = (t - t.shift(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_378d_jerk_42d_jerk_v149_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 378)
    base = (t - t.shift(378)) * closeadj
    sl = _slope_pct(base, 42)
    result = sl.diff(periods=42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_504d_jerk_63d_jerk_v150_signal(opex, revenue, closeadj):
    t = _f17_combined_ratio_trend(opex, revenue, 504)
    base = (t - t.shift(504)) * closeadj
    sl = _slope_diff_norm(base, 63)
    result = sl.diff(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_5d_jerk_5d_jerk_v001_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_8d_jerk_10d_jerk_v002_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_10d_jerk_21d_jerk_v003_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_15d_jerk_42d_jerk_v004_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_21d_jerk_63d_jerk_v005_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_30d_jerk_5d_jerk_v006_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_42d_jerk_10d_jerk_v007_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_63d_jerk_21d_jerk_v008_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_90d_jerk_42d_jerk_v009_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_126d_jerk_63d_jerk_v010_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_150d_jerk_5d_jerk_v011_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_189d_jerk_10d_jerk_v012_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_252d_jerk_21d_jerk_v013_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_378d_jerk_42d_jerk_v014_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxy_504d_jerk_63d_jerk_v015_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_5d_jerk_5d_jerk_v016_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_8d_jerk_10d_jerk_v017_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_10d_jerk_21d_jerk_v018_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_15d_jerk_42d_jerk_v019_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_21d_jerk_63d_jerk_v020_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_30d_jerk_5d_jerk_v021_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_42d_jerk_10d_jerk_v022_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_63d_jerk_21d_jerk_v023_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_90d_jerk_42d_jerk_v024_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_126d_jerk_63d_jerk_v025_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_150d_jerk_5d_jerk_v026_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_189d_jerk_10d_jerk_v027_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_252d_jerk_21d_jerk_v028_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_378d_jerk_42d_jerk_v029_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrend_504d_jerk_63d_jerk_v030_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_5d_jerk_5d_jerk_v031_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_8d_jerk_10d_jerk_v032_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_10d_jerk_21d_jerk_v033_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_15d_jerk_42d_jerk_v034_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_21d_jerk_63d_jerk_v035_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_30d_jerk_5d_jerk_v036_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_42d_jerk_10d_jerk_v037_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_63d_jerk_21d_jerk_v038_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_90d_jerk_42d_jerk_v039_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_126d_jerk_63d_jerk_v040_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_150d_jerk_5d_jerk_v041_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_189d_jerk_10d_jerk_v042_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_252d_jerk_21d_jerk_v043_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_378d_jerk_42d_jerk_v044_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyema_504d_jerk_63d_jerk_v045_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_5d_jerk_5d_jerk_v046_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_8d_jerk_10d_jerk_v047_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_10d_jerk_21d_jerk_v048_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_15d_jerk_42d_jerk_v049_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_21d_jerk_63d_jerk_v050_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_30d_jerk_5d_jerk_v051_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_42d_jerk_10d_jerk_v052_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_63d_jerk_21d_jerk_v053_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_90d_jerk_42d_jerk_v054_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_126d_jerk_63d_jerk_v055_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_150d_jerk_5d_jerk_v056_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_189d_jerk_10d_jerk_v057_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_252d_jerk_21d_jerk_v058_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_378d_jerk_42d_jerk_v059_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxyz_504d_jerk_63d_jerk_v060_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_5d_jerk_5d_jerk_v061_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_8d_jerk_10d_jerk_v062_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_10d_jerk_21d_jerk_v063_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_15d_jerk_42d_jerk_v064_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_21d_jerk_63d_jerk_v065_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_30d_jerk_5d_jerk_v066_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_42d_jerk_10d_jerk_v067_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_63d_jerk_21d_jerk_v068_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_90d_jerk_42d_jerk_v069_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_126d_jerk_63d_jerk_v070_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_150d_jerk_5d_jerk_v071_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_189d_jerk_10d_jerk_v072_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_252d_jerk_21d_jerk_v073_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_378d_jerk_42d_jerk_v074_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crproxystd_504d_jerk_63d_jerk_v075_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_5d_jerk_5d_jerk_v076_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_8d_jerk_10d_jerk_v077_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_10d_jerk_21d_jerk_v078_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_15d_jerk_42d_jerk_v079_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_21d_jerk_63d_jerk_v080_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_30d_jerk_5d_jerk_v081_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_42d_jerk_10d_jerk_v082_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_63d_jerk_21d_jerk_v083_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_90d_jerk_42d_jerk_v084_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_126d_jerk_63d_jerk_v085_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_150d_jerk_5d_jerk_v086_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_189d_jerk_10d_jerk_v087_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_252d_jerk_21d_jerk_v088_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_378d_jerk_42d_jerk_v089_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrendz_504d_jerk_63d_jerk_v090_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_5d_jerk_5d_jerk_v091_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_8d_jerk_10d_jerk_v092_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_10d_jerk_21d_jerk_v093_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_15d_jerk_42d_jerk_v094_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_21d_jerk_63d_jerk_v095_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_30d_jerk_5d_jerk_v096_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_42d_jerk_10d_jerk_v097_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_63d_jerk_21d_jerk_v098_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_90d_jerk_42d_jerk_v099_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_126d_jerk_63d_jerk_v100_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_150d_jerk_5d_jerk_v101_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_189d_jerk_10d_jerk_v102_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_252d_jerk_21d_jerk_v103_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_378d_jerk_42d_jerk_v104_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweff_504d_jerk_63d_jerk_v105_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_5d_jerk_5d_jerk_v106_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_8d_jerk_10d_jerk_v107_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_10d_jerk_21d_jerk_v108_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_15d_jerk_42d_jerk_v109_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_21d_jerk_63d_jerk_v110_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_30d_jerk_5d_jerk_v111_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_42d_jerk_10d_jerk_v112_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_63d_jerk_21d_jerk_v113_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_90d_jerk_42d_jerk_v114_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_126d_jerk_63d_jerk_v115_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_150d_jerk_5d_jerk_v116_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_189d_jerk_10d_jerk_v117_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_252d_jerk_21d_jerk_v118_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_378d_jerk_42d_jerk_v119_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffema_504d_jerk_63d_jerk_v120_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_5d_jerk_5d_jerk_v121_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_8d_jerk_10d_jerk_v122_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_10d_jerk_21d_jerk_v123_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_15d_jerk_42d_jerk_v124_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_21d_jerk_63d_jerk_v125_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_30d_jerk_5d_jerk_v126_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_42d_jerk_10d_jerk_v127_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_63d_jerk_21d_jerk_v128_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_90d_jerk_42d_jerk_v129_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_126d_jerk_63d_jerk_v130_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_150d_jerk_5d_jerk_v131_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_189d_jerk_10d_jerk_v132_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_252d_jerk_21d_jerk_v133_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_378d_jerk_42d_jerk_v134_signal,
    f17icr_f17_insurance_combined_ratio_proxy_uweffz_504d_jerk_63d_jerk_v135_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_5d_jerk_5d_jerk_v136_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_8d_jerk_10d_jerk_v137_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_10d_jerk_21d_jerk_v138_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_15d_jerk_42d_jerk_v139_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_21d_jerk_63d_jerk_v140_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_30d_jerk_5d_jerk_v141_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_42d_jerk_10d_jerk_v142_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_63d_jerk_21d_jerk_v143_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_90d_jerk_42d_jerk_v144_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_126d_jerk_63d_jerk_v145_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_150d_jerk_5d_jerk_v146_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_189d_jerk_10d_jerk_v147_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_252d_jerk_21d_jerk_v148_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_378d_jerk_42d_jerk_v149_signal,
    f17icr_f17_insurance_combined_ratio_proxy_crtrenddiff_504d_jerk_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_INSURANCE_COMBINED_RATIO_PROXY_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_insurance_combined_ratio_proxy_jerk_001_150_claude: {n_features} features pass")
