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

def _f36_op_leverage_proxy(ebit, revenue, w):
    em = (ebit / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()
    eb = ebit.rolling(w, min_periods=max(1, w // 2)).mean()
    rv = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return em * eb / rv.replace(0, np.nan)


def _f36_margin_revenue_beta(ebitdamargin, revenue, w):
    dm = ebitdamargin.diff(periods=w)
    dr = revenue.pct_change(periods=w)
    return dm / dr.replace(0, np.nan)


def _f36_drop_through(ebit, revenue, w):
    deb = ebit.diff(periods=w)
    drv = revenue.diff(periods=w)
    return deb / drv.replace(0, np.nan)




def f36hol_f36_healthcare_operating_leverage_oplmulclose_5d_base_v001_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_10d_base_v002_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_21d_base_v003_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_42d_base_v004_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_63d_base_v005_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_126d_base_v006_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_189d_base_v007_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_252d_base_v008_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_378d_base_v009_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclose_504d_base_v010_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_5d_base_v011_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_10d_base_v012_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_21d_base_v013_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_42d_base_v014_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_63d_base_v015_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_126d_base_v016_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_189d_base_v017_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_252d_base_v018_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_378d_base_v019_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclose_504d_base_v020_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_5d_base_v021_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_10d_base_v022_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_21d_base_v023_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_42d_base_v024_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_63d_base_v025_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_126d_base_v026_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_189d_base_v027_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_252d_base_v028_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_378d_base_v029_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclose_504d_base_v030_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_5d_base_v031_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_10d_base_v032_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_21d_base_v033_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_42d_base_v034_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_63d_base_v035_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_126d_base_v036_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_189d_base_v037_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_252d_base_v038_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_378d_base_v039_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmulclosesq_504d_base_v040_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_5d_base_v041_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_10d_base_v042_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_21d_base_v043_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_42d_base_v044_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_63d_base_v045_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_126d_base_v046_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_189d_base_v047_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_252d_base_v048_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_378d_base_v049_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_504d_base_v050_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_5d_base_v051_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_10d_base_v052_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_21d_base_v053_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_42d_base_v054_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_63d_base_v055_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_126d_base_v056_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_189d_base_v057_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_252d_base_v058_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_378d_base_v059_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_drpmulclosesq_504d_base_v060_signal(ebit, revenue, closeadj):
    base = _f36_drop_through(ebit, revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_5d_base_v061_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_10d_base_v062_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_21d_base_v063_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_42d_base_v064_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_63d_base_v065_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_126d_base_v066_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_189d_base_v067_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_252d_base_v068_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_378d_base_v069_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_opldivclose_504d_base_v070_signal(ebit, revenue, closeadj):
    base = _f36_op_leverage_proxy(ebit, revenue, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_5d_base_v071_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_10d_base_v072_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_21d_base_v073_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_42d_base_v074_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_mrbdivclose_63d_base_v075_signal(ebitdamargin, revenue, closeadj):
    base = _f36_margin_revenue_beta(ebitdamargin, revenue, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36hol_f36_healthcare_operating_leverage_oplmulclose_5d_base_v001_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_10d_base_v002_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_21d_base_v003_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_42d_base_v004_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_63d_base_v005_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_126d_base_v006_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_189d_base_v007_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_252d_base_v008_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_378d_base_v009_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclose_504d_base_v010_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_5d_base_v011_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_10d_base_v012_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_21d_base_v013_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_42d_base_v014_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_63d_base_v015_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_126d_base_v016_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_189d_base_v017_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_252d_base_v018_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_378d_base_v019_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclose_504d_base_v020_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_5d_base_v021_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_10d_base_v022_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_21d_base_v023_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_42d_base_v024_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_63d_base_v025_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_126d_base_v026_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_189d_base_v027_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_252d_base_v028_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_378d_base_v029_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclose_504d_base_v030_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_5d_base_v031_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_10d_base_v032_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_21d_base_v033_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_42d_base_v034_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_63d_base_v035_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_126d_base_v036_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_189d_base_v037_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_252d_base_v038_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_378d_base_v039_signal,
    f36hol_f36_healthcare_operating_leverage_oplmulclosesq_504d_base_v040_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_5d_base_v041_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_10d_base_v042_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_21d_base_v043_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_42d_base_v044_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_63d_base_v045_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_126d_base_v046_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_189d_base_v047_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_252d_base_v048_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_378d_base_v049_signal,
    f36hol_f36_healthcare_operating_leverage_mrbmulclosesq_504d_base_v050_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_5d_base_v051_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_10d_base_v052_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_21d_base_v053_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_42d_base_v054_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_63d_base_v055_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_126d_base_v056_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_189d_base_v057_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_252d_base_v058_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_378d_base_v059_signal,
    f36hol_f36_healthcare_operating_leverage_drpmulclosesq_504d_base_v060_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_5d_base_v061_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_10d_base_v062_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_21d_base_v063_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_42d_base_v064_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_63d_base_v065_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_126d_base_v066_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_189d_base_v067_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_252d_base_v068_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_378d_base_v069_signal,
    f36hol_f36_healthcare_operating_leverage_opldivclose_504d_base_v070_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_5d_base_v071_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_10d_base_v072_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_21d_base_v073_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_42d_base_v074_signal,
    f36hol_f36_healthcare_operating_leverage_mrbdivclose_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F36_HEALTHCARE_OPERATING_LEVERAGE_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f36_op_leverage_proxy", "_f36_margin_revenue_beta", "_f36_drop_through")
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
    print(f"OK f36_healthcare_operating_leverage_base_001_075_claude: {n_features} features pass")
