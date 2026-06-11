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

def _f40_margin_expansion(grossmargin, w):
    return grossmargin.diff(periods=w)


def _f40_margin_compound(ebitdamargin, w):
    avg = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return avg.diff(periods=w) * avg


def _f40_expansion_quality(grossmargin, ebitdamargin, w):
    dg = grossmargin.diff(periods=w)
    de = ebitdamargin.diff(periods=w)
    return dg * de




def f40hme_f40_healthcare_margin_expansion_expmulclose_5d_base_v001_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_10d_base_v002_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_21d_base_v003_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_42d_base_v004_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_63d_base_v005_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_126d_base_v006_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_189d_base_v007_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_252d_base_v008_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_378d_base_v009_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclose_504d_base_v010_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_5d_base_v011_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_10d_base_v012_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_21d_base_v013_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_42d_base_v014_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_63d_base_v015_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_126d_base_v016_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_189d_base_v017_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_252d_base_v018_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_378d_base_v019_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclose_504d_base_v020_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_5d_base_v021_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_10d_base_v022_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_21d_base_v023_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_42d_base_v024_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_63d_base_v025_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_126d_base_v026_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_189d_base_v027_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_252d_base_v028_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_378d_base_v029_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclose_504d_base_v030_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_5d_base_v031_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_10d_base_v032_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_21d_base_v033_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_42d_base_v034_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_63d_base_v035_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_126d_base_v036_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_189d_base_v037_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_252d_base_v038_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_378d_base_v039_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmulclosesq_504d_base_v040_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_5d_base_v041_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_10d_base_v042_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_21d_base_v043_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_42d_base_v044_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_63d_base_v045_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_126d_base_v046_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_189d_base_v047_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_252d_base_v048_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_378d_base_v049_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_504d_base_v050_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_5d_base_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_10d_base_v052_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_21d_base_v053_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_42d_base_v054_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_63d_base_v055_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_126d_base_v056_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_189d_base_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_252d_base_v058_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_378d_base_v059_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_quamulclosesq_504d_base_v060_signal(grossmargin, ebitdamargin, closeadj):
    base = _f40_expansion_quality(grossmargin, ebitdamargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_5d_base_v061_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_10d_base_v062_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_21d_base_v063_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_42d_base_v064_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_63d_base_v065_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_126d_base_v066_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_189d_base_v067_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_252d_base_v068_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_378d_base_v069_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expdivclose_504d_base_v070_signal(grossmargin, closeadj):
    base = _f40_margin_expansion(grossmargin, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpdivclose_5d_base_v071_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpdivclose_10d_base_v072_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpdivclose_21d_base_v073_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpdivclose_42d_base_v074_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_cmpdivclose_63d_base_v075_signal(ebitdamargin, closeadj):
    base = _f40_margin_compound(ebitdamargin, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40hme_f40_healthcare_margin_expansion_expmulclose_5d_base_v001_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_10d_base_v002_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_21d_base_v003_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_42d_base_v004_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_63d_base_v005_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_126d_base_v006_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_189d_base_v007_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_252d_base_v008_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_378d_base_v009_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclose_504d_base_v010_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_5d_base_v011_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_10d_base_v012_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_21d_base_v013_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_42d_base_v014_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_63d_base_v015_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_126d_base_v016_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_189d_base_v017_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_252d_base_v018_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_378d_base_v019_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclose_504d_base_v020_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_5d_base_v021_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_10d_base_v022_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_21d_base_v023_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_42d_base_v024_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_63d_base_v025_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_126d_base_v026_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_189d_base_v027_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_252d_base_v028_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_378d_base_v029_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclose_504d_base_v030_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_5d_base_v031_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_10d_base_v032_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_21d_base_v033_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_42d_base_v034_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_63d_base_v035_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_126d_base_v036_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_189d_base_v037_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_252d_base_v038_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_378d_base_v039_signal,
    f40hme_f40_healthcare_margin_expansion_expmulclosesq_504d_base_v040_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_5d_base_v041_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_10d_base_v042_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_21d_base_v043_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_42d_base_v044_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_63d_base_v045_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_126d_base_v046_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_189d_base_v047_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_252d_base_v048_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_378d_base_v049_signal,
    f40hme_f40_healthcare_margin_expansion_cmpmulclosesq_504d_base_v050_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_5d_base_v051_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_10d_base_v052_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_21d_base_v053_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_42d_base_v054_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_63d_base_v055_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_126d_base_v056_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_189d_base_v057_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_252d_base_v058_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_378d_base_v059_signal,
    f40hme_f40_healthcare_margin_expansion_quamulclosesq_504d_base_v060_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_5d_base_v061_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_10d_base_v062_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_21d_base_v063_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_42d_base_v064_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_63d_base_v065_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_126d_base_v066_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_189d_base_v067_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_252d_base_v068_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_378d_base_v069_signal,
    f40hme_f40_healthcare_margin_expansion_expdivclose_504d_base_v070_signal,
    f40hme_f40_healthcare_margin_expansion_cmpdivclose_5d_base_v071_signal,
    f40hme_f40_healthcare_margin_expansion_cmpdivclose_10d_base_v072_signal,
    f40hme_f40_healthcare_margin_expansion_cmpdivclose_21d_base_v073_signal,
    f40hme_f40_healthcare_margin_expansion_cmpdivclose_42d_base_v074_signal,
    f40hme_f40_healthcare_margin_expansion_cmpdivclose_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F40_HEALTHCARE_MARGIN_EXPANSION_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f40_margin_expansion", "_f40_margin_compound", "_f40_expansion_quality")
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
    print(f"OK f40_healthcare_margin_expansion_base_001_075_claude: {n_features} features pass")
