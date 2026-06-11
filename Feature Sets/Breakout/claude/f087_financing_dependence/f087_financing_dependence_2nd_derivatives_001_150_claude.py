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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# Build 150 slope features by varying primitive, window, scaling, slope window
def _make_slope_features():
    pass


# v001 21d slope of 21d ext fin × close
def f087fdp_f087_financing_dependence_extfin_21d_slope_v001_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v002 5d slope of 21d ext fin × close
def f087fdp_f087_financing_dependence_extfin_21d_slope_v002_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v003 21d slope of 63d ext fin × close
def f087fdp_f087_financing_dependence_extfin_63d_slope_v003_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v004 63d slope of 126d ext fin × close
def f087fdp_f087_financing_dependence_extfin_126d_slope_v004_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v005 63d slope of 252d ext fin × close
def f087fdp_f087_financing_dependence_extfin_252d_slope_v005_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v006 63d slope of 504d ext fin × close
def f087fdp_f087_financing_dependence_extfin_504d_slope_v006_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007 21d slope of 21d fta × close
def f087fdp_f087_financing_dependence_fta_21d_slope_v007_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v008 5d slope of 21d fta × close
def f087fdp_f087_financing_dependence_fta_21d_slope_v008_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v009 21d slope of 63d fta × close
def f087fdp_f087_financing_dependence_fta_63d_slope_v009_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v010 63d slope of 126d fta × close
def f087fdp_f087_financing_dependence_fta_126d_slope_v010_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011 63d slope of 252d fta × close
def f087fdp_f087_financing_dependence_fta_252d_slope_v011_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v012 63d slope of 504d fta × close
def f087fdp_f087_financing_dependence_fta_504d_slope_v012_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013 21d slope of 21d capdep × close
def f087fdp_f087_financing_dependence_capdep_21d_slope_v013_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v014 21d slope of 63d capdep × close
def f087fdp_f087_financing_dependence_capdep_63d_slope_v014_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015 63d slope of 126d capdep × close
def f087fdp_f087_financing_dependence_capdep_126d_slope_v015_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016 63d slope of 252d capdep × close
def f087fdp_f087_financing_dependence_capdep_252d_slope_v016_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v017 63d slope of 504d capdep × close
def f087fdp_f087_financing_dependence_capdep_504d_slope_v017_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v018 21d slope of 21d ext fin z × close
def f087fdp_f087_financing_dependence_extfinz_21d_slope_v018_signal(debt, sharesbas, closeadj):
    base = _z(_f087_ext_financing(debt, sharesbas, 21), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v019 21d slope of 63d ext fin z × close
def f087fdp_f087_financing_dependence_extfinz_63d_slope_v019_signal(debt, sharesbas, closeadj):
    base = _z(_f087_ext_financing(debt, sharesbas, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v020 63d slope of 252d ext fin z × close
def f087fdp_f087_financing_dependence_extfinz_252d_slope_v020_signal(debt, sharesbas, closeadj):
    base = _z(_f087_ext_financing(debt, sharesbas, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v021 21d slope of 21d ext fin EMA × close
def f087fdp_f087_financing_dependence_extfinema_21d_slope_v021_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v022 21d slope of 63d ext fin EMA × close
def f087fdp_f087_financing_dependence_extfinema_63d_slope_v022_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).ewm(span=63, min_periods=30).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v023 63d slope of 252d ext fin EMA × close
def f087fdp_f087_financing_dependence_extfinema_252d_slope_v023_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252).ewm(span=126, min_periods=60).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v024 21d slope of 21d ext fin std × close
def f087fdp_f087_financing_dependence_extfinstd_21d_slope_v024_signal(debt, sharesbas, closeadj):
    base = _std(_f087_ext_financing(debt, sharesbas, 21), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v025 21d slope of 63d ext fin std × close
def f087fdp_f087_financing_dependence_extfinstd_63d_slope_v025_signal(debt, sharesbas, closeadj):
    base = _std(_f087_ext_financing(debt, sharesbas, 63), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v026 63d slope of 252d ext fin std × close
def f087fdp_f087_financing_dependence_extfinstd_252d_slope_v026_signal(debt, sharesbas, closeadj):
    base = _std(_f087_ext_financing(debt, sharesbas, 252), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v027 21d slope of 21d ext fin × log close
def f087fdp_f087_financing_dependence_extfinxlog_21d_slope_v027_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v028 21d slope of 63d ext fin × log close
def f087fdp_f087_financing_dependence_extfinxlog_63d_slope_v028_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v029 63d slope of 252d ext fin × log close
def f087fdp_f087_financing_dependence_extfinxlog_252d_slope_v029_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v030 21d slope of 21d sign-sqrt ext fin × close
def f087fdp_f087_financing_dependence_extfinsign_21d_slope_v030_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 21)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v031 21d slope of 63d sign-sqrt × close
def f087fdp_f087_financing_dependence_extfinsign_63d_slope_v031_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 63)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v032 63d slope of 252d sign-sqrt × close
def f087fdp_f087_financing_dependence_extfinsign_252d_slope_v032_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 252)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v033 21d slope of 21d fta z × close
def f087fdp_f087_financing_dependence_ftaz_21d_slope_v033_signal(debt, sharesbas, assets, closeadj):
    base = _z(_f087_financing_to_assets(debt, sharesbas, assets, 21), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v034 21d slope of 63d fta z × close
def f087fdp_f087_financing_dependence_ftaz_63d_slope_v034_signal(debt, sharesbas, assets, closeadj):
    base = _z(_f087_financing_to_assets(debt, sharesbas, assets, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v035 63d slope of 252d fta z × close
def f087fdp_f087_financing_dependence_ftaz_252d_slope_v035_signal(debt, sharesbas, assets, closeadj):
    base = _z(_f087_financing_to_assets(debt, sharesbas, assets, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v036 21d slope of 21d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_21d_slope_v036_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 21).ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v037 21d slope of 63d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_63d_slope_v037_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 63).ewm(span=63, min_periods=30).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v038 63d slope of 252d fta EMA × close
def f087fdp_f087_financing_dependence_ftaema_252d_slope_v038_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 252).ewm(span=126, min_periods=60).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v039 21d slope of 21d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_21d_slope_v039_signal(debt, equity, closeadj):
    base = _z(_f087_capital_dependence(debt, equity, 21), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v040 21d slope of 63d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_63d_slope_v040_signal(debt, equity, closeadj):
    base = _z(_f087_capital_dependence(debt, equity, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v041 63d slope of 252d capdep z × close
def f087fdp_f087_financing_dependence_capdepz_252d_slope_v041_signal(debt, equity, closeadj):
    base = _z(_f087_capital_dependence(debt, equity, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v042 21d slope of 21d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_21d_slope_v042_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21).ewm(span=21, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v043 21d slope of 63d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_63d_slope_v043_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63).ewm(span=63, min_periods=30).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v044 63d slope of 252d capdep EMA × close
def f087fdp_f087_financing_dependence_capdepema_252d_slope_v044_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252).ewm(span=126, min_periods=60).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v045 5d slope of 5d ext fin × close
def f087fdp_f087_financing_dependence_extfin_5d_slope_v045_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v046 5d slope of 10d ext fin × close
def f087fdp_f087_financing_dependence_extfin_10d_slope_v046_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047 21d slope of 42d ext fin × close
def f087fdp_f087_financing_dependence_extfin_42d_slope_v047_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048 63d slope of 189d ext fin × close
def f087fdp_f087_financing_dependence_extfin_189d_slope_v048_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049 63d slope of 378d ext fin × close
def f087fdp_f087_financing_dependence_extfin_378d_slope_v049_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v050 5d slope of 5d fta × close
def f087fdp_f087_financing_dependence_fta_5d_slope_v050_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v051 5d slope of 10d fta × close
def f087fdp_f087_financing_dependence_fta_10d_slope_v051_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v052 21d slope of 42d fta × close
def f087fdp_f087_financing_dependence_fta_42d_slope_v052_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v053 63d slope of 189d fta × close
def f087fdp_f087_financing_dependence_fta_189d_slope_v053_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v054 63d slope of 378d fta × close
def f087fdp_f087_financing_dependence_fta_378d_slope_v054_signal(debt, sharesbas, assets, closeadj):
    base = _f087_financing_to_assets(debt, sharesbas, assets, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055 21d slope of 42d capdep × close
def f087fdp_f087_financing_dependence_capdep_42d_slope_v055_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v056 63d slope of 189d capdep × close
def f087fdp_f087_financing_dependence_capdep_189d_slope_v056_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v057 63d slope of 378d capdep × close
def f087fdp_f087_financing_dependence_capdep_378d_slope_v057_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058 21d slope of 21d ext fin mean × close
def f087fdp_f087_financing_dependence_extfinmean_21d_slope_v058_signal(debt, sharesbas, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 21), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v059 21d slope of 63d ext fin mean × close
def f087fdp_f087_financing_dependence_extfinmean_63d_slope_v059_signal(debt, sharesbas, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 63), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060 63d slope of 252d ext fin mean × close
def f087fdp_f087_financing_dependence_extfinmean_252d_slope_v060_signal(debt, sharesbas, closeadj):
    base = _mean(_f087_ext_financing(debt, sharesbas, 252), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061 21d slope of 21d ext fin × close × log equity
def f087fdp_f087_financing_dependence_extfinxeqs_21d_slope_v061_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v062 21d slope of 63d ext fin × close × log equity
def f087fdp_f087_financing_dependence_extfinxeqs_63d_slope_v062_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063 63d slope of 252d ext fin × close × log equity
def f087fdp_f087_financing_dependence_extfinxeqs_252d_slope_v063_signal(debt, sharesbas, equity, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064 21d slope of 21d ext fin × close²
def f087fdp_f087_financing_dependence_extfinxcsq_21d_slope_v064_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v065 21d slope of 63d ext fin × close²
def f087fdp_f087_financing_dependence_extfinxcsq_63d_slope_v065_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066 63d slope of 252d ext fin × close²
def f087fdp_f087_financing_dependence_extfinxcsq_252d_slope_v066_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067 21d slope of 21d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_21d_slope_v067_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v068 21d slope of 63d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_63d_slope_v068_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069 63d slope of 252d capdep × close × log close
def f087fdp_f087_financing_dependence_capdepxlc_252d_slope_v069_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070 21d slope of 21d combined × close
def f087fdp_f087_financing_dependence_combfin_21d_slope_v070_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_capital_dependence(debt, equity, 21)
    base = (a + b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v071 21d slope of 63d combined × close
def f087fdp_f087_financing_dependence_combfin_63d_slope_v071_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_capital_dependence(debt, equity, 63)
    base = (a + b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072 63d slope of 252d combined × close
def f087fdp_f087_financing_dependence_combfin_252d_slope_v072_signal(debt, sharesbas, equity, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 252)
    b = _f087_capital_dependence(debt, equity, 252)
    base = (a + b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073 21d slope of 21d ext fin sq × close
def f087fdp_f087_financing_dependence_extfinsq_21d_slope_v073_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 21)
    base = (b * b.abs()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v074 21d slope of 63d ext fin sq × close
def f087fdp_f087_financing_dependence_extfinsq_63d_slope_v074_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 63)
    base = (b * b.abs()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075 63d slope of 252d ext fin sq × close
def f087fdp_f087_financing_dependence_extfinsq_252d_slope_v075_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 252)
    base = (b * b.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076 21d slope of 21d ext fin × close × log assets
def f087fdp_f087_financing_dependence_extfinxla_21d_slope_v076_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * np.log(assets.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v077 63d slope of 252d ext fin × close × log assets
def f087fdp_f087_financing_dependence_extfinxla_252d_slope_v077_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * np.log(assets.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v078 21d slope of 21d ext fin × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_21d_slope_v078_signal(debt, sharesbas, closeadj):
    base = np.tanh(_f087_ext_financing(debt, sharesbas, 21) * 5.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v079 21d slope of 63d ext fin × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_63d_slope_v079_signal(debt, sharesbas, closeadj):
    base = np.tanh(_f087_ext_financing(debt, sharesbas, 63) * 5.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v080 63d slope of 252d ext fin × close × tanh
def f087fdp_f087_financing_dependence_extfintanh_252d_slope_v080_signal(debt, sharesbas, closeadj):
    base = np.tanh(_f087_ext_financing(debt, sharesbas, 252) * 5.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v081 21d slope of 21d ext fin lag × close
def f087fdp_f087_financing_dependence_extfinlag_21d_slope_v081_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).shift(5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v082 21d slope of 63d ext fin lag × close
def f087fdp_f087_financing_dependence_extfinlag_63d_slope_v082_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).shift(21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v083 63d slope of 252d ext fin lag × close
def f087fdp_f087_financing_dependence_extfinlag_252d_slope_v083_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252).shift(63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v084 21d slope of 21d ext fin × asset turnover × close
def f087fdp_f087_financing_dependence_extfinxat_21d_slope_v084_signal(debt, sharesbas, assets, closeadj):
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    base = _f087_ext_financing(debt, sharesbas, 21) * at * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v085 21d slope of 63d ext fin × at × close
def f087fdp_f087_financing_dependence_extfinxat_63d_slope_v085_signal(debt, sharesbas, assets, closeadj):
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    base = _f087_ext_financing(debt, sharesbas, 63) * at * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v086 63d slope of 252d ext fin × at × close
def f087fdp_f087_financing_dependence_extfinxat_252d_slope_v086_signal(debt, sharesbas, assets, closeadj):
    at = (assets / assets.shift(252).replace(0, np.nan)).clip(0.5, 2.0)
    base = _f087_ext_financing(debt, sharesbas, 252) * at * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v087 21d slope of 21d fta tanh × close
def f087fdp_f087_financing_dependence_ftatanh_21d_slope_v087_signal(debt, sharesbas, assets, closeadj):
    base = np.tanh(_f087_financing_to_assets(debt, sharesbas, assets, 21) * 50.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v088 21d slope of 63d fta tanh × close
def f087fdp_f087_financing_dependence_ftatanh_63d_slope_v088_signal(debt, sharesbas, assets, closeadj):
    base = np.tanh(_f087_financing_to_assets(debt, sharesbas, assets, 63) * 50.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v089 63d slope of 252d fta tanh × close
def f087fdp_f087_financing_dependence_ftatanh_252d_slope_v089_signal(debt, sharesbas, assets, closeadj):
    base = np.tanh(_f087_financing_to_assets(debt, sharesbas, assets, 252) * 50.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v090 21d slope of 21d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_21d_slope_v090_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v091 21d slope of 63d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_63d_slope_v091_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v092 63d slope of 252d fta sign × close
def f087fdp_f087_financing_dependence_ftasign_252d_slope_v092_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    base = np.sign(b) * b.abs().pow(0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v093 21d slope of 21d ext fin × close × log assets/2
def f087fdp_f087_financing_dependence_extfinxla2_21d_slope_v093_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v094 21d slope of 63d ext fin × close × log assets/2
def f087fdp_f087_financing_dependence_extfinxla2_63d_slope_v094_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v095 63d slope of 252d ext fin × close × log assets/2
def f087fdp_f087_financing_dependence_extfinxla2_252d_slope_v095_signal(debt, sharesbas, assets, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * np.log(assets.abs().replace(0, np.nan).pow(0.5))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v096 21d slope of 21d ext fin × de × close
def f087fdp_f087_financing_dependence_extfinxde_21d_slope_v096_signal(debt, sharesbas, equity, closeadj):
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    base = _mean(_f087_ext_financing(debt, sharesbas, 21), 63) * de * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v097 21d slope of 63d ext fin × de × close
def f087fdp_f087_financing_dependence_extfinxde_63d_slope_v097_signal(debt, sharesbas, equity, closeadj):
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    base = _mean(_f087_ext_financing(debt, sharesbas, 63), 126) * de * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v098 63d slope of 252d ext fin × de × close
def f087fdp_f087_financing_dependence_extfinxde_252d_slope_v098_signal(debt, sharesbas, equity, closeadj):
    de = (debt / equity.replace(0, np.nan)).clip(0, 5)
    base = _mean(_f087_ext_financing(debt, sharesbas, 252), 252) * de * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v099 21d slope of 21d ext fin × close × log shares
def f087fdp_f087_financing_dependence_extfinxls_21d_slope_v099_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v100 21d slope of 63d ext fin × close × log shares
def f087fdp_f087_financing_dependence_extfinxls_63d_slope_v100_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v101 63d slope of 252d ext fin × close × log shares
def f087fdp_f087_financing_dependence_extfinxls_252d_slope_v101_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v102 21d slope of 21d ext fin max × close
def f087fdp_f087_financing_dependence_extfinmax_21d_slope_v102_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v103 21d slope of 63d ext fin max × close
def f087fdp_f087_financing_dependence_extfinmax_63d_slope_v103_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).rolling(126, min_periods=42).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v104 63d slope of 252d ext fin max × close
def f087fdp_f087_financing_dependence_extfinmax_252d_slope_v104_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v105 21d slope of 21d ext fin min × close
def f087fdp_f087_financing_dependence_extfinmin_21d_slope_v105_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v106 21d slope of 63d ext fin min × close
def f087fdp_f087_financing_dependence_extfinmin_63d_slope_v106_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).rolling(126, min_periods=42).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v107 63d slope of 252d ext fin min × close
def f087fdp_f087_financing_dependence_extfinmin_252d_slope_v107_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252).rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v108 21d slope of 21d ext fin range × close
def f087fdp_f087_financing_dependence_extfinrange_21d_slope_v108_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 21)
    rng = b.rolling(126, min_periods=42).max() - b.rolling(126, min_periods=42).min()
    base = rng * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v109 21d slope of 63d ext fin range × close
def f087fdp_f087_financing_dependence_extfinrange_63d_slope_v109_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 63)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v110 63d slope of 252d ext fin range × close
def f087fdp_f087_financing_dependence_extfinrange_252d_slope_v110_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 252)
    rng = b.rolling(504, min_periods=126).max() - b.rolling(504, min_periods=126).min()
    base = rng * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v111 21d slope of short/long fin ratio × close
def f087fdp_f087_financing_dependence_finratio_21v252_slope_v111_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_ext_financing(debt, sharesbas, 252).abs() + 1e-9
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v112 63d slope of 63v504 fin ratio × close
def f087fdp_f087_financing_dependence_finratio_63v504_slope_v112_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_ext_financing(debt, sharesbas, 504).abs() + 1e-9
    base = (a / b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v113 21d slope of 21m63 fin diff × close
def f087fdp_f087_financing_dependence_findiff_21m63_slope_v113_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 21)
    b = _f087_ext_financing(debt, sharesbas, 63)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114 63d slope of 63m252 fin diff × close
def f087fdp_f087_financing_dependence_findiff_63m252_slope_v114_signal(debt, sharesbas, closeadj):
    a = _f087_ext_financing(debt, sharesbas, 63)
    b = _f087_ext_financing(debt, sharesbas, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115 21d slope of 21d ext fin × close × log debt
def f087fdp_f087_financing_dependence_extfinxld_21d_slope_v115_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v116 21d slope of 63d ext fin × close × log debt
def f087fdp_f087_financing_dependence_extfinxld_63d_slope_v116_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117 63d slope of 252d ext fin × close × log debt
def f087fdp_f087_financing_dependence_extfinxld_252d_slope_v117_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 252) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118 21d slope of 21d capdep × close × log debt
def f087fdp_f087_financing_dependence_capdepxd_21d_slope_v118_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v119 21d slope of 63d capdep × close × log debt
def f087fdp_f087_financing_dependence_capdepxd_63d_slope_v119_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120 63d slope of 252d capdep × close × log debt
def f087fdp_f087_financing_dependence_capdepxd_252d_slope_v120_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj * np.log(debt.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121 21d slope of 21d capdep × close × log equity
def f087fdp_f087_financing_dependence_capdepxe_21d_slope_v121_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v122 21d slope of 63d capdep × close × log equity
def f087fdp_f087_financing_dependence_capdepxe_63d_slope_v122_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123 63d slope of 252d capdep × close × log equity
def f087fdp_f087_financing_dependence_capdepxe_252d_slope_v123_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252) * closeadj * np.log(equity.abs().replace(0, np.nan))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124 21d slope of 21d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_21d_slope_v124_signal(debt, equity, closeadj):
    base = _std(_f087_capital_dependence(debt, equity, 21), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v125 21d slope of 63d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_63d_slope_v125_signal(debt, equity, closeadj):
    base = _std(_f087_capital_dependence(debt, equity, 63), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126 63d slope of 252d capdep std × close
def f087fdp_f087_financing_dependence_capdepstd_252d_slope_v126_signal(debt, equity, closeadj):
    base = _std(_f087_capital_dependence(debt, equity, 252), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127 21d slope of 21d capdep×ef × close
def f087fdp_f087_financing_dependence_capdepxef_21d_slope_v127_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 21)
    b = _f087_ext_financing(debt, sharesbas, 21)
    base = (a * b) * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v128 21d slope of 63d capdep×ef × close
def f087fdp_f087_financing_dependence_capdepxef_63d_slope_v128_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 63)
    b = _f087_ext_financing(debt, sharesbas, 63)
    base = (a * b) * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129 63d slope of 252d capdep×ef × close
def f087fdp_f087_financing_dependence_capdepxef_252d_slope_v129_signal(debt, sharesbas, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 252)
    b = _f087_ext_financing(debt, sharesbas, 252)
    base = (a * b) * closeadj * 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130 21d slope of 21d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_21d_slope_v130_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 21)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    base = a * base_lvl * closeadj * 10.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v131 21d slope of 63d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_63d_slope_v131_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 63)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    base = a * base_lvl * closeadj * 10.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132 63d slope of 252d capdep ratio × close
def f087fdp_f087_financing_dependence_capdepratio_252d_slope_v132_signal(debt, equity, closeadj):
    a = _f087_capital_dependence(debt, equity, 252)
    base_lvl = (debt / (debt + equity).replace(0, np.nan)).clip(0, 1)
    base = a * base_lvl * closeadj * 10.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133 21d slope of 21d fta sq × close
def f087fdp_f087_financing_dependence_ftasq_21d_slope_v133_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    base = (b * b.abs()) * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v134 21d slope of 63d fta sq × close
def f087fdp_f087_financing_dependence_ftasq_63d_slope_v134_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    base = (b * b.abs()) * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135 63d slope of 252d fta sq × close
def f087fdp_f087_financing_dependence_ftasq_252d_slope_v135_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    base = (b * b.abs()) * closeadj * 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136 21d slope of 21d fta range × close
def f087fdp_f087_financing_dependence_ftarange_21d_slope_v136_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 21)
    rng = b.rolling(126, min_periods=42).max() - b.rolling(126, min_periods=42).min()
    base = rng * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v137 21d slope of 63d fta range × close
def f087fdp_f087_financing_dependence_ftarange_63d_slope_v137_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 63)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj * 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138 63d slope of 252d fta range × close
def f087fdp_f087_financing_dependence_ftarange_252d_slope_v138_signal(debt, sharesbas, assets, closeadj):
    b = _f087_financing_to_assets(debt, sharesbas, assets, 252)
    rng = b.rolling(504, min_periods=126).max() - b.rolling(504, min_periods=126).min()
    base = rng * closeadj * 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139 21d slope of 21d ext fin count × close
def f087fdp_f087_financing_dependence_extfincount_21d_slope_v139_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 21)
    cnt = (b > 0).astype(float).rolling(126, min_periods=21).sum()
    base = cnt * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v140 21d slope of 63d ext fin count × close
def f087fdp_f087_financing_dependence_extfincount_63d_slope_v140_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 63)
    cnt = (b > 0).astype(float).rolling(252, min_periods=63).sum()
    base = cnt * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141 63d slope of 252d ext fin count × close
def f087fdp_f087_financing_dependence_extfincount_252d_slope_v141_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 252)
    cnt = (b > 0).astype(float).rolling(504, min_periods=126).sum()
    base = cnt * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142 21d slope of 21d ext fin area × close
def f087fdp_f087_financing_dependence_extfinarea_21d_slope_v142_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 21).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v143 63d slope of 63d ext fin area × close
def f087fdp_f087_financing_dependence_extfinarea_63d_slope_v143_signal(debt, sharesbas, closeadj):
    base = _f087_ext_financing(debt, sharesbas, 63).rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v144 21d slope of 21d ext fin sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_21d_slope_v144_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 21)
    s = _std(b, 252).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v145 21d slope of 63d ext fin sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_63d_slope_v145_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 63)
    s = _std(b, 252).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v146 63d slope of 252d ext fin sharpe × close
def f087fdp_f087_financing_dependence_extfinsharpe_252d_slope_v146_signal(debt, sharesbas, closeadj):
    b = _f087_ext_financing(debt, sharesbas, 252)
    s = _std(b, 504).replace(0, np.nan)
    base = (b / s) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v147 21d slope of 21d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_21d_slope_v147_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21).rolling(63, min_periods=21).min() * closeadj * 10.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v148 21d slope of 63d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_63d_slope_v148_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 63).rolling(126, min_periods=42).min() * closeadj * 10.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v149 63d slope of 252d capdep min × close
def f087fdp_f087_financing_dependence_capdepmin_252d_slope_v149_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 252).rolling(252, min_periods=63).min() * closeadj * 10.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v150 21d slope of 21d capdep max × close
def f087fdp_f087_financing_dependence_capdepmax_21d_slope_v150_signal(debt, equity, closeadj):
    base = _f087_capital_dependence(debt, equity, 21).rolling(63, min_periods=21).max() * closeadj * 10.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f087fdp_f087_financing_dependence_extfin_21d_slope_v001_signal,
    f087fdp_f087_financing_dependence_extfin_21d_slope_v002_signal,
    f087fdp_f087_financing_dependence_extfin_63d_slope_v003_signal,
    f087fdp_f087_financing_dependence_extfin_126d_slope_v004_signal,
    f087fdp_f087_financing_dependence_extfin_252d_slope_v005_signal,
    f087fdp_f087_financing_dependence_extfin_504d_slope_v006_signal,
    f087fdp_f087_financing_dependence_fta_21d_slope_v007_signal,
    f087fdp_f087_financing_dependence_fta_21d_slope_v008_signal,
    f087fdp_f087_financing_dependence_fta_63d_slope_v009_signal,
    f087fdp_f087_financing_dependence_fta_126d_slope_v010_signal,
    f087fdp_f087_financing_dependence_fta_252d_slope_v011_signal,
    f087fdp_f087_financing_dependence_fta_504d_slope_v012_signal,
    f087fdp_f087_financing_dependence_capdep_21d_slope_v013_signal,
    f087fdp_f087_financing_dependence_capdep_63d_slope_v014_signal,
    f087fdp_f087_financing_dependence_capdep_126d_slope_v015_signal,
    f087fdp_f087_financing_dependence_capdep_252d_slope_v016_signal,
    f087fdp_f087_financing_dependence_capdep_504d_slope_v017_signal,
    f087fdp_f087_financing_dependence_extfinz_21d_slope_v018_signal,
    f087fdp_f087_financing_dependence_extfinz_63d_slope_v019_signal,
    f087fdp_f087_financing_dependence_extfinz_252d_slope_v020_signal,
    f087fdp_f087_financing_dependence_extfinema_21d_slope_v021_signal,
    f087fdp_f087_financing_dependence_extfinema_63d_slope_v022_signal,
    f087fdp_f087_financing_dependence_extfinema_252d_slope_v023_signal,
    f087fdp_f087_financing_dependence_extfinstd_21d_slope_v024_signal,
    f087fdp_f087_financing_dependence_extfinstd_63d_slope_v025_signal,
    f087fdp_f087_financing_dependence_extfinstd_252d_slope_v026_signal,
    f087fdp_f087_financing_dependence_extfinxlog_21d_slope_v027_signal,
    f087fdp_f087_financing_dependence_extfinxlog_63d_slope_v028_signal,
    f087fdp_f087_financing_dependence_extfinxlog_252d_slope_v029_signal,
    f087fdp_f087_financing_dependence_extfinsign_21d_slope_v030_signal,
    f087fdp_f087_financing_dependence_extfinsign_63d_slope_v031_signal,
    f087fdp_f087_financing_dependence_extfinsign_252d_slope_v032_signal,
    f087fdp_f087_financing_dependence_ftaz_21d_slope_v033_signal,
    f087fdp_f087_financing_dependence_ftaz_63d_slope_v034_signal,
    f087fdp_f087_financing_dependence_ftaz_252d_slope_v035_signal,
    f087fdp_f087_financing_dependence_ftaema_21d_slope_v036_signal,
    f087fdp_f087_financing_dependence_ftaema_63d_slope_v037_signal,
    f087fdp_f087_financing_dependence_ftaema_252d_slope_v038_signal,
    f087fdp_f087_financing_dependence_capdepz_21d_slope_v039_signal,
    f087fdp_f087_financing_dependence_capdepz_63d_slope_v040_signal,
    f087fdp_f087_financing_dependence_capdepz_252d_slope_v041_signal,
    f087fdp_f087_financing_dependence_capdepema_21d_slope_v042_signal,
    f087fdp_f087_financing_dependence_capdepema_63d_slope_v043_signal,
    f087fdp_f087_financing_dependence_capdepema_252d_slope_v044_signal,
    f087fdp_f087_financing_dependence_extfin_5d_slope_v045_signal,
    f087fdp_f087_financing_dependence_extfin_10d_slope_v046_signal,
    f087fdp_f087_financing_dependence_extfin_42d_slope_v047_signal,
    f087fdp_f087_financing_dependence_extfin_189d_slope_v048_signal,
    f087fdp_f087_financing_dependence_extfin_378d_slope_v049_signal,
    f087fdp_f087_financing_dependence_fta_5d_slope_v050_signal,
    f087fdp_f087_financing_dependence_fta_10d_slope_v051_signal,
    f087fdp_f087_financing_dependence_fta_42d_slope_v052_signal,
    f087fdp_f087_financing_dependence_fta_189d_slope_v053_signal,
    f087fdp_f087_financing_dependence_fta_378d_slope_v054_signal,
    f087fdp_f087_financing_dependence_capdep_42d_slope_v055_signal,
    f087fdp_f087_financing_dependence_capdep_189d_slope_v056_signal,
    f087fdp_f087_financing_dependence_capdep_378d_slope_v057_signal,
    f087fdp_f087_financing_dependence_extfinmean_21d_slope_v058_signal,
    f087fdp_f087_financing_dependence_extfinmean_63d_slope_v059_signal,
    f087fdp_f087_financing_dependence_extfinmean_252d_slope_v060_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_21d_slope_v061_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_63d_slope_v062_signal,
    f087fdp_f087_financing_dependence_extfinxeqs_252d_slope_v063_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_21d_slope_v064_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_63d_slope_v065_signal,
    f087fdp_f087_financing_dependence_extfinxcsq_252d_slope_v066_signal,
    f087fdp_f087_financing_dependence_capdepxlc_21d_slope_v067_signal,
    f087fdp_f087_financing_dependence_capdepxlc_63d_slope_v068_signal,
    f087fdp_f087_financing_dependence_capdepxlc_252d_slope_v069_signal,
    f087fdp_f087_financing_dependence_combfin_21d_slope_v070_signal,
    f087fdp_f087_financing_dependence_combfin_63d_slope_v071_signal,
    f087fdp_f087_financing_dependence_combfin_252d_slope_v072_signal,
    f087fdp_f087_financing_dependence_extfinsq_21d_slope_v073_signal,
    f087fdp_f087_financing_dependence_extfinsq_63d_slope_v074_signal,
    f087fdp_f087_financing_dependence_extfinsq_252d_slope_v075_signal,
    f087fdp_f087_financing_dependence_extfinxla_21d_slope_v076_signal,
    f087fdp_f087_financing_dependence_extfinxla_252d_slope_v077_signal,
    f087fdp_f087_financing_dependence_extfintanh_21d_slope_v078_signal,
    f087fdp_f087_financing_dependence_extfintanh_63d_slope_v079_signal,
    f087fdp_f087_financing_dependence_extfintanh_252d_slope_v080_signal,
    f087fdp_f087_financing_dependence_extfinlag_21d_slope_v081_signal,
    f087fdp_f087_financing_dependence_extfinlag_63d_slope_v082_signal,
    f087fdp_f087_financing_dependence_extfinlag_252d_slope_v083_signal,
    f087fdp_f087_financing_dependence_extfinxat_21d_slope_v084_signal,
    f087fdp_f087_financing_dependence_extfinxat_63d_slope_v085_signal,
    f087fdp_f087_financing_dependence_extfinxat_252d_slope_v086_signal,
    f087fdp_f087_financing_dependence_ftatanh_21d_slope_v087_signal,
    f087fdp_f087_financing_dependence_ftatanh_63d_slope_v088_signal,
    f087fdp_f087_financing_dependence_ftatanh_252d_slope_v089_signal,
    f087fdp_f087_financing_dependence_ftasign_21d_slope_v090_signal,
    f087fdp_f087_financing_dependence_ftasign_63d_slope_v091_signal,
    f087fdp_f087_financing_dependence_ftasign_252d_slope_v092_signal,
    f087fdp_f087_financing_dependence_extfinxla2_21d_slope_v093_signal,
    f087fdp_f087_financing_dependence_extfinxla2_63d_slope_v094_signal,
    f087fdp_f087_financing_dependence_extfinxla2_252d_slope_v095_signal,
    f087fdp_f087_financing_dependence_extfinxde_21d_slope_v096_signal,
    f087fdp_f087_financing_dependence_extfinxde_63d_slope_v097_signal,
    f087fdp_f087_financing_dependence_extfinxde_252d_slope_v098_signal,
    f087fdp_f087_financing_dependence_extfinxls_21d_slope_v099_signal,
    f087fdp_f087_financing_dependence_extfinxls_63d_slope_v100_signal,
    f087fdp_f087_financing_dependence_extfinxls_252d_slope_v101_signal,
    f087fdp_f087_financing_dependence_extfinmax_21d_slope_v102_signal,
    f087fdp_f087_financing_dependence_extfinmax_63d_slope_v103_signal,
    f087fdp_f087_financing_dependence_extfinmax_252d_slope_v104_signal,
    f087fdp_f087_financing_dependence_extfinmin_21d_slope_v105_signal,
    f087fdp_f087_financing_dependence_extfinmin_63d_slope_v106_signal,
    f087fdp_f087_financing_dependence_extfinmin_252d_slope_v107_signal,
    f087fdp_f087_financing_dependence_extfinrange_21d_slope_v108_signal,
    f087fdp_f087_financing_dependence_extfinrange_63d_slope_v109_signal,
    f087fdp_f087_financing_dependence_extfinrange_252d_slope_v110_signal,
    f087fdp_f087_financing_dependence_finratio_21v252_slope_v111_signal,
    f087fdp_f087_financing_dependence_finratio_63v504_slope_v112_signal,
    f087fdp_f087_financing_dependence_findiff_21m63_slope_v113_signal,
    f087fdp_f087_financing_dependence_findiff_63m252_slope_v114_signal,
    f087fdp_f087_financing_dependence_extfinxld_21d_slope_v115_signal,
    f087fdp_f087_financing_dependence_extfinxld_63d_slope_v116_signal,
    f087fdp_f087_financing_dependence_extfinxld_252d_slope_v117_signal,
    f087fdp_f087_financing_dependence_capdepxd_21d_slope_v118_signal,
    f087fdp_f087_financing_dependence_capdepxd_63d_slope_v119_signal,
    f087fdp_f087_financing_dependence_capdepxd_252d_slope_v120_signal,
    f087fdp_f087_financing_dependence_capdepxe_21d_slope_v121_signal,
    f087fdp_f087_financing_dependence_capdepxe_63d_slope_v122_signal,
    f087fdp_f087_financing_dependence_capdepxe_252d_slope_v123_signal,
    f087fdp_f087_financing_dependence_capdepstd_21d_slope_v124_signal,
    f087fdp_f087_financing_dependence_capdepstd_63d_slope_v125_signal,
    f087fdp_f087_financing_dependence_capdepstd_252d_slope_v126_signal,
    f087fdp_f087_financing_dependence_capdepxef_21d_slope_v127_signal,
    f087fdp_f087_financing_dependence_capdepxef_63d_slope_v128_signal,
    f087fdp_f087_financing_dependence_capdepxef_252d_slope_v129_signal,
    f087fdp_f087_financing_dependence_capdepratio_21d_slope_v130_signal,
    f087fdp_f087_financing_dependence_capdepratio_63d_slope_v131_signal,
    f087fdp_f087_financing_dependence_capdepratio_252d_slope_v132_signal,
    f087fdp_f087_financing_dependence_ftasq_21d_slope_v133_signal,
    f087fdp_f087_financing_dependence_ftasq_63d_slope_v134_signal,
    f087fdp_f087_financing_dependence_ftasq_252d_slope_v135_signal,
    f087fdp_f087_financing_dependence_ftarange_21d_slope_v136_signal,
    f087fdp_f087_financing_dependence_ftarange_63d_slope_v137_signal,
    f087fdp_f087_financing_dependence_ftarange_252d_slope_v138_signal,
    f087fdp_f087_financing_dependence_extfincount_21d_slope_v139_signal,
    f087fdp_f087_financing_dependence_extfincount_63d_slope_v140_signal,
    f087fdp_f087_financing_dependence_extfincount_252d_slope_v141_signal,
    f087fdp_f087_financing_dependence_extfinarea_21d_slope_v142_signal,
    f087fdp_f087_financing_dependence_extfinarea_63d_slope_v143_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_21d_slope_v144_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_63d_slope_v145_signal,
    f087fdp_f087_financing_dependence_extfinsharpe_252d_slope_v146_signal,
    f087fdp_f087_financing_dependence_capdepmin_21d_slope_v147_signal,
    f087fdp_f087_financing_dependence_capdepmin_63d_slope_v148_signal,
    f087fdp_f087_financing_dependence_capdepmin_252d_slope_v149_signal,
    f087fdp_f087_financing_dependence_capdepmax_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F087_FINANCING_DEPENDENCE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f087_financing_dependence_2nd_derivatives_001_150_claude: {n_features} features pass")
