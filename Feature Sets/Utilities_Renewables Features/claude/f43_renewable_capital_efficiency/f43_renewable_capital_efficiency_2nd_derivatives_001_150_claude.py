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
def _f43_asset_turnover(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f43_capital_efficiency(revenue, ppnenet, w):
    e = revenue / ppnenet.replace(0, np.nan).abs()
    return e.rolling(w, min_periods=max(1, w // 2)).mean()


def _f43_efficiency_compound(revenue, assets, w):
    t = revenue / assets.replace(0, np.nan).abs()
    return t.rolling(w, min_periods=max(1, w // 2)).mean() * np.sqrt(w)

def f43rce_f43_renewable_capital_efficiency_atorawxc5d_slope_v001_signal(revenue, assets, ppnenet, closeadj):
    # rid=1
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxlc10d_slope_v002_signal(revenue, assets, ppnenet, closeadj):
    # rid=2
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawdc21d_slope_v003_signal(revenue, assets, ppnenet, closeadj):
    # rid=3
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm42d_slope_v004_signal(revenue, assets, ppnenet, closeadj):
    # rid=4
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm6363d_slope_v005_signal(revenue, assets, ppnenet, closeadj):
    # rid=5
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm126126d_slope_v006_signal(revenue, assets, ppnenet, closeadj):
    # rid=6
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcz5d_slope_v007_signal(revenue, assets, ppnenet, closeadj):
    # rid=7
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcr10d_slope_v008_signal(revenue, assets, ppnenet, closeadj):
    # rid=8
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcr6321d_slope_v009_signal(revenue, assets, ppnenet, closeadj):
    # rid=9
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc42d_slope_v010_signal(revenue, assets, ppnenet, closeadj):
    # rid=10
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc63d_slope_v011_signal(revenue, assets, ppnenet, closeadj):
    # rid=11
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc126d_slope_v012_signal(revenue, assets, ppnenet, closeadj):
    # rid=12
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc5d_slope_v013_signal(revenue, assets, ppnenet, closeadj):
    # rid=13
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc10d_slope_v014_signal(revenue, assets, ppnenet, closeadj):
    # rid=14
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc21d_slope_v015_signal(revenue, assets, ppnenet, closeadj):
    # rid=15
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc42d_slope_v016_signal(revenue, assets, ppnenet, closeadj):
    # rid=16
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc63d_slope_v017_signal(revenue, assets, ppnenet, closeadj):
    # rid=17
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc126d_slope_v018_signal(revenue, assets, ppnenet, closeadj):
    # rid=18
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm5d_slope_v019_signal(revenue, assets, ppnenet, closeadj):
    # rid=19
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm10d_slope_v020_signal(revenue, assets, ppnenet, closeadj):
    # rid=20
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm21d_slope_v021_signal(revenue, assets, ppnenet, closeadj):
    # rid=21
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm6342d_slope_v022_signal(revenue, assets, ppnenet, closeadj):
    # rid=22
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm6363d_slope_v023_signal(revenue, assets, ppnenet, closeadj):
    # rid=23
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm63126d_slope_v024_signal(revenue, assets, ppnenet, closeadj):
    # rid=24
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm1265d_slope_v025_signal(revenue, assets, ppnenet, closeadj):
    # rid=25
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm12610d_slope_v026_signal(revenue, assets, ppnenet, closeadj):
    # rid=26
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm12621d_slope_v027_signal(revenue, assets, ppnenet, closeadj):
    # rid=27
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz42d_slope_v028_signal(revenue, assets, ppnenet, closeadj):
    # rid=28
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz63d_slope_v029_signal(revenue, assets, ppnenet, closeadj):
    # rid=29
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz126d_slope_v030_signal(revenue, assets, ppnenet, closeadj):
    # rid=30
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr5d_slope_v031_signal(revenue, assets, ppnenet, closeadj):
    # rid=31
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr10d_slope_v032_signal(revenue, assets, ppnenet, closeadj):
    # rid=32
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr21d_slope_v033_signal(revenue, assets, ppnenet, closeadj):
    # rid=33
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr6342d_slope_v034_signal(revenue, assets, ppnenet, closeadj):
    # rid=34
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr6363d_slope_v035_signal(revenue, assets, ppnenet, closeadj):
    # rid=35
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr63126d_slope_v036_signal(revenue, assets, ppnenet, closeadj):
    # rid=36
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc5d_slope_v037_signal(revenue, assets, ppnenet, closeadj):
    # rid=37
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc10d_slope_v038_signal(revenue, assets, ppnenet, closeadj):
    # rid=38
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc21d_slope_v039_signal(revenue, assets, ppnenet, closeadj):
    # rid=39
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc42d_slope_v040_signal(revenue, assets, ppnenet, closeadj):
    # rid=40
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc63d_slope_v041_signal(revenue, assets, ppnenet, closeadj):
    # rid=41
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc126d_slope_v042_signal(revenue, assets, ppnenet, closeadj):
    # rid=42
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc5d_slope_v043_signal(revenue, assets, ppnenet, closeadj):
    # rid=43
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc10d_slope_v044_signal(revenue, assets, ppnenet, closeadj):
    # rid=44
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc21d_slope_v045_signal(revenue, assets, ppnenet, closeadj):
    # rid=45
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm42d_slope_v046_signal(revenue, assets, ppnenet, closeadj):
    # rid=46
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm63d_slope_v047_signal(revenue, assets, ppnenet, closeadj):
    # rid=47
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm126d_slope_v048_signal(revenue, assets, ppnenet, closeadj):
    # rid=48
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm635d_slope_v049_signal(revenue, assets, ppnenet, closeadj):
    # rid=49
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm6310d_slope_v050_signal(revenue, assets, ppnenet, closeadj):
    # rid=50
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm6321d_slope_v051_signal(revenue, assets, ppnenet, closeadj):
    # rid=51
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm12642d_slope_v052_signal(revenue, assets, ppnenet, closeadj):
    # rid=52
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm12663d_slope_v053_signal(revenue, assets, ppnenet, closeadj):
    # rid=53
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm126126d_slope_v054_signal(revenue, assets, ppnenet, closeadj):
    # rid=54
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz5d_slope_v055_signal(revenue, assets, ppnenet, closeadj):
    # rid=55
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz10d_slope_v056_signal(revenue, assets, ppnenet, closeadj):
    # rid=56
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz21d_slope_v057_signal(revenue, assets, ppnenet, closeadj):
    # rid=57
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr42d_slope_v058_signal(revenue, assets, ppnenet, closeadj):
    # rid=58
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr63d_slope_v059_signal(revenue, assets, ppnenet, closeadj):
    # rid=59
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr126d_slope_v060_signal(revenue, assets, ppnenet, closeadj):
    # rid=60
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr635d_slope_v061_signal(revenue, assets, ppnenet, closeadj):
    # rid=61
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr6310d_slope_v062_signal(revenue, assets, ppnenet, closeadj):
    # rid=62
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr6321d_slope_v063_signal(revenue, assets, ppnenet, closeadj):
    # rid=63
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc42d_slope_v064_signal(revenue, assets, ppnenet, closeadj):
    # rid=64
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc63d_slope_v065_signal(revenue, assets, ppnenet, closeadj):
    # rid=65
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc126d_slope_v066_signal(revenue, assets, ppnenet, closeadj):
    # rid=66
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * closeadj
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc5d_slope_v067_signal(revenue, assets, ppnenet, closeadj):
    # rid=67
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc10d_slope_v068_signal(revenue, assets, ppnenet, closeadj):
    # rid=68
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc21d_slope_v069_signal(revenue, assets, ppnenet, closeadj):
    # rid=69
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc42d_slope_v070_signal(revenue, assets, ppnenet, closeadj):
    # rid=70
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc63d_slope_v071_signal(revenue, assets, ppnenet, closeadj):
    # rid=71
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc126d_slope_v072_signal(revenue, assets, ppnenet, closeadj):
    # rid=72
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm5d_slope_v073_signal(revenue, assets, ppnenet, closeadj):
    # rid=73
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm10d_slope_v074_signal(revenue, assets, ppnenet, closeadj):
    # rid=74
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm21d_slope_v075_signal(revenue, assets, ppnenet, closeadj):
    # rid=75
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm6342d_slope_v076_signal(revenue, assets, ppnenet, closeadj):
    # rid=76
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm6363d_slope_v077_signal(revenue, assets, ppnenet, closeadj):
    # rid=77
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm63126d_slope_v078_signal(revenue, assets, ppnenet, closeadj):
    # rid=78
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm1265d_slope_v079_signal(revenue, assets, ppnenet, closeadj):
    # rid=79
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm12610d_slope_v080_signal(revenue, assets, ppnenet, closeadj):
    # rid=80
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm12621d_slope_v081_signal(revenue, assets, ppnenet, closeadj):
    # rid=81
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcz42d_slope_v082_signal(revenue, assets, ppnenet, closeadj):
    # rid=82
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcz63d_slope_v083_signal(revenue, assets, ppnenet, closeadj):
    # rid=83
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcz126d_slope_v084_signal(revenue, assets, ppnenet, closeadj):
    # rid=84
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr5d_slope_v085_signal(revenue, assets, ppnenet, closeadj):
    # rid=85
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr10d_slope_v086_signal(revenue, assets, ppnenet, closeadj):
    # rid=86
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr21d_slope_v087_signal(revenue, assets, ppnenet, closeadj):
    # rid=87
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr6342d_slope_v088_signal(revenue, assets, ppnenet, closeadj):
    # rid=88
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr6363d_slope_v089_signal(revenue, assets, ppnenet, closeadj):
    # rid=89
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcr63126d_slope_v090_signal(revenue, assets, ppnenet, closeadj):
    # rid=90
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxc5d_slope_v091_signal(revenue, assets, ppnenet, closeadj):
    # rid=91
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxc10d_slope_v092_signal(revenue, assets, ppnenet, closeadj):
    # rid=92
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * closeadj
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxc21d_slope_v093_signal(revenue, assets, ppnenet, closeadj):
    # rid=93
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxlc42d_slope_v094_signal(revenue, assets, ppnenet, closeadj):
    # rid=94
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxlc63d_slope_v095_signal(revenue, assets, ppnenet, closeadj):
    # rid=95
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxlc126d_slope_v096_signal(revenue, assets, ppnenet, closeadj):
    # rid=96
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemadc5d_slope_v097_signal(revenue, assets, ppnenet, closeadj):
    # rid=97
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemadc10d_slope_v098_signal(revenue, assets, ppnenet, closeadj):
    # rid=98
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemadc21d_slope_v099_signal(revenue, assets, ppnenet, closeadj):
    # rid=99
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm42d_slope_v100_signal(revenue, assets, ppnenet, closeadj):
    # rid=100
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm63d_slope_v101_signal(revenue, assets, ppnenet, closeadj):
    # rid=101
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm126d_slope_v102_signal(revenue, assets, ppnenet, closeadj):
    # rid=102
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm635d_slope_v103_signal(revenue, assets, ppnenet, closeadj):
    # rid=103
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm6310d_slope_v104_signal(revenue, assets, ppnenet, closeadj):
    # rid=104
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm6321d_slope_v105_signal(revenue, assets, ppnenet, closeadj):
    # rid=105
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm12642d_slope_v106_signal(revenue, assets, ppnenet, closeadj):
    # rid=106
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm12663d_slope_v107_signal(revenue, assets, ppnenet, closeadj):
    # rid=107
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcm126126d_slope_v108_signal(revenue, assets, ppnenet, closeadj):
    # rid=108
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcz5d_slope_v109_signal(revenue, assets, ppnenet, closeadj):
    # rid=109
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcz10d_slope_v110_signal(revenue, assets, ppnenet, closeadj):
    # rid=110
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcz21d_slope_v111_signal(revenue, assets, ppnenet, closeadj):
    # rid=111
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr42d_slope_v112_signal(revenue, assets, ppnenet, closeadj):
    # rid=112
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr63d_slope_v113_signal(revenue, assets, ppnenet, closeadj):
    # rid=113
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr126d_slope_v114_signal(revenue, assets, ppnenet, closeadj):
    # rid=114
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr635d_slope_v115_signal(revenue, assets, ppnenet, closeadj):
    # rid=115
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 21)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr6310d_slope_v116_signal(revenue, assets, ppnenet, closeadj):
    # rid=116
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 63)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoemaxcr6321d_slope_v117_signal(revenue, assets, ppnenet, closeadj):
    # rid=117
    base = _f43_asset_turnover(revenue, assets)
    trans = _ema(base, 126)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxc42d_slope_v118_signal(revenue, assets, ppnenet, closeadj):
    # rid=118
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxlc63d_slope_v119_signal(revenue, assets, ppnenet, closeadj):
    # rid=119
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsdc126d_slope_v120_signal(revenue, assets, ppnenet, closeadj):
    # rid=120
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcm5d_slope_v121_signal(revenue, assets, ppnenet, closeadj):
    # rid=121
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcm6310d_slope_v122_signal(revenue, assets, ppnenet, closeadj):
    # rid=122
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcm12621d_slope_v123_signal(revenue, assets, ppnenet, closeadj):
    # rid=123
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcz42d_slope_v124_signal(revenue, assets, ppnenet, closeadj):
    # rid=124
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcr63d_slope_v125_signal(revenue, assets, ppnenet, closeadj):
    # rid=125
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atoabsxcr63126d_slope_v126_signal(revenue, assets, ppnenet, closeadj):
    # rid=126
    base = _f43_asset_turnover(revenue, assets)
    trans = base.abs()
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxc5d_slope_v127_signal(revenue, assets, ppnenet, closeadj):
    # rid=127
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxlc10d_slope_v128_signal(revenue, assets, ppnenet, closeadj):
    # rid=128
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologdc21d_slope_v129_signal(revenue, assets, ppnenet, closeadj):
    # rid=129
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcm42d_slope_v130_signal(revenue, assets, ppnenet, closeadj):
    # rid=130
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcm6363d_slope_v131_signal(revenue, assets, ppnenet, closeadj):
    # rid=131
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcm126126d_slope_v132_signal(revenue, assets, ppnenet, closeadj):
    # rid=132
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcz5d_slope_v133_signal(revenue, assets, ppnenet, closeadj):
    # rid=133
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * _z(closeadj, 63)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcr10d_slope_v134_signal(revenue, assets, ppnenet, closeadj):
    # rid=134
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(21)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atologxcr6321d_slope_v135_signal(revenue, assets, ppnenet, closeadj):
    # rid=135
    base = _f43_asset_turnover(revenue, assets)
    trans = np.log(base.abs() + 1e-9)
    pre = trans * closeadj.pct_change(63)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxc42d_slope_v136_signal(revenue, assets, ppnenet, closeadj):
    # rid=136
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * closeadj
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxlc63d_slope_v137_signal(revenue, assets, ppnenet, closeadj):
    # rid=137
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * np.log(closeadj)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosigndc126d_slope_v138_signal(revenue, assets, ppnenet, closeadj):
    # rid=138
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcm5d_slope_v139_signal(revenue, assets, ppnenet, closeadj):
    # rid=139
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 21)
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcm6310d_slope_v140_signal(revenue, assets, ppnenet, closeadj):
    # rid=140
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 63)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcm12621d_slope_v141_signal(revenue, assets, ppnenet, closeadj):
    # rid=141
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * _mean(closeadj, 126)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcz42d_slope_v142_signal(revenue, assets, ppnenet, closeadj):
    # rid=142
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * _z(closeadj, 63)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcr63d_slope_v143_signal(revenue, assets, ppnenet, closeadj):
    # rid=143
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(21)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosignxcr63126d_slope_v144_signal(revenue, assets, ppnenet, closeadj):
    # rid=144
    base = _f43_asset_turnover(revenue, assets)
    trans = np.sign(base)
    pre = trans * closeadj.pct_change(63)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqxc5d_slope_v145_signal(revenue, assets, ppnenet, closeadj):
    # rid=145
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans * closeadj
    result = _slope_diff_norm(pre, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqxlc10d_slope_v146_signal(revenue, assets, ppnenet, closeadj):
    # rid=146
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans * np.log(closeadj)
    result = _slope_pct(pre, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqdc21d_slope_v147_signal(revenue, assets, ppnenet, closeadj):
    # rid=147
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans / closeadj.replace(0, np.nan)
    result = _slope_diff_norm(pre, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqxcm42d_slope_v148_signal(revenue, assets, ppnenet, closeadj):
    # rid=148
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 21)
    result = _slope_pct(pre, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqxcm6363d_slope_v149_signal(revenue, assets, ppnenet, closeadj):
    # rid=149
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 63)
    result = _slope_diff_norm(pre, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atosqxcm126126d_slope_v150_signal(revenue, assets, ppnenet, closeadj):
    # rid=150
    base = _f43_asset_turnover(revenue, assets)
    trans = base * base.abs()
    pre = trans * _mean(closeadj, 126)
    result = _slope_pct(pre, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43rce_f43_renewable_capital_efficiency_atorawxc5d_slope_v001_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxlc10d_slope_v002_signal,
    f43rce_f43_renewable_capital_efficiency_atorawdc21d_slope_v003_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm42d_slope_v004_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm6363d_slope_v005_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm126126d_slope_v006_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcz5d_slope_v007_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcr10d_slope_v008_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcr6321d_slope_v009_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc42d_slope_v010_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc63d_slope_v011_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc126d_slope_v012_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc5d_slope_v013_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc10d_slope_v014_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc21d_slope_v015_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc42d_slope_v016_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc63d_slope_v017_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc126d_slope_v018_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm5d_slope_v019_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm10d_slope_v020_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm21d_slope_v021_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm6342d_slope_v022_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm6363d_slope_v023_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm63126d_slope_v024_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm1265d_slope_v025_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm12610d_slope_v026_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm12621d_slope_v027_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz42d_slope_v028_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz63d_slope_v029_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz126d_slope_v030_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr5d_slope_v031_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr10d_slope_v032_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr21d_slope_v033_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr6342d_slope_v034_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr6363d_slope_v035_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr63126d_slope_v036_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc5d_slope_v037_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc10d_slope_v038_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc21d_slope_v039_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc42d_slope_v040_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc63d_slope_v041_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc126d_slope_v042_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc5d_slope_v043_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc10d_slope_v044_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc21d_slope_v045_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm42d_slope_v046_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm63d_slope_v047_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm126d_slope_v048_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm635d_slope_v049_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm6310d_slope_v050_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm6321d_slope_v051_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm12642d_slope_v052_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm12663d_slope_v053_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm126126d_slope_v054_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz5d_slope_v055_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz10d_slope_v056_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz21d_slope_v057_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr42d_slope_v058_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr63d_slope_v059_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr126d_slope_v060_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr635d_slope_v061_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr6310d_slope_v062_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr6321d_slope_v063_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc42d_slope_v064_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc63d_slope_v065_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc126d_slope_v066_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc5d_slope_v067_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc10d_slope_v068_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc21d_slope_v069_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc42d_slope_v070_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc63d_slope_v071_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc126d_slope_v072_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm5d_slope_v073_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm10d_slope_v074_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm21d_slope_v075_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm6342d_slope_v076_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm6363d_slope_v077_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm63126d_slope_v078_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm1265d_slope_v079_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm12610d_slope_v080_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm12621d_slope_v081_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcz42d_slope_v082_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcz63d_slope_v083_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcz126d_slope_v084_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr5d_slope_v085_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr10d_slope_v086_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr21d_slope_v087_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr6342d_slope_v088_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr6363d_slope_v089_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcr63126d_slope_v090_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxc5d_slope_v091_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxc10d_slope_v092_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxc21d_slope_v093_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxlc42d_slope_v094_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxlc63d_slope_v095_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxlc126d_slope_v096_signal,
    f43rce_f43_renewable_capital_efficiency_atoemadc5d_slope_v097_signal,
    f43rce_f43_renewable_capital_efficiency_atoemadc10d_slope_v098_signal,
    f43rce_f43_renewable_capital_efficiency_atoemadc21d_slope_v099_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm42d_slope_v100_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm63d_slope_v101_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm126d_slope_v102_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm635d_slope_v103_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm6310d_slope_v104_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm6321d_slope_v105_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm12642d_slope_v106_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm12663d_slope_v107_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcm126126d_slope_v108_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcz5d_slope_v109_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcz10d_slope_v110_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcz21d_slope_v111_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr42d_slope_v112_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr63d_slope_v113_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr126d_slope_v114_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr635d_slope_v115_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr6310d_slope_v116_signal,
    f43rce_f43_renewable_capital_efficiency_atoemaxcr6321d_slope_v117_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxc42d_slope_v118_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxlc63d_slope_v119_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsdc126d_slope_v120_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcm5d_slope_v121_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcm6310d_slope_v122_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcm12621d_slope_v123_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcz42d_slope_v124_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcr63d_slope_v125_signal,
    f43rce_f43_renewable_capital_efficiency_atoabsxcr63126d_slope_v126_signal,
    f43rce_f43_renewable_capital_efficiency_atologxc5d_slope_v127_signal,
    f43rce_f43_renewable_capital_efficiency_atologxlc10d_slope_v128_signal,
    f43rce_f43_renewable_capital_efficiency_atologdc21d_slope_v129_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcm42d_slope_v130_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcm6363d_slope_v131_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcm126126d_slope_v132_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcz5d_slope_v133_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcr10d_slope_v134_signal,
    f43rce_f43_renewable_capital_efficiency_atologxcr6321d_slope_v135_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxc42d_slope_v136_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxlc63d_slope_v137_signal,
    f43rce_f43_renewable_capital_efficiency_atosigndc126d_slope_v138_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcm5d_slope_v139_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcm6310d_slope_v140_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcm12621d_slope_v141_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcz42d_slope_v142_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcr63d_slope_v143_signal,
    f43rce_f43_renewable_capital_efficiency_atosignxcr63126d_slope_v144_signal,
    f43rce_f43_renewable_capital_efficiency_atosqxc5d_slope_v145_signal,
    f43rce_f43_renewable_capital_efficiency_atosqxlc10d_slope_v146_signal,
    f43rce_f43_renewable_capital_efficiency_atosqdc21d_slope_v147_signal,
    f43rce_f43_renewable_capital_efficiency_atosqxcm42d_slope_v148_signal,
    f43rce_f43_renewable_capital_efficiency_atosqxcm6363d_slope_v149_signal,
    f43rce_f43_renewable_capital_efficiency_atosqxcm126126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_RENEWABLE_CAPITAL_EFFICIENCY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f43_asset_turnover", "_f43_capital_efficiency", "_f43_efficiency_compound")
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
    print(f"OK f43_renewable_capital_efficiency_2nd_derivatives_001_150_claude: {n_features} features pass")
