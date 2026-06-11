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


# ===== folder domain primitives =====
def _f41_roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def _f41_roic_compound(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean() * np.sqrt(w)


def _f41_roic_quality(roic, roa, w):
    spread = roic - roa
    return spread.rolling(w, min_periods=max(1, w // 2)).mean()

def f41urs_f41_utility_roic_stability_stabrawxc5d_slope_v001_signal(roic, roa, roe, closeadj):
    # rid=1
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxlc10d_slope_v002_signal(roic, roa, roe, closeadj):
    # rid=2
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawdc21d_slope_v003_signal(roic, roa, roe, closeadj):
    # rid=3
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm42d_slope_v004_signal(roic, roa, roe, closeadj):
    # rid=4
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm6363d_slope_v005_signal(roic, roa, roe, closeadj):
    # rid=5
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm126126d_slope_v006_signal(roic, roa, roe, closeadj):
    # rid=6
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcz5d_slope_v007_signal(roic, roa, roe, closeadj):
    # rid=7
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcr10d_slope_v008_signal(roic, roa, roe, closeadj):
    # rid=8
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcr6321d_slope_v009_signal(roic, roa, roe, closeadj):
    # rid=9
    base = _f41_roic_stability(roic, 21)
    trans = base
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc42d_slope_v010_signal(roic, roa, roe, closeadj):
    # rid=10
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc63d_slope_v011_signal(roic, roa, roe, closeadj):
    # rid=11
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc126d_slope_v012_signal(roic, roa, roe, closeadj):
    # rid=12
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc5d_slope_v013_signal(roic, roa, roe, closeadj):
    # rid=13
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc10d_slope_v014_signal(roic, roa, roe, closeadj):
    # rid=14
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc21d_slope_v015_signal(roic, roa, roe, closeadj):
    # rid=15
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc42d_slope_v016_signal(roic, roa, roe, closeadj):
    # rid=16
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc63d_slope_v017_signal(roic, roa, roe, closeadj):
    # rid=17
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc126d_slope_v018_signal(roic, roa, roe, closeadj):
    # rid=18
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm5d_slope_v019_signal(roic, roa, roe, closeadj):
    # rid=19
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm10d_slope_v020_signal(roic, roa, roe, closeadj):
    # rid=20
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm21d_slope_v021_signal(roic, roa, roe, closeadj):
    # rid=21
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm6342d_slope_v022_signal(roic, roa, roe, closeadj):
    # rid=22
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm6363d_slope_v023_signal(roic, roa, roe, closeadj):
    # rid=23
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm63126d_slope_v024_signal(roic, roa, roe, closeadj):
    # rid=24
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm1265d_slope_v025_signal(roic, roa, roe, closeadj):
    # rid=25
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm12610d_slope_v026_signal(roic, roa, roe, closeadj):
    # rid=26
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm12621d_slope_v027_signal(roic, roa, roe, closeadj):
    # rid=27
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz42d_slope_v028_signal(roic, roa, roe, closeadj):
    # rid=28
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz63d_slope_v029_signal(roic, roa, roe, closeadj):
    # rid=29
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz126d_slope_v030_signal(roic, roa, roe, closeadj):
    # rid=30
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr5d_slope_v031_signal(roic, roa, roe, closeadj):
    # rid=31
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr10d_slope_v032_signal(roic, roa, roe, closeadj):
    # rid=32
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr21d_slope_v033_signal(roic, roa, roe, closeadj):
    # rid=33
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr6342d_slope_v034_signal(roic, roa, roe, closeadj):
    # rid=34
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr6363d_slope_v035_signal(roic, roa, roe, closeadj):
    # rid=35
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr63126d_slope_v036_signal(roic, roa, roe, closeadj):
    # rid=36
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc5d_slope_v037_signal(roic, roa, roe, closeadj):
    # rid=37
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc10d_slope_v038_signal(roic, roa, roe, closeadj):
    # rid=38
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc21d_slope_v039_signal(roic, roa, roe, closeadj):
    # rid=39
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc42d_slope_v040_signal(roic, roa, roe, closeadj):
    # rid=40
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc63d_slope_v041_signal(roic, roa, roe, closeadj):
    # rid=41
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc126d_slope_v042_signal(roic, roa, roe, closeadj):
    # rid=42
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc5d_slope_v043_signal(roic, roa, roe, closeadj):
    # rid=43
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc10d_slope_v044_signal(roic, roa, roe, closeadj):
    # rid=44
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc21d_slope_v045_signal(roic, roa, roe, closeadj):
    # rid=45
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm42d_slope_v046_signal(roic, roa, roe, closeadj):
    # rid=46
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm63d_slope_v047_signal(roic, roa, roe, closeadj):
    # rid=47
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm126d_slope_v048_signal(roic, roa, roe, closeadj):
    # rid=48
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm635d_slope_v049_signal(roic, roa, roe, closeadj):
    # rid=49
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm6310d_slope_v050_signal(roic, roa, roe, closeadj):
    # rid=50
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm6321d_slope_v051_signal(roic, roa, roe, closeadj):
    # rid=51
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm12642d_slope_v052_signal(roic, roa, roe, closeadj):
    # rid=52
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm12663d_slope_v053_signal(roic, roa, roe, closeadj):
    # rid=53
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm126126d_slope_v054_signal(roic, roa, roe, closeadj):
    # rid=54
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz5d_slope_v055_signal(roic, roa, roe, closeadj):
    # rid=55
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz10d_slope_v056_signal(roic, roa, roe, closeadj):
    # rid=56
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz21d_slope_v057_signal(roic, roa, roe, closeadj):
    # rid=57
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr42d_slope_v058_signal(roic, roa, roe, closeadj):
    # rid=58
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr63d_slope_v059_signal(roic, roa, roe, closeadj):
    # rid=59
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr126d_slope_v060_signal(roic, roa, roe, closeadj):
    # rid=60
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr635d_slope_v061_signal(roic, roa, roe, closeadj):
    # rid=61
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr6310d_slope_v062_signal(roic, roa, roe, closeadj):
    # rid=62
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr6321d_slope_v063_signal(roic, roa, roe, closeadj):
    # rid=63
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc42d_slope_v064_signal(roic, roa, roe, closeadj):
    # rid=64
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc63d_slope_v065_signal(roic, roa, roe, closeadj):
    # rid=65
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc126d_slope_v066_signal(roic, roa, roe, closeadj):
    # rid=66
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc5d_slope_v067_signal(roic, roa, roe, closeadj):
    # rid=67
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc10d_slope_v068_signal(roic, roa, roe, closeadj):
    # rid=68
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc21d_slope_v069_signal(roic, roa, roe, closeadj):
    # rid=69
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc42d_slope_v070_signal(roic, roa, roe, closeadj):
    # rid=70
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc63d_slope_v071_signal(roic, roa, roe, closeadj):
    # rid=71
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc126d_slope_v072_signal(roic, roa, roe, closeadj):
    # rid=72
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm5d_slope_v073_signal(roic, roa, roe, closeadj):
    # rid=73
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm10d_slope_v074_signal(roic, roa, roe, closeadj):
    # rid=74
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm21d_slope_v075_signal(roic, roa, roe, closeadj):
    # rid=75
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm6342d_slope_v076_signal(roic, roa, roe, closeadj):
    # rid=76
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm6363d_slope_v077_signal(roic, roa, roe, closeadj):
    # rid=77
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm63126d_slope_v078_signal(roic, roa, roe, closeadj):
    # rid=78
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm1265d_slope_v079_signal(roic, roa, roe, closeadj):
    # rid=79
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm12610d_slope_v080_signal(roic, roa, roe, closeadj):
    # rid=80
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm12621d_slope_v081_signal(roic, roa, roe, closeadj):
    # rid=81
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz42d_slope_v082_signal(roic, roa, roe, closeadj):
    # rid=82
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz63d_slope_v083_signal(roic, roa, roe, closeadj):
    # rid=83
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz126d_slope_v084_signal(roic, roa, roe, closeadj):
    # rid=84
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr5d_slope_v085_signal(roic, roa, roe, closeadj):
    # rid=85
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr10d_slope_v086_signal(roic, roa, roe, closeadj):
    # rid=86
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr21d_slope_v087_signal(roic, roa, roe, closeadj):
    # rid=87
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr6342d_slope_v088_signal(roic, roa, roe, closeadj):
    # rid=88
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr6363d_slope_v089_signal(roic, roa, roe, closeadj):
    # rid=89
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr63126d_slope_v090_signal(roic, roa, roe, closeadj):
    # rid=90
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc5d_slope_v091_signal(roic, roa, roe, closeadj):
    # rid=91
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc10d_slope_v092_signal(roic, roa, roe, closeadj):
    # rid=92
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc21d_slope_v093_signal(roic, roa, roe, closeadj):
    # rid=93
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc42d_slope_v094_signal(roic, roa, roe, closeadj):
    # rid=94
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc63d_slope_v095_signal(roic, roa, roe, closeadj):
    # rid=95
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc126d_slope_v096_signal(roic, roa, roe, closeadj):
    # rid=96
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc5d_slope_v097_signal(roic, roa, roe, closeadj):
    # rid=97
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc10d_slope_v098_signal(roic, roa, roe, closeadj):
    # rid=98
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc21d_slope_v099_signal(roic, roa, roe, closeadj):
    # rid=99
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm42d_slope_v100_signal(roic, roa, roe, closeadj):
    # rid=100
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm63d_slope_v101_signal(roic, roa, roe, closeadj):
    # rid=101
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm126d_slope_v102_signal(roic, roa, roe, closeadj):
    # rid=102
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm635d_slope_v103_signal(roic, roa, roe, closeadj):
    # rid=103
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm6310d_slope_v104_signal(roic, roa, roe, closeadj):
    # rid=104
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm6321d_slope_v105_signal(roic, roa, roe, closeadj):
    # rid=105
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm12642d_slope_v106_signal(roic, roa, roe, closeadj):
    # rid=106
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm12663d_slope_v107_signal(roic, roa, roe, closeadj):
    # rid=107
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm126126d_slope_v108_signal(roic, roa, roe, closeadj):
    # rid=108
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz5d_slope_v109_signal(roic, roa, roe, closeadj):
    # rid=109
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz10d_slope_v110_signal(roic, roa, roe, closeadj):
    # rid=110
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz21d_slope_v111_signal(roic, roa, roe, closeadj):
    # rid=111
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr42d_slope_v112_signal(roic, roa, roe, closeadj):
    # rid=112
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr63d_slope_v113_signal(roic, roa, roe, closeadj):
    # rid=113
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr126d_slope_v114_signal(roic, roa, roe, closeadj):
    # rid=114
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr635d_slope_v115_signal(roic, roa, roe, closeadj):
    # rid=115
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr6310d_slope_v116_signal(roic, roa, roe, closeadj):
    # rid=116
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr6321d_slope_v117_signal(roic, roa, roe, closeadj):
    # rid=117
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxc42d_slope_v118_signal(roic, roa, roe, closeadj):
    # rid=118
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxlc63d_slope_v119_signal(roic, roa, roe, closeadj):
    # rid=119
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsdc126d_slope_v120_signal(roic, roa, roe, closeadj):
    # rid=120
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm5d_slope_v121_signal(roic, roa, roe, closeadj):
    # rid=121
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm6310d_slope_v122_signal(roic, roa, roe, closeadj):
    # rid=122
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm12621d_slope_v123_signal(roic, roa, roe, closeadj):
    # rid=123
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcz42d_slope_v124_signal(roic, roa, roe, closeadj):
    # rid=124
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcr63d_slope_v125_signal(roic, roa, roe, closeadj):
    # rid=125
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcr63126d_slope_v126_signal(roic, roa, roe, closeadj):
    # rid=126
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxc5d_slope_v127_signal(roic, roa, roe, closeadj):
    # rid=127
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxlc10d_slope_v128_signal(roic, roa, roe, closeadj):
    # rid=128
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogdc21d_slope_v129_signal(roic, roa, roe, closeadj):
    # rid=129
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm42d_slope_v130_signal(roic, roa, roe, closeadj):
    # rid=130
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm6363d_slope_v131_signal(roic, roa, roe, closeadj):
    # rid=131
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm126126d_slope_v132_signal(roic, roa, roe, closeadj):
    # rid=132
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcz5d_slope_v133_signal(roic, roa, roe, closeadj):
    # rid=133
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcr10d_slope_v134_signal(roic, roa, roe, closeadj):
    # rid=134
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcr6321d_slope_v135_signal(roic, roa, roe, closeadj):
    # rid=135
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxc42d_slope_v136_signal(roic, roa, roe, closeadj):
    # rid=136
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxlc63d_slope_v137_signal(roic, roa, roe, closeadj):
    # rid=137
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsigndc126d_slope_v138_signal(roic, roa, roe, closeadj):
    # rid=138
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm5d_slope_v139_signal(roic, roa, roe, closeadj):
    # rid=139
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm6310d_slope_v140_signal(roic, roa, roe, closeadj):
    # rid=140
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm12621d_slope_v141_signal(roic, roa, roe, closeadj):
    # rid=141
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcz42d_slope_v142_signal(roic, roa, roe, closeadj):
    # rid=142
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcr63d_slope_v143_signal(roic, roa, roe, closeadj):
    # rid=143
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcr63126d_slope_v144_signal(roic, roa, roe, closeadj):
    # rid=144
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxc5d_slope_v145_signal(roic, roa, roe, closeadj):
    # rid=145
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxlc10d_slope_v146_signal(roic, roa, roe, closeadj):
    # rid=146
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqdc21d_slope_v147_signal(roic, roa, roe, closeadj):
    # rid=147
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm42d_slope_v148_signal(roic, roa, roe, closeadj):
    # rid=148
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm6363d_slope_v149_signal(roic, roa, roe, closeadj):
    # rid=149
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm126126d_slope_v150_signal(roic, roa, roe, closeadj):
    # rid=150
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41urs_f41_utility_roic_stability_stabrawxc5d_slope_v001_signal,
    f41urs_f41_utility_roic_stability_stabrawxlc10d_slope_v002_signal,
    f41urs_f41_utility_roic_stability_stabrawdc21d_slope_v003_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm42d_slope_v004_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm6363d_slope_v005_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm126126d_slope_v006_signal,
    f41urs_f41_utility_roic_stability_stabrawxcz5d_slope_v007_signal,
    f41urs_f41_utility_roic_stability_stabrawxcr10d_slope_v008_signal,
    f41urs_f41_utility_roic_stability_stabrawxcr6321d_slope_v009_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc42d_slope_v010_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc63d_slope_v011_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc126d_slope_v012_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc5d_slope_v013_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc10d_slope_v014_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc21d_slope_v015_signal,
    f41urs_f41_utility_roic_stability_stabmeandc42d_slope_v016_signal,
    f41urs_f41_utility_roic_stability_stabmeandc63d_slope_v017_signal,
    f41urs_f41_utility_roic_stability_stabmeandc126d_slope_v018_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm5d_slope_v019_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm10d_slope_v020_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm21d_slope_v021_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm6342d_slope_v022_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm6363d_slope_v023_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm63126d_slope_v024_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm1265d_slope_v025_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm12610d_slope_v026_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm12621d_slope_v027_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz42d_slope_v028_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz63d_slope_v029_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz126d_slope_v030_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr5d_slope_v031_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr10d_slope_v032_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr21d_slope_v033_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr6342d_slope_v034_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr6363d_slope_v035_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr63126d_slope_v036_signal,
    f41urs_f41_utility_roic_stability_stabstdxc5d_slope_v037_signal,
    f41urs_f41_utility_roic_stability_stabstdxc10d_slope_v038_signal,
    f41urs_f41_utility_roic_stability_stabstdxc21d_slope_v039_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc42d_slope_v040_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc63d_slope_v041_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc126d_slope_v042_signal,
    f41urs_f41_utility_roic_stability_stabstddc5d_slope_v043_signal,
    f41urs_f41_utility_roic_stability_stabstddc10d_slope_v044_signal,
    f41urs_f41_utility_roic_stability_stabstddc21d_slope_v045_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm42d_slope_v046_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm63d_slope_v047_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm126d_slope_v048_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm635d_slope_v049_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm6310d_slope_v050_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm6321d_slope_v051_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm12642d_slope_v052_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm12663d_slope_v053_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm126126d_slope_v054_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz5d_slope_v055_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz10d_slope_v056_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz21d_slope_v057_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr42d_slope_v058_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr63d_slope_v059_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr126d_slope_v060_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr635d_slope_v061_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr6310d_slope_v062_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr6321d_slope_v063_signal,
    f41urs_f41_utility_roic_stability_stabzxc42d_slope_v064_signal,
    f41urs_f41_utility_roic_stability_stabzxc63d_slope_v065_signal,
    f41urs_f41_utility_roic_stability_stabzxc126d_slope_v066_signal,
    f41urs_f41_utility_roic_stability_stabzxlc5d_slope_v067_signal,
    f41urs_f41_utility_roic_stability_stabzxlc10d_slope_v068_signal,
    f41urs_f41_utility_roic_stability_stabzxlc21d_slope_v069_signal,
    f41urs_f41_utility_roic_stability_stabzdc42d_slope_v070_signal,
    f41urs_f41_utility_roic_stability_stabzdc63d_slope_v071_signal,
    f41urs_f41_utility_roic_stability_stabzdc126d_slope_v072_signal,
    f41urs_f41_utility_roic_stability_stabzxcm5d_slope_v073_signal,
    f41urs_f41_utility_roic_stability_stabzxcm10d_slope_v074_signal,
    f41urs_f41_utility_roic_stability_stabzxcm21d_slope_v075_signal,
    f41urs_f41_utility_roic_stability_stabzxcm6342d_slope_v076_signal,
    f41urs_f41_utility_roic_stability_stabzxcm6363d_slope_v077_signal,
    f41urs_f41_utility_roic_stability_stabzxcm63126d_slope_v078_signal,
    f41urs_f41_utility_roic_stability_stabzxcm1265d_slope_v079_signal,
    f41urs_f41_utility_roic_stability_stabzxcm12610d_slope_v080_signal,
    f41urs_f41_utility_roic_stability_stabzxcm12621d_slope_v081_signal,
    f41urs_f41_utility_roic_stability_stabzxcz42d_slope_v082_signal,
    f41urs_f41_utility_roic_stability_stabzxcz63d_slope_v083_signal,
    f41urs_f41_utility_roic_stability_stabzxcz126d_slope_v084_signal,
    f41urs_f41_utility_roic_stability_stabzxcr5d_slope_v085_signal,
    f41urs_f41_utility_roic_stability_stabzxcr10d_slope_v086_signal,
    f41urs_f41_utility_roic_stability_stabzxcr21d_slope_v087_signal,
    f41urs_f41_utility_roic_stability_stabzxcr6342d_slope_v088_signal,
    f41urs_f41_utility_roic_stability_stabzxcr6363d_slope_v089_signal,
    f41urs_f41_utility_roic_stability_stabzxcr63126d_slope_v090_signal,
    f41urs_f41_utility_roic_stability_stabemaxc5d_slope_v091_signal,
    f41urs_f41_utility_roic_stability_stabemaxc10d_slope_v092_signal,
    f41urs_f41_utility_roic_stability_stabemaxc21d_slope_v093_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc42d_slope_v094_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc63d_slope_v095_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc126d_slope_v096_signal,
    f41urs_f41_utility_roic_stability_stabemadc5d_slope_v097_signal,
    f41urs_f41_utility_roic_stability_stabemadc10d_slope_v098_signal,
    f41urs_f41_utility_roic_stability_stabemadc21d_slope_v099_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm42d_slope_v100_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm63d_slope_v101_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm126d_slope_v102_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm635d_slope_v103_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm6310d_slope_v104_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm6321d_slope_v105_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm12642d_slope_v106_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm12663d_slope_v107_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm126126d_slope_v108_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz5d_slope_v109_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz10d_slope_v110_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz21d_slope_v111_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr42d_slope_v112_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr63d_slope_v113_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr126d_slope_v114_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr635d_slope_v115_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr6310d_slope_v116_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr6321d_slope_v117_signal,
    f41urs_f41_utility_roic_stability_stababsxc42d_slope_v118_signal,
    f41urs_f41_utility_roic_stability_stababsxlc63d_slope_v119_signal,
    f41urs_f41_utility_roic_stability_stababsdc126d_slope_v120_signal,
    f41urs_f41_utility_roic_stability_stababsxcm5d_slope_v121_signal,
    f41urs_f41_utility_roic_stability_stababsxcm6310d_slope_v122_signal,
    f41urs_f41_utility_roic_stability_stababsxcm12621d_slope_v123_signal,
    f41urs_f41_utility_roic_stability_stababsxcz42d_slope_v124_signal,
    f41urs_f41_utility_roic_stability_stababsxcr63d_slope_v125_signal,
    f41urs_f41_utility_roic_stability_stababsxcr63126d_slope_v126_signal,
    f41urs_f41_utility_roic_stability_stablogxc5d_slope_v127_signal,
    f41urs_f41_utility_roic_stability_stablogxlc10d_slope_v128_signal,
    f41urs_f41_utility_roic_stability_stablogdc21d_slope_v129_signal,
    f41urs_f41_utility_roic_stability_stablogxcm42d_slope_v130_signal,
    f41urs_f41_utility_roic_stability_stablogxcm6363d_slope_v131_signal,
    f41urs_f41_utility_roic_stability_stablogxcm126126d_slope_v132_signal,
    f41urs_f41_utility_roic_stability_stablogxcz5d_slope_v133_signal,
    f41urs_f41_utility_roic_stability_stablogxcr10d_slope_v134_signal,
    f41urs_f41_utility_roic_stability_stablogxcr6321d_slope_v135_signal,
    f41urs_f41_utility_roic_stability_stabsignxc42d_slope_v136_signal,
    f41urs_f41_utility_roic_stability_stabsignxlc63d_slope_v137_signal,
    f41urs_f41_utility_roic_stability_stabsigndc126d_slope_v138_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm5d_slope_v139_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm6310d_slope_v140_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm12621d_slope_v141_signal,
    f41urs_f41_utility_roic_stability_stabsignxcz42d_slope_v142_signal,
    f41urs_f41_utility_roic_stability_stabsignxcr63d_slope_v143_signal,
    f41urs_f41_utility_roic_stability_stabsignxcr63126d_slope_v144_signal,
    f41urs_f41_utility_roic_stability_stabsqxc5d_slope_v145_signal,
    f41urs_f41_utility_roic_stability_stabsqxlc10d_slope_v146_signal,
    f41urs_f41_utility_roic_stability_stabsqdc21d_slope_v147_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm42d_slope_v148_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm6363d_slope_v149_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm126126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_UTILITY_ROIC_STABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f41_roic_stability", "_f41_roic_compound", "_f41_roic_quality")
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
    print(f"OK f41_utility_roic_stability_2nd_derivatives_001_150_claude: {n_features} features pass")
