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
def _f006_in_range_count(close, w):
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    mn = close.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (mx - mn).replace(0, np.nan).abs()
    pos = (close - mn) / rng
    inside = ((pos >= 0.15) & (pos <= 0.85)).astype(float)
    return inside.rolling(w, min_periods=max(1, w // 2)).sum()


def _f006_base_length(close, w):
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    mn = close.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (mx - mn) / mn.replace(0, np.nan).abs()
    med = rng.rolling(252, min_periods=63).median()
    tight = (rng < med).astype(float)
    grp = (1.0 - tight).cumsum()
    return tight.groupby(grp).cumsum()


def _f006_consolidation_duration(close, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    cv = sd / m.replace(0, np.nan).abs()
    quiet = (cv < cv.rolling(252, min_periods=63).median()).astype(float)
    grp = (1.0 - quiet).cumsum()
    return quiet.groupby(grp).cumsum()


# v001-v005: in-range count at varying windows scaled by close
def f006bln_f006_base_length_inrange_21d_base_v001_signal(closeadj):
    result = _f006_in_range_count(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrange_42d_base_v002_signal(closeadj):
    result = _f006_in_range_count(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrange_63d_base_v003_signal(closeadj):
    result = _f006_in_range_count(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrange_126d_base_v004_signal(closeadj):
    result = _f006_in_range_count(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrange_252d_base_v005_signal(closeadj):
    result = _f006_in_range_count(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006-v010: base length (consecutive tight days) at varying windows
def f006bln_f006_base_length_blen_21d_base_v006_signal(closeadj):
    result = _f006_base_length(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blen_42d_base_v007_signal(closeadj):
    result = _f006_base_length(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blen_63d_base_v008_signal(closeadj):
    result = _f006_base_length(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blen_126d_base_v009_signal(closeadj):
    result = _f006_base_length(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blen_252d_base_v010_signal(closeadj):
    result = _f006_base_length(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011-v015: consolidation duration scaled by close
def f006bln_f006_base_length_consdur_21d_base_v011_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consdur_63d_base_v012_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consdur_126d_base_v013_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consdur_252d_base_v014_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consdur_504d_base_v015_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016-v020: in-range fraction (count / w)
def f006bln_f006_base_length_inrfrac_21d_base_v016_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 21) / 21.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfrac_63d_base_v017_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 63) / 63.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfrac_126d_base_v018_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 126) / 126.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfrac_252d_base_v019_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 252) / 252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfrac_504d_base_v020_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 504) / 504.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021-v025: rolling mean of in-range count
def f006bln_f006_base_length_inrmean_21d_base_v021_signal(closeadj):
    result = _mean(_f006_in_range_count(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrmean_63d_base_v022_signal(closeadj):
    result = _mean(_f006_in_range_count(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrmean_126d_base_v023_signal(closeadj):
    result = _mean(_f006_in_range_count(closeadj, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrmean_252d_base_v024_signal(closeadj):
    result = _mean(_f006_in_range_count(closeadj, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrmean_504d_base_v025_signal(closeadj):
    result = _mean(_f006_in_range_count(closeadj, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026-v030: rolling std of base length
def f006bln_f006_base_length_blenstd_21d_base_v026_signal(closeadj):
    result = _std(_f006_base_length(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenstd_63d_base_v027_signal(closeadj):
    result = _std(_f006_base_length(closeadj, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenstd_126d_base_v028_signal(closeadj):
    result = _std(_f006_base_length(closeadj, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenstd_252d_base_v029_signal(closeadj):
    result = _std(_f006_base_length(closeadj, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenstd_504d_base_v030_signal(closeadj):
    result = _std(_f006_base_length(closeadj, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031-v035: z-score of in-range count
def f006bln_f006_base_length_inrz_21d_base_v031_signal(closeadj):
    result = _z(_f006_in_range_count(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrz_63d_base_v032_signal(closeadj):
    result = _z(_f006_in_range_count(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrz_126d_base_v033_signal(closeadj):
    result = _z(_f006_in_range_count(closeadj, 126), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrz_252d_base_v034_signal(closeadj):
    result = _z(_f006_in_range_count(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrz_504d_base_v035_signal(closeadj):
    result = _z(_f006_in_range_count(closeadj, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v040: z-score of base length
def f006bln_f006_base_length_blenz_21d_base_v036_signal(closeadj):
    result = _z(_f006_base_length(closeadj, 21), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenz_63d_base_v037_signal(closeadj):
    result = _z(_f006_base_length(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenz_126d_base_v038_signal(closeadj):
    result = _z(_f006_base_length(closeadj, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenz_252d_base_v039_signal(closeadj):
    result = _z(_f006_base_length(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenz_504d_base_v040_signal(closeadj):
    result = _z(_f006_base_length(closeadj, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041-v045: consolidation duration z-score
def f006bln_f006_base_length_consz_21d_base_v041_signal(closeadj):
    result = _z(_f006_consolidation_duration(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consz_63d_base_v042_signal(closeadj):
    result = _z(_f006_consolidation_duration(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consz_126d_base_v043_signal(closeadj):
    result = _z(_f006_consolidation_duration(closeadj, 126), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consz_252d_base_v044_signal(closeadj):
    result = _z(_f006_consolidation_duration(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_consz_504d_base_v045_signal(closeadj):
    result = _z(_f006_consolidation_duration(closeadj, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046-v050: in-range × log close
def f006bln_f006_base_length_inrlog_21d_base_v046_signal(closeadj):
    result = _f006_in_range_count(closeadj, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrlog_63d_base_v047_signal(closeadj):
    result = _f006_in_range_count(closeadj, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrlog_126d_base_v048_signal(closeadj):
    result = _f006_in_range_count(closeadj, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrlog_252d_base_v049_signal(closeadj):
    result = _f006_in_range_count(closeadj, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrlog_504d_base_v050_signal(closeadj):
    result = _f006_in_range_count(closeadj, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v051-v055: base length × log close
def f006bln_f006_base_length_blenlog_21d_base_v051_signal(closeadj):
    result = _f006_base_length(closeadj, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenlog_63d_base_v052_signal(closeadj):
    result = _f006_base_length(closeadj, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenlog_126d_base_v053_signal(closeadj):
    result = _f006_base_length(closeadj, 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenlog_252d_base_v054_signal(closeadj):
    result = _f006_base_length(closeadj, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenlog_504d_base_v055_signal(closeadj):
    result = _f006_base_length(closeadj, 504) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v056-v060: in-range fraction × close²
def f006bln_f006_base_length_inrfracsq_21d_base_v056_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 21) / 21.0) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfracsq_63d_base_v057_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 63) / 63.0) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfracsq_252d_base_v058_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 252) / 252.0) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrfracsq_504d_base_v059_signal(closeadj):
    result = (_f006_in_range_count(closeadj, 504) / 504.0) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: consolidation × close²
def f006bln_f006_base_length_conssq_252d_base_v060_signal(closeadj):
    result = _f006_consolidation_duration(closeadj, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061-v065: composite (base length + consolidation duration) × close
def f006bln_f006_base_length_blenpluscons_21d_base_v061_signal(closeadj):
    result = (_f006_base_length(closeadj, 21) + _f006_consolidation_duration(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenpluscons_63d_base_v062_signal(closeadj):
    result = (_f006_base_length(closeadj, 63) + _f006_consolidation_duration(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenpluscons_126d_base_v063_signal(closeadj):
    result = (_f006_base_length(closeadj, 126) + _f006_consolidation_duration(closeadj, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenpluscons_252d_base_v064_signal(closeadj):
    result = (_f006_base_length(closeadj, 252) + _f006_consolidation_duration(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_blenpluscons_504d_base_v065_signal(closeadj):
    result = (_f006_base_length(closeadj, 504) + _f006_consolidation_duration(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v070: EMA of in-range count
def f006bln_f006_base_length_inrema_21d_base_v066_signal(closeadj):
    base = _f006_in_range_count(closeadj, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrema_63d_base_v067_signal(closeadj):
    base = _f006_in_range_count(closeadj, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrema_126d_base_v068_signal(closeadj):
    base = _f006_in_range_count(closeadj, 126)
    result = base.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrema_252d_base_v069_signal(closeadj):
    base = _f006_in_range_count(closeadj, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_inrema_504d_base_v070_signal(closeadj):
    base = _f006_in_range_count(closeadj, 504)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071-v075: signed base length × close (signed by trend)
def f006bln_f006_base_length_signed_21d_base_v071_signal(closeadj):
    base = _f006_base_length(closeadj, 21)
    sgn = np.sign(closeadj - _mean(closeadj, 21))
    result = base * sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_signed_63d_base_v072_signal(closeadj):
    base = _f006_base_length(closeadj, 63)
    sgn = np.sign(closeadj - _mean(closeadj, 63))
    result = base * sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_signed_126d_base_v073_signal(closeadj):
    base = _f006_base_length(closeadj, 126)
    sgn = np.sign(closeadj - _mean(closeadj, 126))
    result = base * sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_signed_252d_base_v074_signal(closeadj):
    base = _f006_base_length(closeadj, 252)
    sgn = np.sign(closeadj - _mean(closeadj, 252))
    result = base * sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f006bln_f006_base_length_signed_504d_base_v075_signal(closeadj):
    base = _f006_base_length(closeadj, 504)
    sgn = np.sign(closeadj - _mean(closeadj, 252))
    result = base * sgn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f006bln_f006_base_length_inrange_21d_base_v001_signal,
    f006bln_f006_base_length_inrange_42d_base_v002_signal,
    f006bln_f006_base_length_inrange_63d_base_v003_signal,
    f006bln_f006_base_length_inrange_126d_base_v004_signal,
    f006bln_f006_base_length_inrange_252d_base_v005_signal,
    f006bln_f006_base_length_blen_21d_base_v006_signal,
    f006bln_f006_base_length_blen_42d_base_v007_signal,
    f006bln_f006_base_length_blen_63d_base_v008_signal,
    f006bln_f006_base_length_blen_126d_base_v009_signal,
    f006bln_f006_base_length_blen_252d_base_v010_signal,
    f006bln_f006_base_length_consdur_21d_base_v011_signal,
    f006bln_f006_base_length_consdur_63d_base_v012_signal,
    f006bln_f006_base_length_consdur_126d_base_v013_signal,
    f006bln_f006_base_length_consdur_252d_base_v014_signal,
    f006bln_f006_base_length_consdur_504d_base_v015_signal,
    f006bln_f006_base_length_inrfrac_21d_base_v016_signal,
    f006bln_f006_base_length_inrfrac_63d_base_v017_signal,
    f006bln_f006_base_length_inrfrac_126d_base_v018_signal,
    f006bln_f006_base_length_inrfrac_252d_base_v019_signal,
    f006bln_f006_base_length_inrfrac_504d_base_v020_signal,
    f006bln_f006_base_length_inrmean_21d_base_v021_signal,
    f006bln_f006_base_length_inrmean_63d_base_v022_signal,
    f006bln_f006_base_length_inrmean_126d_base_v023_signal,
    f006bln_f006_base_length_inrmean_252d_base_v024_signal,
    f006bln_f006_base_length_inrmean_504d_base_v025_signal,
    f006bln_f006_base_length_blenstd_21d_base_v026_signal,
    f006bln_f006_base_length_blenstd_63d_base_v027_signal,
    f006bln_f006_base_length_blenstd_126d_base_v028_signal,
    f006bln_f006_base_length_blenstd_252d_base_v029_signal,
    f006bln_f006_base_length_blenstd_504d_base_v030_signal,
    f006bln_f006_base_length_inrz_21d_base_v031_signal,
    f006bln_f006_base_length_inrz_63d_base_v032_signal,
    f006bln_f006_base_length_inrz_126d_base_v033_signal,
    f006bln_f006_base_length_inrz_252d_base_v034_signal,
    f006bln_f006_base_length_inrz_504d_base_v035_signal,
    f006bln_f006_base_length_blenz_21d_base_v036_signal,
    f006bln_f006_base_length_blenz_63d_base_v037_signal,
    f006bln_f006_base_length_blenz_126d_base_v038_signal,
    f006bln_f006_base_length_blenz_252d_base_v039_signal,
    f006bln_f006_base_length_blenz_504d_base_v040_signal,
    f006bln_f006_base_length_consz_21d_base_v041_signal,
    f006bln_f006_base_length_consz_63d_base_v042_signal,
    f006bln_f006_base_length_consz_126d_base_v043_signal,
    f006bln_f006_base_length_consz_252d_base_v044_signal,
    f006bln_f006_base_length_consz_504d_base_v045_signal,
    f006bln_f006_base_length_inrlog_21d_base_v046_signal,
    f006bln_f006_base_length_inrlog_63d_base_v047_signal,
    f006bln_f006_base_length_inrlog_126d_base_v048_signal,
    f006bln_f006_base_length_inrlog_252d_base_v049_signal,
    f006bln_f006_base_length_inrlog_504d_base_v050_signal,
    f006bln_f006_base_length_blenlog_21d_base_v051_signal,
    f006bln_f006_base_length_blenlog_63d_base_v052_signal,
    f006bln_f006_base_length_blenlog_126d_base_v053_signal,
    f006bln_f006_base_length_blenlog_252d_base_v054_signal,
    f006bln_f006_base_length_blenlog_504d_base_v055_signal,
    f006bln_f006_base_length_inrfracsq_21d_base_v056_signal,
    f006bln_f006_base_length_inrfracsq_63d_base_v057_signal,
    f006bln_f006_base_length_inrfracsq_252d_base_v058_signal,
    f006bln_f006_base_length_inrfracsq_504d_base_v059_signal,
    f006bln_f006_base_length_conssq_252d_base_v060_signal,
    f006bln_f006_base_length_blenpluscons_21d_base_v061_signal,
    f006bln_f006_base_length_blenpluscons_63d_base_v062_signal,
    f006bln_f006_base_length_blenpluscons_126d_base_v063_signal,
    f006bln_f006_base_length_blenpluscons_252d_base_v064_signal,
    f006bln_f006_base_length_blenpluscons_504d_base_v065_signal,
    f006bln_f006_base_length_inrema_21d_base_v066_signal,
    f006bln_f006_base_length_inrema_63d_base_v067_signal,
    f006bln_f006_base_length_inrema_126d_base_v068_signal,
    f006bln_f006_base_length_inrema_252d_base_v069_signal,
    f006bln_f006_base_length_inrema_504d_base_v070_signal,
    f006bln_f006_base_length_signed_21d_base_v071_signal,
    f006bln_f006_base_length_signed_63d_base_v072_signal,
    f006bln_f006_base_length_signed_126d_base_v073_signal,
    f006bln_f006_base_length_signed_252d_base_v074_signal,
    f006bln_f006_base_length_signed_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F006_BASE_LENGTH_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f006_in_range_count", "_f006_base_length", "_f006_consolidation_duration")
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
    print(f"OK f006_base_length_base_001_075_claude: {n_features} features pass")
