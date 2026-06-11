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


def _f07_tangible_bv(equity, intangibles):
    return equity - intangibles


def _f07_tangible_bvps(equity, intangibles, sharesbas):
    tbv = equity - intangibles
    return tbv / sharesbas.replace(0, np.nan)


def _f07_tbv_growth(equity, intangibles, sharesbas, w):
    tbvps = (equity - intangibles) / sharesbas.replace(0, np.nan)
    return tbvps.pct_change(periods=w)


def f07tbc_f07_tangible_book_compound_tbv_5d_base_v001_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 5) / _mean(closeadj, 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_10d_base_v002_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 10) / _mean(closeadj, 10).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_21d_base_v003_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 21) / _mean(closeadj, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_42d_base_v004_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 42) / _mean(closeadj, 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_63d_base_v005_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 63) / _mean(closeadj, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_126d_base_v006_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 126) / _mean(closeadj, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_189d_base_v007_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 189) / _mean(closeadj, 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_252d_base_v008_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 252) / _mean(closeadj, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_378d_base_v009_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 378) / _mean(closeadj, 378).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbv_504d_base_v010_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _mean(base, 504) / _mean(closeadj, 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_5d_base_v011_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_10d_base_v012_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_21d_base_v013_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_42d_base_v014_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_63d_base_v015_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_126d_base_v016_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_189d_base_v017_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_252d_base_v018_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_378d_base_v019_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvps_504d_base_v020_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_21d_base_v021_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_63d_base_v022_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_126d_base_v023_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_252d_base_v024_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowth_504d_base_v025_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_21d_base_v026_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_63d_base_v027_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_126d_base_v028_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvz_252d_base_v029_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_21d_base_v030_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_63d_base_v031_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_126d_base_v032_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsz_252d_base_v033_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_21d_base_v034_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_63d_base_v035_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_126d_base_v036_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsstd_252d_base_v037_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_21d_base_v038_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _std(base, 21) / _mean(base, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_63d_base_v039_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _std(base, 63) / _mean(base, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_126d_base_v040_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _std(base, 126) / _mean(base, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvstd_252d_base_v041_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = _std(base, 252) / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_10d_base_v042_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_21d_base_v043_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_63d_base_v044_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_126d_base_v045_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsema_252d_base_v046_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_21d_base_v047_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_63d_base_v048_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_126d_base_v049_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthema_252d_base_v050_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_21d_base_v051_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    result = np.log(base.replace(0, np.nan)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_63d_base_v052_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    result = np.log(base.replace(0, np.nan)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpslog_252d_base_v053_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas).abs()
    result = np.log(base.replace(0, np.nan)) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_63d_base_v054_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_126d_base_v055_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpsrank_252d_base_v056_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    rnk = base.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_63d_base_v057_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_126d_base_v058_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrank_252d_base_v059_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rnk = base.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    result = rnk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_5d_base_v060_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = base.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_21d_base_v061_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = base.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_63d_base_v062_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = base.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_126d_base_v063_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = base.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvpschg_252d_base_v064_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tangible_bvps(equity, intangibles, sharesbas)
    result = base.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_5d_base_v065_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.diff(periods=5) / _mean(base, 5).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_21d_base_v066_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.diff(periods=21) / _mean(base, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_63d_base_v067_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.diff(periods=63) / _mean(base, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_126d_base_v068_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.diff(periods=126) / _mean(base, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvchg_252d_base_v069_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    result = base.diff(periods=252) / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_21d_base_v070_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(21, min_periods=max(1, 21//2)).max() - base.rolling(21, min_periods=max(1, 21//2)).min()
    result = rng / _mean(base, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_63d_base_v071_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(63, min_periods=max(1, 63//2)).max() - base.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng / _mean(base, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_126d_base_v072_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(126, min_periods=max(1, 126//2)).max() - base.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng / _mean(base, 126).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvrange_252d_base_v073_signal(equity, intangibles, closeadj):
    base = _f07_tangible_bv(equity, intangibles)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_21d_base_v074_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07tbc_f07_tangible_book_compound_tbvgrowthz_63d_base_v075_signal(equity, intangibles, sharesbas, closeadj):
    base = _f07_tbv_growth(equity, intangibles, sharesbas, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07tbc_f07_tangible_book_compound_tbv_5d_base_v001_signal,
    f07tbc_f07_tangible_book_compound_tbv_10d_base_v002_signal,
    f07tbc_f07_tangible_book_compound_tbv_21d_base_v003_signal,
    f07tbc_f07_tangible_book_compound_tbv_42d_base_v004_signal,
    f07tbc_f07_tangible_book_compound_tbv_63d_base_v005_signal,
    f07tbc_f07_tangible_book_compound_tbv_126d_base_v006_signal,
    f07tbc_f07_tangible_book_compound_tbv_189d_base_v007_signal,
    f07tbc_f07_tangible_book_compound_tbv_252d_base_v008_signal,
    f07tbc_f07_tangible_book_compound_tbv_378d_base_v009_signal,
    f07tbc_f07_tangible_book_compound_tbv_504d_base_v010_signal,
    f07tbc_f07_tangible_book_compound_tbvps_5d_base_v011_signal,
    f07tbc_f07_tangible_book_compound_tbvps_10d_base_v012_signal,
    f07tbc_f07_tangible_book_compound_tbvps_21d_base_v013_signal,
    f07tbc_f07_tangible_book_compound_tbvps_42d_base_v014_signal,
    f07tbc_f07_tangible_book_compound_tbvps_63d_base_v015_signal,
    f07tbc_f07_tangible_book_compound_tbvps_126d_base_v016_signal,
    f07tbc_f07_tangible_book_compound_tbvps_189d_base_v017_signal,
    f07tbc_f07_tangible_book_compound_tbvps_252d_base_v018_signal,
    f07tbc_f07_tangible_book_compound_tbvps_378d_base_v019_signal,
    f07tbc_f07_tangible_book_compound_tbvps_504d_base_v020_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_21d_base_v021_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_63d_base_v022_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_126d_base_v023_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_252d_base_v024_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowth_504d_base_v025_signal,
    f07tbc_f07_tangible_book_compound_tbvz_21d_base_v026_signal,
    f07tbc_f07_tangible_book_compound_tbvz_63d_base_v027_signal,
    f07tbc_f07_tangible_book_compound_tbvz_126d_base_v028_signal,
    f07tbc_f07_tangible_book_compound_tbvz_252d_base_v029_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_21d_base_v030_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_63d_base_v031_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_126d_base_v032_signal,
    f07tbc_f07_tangible_book_compound_tbvpsz_252d_base_v033_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_21d_base_v034_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_63d_base_v035_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_126d_base_v036_signal,
    f07tbc_f07_tangible_book_compound_tbvpsstd_252d_base_v037_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_21d_base_v038_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_63d_base_v039_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_126d_base_v040_signal,
    f07tbc_f07_tangible_book_compound_tbvstd_252d_base_v041_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_10d_base_v042_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_21d_base_v043_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_63d_base_v044_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_126d_base_v045_signal,
    f07tbc_f07_tangible_book_compound_tbvpsema_252d_base_v046_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_21d_base_v047_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_63d_base_v048_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_126d_base_v049_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthema_252d_base_v050_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_21d_base_v051_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_63d_base_v052_signal,
    f07tbc_f07_tangible_book_compound_tbvpslog_252d_base_v053_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_63d_base_v054_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_126d_base_v055_signal,
    f07tbc_f07_tangible_book_compound_tbvpsrank_252d_base_v056_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_63d_base_v057_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_126d_base_v058_signal,
    f07tbc_f07_tangible_book_compound_tbvrank_252d_base_v059_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_5d_base_v060_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_21d_base_v061_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_63d_base_v062_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_126d_base_v063_signal,
    f07tbc_f07_tangible_book_compound_tbvpschg_252d_base_v064_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_5d_base_v065_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_21d_base_v066_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_63d_base_v067_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_126d_base_v068_signal,
    f07tbc_f07_tangible_book_compound_tbvchg_252d_base_v069_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_21d_base_v070_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_63d_base_v071_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_126d_base_v072_signal,
    f07tbc_f07_tangible_book_compound_tbvrange_252d_base_v073_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_21d_base_v074_signal,
    f07tbc_f07_tangible_book_compound_tbvgrowthz_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_TANGIBLE_BOOK_COMPOUND_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_tangible_book_compound_base_001_075_claude: {n_features} features pass")
