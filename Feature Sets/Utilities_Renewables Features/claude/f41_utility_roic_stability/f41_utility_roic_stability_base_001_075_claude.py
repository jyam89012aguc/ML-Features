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

def f41urs_f41_utility_roic_stability_stabrawxc_base_v001_signal(roic, roa, roe, closeadj):
    # rid=1
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxlc_base_v002_signal(roic, roa, roe, closeadj):
    # rid=2
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawdc_base_v003_signal(roic, roa, roe, closeadj):
    # rid=3
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm_base_v004_signal(roic, roa, roe, closeadj):
    # rid=4
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm63_base_v005_signal(roic, roa, roe, closeadj):
    # rid=5
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcm126_base_v006_signal(roic, roa, roe, closeadj):
    # rid=6
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcz_base_v007_signal(roic, roa, roe, closeadj):
    # rid=7
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcr_base_v008_signal(roic, roa, roe, closeadj):
    # rid=8
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabrawxcr63_base_v009_signal(roic, roa, roe, closeadj):
    # rid=9
    base = _f41_roic_stability(roic, 21)
    trans = base
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc_base_v010_signal(roic, roa, roe, closeadj):
    # rid=10
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc_base_v011_signal(roic, roa, roe, closeadj):
    # rid=11
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxc_base_v012_signal(roic, roa, roe, closeadj):
    # rid=12
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc_base_v013_signal(roic, roa, roe, closeadj):
    # rid=13
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc_base_v014_signal(roic, roa, roe, closeadj):
    # rid=14
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxlc_base_v015_signal(roic, roa, roe, closeadj):
    # rid=15
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc_base_v016_signal(roic, roa, roe, closeadj):
    # rid=16
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc_base_v017_signal(roic, roa, roe, closeadj):
    # rid=17
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeandc_base_v018_signal(roic, roa, roe, closeadj):
    # rid=18
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm_base_v019_signal(roic, roa, roe, closeadj):
    # rid=19
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm_base_v020_signal(roic, roa, roe, closeadj):
    # rid=20
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm_base_v021_signal(roic, roa, roe, closeadj):
    # rid=21
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v022_signal(roic, roa, roe, closeadj):
    # rid=22
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v023_signal(roic, roa, roe, closeadj):
    # rid=23
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v024_signal(roic, roa, roe, closeadj):
    # rid=24
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v025_signal(roic, roa, roe, closeadj):
    # rid=25
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v026_signal(roic, roa, roe, closeadj):
    # rid=26
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v027_signal(roic, roa, roe, closeadj):
    # rid=27
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz_base_v028_signal(roic, roa, roe, closeadj):
    # rid=28
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz_base_v029_signal(roic, roa, roe, closeadj):
    # rid=29
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcz_base_v030_signal(roic, roa, roe, closeadj):
    # rid=30
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr_base_v031_signal(roic, roa, roe, closeadj):
    # rid=31
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr_base_v032_signal(roic, roa, roe, closeadj):
    # rid=32
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr_base_v033_signal(roic, roa, roe, closeadj):
    # rid=33
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v034_signal(roic, roa, roe, closeadj):
    # rid=34
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v035_signal(roic, roa, roe, closeadj):
    # rid=35
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v036_signal(roic, roa, roe, closeadj):
    # rid=36
    base = _f41_roic_stability(roic, 21)
    trans = _mean(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc_base_v037_signal(roic, roa, roe, closeadj):
    # rid=37
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc_base_v038_signal(roic, roa, roe, closeadj):
    # rid=38
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxc_base_v039_signal(roic, roa, roe, closeadj):
    # rid=39
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc_base_v040_signal(roic, roa, roe, closeadj):
    # rid=40
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc_base_v041_signal(roic, roa, roe, closeadj):
    # rid=41
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxlc_base_v042_signal(roic, roa, roe, closeadj):
    # rid=42
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc_base_v043_signal(roic, roa, roe, closeadj):
    # rid=43
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc_base_v044_signal(roic, roa, roe, closeadj):
    # rid=44
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstddc_base_v045_signal(roic, roa, roe, closeadj):
    # rid=45
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm_base_v046_signal(roic, roa, roe, closeadj):
    # rid=46
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm_base_v047_signal(roic, roa, roe, closeadj):
    # rid=47
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm_base_v048_signal(roic, roa, roe, closeadj):
    # rid=48
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm63_base_v049_signal(roic, roa, roe, closeadj):
    # rid=49
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm63_base_v050_signal(roic, roa, roe, closeadj):
    # rid=50
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm63_base_v051_signal(roic, roa, roe, closeadj):
    # rid=51
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm126_base_v052_signal(roic, roa, roe, closeadj):
    # rid=52
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm126_base_v053_signal(roic, roa, roe, closeadj):
    # rid=53
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcm126_base_v054_signal(roic, roa, roe, closeadj):
    # rid=54
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz_base_v055_signal(roic, roa, roe, closeadj):
    # rid=55
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz_base_v056_signal(roic, roa, roe, closeadj):
    # rid=56
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcz_base_v057_signal(roic, roa, roe, closeadj):
    # rid=57
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr_base_v058_signal(roic, roa, roe, closeadj):
    # rid=58
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr_base_v059_signal(roic, roa, roe, closeadj):
    # rid=59
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr_base_v060_signal(roic, roa, roe, closeadj):
    # rid=60
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr63_base_v061_signal(roic, roa, roe, closeadj):
    # rid=61
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr63_base_v062_signal(roic, roa, roe, closeadj):
    # rid=62
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabstdxcr63_base_v063_signal(roic, roa, roe, closeadj):
    # rid=63
    base = _f41_roic_stability(roic, 21)
    trans = _std(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc_base_v064_signal(roic, roa, roe, closeadj):
    # rid=64
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc_base_v065_signal(roic, roa, roe, closeadj):
    # rid=65
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxc_base_v066_signal(roic, roa, roe, closeadj):
    # rid=66
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc_base_v067_signal(roic, roa, roe, closeadj):
    # rid=67
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc_base_v068_signal(roic, roa, roe, closeadj):
    # rid=68
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxlc_base_v069_signal(roic, roa, roe, closeadj):
    # rid=69
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc_base_v070_signal(roic, roa, roe, closeadj):
    # rid=70
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc_base_v071_signal(roic, roa, roe, closeadj):
    # rid=71
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzdc_base_v072_signal(roic, roa, roe, closeadj):
    # rid=72
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm_base_v073_signal(roic, roa, roe, closeadj):
    # rid=73
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm_base_v074_signal(roic, roa, roe, closeadj):
    # rid=74
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm_base_v075_signal(roic, roa, roe, closeadj):
    # rid=75
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41urs_f41_utility_roic_stability_stabrawxc_base_v001_signal,
    f41urs_f41_utility_roic_stability_stabrawxlc_base_v002_signal,
    f41urs_f41_utility_roic_stability_stabrawdc_base_v003_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm_base_v004_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm63_base_v005_signal,
    f41urs_f41_utility_roic_stability_stabrawxcm126_base_v006_signal,
    f41urs_f41_utility_roic_stability_stabrawxcz_base_v007_signal,
    f41urs_f41_utility_roic_stability_stabrawxcr_base_v008_signal,
    f41urs_f41_utility_roic_stability_stabrawxcr63_base_v009_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc_base_v010_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc_base_v011_signal,
    f41urs_f41_utility_roic_stability_stabmeanxc_base_v012_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc_base_v013_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc_base_v014_signal,
    f41urs_f41_utility_roic_stability_stabmeanxlc_base_v015_signal,
    f41urs_f41_utility_roic_stability_stabmeandc_base_v016_signal,
    f41urs_f41_utility_roic_stability_stabmeandc_base_v017_signal,
    f41urs_f41_utility_roic_stability_stabmeandc_base_v018_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm_base_v019_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm_base_v020_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm_base_v021_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v022_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v023_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm63_base_v024_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v025_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v026_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcm126_base_v027_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz_base_v028_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz_base_v029_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcz_base_v030_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr_base_v031_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr_base_v032_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr_base_v033_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v034_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v035_signal,
    f41urs_f41_utility_roic_stability_stabmeanxcr63_base_v036_signal,
    f41urs_f41_utility_roic_stability_stabstdxc_base_v037_signal,
    f41urs_f41_utility_roic_stability_stabstdxc_base_v038_signal,
    f41urs_f41_utility_roic_stability_stabstdxc_base_v039_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc_base_v040_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc_base_v041_signal,
    f41urs_f41_utility_roic_stability_stabstdxlc_base_v042_signal,
    f41urs_f41_utility_roic_stability_stabstddc_base_v043_signal,
    f41urs_f41_utility_roic_stability_stabstddc_base_v044_signal,
    f41urs_f41_utility_roic_stability_stabstddc_base_v045_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm_base_v046_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm_base_v047_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm_base_v048_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm63_base_v049_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm63_base_v050_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm63_base_v051_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm126_base_v052_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm126_base_v053_signal,
    f41urs_f41_utility_roic_stability_stabstdxcm126_base_v054_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz_base_v055_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz_base_v056_signal,
    f41urs_f41_utility_roic_stability_stabstdxcz_base_v057_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr_base_v058_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr_base_v059_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr_base_v060_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr63_base_v061_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr63_base_v062_signal,
    f41urs_f41_utility_roic_stability_stabstdxcr63_base_v063_signal,
    f41urs_f41_utility_roic_stability_stabzxc_base_v064_signal,
    f41urs_f41_utility_roic_stability_stabzxc_base_v065_signal,
    f41urs_f41_utility_roic_stability_stabzxc_base_v066_signal,
    f41urs_f41_utility_roic_stability_stabzxlc_base_v067_signal,
    f41urs_f41_utility_roic_stability_stabzxlc_base_v068_signal,
    f41urs_f41_utility_roic_stability_stabzxlc_base_v069_signal,
    f41urs_f41_utility_roic_stability_stabzdc_base_v070_signal,
    f41urs_f41_utility_roic_stability_stabzdc_base_v071_signal,
    f41urs_f41_utility_roic_stability_stabzdc_base_v072_signal,
    f41urs_f41_utility_roic_stability_stabzxcm_base_v073_signal,
    f41urs_f41_utility_roic_stability_stabzxcm_base_v074_signal,
    f41urs_f41_utility_roic_stability_stabzxcm_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_UTILITY_ROIC_STABILITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f41_utility_roic_stability_base_001_075_claude: {n_features} features pass")
