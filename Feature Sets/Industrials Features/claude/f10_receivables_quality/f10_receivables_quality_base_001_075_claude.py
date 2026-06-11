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
def _f10_dso(receivables, revenue):
    # DSO: receivables / revenue * 365 (days sales outstanding proxy)
    return receivables / revenue.replace(0, np.nan).abs() * 365.0


def _f10_rec_revenue_gap(receivables, revenue, w):
    rec_g = receivables.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return rec_g - rev_g


def _f10_collection_efficiency(receivables, revenue, w):
    # efficiency = -change in receivables / revenue (higher = better collection)
    rec_chg = receivables.diff(periods=w)
    return -rec_chg / revenue.replace(0, np.nan).abs()


# 21d mean DSO * closeadj
def f10rcq_f10_receivables_quality_dso_21d_base_v001_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean DSO
def f10rcq_f10_receivables_quality_dso_63d_base_v002_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean DSO
def f10rcq_f10_receivables_quality_dso_126d_base_v003_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean DSO
def f10rcq_f10_receivables_quality_dso_252d_base_v004_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean DSO
def f10rcq_f10_receivables_quality_dso_504d_base_v005_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rec-rev gap * close
def f10rcq_f10_receivables_quality_gap_21d_base_v006_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap
def f10rcq_f10_receivables_quality_gap_63d_base_v007_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gap
def f10rcq_f10_receivables_quality_gap_126d_base_v008_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap
def f10rcq_f10_receivables_quality_gap_252d_base_v009_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap
def f10rcq_f10_receivables_quality_gap_504d_base_v010_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d collection efficiency
def f10rcq_f10_receivables_quality_coll_21d_base_v011_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coll
def f10rcq_f10_receivables_quality_coll_63d_base_v012_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coll
def f10rcq_f10_receivables_quality_coll_126d_base_v013_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coll
def f10rcq_f10_receivables_quality_coll_252d_base_v014_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coll
def f10rcq_f10_receivables_quality_coll_504d_base_v015_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d DSO
def f10rcq_f10_receivables_quality_dso_5d_base_v016_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d DSO
def f10rcq_f10_receivables_quality_dso_10d_base_v017_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d DSO
def f10rcq_f10_receivables_quality_dso_42d_base_v018_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d DSO
def f10rcq_f10_receivables_quality_dso_189d_base_v019_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d DSO
def f10rcq_f10_receivables_quality_dso_378d_base_v020_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d gap
def f10rcq_f10_receivables_quality_gap_5d_base_v021_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d gap
def f10rcq_f10_receivables_quality_gap_10d_base_v022_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gap
def f10rcq_f10_receivables_quality_gap_42d_base_v023_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d gap
def f10rcq_f10_receivables_quality_gap_189d_base_v024_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d gap
def f10rcq_f10_receivables_quality_gap_378d_base_v025_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std DSO
def f10rcq_f10_receivables_quality_dsostd_21d_base_v026_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std DSO
def f10rcq_f10_receivables_quality_dsostd_63d_base_v027_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std DSO
def f10rcq_f10_receivables_quality_dsostd_252d_base_v028_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std DSO
def f10rcq_f10_receivables_quality_dsostd_504d_base_v029_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std coll
def f10rcq_f10_receivables_quality_collstd_21d_base_v030_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std coll
def f10rcq_f10_receivables_quality_collstd_63d_base_v031_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std coll
def f10rcq_f10_receivables_quality_collstd_252d_base_v032_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std coll
def f10rcq_f10_receivables_quality_collstd_504d_base_v033_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z DSO
def f10rcq_f10_receivables_quality_dsoz_21d_base_v034_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z DSO
def f10rcq_f10_receivables_quality_dsoz_63d_base_v035_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z DSO
def f10rcq_f10_receivables_quality_dsoz_252d_base_v036_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z DSO
def f10rcq_f10_receivables_quality_dsoz_504d_base_v037_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z coll
def f10rcq_f10_receivables_quality_collz_21d_base_v038_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z coll
def f10rcq_f10_receivables_quality_collz_63d_base_v039_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z coll
def f10rcq_f10_receivables_quality_collz_252d_base_v040_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z coll
def f10rcq_f10_receivables_quality_collz_504d_base_v041_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA DSO
def f10rcq_f10_receivables_quality_dsoema_21d_base_v042_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA DSO
def f10rcq_f10_receivables_quality_dsoema_63d_base_v043_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA DSO
def f10rcq_f10_receivables_quality_dsoema_252d_base_v044_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA coll
def f10rcq_f10_receivables_quality_collema_21d_base_v045_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA coll
def f10rcq_f10_receivables_quality_collema_63d_base_v046_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA coll
def f10rcq_f10_receivables_quality_collema_252d_base_v047_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 DSO gap
def f10rcq_f10_receivables_quality_dsogap_21v252_base_v048_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 DSO gap
def f10rcq_f10_receivables_quality_dsogap_63v252_base_v049_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v504 DSO gap
def f10rcq_f10_receivables_quality_dsogap_63v504_base_v050_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126v504 DSO gap
def f10rcq_f10_receivables_quality_dsogap_126v504_base_v051_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 126) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ratio 21v252
def f10rcq_f10_receivables_quality_dsoratio_21v252_base_v052_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ratio 63v252
def f10rcq_f10_receivables_quality_dsoratio_63v252_base_v053_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ratio 63v504
def f10rcq_f10_receivables_quality_dsoratio_63v504_base_v054_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * close^2 21d
def f10rcq_f10_receivables_quality_dsoxprice_21d_base_v055_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * close^2 63d
def f10rcq_f10_receivables_quality_dsoxprice_63d_base_v056_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * close^2 252d
def f10rcq_f10_receivables_quality_dsoxprice_252d_base_v057_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * revenue 63d
def f10rcq_f10_receivables_quality_dsoxrev_63d_base_v058_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b * revenue, 63) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * revenue 252d
def f10rcq_f10_receivables_quality_dsoxrev_252d_base_v059_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b * revenue, 252) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap * revenue 63d
def f10rcq_f10_receivables_quality_gapxrev_63d_base_v060_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# gap * revenue 252d
def f10rcq_f10_receivables_quality_gapxrev_252d_base_v061_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * coll 63d composite
def f10rcq_f10_receivables_quality_dsoxcoll_63d_base_v062_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 63)
    result = (_mean(d, 63) * c) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * coll 252d composite
