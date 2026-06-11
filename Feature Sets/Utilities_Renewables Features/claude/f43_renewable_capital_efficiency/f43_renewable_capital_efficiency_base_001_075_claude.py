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
def _f43_asset_turnover(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f43_capital_efficiency(revenue, ppnenet, w):
    e = revenue / ppnenet.replace(0, np.nan).abs()
    return e.rolling(w, min_periods=max(1, w // 2)).mean()


def _f43_efficiency_compound(revenue, assets, w):
    t = revenue / assets.replace(0, np.nan).abs()
    return t.rolling(w, min_periods=max(1, w // 2)).mean() * np.sqrt(w)

def f43rce_f43_renewable_capital_efficiency_atorawxc_base_v001_signal(revenue, assets, ppnenet, closeadj):
    # rid=1
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxlc_base_v002_signal(revenue, assets, ppnenet, closeadj):
    # rid=2
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawdc_base_v003_signal(revenue, assets, ppnenet, closeadj):
    # rid=3
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm_base_v004_signal(revenue, assets, ppnenet, closeadj):
    # rid=4
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm63_base_v005_signal(revenue, assets, ppnenet, closeadj):
    # rid=5
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcm126_base_v006_signal(revenue, assets, ppnenet, closeadj):
    # rid=6
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcz_base_v007_signal(revenue, assets, ppnenet, closeadj):
    # rid=7
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcr_base_v008_signal(revenue, assets, ppnenet, closeadj):
    # rid=8
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atorawxcr63_base_v009_signal(revenue, assets, ppnenet, closeadj):
    # rid=9
    base = _f43_asset_turnover(revenue, assets)
    trans = base
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v010_signal(revenue, assets, ppnenet, closeadj):
    # rid=10
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v011_signal(revenue, assets, ppnenet, closeadj):
    # rid=11
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v012_signal(revenue, assets, ppnenet, closeadj):
    # rid=12
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v013_signal(revenue, assets, ppnenet, closeadj):
    # rid=13
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v014_signal(revenue, assets, ppnenet, closeadj):
    # rid=14
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v015_signal(revenue, assets, ppnenet, closeadj):
    # rid=15
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc_base_v016_signal(revenue, assets, ppnenet, closeadj):
    # rid=16
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc_base_v017_signal(revenue, assets, ppnenet, closeadj):
    # rid=17
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeandc_base_v018_signal(revenue, assets, ppnenet, closeadj):
    # rid=18
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v019_signal(revenue, assets, ppnenet, closeadj):
    # rid=19
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v020_signal(revenue, assets, ppnenet, closeadj):
    # rid=20
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v021_signal(revenue, assets, ppnenet, closeadj):
    # rid=21
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v022_signal(revenue, assets, ppnenet, closeadj):
    # rid=22
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v023_signal(revenue, assets, ppnenet, closeadj):
    # rid=23
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v024_signal(revenue, assets, ppnenet, closeadj):
    # rid=24
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v025_signal(revenue, assets, ppnenet, closeadj):
    # rid=25
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v026_signal(revenue, assets, ppnenet, closeadj):
    # rid=26
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v027_signal(revenue, assets, ppnenet, closeadj):
    # rid=27
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v028_signal(revenue, assets, ppnenet, closeadj):
    # rid=28
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v029_signal(revenue, assets, ppnenet, closeadj):
    # rid=29
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v030_signal(revenue, assets, ppnenet, closeadj):
    # rid=30
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v031_signal(revenue, assets, ppnenet, closeadj):
    # rid=31
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v032_signal(revenue, assets, ppnenet, closeadj):
    # rid=32
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v033_signal(revenue, assets, ppnenet, closeadj):
    # rid=33
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v034_signal(revenue, assets, ppnenet, closeadj):
    # rid=34
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v035_signal(revenue, assets, ppnenet, closeadj):
    # rid=35
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v036_signal(revenue, assets, ppnenet, closeadj):
    # rid=36
    base = _f43_asset_turnover(revenue, assets)
    trans = _mean(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc_base_v037_signal(revenue, assets, ppnenet, closeadj):
    # rid=37
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc_base_v038_signal(revenue, assets, ppnenet, closeadj):
    # rid=38
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxc_base_v039_signal(revenue, assets, ppnenet, closeadj):
    # rid=39
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v040_signal(revenue, assets, ppnenet, closeadj):
    # rid=40
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v041_signal(revenue, assets, ppnenet, closeadj):
    # rid=41
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v042_signal(revenue, assets, ppnenet, closeadj):
    # rid=42
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc_base_v043_signal(revenue, assets, ppnenet, closeadj):
    # rid=43
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc_base_v044_signal(revenue, assets, ppnenet, closeadj):
    # rid=44
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostddc_base_v045_signal(revenue, assets, ppnenet, closeadj):
    # rid=45
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v046_signal(revenue, assets, ppnenet, closeadj):
    # rid=46
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v047_signal(revenue, assets, ppnenet, closeadj):
    # rid=47
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v048_signal(revenue, assets, ppnenet, closeadj):
    # rid=48
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v049_signal(revenue, assets, ppnenet, closeadj):
    # rid=49
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v050_signal(revenue, assets, ppnenet, closeadj):
    # rid=50
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v051_signal(revenue, assets, ppnenet, closeadj):
    # rid=51
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v052_signal(revenue, assets, ppnenet, closeadj):
    # rid=52
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v053_signal(revenue, assets, ppnenet, closeadj):
    # rid=53
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v054_signal(revenue, assets, ppnenet, closeadj):
    # rid=54
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v055_signal(revenue, assets, ppnenet, closeadj):
    # rid=55
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v056_signal(revenue, assets, ppnenet, closeadj):
    # rid=56
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v057_signal(revenue, assets, ppnenet, closeadj):
    # rid=57
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v058_signal(revenue, assets, ppnenet, closeadj):
    # rid=58
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v059_signal(revenue, assets, ppnenet, closeadj):
    # rid=59
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v060_signal(revenue, assets, ppnenet, closeadj):
    # rid=60
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v061_signal(revenue, assets, ppnenet, closeadj):
    # rid=61
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v062_signal(revenue, assets, ppnenet, closeadj):
    # rid=62
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v063_signal(revenue, assets, ppnenet, closeadj):
    # rid=63
    base = _f43_asset_turnover(revenue, assets)
    trans = _std(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc_base_v064_signal(revenue, assets, ppnenet, closeadj):
    # rid=64
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc_base_v065_signal(revenue, assets, ppnenet, closeadj):
    # rid=65
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxc_base_v066_signal(revenue, assets, ppnenet, closeadj):
    # rid=66
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc_base_v067_signal(revenue, assets, ppnenet, closeadj):
    # rid=67
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc_base_v068_signal(revenue, assets, ppnenet, closeadj):
    # rid=68
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxlc_base_v069_signal(revenue, assets, ppnenet, closeadj):
    # rid=69
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc_base_v070_signal(revenue, assets, ppnenet, closeadj):
    # rid=70
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc_base_v071_signal(revenue, assets, ppnenet, closeadj):
    # rid=71
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozdc_base_v072_signal(revenue, assets, ppnenet, closeadj):
    # rid=72
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm_base_v073_signal(revenue, assets, ppnenet, closeadj):
    # rid=73
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm_base_v074_signal(revenue, assets, ppnenet, closeadj):
    # rid=74
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f43rce_f43_renewable_capital_efficiency_atozxcm_base_v075_signal(revenue, assets, ppnenet, closeadj):
    # rid=75
    base = _f43_asset_turnover(revenue, assets)
    trans = _z(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43rce_f43_renewable_capital_efficiency_atorawxc_base_v001_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxlc_base_v002_signal,
    f43rce_f43_renewable_capital_efficiency_atorawdc_base_v003_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm_base_v004_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm63_base_v005_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcm126_base_v006_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcz_base_v007_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcr_base_v008_signal,
    f43rce_f43_renewable_capital_efficiency_atorawxcr63_base_v009_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v010_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v011_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxc_base_v012_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v013_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v014_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxlc_base_v015_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc_base_v016_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc_base_v017_signal,
    f43rce_f43_renewable_capital_efficiency_atomeandc_base_v018_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v019_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v020_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm_base_v021_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v022_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v023_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm63_base_v024_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v025_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v026_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcm126_base_v027_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v028_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v029_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcz_base_v030_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v031_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v032_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr_base_v033_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v034_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v035_signal,
    f43rce_f43_renewable_capital_efficiency_atomeanxcr63_base_v036_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc_base_v037_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc_base_v038_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxc_base_v039_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v040_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v041_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxlc_base_v042_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc_base_v043_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc_base_v044_signal,
    f43rce_f43_renewable_capital_efficiency_atostddc_base_v045_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v046_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v047_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm_base_v048_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v049_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v050_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm63_base_v051_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v052_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v053_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcm126_base_v054_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v055_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v056_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcz_base_v057_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v058_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v059_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr_base_v060_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v061_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v062_signal,
    f43rce_f43_renewable_capital_efficiency_atostdxcr63_base_v063_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc_base_v064_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc_base_v065_signal,
    f43rce_f43_renewable_capital_efficiency_atozxc_base_v066_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc_base_v067_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc_base_v068_signal,
    f43rce_f43_renewable_capital_efficiency_atozxlc_base_v069_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc_base_v070_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc_base_v071_signal,
    f43rce_f43_renewable_capital_efficiency_atozdc_base_v072_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm_base_v073_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm_base_v074_signal,
    f43rce_f43_renewable_capital_efficiency_atozxcm_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_RENEWABLE_CAPITAL_EFFICIENCY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f43_renewable_capital_efficiency_base_001_075_claude: {n_features} features pass")
