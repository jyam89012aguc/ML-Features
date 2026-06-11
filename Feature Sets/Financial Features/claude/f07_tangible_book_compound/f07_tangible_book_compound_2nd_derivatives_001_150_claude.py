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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f07_tangible_bv(equity, intangibles):
    return equity - intangibles


def _f07_tangible_bvps(equity, intangibles, sharesbas):
    tbv = equity - intangibles
    return tbv / sharesbas.replace(0, np.nan)


def _f07_tbv_growth(equity, intangibles, sharesbas, w):
    tbvps = (equity - intangibles) / sharesbas.replace(0, np.nan)
    return tbvps.pct_change(periods=w)


def f07tbc_f07_tangible_book_compound_tbv_5d_slope_v001_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 5) / _mean(closeadj, 5).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_10d_slope_v002_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 10) / _mean(closeadj, 10).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_21d_slope_v003_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 21) / _mean(closeadj, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_42d_slope_v004_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 42) / _mean(closeadj, 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_63d_slope_v005_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 63) / _mean(closeadj, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_126d_slope_v006_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 126) / _mean(closeadj, 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_189d_slope_v007_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 189) / _mean(closeadj, 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_252d_slope_v008_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 252) / _mean(closeadj, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_378d_slope_v009_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 378) / _mean(closeadj, 378).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_504d_slope_v010_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _mean(base, 504) / _mean(closeadj, 504).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_5d_slope_v011_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 5) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_10d_slope_v012_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 10) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_21d_slope_v013_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_42d_slope_v014_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 42) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_63d_slope_v015_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_126d_slope_v016_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_189d_slope_v017_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 189) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_252d_slope_v018_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_378d_slope_v019_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 378) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_504d_slope_v020_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _mean(base, 504) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_21d_slope_v021_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_63d_slope_v022_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = base * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_126d_slope_v023_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    base_series = base * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_252d_slope_v024_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = base * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_504d_slope_v025_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    base_series = base * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_21d_slope_v026_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _z(base, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_63d_slope_v027_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _z(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_126d_slope_v028_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _z(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_252d_slope_v029_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _z(base, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_21d_slope_v030_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _z(base, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_63d_slope_v031_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _z(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_126d_slope_v032_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _z(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_252d_slope_v033_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _z(base, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_21d_slope_v034_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _std(base, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_63d_slope_v035_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _std(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_126d_slope_v036_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _std(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_252d_slope_v037_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _std(base, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_21d_slope_v038_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _std(base, 21) / _mean(base, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_63d_slope_v039_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _std(base, 63) / _mean(base, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_126d_slope_v040_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _std(base, 126) / _mean(base, 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_252d_slope_v041_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = _std(base, 252) / _mean(base, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_10d_slope_v042_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _ema(base, 10) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_21d_slope_v043_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _ema(base, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_63d_slope_v044_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _ema(base, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_126d_slope_v045_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _ema(base, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_252d_slope_v046_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = _ema(base, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_21d_slope_v047_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    base_series = _ema(base, 21) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_63d_slope_v048_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = _ema(base, 63) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_126d_slope_v049_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    base_series = _ema(base, 126) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_252d_slope_v050_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = _ema(base, 252) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_21d_slope_v051_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    base_series = np.log(base.replace(0, np.nan)) * _mean(closeadj, 21)
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_63d_slope_v052_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    base_series = np.log(base.replace(0, np.nan)) * _mean(closeadj, 63)
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_252d_slope_v053_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    base_series = np.log(base.replace(0, np.nan)) * _mean(closeadj, 252)
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_63d_slope_v054_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_126d_slope_v055_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_252d_slope_v056_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_63d_slope_v057_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_126d_slope_v058_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_252d_slope_v059_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    base_series = rnk * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_5d_slope_v060_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = base.diff(periods=5) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_21d_slope_v061_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = base.diff(periods=21) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_63d_slope_v062_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = base.diff(periods=63) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_126d_slope_v063_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = base.diff(periods=126) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_252d_slope_v064_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = base.diff(periods=252) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_5d_slope_v065_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.diff(periods=5) / _mean(base, 5).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_21d_slope_v066_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.diff(periods=21) / _mean(base, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_63d_slope_v067_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.diff(periods=63) / _mean(base, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_126d_slope_v068_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.diff(periods=126) / _mean(base, 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_252d_slope_v069_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.diff(periods=252) / _mean(base, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_21d_slope_v070_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(21, min_periods=max(1, 21//2)).max() - base.rolling(21, min_periods=max(1, 21//2)).min()
    base_series = rng / _mean(base, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_63d_slope_v071_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(63, min_periods=max(1, 63//2)).max() - base.rolling(63, min_periods=max(1, 63//2)).min()
    base_series = rng / _mean(base, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_126d_slope_v072_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(126, min_periods=max(1, 126//2)).max() - base.rolling(126, min_periods=max(1, 126//2)).min()
    base_series = rng / _mean(base, 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_252d_slope_v073_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    base_series = rng / _mean(base, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_21d_slope_v074_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    base_series = _z(base, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_63d_slope_v075_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = _z(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_126d_slope_v076_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    base_series = _z(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_252d_slope_v077_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = _z(base, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_21d_slope_v078_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    base_series = _std(base, 21) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_63d_slope_v079_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = _std(base, 63) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_126d_slope_v080_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    base_series = _std(base, 126) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthstd_252d_slope_v081_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = _std(base, 252) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_21d_slope_v082_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    base_series = bvps * g * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_63d_slope_v083_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = bvps * g * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_126d_slope_v084_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    base_series = bvps * g * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsxgrowth_252d_slope_v085_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = bvps * g * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_21v63_slope_v086_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_63v252_slope_v087_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_126v504_slope_v088_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthratio_42v189_slope_v089_signal(equity, intangibles, sharesbas, closeadj):
    a = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    b = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    base_series = (a - b) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_21d_slope_v090_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 21)
    base_series = result * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_63d_slope_v091_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 63)
    base_series = result * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_126d_slope_v092_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 126)
    base_series = result * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsemax_252d_slope_v093_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = bvps - _ema(bvps, 252)
    base_series = result * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_63d_slope_v094_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = (base / base.shift(63).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_126d_slope_v095_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = (base / base.shift(126).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_252d_slope_v096_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = (base / base.shift(252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvcompound_504d_slope_v097_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = (base / base.shift(504).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_63d_slope_v098_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (bvps / bvps.shift(63).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_126d_slope_v099_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (bvps / bvps.shift(126).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_252d_slope_v100_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (bvps / bvps.shift(252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpscompound_504d_slope_v101_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (bvps / bvps.shift(504).replace(0, np.nan)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxintang_63d_slope_v102_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    intratio = intangibles / equity.replace(0, np.nan)
    base_series = g * intratio * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxintang_252d_slope_v103_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    intratio = intangibles / equity.replace(0, np.nan)
    base_series = g * intratio * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_21d_slope_v104_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (base - _mean(base, 21)) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_63d_slope_v105_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (base - _mean(base, 63)) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_126d_slope_v106_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (base - _mean(base, 126)) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsdev_252d_slope_v107_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = (base - _mean(base, 252)) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_21d_slope_v108_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=21)
    base_series = _mean(base, 21) * rv
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_42d_slope_v109_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=42)
    base_series = _mean(base, 42) * rv
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_63d_slope_v110_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=63)
    base_series = _mean(base, 63) * rv
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_126d_slope_v111_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=126)
    base_series = _mean(base, 126) * rv
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_189d_slope_v112_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=189)
    base_series = _mean(base, 189) * rv
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_252d_slope_v113_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=252)
    base_series = _mean(base, 252) * rv
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_378d_slope_v114_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=378)
    base_series = _mean(base, 378) * rv
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvmeanxret_504d_slope_v115_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rv = closeadj.pct_change(periods=504)
    base_series = _mean(base, 504) * rv
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_21d_slope_v116_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=21)
    base_series = _mean(base, 21) * rv
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_42d_slope_v117_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=42)
    base_series = _mean(base, 42) * rv
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_63d_slope_v118_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=63)
    base_series = _mean(base, 63) * rv
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_126d_slope_v119_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=126)
    base_series = _mean(base, 126) * rv
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_189d_slope_v120_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=189)
    base_series = _mean(base, 189) * rv
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_252d_slope_v121_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=252)
    base_series = _mean(base, 252) * rv
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_378d_slope_v122_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=378)
    base_series = _mean(base, 378) * rv
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsmeanxret_504d_slope_v123_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rv = closeadj.pct_change(periods=504)
    base_series = _mean(base, 504) * rv
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_21d_slope_v124_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    dil = sharesbas.pct_change(periods=21)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_42d_slope_v125_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    dil = sharesbas.pct_change(periods=42)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_63d_slope_v126_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    dil = sharesbas.pct_change(periods=63)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_126d_slope_v127_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    dil = sharesbas.pct_change(periods=126)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_189d_slope_v128_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    dil = sharesbas.pct_change(periods=189)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_252d_slope_v129_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    dil = sharesbas.pct_change(periods=252)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_378d_slope_v130_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 378)
    dil = sharesbas.pct_change(periods=378)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxdilution_504d_slope_v131_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    dil = sharesbas.pct_change(periods=504)
    base_series = g * dil * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_21d_slope_v132_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_42d_slope_v133_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_63d_slope_v134_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_126d_slope_v135_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_189d_slope_v136_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_252d_slope_v137_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvabs_378d_slope_v138_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    base_series = base.abs() / _mean(base.abs(), 378).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_21d_slope_v139_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_42d_slope_v140_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 42)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_63d_slope_v141_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_126d_slope_v142_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_189d_slope_v143_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 189)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgxeqratio_252d_slope_v144_signal(equity, intangibles, sharesbas, closeadj):
    g = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    tbv = _f07_tangible_bv(equity, intangibles)
    eq_ratio = tbv / equity.replace(0, np.nan)
    base_series = g * eq_ratio * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_21d_slope_v145_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(21, min_periods=max(1, 21//2)).sum() / _mean(bvps, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_42d_slope_v146_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(42, min_periods=max(1, 42//2)).sum() / _mean(bvps, 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_63d_slope_v147_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(63, min_periods=max(1, 63//2)).sum() / _mean(bvps, 63).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_126d_slope_v148_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(126, min_periods=max(1, 126//2)).sum() / _mean(bvps, 126).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_189d_slope_v149_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(189, min_periods=max(1, 189//2)).sum() / _mean(bvps, 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsacc_252d_slope_v150_signal(equity, intangibles, sharesbas, closeadj):
    bvps = _f07_tangible_bvps(equity, intangibles, sharesbas)
    base_series = bvps.rolling(252, min_periods=max(1, 252//2)).sum() / _mean(bvps, 252).replace(0, np.nan) * closeadj
    result = _slope_pct(base_series, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07tbc_f07_tangible_book_compound_tbv_5d_slope_v001_signal,
    f07tbc_f07_tangible_book_compound_tbv_10d_slope_v002_signal,
    f07tbc_f07_tangible_book_compound_tbv_21d_slope_v003_signal,
    f07tbc_f07_tangible_book_compound_tbv_42d_slope_v004_signal,
    f07tbc_f07_tangible_book_compound_tbv_63d_slope_v005_signal,
    f07tbc_f07_tangible_book_compound_tbv_126d_slope_v006_signal,
    f07tbc_f07_tangible_book_compound_tbv_189d_slope_v007_signal,
    f07tbc_f07_tangible_book_compound_tbv_252d_slope_v008_signal,
    f07tbc_f07_tangible_book_compound_tbv_378d_slope_v009_signal,
    f07tbc_f07_tangible_book_compound_tbv_504d_slope_v010_signal,
    f07tbc_f07_tangible_book_compound_tbvps_5d_slope_v011_signal,
    f07tbc_f07_tangible_book_compound_tbvps_10d_slope_v012_signal,
    f07tbc_f07_tangible_book_compound_tbvps_21d_slope_v013_signal,
    f07tbc_f07_tangible_book_compound_tbvps_42d_slope_v014_signal,
    f07tbc_f07_tangible_book_compound_tbvps_63d_slope_v015_signal,
    f07tbc_f07_tangible_book_compound_tbvps_126d_slope_v016_signal,
    f07tbc_f07_tangible_book_compound_tbvps_189d_slope_v017_signal,
    f07tbc_f07_tangible_book_compound_tbvps_252d_slope_v018_signal,
    f07tbc_f07_tangible_book_compound_tbvps_378d_slope_v019_signal,
    f07tbc_f07_tangible_book_compound_tbvps_504d_slope_v020_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_21d_slope_v021_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_63d_slope_v022_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_126d_slope_v023_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_252d_slope_v024_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_504d_slope_v025_signal,
    f07tbc_f07_tangible_book_compound_tbvz_21d_slope_v026_signal,
    f07tbc_f07_tangible_book_compound_tbvz_63d_slope_v027_signal,
    f07tbc_f07_tangible_book_compound_tbvz_126d_slope_v028_signal,
    f07tbc_f07_tangible_book_compound_tbvz_252d_slope_v029_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_21d_slope_v030_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_63d_slope_v031_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_126d_slope_v032_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_252d_slope_v033_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_21d_slope_v034_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_63d_slope_v035_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_126d_slope_v036_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_252d_slope_v037_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_21d_slope_v038_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_63d_slope_v039_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_126d_slope_v040_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_252d_slope_v041_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_10d_slope_v042_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_21d_slope_v043_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_63d_slope_v044_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_126d_slope_v045_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_252d_slope_v046_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_21d_slope_v047_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_63d_slope_v048_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_126d_slope_v049_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_252d_slope_v050_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_21d_slope_v051_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_63d_slope_v052_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_252d_slope_v053_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_63d_slope_v054_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_126d_slope_v055_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_252d_slope_v056_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_63d_slope_v057_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_126d_slope_v058_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_252d_slope_v059_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_5d_slope_v060_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_21d_slope_v061_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_63d_slope_v062_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_126d_slope_v063_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_252d_slope_v064_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_5d_slope_v065_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_21d_slope_v066_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_63d_slope_v067_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_126d_slope_v068_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_252d_slope_v069_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_21d_slope_v070_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_63d_slope_v071_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_126d_slope_v072_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_252d_slope_v073_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_21d_slope_v074_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_63d_slope_v075_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_126d_slope_v076_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_252d_slope_v077_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_21d_slope_v078_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_63d_slope_v079_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_126d_slope_v080_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthstd_252d_slope_v081_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_21d_slope_v082_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_63d_slope_v083_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_126d_slope_v084_signal,
    f07tbc_f07_tangible_book_compound_tbvpsxgrowth_252d_slope_v085_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_21v63_slope_v086_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_63v252_slope_v087_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_126v504_slope_v088_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthratio_42v189_slope_v089_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_21d_slope_v090_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_63d_slope_v091_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_126d_slope_v092_signal,
    f07tbc_f07_tangible_book_compound_tbvpsemax_252d_slope_v093_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_63d_slope_v094_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_126d_slope_v095_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_252d_slope_v096_signal,
    f07tbc_f07_tangible_book_compound_tbvcompound_504d_slope_v097_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_63d_slope_v098_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_126d_slope_v099_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_252d_slope_v100_signal,
    f07tbc_f07_tangible_book_compound_tbvpscompound_504d_slope_v101_signal,
    f07tbc_f07_tangible_book_compound_tbvgxintang_63d_slope_v102_signal,
    f07tbc_f07_tangible_book_compound_tbvgxintang_252d_slope_v103_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_21d_slope_v104_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_63d_slope_v105_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_126d_slope_v106_signal,
    f07tbc_f07_tangible_book_compound_tbvpsdev_252d_slope_v107_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_21d_slope_v108_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_42d_slope_v109_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_63d_slope_v110_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_126d_slope_v111_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_189d_slope_v112_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_252d_slope_v113_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_378d_slope_v114_signal,
    f07tbc_f07_tangible_book_compound_tbvmeanxret_504d_slope_v115_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_21d_slope_v116_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_42d_slope_v117_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_63d_slope_v118_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_126d_slope_v119_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_189d_slope_v120_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_252d_slope_v121_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_378d_slope_v122_signal,
    f07tbc_f07_tangible_book_compound_tbvpsmeanxret_504d_slope_v123_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_21d_slope_v124_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_42d_slope_v125_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_63d_slope_v126_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_126d_slope_v127_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_189d_slope_v128_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_252d_slope_v129_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_378d_slope_v130_signal,
    f07tbc_f07_tangible_book_compound_tbvgxdilution_504d_slope_v131_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_21d_slope_v132_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_42d_slope_v133_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_63d_slope_v134_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_126d_slope_v135_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_189d_slope_v136_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_252d_slope_v137_signal,
    f07tbc_f07_tangible_book_compound_tbvabs_378d_slope_v138_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_21d_slope_v139_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_42d_slope_v140_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_63d_slope_v141_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_126d_slope_v142_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_189d_slope_v143_signal,
    f07tbc_f07_tangible_book_compound_tbvgxeqratio_252d_slope_v144_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_21d_slope_v145_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_42d_slope_v146_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_63d_slope_v147_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_126d_slope_v148_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_189d_slope_v149_signal,
    f07tbc_f07_tangible_book_compound_tbvpsacc_252d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_TANGIBLE_BOOK_COMPOUND_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f07_tangible_bv', '_f07_tangible_bvps', '_f07_tbv_growth')
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
    print(f"OK f07_tangible_book_compound_2nd_derivatives_001_150_claude: {n_features} features pass")
