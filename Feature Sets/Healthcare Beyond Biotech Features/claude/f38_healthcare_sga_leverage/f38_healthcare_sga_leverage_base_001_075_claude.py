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



# ===== folder domain primitives =====

def _f38_sga_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f38_sga_revenue_gap(sgna, revenue, w):
    ds = sgna.pct_change(periods=w)
    dr = revenue.pct_change(periods=w)
    return dr - ds


def _f38_sga_leverage(sgna, revenue, w):
    intensity = sgna / revenue.replace(0, np.nan)
    return -intensity.diff(periods=w)




def f38hsl_f38_healthcare_sga_leverage_gapmulclose_5d_base_v001_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_10d_base_v002_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_21d_base_v003_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_42d_base_v004_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_63d_base_v005_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_126d_base_v006_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_189d_base_v007_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_252d_base_v008_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_378d_base_v009_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclose_504d_base_v010_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_5d_base_v011_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_10d_base_v012_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_21d_base_v013_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_42d_base_v014_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_63d_base_v015_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_126d_base_v016_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_189d_base_v017_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_252d_base_v018_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_378d_base_v019_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclose_504d_base_v020_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_5d_base_v021_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_10d_base_v022_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_21d_base_v023_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_42d_base_v024_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_63d_base_v025_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_126d_base_v026_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_189d_base_v027_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_252d_base_v028_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_378d_base_v029_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_504d_base_v030_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_5d_base_v031_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_10d_base_v032_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_21d_base_v033_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_42d_base_v034_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_63d_base_v035_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_126d_base_v036_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_189d_base_v037_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_252d_base_v038_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_378d_base_v039_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levmulclosesq_504d_base_v040_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_5d_base_v041_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_10d_base_v042_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_21d_base_v043_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_42d_base_v044_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_63d_base_v045_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_126d_base_v046_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_189d_base_v047_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_252d_base_v048_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_378d_base_v049_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapdivclose_504d_base_v050_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_5d_base_v051_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_10d_base_v052_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_21d_base_v053_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_42d_base_v054_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_63d_base_v055_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_126d_base_v056_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_189d_base_v057_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_252d_base_v058_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_378d_base_v059_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_levdivclose_504d_base_v060_signal(sgna, revenue, closeadj):
    base = _f38_sga_leverage(sgna, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d5d_base_v061_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d10d_base_v062_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d21d_base_v063_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d42d_base_v064_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d63d_base_v065_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d126d_base_v066_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d189d_base_v067_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d252d_base_v068_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d378d_base_v069_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d504d_base_v070_signal(sgna, revenue, closeadj):
    base = _f38_sga_intensity(sgna, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d5d_base_v071_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d10d_base_v072_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d21d_base_v073_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d42d_base_v074_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d63d_base_v075_signal(sgna, revenue, closeadj):
    base = _f38_sga_revenue_gap(sgna, revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_5d_base_v001_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_10d_base_v002_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_21d_base_v003_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_42d_base_v004_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_63d_base_v005_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_126d_base_v006_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_189d_base_v007_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_252d_base_v008_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_378d_base_v009_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclose_504d_base_v010_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_5d_base_v011_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_10d_base_v012_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_21d_base_v013_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_42d_base_v014_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_63d_base_v015_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_126d_base_v016_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_189d_base_v017_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_252d_base_v018_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_378d_base_v019_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclose_504d_base_v020_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_5d_base_v021_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_10d_base_v022_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_21d_base_v023_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_42d_base_v024_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_63d_base_v025_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_126d_base_v026_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_189d_base_v027_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_252d_base_v028_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_378d_base_v029_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmulclosesq_504d_base_v030_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_5d_base_v031_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_10d_base_v032_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_21d_base_v033_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_42d_base_v034_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_63d_base_v035_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_126d_base_v036_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_189d_base_v037_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_252d_base_v038_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_378d_base_v039_signal,
    f38hsl_f38_healthcare_sga_leverage_levmulclosesq_504d_base_v040_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_5d_base_v041_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_10d_base_v042_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_21d_base_v043_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_42d_base_v044_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_63d_base_v045_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_126d_base_v046_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_189d_base_v047_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_252d_base_v048_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_378d_base_v049_signal,
    f38hsl_f38_healthcare_sga_leverage_gapdivclose_504d_base_v050_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_5d_base_v051_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_10d_base_v052_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_21d_base_v053_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_42d_base_v054_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_63d_base_v055_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_126d_base_v056_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_189d_base_v057_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_252d_base_v058_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_378d_base_v059_signal,
    f38hsl_f38_healthcare_sga_leverage_levdivclose_504d_base_v060_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d5d_base_v061_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d10d_base_v062_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d21d_base_v063_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d42d_base_v064_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d63d_base_v065_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d126d_base_v066_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d189d_base_v067_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d252d_base_v068_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d378d_base_v069_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanmulclose_5d504d_base_v070_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d5d_base_v071_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d10d_base_v072_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d21d_base_v073_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d42d_base_v074_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanmulclose_5d63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F38_HEALTHCARE_SGA_LEVERAGE_REGISTRY_001_075 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "sgna": sgna, "opex": opex, "rnd": rnd,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f38_sga_intensity", "_f38_sga_revenue_gap", "_f38_sga_leverage")
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
    print(f"OK f38_healthcare_sga_leverage_base_001_075_claude: {n_features} features pass")
