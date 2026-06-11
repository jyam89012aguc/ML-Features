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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f10_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan).abs() * 365.0


def _f10_rec_revenue_gap(receivables, revenue, w):
    rec_g = receivables.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return rec_g - rev_g


def _f10_collection_efficiency(receivables, revenue, w):
    rec_chg = receivables.diff(periods=w)
    return -rec_chg / revenue.replace(0, np.nan).abs()


def f10rcq_f10_receivables_quality_dso_21d_slope_v001_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 21) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_21d_slope_v002_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_63d_slope_v003_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_63d_slope_v004_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 63) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_126d_slope_v005_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 126) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_126d_slope_v006_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 126) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_252d_slope_v007_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 252) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_252d_slope_v008_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_504d_slope_v009_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 504) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_504d_slope_v010_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_21d_slope_v011_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_21d_slope_v012_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_63d_slope_v013_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_126d_slope_v014_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 126) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_252d_slope_v015_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_504d_slope_v016_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_21d_slope_v017_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_21d_slope_v018_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_63d_slope_v019_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_126d_slope_v020_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 126) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_252d_slope_v021_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_504d_slope_v022_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_5d_slope_v023_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 5) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_10d_slope_v024_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 10) * closeadj
    return _slope_pct(base, 10).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_42d_slope_v025_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 42) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_189d_slope_v026_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 189) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_378d_slope_v027_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 378) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_5d_slope_v028_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 5) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_10d_slope_v029_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 10) * closeadj
    return _slope_diff_norm(base, 10).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_42d_slope_v030_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 42) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_189d_slope_v031_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 189) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gap_378d_slope_v032_signal(receivables, revenue, closeadj):
    base = _f10_rec_revenue_gap(receivables, revenue, 378) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsostd_21d_slope_v033_signal(receivables, revenue, closeadj):
    base = _std(_f10_dso(receivables, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsostd_63d_slope_v034_signal(receivables, revenue, closeadj):
    base = _std(_f10_dso(receivables, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsostd_252d_slope_v035_signal(receivables, revenue, closeadj):
    base = _std(_f10_dso(receivables, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsostd_504d_slope_v036_signal(receivables, revenue, closeadj):
    base = _std(_f10_dso(receivables, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collstd_21d_slope_v037_signal(receivables, revenue, closeadj):
    base = _std(_f10_collection_efficiency(receivables, revenue, 21), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collstd_63d_slope_v038_signal(receivables, revenue, closeadj):
    base = _std(_f10_collection_efficiency(receivables, revenue, 21), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collstd_252d_slope_v039_signal(receivables, revenue, closeadj):
    base = _std(_f10_collection_efficiency(receivables, revenue, 21), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collstd_504d_slope_v040_signal(receivables, revenue, closeadj):
    base = _std(_f10_collection_efficiency(receivables, revenue, 21), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoz_21d_slope_v041_signal(receivables, revenue, closeadj):
    base = _z(_f10_dso(receivables, revenue), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoz_63d_slope_v042_signal(receivables, revenue, closeadj):
    base = _z(_f10_dso(receivables, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoz_252d_slope_v043_signal(receivables, revenue, closeadj):
    base = _z(_f10_dso(receivables, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoz_504d_slope_v044_signal(receivables, revenue, closeadj):
    base = _z(_f10_dso(receivables, revenue), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collz_21d_slope_v045_signal(receivables, revenue, closeadj):
    base = _z(_f10_collection_efficiency(receivables, revenue, 21), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collz_63d_slope_v046_signal(receivables, revenue, closeadj):
    base = _z(_f10_collection_efficiency(receivables, revenue, 21), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collz_252d_slope_v047_signal(receivables, revenue, closeadj):
    base = _z(_f10_collection_efficiency(receivables, revenue, 21), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collz_504d_slope_v048_signal(receivables, revenue, closeadj):
    base = _z(_f10_collection_efficiency(receivables, revenue, 21), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoema_21d_slope_v049_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoema_63d_slope_v050_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoema_252d_slope_v051_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collema_21d_slope_v052_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collema_63d_slope_v053_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collema_252d_slope_v054_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsogap_21v252_slope_v055_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsogap_63v252_slope_v056_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsogap_63v504_slope_v057_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsogap_126v504_slope_v058_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoratio_21v252_slope_v059_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 21) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoratio_63v252_slope_v060_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 63) / _mean(b, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoratio_63v504_slope_v061_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 63) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxprice_63d_slope_v062_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b, 63) * closeadj * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxprice_252d_slope_v063_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b, 252) * closeadj * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxrev_63d_slope_v064_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b * revenue, 63) * closeadj / 1e9
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxrev_252d_slope_v065_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b * revenue, 252) * closeadj / 1e9
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapxrev_63d_slope_v066_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapxrev_252d_slope_v067_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxcoll_63d_slope_v068_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 63)
    base = (_mean(d, 63) * c) * closeadj / 100
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxcoll_252d_slope_v069_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    base = (_mean(d, 252) * c) * closeadj / 100
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsosq_63d_slope_v070_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b * b, 63) * closeadj / 100
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsosq_252d_slope_v071_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b * b, 252) * closeadj / 100
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapsq_63d_slope_v072_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapsq_252d_slope_v073_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapxcret_63d_slope_v074_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    cret = closeadj.pct_change(63)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapxcret_252d_slope_v075_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    cret = closeadj.pct_change(252)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsosqrt_252d_slope_v076_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue).abs()
    base = np.sqrt(_mean(b, 252)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsolog_252d_slope_v077_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = np.log(_mean(b, 252).replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collcum_252d_slope_v078_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = c.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collcum_504d_slope_v079_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = c.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsomax_252d_slope_v080_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = b.rolling(252, min_periods=63).max() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsomax_504d_slope_v081_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = b.rolling(504, min_periods=126).max() * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsomin_252d_slope_v082_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = b.rolling(252, min_periods=63).min() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsorng_252d_slope_v083_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    base = rng * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsopct_252d_slope_v084_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsopct_504d_slope_v085_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsocv_63d_slope_v086_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsocv_252d_slope_v087_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_comp_63d_slope_v088_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = (_mean(d, 63) / 100 + g) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_comp_252d_slope_v089_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = (_mean(d, 252) / 100 + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_comp_504d_slope_v090_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 504)
    base = (_mean(d, 504) / 100 + g) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxcumcl_63d_slope_v091_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 63) * closeadj
    base = _mean(b, 63) * cv / 100
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxcumcl_252d_slope_v092_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 252) * closeadj
    base = _mean(b, 252) * cv / 100
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapz_21d_slope_v093_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = _z(g, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapz_63d_slope_v094_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = _z(g, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapz_252d_slope_v095_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = _z(g, 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapstd_63d_slope_v096_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = _std(g, 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapstd_252d_slope_v097_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = _std(g, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapabs_63d_slope_v098_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = g.abs() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapabs_252d_slope_v099_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = g.abs() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapcum_252d_slope_v100_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapcum_504d_slope_v101_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = g.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_excesscount_252d_slope_v102_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    excess = (g > 0.05).astype(float)
    base = (excess.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_excesscount_504d_slope_v103_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    excess = (g > 0.05).astype(float)
    base = (excess.rolling(504, min_periods=126).sum() + g) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxrec_63d_slope_v104_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b, 63) * receivables * closeadj / 1e10
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxrec_252d_slope_v105_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = _mean(b, 252) * receivables * closeadj / 1e10
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collxrev_63d_slope_v106_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 63)
    base = c * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collxrev_252d_slope_v107_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 252)
    base = c * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsolevel_63d_slope_v108_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsolevel_252d_slope_v109_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    base = norm * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collzxcret_21d_slope_v110_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    z = _z(c, 252)
    cret = closeadj.pct_change(21)
    base = z * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collzxcret_63d_slope_v111_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 63)
    z = _z(c, 252)
    cret = closeadj.pct_change(63)
    base = z * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collzxcret_252d_slope_v112_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 252)
    z = _z(c, 504)
    cret = closeadj.pct_change(252)
    base = z * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_badrisk_252d_slope_v113_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    risk = ((g > 0.05) & (d > _mean(d, 252))).astype(float)
    base = (risk.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_badrisk_504d_slope_v114_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    risk = ((g > 0.05) & (d > _mean(d, 252))).astype(float)
    base = (risk.rolling(504, min_periods=126).sum() + g) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_goodcount_252d_slope_v115_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    good = ((g < -0.05) & (d < _mean(d, 252))).astype(float)
    base = (good.rolling(252, min_periods=63).sum() + g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_arar_63d_slope_v116_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    base = _mean(b, 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_arar_252d_slope_v117_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    base = _mean(b, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_arar_504d_slope_v118_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    base = _mean(b, 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_colllong_slope_v119_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsolong_slope_v120_signal(receivables, revenue, closeadj):
    base = _f10_dso(receivables, revenue) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_recgrwscaled_63d_slope_v121_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    rev_g = revenue.pct_change(63)
    base = g / (rev_g.abs() + 0.01) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_recgrwscaled_252d_slope_v122_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    rev_g = revenue.pct_change(252)
    base = g / (rev_g.abs() + 0.01) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoemagap_63v252_slope_v123_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    e63 = b.ewm(span=63, adjust=False).mean()
    e252 = b.ewm(span=252, adjust=False).mean()
    base = (e63 - e252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoemagap_21v252_slope_v124_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    e21 = b.ewm(span=21, adjust=False).mean()
    e252 = b.ewm(span=252, adjust=False).mean()
    base = (e21 - e252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collemagap_21v252_slope_v125_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    e21 = c.ewm(span=21, adjust=False).mean()
    e252 = c.ewm(span=252, adjust=False).mean()
    base = (e21 - e252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_qualcomp_63d_slope_v126_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 63)
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    base = (-_mean(d, 63) / 100 + c - g) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_qualcomp_252d_slope_v127_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    base = (-_mean(d, 252) / 100 + c - g) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxret_21d_slope_v128_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cret = closeadj.pct_change(21)
    base = b * cret * closeadj / 100
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxret_252d_slope_v129_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cret = closeadj.pct_change(252)
    base = b * cret * closeadj / 100
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gappct_252d_slope_v130_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    mx = g.rolling(252, min_periods=63).max()
    mn = g.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((g - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collpct_252d_slope_v131_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    mx = c.rolling(252, min_periods=63).max()
    mn = c.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((c - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collmax_252d_slope_v132_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = c.rolling(252, min_periods=63).max() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collmin_252d_slope_v133_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = c.rolling(252, min_periods=63).min() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collrng_252d_slope_v134_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    rng = c.rolling(252, min_periods=63).max() - c.rolling(252, min_periods=63).min()
    base = rng * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxvolp_252d_slope_v135_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 252) * closeadj
    base = _mean(b, 252) * cv / 100
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_compfull_504d_slope_v136_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    g = _f10_rec_revenue_gap(receivables, revenue, 504)
    base = (_mean(d, 504) / 100 + c + g) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoratio_21v504_slope_v137_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 21) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoratio_126v504_slope_v138_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = (_mean(b, 126) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collratio_63v252_slope_v139_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = (_mean(c, 63) / _mean(c, 252).replace(0, np.nan).abs()) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_riskz_63d_slope_v140_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = _z(d, 63) * _z(c, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_riskz_252d_slope_v141_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 21)
    base = _z(d, 252) * _z(c, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_gapcumz_252d_slope_v142_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = (g.rolling(252, min_periods=63).sum() + _z(g, 252)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoworst_504d_slope_v143_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = b.expanding(min_periods=126).max() / b.expanding(min_periods=126).mean().replace(0, np.nan)
    base = base * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsobest_504d_slope_v144_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    base = b.expanding(min_periods=126).min() / b.expanding(min_periods=126).mean().replace(0, np.nan)
    base = base * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoflip_252d_slope_v145_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    chg = b.diff(21)
    flips = (np.sign(chg).diff().abs() > 1).astype(float)
    base = (flips.rolling(252, min_periods=63).sum() + b) * closeadj / 100
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsosign_63d_slope_v146_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    dev = b - _mean(b, 252)
    base = np.sign(dev) * _std(b, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_collsign_63d_slope_v147_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    dev = c - _mean(c, 252)
    base = np.sign(dev) * _std(c, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dsoxarsq_63d_slope_v148_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    ar_rev = b / 365.0
    base = _mean(b * ar_rev, 63) * closeadj / 100
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_dso_252d_long_slope_v149_signal(receivables, revenue, closeadj):
    base = _mean(_f10_dso(receivables, revenue), 252) * closeadj
    return _slope_pct(base, 252).replace([np.inf, -np.inf], np.nan)


def f10rcq_f10_receivables_quality_coll_252d_long_slope_v150_signal(receivables, revenue, closeadj):
    base = _f10_collection_efficiency(receivables, revenue, 252) * closeadj
    return _slope_diff_norm(base, 252).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rcq_f10_receivables_quality_dso_21d_slope_v001_signal,
    f10rcq_f10_receivables_quality_dso_21d_slope_v002_signal,
    f10rcq_f10_receivables_quality_dso_63d_slope_v003_signal,
    f10rcq_f10_receivables_quality_dso_63d_slope_v004_signal,
    f10rcq_f10_receivables_quality_dso_126d_slope_v005_signal,
    f10rcq_f10_receivables_quality_dso_126d_slope_v006_signal,
    f10rcq_f10_receivables_quality_dso_252d_slope_v007_signal,
    f10rcq_f10_receivables_quality_dso_252d_slope_v008_signal,
    f10rcq_f10_receivables_quality_dso_504d_slope_v009_signal,
    f10rcq_f10_receivables_quality_dso_504d_slope_v010_signal,
    f10rcq_f10_receivables_quality_gap_21d_slope_v011_signal,
    f10rcq_f10_receivables_quality_gap_21d_slope_v012_signal,
    f10rcq_f10_receivables_quality_gap_63d_slope_v013_signal,
    f10rcq_f10_receivables_quality_gap_126d_slope_v014_signal,
    f10rcq_f10_receivables_quality_gap_252d_slope_v015_signal,
    f10rcq_f10_receivables_quality_gap_504d_slope_v016_signal,
    f10rcq_f10_receivables_quality_coll_21d_slope_v017_signal,
    f10rcq_f10_receivables_quality_coll_21d_slope_v018_signal,
    f10rcq_f10_receivables_quality_coll_63d_slope_v019_signal,
    f10rcq_f10_receivables_quality_coll_126d_slope_v020_signal,
    f10rcq_f10_receivables_quality_coll_252d_slope_v021_signal,
    f10rcq_f10_receivables_quality_coll_504d_slope_v022_signal,
    f10rcq_f10_receivables_quality_dso_5d_slope_v023_signal,
    f10rcq_f10_receivables_quality_dso_10d_slope_v024_signal,
    f10rcq_f10_receivables_quality_dso_42d_slope_v025_signal,
    f10rcq_f10_receivables_quality_dso_189d_slope_v026_signal,
    f10rcq_f10_receivables_quality_dso_378d_slope_v027_signal,
    f10rcq_f10_receivables_quality_gap_5d_slope_v028_signal,
    f10rcq_f10_receivables_quality_gap_10d_slope_v029_signal,
    f10rcq_f10_receivables_quality_gap_42d_slope_v030_signal,
    f10rcq_f10_receivables_quality_gap_189d_slope_v031_signal,
    f10rcq_f10_receivables_quality_gap_378d_slope_v032_signal,
    f10rcq_f10_receivables_quality_dsostd_21d_slope_v033_signal,
    f10rcq_f10_receivables_quality_dsostd_63d_slope_v034_signal,
    f10rcq_f10_receivables_quality_dsostd_252d_slope_v035_signal,
    f10rcq_f10_receivables_quality_dsostd_504d_slope_v036_signal,
    f10rcq_f10_receivables_quality_collstd_21d_slope_v037_signal,
    f10rcq_f10_receivables_quality_collstd_63d_slope_v038_signal,
    f10rcq_f10_receivables_quality_collstd_252d_slope_v039_signal,
    f10rcq_f10_receivables_quality_collstd_504d_slope_v040_signal,
    f10rcq_f10_receivables_quality_dsoz_21d_slope_v041_signal,
    f10rcq_f10_receivables_quality_dsoz_63d_slope_v042_signal,
    f10rcq_f10_receivables_quality_dsoz_252d_slope_v043_signal,
    f10rcq_f10_receivables_quality_dsoz_504d_slope_v044_signal,
    f10rcq_f10_receivables_quality_collz_21d_slope_v045_signal,
    f10rcq_f10_receivables_quality_collz_63d_slope_v046_signal,
    f10rcq_f10_receivables_quality_collz_252d_slope_v047_signal,
    f10rcq_f10_receivables_quality_collz_504d_slope_v048_signal,
    f10rcq_f10_receivables_quality_dsoema_21d_slope_v049_signal,
    f10rcq_f10_receivables_quality_dsoema_63d_slope_v050_signal,
    f10rcq_f10_receivables_quality_dsoema_252d_slope_v051_signal,
    f10rcq_f10_receivables_quality_collema_21d_slope_v052_signal,
    f10rcq_f10_receivables_quality_collema_63d_slope_v053_signal,
    f10rcq_f10_receivables_quality_collema_252d_slope_v054_signal,
    f10rcq_f10_receivables_quality_dsogap_21v252_slope_v055_signal,
    f10rcq_f10_receivables_quality_dsogap_63v252_slope_v056_signal,
    f10rcq_f10_receivables_quality_dsogap_63v504_slope_v057_signal,
    f10rcq_f10_receivables_quality_dsogap_126v504_slope_v058_signal,
    f10rcq_f10_receivables_quality_dsoratio_21v252_slope_v059_signal,
    f10rcq_f10_receivables_quality_dsoratio_63v252_slope_v060_signal,
    f10rcq_f10_receivables_quality_dsoratio_63v504_slope_v061_signal,
    f10rcq_f10_receivables_quality_dsoxprice_63d_slope_v062_signal,
    f10rcq_f10_receivables_quality_dsoxprice_252d_slope_v063_signal,
    f10rcq_f10_receivables_quality_dsoxrev_63d_slope_v064_signal,
    f10rcq_f10_receivables_quality_dsoxrev_252d_slope_v065_signal,
    f10rcq_f10_receivables_quality_gapxrev_63d_slope_v066_signal,
    f10rcq_f10_receivables_quality_gapxrev_252d_slope_v067_signal,
    f10rcq_f10_receivables_quality_dsoxcoll_63d_slope_v068_signal,
    f10rcq_f10_receivables_quality_dsoxcoll_252d_slope_v069_signal,
    f10rcq_f10_receivables_quality_dsosq_63d_slope_v070_signal,
    f10rcq_f10_receivables_quality_dsosq_252d_slope_v071_signal,
    f10rcq_f10_receivables_quality_gapsq_63d_slope_v072_signal,
    f10rcq_f10_receivables_quality_gapsq_252d_slope_v073_signal,
    f10rcq_f10_receivables_quality_gapxcret_63d_slope_v074_signal,
    f10rcq_f10_receivables_quality_gapxcret_252d_slope_v075_signal,
    f10rcq_f10_receivables_quality_dsosqrt_252d_slope_v076_signal,
    f10rcq_f10_receivables_quality_dsolog_252d_slope_v077_signal,
    f10rcq_f10_receivables_quality_collcum_252d_slope_v078_signal,
    f10rcq_f10_receivables_quality_collcum_504d_slope_v079_signal,
    f10rcq_f10_receivables_quality_dsomax_252d_slope_v080_signal,
    f10rcq_f10_receivables_quality_dsomax_504d_slope_v081_signal,
    f10rcq_f10_receivables_quality_dsomin_252d_slope_v082_signal,
    f10rcq_f10_receivables_quality_dsorng_252d_slope_v083_signal,
    f10rcq_f10_receivables_quality_dsopct_252d_slope_v084_signal,
    f10rcq_f10_receivables_quality_dsopct_504d_slope_v085_signal,
    f10rcq_f10_receivables_quality_dsocv_63d_slope_v086_signal,
    f10rcq_f10_receivables_quality_dsocv_252d_slope_v087_signal,
    f10rcq_f10_receivables_quality_comp_63d_slope_v088_signal,
    f10rcq_f10_receivables_quality_comp_252d_slope_v089_signal,
    f10rcq_f10_receivables_quality_comp_504d_slope_v090_signal,
    f10rcq_f10_receivables_quality_dsoxcumcl_63d_slope_v091_signal,
    f10rcq_f10_receivables_quality_dsoxcumcl_252d_slope_v092_signal,
    f10rcq_f10_receivables_quality_gapz_21d_slope_v093_signal,
    f10rcq_f10_receivables_quality_gapz_63d_slope_v094_signal,
    f10rcq_f10_receivables_quality_gapz_252d_slope_v095_signal,
    f10rcq_f10_receivables_quality_gapstd_63d_slope_v096_signal,
    f10rcq_f10_receivables_quality_gapstd_252d_slope_v097_signal,
    f10rcq_f10_receivables_quality_gapabs_63d_slope_v098_signal,
    f10rcq_f10_receivables_quality_gapabs_252d_slope_v099_signal,
    f10rcq_f10_receivables_quality_gapcum_252d_slope_v100_signal,
    f10rcq_f10_receivables_quality_gapcum_504d_slope_v101_signal,
    f10rcq_f10_receivables_quality_excesscount_252d_slope_v102_signal,
    f10rcq_f10_receivables_quality_excesscount_504d_slope_v103_signal,
    f10rcq_f10_receivables_quality_dsoxrec_63d_slope_v104_signal,
    f10rcq_f10_receivables_quality_dsoxrec_252d_slope_v105_signal,
    f10rcq_f10_receivables_quality_collxrev_63d_slope_v106_signal,
    f10rcq_f10_receivables_quality_collxrev_252d_slope_v107_signal,
    f10rcq_f10_receivables_quality_dsolevel_63d_slope_v108_signal,
    f10rcq_f10_receivables_quality_dsolevel_252d_slope_v109_signal,
    f10rcq_f10_receivables_quality_collzxcret_21d_slope_v110_signal,
    f10rcq_f10_receivables_quality_collzxcret_63d_slope_v111_signal,
    f10rcq_f10_receivables_quality_collzxcret_252d_slope_v112_signal,
    f10rcq_f10_receivables_quality_badrisk_252d_slope_v113_signal,
    f10rcq_f10_receivables_quality_badrisk_504d_slope_v114_signal,
    f10rcq_f10_receivables_quality_goodcount_252d_slope_v115_signal,
    f10rcq_f10_receivables_quality_arar_63d_slope_v116_signal,
    f10rcq_f10_receivables_quality_arar_252d_slope_v117_signal,
    f10rcq_f10_receivables_quality_arar_504d_slope_v118_signal,
    f10rcq_f10_receivables_quality_colllong_slope_v119_signal,
    f10rcq_f10_receivables_quality_dsolong_slope_v120_signal,
    f10rcq_f10_receivables_quality_recgrwscaled_63d_slope_v121_signal,
    f10rcq_f10_receivables_quality_recgrwscaled_252d_slope_v122_signal,
    f10rcq_f10_receivables_quality_dsoemagap_63v252_slope_v123_signal,
    f10rcq_f10_receivables_quality_dsoemagap_21v252_slope_v124_signal,
    f10rcq_f10_receivables_quality_collemagap_21v252_slope_v125_signal,
    f10rcq_f10_receivables_quality_qualcomp_63d_slope_v126_signal,
    f10rcq_f10_receivables_quality_qualcomp_252d_slope_v127_signal,
    f10rcq_f10_receivables_quality_dsoxret_21d_slope_v128_signal,
    f10rcq_f10_receivables_quality_dsoxret_252d_slope_v129_signal,
    f10rcq_f10_receivables_quality_gappct_252d_slope_v130_signal,
    f10rcq_f10_receivables_quality_collpct_252d_slope_v131_signal,
    f10rcq_f10_receivables_quality_collmax_252d_slope_v132_signal,
    f10rcq_f10_receivables_quality_collmin_252d_slope_v133_signal,
    f10rcq_f10_receivables_quality_collrng_252d_slope_v134_signal,
    f10rcq_f10_receivables_quality_dsoxvolp_252d_slope_v135_signal,
    f10rcq_f10_receivables_quality_compfull_504d_slope_v136_signal,
    f10rcq_f10_receivables_quality_dsoratio_21v504_slope_v137_signal,
    f10rcq_f10_receivables_quality_dsoratio_126v504_slope_v138_signal,
    f10rcq_f10_receivables_quality_collratio_63v252_slope_v139_signal,
    f10rcq_f10_receivables_quality_riskz_63d_slope_v140_signal,
    f10rcq_f10_receivables_quality_riskz_252d_slope_v141_signal,
    f10rcq_f10_receivables_quality_gapcumz_252d_slope_v142_signal,
    f10rcq_f10_receivables_quality_dsoworst_504d_slope_v143_signal,
    f10rcq_f10_receivables_quality_dsobest_504d_slope_v144_signal,
    f10rcq_f10_receivables_quality_dsoflip_252d_slope_v145_signal,
    f10rcq_f10_receivables_quality_dsosign_63d_slope_v146_signal,
    f10rcq_f10_receivables_quality_collsign_63d_slope_v147_signal,
    f10rcq_f10_receivables_quality_dsoxarsq_63d_slope_v148_signal,
    f10rcq_f10_receivables_quality_dso_252d_long_slope_v149_signal,
    f10rcq_f10_receivables_quality_coll_252d_long_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RECEIVABLES_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f10_receivables_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
