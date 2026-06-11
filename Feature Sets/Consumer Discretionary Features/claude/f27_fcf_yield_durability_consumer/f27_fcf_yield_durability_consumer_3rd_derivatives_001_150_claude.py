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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f27_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f27_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f27_fcf_compound_quality(fcf, marketcap, w):
    yld = fcf / marketcap.replace(0, np.nan)
    return _mean(yld, w) - _std(yld, w)


# ===== features =====

def f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v001_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v002_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v003_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v004_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v005_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 5) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v006_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v007_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v008_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v009_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 10) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v010_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 10) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v011_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v012_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v013_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v014_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v015_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v016_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v017_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v018_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v019_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v020_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 42) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v021_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v022_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v023_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v024_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v025_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v026_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v027_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v028_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v029_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v030_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 126) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v031_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v032_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v033_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v034_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 189) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v035_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 189) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v036_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v037_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v038_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v039_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v040_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v041_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v042_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v043_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v044_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 378) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v045_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 378) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v046_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v047_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v048_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v049_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v050_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    base = _mean(b, 504) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v051_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v052_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v053_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v054_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v055_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v056_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v057_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v058_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v059_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v060_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v061_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v062_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v063_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v064_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v065_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v066_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v067_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v068_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v069_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v070_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v071_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v072_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v073_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v074_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v075_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v076_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v077_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v078_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v079_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v080_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v081_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v082_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v083_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v084_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v085_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v086_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v087_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v088_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v089_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v090_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v091_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v092_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v093_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v094_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v095_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v096_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v097_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v098_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v099_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v100_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v101_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 5)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v102_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 5)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v103_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 5)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v104_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 5)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v105_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 5)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v106_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v107_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v108_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v109_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v110_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v111_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v112_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v113_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v114_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v115_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 21)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v116_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v117_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v118_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v119_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v120_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v121_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v122_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v123_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v124_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v125_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 63)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v126_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v127_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v128_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v129_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v130_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 126)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v131_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v132_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v133_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v134_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v135_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v136_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v137_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v138_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v139_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v140_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v141_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v142_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v143_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v144_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v145_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v146_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    base = b * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v147_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    base = b * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v148_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    base = b * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v149_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    base = b * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v150_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 504)
    base = b * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v001_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v002_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v003_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v004_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_5d_jerk_v005_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v006_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v007_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v008_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v009_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_10d_jerk_v010_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v011_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v012_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v013_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v014_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_21d_jerk_v015_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v016_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v017_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v018_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v019_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_42d_jerk_v020_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v021_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v022_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v023_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v024_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_63d_jerk_v025_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v026_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v027_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v028_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v029_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_126d_jerk_v030_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v031_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v032_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v033_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v034_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_189d_jerk_v035_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v036_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v037_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v038_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v039_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_252d_jerk_v040_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v041_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v042_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v043_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v044_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_378d_jerk_v045_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v046_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v047_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v048_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v049_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yld_504d_jerk_v050_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v051_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v052_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v053_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v054_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_5d_jerk_v055_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v056_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v057_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v058_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v059_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_10d_jerk_v060_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v061_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v062_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v063_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v064_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_21d_jerk_v065_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v066_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v067_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v068_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v069_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_42d_jerk_v070_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v071_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v072_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v073_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v074_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_63d_jerk_v075_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v076_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v077_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v078_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v079_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_126d_jerk_v080_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v081_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v082_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v083_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v084_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_189d_jerk_v085_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v086_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v087_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v088_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v089_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_252d_jerk_v090_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v091_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v092_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v093_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v094_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_378d_jerk_v095_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v096_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v097_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v098_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v099_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stab_504d_jerk_v100_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v101_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v102_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v103_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v104_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_5d_jerk_v105_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v106_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v107_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v108_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v109_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_10d_jerk_v110_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v111_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v112_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v113_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v114_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_21d_jerk_v115_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v116_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v117_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v118_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v119_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_42d_jerk_v120_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v121_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v122_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v123_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v124_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_63d_jerk_v125_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v126_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v127_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v128_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v129_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_126d_jerk_v130_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v131_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v132_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v133_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v134_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_189d_jerk_v135_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v136_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v137_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v138_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v139_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_252d_jerk_v140_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v141_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v142_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v143_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v144_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_378d_jerk_v145_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v146_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v147_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v148_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v149_signal,
    f27fyd_f27_fcf_yield_durability_consumer_comp_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_FCF_YIELD_DURABILITY_CONSUMER_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf       = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt      = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq   = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev        = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    cols = {"closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_fcf_yield", "_f27_fcf_yield_stability", "_f27_fcf_compound_quality",)
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
    print(f"OK f27_fcf_yield_durability_consumer_3rd_derivatives_001_150_claude: {n_features} features pass")
