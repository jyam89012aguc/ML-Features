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

def _f39_rd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f39_rd_growth_gap(rnd, revenue, w):
    drd = rnd.pct_change(periods=w)
    drv = revenue.pct_change(periods=w)
    return drv - drd


def _f39_rd_productivity(rnd, revenue, w):
    drv = revenue.diff(periods=w)
    rnd_avg = rnd.rolling(w, min_periods=max(1, w // 2)).mean()
    return drv / rnd_avg.replace(0, np.nan)




def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_5d_base_v001_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_10d_base_v002_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_21d_base_v003_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_42d_base_v004_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_63d_base_v005_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_126d_base_v006_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_189d_base_v007_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_252d_base_v008_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_378d_base_v009_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclose_504d_base_v010_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_5d_base_v011_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_10d_base_v012_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_21d_base_v013_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_42d_base_v014_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_63d_base_v015_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_126d_base_v016_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_189d_base_v017_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_252d_base_v018_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_378d_base_v019_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclose_504d_base_v020_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_5d_base_v021_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_10d_base_v022_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_21d_base_v023_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_42d_base_v024_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_63d_base_v025_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_126d_base_v026_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_189d_base_v027_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_252d_base_v028_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_378d_base_v029_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_504d_base_v030_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_5d_base_v031_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_10d_base_v032_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_21d_base_v033_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_42d_base_v034_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_63d_base_v035_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_126d_base_v036_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_189d_base_v037_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_252d_base_v038_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_378d_base_v039_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_504d_base_v040_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_5d_base_v041_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_10d_base_v042_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_21d_base_v043_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_42d_base_v044_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_63d_base_v045_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_126d_base_v046_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_189d_base_v047_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_252d_base_v048_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_378d_base_v049_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapdivclose_504d_base_v050_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_5d_base_v051_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_10d_base_v052_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_21d_base_v053_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_42d_base_v054_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_63d_base_v055_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_126d_base_v056_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_189d_base_v057_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_252d_base_v058_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_378d_base_v059_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_prddivclose_504d_base_v060_signal(rnd, revenue, closeadj):
    base = _f39_rd_productivity(rnd, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d5d_base_v061_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d10d_base_v062_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d21d_base_v063_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d42d_base_v064_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d63d_base_v065_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d126d_base_v066_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d189d_base_v067_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d252d_base_v068_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d378d_base_v069_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d504d_base_v070_signal(rnd, revenue, closeadj):
    base = _f39_rd_intensity(rnd, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d5d_base_v071_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d10d_base_v072_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d21d_base_v073_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d42d_base_v074_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d63d_base_v075_signal(rnd, revenue, closeadj):
    base = _f39_rd_growth_gap(rnd, revenue, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_5d_base_v001_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_10d_base_v002_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_21d_base_v003_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_42d_base_v004_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_63d_base_v005_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_126d_base_v006_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_189d_base_v007_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_252d_base_v008_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_378d_base_v009_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclose_504d_base_v010_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_5d_base_v011_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_10d_base_v012_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_21d_base_v013_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_42d_base_v014_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_63d_base_v015_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_126d_base_v016_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_189d_base_v017_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_252d_base_v018_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_378d_base_v019_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclose_504d_base_v020_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_5d_base_v021_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_10d_base_v022_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_21d_base_v023_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_42d_base_v024_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_63d_base_v025_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_126d_base_v026_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_189d_base_v027_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_252d_base_v028_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_378d_base_v029_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmulclosesq_504d_base_v030_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_5d_base_v031_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_10d_base_v032_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_21d_base_v033_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_42d_base_v034_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_63d_base_v035_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_126d_base_v036_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_189d_base_v037_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_252d_base_v038_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_378d_base_v039_signal,
    f39hrg_f39_healthcare_rd_to_growth_prdmulclosesq_504d_base_v040_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_5d_base_v041_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_10d_base_v042_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_21d_base_v043_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_42d_base_v044_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_63d_base_v045_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_126d_base_v046_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_189d_base_v047_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_252d_base_v048_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_378d_base_v049_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapdivclose_504d_base_v050_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_5d_base_v051_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_10d_base_v052_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_21d_base_v053_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_42d_base_v054_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_63d_base_v055_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_126d_base_v056_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_189d_base_v057_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_252d_base_v058_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_378d_base_v059_signal,
    f39hrg_f39_healthcare_rd_to_growth_prddivclose_504d_base_v060_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d5d_base_v061_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d10d_base_v062_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d21d_base_v063_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d42d_base_v064_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d63d_base_v065_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d126d_base_v066_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d189d_base_v067_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d252d_base_v068_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d378d_base_v069_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanmulclose_5d504d_base_v070_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d5d_base_v071_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d10d_base_v072_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d21d_base_v073_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d42d_base_v074_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanmulclose_5d63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F39_HEALTHCARE_RD_TO_GROWTH_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f39_rd_intensity", "_f39_rd_growth_gap", "_f39_rd_productivity")
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
    print(f"OK f39_healthcare_rd_to_growth_base_001_075_claude: {n_features} features pass")
