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
def _f27_revenue_floor(revenue, w):
    # floor over window — captures the non-cyclical baseline
    return revenue.rolling(w, min_periods=max(1, w // 2)).min()


def _f27_non_cyclical_share_proxy(revenue, w):
    # share of trailing min vs trailing mean — durable revenue share proxy
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / m.replace(0, np.nan)


def _f27_durability_score(revenue, ebitdamargin, w):
    # durability: stability of margin × stability of revenue (lower std = higher durability)
    rsd = revenue.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    msd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / ((rsd.replace(0, np.nan) + 1e-6) * (msd.replace(0, np.nan) + 1e-6))


# v001 21d revenue floor / revenue × close
def f27rrd_f27_repair_remodel_durability_floor_21d_base_v001_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 21) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_63d_base_v002_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_126d_base_v003_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 126) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_252d_base_v004_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_504d_base_v005_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_5d_base_v006_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 5) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_42d_base_v007_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 42) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_189d_base_v008_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 189) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_378d_base_v009_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 378) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share proxy windows
def f27rrd_f27_repair_remodel_durability_share_21d_base_v010_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_63d_base_v011_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_126d_base_v012_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_252d_base_v013_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_504d_base_v014_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_42d_base_v015_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_189d_base_v016_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_378d_base_v017_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# durability score
def f27rrd_f27_repair_remodel_durability_dur_21d_base_v018_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 21)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_63d_base_v019_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 63)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_126d_base_v020_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 126)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_252d_base_v021_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_504d_base_v022_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 504)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_42d_base_v023_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 42)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_189d_base_v024_signal(revenue, ebitdamargin, closeadj):
    base = _f27_durability_score(revenue, ebitdamargin, 189)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor mean
def f27rrd_f27_repair_remodel_durability_floorma_21d_base_v025_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorma_63d_base_v026_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorstd_63d_base_v027_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorstd_252d_base_v028_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorz_63d_base_v029_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorz_252d_base_v030_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share mean/std/z
def f27rrd_f27_repair_remodel_durability_sharema_21d_base_v031_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharema_63d_base_v032_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharestd_63d_base_v033_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharestd_252d_base_v034_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 504)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharez_63d_base_v035_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharez_252d_base_v036_signal(revenue, closeadj):
    base = _f27_non_cyclical_share_proxy(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# durability mean/std/z
def f27rrd_f27_repair_remodel_durability_durma_63d_base_v037_signal(revenue, ebitdamargin, closeadj):
    base = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durma_252d_base_v038_signal(revenue, ebitdamargin, closeadj):
    base = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durstd_252d_base_v039_signal(revenue, ebitdamargin, closeadj):
    base = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durz_63d_base_v040_signal(revenue, ebitdamargin, closeadj):
    base = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durz_252d_base_v041_signal(revenue, ebitdamargin, closeadj):
    base = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite floor × share × close
def f27rrd_f27_repair_remodel_durability_floorxshare_63d_base_v042_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = f * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxshare_252d_base_v043_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = f * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor × durability
def f27rrd_f27_repair_remodel_durability_floorxdur_63d_base_v044_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = f * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxdur_252d_base_v045_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = f * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share × durability
def f27rrd_f27_repair_remodel_durability_sharexdur_63d_base_v046_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = s * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexdur_252d_base_v047_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = s * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor log × close
def f27rrd_f27_repair_remodel_durability_floorlog_63d_base_v048_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63)
    result = np.log(f.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorlog_252d_base_v049_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252)
    result = np.log(f.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor diff (rate of erosion)
def f27rrd_f27_repair_remodel_durability_floordiff_21d_base_v050_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63)
    result = f.diff(21) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floordiff_63d_base_v051_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252)
    result = f.diff(63) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share diff
