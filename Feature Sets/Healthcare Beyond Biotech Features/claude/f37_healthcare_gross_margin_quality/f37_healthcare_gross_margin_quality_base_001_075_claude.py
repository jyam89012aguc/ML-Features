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

def _f37_gm_floor(grossmargin, w):
    floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    return (grossmargin - floor)


def _f37_gm_consistency(grossmargin, w):
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    m = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return 1.0 / (sd / m.replace(0, np.nan)).replace(0, np.nan)


def _f37_gm_quality_score(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm * em) / sd.replace(0, np.nan)




def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_5d_base_v001_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_10d_base_v002_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_21d_base_v003_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_42d_base_v004_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_63d_base_v005_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_126d_base_v006_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_189d_base_v007_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_252d_base_v008_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_378d_base_v009_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_504d_base_v010_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_5d_base_v011_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_10d_base_v012_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_21d_base_v013_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_42d_base_v014_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_63d_base_v015_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_126d_base_v016_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_189d_base_v017_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_252d_base_v018_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_378d_base_v019_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_504d_base_v020_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_5d_base_v021_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_10d_base_v022_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_21d_base_v023_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_42d_base_v024_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_63d_base_v025_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_126d_base_v026_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_189d_base_v027_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_252d_base_v028_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_378d_base_v029_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_504d_base_v030_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_5d_base_v031_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_10d_base_v032_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_21d_base_v033_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_42d_base_v034_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_63d_base_v035_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_126d_base_v036_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_189d_base_v037_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_252d_base_v038_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_378d_base_v039_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_504d_base_v040_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_5d_base_v041_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_10d_base_v042_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_21d_base_v043_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_42d_base_v044_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_63d_base_v045_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_126d_base_v046_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_189d_base_v047_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_252d_base_v048_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_378d_base_v049_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_504d_base_v050_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_5d_base_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_10d_base_v052_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_21d_base_v053_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_42d_base_v054_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_63d_base_v055_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_126d_base_v056_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_189d_base_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_252d_base_v058_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_378d_base_v059_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_504d_base_v060_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_5d_base_v061_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_10d_base_v062_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_21d_base_v063_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_42d_base_v064_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_63d_base_v065_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_126d_base_v066_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_189d_base_v067_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_252d_base_v068_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_378d_base_v069_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_504d_base_v070_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_5d_base_v071_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_10d_base_v072_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_21d_base_v073_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_42d_base_v074_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_63d_base_v075_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_5d_base_v001_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_10d_base_v002_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_21d_base_v003_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_42d_base_v004_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_63d_base_v005_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_126d_base_v006_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_189d_base_v007_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_252d_base_v008_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_378d_base_v009_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclose_504d_base_v010_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_5d_base_v011_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_10d_base_v012_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_21d_base_v013_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_42d_base_v014_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_63d_base_v015_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_126d_base_v016_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_189d_base_v017_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_252d_base_v018_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_378d_base_v019_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclose_504d_base_v020_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_5d_base_v021_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_10d_base_v022_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_21d_base_v023_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_42d_base_v024_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_63d_base_v025_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_126d_base_v026_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_189d_base_v027_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_252d_base_v028_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_378d_base_v029_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclose_504d_base_v030_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_5d_base_v031_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_10d_base_v032_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_21d_base_v033_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_42d_base_v034_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_63d_base_v035_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_126d_base_v036_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_189d_base_v037_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_252d_base_v038_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_378d_base_v039_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmulclosesq_504d_base_v040_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_5d_base_v041_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_10d_base_v042_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_21d_base_v043_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_42d_base_v044_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_63d_base_v045_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_126d_base_v046_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_189d_base_v047_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_252d_base_v048_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_378d_base_v049_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsmulclosesq_504d_base_v050_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_5d_base_v051_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_10d_base_v052_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_21d_base_v053_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_42d_base_v054_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_63d_base_v055_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_126d_base_v056_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_189d_base_v057_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_252d_base_v058_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_378d_base_v059_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscmulclosesq_504d_base_v060_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_5d_base_v061_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_10d_base_v062_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_21d_base_v063_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_42d_base_v064_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_63d_base_v065_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_126d_base_v066_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_189d_base_v067_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_252d_base_v068_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_378d_base_v069_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrdivclose_504d_base_v070_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_5d_base_v071_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_10d_base_v072_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_21d_base_v073_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_42d_base_v074_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F37_HEALTHCARE_GROSS_MARGIN_QUALITY_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f37_gm_floor", "_f37_gm_consistency", "_f37_gm_quality_score")
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
    print(f"OK f37_healthcare_gross_margin_quality_base_001_075_claude: {n_features} features pass")
