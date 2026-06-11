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
def _f001_ath_level(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).max()


def _f001_drawdown_from_ath(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - ath) / ath.replace(0, np.nan).abs()


def _f001_dd_signature(close, w):
    ath = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = (close - ath) / ath.replace(0, np.nan).abs()
    rng = ath - close.rolling(w, min_periods=max(1, w // 2)).min()
    return dd * close / rng.replace(0, np.nan).abs()

def f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v001_signal(closeadj):
    base = _f001_ath_level(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v002_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v003_signal(closeadj):
    base = _f001_dd_signature(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v004_signal(closeadj):
    base = _f001_ath_level(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v005_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v006_signal(closeadj):
    base = _f001_dd_signature(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v007_signal(closeadj):
    base = _f001_ath_level(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v008_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v009_signal(closeadj):
    base = _f001_dd_signature(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v010_signal(closeadj):
    base = _f001_ath_level(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v011_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v012_signal(closeadj):
    base = _f001_dd_signature(closeadj, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v013_signal(closeadj):
    base = _f001_ath_level(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v014_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v015_signal(closeadj):
    base = _f001_dd_signature(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v016_signal(closeadj):
    base = _f001_ath_level(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v017_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v018_signal(closeadj):
    base = _f001_dd_signature(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v019_signal(closeadj):
    base = _f001_ath_level(closeadj, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v020_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v021_signal(closeadj):
    base = _f001_dd_signature(closeadj, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v022_signal(closeadj):
    base = _f001_ath_level(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v023_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v024_signal(closeadj):
    base = _f001_dd_signature(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v025_signal(closeadj):
    base = _f001_ath_level(closeadj, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v026_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v027_signal(closeadj):
    base = _f001_dd_signature(closeadj, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v028_signal(closeadj):
    base = _f001_ath_level(closeadj, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v029_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v030_signal(closeadj):
    base = _f001_dd_signature(closeadj, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v031_signal(closeadj):
    base = _f001_ath_level(closeadj, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v032_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v033_signal(closeadj):
    base = _f001_dd_signature(closeadj, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v034_signal(closeadj):
    base = _f001_ath_level(closeadj, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v035_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v036_signal(closeadj):
    base = _f001_dd_signature(closeadj, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v037_signal(closeadj):
    base = _f001_ath_level(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v038_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v039_signal(closeadj):
    base = _f001_dd_signature(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v040_signal(closeadj):
    base = _f001_ath_level(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v041_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v042_signal(closeadj):
    base = _f001_dd_signature(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v043_signal(closeadj):
    base = _f001_ath_level(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v044_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v045_signal(closeadj):
    base = _f001_dd_signature(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v046_signal(closeadj):
    base = _f001_ath_level(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v047_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v048_signal(closeadj):
    base = _f001_dd_signature(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v049_signal(closeadj):
    base = _f001_ath_level(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v050_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v051_signal(closeadj):
    base = _f001_dd_signature(closeadj, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v052_signal(closeadj):
    base = _f001_ath_level(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v053_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v054_signal(closeadj):
    base = _f001_dd_signature(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v055_signal(closeadj):
    base = _f001_ath_level(closeadj, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v056_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v057_signal(closeadj):
    base = _f001_dd_signature(closeadj, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v058_signal(closeadj):
    base = _f001_ath_level(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v059_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v060_signal(closeadj):
    base = _f001_dd_signature(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v061_signal(closeadj):
    base = _f001_ath_level(closeadj, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v062_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v063_signal(closeadj):
    base = _f001_dd_signature(closeadj, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v064_signal(closeadj):
    base = _f001_ath_level(closeadj, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v065_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v066_signal(closeadj):
    base = _f001_dd_signature(closeadj, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v067_signal(closeadj):
    base = _f001_ath_level(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v068_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v069_signal(closeadj):
    base = _f001_dd_signature(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v070_signal(closeadj):
    base = _f001_ath_level(closeadj, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v071_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v072_signal(closeadj):
    base = _f001_dd_signature(closeadj, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v073_signal(closeadj):
    base = _f001_ath_level(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v074_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v075_signal(closeadj):
    base = _f001_dd_signature(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v076_signal(closeadj):
    base = _f001_ath_level(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v077_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v078_signal(closeadj):
    base = _f001_dd_signature(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v079_signal(closeadj):
    base = _f001_ath_level(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v080_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v081_signal(closeadj):
    base = _f001_dd_signature(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v082_signal(closeadj):
    base = _f001_ath_level(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v083_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v084_signal(closeadj):
    base = _f001_dd_signature(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v085_signal(closeadj):
    base = _f001_ath_level(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v086_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v087_signal(closeadj):
    base = _f001_dd_signature(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v088_signal(closeadj):
    base = _f001_ath_level(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v089_signal(closeadj):
    base = _f001_drawdown_from_ath(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v090_signal(closeadj):
    base = _f001_dd_signature(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_5d_jerk_v091_signal(closeadj):
    base = (_f001_ath_level(closeadj, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_5d_jerk_v092_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_5d_jerk_v093_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_10d_jerk_v094_signal(closeadj):
    base = (_f001_ath_level(closeadj, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_10d_jerk_v095_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_10d_jerk_v096_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_21d_jerk_v097_signal(closeadj):
    base = (_f001_ath_level(closeadj, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_21d_jerk_v098_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_21d_jerk_v099_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_42d_jerk_v100_signal(closeadj):
    base = (_f001_ath_level(closeadj, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_42d_jerk_v101_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_42d_jerk_v102_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_63d_jerk_v103_signal(closeadj):
    base = (_f001_ath_level(closeadj, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_63d_jerk_v104_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_63d_jerk_v105_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_126d_jerk_v106_signal(closeadj):
    base = (_f001_ath_level(closeadj, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_126d_jerk_v107_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_126d_jerk_v108_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_189d_jerk_v109_signal(closeadj):
    base = (_f001_ath_level(closeadj, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_189d_jerk_v110_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_189d_jerk_v111_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_252d_jerk_v112_signal(closeadj):
    base = (_f001_ath_level(closeadj, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_252d_jerk_v113_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_252d_jerk_v114_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_378d_jerk_v115_signal(closeadj):
    base = (_f001_ath_level(closeadj, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_378d_jerk_v116_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_378d_jerk_v117_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlsq_504d_jerk_v118_signal(closeadj):
    base = (_f001_ath_level(closeadj, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathsq_504d_jerk_v119_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigsq_504d_jerk_v120_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_5d_jerk_v121_signal(closeadj):
    base = (_f001_ath_level(closeadj, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_5d_jerk_v122_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_5d_jerk_v123_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_10d_jerk_v124_signal(closeadj):
    base = (_f001_ath_level(closeadj, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_10d_jerk_v125_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_10d_jerk_v126_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_21d_jerk_v127_signal(closeadj):
    base = (_f001_ath_level(closeadj, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_21d_jerk_v128_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_21d_jerk_v129_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_42d_jerk_v130_signal(closeadj):
    base = (_f001_ath_level(closeadj, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_42d_jerk_v131_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_42d_jerk_v132_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_63d_jerk_v133_signal(closeadj):
    base = (_f001_ath_level(closeadj, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_63d_jerk_v134_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_63d_jerk_v135_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_126d_jerk_v136_signal(closeadj):
    base = (_f001_ath_level(closeadj, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_126d_jerk_v137_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_126d_jerk_v138_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_189d_jerk_v139_signal(closeadj):
    base = (_f001_ath_level(closeadj, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_189d_jerk_v140_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_189d_jerk_v141_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_252d_jerk_v142_signal(closeadj):
    base = (_f001_ath_level(closeadj, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_252d_jerk_v143_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_252d_jerk_v144_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_378d_jerk_v145_signal(closeadj):
    base = (_f001_ath_level(closeadj, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_378d_jerk_v146_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_378d_jerk_v147_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_athlvlab_504d_jerk_v148_signal(closeadj):
    base = (_f001_ath_level(closeadj, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddathab_504d_jerk_v149_signal(closeadj):
    base = (_f001_drawdown_from_ath(closeadj, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f001dfa_f001_drawdown_from_ath_ddsigab_504d_jerk_v150_signal(closeadj):
    base = (_f001_dd_signature(closeadj, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v001_signal,
    f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v002_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v003_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v004_signal,
    f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v005_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v006_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v007_signal,
    f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v008_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v009_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v010_signal,
    f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v011_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v012_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v013_signal,
    f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v014_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v015_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v016_signal,
    f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v017_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v018_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v019_signal,
    f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v020_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v021_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v022_signal,
    f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v023_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v024_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v025_signal,
    f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v026_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v027_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v028_signal,
    f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v029_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v030_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v031_signal,
    f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v032_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v033_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v034_signal,
    f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v035_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v036_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v037_signal,
    f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v038_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v039_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v040_signal,
    f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v041_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v042_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v043_signal,
    f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v044_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v045_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v046_signal,
    f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v047_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v048_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v049_signal,
    f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v050_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v051_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v052_signal,
    f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v053_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v054_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v055_signal,
    f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v056_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v057_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v058_signal,
    f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v059_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v060_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_5d_jerk_v061_signal,
    f001dfa_f001_drawdown_from_ath_ddath_5d_jerk_v062_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_5d_jerk_v063_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_10d_jerk_v064_signal,
    f001dfa_f001_drawdown_from_ath_ddath_10d_jerk_v065_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_10d_jerk_v066_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_21d_jerk_v067_signal,
    f001dfa_f001_drawdown_from_ath_ddath_21d_jerk_v068_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_21d_jerk_v069_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_42d_jerk_v070_signal,
    f001dfa_f001_drawdown_from_ath_ddath_42d_jerk_v071_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_42d_jerk_v072_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_63d_jerk_v073_signal,
    f001dfa_f001_drawdown_from_ath_ddath_63d_jerk_v074_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_63d_jerk_v075_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_126d_jerk_v076_signal,
    f001dfa_f001_drawdown_from_ath_ddath_126d_jerk_v077_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_126d_jerk_v078_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_189d_jerk_v079_signal,
    f001dfa_f001_drawdown_from_ath_ddath_189d_jerk_v080_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_189d_jerk_v081_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_252d_jerk_v082_signal,
    f001dfa_f001_drawdown_from_ath_ddath_252d_jerk_v083_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_252d_jerk_v084_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_378d_jerk_v085_signal,
    f001dfa_f001_drawdown_from_ath_ddath_378d_jerk_v086_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_378d_jerk_v087_signal,
    f001dfa_f001_drawdown_from_ath_athlvl_504d_jerk_v088_signal,
    f001dfa_f001_drawdown_from_ath_ddath_504d_jerk_v089_signal,
    f001dfa_f001_drawdown_from_ath_ddsig_504d_jerk_v090_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_5d_jerk_v091_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_5d_jerk_v092_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_5d_jerk_v093_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_10d_jerk_v094_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_10d_jerk_v095_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_10d_jerk_v096_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_21d_jerk_v097_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_21d_jerk_v098_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_21d_jerk_v099_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_42d_jerk_v100_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_42d_jerk_v101_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_42d_jerk_v102_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_63d_jerk_v103_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_63d_jerk_v104_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_63d_jerk_v105_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_126d_jerk_v106_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_126d_jerk_v107_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_126d_jerk_v108_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_189d_jerk_v109_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_189d_jerk_v110_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_189d_jerk_v111_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_252d_jerk_v112_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_252d_jerk_v113_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_252d_jerk_v114_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_378d_jerk_v115_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_378d_jerk_v116_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_378d_jerk_v117_signal,
    f001dfa_f001_drawdown_from_ath_athlvlsq_504d_jerk_v118_signal,
    f001dfa_f001_drawdown_from_ath_ddathsq_504d_jerk_v119_signal,
    f001dfa_f001_drawdown_from_ath_ddsigsq_504d_jerk_v120_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_5d_jerk_v121_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_5d_jerk_v122_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_5d_jerk_v123_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_10d_jerk_v124_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_10d_jerk_v125_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_10d_jerk_v126_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_21d_jerk_v127_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_21d_jerk_v128_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_21d_jerk_v129_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_42d_jerk_v130_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_42d_jerk_v131_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_42d_jerk_v132_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_63d_jerk_v133_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_63d_jerk_v134_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_63d_jerk_v135_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_126d_jerk_v136_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_126d_jerk_v137_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_126d_jerk_v138_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_189d_jerk_v139_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_189d_jerk_v140_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_189d_jerk_v141_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_252d_jerk_v142_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_252d_jerk_v143_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_252d_jerk_v144_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_378d_jerk_v145_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_378d_jerk_v146_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_378d_jerk_v147_signal,
    f001dfa_f001_drawdown_from_ath_athlvlab_504d_jerk_v148_signal,
    f001dfa_f001_drawdown_from_ath_ddathab_504d_jerk_v149_signal,
    f001dfa_f001_drawdown_from_ath_ddsigab_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F001_DRAWDOWN_FROM_ATH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f001_ath_level", "_f001_drawdown_from_ath", "_f001_dd_signature",)
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
    print(f"OK f001_drawdown_from_ath_3rd_derivatives_001_150_claude: {n_features} features pass")
