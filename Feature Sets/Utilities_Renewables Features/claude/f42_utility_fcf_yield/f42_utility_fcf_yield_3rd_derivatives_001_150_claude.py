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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


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
def _f42_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan).abs()


def _f42_fcf_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan).abs()
    m = y.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = y.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def _f42_fcf_compound(fcf, marketcap, w):
    y = fcf / marketcap.replace(0, np.nan).abs()
    return y.rolling(w, min_periods=max(1, w // 2)).mean() * np.sqrt(w)

def f42ufy_f42_utility_fcf_yield_yldrawxc5d_jerk_v001_signal(fcf, ev, marketcap, closeadj):
    # rid=1
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * closeadj
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxlc10d_jerk_v002_signal(fcf, ev, marketcap, closeadj):
    # rid=2
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawdc21d_jerk_v003_signal(fcf, ev, marketcap, closeadj):
    # rid=3
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcm42d_jerk_v004_signal(fcf, ev, marketcap, closeadj):
    # rid=4
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcm6363d_jerk_v005_signal(fcf, ev, marketcap, closeadj):
    # rid=5
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcm126126d_jerk_v006_signal(fcf, ev, marketcap, closeadj):
    # rid=6
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcz5d_jerk_v007_signal(fcf, ev, marketcap, closeadj):
    # rid=7
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcr10d_jerk_v008_signal(fcf, ev, marketcap, closeadj):
    # rid=8
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldrawxcr6321d_jerk_v009_signal(fcf, ev, marketcap, closeadj):
    # rid=9
    base = _f42_fcf_yield(fcf, ev)
    trans = base
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxc42d_jerk_v010_signal(fcf, ev, marketcap, closeadj):
    # rid=10
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * closeadj
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxc63d_jerk_v011_signal(fcf, ev, marketcap, closeadj):
    # rid=11
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * closeadj
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxc126d_jerk_v012_signal(fcf, ev, marketcap, closeadj):
    # rid=12
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * closeadj
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxlc5d_jerk_v013_signal(fcf, ev, marketcap, closeadj):
    # rid=13
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxlc10d_jerk_v014_signal(fcf, ev, marketcap, closeadj):
    # rid=14
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxlc21d_jerk_v015_signal(fcf, ev, marketcap, closeadj):
    # rid=15
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeandc42d_jerk_v016_signal(fcf, ev, marketcap, closeadj):
    # rid=16
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeandc63d_jerk_v017_signal(fcf, ev, marketcap, closeadj):
    # rid=17
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeandc126d_jerk_v018_signal(fcf, ev, marketcap, closeadj):
    # rid=18
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm5d_jerk_v019_signal(fcf, ev, marketcap, closeadj):
    # rid=19
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm10d_jerk_v020_signal(fcf, ev, marketcap, closeadj):
    # rid=20
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm21d_jerk_v021_signal(fcf, ev, marketcap, closeadj):
    # rid=21
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm6342d_jerk_v022_signal(fcf, ev, marketcap, closeadj):
    # rid=22
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm6363d_jerk_v023_signal(fcf, ev, marketcap, closeadj):
    # rid=23
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm63126d_jerk_v024_signal(fcf, ev, marketcap, closeadj):
    # rid=24
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm1265d_jerk_v025_signal(fcf, ev, marketcap, closeadj):
    # rid=25
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm12610d_jerk_v026_signal(fcf, ev, marketcap, closeadj):
    # rid=26
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcm12621d_jerk_v027_signal(fcf, ev, marketcap, closeadj):
    # rid=27
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcz42d_jerk_v028_signal(fcf, ev, marketcap, closeadj):
    # rid=28
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcz63d_jerk_v029_signal(fcf, ev, marketcap, closeadj):
    # rid=29
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcz126d_jerk_v030_signal(fcf, ev, marketcap, closeadj):
    # rid=30
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr5d_jerk_v031_signal(fcf, ev, marketcap, closeadj):
    # rid=31
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr10d_jerk_v032_signal(fcf, ev, marketcap, closeadj):
    # rid=32
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr21d_jerk_v033_signal(fcf, ev, marketcap, closeadj):
    # rid=33
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr6342d_jerk_v034_signal(fcf, ev, marketcap, closeadj):
    # rid=34
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr6363d_jerk_v035_signal(fcf, ev, marketcap, closeadj):
    # rid=35
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldmeanxcr63126d_jerk_v036_signal(fcf, ev, marketcap, closeadj):
    # rid=36
    base = _f42_fcf_yield(fcf, ev)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxc5d_jerk_v037_signal(fcf, ev, marketcap, closeadj):
    # rid=37
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * closeadj
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxc10d_jerk_v038_signal(fcf, ev, marketcap, closeadj):
    # rid=38
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * closeadj
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxc21d_jerk_v039_signal(fcf, ev, marketcap, closeadj):
    # rid=39
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * closeadj
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxlc42d_jerk_v040_signal(fcf, ev, marketcap, closeadj):
    # rid=40
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxlc63d_jerk_v041_signal(fcf, ev, marketcap, closeadj):
    # rid=41
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxlc126d_jerk_v042_signal(fcf, ev, marketcap, closeadj):
    # rid=42
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstddc5d_jerk_v043_signal(fcf, ev, marketcap, closeadj):
    # rid=43
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstddc10d_jerk_v044_signal(fcf, ev, marketcap, closeadj):
    # rid=44
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstddc21d_jerk_v045_signal(fcf, ev, marketcap, closeadj):
    # rid=45
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm42d_jerk_v046_signal(fcf, ev, marketcap, closeadj):
    # rid=46
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm63d_jerk_v047_signal(fcf, ev, marketcap, closeadj):
    # rid=47
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm126d_jerk_v048_signal(fcf, ev, marketcap, closeadj):
    # rid=48
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm635d_jerk_v049_signal(fcf, ev, marketcap, closeadj):
    # rid=49
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm6310d_jerk_v050_signal(fcf, ev, marketcap, closeadj):
    # rid=50
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm6321d_jerk_v051_signal(fcf, ev, marketcap, closeadj):
    # rid=51
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm12642d_jerk_v052_signal(fcf, ev, marketcap, closeadj):
    # rid=52
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm12663d_jerk_v053_signal(fcf, ev, marketcap, closeadj):
    # rid=53
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcm126126d_jerk_v054_signal(fcf, ev, marketcap, closeadj):
    # rid=54
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcz5d_jerk_v055_signal(fcf, ev, marketcap, closeadj):
    # rid=55
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcz10d_jerk_v056_signal(fcf, ev, marketcap, closeadj):
    # rid=56
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcz21d_jerk_v057_signal(fcf, ev, marketcap, closeadj):
    # rid=57
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr42d_jerk_v058_signal(fcf, ev, marketcap, closeadj):
    # rid=58
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr63d_jerk_v059_signal(fcf, ev, marketcap, closeadj):
    # rid=59
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr126d_jerk_v060_signal(fcf, ev, marketcap, closeadj):
    # rid=60
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr635d_jerk_v061_signal(fcf, ev, marketcap, closeadj):
    # rid=61
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr6310d_jerk_v062_signal(fcf, ev, marketcap, closeadj):
    # rid=62
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldstdxcr6321d_jerk_v063_signal(fcf, ev, marketcap, closeadj):
    # rid=63
    base = _f42_fcf_yield(fcf, ev)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxc42d_jerk_v064_signal(fcf, ev, marketcap, closeadj):
    # rid=64
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * closeadj
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxc63d_jerk_v065_signal(fcf, ev, marketcap, closeadj):
    # rid=65
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * closeadj
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxc126d_jerk_v066_signal(fcf, ev, marketcap, closeadj):
    # rid=66
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * closeadj
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxlc5d_jerk_v067_signal(fcf, ev, marketcap, closeadj):
    # rid=67
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxlc10d_jerk_v068_signal(fcf, ev, marketcap, closeadj):
    # rid=68
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxlc21d_jerk_v069_signal(fcf, ev, marketcap, closeadj):
    # rid=69
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzdc42d_jerk_v070_signal(fcf, ev, marketcap, closeadj):
    # rid=70
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzdc63d_jerk_v071_signal(fcf, ev, marketcap, closeadj):
    # rid=71
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzdc126d_jerk_v072_signal(fcf, ev, marketcap, closeadj):
    # rid=72
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm5d_jerk_v073_signal(fcf, ev, marketcap, closeadj):
    # rid=73
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm10d_jerk_v074_signal(fcf, ev, marketcap, closeadj):
    # rid=74
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm21d_jerk_v075_signal(fcf, ev, marketcap, closeadj):
    # rid=75
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm6342d_jerk_v076_signal(fcf, ev, marketcap, closeadj):
    # rid=76
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm6363d_jerk_v077_signal(fcf, ev, marketcap, closeadj):
    # rid=77
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm63126d_jerk_v078_signal(fcf, ev, marketcap, closeadj):
    # rid=78
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm1265d_jerk_v079_signal(fcf, ev, marketcap, closeadj):
    # rid=79
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm12610d_jerk_v080_signal(fcf, ev, marketcap, closeadj):
    # rid=80
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcm12621d_jerk_v081_signal(fcf, ev, marketcap, closeadj):
    # rid=81
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcz42d_jerk_v082_signal(fcf, ev, marketcap, closeadj):
    # rid=82
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcz63d_jerk_v083_signal(fcf, ev, marketcap, closeadj):
    # rid=83
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcz126d_jerk_v084_signal(fcf, ev, marketcap, closeadj):
    # rid=84
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr5d_jerk_v085_signal(fcf, ev, marketcap, closeadj):
    # rid=85
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr10d_jerk_v086_signal(fcf, ev, marketcap, closeadj):
    # rid=86
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr21d_jerk_v087_signal(fcf, ev, marketcap, closeadj):
    # rid=87
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr6342d_jerk_v088_signal(fcf, ev, marketcap, closeadj):
    # rid=88
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr6363d_jerk_v089_signal(fcf, ev, marketcap, closeadj):
    # rid=89
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldzxcr63126d_jerk_v090_signal(fcf, ev, marketcap, closeadj):
    # rid=90
    base = _f42_fcf_yield(fcf, ev)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxc5d_jerk_v091_signal(fcf, ev, marketcap, closeadj):
    # rid=91
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * closeadj
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxc10d_jerk_v092_signal(fcf, ev, marketcap, closeadj):
    # rid=92
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * closeadj
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxc21d_jerk_v093_signal(fcf, ev, marketcap, closeadj):
    # rid=93
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * closeadj
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxlc42d_jerk_v094_signal(fcf, ev, marketcap, closeadj):
    # rid=94
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxlc63d_jerk_v095_signal(fcf, ev, marketcap, closeadj):
    # rid=95
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxlc126d_jerk_v096_signal(fcf, ev, marketcap, closeadj):
    # rid=96
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemadc5d_jerk_v097_signal(fcf, ev, marketcap, closeadj):
    # rid=97
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemadc10d_jerk_v098_signal(fcf, ev, marketcap, closeadj):
    # rid=98
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemadc21d_jerk_v099_signal(fcf, ev, marketcap, closeadj):
    # rid=99
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm42d_jerk_v100_signal(fcf, ev, marketcap, closeadj):
    # rid=100
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm63d_jerk_v101_signal(fcf, ev, marketcap, closeadj):
    # rid=101
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm126d_jerk_v102_signal(fcf, ev, marketcap, closeadj):
    # rid=102
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm635d_jerk_v103_signal(fcf, ev, marketcap, closeadj):
    # rid=103
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm6310d_jerk_v104_signal(fcf, ev, marketcap, closeadj):
    # rid=104
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm6321d_jerk_v105_signal(fcf, ev, marketcap, closeadj):
    # rid=105
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm12642d_jerk_v106_signal(fcf, ev, marketcap, closeadj):
    # rid=106
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm12663d_jerk_v107_signal(fcf, ev, marketcap, closeadj):
    # rid=107
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcm126126d_jerk_v108_signal(fcf, ev, marketcap, closeadj):
    # rid=108
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcz5d_jerk_v109_signal(fcf, ev, marketcap, closeadj):
    # rid=109
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcz10d_jerk_v110_signal(fcf, ev, marketcap, closeadj):
    # rid=110
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcz21d_jerk_v111_signal(fcf, ev, marketcap, closeadj):
    # rid=111
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr42d_jerk_v112_signal(fcf, ev, marketcap, closeadj):
    # rid=112
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr63d_jerk_v113_signal(fcf, ev, marketcap, closeadj):
    # rid=113
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr126d_jerk_v114_signal(fcf, ev, marketcap, closeadj):
    # rid=114
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr635d_jerk_v115_signal(fcf, ev, marketcap, closeadj):
    # rid=115
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr6310d_jerk_v116_signal(fcf, ev, marketcap, closeadj):
    # rid=116
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldemaxcr6321d_jerk_v117_signal(fcf, ev, marketcap, closeadj):
    # rid=117
    base = _f42_fcf_yield(fcf, ev)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxc42d_jerk_v118_signal(fcf, ev, marketcap, closeadj):
    # rid=118
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * closeadj
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxlc63d_jerk_v119_signal(fcf, ev, marketcap, closeadj):
    # rid=119
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsdc126d_jerk_v120_signal(fcf, ev, marketcap, closeadj):
    # rid=120
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcm5d_jerk_v121_signal(fcf, ev, marketcap, closeadj):
    # rid=121
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcm6310d_jerk_v122_signal(fcf, ev, marketcap, closeadj):
    # rid=122
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcm12621d_jerk_v123_signal(fcf, ev, marketcap, closeadj):
    # rid=123
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcz42d_jerk_v124_signal(fcf, ev, marketcap, closeadj):
    # rid=124
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcr63d_jerk_v125_signal(fcf, ev, marketcap, closeadj):
    # rid=125
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldabsxcr63126d_jerk_v126_signal(fcf, ev, marketcap, closeadj):
    # rid=126
    base = _f42_fcf_yield(fcf, ev)
    trans = base.abs()
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxc5d_jerk_v127_signal(fcf, ev, marketcap, closeadj):
    # rid=127
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxlc10d_jerk_v128_signal(fcf, ev, marketcap, closeadj):
    # rid=128
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogdc21d_jerk_v129_signal(fcf, ev, marketcap, closeadj):
    # rid=129
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcm42d_jerk_v130_signal(fcf, ev, marketcap, closeadj):
    # rid=130
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcm6363d_jerk_v131_signal(fcf, ev, marketcap, closeadj):
    # rid=131
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcm126126d_jerk_v132_signal(fcf, ev, marketcap, closeadj):
    # rid=132
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcz5d_jerk_v133_signal(fcf, ev, marketcap, closeadj):
    # rid=133
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcr10d_jerk_v134_signal(fcf, ev, marketcap, closeadj):
    # rid=134
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldlogxcr6321d_jerk_v135_signal(fcf, ev, marketcap, closeadj):
    # rid=135
    base = _f42_fcf_yield(fcf, ev)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxc42d_jerk_v136_signal(fcf, ev, marketcap, closeadj):
    # rid=136
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * closeadj
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxlc63d_jerk_v137_signal(fcf, ev, marketcap, closeadj):
    # rid=137
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsigndc126d_jerk_v138_signal(fcf, ev, marketcap, closeadj):
    # rid=138
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcm5d_jerk_v139_signal(fcf, ev, marketcap, closeadj):
    # rid=139
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcm6310d_jerk_v140_signal(fcf, ev, marketcap, closeadj):
    # rid=140
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcm12621d_jerk_v141_signal(fcf, ev, marketcap, closeadj):
    # rid=141
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcz42d_jerk_v142_signal(fcf, ev, marketcap, closeadj):
    # rid=142
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * _z(closeadj, 63)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcr63d_jerk_v143_signal(fcf, ev, marketcap, closeadj):
    # rid=143
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(21)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsignxcr63126d_jerk_v144_signal(fcf, ev, marketcap, closeadj):
    # rid=144
    base = _f42_fcf_yield(fcf, ev)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(63)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqxc5d_jerk_v145_signal(fcf, ev, marketcap, closeadj):
    # rid=145
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans * closeadj
    result = _jerk(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqxlc10d_jerk_v146_signal(fcf, ev, marketcap, closeadj):
    # rid=146
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans * np.log(closeadj)
    result = _jerk(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqdc21d_jerk_v147_signal(fcf, ev, marketcap, closeadj):
    # rid=147
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _jerk(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqxcm42d_jerk_v148_signal(fcf, ev, marketcap, closeadj):
    # rid=148
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _jerk(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqxcm6363d_jerk_v149_signal(fcf, ev, marketcap, closeadj):
    # rid=149
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _jerk(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42ufy_f42_utility_fcf_yield_yldsqxcm126126d_jerk_v150_signal(fcf, ev, marketcap, closeadj):
    # rid=150
    base = _f42_fcf_yield(fcf, ev)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _jerk(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42ufy_f42_utility_fcf_yield_yldrawxc5d_jerk_v001_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxlc10d_jerk_v002_signal,
    f42ufy_f42_utility_fcf_yield_yldrawdc21d_jerk_v003_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcm42d_jerk_v004_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcm6363d_jerk_v005_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcm126126d_jerk_v006_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcz5d_jerk_v007_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcr10d_jerk_v008_signal,
    f42ufy_f42_utility_fcf_yield_yldrawxcr6321d_jerk_v009_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxc42d_jerk_v010_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxc63d_jerk_v011_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxc126d_jerk_v012_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxlc5d_jerk_v013_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxlc10d_jerk_v014_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxlc21d_jerk_v015_signal,
    f42ufy_f42_utility_fcf_yield_yldmeandc42d_jerk_v016_signal,
    f42ufy_f42_utility_fcf_yield_yldmeandc63d_jerk_v017_signal,
    f42ufy_f42_utility_fcf_yield_yldmeandc126d_jerk_v018_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm5d_jerk_v019_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm10d_jerk_v020_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm21d_jerk_v021_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm6342d_jerk_v022_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm6363d_jerk_v023_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm63126d_jerk_v024_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm1265d_jerk_v025_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm12610d_jerk_v026_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcm12621d_jerk_v027_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcz42d_jerk_v028_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcz63d_jerk_v029_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcz126d_jerk_v030_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr5d_jerk_v031_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr10d_jerk_v032_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr21d_jerk_v033_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr6342d_jerk_v034_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr6363d_jerk_v035_signal,
    f42ufy_f42_utility_fcf_yield_yldmeanxcr63126d_jerk_v036_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxc5d_jerk_v037_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxc10d_jerk_v038_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxc21d_jerk_v039_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxlc42d_jerk_v040_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxlc63d_jerk_v041_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxlc126d_jerk_v042_signal,
    f42ufy_f42_utility_fcf_yield_yldstddc5d_jerk_v043_signal,
    f42ufy_f42_utility_fcf_yield_yldstddc10d_jerk_v044_signal,
    f42ufy_f42_utility_fcf_yield_yldstddc21d_jerk_v045_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm42d_jerk_v046_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm63d_jerk_v047_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm126d_jerk_v048_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm635d_jerk_v049_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm6310d_jerk_v050_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm6321d_jerk_v051_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm12642d_jerk_v052_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm12663d_jerk_v053_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcm126126d_jerk_v054_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcz5d_jerk_v055_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcz10d_jerk_v056_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcz21d_jerk_v057_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr42d_jerk_v058_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr63d_jerk_v059_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr126d_jerk_v060_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr635d_jerk_v061_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr6310d_jerk_v062_signal,
    f42ufy_f42_utility_fcf_yield_yldstdxcr6321d_jerk_v063_signal,
    f42ufy_f42_utility_fcf_yield_yldzxc42d_jerk_v064_signal,
    f42ufy_f42_utility_fcf_yield_yldzxc63d_jerk_v065_signal,
    f42ufy_f42_utility_fcf_yield_yldzxc126d_jerk_v066_signal,
    f42ufy_f42_utility_fcf_yield_yldzxlc5d_jerk_v067_signal,
    f42ufy_f42_utility_fcf_yield_yldzxlc10d_jerk_v068_signal,
    f42ufy_f42_utility_fcf_yield_yldzxlc21d_jerk_v069_signal,
    f42ufy_f42_utility_fcf_yield_yldzdc42d_jerk_v070_signal,
    f42ufy_f42_utility_fcf_yield_yldzdc63d_jerk_v071_signal,
    f42ufy_f42_utility_fcf_yield_yldzdc126d_jerk_v072_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm5d_jerk_v073_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm10d_jerk_v074_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm21d_jerk_v075_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm6342d_jerk_v076_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm6363d_jerk_v077_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm63126d_jerk_v078_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm1265d_jerk_v079_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm12610d_jerk_v080_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcm12621d_jerk_v081_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcz42d_jerk_v082_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcz63d_jerk_v083_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcz126d_jerk_v084_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr5d_jerk_v085_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr10d_jerk_v086_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr21d_jerk_v087_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr6342d_jerk_v088_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr6363d_jerk_v089_signal,
    f42ufy_f42_utility_fcf_yield_yldzxcr63126d_jerk_v090_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxc5d_jerk_v091_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxc10d_jerk_v092_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxc21d_jerk_v093_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxlc42d_jerk_v094_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxlc63d_jerk_v095_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxlc126d_jerk_v096_signal,
    f42ufy_f42_utility_fcf_yield_yldemadc5d_jerk_v097_signal,
    f42ufy_f42_utility_fcf_yield_yldemadc10d_jerk_v098_signal,
    f42ufy_f42_utility_fcf_yield_yldemadc21d_jerk_v099_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm42d_jerk_v100_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm63d_jerk_v101_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm126d_jerk_v102_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm635d_jerk_v103_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm6310d_jerk_v104_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm6321d_jerk_v105_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm12642d_jerk_v106_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm12663d_jerk_v107_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcm126126d_jerk_v108_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcz5d_jerk_v109_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcz10d_jerk_v110_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcz21d_jerk_v111_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr42d_jerk_v112_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr63d_jerk_v113_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr126d_jerk_v114_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr635d_jerk_v115_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr6310d_jerk_v116_signal,
    f42ufy_f42_utility_fcf_yield_yldemaxcr6321d_jerk_v117_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxc42d_jerk_v118_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxlc63d_jerk_v119_signal,
    f42ufy_f42_utility_fcf_yield_yldabsdc126d_jerk_v120_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcm5d_jerk_v121_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcm6310d_jerk_v122_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcm12621d_jerk_v123_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcz42d_jerk_v124_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcr63d_jerk_v125_signal,
    f42ufy_f42_utility_fcf_yield_yldabsxcr63126d_jerk_v126_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxc5d_jerk_v127_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxlc10d_jerk_v128_signal,
    f42ufy_f42_utility_fcf_yield_yldlogdc21d_jerk_v129_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcm42d_jerk_v130_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcm6363d_jerk_v131_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcm126126d_jerk_v132_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcz5d_jerk_v133_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcr10d_jerk_v134_signal,
    f42ufy_f42_utility_fcf_yield_yldlogxcr6321d_jerk_v135_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxc42d_jerk_v136_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxlc63d_jerk_v137_signal,
    f42ufy_f42_utility_fcf_yield_yldsigndc126d_jerk_v138_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcm5d_jerk_v139_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcm6310d_jerk_v140_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcm12621d_jerk_v141_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcz42d_jerk_v142_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcr63d_jerk_v143_signal,
    f42ufy_f42_utility_fcf_yield_yldsignxcr63126d_jerk_v144_signal,
    f42ufy_f42_utility_fcf_yield_yldsqxc5d_jerk_v145_signal,
    f42ufy_f42_utility_fcf_yield_yldsqxlc10d_jerk_v146_signal,
    f42ufy_f42_utility_fcf_yield_yldsqdc21d_jerk_v147_signal,
    f42ufy_f42_utility_fcf_yield_yldsqxcm42d_jerk_v148_signal,
    f42ufy_f42_utility_fcf_yield_yldsqxcm6363d_jerk_v149_signal,
    f42ufy_f42_utility_fcf_yield_yldsqxcm126126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_UTILITY_FCF_YIELD_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f42_fcf_yield", "_f42_fcf_stability", "_f42_fcf_compound")
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
    print(f"OK f42_utility_fcf_yield_3rd_derivatives_001_150_claude: {n_features} features pass")
