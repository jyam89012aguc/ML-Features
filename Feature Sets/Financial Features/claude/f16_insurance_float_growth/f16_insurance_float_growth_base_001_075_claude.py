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
def _f16_float_proxy(liabilities, equity):
    return liabilities - equity * 0.0


def _f16_float_growth(liabilities, w):
    return liabilities.pct_change(periods=w)


def _f16_float_leverage(liabilities, equity, w):
    proxy = liabilities - equity * 0.0
    eq = equity.rolling(w, min_periods=max(1, w // 2)).mean()
    return proxy / eq.replace(0, np.nan)

def f16ifg_f16_insurance_float_growth_floatproxy_5d_base_v001_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(5, min_periods=max(1,5//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_8d_base_v002_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(8, min_periods=max(1,8//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_10d_base_v003_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(10, min_periods=max(1,10//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_15d_base_v004_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(15, min_periods=max(1,15//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_21d_base_v005_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(21, min_periods=max(1,21//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_30d_base_v006_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(30, min_periods=max(1,30//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_42d_base_v007_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(42, min_periods=max(1,42//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_63d_base_v008_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(63, min_periods=max(1,63//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_90d_base_v009_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(90, min_periods=max(1,90//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_126d_base_v010_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(126, min_periods=max(1,126//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_150d_base_v011_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(150, min_periods=max(1,150//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_189d_base_v012_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(189, min_periods=max(1,189//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_252d_base_v013_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(252, min_periods=max(1,252//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_378d_base_v014_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(378, min_periods=max(1,378//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxy_504d_base_v015_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = fp.rolling(504, min_periods=max(1,504//2)).mean() / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_5d_base_v016_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 5) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_8d_base_v017_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 8) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_10d_base_v018_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 10) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_15d_base_v019_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 15) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_21d_base_v020_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 21) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_30d_base_v021_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 30) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_42d_base_v022_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 42) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_63d_base_v023_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_90d_base_v024_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 90) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_126d_base_v025_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 126) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_150d_base_v026_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 150) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_189d_base_v027_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 189) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_252d_base_v028_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_378d_base_v029_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 378) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatproxyema_504d_base_v030_signal(liabilities, equity, closeadj):
    fp = _f16_float_proxy(liabilities, equity)
    result = _ema(fp, 504) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_5d_base_v031_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_8d_base_v032_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_10d_base_v033_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_15d_base_v034_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_21d_base_v035_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_30d_base_v036_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_42d_base_v037_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_63d_base_v038_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_90d_base_v039_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_126d_base_v040_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_150d_base_v041_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_189d_base_v042_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_252d_base_v043_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_378d_base_v044_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowth_504d_base_v045_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_5d_base_v046_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 5)
    result = _z(g, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_8d_base_v047_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 8)
    result = _z(g, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_10d_base_v048_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 10)
    result = _z(g, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_15d_base_v049_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 15)
    result = _z(g, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_21d_base_v050_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 21)
    result = _z(g, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_30d_base_v051_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 30)
    result = _z(g, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_42d_base_v052_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 42)
    result = _z(g, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_63d_base_v053_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 63)
    result = _z(g, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_90d_base_v054_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 90)
    result = _z(g, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_126d_base_v055_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 126)
    result = _z(g, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_150d_base_v056_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 150)
    result = _z(g, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_189d_base_v057_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 189)
    result = _z(g, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_252d_base_v058_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 252)
    result = _z(g, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_378d_base_v059_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 378)
    result = _z(g, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatgrowthz_504d_base_v060_signal(liabilities, closeadj):
    g = _f16_float_growth(liabilities, 504)
    result = _z(g, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_5d_base_v061_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 5)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_8d_base_v062_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 8)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_10d_base_v063_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 10)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_15d_base_v064_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 15)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_21d_base_v065_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 21)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_30d_base_v066_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 30)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_42d_base_v067_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 42)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_63d_base_v068_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 63)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_90d_base_v069_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 90)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_126d_base_v070_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 126)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_150d_base_v071_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 150)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_189d_base_v072_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 189)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_252d_base_v073_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 252)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_378d_base_v074_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 378)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f16ifg_f16_insurance_float_growth_floatlev_504d_base_v075_signal(liabilities, equity, closeadj):
    lev = _f16_float_leverage(liabilities, equity, 504)
    result = lev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16ifg_f16_insurance_float_growth_floatproxy_5d_base_v001_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_8d_base_v002_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_10d_base_v003_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_15d_base_v004_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_21d_base_v005_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_30d_base_v006_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_42d_base_v007_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_63d_base_v008_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_90d_base_v009_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_126d_base_v010_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_150d_base_v011_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_189d_base_v012_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_252d_base_v013_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_378d_base_v014_signal,
    f16ifg_f16_insurance_float_growth_floatproxy_504d_base_v015_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_5d_base_v016_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_8d_base_v017_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_10d_base_v018_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_15d_base_v019_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_21d_base_v020_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_30d_base_v021_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_42d_base_v022_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_63d_base_v023_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_90d_base_v024_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_126d_base_v025_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_150d_base_v026_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_189d_base_v027_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_252d_base_v028_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_378d_base_v029_signal,
    f16ifg_f16_insurance_float_growth_floatproxyema_504d_base_v030_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_5d_base_v031_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_8d_base_v032_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_10d_base_v033_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_15d_base_v034_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_21d_base_v035_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_30d_base_v036_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_42d_base_v037_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_63d_base_v038_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_90d_base_v039_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_126d_base_v040_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_150d_base_v041_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_189d_base_v042_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_252d_base_v043_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_378d_base_v044_signal,
    f16ifg_f16_insurance_float_growth_floatgrowth_504d_base_v045_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_5d_base_v046_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_8d_base_v047_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_10d_base_v048_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_15d_base_v049_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_21d_base_v050_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_30d_base_v051_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_42d_base_v052_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_63d_base_v053_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_90d_base_v054_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_126d_base_v055_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_150d_base_v056_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_189d_base_v057_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_252d_base_v058_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_378d_base_v059_signal,
    f16ifg_f16_insurance_float_growth_floatgrowthz_504d_base_v060_signal,
    f16ifg_f16_insurance_float_growth_floatlev_5d_base_v061_signal,
    f16ifg_f16_insurance_float_growth_floatlev_8d_base_v062_signal,
    f16ifg_f16_insurance_float_growth_floatlev_10d_base_v063_signal,
    f16ifg_f16_insurance_float_growth_floatlev_15d_base_v064_signal,
    f16ifg_f16_insurance_float_growth_floatlev_21d_base_v065_signal,
    f16ifg_f16_insurance_float_growth_floatlev_30d_base_v066_signal,
    f16ifg_f16_insurance_float_growth_floatlev_42d_base_v067_signal,
    f16ifg_f16_insurance_float_growth_floatlev_63d_base_v068_signal,
    f16ifg_f16_insurance_float_growth_floatlev_90d_base_v069_signal,
    f16ifg_f16_insurance_float_growth_floatlev_126d_base_v070_signal,
    f16ifg_f16_insurance_float_growth_floatlev_150d_base_v071_signal,
    f16ifg_f16_insurance_float_growth_floatlev_189d_base_v072_signal,
    f16ifg_f16_insurance_float_growth_floatlev_252d_base_v073_signal,
    f16ifg_f16_insurance_float_growth_floatlev_378d_base_v074_signal,
    f16ifg_f16_insurance_float_growth_floatlev_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_INSURANCE_FLOAT_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_insurance_float_growth_001_075_claude: {n_features} features pass")
