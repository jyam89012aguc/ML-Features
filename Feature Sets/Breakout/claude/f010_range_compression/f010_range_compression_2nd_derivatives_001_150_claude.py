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
def _f010_n_day_range(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo)


def _f010_range_compression(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    rng_short = (hi - lo)
    rng_long = (high.rolling(w * 2, min_periods=max(1, w)).max()
                - low.rolling(w * 2, min_periods=max(1, w)).min())
    return rng_short / rng_long.replace(0, np.nan).abs()


def _f010_compression_ratio(high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (hi - lo)
    med = rng.rolling(252, min_periods=63).median()
    return (med - rng) / med.replace(0, np.nan).abs()


def _slope_inrange_x_close(high, low, close, w, sw):
    base = _f010_n_day_range(high, low, w) * close
    return _slope_pct(base, sw)


def _slope_blen_x_close(high, low, close, w, sw):
    base = _f010_range_compression(high, low, w) * close
    return _slope_pct(base, sw)


def _slope_cons_x_close(high, low, close, w, sw):
    base = _f010_compression_ratio(high, low, w) * close
    return _slope_pct(base, sw)


# v001-v015: slope of in-range count × close at varying windows and slope-windows
def f010rcm_f010_range_compression_inrange_21d_slope_v001_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_21d_slope_v002_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_42d_slope_v003_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_42d_slope_v004_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_63d_slope_v005_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_63d_slope_v006_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_126d_slope_v007_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_126d_slope_v008_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_252d_slope_v009_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_252d_slope_v010_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_504d_slope_v011_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_504d_slope_v012_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_504d_slope_v013_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 504) * closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_189d_slope_v014_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrange_378d_slope_v015_signal(closeadj, high, low):
    result = _slope_pct(_f010_n_day_range(high, low, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v030: slope of base length × close
def f010rcm_f010_range_compression_blen_21d_slope_v016_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_21d_slope_v017_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_42d_slope_v018_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_63d_slope_v019_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_63d_slope_v020_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_126d_slope_v021_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_126d_slope_v022_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_252d_slope_v023_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_252d_slope_v024_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_504d_slope_v025_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_504d_slope_v026_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_504d_slope_v027_signal(closeadj, high, low):
    base = (_f010_range_compression(high, low, 504) + 1.0) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_189d_slope_v028_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_378d_slope_v029_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blen_42d_slope_v030_signal(closeadj, high, low):
    result = _slope_pct(_f010_range_compression(high, low, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v045: slope of consolidation × close
def f010rcm_f010_range_compression_consdur_21d_slope_v031_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_21d_slope_v032_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_63d_slope_v033_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_63d_slope_v034_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_126d_slope_v035_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_126d_slope_v036_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_252d_slope_v037_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_252d_slope_v038_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_504d_slope_v039_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_504d_slope_v040_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_504d_slope_v041_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 504) * closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_189d_slope_v042_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_378d_slope_v043_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_42d_slope_v044_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consdur_42d_slope_v045_signal(closeadj, high, low):
    result = _slope_pct(_f010_compression_ratio(high, low, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v060: slope_diff_norm of in-range × close
def f010rcm_f010_range_compression_inrnorm_21d_slope_v046_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_21d_slope_v047_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_63d_slope_v048_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_63d_slope_v049_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_126d_slope_v050_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_126d_slope_v051_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_252d_slope_v052_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_252d_slope_v053_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_504d_slope_v054_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_504d_slope_v055_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_504d_slope_v056_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 504) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_42d_slope_v057_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 42) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_42d_slope_v058_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_189d_slope_v059_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrnorm_378d_slope_v060_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v075: slope of in-range × volume (dollar-flow)
def f010rcm_f010_range_compression_inrxvol_21d_slope_v061_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_21d_slope_v062_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_63d_slope_v063_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_63d_slope_v064_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_126d_slope_v065_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_252d_slope_v066_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_252d_slope_v067_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_504d_slope_v068_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 504) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxvol_504d_slope_v069_signal(closeadj, high, low, volume):
    base = _f010_n_day_range(high, low, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_21d_slope_v070_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_63d_slope_v071_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_252d_slope_v072_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 252) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_252d_slope_v073_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 252) * _mean(dv, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_504d_slope_v074_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxdv_504d_slope_v075_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_n_day_range(high, low, 504) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v076-v090: slope of base length × volume
def f010rcm_f010_range_compression_blenxvol_21d_slope_v076_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_21d_slope_v077_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_63d_slope_v078_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_63d_slope_v079_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_126d_slope_v080_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_252d_slope_v081_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_252d_slope_v082_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_504d_slope_v083_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 504) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxvol_504d_slope_v084_signal(closeadj, high, low, volume):
    base = _f010_range_compression(high, low, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_21d_slope_v085_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_range_compression(high, low, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_63d_slope_v086_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_range_compression(high, low, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_126d_slope_v087_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_range_compression(high, low, 126) * _mean(dv, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_252d_slope_v088_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_range_compression(high, low, 252) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_504d_slope_v089_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_range_compression(high, low, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxdv_504d_slope_v090_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = (_f010_range_compression(high, low, 504) + 1.0) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v105: slope of consolidation × volume
def f010rcm_f010_range_compression_consxvol_21d_slope_v091_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_21d_slope_v092_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_63d_slope_v093_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_63d_slope_v094_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_126d_slope_v095_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_252d_slope_v096_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_252d_slope_v097_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_504d_slope_v098_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxvol_504d_slope_v099_signal(closeadj, high, low, volume):
    base = _f010_compression_ratio(high, low, 504) * volume
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_21d_slope_v100_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_63d_slope_v101_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_126d_slope_v102_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 126) * _mean(dv, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_252d_slope_v103_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 252) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_504d_slope_v104_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxdv_504d_slope_v105_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f010_compression_ratio(high, low, 504) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v120: slope of in-range × HL range
def f010rcm_f010_range_compression_inrxhlr_21d_slope_v106_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f010_n_day_range(high, low, 21) * rng
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_21d_slope_v107_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f010_n_day_range(high, low, 21) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_63d_slope_v108_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f010_n_day_range(high, low, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_63d_slope_v109_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f010_n_day_range(high, low, 63) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_126d_slope_v110_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f010_n_day_range(high, low, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_252d_slope_v111_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f010_n_day_range(high, low, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrxhlr_252d_slope_v112_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f010_n_day_range(high, low, 252) * rng
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxhlr_21d_slope_v113_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f010_range_compression(high, low, 21) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxhlr_63d_slope_v114_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f010_range_compression(high, low, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxhlr_126d_slope_v115_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f010_range_compression(high, low, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenxhlr_252d_slope_v116_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f010_range_compression(high, low, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxhlr_63d_slope_v117_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f010_compression_ratio(high, low, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxhlr_126d_slope_v118_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f010_compression_ratio(high, low, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxhlr_252d_slope_v119_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f010_compression_ratio(high, low, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consxhlr_504d_slope_v120_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f010_compression_ratio(high, low, 504) * rng
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v135: slope of log(1+in-range) × close
def f010rcm_f010_range_compression_lninr_21d_slope_v121_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_21d_slope_v122_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_63d_slope_v123_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_63d_slope_v124_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_126d_slope_v125_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_252d_slope_v126_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_252d_slope_v127_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lninr_504d_slope_v128_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_n_day_range(high, low, 504)) + 1.0) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnblen_21d_slope_v129_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_range_compression(high, low, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnblen_63d_slope_v130_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_range_compression(high, low, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnblen_126d_slope_v131_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_range_compression(high, low, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lnblen_252d_slope_v132_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_range_compression(high, low, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lncons_63d_slope_v133_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_compression_ratio(high, low, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lncons_126d_slope_v134_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_compression_ratio(high, low, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_lncons_252d_slope_v135_signal(closeadj, high, low):
    base = np.log1p(np.abs(_f010_compression_ratio(high, low, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v150: composite slope
def f010rcm_f010_range_compression_inrema_21d_slope_v136_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrema_63d_slope_v137_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_inrema_252d_slope_v138_signal(closeadj, high, low):
    base = _f010_n_day_range(high, low, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_21d_slope_v139_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_63d_slope_v140_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenema_252d_slope_v141_signal(closeadj, high, low):
    base = _f010_range_compression(high, low, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consema_21d_slope_v142_signal(closeadj, high, low):
    base = _f010_compression_ratio(high, low, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consema_63d_slope_v143_signal(closeadj, high, low):
    base = _f010_compression_ratio(high, low, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consema_252d_slope_v144_signal(closeadj, high, low):
    base = _f010_compression_ratio(high, low, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenplusinr_63d_slope_v145_signal(closeadj, high, low):
    base = (_f010_range_compression(high, low, 63) + _f010_n_day_range(high, low, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenplusinr_126d_slope_v146_signal(closeadj, high, low):
    base = (_f010_range_compression(high, low, 126) + _f010_n_day_range(high, low, 126)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_blenplusinr_252d_slope_v147_signal(closeadj, high, low):
    base = (_f010_range_compression(high, low, 252) + _f010_n_day_range(high, low, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consplusinr_63d_slope_v148_signal(closeadj, high, low):
    base = (_f010_compression_ratio(high, low, 63) + _f010_n_day_range(high, low, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consplusinr_126d_slope_v149_signal(closeadj, high, low):
    base = (_f010_compression_ratio(high, low, 126) + _f010_n_day_range(high, low, 126)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f010rcm_f010_range_compression_consplusinr_252d_slope_v150_signal(closeadj, high, low):
    base = (_f010_compression_ratio(high, low, 252) + _f010_n_day_range(high, low, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f010rcm_f010_range_compression_inrange_21d_slope_v001_signal,
    f010rcm_f010_range_compression_inrange_21d_slope_v002_signal,
    f010rcm_f010_range_compression_inrange_42d_slope_v003_signal,
    f010rcm_f010_range_compression_inrange_42d_slope_v004_signal,
    f010rcm_f010_range_compression_inrange_63d_slope_v005_signal,
    f010rcm_f010_range_compression_inrange_63d_slope_v006_signal,
    f010rcm_f010_range_compression_inrange_126d_slope_v007_signal,
    f010rcm_f010_range_compression_inrange_126d_slope_v008_signal,
    f010rcm_f010_range_compression_inrange_252d_slope_v009_signal,
    f010rcm_f010_range_compression_inrange_252d_slope_v010_signal,
    f010rcm_f010_range_compression_inrange_504d_slope_v011_signal,
    f010rcm_f010_range_compression_inrange_504d_slope_v012_signal,
    f010rcm_f010_range_compression_inrange_504d_slope_v013_signal,
    f010rcm_f010_range_compression_inrange_189d_slope_v014_signal,
    f010rcm_f010_range_compression_inrange_378d_slope_v015_signal,
    f010rcm_f010_range_compression_blen_21d_slope_v016_signal,
    f010rcm_f010_range_compression_blen_21d_slope_v017_signal,
    f010rcm_f010_range_compression_blen_42d_slope_v018_signal,
    f010rcm_f010_range_compression_blen_63d_slope_v019_signal,
    f010rcm_f010_range_compression_blen_63d_slope_v020_signal,
    f010rcm_f010_range_compression_blen_126d_slope_v021_signal,
    f010rcm_f010_range_compression_blen_126d_slope_v022_signal,
    f010rcm_f010_range_compression_blen_252d_slope_v023_signal,
    f010rcm_f010_range_compression_blen_252d_slope_v024_signal,
    f010rcm_f010_range_compression_blen_504d_slope_v025_signal,
    f010rcm_f010_range_compression_blen_504d_slope_v026_signal,
    f010rcm_f010_range_compression_blen_504d_slope_v027_signal,
    f010rcm_f010_range_compression_blen_189d_slope_v028_signal,
    f010rcm_f010_range_compression_blen_378d_slope_v029_signal,
    f010rcm_f010_range_compression_blen_42d_slope_v030_signal,
    f010rcm_f010_range_compression_consdur_21d_slope_v031_signal,
    f010rcm_f010_range_compression_consdur_21d_slope_v032_signal,
    f010rcm_f010_range_compression_consdur_63d_slope_v033_signal,
    f010rcm_f010_range_compression_consdur_63d_slope_v034_signal,
    f010rcm_f010_range_compression_consdur_126d_slope_v035_signal,
    f010rcm_f010_range_compression_consdur_126d_slope_v036_signal,
    f010rcm_f010_range_compression_consdur_252d_slope_v037_signal,
    f010rcm_f010_range_compression_consdur_252d_slope_v038_signal,
    f010rcm_f010_range_compression_consdur_504d_slope_v039_signal,
    f010rcm_f010_range_compression_consdur_504d_slope_v040_signal,
    f010rcm_f010_range_compression_consdur_504d_slope_v041_signal,
    f010rcm_f010_range_compression_consdur_189d_slope_v042_signal,
    f010rcm_f010_range_compression_consdur_378d_slope_v043_signal,
    f010rcm_f010_range_compression_consdur_42d_slope_v044_signal,
    f010rcm_f010_range_compression_consdur_42d_slope_v045_signal,
    f010rcm_f010_range_compression_inrnorm_21d_slope_v046_signal,
    f010rcm_f010_range_compression_inrnorm_21d_slope_v047_signal,
    f010rcm_f010_range_compression_inrnorm_63d_slope_v048_signal,
    f010rcm_f010_range_compression_inrnorm_63d_slope_v049_signal,
    f010rcm_f010_range_compression_inrnorm_126d_slope_v050_signal,
    f010rcm_f010_range_compression_inrnorm_126d_slope_v051_signal,
    f010rcm_f010_range_compression_inrnorm_252d_slope_v052_signal,
    f010rcm_f010_range_compression_inrnorm_252d_slope_v053_signal,
    f010rcm_f010_range_compression_inrnorm_504d_slope_v054_signal,
    f010rcm_f010_range_compression_inrnorm_504d_slope_v055_signal,
    f010rcm_f010_range_compression_inrnorm_504d_slope_v056_signal,
    f010rcm_f010_range_compression_inrnorm_42d_slope_v057_signal,
    f010rcm_f010_range_compression_inrnorm_42d_slope_v058_signal,
    f010rcm_f010_range_compression_inrnorm_189d_slope_v059_signal,
    f010rcm_f010_range_compression_inrnorm_378d_slope_v060_signal,
    f010rcm_f010_range_compression_inrxvol_21d_slope_v061_signal,
    f010rcm_f010_range_compression_inrxvol_21d_slope_v062_signal,
    f010rcm_f010_range_compression_inrxvol_63d_slope_v063_signal,
    f010rcm_f010_range_compression_inrxvol_63d_slope_v064_signal,
    f010rcm_f010_range_compression_inrxvol_126d_slope_v065_signal,
    f010rcm_f010_range_compression_inrxvol_252d_slope_v066_signal,
    f010rcm_f010_range_compression_inrxvol_252d_slope_v067_signal,
    f010rcm_f010_range_compression_inrxvol_504d_slope_v068_signal,
    f010rcm_f010_range_compression_inrxvol_504d_slope_v069_signal,
    f010rcm_f010_range_compression_inrxdv_21d_slope_v070_signal,
    f010rcm_f010_range_compression_inrxdv_63d_slope_v071_signal,
    f010rcm_f010_range_compression_inrxdv_252d_slope_v072_signal,
    f010rcm_f010_range_compression_inrxdv_252d_slope_v073_signal,
    f010rcm_f010_range_compression_inrxdv_504d_slope_v074_signal,
    f010rcm_f010_range_compression_inrxdv_504d_slope_v075_signal,
    f010rcm_f010_range_compression_blenxvol_21d_slope_v076_signal,
    f010rcm_f010_range_compression_blenxvol_21d_slope_v077_signal,
    f010rcm_f010_range_compression_blenxvol_63d_slope_v078_signal,
    f010rcm_f010_range_compression_blenxvol_63d_slope_v079_signal,
    f010rcm_f010_range_compression_blenxvol_126d_slope_v080_signal,
    f010rcm_f010_range_compression_blenxvol_252d_slope_v081_signal,
    f010rcm_f010_range_compression_blenxvol_252d_slope_v082_signal,
    f010rcm_f010_range_compression_blenxvol_504d_slope_v083_signal,
    f010rcm_f010_range_compression_blenxvol_504d_slope_v084_signal,
    f010rcm_f010_range_compression_blenxdv_21d_slope_v085_signal,
    f010rcm_f010_range_compression_blenxdv_63d_slope_v086_signal,
    f010rcm_f010_range_compression_blenxdv_126d_slope_v087_signal,
    f010rcm_f010_range_compression_blenxdv_252d_slope_v088_signal,
    f010rcm_f010_range_compression_blenxdv_504d_slope_v089_signal,
    f010rcm_f010_range_compression_blenxdv_504d_slope_v090_signal,
    f010rcm_f010_range_compression_consxvol_21d_slope_v091_signal,
    f010rcm_f010_range_compression_consxvol_21d_slope_v092_signal,
    f010rcm_f010_range_compression_consxvol_63d_slope_v093_signal,
    f010rcm_f010_range_compression_consxvol_63d_slope_v094_signal,
    f010rcm_f010_range_compression_consxvol_126d_slope_v095_signal,
    f010rcm_f010_range_compression_consxvol_252d_slope_v096_signal,
    f010rcm_f010_range_compression_consxvol_252d_slope_v097_signal,
    f010rcm_f010_range_compression_consxvol_504d_slope_v098_signal,
    f010rcm_f010_range_compression_consxvol_504d_slope_v099_signal,
    f010rcm_f010_range_compression_consxdv_21d_slope_v100_signal,
    f010rcm_f010_range_compression_consxdv_63d_slope_v101_signal,
    f010rcm_f010_range_compression_consxdv_126d_slope_v102_signal,
    f010rcm_f010_range_compression_consxdv_252d_slope_v103_signal,
    f010rcm_f010_range_compression_consxdv_504d_slope_v104_signal,
    f010rcm_f010_range_compression_consxdv_504d_slope_v105_signal,
    f010rcm_f010_range_compression_inrxhlr_21d_slope_v106_signal,
    f010rcm_f010_range_compression_inrxhlr_21d_slope_v107_signal,
    f010rcm_f010_range_compression_inrxhlr_63d_slope_v108_signal,
    f010rcm_f010_range_compression_inrxhlr_63d_slope_v109_signal,
    f010rcm_f010_range_compression_inrxhlr_126d_slope_v110_signal,
    f010rcm_f010_range_compression_inrxhlr_252d_slope_v111_signal,
    f010rcm_f010_range_compression_inrxhlr_252d_slope_v112_signal,
    f010rcm_f010_range_compression_blenxhlr_21d_slope_v113_signal,
    f010rcm_f010_range_compression_blenxhlr_63d_slope_v114_signal,
    f010rcm_f010_range_compression_blenxhlr_126d_slope_v115_signal,
    f010rcm_f010_range_compression_blenxhlr_252d_slope_v116_signal,
    f010rcm_f010_range_compression_consxhlr_63d_slope_v117_signal,
    f010rcm_f010_range_compression_consxhlr_126d_slope_v118_signal,
    f010rcm_f010_range_compression_consxhlr_252d_slope_v119_signal,
    f010rcm_f010_range_compression_consxhlr_504d_slope_v120_signal,
    f010rcm_f010_range_compression_lninr_21d_slope_v121_signal,
    f010rcm_f010_range_compression_lninr_21d_slope_v122_signal,
    f010rcm_f010_range_compression_lninr_63d_slope_v123_signal,
    f010rcm_f010_range_compression_lninr_63d_slope_v124_signal,
    f010rcm_f010_range_compression_lninr_126d_slope_v125_signal,
    f010rcm_f010_range_compression_lninr_252d_slope_v126_signal,
    f010rcm_f010_range_compression_lninr_252d_slope_v127_signal,
    f010rcm_f010_range_compression_lninr_504d_slope_v128_signal,
    f010rcm_f010_range_compression_lnblen_21d_slope_v129_signal,
    f010rcm_f010_range_compression_lnblen_63d_slope_v130_signal,
    f010rcm_f010_range_compression_lnblen_126d_slope_v131_signal,
    f010rcm_f010_range_compression_lnblen_252d_slope_v132_signal,
    f010rcm_f010_range_compression_lncons_63d_slope_v133_signal,
    f010rcm_f010_range_compression_lncons_126d_slope_v134_signal,
    f010rcm_f010_range_compression_lncons_252d_slope_v135_signal,
    f010rcm_f010_range_compression_inrema_21d_slope_v136_signal,
    f010rcm_f010_range_compression_inrema_63d_slope_v137_signal,
    f010rcm_f010_range_compression_inrema_252d_slope_v138_signal,
    f010rcm_f010_range_compression_blenema_21d_slope_v139_signal,
    f010rcm_f010_range_compression_blenema_63d_slope_v140_signal,
    f010rcm_f010_range_compression_blenema_252d_slope_v141_signal,
    f010rcm_f010_range_compression_consema_21d_slope_v142_signal,
    f010rcm_f010_range_compression_consema_63d_slope_v143_signal,
    f010rcm_f010_range_compression_consema_252d_slope_v144_signal,
    f010rcm_f010_range_compression_blenplusinr_63d_slope_v145_signal,
    f010rcm_f010_range_compression_blenplusinr_126d_slope_v146_signal,
    f010rcm_f010_range_compression_blenplusinr_252d_slope_v147_signal,
    f010rcm_f010_range_compression_consplusinr_63d_slope_v148_signal,
    f010rcm_f010_range_compression_consplusinr_126d_slope_v149_signal,
    f010rcm_f010_range_compression_consplusinr_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F010_RANGE_COMPRESSION_REGISTRY_SLOPE_001_150 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f010_n_day_range", "_f010_range_compression", "_f010_compression_ratio")
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
    print(f"OK f010_range_compression_2nd_derivatives_001_150_claude: {n_features} features pass")