def f10rcq_f10_receivables_quality_dsoxcoll_252d_base_v063_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    result = (_mean(d, 252) * c) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO squared 63d
def f10rcq_f10_receivables_quality_dsosq_63d_base_v064_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b * b, 63) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO squared 252d
def f10rcq_f10_receivables_quality_dsosq_252d_base_v065_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b * b, 252) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# gap squared 63d
def f10rcq_f10_receivables_quality_gapsq_63d_base_v066_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap squared 252d
def f10rcq_f10_receivables_quality_gapsq_252d_base_v067_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap * close return 21d
def f10rcq_f10_receivables_quality_gapxcret_21d_base_v068_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    cret = closeadj.pct_change(21)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap * close return 63d
def f10rcq_f10_receivables_quality_gapxcret_63d_base_v069_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    cret = closeadj.pct_change(63)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap * close return 252d
def f10rcq_f10_receivables_quality_gapxcret_252d_base_v070_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    cret = closeadj.pct_change(252)
    result = g * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt DSO 63d
def f10rcq_f10_receivables_quality_dsosqrt_63d_base_v071_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue).abs()
    result = np.sqrt(_mean(b, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt DSO 252d
def f10rcq_f10_receivables_quality_dsosqrt_252d_base_v072_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue).abs()
    result = np.sqrt(_mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log DSO 252d
def f10rcq_f10_receivables_quality_dsolog_252d_base_v073_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll cum 252d
def f10rcq_f10_receivables_quality_collcum_252d_base_v074_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = c.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll cum 504d
def f10rcq_f10_receivables_quality_collcum_504d_base_v075_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = c.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rcq_f10_receivables_quality_dso_21d_base_v001_signal,
    f10rcq_f10_receivables_quality_dso_63d_base_v002_signal,
    f10rcq_f10_receivables_quality_dso_126d_base_v003_signal,
    f10rcq_f10_receivables_quality_dso_252d_base_v004_signal,
    f10rcq_f10_receivables_quality_dso_504d_base_v005_signal,
    f10rcq_f10_receivables_quality_gap_21d_base_v006_signal,
    f10rcq_f10_receivables_quality_gap_63d_base_v007_signal,
    f10rcq_f10_receivables_quality_gap_126d_base_v008_signal,
    f10rcq_f10_receivables_quality_gap_252d_base_v009_signal,
    f10rcq_f10_receivables_quality_gap_504d_base_v010_signal,
    f10rcq_f10_receivables_quality_coll_21d_base_v011_signal,
    f10rcq_f10_receivables_quality_coll_63d_base_v012_signal,
    f10rcq_f10_receivables_quality_coll_126d_base_v013_signal,
    f10rcq_f10_receivables_quality_coll_252d_base_v014_signal,
    f10rcq_f10_receivables_quality_coll_504d_base_v015_signal,
    f10rcq_f10_receivables_quality_dso_5d_base_v016_signal,
    f10rcq_f10_receivables_quality_dso_10d_base_v017_signal,
    f10rcq_f10_receivables_quality_dso_42d_base_v018_signal,
    f10rcq_f10_receivables_quality_dso_189d_base_v019_signal,
    f10rcq_f10_receivables_quality_dso_378d_base_v020_signal,
    f10rcq_f10_receivables_quality_gap_5d_base_v021_signal,
    f10rcq_f10_receivables_quality_gap_10d_base_v022_signal,
    f10rcq_f10_receivables_quality_gap_42d_base_v023_signal,
    f10rcq_f10_receivables_quality_gap_189d_base_v024_signal,
    f10rcq_f10_receivables_quality_gap_378d_base_v025_signal,
    f10rcq_f10_receivables_quality_dsostd_21d_base_v026_signal,
    f10rcq_f10_receivables_quality_dsostd_63d_base_v027_signal,
    f10rcq_f10_receivables_quality_dsostd_252d_base_v028_signal,
    f10rcq_f10_receivables_quality_dsostd_504d_base_v029_signal,
    f10rcq_f10_receivables_quality_collstd_21d_base_v030_signal,
    f10rcq_f10_receivables_quality_collstd_63d_base_v031_signal,
    f10rcq_f10_receivables_quality_collstd_252d_base_v032_signal,
    f10rcq_f10_receivables_quality_collstd_504d_base_v033_signal,
    f10rcq_f10_receivables_quality_dsoz_21d_base_v034_signal,
    f10rcq_f10_receivables_quality_dsoz_63d_base_v035_signal,
    f10rcq_f10_receivables_quality_dsoz_252d_base_v036_signal,
    f10rcq_f10_receivables_quality_dsoz_504d_base_v037_signal,
    f10rcq_f10_receivables_quality_collz_21d_base_v038_signal,
    f10rcq_f10_receivables_quality_collz_63d_base_v039_signal,
    f10rcq_f10_receivables_quality_collz_252d_base_v040_signal,
    f10rcq_f10_receivables_quality_collz_504d_base_v041_signal,
    f10rcq_f10_receivables_quality_dsoema_21d_base_v042_signal,
    f10rcq_f10_receivables_quality_dsoema_63d_base_v043_signal,
    f10rcq_f10_receivables_quality_dsoema_252d_base_v044_signal,
    f10rcq_f10_receivables_quality_collema_21d_base_v045_signal,
    f10rcq_f10_receivables_quality_collema_63d_base_v046_signal,
    f10rcq_f10_receivables_quality_collema_252d_base_v047_signal,
    f10rcq_f10_receivables_quality_dsogap_21v252_base_v048_signal,
    f10rcq_f10_receivables_quality_dsogap_63v252_base_v049_signal,
    f10rcq_f10_receivables_quality_dsogap_63v504_base_v050_signal,
    f10rcq_f10_receivables_quality_dsogap_126v504_base_v051_signal,
    f10rcq_f10_receivables_quality_dsoratio_21v252_base_v052_signal,
    f10rcq_f10_receivables_quality_dsoratio_63v252_base_v053_signal,
    f10rcq_f10_receivables_quality_dsoratio_63v504_base_v054_signal,
    f10rcq_f10_receivables_quality_dsoxprice_21d_base_v055_signal,
    f10rcq_f10_receivables_quality_dsoxprice_63d_base_v056_signal,
    f10rcq_f10_receivables_quality_dsoxprice_252d_base_v057_signal,
    f10rcq_f10_receivables_quality_dsoxrev_63d_base_v058_signal,
    f10rcq_f10_receivables_quality_dsoxrev_252d_base_v059_signal,
    f10rcq_f10_receivables_quality_gapxrev_63d_base_v060_signal,
    f10rcq_f10_receivables_quality_gapxrev_252d_base_v061_signal,
    f10rcq_f10_receivables_quality_dsoxcoll_63d_base_v062_signal,
    f10rcq_f10_receivables_quality_dsoxcoll_252d_base_v063_signal,
    f10rcq_f10_receivables_quality_dsosq_63d_base_v064_signal,
    f10rcq_f10_receivables_quality_dsosq_252d_base_v065_signal,
    f10rcq_f10_receivables_quality_gapsq_63d_base_v066_signal,
    f10rcq_f10_receivables_quality_gapsq_252d_base_v067_signal,
    f10rcq_f10_receivables_quality_gapxcret_21d_base_v068_signal,
    f10rcq_f10_receivables_quality_gapxcret_63d_base_v069_signal,
    f10rcq_f10_receivables_quality_gapxcret_252d_base_v070_signal,
    f10rcq_f10_receivables_quality_dsosqrt_63d_base_v071_signal,
    f10rcq_f10_receivables_quality_dsosqrt_252d_base_v072_signal,
    f10rcq_f10_receivables_quality_dsolog_252d_base_v073_signal,
    f10rcq_f10_receivables_quality_collcum_252d_base_v074_signal,
    f10rcq_f10_receivables_quality_collcum_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RECEIVABLES_QUALITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "receivables": receivables, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_dso", "_f10_rec_revenue_gap", "_f10_collection_efficiency")
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
    print(f"OK f10_receivables_quality_base_001_075_claude: {n_features} features pass")
