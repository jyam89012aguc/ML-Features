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
def _f009_close_std_norm(close, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / m.replace(0, np.nan).abs()


def _f009_coiling_score(close, w):
    sd_short = close.rolling(max(2, w // 3), min_periods=max(1, w // 6)).std()
    sd_long = close.rolling(w, min_periods=max(1, w // 2)).std()
    return sd_short / sd_long.replace(0, np.nan).abs()


def _f009_tightness_signature(close, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    cv = sd / m.replace(0, np.nan).abs()
    med = cv.rolling(252, min_periods=63).median()
    return (med - cv) / med.replace(0, np.nan).abs()


def _slope_inrange_x_close(close, w, sw):
    base = _f009_close_std_norm(close, w) * close
    return _slope_pct(base, sw)


def _slope_blen_x_close(close, w, sw):
    base = _f009_coiling_score(close, w) * close
    return _slope_pct(base, sw)


def _slope_cons_x_close(close, w, sw):
    base = _f009_tightness_signature(close, w) * close
    return _slope_pct(base, sw)


# v001-v015: slope of in-range count × close at varying windows and slope-windows
def f009ctn_f009_consolidation_tightness_inrange_21d_slope_v001_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_21d_slope_v002_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_42d_slope_v003_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_42d_slope_v004_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_63d_slope_v005_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_63d_slope_v006_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_126d_slope_v007_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_126d_slope_v008_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_252d_slope_v009_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_252d_slope_v010_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_504d_slope_v011_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_504d_slope_v012_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_504d_slope_v013_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 504) * closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_189d_slope_v014_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrange_378d_slope_v015_signal(closeadj):
    result = _slope_pct(_f009_close_std_norm(closeadj, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v030: slope of base length × close
def f009ctn_f009_consolidation_tightness_blen_21d_slope_v016_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_21d_slope_v017_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_42d_slope_v018_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_63d_slope_v019_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_63d_slope_v020_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_126d_slope_v021_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_126d_slope_v022_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_252d_slope_v023_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_252d_slope_v024_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_504d_slope_v025_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_504d_slope_v026_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_504d_slope_v027_signal(closeadj):
    base = (_f009_coiling_score(closeadj, 504) + 1.0) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_189d_slope_v028_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_378d_slope_v029_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blen_42d_slope_v030_signal(closeadj):
    result = _slope_pct(_f009_coiling_score(closeadj, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v045: slope of consolidation × close
def f009ctn_f009_consolidation_tightness_consdur_21d_slope_v031_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 21) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_21d_slope_v032_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 21) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_63d_slope_v033_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 63) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_63d_slope_v034_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 63) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_126d_slope_v035_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 126) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_126d_slope_v036_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 126) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_252d_slope_v037_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 252) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_252d_slope_v038_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 252) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_504d_slope_v039_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 504) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_504d_slope_v040_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 504) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_504d_slope_v041_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 504) * closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_189d_slope_v042_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 189) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_378d_slope_v043_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 378) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_42d_slope_v044_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 42) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consdur_42d_slope_v045_signal(closeadj):
    result = _slope_pct(_f009_tightness_signature(closeadj, 42) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v060: slope_diff_norm of in-range × close
def f009ctn_f009_consolidation_tightness_inrnorm_21d_slope_v046_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_21d_slope_v047_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_63d_slope_v048_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_63d_slope_v049_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_126d_slope_v050_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_126d_slope_v051_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_252d_slope_v052_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_252d_slope_v053_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v054_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v055_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v056_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_42d_slope_v057_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 42) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_42d_slope_v058_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_189d_slope_v059_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrnorm_378d_slope_v060_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v075: slope of in-range × volume (dollar-flow)
def f009ctn_f009_consolidation_tightness_inrxvol_21d_slope_v061_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_21d_slope_v062_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_63d_slope_v063_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_63d_slope_v064_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_126d_slope_v065_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_252d_slope_v066_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_252d_slope_v067_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_504d_slope_v068_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 504) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxvol_504d_slope_v069_signal(closeadj, volume):
    base = _f009_close_std_norm(closeadj, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_21d_slope_v070_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_63d_slope_v071_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_252d_slope_v072_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 252) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_252d_slope_v073_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 252) * _mean(dv, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_504d_slope_v074_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxdv_504d_slope_v075_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_close_std_norm(closeadj, 504) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v076-v090: slope of base length × volume
def f009ctn_f009_consolidation_tightness_blenxvol_21d_slope_v076_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_21d_slope_v077_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_63d_slope_v078_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_63d_slope_v079_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_126d_slope_v080_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_252d_slope_v081_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_252d_slope_v082_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_504d_slope_v083_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 504) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxvol_504d_slope_v084_signal(closeadj, volume):
    base = _f009_coiling_score(closeadj, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_21d_slope_v085_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_coiling_score(closeadj, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_63d_slope_v086_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_coiling_score(closeadj, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_126d_slope_v087_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_coiling_score(closeadj, 126) * _mean(dv, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_252d_slope_v088_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_coiling_score(closeadj, 252) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_504d_slope_v089_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_coiling_score(closeadj, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxdv_504d_slope_v090_signal(closeadj, volume):
    dv = closeadj * volume
    base = (_f009_coiling_score(closeadj, 504) + 1.0) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v091-v105: slope of consolidation × volume
def f009ctn_f009_consolidation_tightness_consxvol_21d_slope_v091_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_21d_slope_v092_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 21) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_63d_slope_v093_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_63d_slope_v094_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 63) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_126d_slope_v095_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 126) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_252d_slope_v096_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 252) * volume
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_252d_slope_v097_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 252) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_504d_slope_v098_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 504) * volume
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxvol_504d_slope_v099_signal(closeadj, volume):
    base = _f009_tightness_signature(closeadj, 504) * volume
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_21d_slope_v100_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 21) * _mean(dv, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_63d_slope_v101_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 63) * _mean(dv, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_126d_slope_v102_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 126) * _mean(dv, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_252d_slope_v103_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 252) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_504d_slope_v104_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 504) * _mean(dv, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxdv_504d_slope_v105_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f009_tightness_signature(closeadj, 504) * _mean(dv, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v106-v120: slope of in-range × HL range
def f009ctn_f009_consolidation_tightness_inrxhlr_21d_slope_v106_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f009_close_std_norm(closeadj, 21) * rng
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_21d_slope_v107_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f009_close_std_norm(closeadj, 21) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_63d_slope_v108_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f009_close_std_norm(closeadj, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_63d_slope_v109_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f009_close_std_norm(closeadj, 63) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_126d_slope_v110_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f009_close_std_norm(closeadj, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_252d_slope_v111_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f009_close_std_norm(closeadj, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrxhlr_252d_slope_v112_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f009_close_std_norm(closeadj, 252) * rng
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxhlr_21d_slope_v113_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f009_coiling_score(closeadj, 21) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxhlr_63d_slope_v114_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f009_coiling_score(closeadj, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxhlr_126d_slope_v115_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f009_coiling_score(closeadj, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenxhlr_252d_slope_v116_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f009_coiling_score(closeadj, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxhlr_63d_slope_v117_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f009_tightness_signature(closeadj, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxhlr_126d_slope_v118_signal(closeadj, high, low):
    rng = (high - low).rolling(126, min_periods=21).mean()
    base = _f009_tightness_signature(closeadj, 126) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxhlr_252d_slope_v119_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f009_tightness_signature(closeadj, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consxhlr_504d_slope_v120_signal(closeadj, high, low):
    rng = (high - low).rolling(252, min_periods=63).mean()
    base = _f009_tightness_signature(closeadj, 504) * rng
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v121-v135: slope of log(1+in-range) × close
def f009ctn_f009_consolidation_tightness_lninr_21d_slope_v121_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_21d_slope_v122_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_63d_slope_v123_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_63d_slope_v124_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_126d_slope_v125_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_252d_slope_v126_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_252d_slope_v127_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lninr_504d_slope_v128_signal(closeadj):
    base = np.log1p(np.abs(_f009_close_std_norm(closeadj, 504)) + 1.0) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnblen_21d_slope_v129_signal(closeadj):
    base = np.log1p(np.abs(_f009_coiling_score(closeadj, 21)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnblen_63d_slope_v130_signal(closeadj):
    base = np.log1p(np.abs(_f009_coiling_score(closeadj, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnblen_126d_slope_v131_signal(closeadj):
    base = np.log1p(np.abs(_f009_coiling_score(closeadj, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lnblen_252d_slope_v132_signal(closeadj):
    base = np.log1p(np.abs(_f009_coiling_score(closeadj, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lncons_63d_slope_v133_signal(closeadj):
    base = np.log1p(np.abs(_f009_tightness_signature(closeadj, 63)) + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lncons_126d_slope_v134_signal(closeadj):
    base = np.log1p(np.abs(_f009_tightness_signature(closeadj, 126)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_lncons_252d_slope_v135_signal(closeadj):
    base = np.log1p(np.abs(_f009_tightness_signature(closeadj, 252)) + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136-v150: composite slope
def f009ctn_f009_consolidation_tightness_inrema_21d_slope_v136_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrema_63d_slope_v137_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_inrema_252d_slope_v138_signal(closeadj):
    base = _f009_close_std_norm(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_21d_slope_v139_signal(closeadj):
    base = _f009_coiling_score(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_63d_slope_v140_signal(closeadj):
    base = _f009_coiling_score(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenema_252d_slope_v141_signal(closeadj):
    base = _f009_coiling_score(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consema_21d_slope_v142_signal(closeadj):
    base = _f009_tightness_signature(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consema_63d_slope_v143_signal(closeadj):
    base = _f009_tightness_signature(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consema_252d_slope_v144_signal(closeadj):
    base = _f009_tightness_signature(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenplusinr_63d_slope_v145_signal(closeadj):
    base = (_f009_coiling_score(closeadj, 63) + _f009_close_std_norm(closeadj, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenplusinr_126d_slope_v146_signal(closeadj):
    base = (_f009_coiling_score(closeadj, 126) + _f009_close_std_norm(closeadj, 126)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_blenplusinr_252d_slope_v147_signal(closeadj):
    base = (_f009_coiling_score(closeadj, 252) + _f009_close_std_norm(closeadj, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consplusinr_63d_slope_v148_signal(closeadj):
    base = (_f009_tightness_signature(closeadj, 63) + _f009_close_std_norm(closeadj, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consplusinr_126d_slope_v149_signal(closeadj):
    base = (_f009_tightness_signature(closeadj, 126) + _f009_close_std_norm(closeadj, 126)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f009ctn_f009_consolidation_tightness_consplusinr_252d_slope_v150_signal(closeadj):
    base = (_f009_tightness_signature(closeadj, 252) + _f009_close_std_norm(closeadj, 252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f009ctn_f009_consolidation_tightness_inrange_21d_slope_v001_signal,
    f009ctn_f009_consolidation_tightness_inrange_21d_slope_v002_signal,
    f009ctn_f009_consolidation_tightness_inrange_42d_slope_v003_signal,
    f009ctn_f009_consolidation_tightness_inrange_42d_slope_v004_signal,
    f009ctn_f009_consolidation_tightness_inrange_63d_slope_v005_signal,
    f009ctn_f009_consolidation_tightness_inrange_63d_slope_v006_signal,
    f009ctn_f009_consolidation_tightness_inrange_126d_slope_v007_signal,
    f009ctn_f009_consolidation_tightness_inrange_126d_slope_v008_signal,
    f009ctn_f009_consolidation_tightness_inrange_252d_slope_v009_signal,
    f009ctn_f009_consolidation_tightness_inrange_252d_slope_v010_signal,
    f009ctn_f009_consolidation_tightness_inrange_504d_slope_v011_signal,
    f009ctn_f009_consolidation_tightness_inrange_504d_slope_v012_signal,
    f009ctn_f009_consolidation_tightness_inrange_504d_slope_v013_signal,
    f009ctn_f009_consolidation_tightness_inrange_189d_slope_v014_signal,
    f009ctn_f009_consolidation_tightness_inrange_378d_slope_v015_signal,
    f009ctn_f009_consolidation_tightness_blen_21d_slope_v016_signal,
    f009ctn_f009_consolidation_tightness_blen_21d_slope_v017_signal,
    f009ctn_f009_consolidation_tightness_blen_42d_slope_v018_signal,
    f009ctn_f009_consolidation_tightness_blen_63d_slope_v019_signal,
    f009ctn_f009_consolidation_tightness_blen_63d_slope_v020_signal,
    f009ctn_f009_consolidation_tightness_blen_126d_slope_v021_signal,
    f009ctn_f009_consolidation_tightness_blen_126d_slope_v022_signal,
    f009ctn_f009_consolidation_tightness_blen_252d_slope_v023_signal,
    f009ctn_f009_consolidation_tightness_blen_252d_slope_v024_signal,
    f009ctn_f009_consolidation_tightness_blen_504d_slope_v025_signal,
    f009ctn_f009_consolidation_tightness_blen_504d_slope_v026_signal,
    f009ctn_f009_consolidation_tightness_blen_504d_slope_v027_signal,
    f009ctn_f009_consolidation_tightness_blen_189d_slope_v028_signal,
    f009ctn_f009_consolidation_tightness_blen_378d_slope_v029_signal,
    f009ctn_f009_consolidation_tightness_blen_42d_slope_v030_signal,
    f009ctn_f009_consolidation_tightness_consdur_21d_slope_v031_signal,
    f009ctn_f009_consolidation_tightness_consdur_21d_slope_v032_signal,
    f009ctn_f009_consolidation_tightness_consdur_63d_slope_v033_signal,
    f009ctn_f009_consolidation_tightness_consdur_63d_slope_v034_signal,
    f009ctn_f009_consolidation_tightness_consdur_126d_slope_v035_signal,
    f009ctn_f009_consolidation_tightness_consdur_126d_slope_v036_signal,
    f009ctn_f009_consolidation_tightness_consdur_252d_slope_v037_signal,
    f009ctn_f009_consolidation_tightness_consdur_252d_slope_v038_signal,
    f009ctn_f009_consolidation_tightness_consdur_504d_slope_v039_signal,
    f009ctn_f009_consolidation_tightness_consdur_504d_slope_v040_signal,
    f009ctn_f009_consolidation_tightness_consdur_504d_slope_v041_signal,
    f009ctn_f009_consolidation_tightness_consdur_189d_slope_v042_signal,
    f009ctn_f009_consolidation_tightness_consdur_378d_slope_v043_signal,
    f009ctn_f009_consolidation_tightness_consdur_42d_slope_v044_signal,
    f009ctn_f009_consolidation_tightness_consdur_42d_slope_v045_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_21d_slope_v046_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_21d_slope_v047_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_63d_slope_v048_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_63d_slope_v049_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_126d_slope_v050_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_126d_slope_v051_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_252d_slope_v052_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_252d_slope_v053_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v054_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v055_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_504d_slope_v056_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_42d_slope_v057_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_42d_slope_v058_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_189d_slope_v059_signal,
    f009ctn_f009_consolidation_tightness_inrnorm_378d_slope_v060_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_21d_slope_v061_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_21d_slope_v062_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_63d_slope_v063_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_63d_slope_v064_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_126d_slope_v065_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_252d_slope_v066_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_252d_slope_v067_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_504d_slope_v068_signal,
    f009ctn_f009_consolidation_tightness_inrxvol_504d_slope_v069_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_21d_slope_v070_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_63d_slope_v071_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_252d_slope_v072_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_252d_slope_v073_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_504d_slope_v074_signal,
    f009ctn_f009_consolidation_tightness_inrxdv_504d_slope_v075_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_21d_slope_v076_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_21d_slope_v077_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_63d_slope_v078_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_63d_slope_v079_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_126d_slope_v080_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_252d_slope_v081_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_252d_slope_v082_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_504d_slope_v083_signal,
    f009ctn_f009_consolidation_tightness_blenxvol_504d_slope_v084_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_21d_slope_v085_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_63d_slope_v086_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_126d_slope_v087_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_252d_slope_v088_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_504d_slope_v089_signal,
    f009ctn_f009_consolidation_tightness_blenxdv_504d_slope_v090_signal,
    f009ctn_f009_consolidation_tightness_consxvol_21d_slope_v091_signal,
    f009ctn_f009_consolidation_tightness_consxvol_21d_slope_v092_signal,
    f009ctn_f009_consolidation_tightness_consxvol_63d_slope_v093_signal,
    f009ctn_f009_consolidation_tightness_consxvol_63d_slope_v094_signal,
    f009ctn_f009_consolidation_tightness_consxvol_126d_slope_v095_signal,
    f009ctn_f009_consolidation_tightness_consxvol_252d_slope_v096_signal,
    f009ctn_f009_consolidation_tightness_consxvol_252d_slope_v097_signal,
    f009ctn_f009_consolidation_tightness_consxvol_504d_slope_v098_signal,
    f009ctn_f009_consolidation_tightness_consxvol_504d_slope_v099_signal,
    f009ctn_f009_consolidation_tightness_consxdv_21d_slope_v100_signal,
    f009ctn_f009_consolidation_tightness_consxdv_63d_slope_v101_signal,
    f009ctn_f009_consolidation_tightness_consxdv_126d_slope_v102_signal,
    f009ctn_f009_consolidation_tightness_consxdv_252d_slope_v103_signal,
    f009ctn_f009_consolidation_tightness_consxdv_504d_slope_v104_signal,
    f009ctn_f009_consolidation_tightness_consxdv_504d_slope_v105_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_21d_slope_v106_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_21d_slope_v107_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_63d_slope_v108_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_63d_slope_v109_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_126d_slope_v110_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_252d_slope_v111_signal,
    f009ctn_f009_consolidation_tightness_inrxhlr_252d_slope_v112_signal,
    f009ctn_f009_consolidation_tightness_blenxhlr_21d_slope_v113_signal,
    f009ctn_f009_consolidation_tightness_blenxhlr_63d_slope_v114_signal,
    f009ctn_f009_consolidation_tightness_blenxhlr_126d_slope_v115_signal,
    f009ctn_f009_consolidation_tightness_blenxhlr_252d_slope_v116_signal,
    f009ctn_f009_consolidation_tightness_consxhlr_63d_slope_v117_signal,
    f009ctn_f009_consolidation_tightness_consxhlr_126d_slope_v118_signal,
    f009ctn_f009_consolidation_tightness_consxhlr_252d_slope_v119_signal,
    f009ctn_f009_consolidation_tightness_consxhlr_504d_slope_v120_signal,
    f009ctn_f009_consolidation_tightness_lninr_21d_slope_v121_signal,
    f009ctn_f009_consolidation_tightness_lninr_21d_slope_v122_signal,
    f009ctn_f009_consolidation_tightness_lninr_63d_slope_v123_signal,
    f009ctn_f009_consolidation_tightness_lninr_63d_slope_v124_signal,
    f009ctn_f009_consolidation_tightness_lninr_126d_slope_v125_signal,
    f009ctn_f009_consolidation_tightness_lninr_252d_slope_v126_signal,
    f009ctn_f009_consolidation_tightness_lninr_252d_slope_v127_signal,
    f009ctn_f009_consolidation_tightness_lninr_504d_slope_v128_signal,
    f009ctn_f009_consolidation_tightness_lnblen_21d_slope_v129_signal,
    f009ctn_f009_consolidation_tightness_lnblen_63d_slope_v130_signal,
    f009ctn_f009_consolidation_tightness_lnblen_126d_slope_v131_signal,
    f009ctn_f009_consolidation_tightness_lnblen_252d_slope_v132_signal,
    f009ctn_f009_consolidation_tightness_lncons_63d_slope_v133_signal,
    f009ctn_f009_consolidation_tightness_lncons_126d_slope_v134_signal,
    f009ctn_f009_consolidation_tightness_lncons_252d_slope_v135_signal,
    f009ctn_f009_consolidation_tightness_inrema_21d_slope_v136_signal,
    f009ctn_f009_consolidation_tightness_inrema_63d_slope_v137_signal,
    f009ctn_f009_consolidation_tightness_inrema_252d_slope_v138_signal,
    f009ctn_f009_consolidation_tightness_blenema_21d_slope_v139_signal,
    f009ctn_f009_consolidation_tightness_blenema_63d_slope_v140_signal,
    f009ctn_f009_consolidation_tightness_blenema_252d_slope_v141_signal,
    f009ctn_f009_consolidation_tightness_consema_21d_slope_v142_signal,
    f009ctn_f009_consolidation_tightness_consema_63d_slope_v143_signal,
    f009ctn_f009_consolidation_tightness_consema_252d_slope_v144_signal,
    f009ctn_f009_consolidation_tightness_blenplusinr_63d_slope_v145_signal,
    f009ctn_f009_consolidation_tightness_blenplusinr_126d_slope_v146_signal,
    f009ctn_f009_consolidation_tightness_blenplusinr_252d_slope_v147_signal,
    f009ctn_f009_consolidation_tightness_consplusinr_63d_slope_v148_signal,
    f009ctn_f009_consolidation_tightness_consplusinr_126d_slope_v149_signal,
    f009ctn_f009_consolidation_tightness_consplusinr_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F009_CONSOLIDATION_TIGHTNESS_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f009_close_std_norm", "_f009_coiling_score", "_f009_tightness_signature")
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
    print(f"OK f009_consolidation_tightness_2nd_derivatives_001_150_claude: {n_features} features pass")
