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

def f19iuq_f19_insurance_underwriting_quality_mfloor_5d_slope_5d_slope_v001_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    base = mf * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_8d_slope_10d_slope_v002_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    base = mf * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_10d_slope_21d_slope_v003_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    base = mf * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_15d_slope_42d_slope_v004_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    base = mf * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_21d_slope_63d_slope_v005_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    base = mf * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_30d_slope_126d_slope_v006_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    base = mf * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_42d_slope_5d_slope_v007_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    base = mf * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_63d_slope_10d_slope_v008_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    base = mf * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_90d_slope_21d_slope_v009_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    base = mf * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_126d_slope_42d_slope_v010_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    base = mf * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_150d_slope_63d_slope_v011_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    base = mf * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_189d_slope_126d_slope_v012_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    base = mf * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_252d_slope_5d_slope_v013_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    base = mf * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_378d_slope_10d_slope_v014_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    base = mf * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloor_504d_slope_21d_slope_v015_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    base = mf * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_5d_slope_42d_slope_v016_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    base = _ema(mf, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_8d_slope_63d_slope_v017_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    base = _ema(mf, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_10d_slope_126d_slope_v018_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    base = _ema(mf, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_15d_slope_5d_slope_v019_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    base = _ema(mf, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_21d_slope_10d_slope_v020_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    base = _ema(mf, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_30d_slope_21d_slope_v021_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    base = _ema(mf, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_42d_slope_42d_slope_v022_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    base = _ema(mf, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_63d_slope_63d_slope_v023_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    base = _ema(mf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_90d_slope_126d_slope_v024_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    base = _ema(mf, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_126d_slope_5d_slope_v025_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    base = _ema(mf, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_150d_slope_10d_slope_v026_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    base = _ema(mf, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_189d_slope_21d_slope_v027_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    base = _ema(mf, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_252d_slope_42d_slope_v028_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    base = _ema(mf, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_378d_slope_63d_slope_v029_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    base = _ema(mf, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorema_504d_slope_126d_slope_v030_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    base = _ema(mf, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_5d_slope_5d_slope_v031_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    base = _z(mf, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_8d_slope_10d_slope_v032_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    base = _z(mf, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_10d_slope_21d_slope_v033_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    base = _z(mf, 252) * closeadj * (0.1000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_15d_slope_42d_slope_v034_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    base = _z(mf, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_21d_slope_63d_slope_v035_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    base = _z(mf, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_30d_slope_126d_slope_v036_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    base = _z(mf, 252) * closeadj * (0.3000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_42d_slope_5d_slope_v037_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    base = _z(mf, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_63d_slope_10d_slope_v038_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    base = _z(mf, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_90d_slope_21d_slope_v039_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    base = _z(mf, 252) * closeadj * (0.9000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_126d_slope_42d_slope_v040_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    base = _z(mf, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_150d_slope_63d_slope_v041_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    base = _z(mf, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_189d_slope_126d_slope_v042_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    base = _z(mf, 252) * closeadj * (1.8900)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_252d_slope_5d_slope_v043_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    base = _z(mf, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_378d_slope_10d_slope_v044_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    base = _z(mf, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloorz_504d_slope_21d_slope_v045_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    base = _z(mf, 252) * closeadj * (5.0400)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_5d_slope_42d_slope_v046_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    base = q * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_8d_slope_63d_slope_v047_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    base = q * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_10d_slope_126d_slope_v048_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    base = q * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_15d_slope_5d_slope_v049_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    base = q * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_21d_slope_10d_slope_v050_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    base = q * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_30d_slope_21d_slope_v051_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    base = q * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_42d_slope_42d_slope_v052_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    base = q * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_63d_slope_63d_slope_v053_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    base = q * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_90d_slope_126d_slope_v054_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    base = q * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_126d_slope_5d_slope_v055_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    base = q * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_150d_slope_10d_slope_v056_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    base = q * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_189d_slope_21d_slope_v057_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    base = q * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_252d_slope_42d_slope_v058_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    base = q * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_378d_slope_63d_slope_v059_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    base = q * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwq_504d_slope_126d_slope_v060_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    base = q * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_5d_slope_5d_slope_v061_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    base = _ema(q, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_8d_slope_10d_slope_v062_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    base = _ema(q, 8) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_10d_slope_21d_slope_v063_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    base = _ema(q, 10) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_15d_slope_42d_slope_v064_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    base = _ema(q, 15) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_21d_slope_63d_slope_v065_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    base = _ema(q, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_30d_slope_126d_slope_v066_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    base = _ema(q, 30) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_42d_slope_5d_slope_v067_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    base = _ema(q, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_63d_slope_10d_slope_v068_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    base = _ema(q, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_90d_slope_21d_slope_v069_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    base = _ema(q, 90) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_126d_slope_42d_slope_v070_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    base = _ema(q, 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_150d_slope_63d_slope_v071_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    base = _ema(q, 150) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_189d_slope_126d_slope_v072_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    base = _ema(q, 189) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_252d_slope_5d_slope_v073_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    base = _ema(q, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_378d_slope_10d_slope_v074_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    base = _ema(q, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqema_504d_slope_21d_slope_v075_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    base = _ema(q, 504) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_5d_slope_42d_slope_v076_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 5)
    base = _std(q, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_8d_slope_63d_slope_v077_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 8)
    base = _std(q, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_10d_slope_126d_slope_v078_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 10)
    base = _std(q, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_15d_slope_5d_slope_v079_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 15)
    base = _std(q, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_21d_slope_10d_slope_v080_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 21)
    base = _std(q, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_30d_slope_21d_slope_v081_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 30)
    base = _std(q, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_42d_slope_42d_slope_v082_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 42)
    base = _std(q, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_63d_slope_63d_slope_v083_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 63)
    base = _std(q, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_90d_slope_126d_slope_v084_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 90)
    base = _std(q, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_126d_slope_5d_slope_v085_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 126)
    base = _std(q, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_150d_slope_10d_slope_v086_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 150)
    base = _std(q, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_189d_slope_21d_slope_v087_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 189)
    base = _std(q, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_252d_slope_42d_slope_v088_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 252)
    base = _std(q, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_378d_slope_63d_slope_v089_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 378)
    base = _std(q, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwqstd_504d_slope_126d_slope_v090_signal(netmargin, closeadj):
    q = _f19_uw_quality(netmargin, 504)
    base = _std(q, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_5d_slope_5d_slope_v091_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_8d_slope_10d_slope_v092_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    base = d * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_10d_slope_21d_slope_v093_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    base = d * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_15d_slope_42d_slope_v094_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    base = d * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_21d_slope_63d_slope_v095_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    base = d * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_30d_slope_126d_slope_v096_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    base = d * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_42d_slope_5d_slope_v097_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_63d_slope_10d_slope_v098_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    base = d * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_90d_slope_21d_slope_v099_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    base = d * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_126d_slope_42d_slope_v100_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    base = d * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_150d_slope_63d_slope_v101_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    base = d * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_189d_slope_126d_slope_v102_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    base = d * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_252d_slope_5d_slope_v103_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    base = d * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_378d_slope_10d_slope_v104_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    base = d * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdur_504d_slope_21d_slope_v105_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    base = d * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_5d_slope_42d_slope_v106_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    base = _ema(d, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_8d_slope_63d_slope_v107_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    base = _ema(d, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_10d_slope_126d_slope_v108_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    base = _ema(d, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_15d_slope_5d_slope_v109_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    base = _ema(d, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_21d_slope_10d_slope_v110_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    base = _ema(d, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_30d_slope_21d_slope_v111_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    base = _ema(d, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_42d_slope_42d_slope_v112_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    base = _ema(d, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_63d_slope_63d_slope_v113_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    base = _ema(d, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_90d_slope_126d_slope_v114_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    base = _ema(d, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_126d_slope_5d_slope_v115_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    base = _ema(d, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_150d_slope_10d_slope_v116_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    base = _ema(d, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_189d_slope_21d_slope_v117_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    base = _ema(d, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_252d_slope_42d_slope_v118_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    base = _ema(d, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_378d_slope_63d_slope_v119_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    base = _ema(d, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurema_504d_slope_126d_slope_v120_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    base = _ema(d, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_5d_slope_5d_slope_v121_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 5)
    base = _z(d, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_8d_slope_10d_slope_v122_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 8)
    base = _z(d, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_10d_slope_21d_slope_v123_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 10)
    base = _z(d, 252) * closeadj * (0.1000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_15d_slope_42d_slope_v124_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 15)
    base = _z(d, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_21d_slope_63d_slope_v125_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 21)
    base = _z(d, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_30d_slope_126d_slope_v126_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 30)
    base = _z(d, 252) * closeadj * (0.3000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_42d_slope_5d_slope_v127_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 42)
    base = _z(d, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_63d_slope_10d_slope_v128_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 63)
    base = _z(d, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_90d_slope_21d_slope_v129_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 90)
    base = _z(d, 252) * closeadj * (0.9000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_126d_slope_42d_slope_v130_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 126)
    base = _z(d, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_150d_slope_63d_slope_v131_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 150)
    base = _z(d, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_189d_slope_126d_slope_v132_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 189)
    base = _z(d, 252) * closeadj * (1.8900)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_252d_slope_5d_slope_v133_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 252)
    base = _z(d, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_378d_slope_10d_slope_v134_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 378)
    base = _z(d, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_uwdurz_504d_slope_21d_slope_v135_signal(netmargin, ebitdamargin, closeadj):
    d = _f19_uw_durability(netmargin, ebitdamargin, 504)
    base = _z(d, 252) * closeadj * (5.0400)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_5d_slope_42d_slope_v136_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 5)
    base = (mf - mf.shift(5)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_8d_slope_63d_slope_v137_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 8)
    base = (mf - mf.shift(8)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_10d_slope_126d_slope_v138_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 10)
    base = (mf - mf.shift(10)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_15d_slope_5d_slope_v139_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 15)
    base = (mf - mf.shift(15)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_21d_slope_10d_slope_v140_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 21)
    base = (mf - mf.shift(21)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_30d_slope_21d_slope_v141_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 30)
    base = (mf - mf.shift(30)) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_42d_slope_42d_slope_v142_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 42)
    base = (mf - mf.shift(42)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_63d_slope_63d_slope_v143_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 63)
    base = (mf - mf.shift(63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_90d_slope_126d_slope_v144_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 90)
    base = (mf - mf.shift(90)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_126d_slope_5d_slope_v145_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 126)
    base = (mf - mf.shift(126)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_150d_slope_10d_slope_v146_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 150)
    base = (mf - mf.shift(150)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_189d_slope_21d_slope_v147_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 189)
    base = (mf - mf.shift(189)) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_252d_slope_42d_slope_v148_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 252)
    base = (mf - mf.shift(252)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_378d_slope_63d_slope_v149_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 378)
    base = (mf - mf.shift(378)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19iuq_f19_insurance_underwriting_quality_mfloordiff_504d_slope_126d_slope_v150_signal(netmargin, closeadj):
    mf = _f19_margin_floor(netmargin, 504)
    base = (mf - mf.shift(504)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19iuq_f19_insurance_underwriting_quality_mfloor_5d_slope_5d_slope_v001_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_8d_slope_10d_slope_v002_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_10d_slope_21d_slope_v003_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_15d_slope_42d_slope_v004_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_21d_slope_63d_slope_v005_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_30d_slope_126d_slope_v006_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_42d_slope_5d_slope_v007_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_63d_slope_10d_slope_v008_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_90d_slope_21d_slope_v009_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_126d_slope_42d_slope_v010_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_150d_slope_63d_slope_v011_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_189d_slope_126d_slope_v012_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_252d_slope_5d_slope_v013_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_378d_slope_10d_slope_v014_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloor_504d_slope_21d_slope_v015_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_5d_slope_42d_slope_v016_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_8d_slope_63d_slope_v017_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_10d_slope_126d_slope_v018_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_15d_slope_5d_slope_v019_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_21d_slope_10d_slope_v020_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_30d_slope_21d_slope_v021_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_42d_slope_42d_slope_v022_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_63d_slope_63d_slope_v023_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_90d_slope_126d_slope_v024_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_126d_slope_5d_slope_v025_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_150d_slope_10d_slope_v026_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_189d_slope_21d_slope_v027_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_252d_slope_42d_slope_v028_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_378d_slope_63d_slope_v029_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorema_504d_slope_126d_slope_v030_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_5d_slope_5d_slope_v031_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_8d_slope_10d_slope_v032_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_10d_slope_21d_slope_v033_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_15d_slope_42d_slope_v034_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_21d_slope_63d_slope_v035_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_30d_slope_126d_slope_v036_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_42d_slope_5d_slope_v037_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_63d_slope_10d_slope_v038_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_90d_slope_21d_slope_v039_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_126d_slope_42d_slope_v040_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_150d_slope_63d_slope_v041_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_189d_slope_126d_slope_v042_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_252d_slope_5d_slope_v043_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_378d_slope_10d_slope_v044_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloorz_504d_slope_21d_slope_v045_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_5d_slope_42d_slope_v046_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_8d_slope_63d_slope_v047_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_10d_slope_126d_slope_v048_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_15d_slope_5d_slope_v049_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_21d_slope_10d_slope_v050_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_30d_slope_21d_slope_v051_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_42d_slope_42d_slope_v052_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_63d_slope_63d_slope_v053_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_90d_slope_126d_slope_v054_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_126d_slope_5d_slope_v055_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_150d_slope_10d_slope_v056_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_189d_slope_21d_slope_v057_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_252d_slope_42d_slope_v058_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_378d_slope_63d_slope_v059_signal,
    f19iuq_f19_insurance_underwriting_quality_uwq_504d_slope_126d_slope_v060_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_5d_slope_5d_slope_v061_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_8d_slope_10d_slope_v062_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_10d_slope_21d_slope_v063_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_15d_slope_42d_slope_v064_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_21d_slope_63d_slope_v065_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_30d_slope_126d_slope_v066_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_42d_slope_5d_slope_v067_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_63d_slope_10d_slope_v068_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_90d_slope_21d_slope_v069_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_126d_slope_42d_slope_v070_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_150d_slope_63d_slope_v071_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_189d_slope_126d_slope_v072_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_252d_slope_5d_slope_v073_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_378d_slope_10d_slope_v074_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqema_504d_slope_21d_slope_v075_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_5d_slope_42d_slope_v076_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_8d_slope_63d_slope_v077_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_10d_slope_126d_slope_v078_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_15d_slope_5d_slope_v079_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_21d_slope_10d_slope_v080_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_30d_slope_21d_slope_v081_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_42d_slope_42d_slope_v082_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_63d_slope_63d_slope_v083_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_90d_slope_126d_slope_v084_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_126d_slope_5d_slope_v085_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_150d_slope_10d_slope_v086_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_189d_slope_21d_slope_v087_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_252d_slope_42d_slope_v088_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_378d_slope_63d_slope_v089_signal,
    f19iuq_f19_insurance_underwriting_quality_uwqstd_504d_slope_126d_slope_v090_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_5d_slope_5d_slope_v091_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_8d_slope_10d_slope_v092_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_10d_slope_21d_slope_v093_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_15d_slope_42d_slope_v094_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_21d_slope_63d_slope_v095_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_30d_slope_126d_slope_v096_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_42d_slope_5d_slope_v097_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_63d_slope_10d_slope_v098_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_90d_slope_21d_slope_v099_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_126d_slope_42d_slope_v100_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_150d_slope_63d_slope_v101_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_189d_slope_126d_slope_v102_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_252d_slope_5d_slope_v103_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_378d_slope_10d_slope_v104_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdur_504d_slope_21d_slope_v105_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_5d_slope_42d_slope_v106_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_8d_slope_63d_slope_v107_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_10d_slope_126d_slope_v108_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_15d_slope_5d_slope_v109_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_21d_slope_10d_slope_v110_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_30d_slope_21d_slope_v111_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_42d_slope_42d_slope_v112_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_63d_slope_63d_slope_v113_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_90d_slope_126d_slope_v114_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_126d_slope_5d_slope_v115_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_150d_slope_10d_slope_v116_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_189d_slope_21d_slope_v117_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_252d_slope_42d_slope_v118_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_378d_slope_63d_slope_v119_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurema_504d_slope_126d_slope_v120_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_5d_slope_5d_slope_v121_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_8d_slope_10d_slope_v122_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_10d_slope_21d_slope_v123_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_15d_slope_42d_slope_v124_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_21d_slope_63d_slope_v125_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_30d_slope_126d_slope_v126_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_42d_slope_5d_slope_v127_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_63d_slope_10d_slope_v128_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_90d_slope_21d_slope_v129_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_126d_slope_42d_slope_v130_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_150d_slope_63d_slope_v131_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_189d_slope_126d_slope_v132_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_252d_slope_5d_slope_v133_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_378d_slope_10d_slope_v134_signal,
    f19iuq_f19_insurance_underwriting_quality_uwdurz_504d_slope_21d_slope_v135_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_5d_slope_42d_slope_v136_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_8d_slope_63d_slope_v137_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_10d_slope_126d_slope_v138_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_15d_slope_5d_slope_v139_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_21d_slope_10d_slope_v140_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_30d_slope_21d_slope_v141_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_42d_slope_42d_slope_v142_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_63d_slope_63d_slope_v143_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_90d_slope_126d_slope_v144_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_126d_slope_5d_slope_v145_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_150d_slope_10d_slope_v146_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_189d_slope_21d_slope_v147_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_252d_slope_42d_slope_v148_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_378d_slope_63d_slope_v149_signal,
    f19iuq_f19_insurance_underwriting_quality_mfloordiff_504d_slope_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_INSURANCE_UNDERWRITING_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_insurance_underwriting_quality_slope_001_150_claude: {n_features} features pass")
