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

# ===== folder domain primitives =====
def _f16_float_proxy(liabilities, equity):
    return liabilities - equity * 0.0


def _f16_float_growth(liabilities, w):
    return liabilities.pct_change(periods=w)


def _f16_float_leverage(liabilities, equity, w):
    proxy = liabilities - equity * 0.0
    eq = equity.rolling(w, min_periods=max(1, w // 2)).mean()
    return proxy / eq.replace(0, np.nan)

def f16ifg_f16_insurance_float_growth_floatproxy_5d_slope_5d_slope_v001_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(5, min_periods=max(1,5//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_8d_slope_10d_slope_v002_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(8, min_periods=max(1,8//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_10d_slope_21d_slope_v003_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(10, min_periods=max(1,10//2)).mean() / closeadj.replace(0, np.nan)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_15d_slope_42d_slope_v004_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(15, min_periods=max(1,15//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_21d_slope_63d_slope_v005_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(21, min_periods=max(1,21//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_30d_slope_126d_slope_v006_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(30, min_periods=max(1,30//2)).mean() / closeadj.replace(0, np.nan)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_42d_slope_5d_slope_v007_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(42, min_periods=max(1,42//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_63d_slope_10d_slope_v008_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(63, min_periods=max(1,63//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_90d_slope_21d_slope_v009_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(90, min_periods=max(1,90//2)).mean() / closeadj.replace(0, np.nan)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_126d_slope_42d_slope_v010_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(126, min_periods=max(1,126//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_150d_slope_63d_slope_v011_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(150, min_periods=max(1,150//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_189d_slope_126d_slope_v012_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(189, min_periods=max(1,189//2)).mean() / closeadj.replace(0, np.nan)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_252d_slope_5d_slope_v013_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(252, min_periods=max(1,252//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_378d_slope_10d_slope_v014_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(378, min_periods=max(1,378//2)).mean() / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_504d_slope_21d_slope_v015_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = fp.rolling(504, min_periods=max(1,504//2)).mean() / closeadj.replace(0, np.nan)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_5d_slope_42d_slope_v016_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 5) * closeadj / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_8d_slope_63d_slope_v017_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 8) * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_10d_slope_126d_slope_v018_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 10) * closeadj / 1e9
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_15d_slope_5d_slope_v019_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 15) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_21d_slope_10d_slope_v020_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_30d_slope_21d_slope_v021_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 30) * closeadj / 1e9
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_42d_slope_42d_slope_v022_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 42) * closeadj / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_63d_slope_63d_slope_v023_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_90d_slope_126d_slope_v024_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 90) * closeadj / 1e9
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_126d_slope_5d_slope_v025_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 126) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_150d_slope_10d_slope_v026_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 150) * closeadj / 1e9
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_189d_slope_21d_slope_v027_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 189) * closeadj / 1e9
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_252d_slope_42d_slope_v028_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 252) * closeadj / 1e9
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_378d_slope_63d_slope_v029_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 378) * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_504d_slope_126d_slope_v030_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _ema(fp, 504) * closeadj / 1e9
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_5d_slope_5d_slope_v031_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_8d_slope_10d_slope_v032_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    base = g * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_10d_slope_21d_slope_v033_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    base = g * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_15d_slope_42d_slope_v034_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    base = g * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_21d_slope_63d_slope_v035_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    base = g * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_30d_slope_126d_slope_v036_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    base = g * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_42d_slope_5d_slope_v037_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_63d_slope_10d_slope_v038_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    base = g * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_90d_slope_21d_slope_v039_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    base = g * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_126d_slope_42d_slope_v040_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    base = g * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_150d_slope_63d_slope_v041_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    base = g * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_189d_slope_126d_slope_v042_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    base = g * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_252d_slope_5d_slope_v043_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    base = g * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_378d_slope_10d_slope_v044_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    base = g * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_504d_slope_21d_slope_v045_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    base = g * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_5d_slope_42d_slope_v046_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    base = _z(g, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_8d_slope_63d_slope_v047_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    base = _z(g, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_10d_slope_126d_slope_v048_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    base = _z(g, 252) * closeadj * (0.1000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_15d_slope_5d_slope_v049_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    base = _z(g, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_21d_slope_10d_slope_v050_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    base = _z(g, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_30d_slope_21d_slope_v051_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    base = _z(g, 252) * closeadj * (0.3000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_42d_slope_42d_slope_v052_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    base = _z(g, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_63d_slope_63d_slope_v053_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    base = _z(g, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_90d_slope_126d_slope_v054_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    base = _z(g, 252) * closeadj * (0.9000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_126d_slope_5d_slope_v055_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    base = _z(g, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_150d_slope_10d_slope_v056_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    base = _z(g, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_189d_slope_21d_slope_v057_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    base = _z(g, 252) * closeadj * (1.8900)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_252d_slope_42d_slope_v058_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    base = _z(g, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_378d_slope_63d_slope_v059_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    base = _z(g, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_504d_slope_126d_slope_v060_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    base = _z(g, 252) * closeadj * (5.0400)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_5d_slope_5d_slope_v061_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    base = lev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_8d_slope_10d_slope_v062_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    base = lev * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_10d_slope_21d_slope_v063_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    base = lev * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_15d_slope_42d_slope_v064_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    base = lev * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_21d_slope_63d_slope_v065_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    base = lev * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_30d_slope_126d_slope_v066_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    base = lev * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_42d_slope_5d_slope_v067_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    base = lev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_63d_slope_10d_slope_v068_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    base = lev * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_90d_slope_21d_slope_v069_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    base = lev * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_126d_slope_42d_slope_v070_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    base = lev * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_150d_slope_63d_slope_v071_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    base = lev * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_189d_slope_126d_slope_v072_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    base = lev * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_252d_slope_5d_slope_v073_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    base = lev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_378d_slope_10d_slope_v074_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    base = lev * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_504d_slope_21d_slope_v075_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    base = lev * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_5d_slope_42d_slope_v076_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    base = _mean(lev, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_8d_slope_63d_slope_v077_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    base = _mean(lev, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_10d_slope_126d_slope_v078_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    base = _mean(lev, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_15d_slope_5d_slope_v079_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    base = _mean(lev, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_21d_slope_10d_slope_v080_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    base = _mean(lev, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_30d_slope_21d_slope_v081_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    base = _mean(lev, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_42d_slope_42d_slope_v082_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    base = _mean(lev, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_63d_slope_63d_slope_v083_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    base = _mean(lev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_90d_slope_126d_slope_v084_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    base = _mean(lev, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_126d_slope_5d_slope_v085_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    base = _mean(lev, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_150d_slope_10d_slope_v086_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    base = _mean(lev, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_189d_slope_21d_slope_v087_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    base = _mean(lev, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_252d_slope_42d_slope_v088_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    base = _mean(lev, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_378d_slope_63d_slope_v089_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    base = _mean(lev, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevsm_504d_slope_126d_slope_v090_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    base = _mean(lev, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_5d_slope_5d_slope_v091_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    base = _ema(g, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_8d_slope_10d_slope_v092_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    base = _ema(g, 8) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_10d_slope_21d_slope_v093_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    base = _ema(g, 10) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_15d_slope_42d_slope_v094_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    base = _ema(g, 15) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_21d_slope_63d_slope_v095_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    base = _ema(g, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_30d_slope_126d_slope_v096_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    base = _ema(g, 30) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_42d_slope_5d_slope_v097_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    base = _ema(g, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_63d_slope_10d_slope_v098_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    base = _ema(g, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_90d_slope_21d_slope_v099_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    base = _ema(g, 90) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_126d_slope_42d_slope_v100_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    base = _ema(g, 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_150d_slope_63d_slope_v101_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    base = _ema(g, 150) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_189d_slope_126d_slope_v102_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    base = _ema(g, 189) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_252d_slope_5d_slope_v103_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    base = _ema(g, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_378d_slope_10d_slope_v104_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    base = _ema(g, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgema_504d_slope_21d_slope_v105_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    base = _ema(g, 504) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_5d_slope_42d_slope_v106_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_8d_slope_63d_slope_v107_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_10d_slope_126d_slope_v108_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_15d_slope_5d_slope_v109_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_21d_slope_10d_slope_v110_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_30d_slope_21d_slope_v111_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_42d_slope_42d_slope_v112_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_63d_slope_63d_slope_v113_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_90d_slope_126d_slope_v114_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_126d_slope_5d_slope_v115_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_150d_slope_10d_slope_v116_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_189d_slope_21d_slope_v117_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_252d_slope_42d_slope_v118_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_378d_slope_63d_slope_v119_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyz_504d_slope_126d_slope_v120_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    base = _z(fp, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_5d_slope_5d_slope_v121_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    base = _z(lev, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_8d_slope_10d_slope_v122_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    base = _z(lev, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_10d_slope_21d_slope_v123_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    base = _z(lev, 252) * closeadj * (0.1000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_15d_slope_42d_slope_v124_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    base = _z(lev, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_21d_slope_63d_slope_v125_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    base = _z(lev, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_30d_slope_126d_slope_v126_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    base = _z(lev, 252) * closeadj * (0.3000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_42d_slope_5d_slope_v127_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    base = _z(lev, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_63d_slope_10d_slope_v128_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    base = _z(lev, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_90d_slope_21d_slope_v129_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    base = _z(lev, 252) * closeadj * (0.9000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_126d_slope_42d_slope_v130_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    base = _z(lev, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_150d_slope_63d_slope_v131_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    base = _z(lev, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_189d_slope_126d_slope_v132_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    base = _z(lev, 252) * closeadj * (1.8900)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_252d_slope_5d_slope_v133_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    base = _z(lev, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_378d_slope_10d_slope_v134_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    base = _z(lev, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlevz_504d_slope_21d_slope_v135_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    base = _z(lev, 252) * closeadj * (5.0400)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_5d_slope_42d_slope_v136_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    base = _std(g, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_8d_slope_63d_slope_v137_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    base = _std(g, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_10d_slope_126d_slope_v138_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    base = _std(g, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_15d_slope_5d_slope_v139_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    base = _std(g, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_21d_slope_10d_slope_v140_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    base = _std(g, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_30d_slope_21d_slope_v141_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    base = _std(g, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_42d_slope_42d_slope_v142_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    base = _std(g, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_63d_slope_63d_slope_v143_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    base = _std(g, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_90d_slope_126d_slope_v144_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    base = _std(g, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_126d_slope_5d_slope_v145_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    base = _std(g, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_150d_slope_10d_slope_v146_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    base = _std(g, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_189d_slope_21d_slope_v147_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    base = _std(g, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_252d_slope_42d_slope_v148_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    base = _std(g, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_378d_slope_63d_slope_v149_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    base = _std(g, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgstd_504d_slope_126d_slope_v150_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    base = _std(g, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ifg_f16_insurance_float_growth_floatproxy_5d_slope_5d_slope_v001_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_8d_slope_10d_slope_v002_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_10d_slope_21d_slope_v003_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_15d_slope_42d_slope_v004_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_21d_slope_63d_slope_v005_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_30d_slope_126d_slope_v006_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_42d_slope_5d_slope_v007_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_63d_slope_10d_slope_v008_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_90d_slope_21d_slope_v009_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_126d_slope_42d_slope_v010_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_150d_slope_63d_slope_v011_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_189d_slope_126d_slope_v012_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_252d_slope_5d_slope_v013_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_378d_slope_10d_slope_v014_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_504d_slope_21d_slope_v015_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_5d_slope_42d_slope_v016_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_8d_slope_63d_slope_v017_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_10d_slope_126d_slope_v018_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_15d_slope_5d_slope_v019_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_21d_slope_10d_slope_v020_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_30d_slope_21d_slope_v021_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_42d_slope_42d_slope_v022_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_63d_slope_63d_slope_v023_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_90d_slope_126d_slope_v024_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_126d_slope_5d_slope_v025_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_150d_slope_10d_slope_v026_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_189d_slope_21d_slope_v027_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_252d_slope_42d_slope_v028_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_378d_slope_63d_slope_v029_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_504d_slope_126d_slope_v030_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_5d_slope_5d_slope_v031_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_8d_slope_10d_slope_v032_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_10d_slope_21d_slope_v033_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_15d_slope_42d_slope_v034_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_21d_slope_63d_slope_v035_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_30d_slope_126d_slope_v036_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_42d_slope_5d_slope_v037_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_63d_slope_10d_slope_v038_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_90d_slope_21d_slope_v039_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_126d_slope_42d_slope_v040_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_150d_slope_63d_slope_v041_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_189d_slope_126d_slope_v042_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_252d_slope_5d_slope_v043_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_378d_slope_10d_slope_v044_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_504d_slope_21d_slope_v045_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_5d_slope_42d_slope_v046_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_8d_slope_63d_slope_v047_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_10d_slope_126d_slope_v048_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_15d_slope_5d_slope_v049_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_21d_slope_10d_slope_v050_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_30d_slope_21d_slope_v051_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_42d_slope_42d_slope_v052_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_63d_slope_63d_slope_v053_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_90d_slope_126d_slope_v054_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_126d_slope_5d_slope_v055_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_150d_slope_10d_slope_v056_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_189d_slope_21d_slope_v057_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_252d_slope_42d_slope_v058_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_378d_slope_63d_slope_v059_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_504d_slope_126d_slope_v060_signal,
    f16ifg_f16_insurance_float_growth_floatlev_5d_slope_5d_slope_v061_signal,
    f16ifg_f16_insurance_float_growth_floatlev_8d_slope_10d_slope_v062_signal,
    f16ifg_f16_insurance_float_growth_floatlev_10d_slope_21d_slope_v063_signal,
    f16ifg_f16_insurance_float_growth_floatlev_15d_slope_42d_slope_v064_signal,
    f16ifg_f16_insurance_float_growth_floatlev_21d_slope_63d_slope_v065_signal,
    f16ifg_f16_insurance_float_growth_floatlev_30d_slope_126d_slope_v066_signal,
    f16ifg_f16_insurance_float_growth_floatlev_42d_slope_5d_slope_v067_signal,
    f16ifg_f16_insurance_float_growth_floatlev_63d_slope_10d_slope_v068_signal,
    f16ifg_f16_insurance_float_growth_floatlev_90d_slope_21d_slope_v069_signal,
    f16ifg_f16_insurance_float_growth_floatlev_126d_slope_42d_slope_v070_signal,
    f16ifg_f16_insurance_float_growth_floatlev_150d_slope_63d_slope_v071_signal,
    f16ifg_f16_insurance_float_growth_floatlev_189d_slope_126d_slope_v072_signal,
    f16ifg_f16_insurance_float_growth_floatlev_252d_slope_5d_slope_v073_signal,
    f16ifg_f16_insurance_float_growth_floatlev_378d_slope_10d_slope_v074_signal,
    f16ifg_f16_insurance_float_growth_floatlev_504d_slope_21d_slope_v075_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_5d_slope_42d_slope_v076_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_8d_slope_63d_slope_v077_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_10d_slope_126d_slope_v078_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_15d_slope_5d_slope_v079_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_21d_slope_10d_slope_v080_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_30d_slope_21d_slope_v081_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_42d_slope_42d_slope_v082_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_63d_slope_63d_slope_v083_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_90d_slope_126d_slope_v084_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_126d_slope_5d_slope_v085_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_150d_slope_10d_slope_v086_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_189d_slope_21d_slope_v087_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_252d_slope_42d_slope_v088_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_378d_slope_63d_slope_v089_signal,
    f16ifg_f16_insurance_float_growth_floatlevsm_504d_slope_126d_slope_v090_signal,
    f16ifg_f16_insurance_float_growth_floatgema_5d_slope_5d_slope_v091_signal,
    f16ifg_f16_insurance_float_growth_floatgema_8d_slope_10d_slope_v092_signal,
    f16ifg_f16_insurance_float_growth_floatgema_10d_slope_21d_slope_v093_signal,
    f16ifg_f16_insurance_float_growth_floatgema_15d_slope_42d_slope_v094_signal,
    f16ifg_f16_insurance_float_growth_floatgema_21d_slope_63d_slope_v095_signal,
    f16ifg_f16_insurance_float_growth_floatgema_30d_slope_126d_slope_v096_signal,
    f16ifg_f16_insurance_float_growth_floatgema_42d_slope_5d_slope_v097_signal,
    f16ifg_f16_insurance_float_growth_floatgema_63d_slope_10d_slope_v098_signal,
    f16ifg_f16_insurance_float_growth_floatgema_90d_slope_21d_slope_v099_signal,
    f16ifg_f16_insurance_float_growth_floatgema_126d_slope_42d_slope_v100_signal,
    f16ifg_f16_insurance_float_growth_floatgema_150d_slope_63d_slope_v101_signal,
    f16ifg_f16_insurance_float_growth_floatgema_189d_slope_126d_slope_v102_signal,
    f16ifg_f16_insurance_float_growth_floatgema_252d_slope_5d_slope_v103_signal,
    f16ifg_f16_insurance_float_growth_floatgema_378d_slope_10d_slope_v104_signal,
    f16ifg_f16_insurance_float_growth_floatgema_504d_slope_21d_slope_v105_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_5d_slope_42d_slope_v106_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_8d_slope_63d_slope_v107_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_10d_slope_126d_slope_v108_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_15d_slope_5d_slope_v109_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_21d_slope_10d_slope_v110_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_30d_slope_21d_slope_v111_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_42d_slope_42d_slope_v112_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_63d_slope_63d_slope_v113_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_90d_slope_126d_slope_v114_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_126d_slope_5d_slope_v115_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_150d_slope_10d_slope_v116_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_189d_slope_21d_slope_v117_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_252d_slope_42d_slope_v118_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_378d_slope_63d_slope_v119_signal,
    f16ifg_f16_insurance_float_growth_floatproxyz_504d_slope_126d_slope_v120_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_5d_slope_5d_slope_v121_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_8d_slope_10d_slope_v122_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_10d_slope_21d_slope_v123_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_15d_slope_42d_slope_v124_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_21d_slope_63d_slope_v125_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_30d_slope_126d_slope_v126_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_42d_slope_5d_slope_v127_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_63d_slope_10d_slope_v128_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_90d_slope_21d_slope_v129_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_126d_slope_42d_slope_v130_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_150d_slope_63d_slope_v131_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_189d_slope_126d_slope_v132_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_252d_slope_5d_slope_v133_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_378d_slope_10d_slope_v134_signal,
    f16ifg_f16_insurance_float_growth_floatlevz_504d_slope_21d_slope_v135_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_5d_slope_42d_slope_v136_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_8d_slope_63d_slope_v137_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_10d_slope_126d_slope_v138_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_15d_slope_5d_slope_v139_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_21d_slope_10d_slope_v140_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_30d_slope_21d_slope_v141_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_42d_slope_42d_slope_v142_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_63d_slope_63d_slope_v143_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_90d_slope_126d_slope_v144_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_126d_slope_5d_slope_v145_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_150d_slope_10d_slope_v146_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_189d_slope_21d_slope_v147_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_252d_slope_42d_slope_v148_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_378d_slope_63d_slope_v149_signal,
    f16ifg_f16_insurance_float_growth_floatgstd_504d_slope_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_INSURANCE_FLOAT_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f16_float_proxy", "_f16_float_growth", "_f16_float_leverage",)
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
    print(f"OK f16_insurance_float_growth_slope_001_150_claude: {n_features} features pass")
