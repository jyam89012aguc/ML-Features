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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f087_ext_financing(debt, sharesbas, w):
    d_chg = debt.diff(periods=w) / debt.abs().shift(w).replace(0, np.nan)
    s_chg = sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan)
    return d_chg + s_chg


def _f087_financing_to_assets(debt, sharesbas, assets, w):
    d_chg = debt.diff(periods=w)
    s_chg = sharesbas.diff(periods=w) * 1.0
    return (d_chg + s_chg * 1e1) / assets.abs().replace(0, np.nan)


def _f087_capital_dependence(debt, equity, w):
    cap = debt + equity
    return debt / cap.replace(0, np.nan) - (debt.shift(w) / cap.shift(w).replace(0, np.nan))

def f087fdp_f087_financing_dependence_extfin_5d_jerk_v001_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_5d_jerk_v002_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_5d_jerk_v003_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_10d_jerk_v004_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_10d_jerk_v005_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_10d_jerk_v006_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_21d_jerk_v007_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_21d_jerk_v008_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_21d_jerk_v009_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_42d_jerk_v010_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_42d_jerk_v011_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_42d_jerk_v012_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_63d_jerk_v013_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_63d_jerk_v014_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_63d_jerk_v015_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_126d_jerk_v016_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_126d_jerk_v017_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_126d_jerk_v018_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_189d_jerk_v019_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_189d_jerk_v020_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_189d_jerk_v021_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_252d_jerk_v022_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_252d_jerk_v023_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_252d_jerk_v024_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_378d_jerk_v025_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_378d_jerk_v026_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_378d_jerk_v027_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_504d_jerk_v028_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_504d_jerk_v029_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_504d_jerk_v030_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_5d_jerk_v031_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_5d_jerk_v032_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_5d_jerk_v033_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_10d_jerk_v034_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_10d_jerk_v035_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_10d_jerk_v036_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_21d_jerk_v037_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_21d_jerk_v038_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_21d_jerk_v039_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_42d_jerk_v040_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_42d_jerk_v041_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_42d_jerk_v042_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_63d_jerk_v043_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_63d_jerk_v044_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_63d_jerk_v045_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_126d_jerk_v046_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_126d_jerk_v047_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_126d_jerk_v048_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_189d_jerk_v049_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_189d_jerk_v050_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_189d_jerk_v051_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_252d_jerk_v052_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_252d_jerk_v053_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_252d_jerk_v054_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_378d_jerk_v055_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_378d_jerk_v056_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_378d_jerk_v057_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_504d_jerk_v058_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_504d_jerk_v059_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_504d_jerk_v060_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_5d_jerk_v061_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_5d_jerk_v062_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_5d_jerk_v063_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_10d_jerk_v064_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_10d_jerk_v065_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_10d_jerk_v066_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_21d_jerk_v067_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_21d_jerk_v068_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_21d_jerk_v069_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_42d_jerk_v070_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_42d_jerk_v071_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_42d_jerk_v072_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_63d_jerk_v073_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_63d_jerk_v074_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_63d_jerk_v075_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_126d_jerk_v076_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_126d_jerk_v077_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_126d_jerk_v078_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_189d_jerk_v079_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_189d_jerk_v080_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_189d_jerk_v081_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_252d_jerk_v082_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_252d_jerk_v083_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_252d_jerk_v084_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_378d_jerk_v085_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_378d_jerk_v086_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_378d_jerk_v087_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfin_504d_jerk_v088_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_fta_504d_jerk_v089_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdep_504d_jerk_v090_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_5d_jerk_v091_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_5d_jerk_v092_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_5d_jerk_v093_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_10d_jerk_v094_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_10d_jerk_v095_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_10d_jerk_v096_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_21d_jerk_v097_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_21d_jerk_v098_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_21d_jerk_v099_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_42d_jerk_v100_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_42d_jerk_v101_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_42d_jerk_v102_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_63d_jerk_v103_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_63d_jerk_v104_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_63d_jerk_v105_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_126d_jerk_v106_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_126d_jerk_v107_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_126d_jerk_v108_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_189d_jerk_v109_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_189d_jerk_v110_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_189d_jerk_v111_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_252d_jerk_v112_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_252d_jerk_v113_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_252d_jerk_v114_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_378d_jerk_v115_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_378d_jerk_v116_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_378d_jerk_v117_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinsq_504d_jerk_v118_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftasq_504d_jerk_v119_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepsq_504d_jerk_v120_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_5d_jerk_v121_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_5d_jerk_v122_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_5d_jerk_v123_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_10d_jerk_v124_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_10d_jerk_v125_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_10d_jerk_v126_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_21d_jerk_v127_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_21d_jerk_v128_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_21d_jerk_v129_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_42d_jerk_v130_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_42d_jerk_v131_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_42d_jerk_v132_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_63d_jerk_v133_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_63d_jerk_v134_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_63d_jerk_v135_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_126d_jerk_v136_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_126d_jerk_v137_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_126d_jerk_v138_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_189d_jerk_v139_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_189d_jerk_v140_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_189d_jerk_v141_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_252d_jerk_v142_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_252d_jerk_v143_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_252d_jerk_v144_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_378d_jerk_v145_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_378d_jerk_v146_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_378d_jerk_v147_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_extfinab_504d_jerk_v148_signal(debt, sharesbas, closeadj):
    base = (_f087_ext_financing(debt, sharesbas, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_ftaab_504d_jerk_v149_signal(debt, sharesbas, assets, closeadj):
    base = (_f087_financing_to_assets(debt, sharesbas, assets, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f087fdp_f087_financing_dependence_capdepab_504d_jerk_v150_signal(debt, equity, closeadj):
    base = (_f087_capital_dependence(debt, equity, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f087fdp_f087_financing_dependence_extfin_5d_jerk_v001_signal,
    f087fdp_f087_financing_dependence_fta_5d_jerk_v002_signal,
    f087fdp_f087_financing_dependence_capdep_5d_jerk_v003_signal,
    f087fdp_f087_financing_dependence_extfin_10d_jerk_v004_signal,
    f087fdp_f087_financing_dependence_fta_10d_jerk_v005_signal,
    f087fdp_f087_financing_dependence_capdep_10d_jerk_v006_signal,
    f087fdp_f087_financing_dependence_extfin_21d_jerk_v007_signal,
    f087fdp_f087_financing_dependence_fta_21d_jerk_v008_signal,
    f087fdp_f087_financing_dependence_capdep_21d_jerk_v009_signal,
    f087fdp_f087_financing_dependence_extfin_42d_jerk_v010_signal,
    f087fdp_f087_financing_dependence_fta_42d_jerk_v011_signal,
    f087fdp_f087_financing_dependence_capdep_42d_jerk_v012_signal,
    f087fdp_f087_financing_dependence_extfin_63d_jerk_v013_signal,
    f087fdp_f087_financing_dependence_fta_63d_jerk_v014_signal,
    f087fdp_f087_financing_dependence_capdep_63d_jerk_v015_signal,
    f087fdp_f087_financing_dependence_extfin_126d_jerk_v016_signal,
    f087fdp_f087_financing_dependence_fta_126d_jerk_v017_signal,
    f087fdp_f087_financing_dependence_capdep_126d_jerk_v018_signal,
    f087fdp_f087_financing_dependence_extfin_189d_jerk_v019_signal,
    f087fdp_f087_financing_dependence_fta_189d_jerk_v020_signal,
    f087fdp_f087_financing_dependence_capdep_189d_jerk_v021_signal,
    f087fdp_f087_financing_dependence_extfin_252d_jerk_v022_signal,
    f087fdp_f087_financing_dependence_fta_252d_jerk_v023_signal,
    f087fdp_f087_financing_dependence_capdep_252d_jerk_v024_signal,
    f087fdp_f087_financing_dependence_extfin_378d_jerk_v025_signal,
    f087fdp_f087_financing_dependence_fta_378d_jerk_v026_signal,
    f087fdp_f087_financing_dependence_capdep_378d_jerk_v027_signal,
    f087fdp_f087_financing_dependence_extfin_504d_jerk_v028_signal,
    f087fdp_f087_financing_dependence_fta_504d_jerk_v029_signal,
    f087fdp_f087_financing_dependence_capdep_504d_jerk_v030_signal,
    f087fdp_f087_financing_dependence_extfin_5d_jerk_v031_signal,
    f087fdp_f087_financing_dependence_fta_5d_jerk_v032_signal,
    f087fdp_f087_financing_dependence_capdep_5d_jerk_v033_signal,
    f087fdp_f087_financing_dependence_extfin_10d_jerk_v034_signal,
    f087fdp_f087_financing_dependence_fta_10d_jerk_v035_signal,
    f087fdp_f087_financing_dependence_capdep_10d_jerk_v036_signal,
    f087fdp_f087_financing_dependence_extfin_21d_jerk_v037_signal,
    f087fdp_f087_financing_dependence_fta_21d_jerk_v038_signal,
    f087fdp_f087_financing_dependence_capdep_21d_jerk_v039_signal,
    f087fdp_f087_financing_dependence_extfin_42d_jerk_v040_signal,
    f087fdp_f087_financing_dependence_fta_42d_jerk_v041_signal,
    f087fdp_f087_financing_dependence_capdep_42d_jerk_v042_signal,
    f087fdp_f087_financing_dependence_extfin_63d_jerk_v043_signal,
    f087fdp_f087_financing_dependence_fta_63d_jerk_v044_signal,
    f087fdp_f087_financing_dependence_capdep_63d_jerk_v045_signal,
    f087fdp_f087_financing_dependence_extfin_126d_jerk_v046_signal,
    f087fdp_f087_financing_dependence_fta_126d_jerk_v047_signal,
    f087fdp_f087_financing_dependence_capdep_126d_jerk_v048_signal,
    f087fdp_f087_financing_dependence_extfin_189d_jerk_v049_signal,
    f087fdp_f087_financing_dependence_fta_189d_jerk_v050_signal,
    f087fdp_f087_financing_dependence_capdep_189d_jerk_v051_signal,
    f087fdp_f087_financing_dependence_extfin_252d_jerk_v052_signal,
    f087fdp_f087_financing_dependence_fta_252d_jerk_v053_signal,
    f087fdp_f087_financing_dependence_capdep_252d_jerk_v054_signal,
    f087fdp_f087_financing_dependence_extfin_378d_jerk_v055_signal,
    f087fdp_f087_financing_dependence_fta_378d_jerk_v056_signal,
    f087fdp_f087_financing_dependence_capdep_378d_jerk_v057_signal,
    f087fdp_f087_financing_dependence_extfin_504d_jerk_v058_signal,
    f087fdp_f087_financing_dependence_fta_504d_jerk_v059_signal,
    f087fdp_f087_financing_dependence_capdep_504d_jerk_v060_signal,
    f087fdp_f087_financing_dependence_extfin_5d_jerk_v061_signal,
    f087fdp_f087_financing_dependence_fta_5d_jerk_v062_signal,
    f087fdp_f087_financing_dependence_capdep_5d_jerk_v063_signal,
    f087fdp_f087_financing_dependence_extfin_10d_jerk_v064_signal,
    f087fdp_f087_financing_dependence_fta_10d_jerk_v065_signal,
    f087fdp_f087_financing_dependence_capdep_10d_jerk_v066_signal,
    f087fdp_f087_financing_dependence_extfin_21d_jerk_v067_signal,
    f087fdp_f087_financing_dependence_fta_21d_jerk_v068_signal,
    f087fdp_f087_financing_dependence_capdep_21d_jerk_v069_signal,
    f087fdp_f087_financing_dependence_extfin_42d_jerk_v070_signal,
    f087fdp_f087_financing_dependence_fta_42d_jerk_v071_signal,
    f087fdp_f087_financing_dependence_capdep_42d_jerk_v072_signal,
    f087fdp_f087_financing_dependence_extfin_63d_jerk_v073_signal,
    f087fdp_f087_financing_dependence_fta_63d_jerk_v074_signal,
    f087fdp_f087_financing_dependence_capdep_63d_jerk_v075_signal,
    f087fdp_f087_financing_dependence_extfin_126d_jerk_v076_signal,
    f087fdp_f087_financing_dependence_fta_126d_jerk_v077_signal,
    f087fdp_f087_financing_dependence_capdep_126d_jerk_v078_signal,
    f087fdp_f087_financing_dependence_extfin_189d_jerk_v079_signal,
    f087fdp_f087_financing_dependence_fta_189d_jerk_v080_signal,
    f087fdp_f087_financing_dependence_capdep_189d_jerk_v081_signal,
    f087fdp_f087_financing_dependence_extfin_252d_jerk_v082_signal,
    f087fdp_f087_financing_dependence_fta_252d_jerk_v083_signal,
    f087fdp_f087_financing_dependence_capdep_252d_jerk_v084_signal,
    f087fdp_f087_financing_dependence_extfin_378d_jerk_v085_signal,
    f087fdp_f087_financing_dependence_fta_378d_jerk_v086_signal,
    f087fdp_f087_financing_dependence_capdep_378d_jerk_v087_signal,
    f087fdp_f087_financing_dependence_extfin_504d_jerk_v088_signal,
    f087fdp_f087_financing_dependence_fta_504d_jerk_v089_signal,
    f087fdp_f087_financing_dependence_capdep_504d_jerk_v090_signal,
    f087fdp_f087_financing_dependence_extfinsq_5d_jerk_v091_signal,
    f087fdp_f087_financing_dependence_ftasq_5d_jerk_v092_signal,
    f087fdp_f087_financing_dependence_capdepsq_5d_jerk_v093_signal,
    f087fdp_f087_financing_dependence_extfinsq_10d_jerk_v094_signal,
    f087fdp_f087_financing_dependence_ftasq_10d_jerk_v095_signal,
    f087fdp_f087_financing_dependence_capdepsq_10d_jerk_v096_signal,
    f087fdp_f087_financing_dependence_extfinsq_21d_jerk_v097_signal,
    f087fdp_f087_financing_dependence_ftasq_21d_jerk_v098_signal,
    f087fdp_f087_financing_dependence_capdepsq_21d_jerk_v099_signal,
    f087fdp_f087_financing_dependence_extfinsq_42d_jerk_v100_signal,
    f087fdp_f087_financing_dependence_ftasq_42d_jerk_v101_signal,
    f087fdp_f087_financing_dependence_capdepsq_42d_jerk_v102_signal,
    f087fdp_f087_financing_dependence_extfinsq_63d_jerk_v103_signal,
    f087fdp_f087_financing_dependence_ftasq_63d_jerk_v104_signal,
    f087fdp_f087_financing_dependence_capdepsq_63d_jerk_v105_signal,
    f087fdp_f087_financing_dependence_extfinsq_126d_jerk_v106_signal,
    f087fdp_f087_financing_dependence_ftasq_126d_jerk_v107_signal,
    f087fdp_f087_financing_dependence_capdepsq_126d_jerk_v108_signal,
    f087fdp_f087_financing_dependence_extfinsq_189d_jerk_v109_signal,
    f087fdp_f087_financing_dependence_ftasq_189d_jerk_v110_signal,
    f087fdp_f087_financing_dependence_capdepsq_189d_jerk_v111_signal,
    f087fdp_f087_financing_dependence_extfinsq_252d_jerk_v112_signal,
    f087fdp_f087_financing_dependence_ftasq_252d_jerk_v113_signal,
    f087fdp_f087_financing_dependence_capdepsq_252d_jerk_v114_signal,
    f087fdp_f087_financing_dependence_extfinsq_378d_jerk_v115_signal,
    f087fdp_f087_financing_dependence_ftasq_378d_jerk_v116_signal,
    f087fdp_f087_financing_dependence_capdepsq_378d_jerk_v117_signal,
    f087fdp_f087_financing_dependence_extfinsq_504d_jerk_v118_signal,
    f087fdp_f087_financing_dependence_ftasq_504d_jerk_v119_signal,
    f087fdp_f087_financing_dependence_capdepsq_504d_jerk_v120_signal,
    f087fdp_f087_financing_dependence_extfinab_5d_jerk_v121_signal,
    f087fdp_f087_financing_dependence_ftaab_5d_jerk_v122_signal,
    f087fdp_f087_financing_dependence_capdepab_5d_jerk_v123_signal,
    f087fdp_f087_financing_dependence_extfinab_10d_jerk_v124_signal,
    f087fdp_f087_financing_dependence_ftaab_10d_jerk_v125_signal,
    f087fdp_f087_financing_dependence_capdepab_10d_jerk_v126_signal,
    f087fdp_f087_financing_dependence_extfinab_21d_jerk_v127_signal,
    f087fdp_f087_financing_dependence_ftaab_21d_jerk_v128_signal,
    f087fdp_f087_financing_dependence_capdepab_21d_jerk_v129_signal,
    f087fdp_f087_financing_dependence_extfinab_42d_jerk_v130_signal,
    f087fdp_f087_financing_dependence_ftaab_42d_jerk_v131_signal,
    f087fdp_f087_financing_dependence_capdepab_42d_jerk_v132_signal,
    f087fdp_f087_financing_dependence_extfinab_63d_jerk_v133_signal,
    f087fdp_f087_financing_dependence_ftaab_63d_jerk_v134_signal,
    f087fdp_f087_financing_dependence_capdepab_63d_jerk_v135_signal,
    f087fdp_f087_financing_dependence_extfinab_126d_jerk_v136_signal,
    f087fdp_f087_financing_dependence_ftaab_126d_jerk_v137_signal,
    f087fdp_f087_financing_dependence_capdepab_126d_jerk_v138_signal,
    f087fdp_f087_financing_dependence_extfinab_189d_jerk_v139_signal,
    f087fdp_f087_financing_dependence_ftaab_189d_jerk_v140_signal,
    f087fdp_f087_financing_dependence_capdepab_189d_jerk_v141_signal,
    f087fdp_f087_financing_dependence_extfinab_252d_jerk_v142_signal,
    f087fdp_f087_financing_dependence_ftaab_252d_jerk_v143_signal,
    f087fdp_f087_financing_dependence_capdepab_252d_jerk_v144_signal,
    f087fdp_f087_financing_dependence_extfinab_378d_jerk_v145_signal,
    f087fdp_f087_financing_dependence_ftaab_378d_jerk_v146_signal,
    f087fdp_f087_financing_dependence_capdepab_378d_jerk_v147_signal,
    f087fdp_f087_financing_dependence_extfinab_504d_jerk_v148_signal,
    f087fdp_f087_financing_dependence_ftaab_504d_jerk_v149_signal,
    f087fdp_f087_financing_dependence_capdepab_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F087_FINANCING_DEPENDENCE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")

    cols = {"debt": debt, "sharesbas": sharesbas, "closeadj": closeadj, "assets": assets, "equity": equity}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f087_ext_financing", "_f087_financing_to_assets", "_f087_capital_dependence",)
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
    print(f"OK f087_financing_dependence_3rd_derivatives_001_150_claude: {n_features} features pass")
