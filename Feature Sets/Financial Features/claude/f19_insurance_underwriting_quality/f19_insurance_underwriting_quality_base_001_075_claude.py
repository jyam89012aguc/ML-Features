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
def _f19_margin_floor(netmargin, w):
    return netmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f19_uw_quality(netmargin, w):
    m = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = netmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f19_uw_durability(netmargin, ebitdamargin, w):
    nm = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return nm / em.replace(0, np.nan)

def f19iuq_f19_insurance_underwriting_quality_mfloor_5d_base_v001_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_8d_base_v002_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_10d_base_v003_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_15d_base_v004_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_21d_base_v005_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_30d_base_v006_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_42d_base_v007_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_63d_base_v008_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_90d_base_v009_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_126d_base_v010_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_150d_base_v011_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_189d_base_v012_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_252d_base_v013_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_378d_base_v014_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_504d_base_v015_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    result = mf * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_5d_base_v016_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    result = _ema(mf, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_8d_base_v017_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    result = _ema(mf, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_10d_base_v018_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    result = _ema(mf, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_15d_base_v019_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    result = _ema(mf, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_21d_base_v020_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    result = _ema(mf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_30d_base_v021_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    result = _ema(mf, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_42d_base_v022_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    result = _ema(mf, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_63d_base_v023_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    result = _ema(mf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_90d_base_v024_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    result = _ema(mf, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_126d_base_v025_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    result = _ema(mf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_150d_base_v026_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    result = _ema(mf, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_189d_base_v027_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    result = _ema(mf, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_252d_base_v028_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    result = _ema(mf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_378d_base_v029_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    result = _ema(mf, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_504d_base_v030_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    result = _ema(mf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_5d_base_v031_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    result = _z(mf, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_8d_base_v032_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    result = _z(mf, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_10d_base_v033_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    result = _z(mf, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_15d_base_v034_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    result = _z(mf, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_21d_base_v035_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    result = _z(mf, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_30d_base_v036_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    result = _z(mf, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_42d_base_v037_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    result = _z(mf, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_63d_base_v038_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    result = _z(mf, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_90d_base_v039_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    result = _z(mf, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_126d_base_v040_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    result = _z(mf, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_150d_base_v041_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    result = _z(mf, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_189d_base_v042_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    result = _z(mf, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_252d_base_v043_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    result = _z(mf, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_378d_base_v044_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    result = _z(mf, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_504d_base_v045_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    result = _z(mf, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_5d_base_v046_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_8d_base_v047_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_10d_base_v048_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_15d_base_v049_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_21d_base_v050_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_30d_base_v051_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_42d_base_v052_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_63d_base_v053_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_90d_base_v054_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_126d_base_v055_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_150d_base_v056_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_189d_base_v057_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_252d_base_v058_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_378d_base_v059_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_504d_base_v060_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    result = q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_5d_base_v061_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    result = _ema(q, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_8d_base_v062_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    result = _ema(q, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_10d_base_v063_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    result = _ema(q, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_15d_base_v064_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    result = _ema(q, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_21d_base_v065_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    result = _ema(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_30d_base_v066_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    result = _ema(q, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_42d_base_v067_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    result = _ema(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_63d_base_v068_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    result = _ema(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_90d_base_v069_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    result = _ema(q, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_126d_base_v070_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    result = _ema(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_150d_base_v071_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    result = _ema(q, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_189d_base_v072_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    result = _ema(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_252d_base_v073_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    result = _ema(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_378d_base_v074_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    result = _ema(q, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_504d_base_v075_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    result = _ema(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19iuq_f19_insurance_underwriting_quality_mfloor_5d_base_v001_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_8d_base_v002_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_10d_base_v003_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_15d_base_v004_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_21d_base_v005_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_30d_base_v006_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_42d_base_v007_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_63d_base_v008_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_90d_base_v009_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_126d_base_v010_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_150d_base_v011_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_189d_base_v012_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_252d_base_v013_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_378d_base_v014_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_504d_base_v015_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_5d_base_v016_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_8d_base_v017_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_10d_base_v018_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_15d_base_v019_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_21d_base_v020_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_30d_base_v021_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_42d_base_v022_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_63d_base_v023_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_90d_base_v024_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_126d_base_v025_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_150d_base_v026_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_189d_base_v027_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_252d_base_v028_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_378d_base_v029_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_504d_base_v030_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_5d_base_v031_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_8d_base_v032_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_10d_base_v033_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_15d_base_v034_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_21d_base_v035_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_30d_base_v036_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_42d_base_v037_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_63d_base_v038_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_90d_base_v039_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_126d_base_v040_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_150d_base_v041_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_189d_base_v042_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_252d_base_v043_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_378d_base_v044_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_504d_base_v045_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_5d_base_v046_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_8d_base_v047_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_10d_base_v048_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_15d_base_v049_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_21d_base_v050_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_30d_base_v051_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_42d_base_v052_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_63d_base_v053_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_90d_base_v054_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_126d_base_v055_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_150d_base_v056_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_189d_base_v057_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_252d_base_v058_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_378d_base_v059_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_504d_base_v060_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_5d_base_v061_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_8d_base_v062_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_10d_base_v063_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_15d_base_v064_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_21d_base_v065_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_30d_base_v066_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_42d_base_v067_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_63d_base_v068_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_90d_base_v069_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_126d_base_v070_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_150d_base_v071_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_189d_base_v072_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_252d_base_v073_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_378d_base_v074_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_INSURANCE_UNDERWRITING_QUALITY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f19_margin_floor", "_f19_uw_quality", "_f19_uw_durability",)
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
    print(f"OK f19_insurance_underwriting_quality_001_075_claude: {n_features} features pass")