def f27rrd_f27_repair_remodel_durability_sharediff_21d_base_v052_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharediff_63d_base_v053_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = s.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# durability sign × close
def f27rrd_f27_repair_remodel_durability_durdiff_63d_base_v054_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durdiff_252d_base_v055_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor × ebitdamargin
def f27rrd_f27_repair_remodel_durability_floorxebmgn_63d_base_v056_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = f * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxebmgn_252d_base_v057_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = f * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share × ebitdamargin
def f27rrd_f27_repair_remodel_durability_sharexebmgn_63d_base_v058_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexebmgn_252d_base_v059_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = s * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EMA versions
def f27rrd_f27_repair_remodel_durability_floorema_21d_base_v060_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = f.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorema_63d_base_v061_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = f.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareema_21d_base_v062_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareema_63d_base_v063_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = s.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# quantile rank
def f27rrd_f27_repair_remodel_durability_floorrank_252d_base_v064_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    rank = f.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharerank_252d_base_v065_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    rank = s.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durrank_252d_base_v066_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    rank = d.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor squared
def f27rrd_f27_repair_remodel_durability_floorsq_63d_base_v067_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = f * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharesq_63d_base_v068_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor sign × close
def f27rrd_f27_repair_remodel_durability_floorlogpx_252d_base_v069_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = f * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# durability log × log close × close
def f27rrd_f27_repair_remodel_durability_durxlogpx_63d_base_v070_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = d * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor × close drawdown
def f27rrd_f27_repair_remodel_durability_floorxpkgap_252d_base_v071_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = f * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share × close drawdown
def f27rrd_f27_repair_remodel_durability_sharexpkgap_252d_base_v072_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    result = s * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# floor × close detrended
def f27rrd_f27_repair_remodel_durability_floorxpxdet_252d_base_v073_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    result = f * det * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite full
def f27rrd_f27_repair_remodel_durability_compo3_252d_base_v074_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (f + s + d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# weighted composite
def f27rrd_f27_repair_remodel_durability_compow_252d_base_v075_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (0.5 * f + 0.3 * s + 0.2 * d) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27rrd_f27_repair_remodel_durability_floor_21d_base_v001_signal,
    f27rrd_f27_repair_remodel_durability_floor_63d_base_v002_signal,
    f27rrd_f27_repair_remodel_durability_floor_126d_base_v003_signal,
    f27rrd_f27_repair_remodel_durability_floor_252d_base_v004_signal,
    f27rrd_f27_repair_remodel_durability_floor_504d_base_v005_signal,
    f27rrd_f27_repair_remodel_durability_floor_5d_base_v006_signal,
    f27rrd_f27_repair_remodel_durability_floor_42d_base_v007_signal,
    f27rrd_f27_repair_remodel_durability_floor_189d_base_v008_signal,
    f27rrd_f27_repair_remodel_durability_floor_378d_base_v009_signal,
    f27rrd_f27_repair_remodel_durability_share_21d_base_v010_signal,
    f27rrd_f27_repair_remodel_durability_share_63d_base_v011_signal,
    f27rrd_f27_repair_remodel_durability_share_126d_base_v012_signal,
    f27rrd_f27_repair_remodel_durability_share_252d_base_v013_signal,
    f27rrd_f27_repair_remodel_durability_share_504d_base_v014_signal,
    f27rrd_f27_repair_remodel_durability_share_42d_base_v015_signal,
    f27rrd_f27_repair_remodel_durability_share_189d_base_v016_signal,
    f27rrd_f27_repair_remodel_durability_share_378d_base_v017_signal,
    f27rrd_f27_repair_remodel_durability_dur_21d_base_v018_signal,
    f27rrd_f27_repair_remodel_durability_dur_63d_base_v019_signal,
    f27rrd_f27_repair_remodel_durability_dur_126d_base_v020_signal,
    f27rrd_f27_repair_remodel_durability_dur_252d_base_v021_signal,
    f27rrd_f27_repair_remodel_durability_dur_504d_base_v022_signal,
    f27rrd_f27_repair_remodel_durability_dur_42d_base_v023_signal,
    f27rrd_f27_repair_remodel_durability_dur_189d_base_v024_signal,
    f27rrd_f27_repair_remodel_durability_floorma_21d_base_v025_signal,
    f27rrd_f27_repair_remodel_durability_floorma_63d_base_v026_signal,
    f27rrd_f27_repair_remodel_durability_floorstd_63d_base_v027_signal,
    f27rrd_f27_repair_remodel_durability_floorstd_252d_base_v028_signal,
    f27rrd_f27_repair_remodel_durability_floorz_63d_base_v029_signal,
    f27rrd_f27_repair_remodel_durability_floorz_252d_base_v030_signal,
    f27rrd_f27_repair_remodel_durability_sharema_21d_base_v031_signal,
    f27rrd_f27_repair_remodel_durability_sharema_63d_base_v032_signal,
    f27rrd_f27_repair_remodel_durability_sharestd_63d_base_v033_signal,
    f27rrd_f27_repair_remodel_durability_sharestd_252d_base_v034_signal,
    f27rrd_f27_repair_remodel_durability_sharez_63d_base_v035_signal,
    f27rrd_f27_repair_remodel_durability_sharez_252d_base_v036_signal,
    f27rrd_f27_repair_remodel_durability_durma_63d_base_v037_signal,
    f27rrd_f27_repair_remodel_durability_durma_252d_base_v038_signal,
    f27rrd_f27_repair_remodel_durability_durstd_252d_base_v039_signal,
    f27rrd_f27_repair_remodel_durability_durz_63d_base_v040_signal,
    f27rrd_f27_repair_remodel_durability_durz_252d_base_v041_signal,
    f27rrd_f27_repair_remodel_durability_floorxshare_63d_base_v042_signal,
    f27rrd_f27_repair_remodel_durability_floorxshare_252d_base_v043_signal,
    f27rrd_f27_repair_remodel_durability_floorxdur_63d_base_v044_signal,
    f27rrd_f27_repair_remodel_durability_floorxdur_252d_base_v045_signal,
    f27rrd_f27_repair_remodel_durability_sharexdur_63d_base_v046_signal,
    f27rrd_f27_repair_remodel_durability_sharexdur_252d_base_v047_signal,
    f27rrd_f27_repair_remodel_durability_floorlog_63d_base_v048_signal,
    f27rrd_f27_repair_remodel_durability_floorlog_252d_base_v049_signal,
    f27rrd_f27_repair_remodel_durability_floordiff_21d_base_v050_signal,
    f27rrd_f27_repair_remodel_durability_floordiff_63d_base_v051_signal,
    f27rrd_f27_repair_remodel_durability_sharediff_21d_base_v052_signal,
    f27rrd_f27_repair_remodel_durability_sharediff_63d_base_v053_signal,
    f27rrd_f27_repair_remodel_durability_durdiff_63d_base_v054_signal,
    f27rrd_f27_repair_remodel_durability_durdiff_252d_base_v055_signal,
    f27rrd_f27_repair_remodel_durability_floorxebmgn_63d_base_v056_signal,
    f27rrd_f27_repair_remodel_durability_floorxebmgn_252d_base_v057_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgn_63d_base_v058_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgn_252d_base_v059_signal,
    f27rrd_f27_repair_remodel_durability_floorema_21d_base_v060_signal,
    f27rrd_f27_repair_remodel_durability_floorema_63d_base_v061_signal,
    f27rrd_f27_repair_remodel_durability_shareema_21d_base_v062_signal,
    f27rrd_f27_repair_remodel_durability_shareema_63d_base_v063_signal,
    f27rrd_f27_repair_remodel_durability_floorrank_252d_base_v064_signal,
    f27rrd_f27_repair_remodel_durability_sharerank_252d_base_v065_signal,
    f27rrd_f27_repair_remodel_durability_durrank_252d_base_v066_signal,
    f27rrd_f27_repair_remodel_durability_floorsq_63d_base_v067_signal,
    f27rrd_f27_repair_remodel_durability_sharesq_63d_base_v068_signal,
    f27rrd_f27_repair_remodel_durability_floorlogpx_252d_base_v069_signal,
    f27rrd_f27_repair_remodel_durability_durxlogpx_63d_base_v070_signal,
    f27rrd_f27_repair_remodel_durability_floorxpkgap_252d_base_v071_signal,
    f27rrd_f27_repair_remodel_durability_sharexpkgap_252d_base_v072_signal,
    f27rrd_f27_repair_remodel_durability_floorxpxdet_252d_base_v073_signal,
    f27rrd_f27_repair_remodel_durability_compo3_252d_base_v074_signal,
    f27rrd_f27_repair_remodel_durability_compow_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REPAIR_REMODEL_DURABILITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_revenue_floor", "_f27_non_cyclical_share_proxy", "_f27_durability_score")
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
    print(f"OK f27_repair_remodel_durability_base_001_075_claude: {n_features} features pass")
