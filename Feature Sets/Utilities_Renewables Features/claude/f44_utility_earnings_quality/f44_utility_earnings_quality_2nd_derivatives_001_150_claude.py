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
def _f44_accrual_cash(netinc, ncfo, w):
    accr = netinc - ncfo
    return accr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_earnings_quality(netinc, ncfo, w):
    q = ncfo / netinc.replace(0, np.nan).abs()
    return q.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_cash_earnings_proxy(ncfo, ebitda, w):
    p = ncfo / ebitda.replace(0, np.nan).abs()
    return p.rolling(w, min_periods=max(1, w // 2)).mean()

def f44ueq_f44_utility_earnings_quality_accrawxc5d_slope_v001_signal(netinc, ncfo, ebitda, closeadj):
    # rid=1
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxlc10d_slope_v002_signal(netinc, ncfo, ebitda, closeadj):
    # rid=2
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawdc21d_slope_v003_signal(netinc, ncfo, ebitda, closeadj):
    # rid=3
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcm42d_slope_v004_signal(netinc, ncfo, ebitda, closeadj):
    # rid=4
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcm6363d_slope_v005_signal(netinc, ncfo, ebitda, closeadj):
    # rid=5
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcm126126d_slope_v006_signal(netinc, ncfo, ebitda, closeadj):
    # rid=6
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcz5d_slope_v007_signal(netinc, ncfo, ebitda, closeadj):
    # rid=7
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcr10d_slope_v008_signal(netinc, ncfo, ebitda, closeadj):
    # rid=8
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accrawxcr6321d_slope_v009_signal(netinc, ncfo, ebitda, closeadj):
    # rid=9
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxc42d_slope_v010_signal(netinc, ncfo, ebitda, closeadj):
    # rid=10
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxc63d_slope_v011_signal(netinc, ncfo, ebitda, closeadj):
    # rid=11
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxc126d_slope_v012_signal(netinc, ncfo, ebitda, closeadj):
    # rid=12
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxlc5d_slope_v013_signal(netinc, ncfo, ebitda, closeadj):
    # rid=13
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxlc10d_slope_v014_signal(netinc, ncfo, ebitda, closeadj):
    # rid=14
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxlc21d_slope_v015_signal(netinc, ncfo, ebitda, closeadj):
    # rid=15
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeandc42d_slope_v016_signal(netinc, ncfo, ebitda, closeadj):
    # rid=16
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeandc63d_slope_v017_signal(netinc, ncfo, ebitda, closeadj):
    # rid=17
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeandc126d_slope_v018_signal(netinc, ncfo, ebitda, closeadj):
    # rid=18
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm5d_slope_v019_signal(netinc, ncfo, ebitda, closeadj):
    # rid=19
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm10d_slope_v020_signal(netinc, ncfo, ebitda, closeadj):
    # rid=20
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm21d_slope_v021_signal(netinc, ncfo, ebitda, closeadj):
    # rid=21
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm6342d_slope_v022_signal(netinc, ncfo, ebitda, closeadj):
    # rid=22
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm6363d_slope_v023_signal(netinc, ncfo, ebitda, closeadj):
    # rid=23
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm63126d_slope_v024_signal(netinc, ncfo, ebitda, closeadj):
    # rid=24
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm1265d_slope_v025_signal(netinc, ncfo, ebitda, closeadj):
    # rid=25
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm12610d_slope_v026_signal(netinc, ncfo, ebitda, closeadj):
    # rid=26
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcm12621d_slope_v027_signal(netinc, ncfo, ebitda, closeadj):
    # rid=27
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcz42d_slope_v028_signal(netinc, ncfo, ebitda, closeadj):
    # rid=28
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcz63d_slope_v029_signal(netinc, ncfo, ebitda, closeadj):
    # rid=29
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcz126d_slope_v030_signal(netinc, ncfo, ebitda, closeadj):
    # rid=30
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr5d_slope_v031_signal(netinc, ncfo, ebitda, closeadj):
    # rid=31
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr10d_slope_v032_signal(netinc, ncfo, ebitda, closeadj):
    # rid=32
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr21d_slope_v033_signal(netinc, ncfo, ebitda, closeadj):
    # rid=33
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr6342d_slope_v034_signal(netinc, ncfo, ebitda, closeadj):
    # rid=34
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr6363d_slope_v035_signal(netinc, ncfo, ebitda, closeadj):
    # rid=35
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accmeanxcr63126d_slope_v036_signal(netinc, ncfo, ebitda, closeadj):
    # rid=36
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxc5d_slope_v037_signal(netinc, ncfo, ebitda, closeadj):
    # rid=37
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxc10d_slope_v038_signal(netinc, ncfo, ebitda, closeadj):
    # rid=38
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxc21d_slope_v039_signal(netinc, ncfo, ebitda, closeadj):
    # rid=39
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxlc42d_slope_v040_signal(netinc, ncfo, ebitda, closeadj):
    # rid=40
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxlc63d_slope_v041_signal(netinc, ncfo, ebitda, closeadj):
    # rid=41
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxlc126d_slope_v042_signal(netinc, ncfo, ebitda, closeadj):
    # rid=42
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstddc5d_slope_v043_signal(netinc, ncfo, ebitda, closeadj):
    # rid=43
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstddc10d_slope_v044_signal(netinc, ncfo, ebitda, closeadj):
    # rid=44
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstddc21d_slope_v045_signal(netinc, ncfo, ebitda, closeadj):
    # rid=45
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm42d_slope_v046_signal(netinc, ncfo, ebitda, closeadj):
    # rid=46
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm63d_slope_v047_signal(netinc, ncfo, ebitda, closeadj):
    # rid=47
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm126d_slope_v048_signal(netinc, ncfo, ebitda, closeadj):
    # rid=48
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm635d_slope_v049_signal(netinc, ncfo, ebitda, closeadj):
    # rid=49
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm6310d_slope_v050_signal(netinc, ncfo, ebitda, closeadj):
    # rid=50
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm6321d_slope_v051_signal(netinc, ncfo, ebitda, closeadj):
    # rid=51
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm12642d_slope_v052_signal(netinc, ncfo, ebitda, closeadj):
    # rid=52
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm12663d_slope_v053_signal(netinc, ncfo, ebitda, closeadj):
    # rid=53
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcm126126d_slope_v054_signal(netinc, ncfo, ebitda, closeadj):
    # rid=54
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcz5d_slope_v055_signal(netinc, ncfo, ebitda, closeadj):
    # rid=55
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcz10d_slope_v056_signal(netinc, ncfo, ebitda, closeadj):
    # rid=56
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcz21d_slope_v057_signal(netinc, ncfo, ebitda, closeadj):
    # rid=57
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr42d_slope_v058_signal(netinc, ncfo, ebitda, closeadj):
    # rid=58
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr63d_slope_v059_signal(netinc, ncfo, ebitda, closeadj):
    # rid=59
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr126d_slope_v060_signal(netinc, ncfo, ebitda, closeadj):
    # rid=60
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr635d_slope_v061_signal(netinc, ncfo, ebitda, closeadj):
    # rid=61
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr6310d_slope_v062_signal(netinc, ncfo, ebitda, closeadj):
    # rid=62
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accstdxcr6321d_slope_v063_signal(netinc, ncfo, ebitda, closeadj):
    # rid=63
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxc42d_slope_v064_signal(netinc, ncfo, ebitda, closeadj):
    # rid=64
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxc63d_slope_v065_signal(netinc, ncfo, ebitda, closeadj):
    # rid=65
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxc126d_slope_v066_signal(netinc, ncfo, ebitda, closeadj):
    # rid=66
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxlc5d_slope_v067_signal(netinc, ncfo, ebitda, closeadj):
    # rid=67
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxlc10d_slope_v068_signal(netinc, ncfo, ebitda, closeadj):
    # rid=68
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxlc21d_slope_v069_signal(netinc, ncfo, ebitda, closeadj):
    # rid=69
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczdc42d_slope_v070_signal(netinc, ncfo, ebitda, closeadj):
    # rid=70
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczdc63d_slope_v071_signal(netinc, ncfo, ebitda, closeadj):
    # rid=71
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczdc126d_slope_v072_signal(netinc, ncfo, ebitda, closeadj):
    # rid=72
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm5d_slope_v073_signal(netinc, ncfo, ebitda, closeadj):
    # rid=73
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm10d_slope_v074_signal(netinc, ncfo, ebitda, closeadj):
    # rid=74
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm21d_slope_v075_signal(netinc, ncfo, ebitda, closeadj):
    # rid=75
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm6342d_slope_v076_signal(netinc, ncfo, ebitda, closeadj):
    # rid=76
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm6363d_slope_v077_signal(netinc, ncfo, ebitda, closeadj):
    # rid=77
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm63126d_slope_v078_signal(netinc, ncfo, ebitda, closeadj):
    # rid=78
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm1265d_slope_v079_signal(netinc, ncfo, ebitda, closeadj):
    # rid=79
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm12610d_slope_v080_signal(netinc, ncfo, ebitda, closeadj):
    # rid=80
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcm12621d_slope_v081_signal(netinc, ncfo, ebitda, closeadj):
    # rid=81
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcz42d_slope_v082_signal(netinc, ncfo, ebitda, closeadj):
    # rid=82
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcz63d_slope_v083_signal(netinc, ncfo, ebitda, closeadj):
    # rid=83
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcz126d_slope_v084_signal(netinc, ncfo, ebitda, closeadj):
    # rid=84
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr5d_slope_v085_signal(netinc, ncfo, ebitda, closeadj):
    # rid=85
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr10d_slope_v086_signal(netinc, ncfo, ebitda, closeadj):
    # rid=86
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr21d_slope_v087_signal(netinc, ncfo, ebitda, closeadj):
    # rid=87
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr6342d_slope_v088_signal(netinc, ncfo, ebitda, closeadj):
    # rid=88
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr6363d_slope_v089_signal(netinc, ncfo, ebitda, closeadj):
    # rid=89
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acczxcr63126d_slope_v090_signal(netinc, ncfo, ebitda, closeadj):
    # rid=90
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxc5d_slope_v091_signal(netinc, ncfo, ebitda, closeadj):
    # rid=91
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxc10d_slope_v092_signal(netinc, ncfo, ebitda, closeadj):
    # rid=92
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxc21d_slope_v093_signal(netinc, ncfo, ebitda, closeadj):
    # rid=93
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxlc42d_slope_v094_signal(netinc, ncfo, ebitda, closeadj):
    # rid=94
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxlc63d_slope_v095_signal(netinc, ncfo, ebitda, closeadj):
    # rid=95
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxlc126d_slope_v096_signal(netinc, ncfo, ebitda, closeadj):
    # rid=96
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemadc5d_slope_v097_signal(netinc, ncfo, ebitda, closeadj):
    # rid=97
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemadc10d_slope_v098_signal(netinc, ncfo, ebitda, closeadj):
    # rid=98
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemadc21d_slope_v099_signal(netinc, ncfo, ebitda, closeadj):
    # rid=99
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm42d_slope_v100_signal(netinc, ncfo, ebitda, closeadj):
    # rid=100
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm63d_slope_v101_signal(netinc, ncfo, ebitda, closeadj):
    # rid=101
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm126d_slope_v102_signal(netinc, ncfo, ebitda, closeadj):
    # rid=102
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm635d_slope_v103_signal(netinc, ncfo, ebitda, closeadj):
    # rid=103
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm6310d_slope_v104_signal(netinc, ncfo, ebitda, closeadj):
    # rid=104
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm6321d_slope_v105_signal(netinc, ncfo, ebitda, closeadj):
    # rid=105
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm12642d_slope_v106_signal(netinc, ncfo, ebitda, closeadj):
    # rid=106
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm12663d_slope_v107_signal(netinc, ncfo, ebitda, closeadj):
    # rid=107
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcm126126d_slope_v108_signal(netinc, ncfo, ebitda, closeadj):
    # rid=108
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcz5d_slope_v109_signal(netinc, ncfo, ebitda, closeadj):
    # rid=109
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcz10d_slope_v110_signal(netinc, ncfo, ebitda, closeadj):
    # rid=110
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcz21d_slope_v111_signal(netinc, ncfo, ebitda, closeadj):
    # rid=111
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr42d_slope_v112_signal(netinc, ncfo, ebitda, closeadj):
    # rid=112
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr63d_slope_v113_signal(netinc, ncfo, ebitda, closeadj):
    # rid=113
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr126d_slope_v114_signal(netinc, ncfo, ebitda, closeadj):
    # rid=114
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr635d_slope_v115_signal(netinc, ncfo, ebitda, closeadj):
    # rid=115
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr6310d_slope_v116_signal(netinc, ncfo, ebitda, closeadj):
    # rid=116
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accemaxcr6321d_slope_v117_signal(netinc, ncfo, ebitda, closeadj):
    # rid=117
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxc42d_slope_v118_signal(netinc, ncfo, ebitda, closeadj):
    # rid=118
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxlc63d_slope_v119_signal(netinc, ncfo, ebitda, closeadj):
    # rid=119
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsdc126d_slope_v120_signal(netinc, ncfo, ebitda, closeadj):
    # rid=120
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcm5d_slope_v121_signal(netinc, ncfo, ebitda, closeadj):
    # rid=121
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcm6310d_slope_v122_signal(netinc, ncfo, ebitda, closeadj):
    # rid=122
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcm12621d_slope_v123_signal(netinc, ncfo, ebitda, closeadj):
    # rid=123
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcz42d_slope_v124_signal(netinc, ncfo, ebitda, closeadj):
    # rid=124
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcr63d_slope_v125_signal(netinc, ncfo, ebitda, closeadj):
    # rid=125
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accabsxcr63126d_slope_v126_signal(netinc, ncfo, ebitda, closeadj):
    # rid=126
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base.abs()
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxc5d_slope_v127_signal(netinc, ncfo, ebitda, closeadj):
    # rid=127
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxlc10d_slope_v128_signal(netinc, ncfo, ebitda, closeadj):
    # rid=128
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogdc21d_slope_v129_signal(netinc, ncfo, ebitda, closeadj):
    # rid=129
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcm42d_slope_v130_signal(netinc, ncfo, ebitda, closeadj):
    # rid=130
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcm6363d_slope_v131_signal(netinc, ncfo, ebitda, closeadj):
    # rid=131
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcm126126d_slope_v132_signal(netinc, ncfo, ebitda, closeadj):
    # rid=132
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcz5d_slope_v133_signal(netinc, ncfo, ebitda, closeadj):
    # rid=133
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcr10d_slope_v134_signal(netinc, ncfo, ebitda, closeadj):
    # rid=134
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_acclogxcr6321d_slope_v135_signal(netinc, ncfo, ebitda, closeadj):
    # rid=135
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxc42d_slope_v136_signal(netinc, ncfo, ebitda, closeadj):
    # rid=136
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxlc63d_slope_v137_signal(netinc, ncfo, ebitda, closeadj):
    # rid=137
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsigndc126d_slope_v138_signal(netinc, ncfo, ebitda, closeadj):
    # rid=138
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcm5d_slope_v139_signal(netinc, ncfo, ebitda, closeadj):
    # rid=139
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcm6310d_slope_v140_signal(netinc, ncfo, ebitda, closeadj):
    # rid=140
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcm12621d_slope_v141_signal(netinc, ncfo, ebitda, closeadj):
    # rid=141
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcz42d_slope_v142_signal(netinc, ncfo, ebitda, closeadj):
    # rid=142
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcr63d_slope_v143_signal(netinc, ncfo, ebitda, closeadj):
    # rid=143
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsignxcr63126d_slope_v144_signal(netinc, ncfo, ebitda, closeadj):
    # rid=144
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqxc5d_slope_v145_signal(netinc, ncfo, ebitda, closeadj):
    # rid=145
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqxlc10d_slope_v146_signal(netinc, ncfo, ebitda, closeadj):
    # rid=146
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqdc21d_slope_v147_signal(netinc, ncfo, ebitda, closeadj):
    # rid=147
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqxcm42d_slope_v148_signal(netinc, ncfo, ebitda, closeadj):
    # rid=148
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqxcm6363d_slope_v149_signal(netinc, ncfo, ebitda, closeadj):
    # rid=149
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44ueq_f44_utility_earnings_quality_accsqxcm126126d_slope_v150_signal(netinc, ncfo, ebitda, closeadj):
    # rid=150
    base = _f44_accrual_cash(netinc, ncfo, 21)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44ueq_f44_utility_earnings_quality_accrawxc5d_slope_v001_signal,
    f44ueq_f44_utility_earnings_quality_accrawxlc10d_slope_v002_signal,
    f44ueq_f44_utility_earnings_quality_accrawdc21d_slope_v003_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcm42d_slope_v004_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcm6363d_slope_v005_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcm126126d_slope_v006_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcz5d_slope_v007_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcr10d_slope_v008_signal,
    f44ueq_f44_utility_earnings_quality_accrawxcr6321d_slope_v009_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxc42d_slope_v010_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxc63d_slope_v011_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxc126d_slope_v012_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxlc5d_slope_v013_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxlc10d_slope_v014_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxlc21d_slope_v015_signal,
    f44ueq_f44_utility_earnings_quality_accmeandc42d_slope_v016_signal,
    f44ueq_f44_utility_earnings_quality_accmeandc63d_slope_v017_signal,
    f44ueq_f44_utility_earnings_quality_accmeandc126d_slope_v018_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm5d_slope_v019_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm10d_slope_v020_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm21d_slope_v021_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm6342d_slope_v022_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm6363d_slope_v023_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm63126d_slope_v024_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm1265d_slope_v025_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm12610d_slope_v026_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcm12621d_slope_v027_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcz42d_slope_v028_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcz63d_slope_v029_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcz126d_slope_v030_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr5d_slope_v031_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr10d_slope_v032_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr21d_slope_v033_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr6342d_slope_v034_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr6363d_slope_v035_signal,
    f44ueq_f44_utility_earnings_quality_accmeanxcr63126d_slope_v036_signal,
    f44ueq_f44_utility_earnings_quality_accstdxc5d_slope_v037_signal,
    f44ueq_f44_utility_earnings_quality_accstdxc10d_slope_v038_signal,
    f44ueq_f44_utility_earnings_quality_accstdxc21d_slope_v039_signal,
    f44ueq_f44_utility_earnings_quality_accstdxlc42d_slope_v040_signal,
    f44ueq_f44_utility_earnings_quality_accstdxlc63d_slope_v041_signal,
    f44ueq_f44_utility_earnings_quality_accstdxlc126d_slope_v042_signal,
    f44ueq_f44_utility_earnings_quality_accstddc5d_slope_v043_signal,
    f44ueq_f44_utility_earnings_quality_accstddc10d_slope_v044_signal,
    f44ueq_f44_utility_earnings_quality_accstddc21d_slope_v045_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm42d_slope_v046_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm63d_slope_v047_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm126d_slope_v048_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm635d_slope_v049_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm6310d_slope_v050_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm6321d_slope_v051_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm12642d_slope_v052_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm12663d_slope_v053_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcm126126d_slope_v054_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcz5d_slope_v055_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcz10d_slope_v056_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcz21d_slope_v057_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr42d_slope_v058_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr63d_slope_v059_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr126d_slope_v060_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr635d_slope_v061_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr6310d_slope_v062_signal,
    f44ueq_f44_utility_earnings_quality_accstdxcr6321d_slope_v063_signal,
    f44ueq_f44_utility_earnings_quality_acczxc42d_slope_v064_signal,
    f44ueq_f44_utility_earnings_quality_acczxc63d_slope_v065_signal,
    f44ueq_f44_utility_earnings_quality_acczxc126d_slope_v066_signal,
    f44ueq_f44_utility_earnings_quality_acczxlc5d_slope_v067_signal,
    f44ueq_f44_utility_earnings_quality_acczxlc10d_slope_v068_signal,
    f44ueq_f44_utility_earnings_quality_acczxlc21d_slope_v069_signal,
    f44ueq_f44_utility_earnings_quality_acczdc42d_slope_v070_signal,
    f44ueq_f44_utility_earnings_quality_acczdc63d_slope_v071_signal,
    f44ueq_f44_utility_earnings_quality_acczdc126d_slope_v072_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm5d_slope_v073_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm10d_slope_v074_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm21d_slope_v075_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm6342d_slope_v076_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm6363d_slope_v077_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm63126d_slope_v078_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm1265d_slope_v079_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm12610d_slope_v080_signal,
    f44ueq_f44_utility_earnings_quality_acczxcm12621d_slope_v081_signal,
    f44ueq_f44_utility_earnings_quality_acczxcz42d_slope_v082_signal,
    f44ueq_f44_utility_earnings_quality_acczxcz63d_slope_v083_signal,
    f44ueq_f44_utility_earnings_quality_acczxcz126d_slope_v084_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr5d_slope_v085_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr10d_slope_v086_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr21d_slope_v087_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr6342d_slope_v088_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr6363d_slope_v089_signal,
    f44ueq_f44_utility_earnings_quality_acczxcr63126d_slope_v090_signal,
    f44ueq_f44_utility_earnings_quality_accemaxc5d_slope_v091_signal,
    f44ueq_f44_utility_earnings_quality_accemaxc10d_slope_v092_signal,
    f44ueq_f44_utility_earnings_quality_accemaxc21d_slope_v093_signal,
    f44ueq_f44_utility_earnings_quality_accemaxlc42d_slope_v094_signal,
    f44ueq_f44_utility_earnings_quality_accemaxlc63d_slope_v095_signal,
    f44ueq_f44_utility_earnings_quality_accemaxlc126d_slope_v096_signal,
    f44ueq_f44_utility_earnings_quality_accemadc5d_slope_v097_signal,
    f44ueq_f44_utility_earnings_quality_accemadc10d_slope_v098_signal,
    f44ueq_f44_utility_earnings_quality_accemadc21d_slope_v099_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm42d_slope_v100_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm63d_slope_v101_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm126d_slope_v102_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm635d_slope_v103_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm6310d_slope_v104_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm6321d_slope_v105_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm12642d_slope_v106_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm12663d_slope_v107_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcm126126d_slope_v108_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcz5d_slope_v109_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcz10d_slope_v110_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcz21d_slope_v111_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr42d_slope_v112_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr63d_slope_v113_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr126d_slope_v114_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr635d_slope_v115_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr6310d_slope_v116_signal,
    f44ueq_f44_utility_earnings_quality_accemaxcr6321d_slope_v117_signal,
    f44ueq_f44_utility_earnings_quality_accabsxc42d_slope_v118_signal,
    f44ueq_f44_utility_earnings_quality_accabsxlc63d_slope_v119_signal,
    f44ueq_f44_utility_earnings_quality_accabsdc126d_slope_v120_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcm5d_slope_v121_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcm6310d_slope_v122_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcm12621d_slope_v123_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcz42d_slope_v124_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcr63d_slope_v125_signal,
    f44ueq_f44_utility_earnings_quality_accabsxcr63126d_slope_v126_signal,
    f44ueq_f44_utility_earnings_quality_acclogxc5d_slope_v127_signal,
    f44ueq_f44_utility_earnings_quality_acclogxlc10d_slope_v128_signal,
    f44ueq_f44_utility_earnings_quality_acclogdc21d_slope_v129_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcm42d_slope_v130_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcm6363d_slope_v131_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcm126126d_slope_v132_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcz5d_slope_v133_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcr10d_slope_v134_signal,
    f44ueq_f44_utility_earnings_quality_acclogxcr6321d_slope_v135_signal,
    f44ueq_f44_utility_earnings_quality_accsignxc42d_slope_v136_signal,
    f44ueq_f44_utility_earnings_quality_accsignxlc63d_slope_v137_signal,
    f44ueq_f44_utility_earnings_quality_accsigndc126d_slope_v138_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcm5d_slope_v139_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcm6310d_slope_v140_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcm12621d_slope_v141_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcz42d_slope_v142_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcr63d_slope_v143_signal,
    f44ueq_f44_utility_earnings_quality_accsignxcr63126d_slope_v144_signal,
    f44ueq_f44_utility_earnings_quality_accsqxc5d_slope_v145_signal,
    f44ueq_f44_utility_earnings_quality_accsqxlc10d_slope_v146_signal,
    f44ueq_f44_utility_earnings_quality_accsqdc21d_slope_v147_signal,
    f44ueq_f44_utility_earnings_quality_accsqxcm42d_slope_v148_signal,
    f44ueq_f44_utility_earnings_quality_accsqxcm6363d_slope_v149_signal,
    f44ueq_f44_utility_earnings_quality_accsqxcm126126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_UTILITY_EARNINGS_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f44_accrual_cash", "_f44_earnings_quality", "_f44_cash_earnings_proxy")
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
    print(f"OK f44_utility_earnings_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
