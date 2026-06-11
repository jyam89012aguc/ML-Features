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


# v001 21d external financing × close
def f087fdp_f087_financing_dependence_extfin_21d_base_v001_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002 63d external financing × close
def f087fdp_f087_financing_dependence_extfin_63d_base_v002_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003 126d ext financing × close
def f087fdp_f087_financing_dependence_extfin_126d_base_v003_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004 252d ext financing × close
def f087fdp_f087_financing_dependence_extfin_252d_base_v004_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005 504d ext financing × close
def f087fdp_f087_financing_dependence_extfin_504d_base_v005_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006 21d financing-to-assets × close
def f087fdp_f087_financing_dependence_fta_21d_base_v006_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007 63d fta × close
def f087fdp_f087_financing_dependence_fta_63d_base_v007_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008 126d fta × close
def f087fdp_f087_financing_dependence_fta_126d_base_v008_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009 252d fta × close
def f087fdp_f087_financing_dependence_fta_252d_base_v009_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010 504d fta × close
def f087fdp_f087_financing_dependence_fta_504d_base_v010_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011 21d capital dependence × close
def f087fdp_f087_financing_dependence_capdep_21d_base_v011_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012 63d capdep × close
def f087fdp_f087_financing_dependence_capdep_63d_base_v012_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013 126d capdep × close
def f087fdp_f087_financing_dependence_capdep_126d_base_v013_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014 252d capdep × close
def f087fdp_f087_financing_dependence_capdep_252d_base_v014_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015 504d capdep × close
def f087fdp_f087_financing_dependence_capdep_504d_base_v015_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016 21d ext financing zscore × close
def f087fdp_f087_financing_dependence_extfinz_21d_base_v016_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017 63d ext financing zscore × close
def f087fdp_f087_financing_dependence_extfinz_63d_base_v017_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018 252d ext financing zscore × close
def f087fdp_f087_financing_dependence_extfinz_252d_base_v018_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019 21d ext financing EMA × close
def f087fdp_f087_financing_dependence_extfinema_21d_base_v019_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020 63d ext financing EMA × close
def f087fdp_f087_financing_dependence_extfinema_63d_base_v020_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base.ewm(span=63, min_periods=30).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021 252d ext financing EMA × close
def f087fdp_f087_financing_dependence_extfinema_252d_base_v021_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base.ewm(span=126, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022 21d ext financing std × close
def f087fdp_f087_financing_dependence_extfinstd_21d_base_v022_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023 63d ext financing std × close
def f087fdp_f087_financing_dependence_extfinstd_63d_base_v023_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024 252d ext financing std × close
def f087fdp_f087_financing_dependence_extfinstd_252d_base_v024_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025 21d ext financing × log close
def f087fdp_f087_financing_dependence_extfinxlog_21d_base_v025_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v026 63d ext financing × log close
def f087fdp_f087_financing_dependence_extfinxlog_63d_base_v026_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v027 252d ext financing × log close
def f087fdp_f087_financing_dependence_extfinxlog_252d_base_v027_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v028 21d sign × sqrt × close ext financing
def f087fdp_f087_financing_dependence_extfinsign_21d_base_v028_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029 63d sign × sqrt × close ext financing
def f087fdp_f087_financing_dependence_extfinsign_63d_base_v029_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030 252d sign × sqrt × close ext financing
def f087fdp_f087_financing_dependence_extfinsign_252d_base_v030_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031 21d fta z × close
def f087fdp_f087_financing_dependence_ftaz_21d_base_v031_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032 63d fta z × close
def f087fdp_f087_financing_dependence_ftaz_63d_base_v032_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033 252d fta z × close
def f087fdp_f087_financing_dependence_ftaz_252d_base_v033_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034 21d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_21d_base_v034_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035 63d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_63d_base_v035_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    result = base.ewm(span=63, min_periods=30).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036 252d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_252d_base_v036_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    result = base.ewm(span=126, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037 21d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_21d_base_v037_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038 63d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_63d_base_v038_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039 252d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_252d_base_v039_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040 21d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_21d_base_v040_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041 63d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_63d_base_v041_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base.ewm(span=63, min_periods=30).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042 252d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_252d_base_v042_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base.ewm(span=126, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043 5d ext financing × close
def f087fdp_f087_financing_dependence_extfin_5d_base_v043_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044 10d ext financing × close
def f087fdp_f087_financing_dependence_extfin_10d_base_v044_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045 42d ext financing × close
def f087fdp_f087_financing_dependence_extfin_42d_base_v045_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046 189d ext financing × close
def f087fdp_f087_financing_dependence_extfin_189d_base_v046_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047 378d ext financing × close
def f087fdp_f087_financing_dependence_extfin_378d_base_v047_signal(debt, sharesbas, closeadj):
    result = _f087_ext_financing(debt, sharesbas, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048 5d fta × close
def f087fdp_f087_financing_dependence_fta_5d_base_v048_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049 10d fta × close
def f087fdp_f087_financing_dependence_fta_10d_base_v049_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050 42d fta × close
def f087fdp_f087_financing_dependence_fta_42d_base_v050_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051 189d fta × close
def f087fdp_f087_financing_dependence_fta_189d_base_v051_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052 378d fta × close
def f087fdp_f087_financing_dependence_fta_378d_base_v052_signal(debt, sharesbas, assets, closeadj):
    result = _f087_financing_to_assets(debt, sharesbas, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053 42d capdep × close
def f087fdp_f087_financing_dependence_capdep_42d_base_v053_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054 189d capdep × close
def f087fdp_f087_financing_dependence_capdep_189d_base_v054_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055 378d capdep × close
def f087fdp_f087_financing_dependence_capdep_378d_base_v055_signal(debt, equity, closeadj):
    result = _f087_capital_dependence(debt, equity, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056 21d ext financing mean × close
def f087fdp_f087_financing_dependence_extfinmean_21d_base_v056_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057 63d ext financing mean × close
def f087fdp_f087_financing_dependence_extfinmean_63d_base_v057_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058 252d ext financing mean × close
def f087fdp_f087_financing_dependence_extfinmean_252d_base_v058_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059 21d ext financing × close × equity scale
def f087fdp_f087_financing_dependence_extfinxeqs_21d_base_v059_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v060 63d ext financing × close × log equity
def f087fdp_f087_financing_dependence_extfinxeqs_63d_base_v060_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v061 252d ext financing × close × log equity
def f087fdp_f087_financing_dependence_extfinxeqs_252d_base_v061_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * np.log(equity.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v062 21d ext financing × close²
def f087fdp_f087_financing_dependence_extfinxcsq_21d_base_v062_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063 63d ext financing × close²
def f087fdp_f087_financing_dependence_extfinxcsq_63d_base_v063_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064 252d ext financing × close²
def f087fdp_f087_financing_dependence_extfinxcsq_252d_base_v064_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065 21d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_21d_base_v065_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21)
    result = base * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v066 63d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_63d_base_v066_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63)
    result = base * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v067 252d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_252d_base_v067_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252)
    result = base * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v068 21d combined: ext fin + capdep × close
def f087fdp_f087_financing_dependence_combfin_21d_base_v068_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_capital_dependence(debt, equity, 21)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069 63d combined × close
def f087fdp_f087_financing_dependence_combfin_63d_base_v069_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_capital_dependence(debt, equity, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070 252d combined × close
def f087fdp_f087_financing_dependence_combfin_252d_base_v070_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 252)
    b = _f087_capital_dependence(debt, equity, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071 21d ext financing squared × close (with sign)
def f087fdp_f087_financing_dependence_extfinsq_21d_base_v071_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072 63d ext financing squared × close
def f087fdp_f087_financing_dependence_extfinsq_63d_base_v072_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073 252d ext financing squared × close
def f087fdp_f087_financing_dependence_extfinsq_252d_base_v073_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = (base * base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074 21d financing × close × assets log
def f087fdp_f087_financing_dependence_extfinxla_21d_base_v074_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21)
    result = base * closeadj * np.log(assets.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v075 252d financing × close × assets log
def f087fdp_f087_financing_dependence_extfinxla_252d_base_v075_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252)
    result = base * closeadj * np.log(assets.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f087fdp_f087_financing_dependence_extfin_21d_base_v001_signal,
    f087fdp_f087_financing_dependence_extfin_63d_base_v002_signal,
    f087fdp_f087_financing_dependence_extfin_126d_base_v003_signal,
    f087fdp_f087_financing_dependence_extfin_252d_base_v004_signal,
    f087fdp_f087_financing_dependence_extfin_504d_base_v005_signal,
    f087fdp_f087_financing_dependence_fta_21d_base_v006_signal,
    f087fdp_f087_financing_dependence_fta_63d_base_v007_signal,
    f087fdp_f087_financing_dependence_fta_126d_base_v008_signal,
    f087fdp_f087_financing_dependence_fta_252d_base_v009_signal,
    f087fdp_f087_financing_dependence_fta_504d_base_v010_signal,
    f087fdp_f087_financing_dependence_capdep_21d_base_v011_signal,
    f087fdp_f087_financing_dependence_capdep_63d_base_v012_signal,
    f087fdp_f087_financing_dependence_capdep_126d_base_v013_signal,
    f087fdp_f087_financing_dependence_capdep_252d_base_v014_signal,
    f087fdp_f087_financing_dependence_capdep_504d_base_v015_signal,
    f087fdp_f087_financing_dependence_extfinz_21d_base_v016_signal,
    f087fdp_f087_financing_dependence_extfinz_63d_base_v017_signal,
    f087fdp_f087_financing_dependence_extfinz_252d_base_v018_signal,
    f087fdp_f087_financing_dependence_extfinema_21d_base_v019_signal,
    f087fdp_f087_financing_dependence_extfinema_63d_base_v020_signal,
    f087fdp_f087_financing_dependence_extfinema_252d_base_v021_signal,
    f087fdp_f087_financing_dependence_extfinstd_21d_base_v022_signal,
    f087fdp_f087_financing_dependence_extfinstd_63d_base_v023_signal,
    f087fdp_f087_financing_dependence_extfinstd_252d_base_v024_signal,
    f087fdp_f087_financing_dependence_extfinxlog_21d_base_v025_signal,
    f087fdp_f087_financing_dependence_extfinxlog_63d_base_v026_signal,
    f087fdp_f087_financing_dependence_extfinxlog_252d_base_v027_signal,
    f087fdp_f087_financing_dependence_extfinsign_21d_base_v028_signal,
    f087fdp_f087_financing_dependence_extfinsign_63d_base_v029_signal,
    f087fdp_f087_financing_dependence_extfinsign_252d_base_v030_signal,
    f087fdp_f087_financing_dependence_ftaz_21d_base_v031_signal,
    f087fdp_f087_financing_dependence_ftaz_63d_base_v032_signal,
    f087fdp_f087_financing_dependence_ftaz_252d_base_v033_signal,
    f087fdp_f087_financing_dependence_ftaema_21d_base_v034_signal,
    f087fdp_f087_financing_dependence_ftaema_63d_base_v035_signal,
    f087fdp_f087_financing_dependence_ftaema_252d_base_v036_signal,
    f087fdp_f087_financing_dependence_capdepz_21d_base_v037_signal,
    f087fdp_f087_financing_dependence_capdepz_63d_base_v038_signal,
    f087fdp_f087_financing_dependence_capdepz_252d_base_v039_signal,
    f087fdp_f087_financing_dependence_capdepema_21d_base_v040_signal,
    f087fdp_f087_financing_dependence_capdepema_63d_base_v041_signal,
    f087fdp_f087_financing_dependence_capdepema_252d_base_v042_signal,
    f087fdp_f087_financing_dependence_extfin_5d_base_v043_signal,
    f087fdp_f087_financing_dependence_extfin_10d_base_v044_signal,
    f087fdp_f087_financing_dependence_extfin_42d_base_v045_signal,
    f087fdp_f087_financing_dependence_extfin_189d_base_v046_signal,
    f087fdp_f087_financing_dependence_extfin_378d_base_v047_signal,
    f087fdp_f087_financing_dependence_fta_5d_base_v048_signal,
    f087fdp_f087_financing_dependence_fta_10d_base_v049_signal,
    f087fdp_f087_financing_dependence_fta_42d_base_v050_signal,
    f087fdp_f087_financing_dependence_fta_189d_base_v051_signal,
    f087fdp_f087_financing_dependence_fta_378d_base_v052_signal,
    f087fdp_f087_financing_dependence_capdep_42d_base_v053_signal,
    f087fdp_f087_financing_dependence_capdep_189d_base_v054_signal,
    f087fdp_f087_financing_dependence_capdep_378d_base_v055_signal,
    f087fdp_f087_financing_dependence_extfinmean_21d_base_v056_signal,
    f087fdp_f087_financing_dependence_extfinmean_63d_base_v057_signal,
    f087fdp_f087_financing_dependence_extfinmean_252d_base_v058_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_21d_base_v059_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_63d_base_v060_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_252d_base_v061_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_21d_base_v062_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_63d_base_v063_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_252d_base_v064_signal,
    f087fdp_f087_financing_dependence_capdepxlc_21d_base_v065_signal,
    f087fdp_f087_financing_dependence_capdepxlc_63d_base_v066_signal,
    f087fdp_f087_financing_dependence_capdepxlc_252d_base_v067_signal,
    f087fdp_f087_financing_dependence_combfin_21d_base_v068_signal,
    f087fdp_f087_financing_dependence_combfin_63d_base_v069_signal,
    f087fdp_f087_financing_dependence_combfin_252d_base_v070_signal,
    f087fdp_f087_financing_dependence_extfinsq_21d_base_v071_signal,
    f087fdp_f087_financing_dependence_extfinsq_63d_base_v072_signal,
    f087fdp_f087_financing_dependence_extfinsq_252d_base_v073_signal,
    f087fdp_f087_financing_dependence_extfinxla_21d_base_v074_signal,
    f087fdp_f087_financing_dependence_extfinxla_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F087_FINANCING_DEPENDENCE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")

    cols = {"closeadj": closeadj, "debt": debt, "sharesbas": sharesbas, "assets": assets, "equity": equity}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f087_ext_financing", "_f087_financing_to_assets", "_f087_capital_dependence")
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
    print(f"OK f087_financing_dependence_base_001_075_claude: {n_features} features pass")
