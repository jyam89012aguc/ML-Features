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
def _f24_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan) * 365.0


def _f24_receivables_growth_gap(receivables, revenue, w):
    rg = receivables.pct_change(periods=w)
    sg = revenue.pct_change(periods=w)
    return rg - sg


def _f24_collection_efficiency(receivables, revenue, w):
    dso = receivables / revenue.replace(0, np.nan) * 365.0
    m = dso.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = dso.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return -((dso - m) / sd)

# ===== features =====

def f24rqc_f24_receivables_quality_consumer_dso_5d_sl5_slope_v001_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 5) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_10d_sl10_slope_v002_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 10) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_21d_sl21_slope_v003_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 21) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_42d_sl42_slope_v004_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 42) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_63d_sl63_slope_v005_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 63) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_84d_sl126_slope_v006_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 84) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_126d_sl5_slope_v007_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 126) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_168d_sl10_slope_v008_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 168) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_189d_sl21_slope_v009_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 189) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_252d_sl42_slope_v010_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 252) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_315d_sl63_slope_v011_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 315) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_378d_sl126_slope_v012_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 378) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dso_504d_sl5_slope_v013_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _mean(base, 504) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_5d_sl10_slope_v014_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 5) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_10d_sl21_slope_v015_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 10) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_21d_sl42_slope_v016_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 21) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_42d_sl63_slope_v017_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 42) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_63d_sl126_slope_v018_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 63) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_84d_sl5_slope_v019_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 84) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_126d_sl10_slope_v020_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 126) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_168d_sl21_slope_v021_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 168) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_189d_sl42_slope_v022_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 189) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_252d_sl63_slope_v023_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 252) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_315d_sl126_slope_v024_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 315) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_378d_sl5_slope_v025_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 378) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsostd_504d_sl10_slope_v026_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _std(base, 504) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_5d_sl21_slope_v027_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 5) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_10d_sl42_slope_v028_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 10) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_21d_sl63_slope_v029_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 21) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_42d_sl126_slope_v030_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 42) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_63d_sl5_slope_v031_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 63) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_84d_sl10_slope_v032_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 84) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_126d_sl21_slope_v033_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 126) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_168d_sl42_slope_v034_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 168) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_189d_sl63_slope_v035_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 189) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_252d_sl126_slope_v036_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 252) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_315d_sl5_slope_v037_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 315) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_378d_sl10_slope_v038_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 378) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoz_504d_sl21_slope_v039_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _z(base, 504) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_5d_sl42_slope_v040_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 5) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_10d_sl63_slope_v041_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 10) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_21d_sl126_slope_v042_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 21) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_42d_sl5_slope_v043_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 42) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_63d_sl10_slope_v044_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 63) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_84d_sl21_slope_v045_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 84) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_126d_sl42_slope_v046_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 126) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_168d_sl63_slope_v047_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 168) * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_189d_sl126_slope_v048_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 189) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_252d_sl5_slope_v049_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 252) * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_315d_sl10_slope_v050_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 315) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_378d_sl21_slope_v051_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 378) * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoema_504d_sl42_slope_v052_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    result = _ema(base, 504) * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_5d_sl63_slope_v053_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_10d_sl126_slope_v054_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_21d_sl5_slope_v055_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_42d_sl10_slope_v056_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_63d_sl21_slope_v057_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_84d_sl42_slope_v058_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_126d_sl63_slope_v059_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_168d_sl126_slope_v060_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_189d_sl5_slope_v061_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_252d_sl10_slope_v062_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_315d_sl21_slope_v063_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_378d_sl42_slope_v064_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgap_504d_sl63_slope_v065_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_5d_sl126_slope_v066_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = _mean(base, 5) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_10d_sl5_slope_v067_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = _mean(base, 10) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_21d_sl10_slope_v068_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = _mean(base, 21) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_42d_sl21_slope_v069_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = _mean(base, 42) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_63d_sl42_slope_v070_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = _mean(base, 63) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_84d_sl63_slope_v071_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = _mean(base, 84) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_126d_sl126_slope_v072_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = _mean(base, 126) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_168d_sl5_slope_v073_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = _mean(base, 168) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_189d_sl10_slope_v074_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = _mean(base, 189) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_252d_sl21_slope_v075_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = _mean(base, 252) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_315d_sl42_slope_v076_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = _mean(base, 315) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_378d_sl63_slope_v077_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = _mean(base, 378) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapmean_504d_sl126_slope_v078_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = _mean(base, 504) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_5d_sl5_slope_v079_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = _std(base, 5) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_10d_sl10_slope_v080_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = _std(base, 10) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_21d_sl21_slope_v081_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = _std(base, 21) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_42d_sl42_slope_v082_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = _std(base, 42) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_63d_sl63_slope_v083_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = _std(base, 63) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_84d_sl126_slope_v084_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = _std(base, 84) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_126d_sl5_slope_v085_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = _std(base, 126) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_168d_sl10_slope_v086_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = _std(base, 168) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_189d_sl21_slope_v087_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = _std(base, 189) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_252d_sl42_slope_v088_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = _std(base, 252) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_315d_sl63_slope_v089_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = _std(base, 315) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_378d_sl126_slope_v090_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = _std(base, 378) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapstd_504d_sl5_slope_v091_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = _std(base, 504) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_5d_sl10_slope_v092_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 5)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_10d_sl21_slope_v093_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 10)
    result = base.abs() * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_21d_sl42_slope_v094_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 21)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_42d_sl63_slope_v095_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 42)
    result = base.abs() * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_63d_sl126_slope_v096_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 63)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_84d_sl5_slope_v097_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 84)
    result = base.abs() * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_126d_sl10_slope_v098_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 126)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_168d_sl21_slope_v099_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 168)
    result = base.abs() * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_189d_sl42_slope_v100_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 189)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_252d_sl63_slope_v101_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 252)
    result = base.abs() * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_315d_sl126_slope_v102_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 315)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_378d_sl5_slope_v103_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 378)
    result = base.abs() * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_recgrgapabs_504d_sl10_slope_v104_signal(receivables, revenue, closeadj):
    base = _f24_receivables_growth_gap(receivables, revenue, 504)
    result = base.abs() * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_5d_sl21_slope_v105_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_10d_sl42_slope_v106_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_21d_sl63_slope_v107_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_42d_sl126_slope_v108_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_63d_sl5_slope_v109_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_84d_sl10_slope_v110_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_126d_sl21_slope_v111_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_168d_sl42_slope_v112_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = base * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_189d_sl63_slope_v113_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = base * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_252d_sl126_slope_v114_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = base * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_315d_sl5_slope_v115_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = base * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_378d_sl10_slope_v116_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = base * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleff_504d_sl21_slope_v117_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = base * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_5d_sl42_slope_v118_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = _ema(base, 5) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_10d_sl63_slope_v119_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = _ema(base, 10) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_21d_sl126_slope_v120_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = _ema(base, 21) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_42d_sl5_slope_v121_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = _ema(base, 42) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_63d_sl10_slope_v122_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = _ema(base, 63) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_84d_sl21_slope_v123_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = _ema(base, 84) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_126d_sl42_slope_v124_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = _ema(base, 126) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_168d_sl63_slope_v125_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = _ema(base, 168) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_189d_sl126_slope_v126_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = _ema(base, 189) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_252d_sl5_slope_v127_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = _ema(base, 252) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_315d_sl10_slope_v128_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = _ema(base, 315) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_378d_sl21_slope_v129_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = _ema(base, 378) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffema_504d_sl42_slope_v130_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = _ema(base, 504) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_5d_sl63_slope_v131_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 5)
    result = _std(base, 5) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_10d_sl126_slope_v132_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 10)
    result = _std(base, 10) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_21d_sl5_slope_v133_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 21)
    result = _std(base, 21) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_42d_sl10_slope_v134_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 42)
    result = _std(base, 42) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_63d_sl21_slope_v135_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 63)
    result = _std(base, 63) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_84d_sl42_slope_v136_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 84)
    result = _std(base, 84) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_126d_sl63_slope_v137_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 126)
    result = _std(base, 126) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_168d_sl126_slope_v138_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 168)
    result = _std(base, 168) * closeadj
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_189d_sl5_slope_v139_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 189)
    result = _std(base, 189) * closeadj
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_252d_sl10_slope_v140_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 252)
    result = _std(base, 252) * closeadj
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_315d_sl21_slope_v141_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 315)
    result = _std(base, 315) * closeadj
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_378d_sl42_slope_v142_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 378)
    result = _std(base, 378) * closeadj
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_colleffstd_504d_sl63_slope_v143_signal(receivables, revenue, closeadj):
    base = _f24_collection_efficiency(receivables, revenue, 504)
    result = _std(base, 504) * closeadj
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_5d_sl126_slope_v144_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=5)
    result = base * rg * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_10d_sl5_slope_v145_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=10)
    result = base * rg * (closeadj / 100.0)
    result = _slope_pct(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_21d_sl10_slope_v146_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=21)
    result = base * rg * (closeadj / 100.0)
    result = _slope_diff_norm(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_42d_sl21_slope_v147_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=42)
    result = base * rg * (closeadj / 100.0)
    result = _slope_pct(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_63d_sl42_slope_v148_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=63)
    result = base * rg * (closeadj / 100.0)
    result = _slope_diff_norm(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_84d_sl63_slope_v149_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=84)
    result = base * rg * (closeadj / 100.0)
    result = _slope_pct(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24rqc_f24_receivables_quality_consumer_dsoxrec_126d_sl126_slope_v150_signal(receivables, revenue, closeadj):
    base = _f24_dso(receivables, revenue)
    rg = receivables.pct_change(periods=126)
    result = base * rg * (closeadj / 100.0)
    result = _slope_diff_norm(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24rqc_f24_receivables_quality_consumer_dso_5d_sl5_slope_v001_signal,
    f24rqc_f24_receivables_quality_consumer_dso_10d_sl10_slope_v002_signal,
    f24rqc_f24_receivables_quality_consumer_dso_21d_sl21_slope_v003_signal,
    f24rqc_f24_receivables_quality_consumer_dso_42d_sl42_slope_v004_signal,
    f24rqc_f24_receivables_quality_consumer_dso_63d_sl63_slope_v005_signal,
    f24rqc_f24_receivables_quality_consumer_dso_84d_sl126_slope_v006_signal,
    f24rqc_f24_receivables_quality_consumer_dso_126d_sl5_slope_v007_signal,
    f24rqc_f24_receivables_quality_consumer_dso_168d_sl10_slope_v008_signal,
    f24rqc_f24_receivables_quality_consumer_dso_189d_sl21_slope_v009_signal,
    f24rqc_f24_receivables_quality_consumer_dso_252d_sl42_slope_v010_signal,
    f24rqc_f24_receivables_quality_consumer_dso_315d_sl63_slope_v011_signal,
    f24rqc_f24_receivables_quality_consumer_dso_378d_sl126_slope_v012_signal,
    f24rqc_f24_receivables_quality_consumer_dso_504d_sl5_slope_v013_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_5d_sl10_slope_v014_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_10d_sl21_slope_v015_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_21d_sl42_slope_v016_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_42d_sl63_slope_v017_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_63d_sl126_slope_v018_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_84d_sl5_slope_v019_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_126d_sl10_slope_v020_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_168d_sl21_slope_v021_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_189d_sl42_slope_v022_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_252d_sl63_slope_v023_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_315d_sl126_slope_v024_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_378d_sl5_slope_v025_signal,
    f24rqc_f24_receivables_quality_consumer_dsostd_504d_sl10_slope_v026_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_5d_sl21_slope_v027_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_10d_sl42_slope_v028_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_21d_sl63_slope_v029_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_42d_sl126_slope_v030_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_63d_sl5_slope_v031_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_84d_sl10_slope_v032_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_126d_sl21_slope_v033_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_168d_sl42_slope_v034_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_189d_sl63_slope_v035_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_252d_sl126_slope_v036_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_315d_sl5_slope_v037_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_378d_sl10_slope_v038_signal,
    f24rqc_f24_receivables_quality_consumer_dsoz_504d_sl21_slope_v039_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_5d_sl42_slope_v040_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_10d_sl63_slope_v041_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_21d_sl126_slope_v042_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_42d_sl5_slope_v043_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_63d_sl10_slope_v044_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_84d_sl21_slope_v045_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_126d_sl42_slope_v046_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_168d_sl63_slope_v047_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_189d_sl126_slope_v048_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_252d_sl5_slope_v049_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_315d_sl10_slope_v050_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_378d_sl21_slope_v051_signal,
    f24rqc_f24_receivables_quality_consumer_dsoema_504d_sl42_slope_v052_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_5d_sl63_slope_v053_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_10d_sl126_slope_v054_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_21d_sl5_slope_v055_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_42d_sl10_slope_v056_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_63d_sl21_slope_v057_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_84d_sl42_slope_v058_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_126d_sl63_slope_v059_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_168d_sl126_slope_v060_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_189d_sl5_slope_v061_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_252d_sl10_slope_v062_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_315d_sl21_slope_v063_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_378d_sl42_slope_v064_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgap_504d_sl63_slope_v065_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_5d_sl126_slope_v066_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_10d_sl5_slope_v067_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_21d_sl10_slope_v068_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_42d_sl21_slope_v069_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_63d_sl42_slope_v070_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_84d_sl63_slope_v071_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_126d_sl126_slope_v072_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_168d_sl5_slope_v073_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_189d_sl10_slope_v074_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_252d_sl21_slope_v075_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_315d_sl42_slope_v076_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_378d_sl63_slope_v077_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapmean_504d_sl126_slope_v078_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_5d_sl5_slope_v079_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_10d_sl10_slope_v080_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_21d_sl21_slope_v081_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_42d_sl42_slope_v082_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_63d_sl63_slope_v083_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_84d_sl126_slope_v084_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_126d_sl5_slope_v085_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_168d_sl10_slope_v086_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_189d_sl21_slope_v087_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_252d_sl42_slope_v088_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_315d_sl63_slope_v089_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_378d_sl126_slope_v090_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapstd_504d_sl5_slope_v091_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_5d_sl10_slope_v092_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_10d_sl21_slope_v093_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_21d_sl42_slope_v094_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_42d_sl63_slope_v095_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_63d_sl126_slope_v096_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_84d_sl5_slope_v097_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_126d_sl10_slope_v098_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_168d_sl21_slope_v099_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_189d_sl42_slope_v100_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_252d_sl63_slope_v101_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_315d_sl126_slope_v102_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_378d_sl5_slope_v103_signal,
    f24rqc_f24_receivables_quality_consumer_recgrgapabs_504d_sl10_slope_v104_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_5d_sl21_slope_v105_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_10d_sl42_slope_v106_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_21d_sl63_slope_v107_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_42d_sl126_slope_v108_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_63d_sl5_slope_v109_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_84d_sl10_slope_v110_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_126d_sl21_slope_v111_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_168d_sl42_slope_v112_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_189d_sl63_slope_v113_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_252d_sl126_slope_v114_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_315d_sl5_slope_v115_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_378d_sl10_slope_v116_signal,
    f24rqc_f24_receivables_quality_consumer_colleff_504d_sl21_slope_v117_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_5d_sl42_slope_v118_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_10d_sl63_slope_v119_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_21d_sl126_slope_v120_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_42d_sl5_slope_v121_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_63d_sl10_slope_v122_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_84d_sl21_slope_v123_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_126d_sl42_slope_v124_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_168d_sl63_slope_v125_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_189d_sl126_slope_v126_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_252d_sl5_slope_v127_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_315d_sl10_slope_v128_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_378d_sl21_slope_v129_signal,
    f24rqc_f24_receivables_quality_consumer_colleffema_504d_sl42_slope_v130_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_5d_sl63_slope_v131_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_10d_sl126_slope_v132_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_21d_sl5_slope_v133_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_42d_sl10_slope_v134_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_63d_sl21_slope_v135_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_84d_sl42_slope_v136_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_126d_sl63_slope_v137_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_168d_sl126_slope_v138_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_189d_sl5_slope_v139_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_252d_sl10_slope_v140_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_315d_sl21_slope_v141_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_378d_sl42_slope_v142_signal,
    f24rqc_f24_receivables_quality_consumer_colleffstd_504d_sl63_slope_v143_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_5d_sl126_slope_v144_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_10d_sl5_slope_v145_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_21d_sl10_slope_v146_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_42d_sl21_slope_v147_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_63d_sl42_slope_v148_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_84d_sl63_slope_v149_signal,
    f24rqc_f24_receivables_quality_consumer_dsoxrec_126d_sl126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_RECEIVABLES_QUALITY_CONSUMER_REGISTRY_SLOPE_001_150 = REGISTRY


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
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "receivables": receivables,
        "revenue": revenue,
        "closeadj": closeadj,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_dso", "_f24_receivables_growth_gap", "_f24_collection_efficiency",)
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
    print(f"OK f24_receivables_quality_consumer_2nd_derivatives_001_150_claude: {n_features} features pass")
