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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f037_up_vol(close, volume, w):
    up = (close.diff() > 0).astype(float)
    return (up * volume).rolling(w, min_periods=max(1, w // 2)).sum()


def _f037_down_vol(close, volume, w):
    down = (close.diff() < 0).astype(float)
    return (down * volume).rolling(w, min_periods=max(1, w // 2)).sum()


def _f037_ud_ratio(close, volume, w):
    upv = _f037_up_vol(close, volume, w)
    dnv = _f037_down_vol(close, volume, w)
    return upv / (dnv + 1.0).replace(0, np.nan)


# helper - build feature - bind w
def _make_slope(name, base_fn, sw):
    pass


# === up_vol slope features (1-30) ===
def f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v001_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v002_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v003_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v004_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v005_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v006_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_126d_slope_v007_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_126d_slope_v008_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v009_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v010_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v011_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_504d_slope_v012_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_504d_slope_v013_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_5d_slope_v014_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_10d_slope_v015_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 10)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_42d_slope_v016_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_189d_slope_v017_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 189)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_378d_slope_v018_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v019_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v020_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# === down_vol slope features (21-40) ===
def f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v021_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v022_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v023_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v024_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v025_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_126d_slope_v026_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_126d_slope_v027_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v028_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v029_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v030_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_504d_slope_v031_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_504d_slope_v032_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_5d_slope_v033_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_10d_slope_v034_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 10)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_42d_slope_v035_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_189d_slope_v036_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 189)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_378d_slope_v037_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v038_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v039_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v040_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# === ud_ratio slope features (41-90) ===
def f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v041_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v042_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v043_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v044_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v045_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v046_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_126d_slope_v047_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_126d_slope_v048_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v049_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v050_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v051_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_504d_slope_v052_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_504d_slope_v053_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_5d_slope_v054_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_10d_slope_v055_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_42d_slope_v056_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_189d_slope_v057_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udratio_378d_slope_v058_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspread_21d_slope_v059_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspread_63d_slope_v060_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspread_252d_slope_v061_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspreadnorm_21d_slope_v062_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    base = _safe_div(upv - dnv, upv + dnv) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspreadnorm_63d_slope_v063_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    base = _safe_div(upv - dnv, upv + dnv) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udspreadnorm_252d_slope_v064_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    base = _safe_div(upv - dnv, upv + dnv) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_meanud_21d_slope_v065_signal(closeadj, volume):
    base = _mean(_f037_ud_ratio(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_meanud_63d_slope_v066_signal(closeadj, volume):
    base = _mean(_f037_ud_ratio(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_meanud_252d_slope_v067_signal(closeadj, volume):
    base = _mean(_f037_ud_ratio(closeadj, volume, 252), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_stdud_21d_slope_v068_signal(closeadj, volume):
    base = _std(_f037_ud_ratio(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_stdud_63d_slope_v069_signal(closeadj, volume):
    base = _std(_f037_ud_ratio(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_zud_21d_slope_v070_signal(closeadj, volume):
    base = _z(_f037_ud_ratio(closeadj, volume, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_zud_63d_slope_v071_signal(closeadj, volume):
    base = _z(_f037_ud_ratio(closeadj, volume, 63), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaud_21d_slope_v072_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaud_63d_slope_v073_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddev_21d_slope_v074_signal(closeadj, volume):
    base = (_f037_ud_ratio(closeadj, volume, 21) - 1.0).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddev_63d_slope_v075_signal(closeadj, volume):
    base = (_f037_ud_ratio(closeadj, volume, 63) - 1.0).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_squd_21d_slope_v076_signal(closeadj, volume):
    r = _f037_ud_ratio(closeadj, volume, 21)
    base = r * r.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_squd_63d_slope_v077_signal(closeadj, volume):
    r = _f037_ud_ratio(closeadj, volume, 63)
    base = r * r.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_updaycnt_21d_slope_v078_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    total_vol = volume.rolling(21, min_periods=5).sum()
    base = _safe_div(upv, total_vol) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_updaycnt_63d_slope_v079_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    total_vol = volume.rolling(63, min_periods=10).sum()
    base = _safe_div(upv, total_vol) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_updaycnt_252d_slope_v080_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    total_vol = volume.rolling(252, min_periods=21).sum()
    base = _safe_div(upv, total_vol) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upbias_21d_slope_v081_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    base = (_safe_div(upv, upv + dnv) - 0.5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upbias_63d_slope_v082_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    base = (_safe_div(upv, upv + dnv) - 0.5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upbias_252d_slope_v083_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    base = (_safe_div(upv, upv + dnv) - 0.5) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolxcl_21d_slope_v084_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolxcl_63d_slope_v085_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolxcl_252d_slope_v086_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolxcl_21d_slope_v087_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolxcl_63d_slope_v088_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolxcl_252d_slope_v089_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxvolz_21d_slope_v090_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxvolz_63d_slope_v091_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signspread_21d_slope_v092_signal(closeadj, volume):
    base = np.sign(_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signspread_63d_slope_v093_signal(closeadj, volume):
    base = np.sign(_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signspread_252d_slope_v094_signal(closeadj, volume):
    base = np.sign(_f037_up_vol(closeadj, volume, 252) - _f037_down_vol(closeadj, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signud_21d_slope_v095_signal(closeadj, volume):
    base = np.sign(_f037_ud_ratio(closeadj, volume, 21) - 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signud_63d_slope_v096_signal(closeadj, volume):
    base = np.sign(_f037_ud_ratio(closeadj, volume, 63) - 1.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_logud_21d_slope_v097_signal(closeadj, volume):
    base = np.log(_f037_ud_ratio(closeadj, volume, 21).replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_logud_63d_slope_v098_signal(closeadj, volume):
    base = np.log(_f037_ud_ratio(closeadj, volume, 63).replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_sqrtud_21d_slope_v099_signal(closeadj, volume):
    base = np.sqrt(_f037_ud_ratio(closeadj, volume, 21).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_sqrtud_63d_slope_v100_signal(closeadj, volume):
    base = np.sqrt(_f037_ud_ratio(closeadj, volume, 63).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxdv_21d_slope_v101_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * (closeadj * volume) / 1e6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxdv_63d_slope_v102_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * (closeadj * volume) / 1e6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxvolxcl_21d_slope_v103_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * volume * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxvolxcl_63d_slope_v104_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * volume * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udregime_21_252_slope_v105_signal(closeadj, volume):
    short_r = _f037_ud_ratio(closeadj, volume, 21)
    long_r = _f037_ud_ratio(closeadj, volume, 252)
    base = _safe_div(short_r - long_r, long_r.abs() + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udregime_63_504_slope_v106_signal(closeadj, volume):
    short_r = _f037_ud_ratio(closeadj, volume, 63)
    long_r = _f037_ud_ratio(closeadj, volume, 504)
    base = _safe_div(short_r - long_r, long_r.abs() + 1.0) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxclxvm_21d_slope_v107_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * _mean(closeadj, 21) * _mean(volume, 21) / 1e6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxclxvm_63d_slope_v108_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * _mean(closeadj, 63) * _mean(volume, 63) / 1e6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxclxvm_252d_slope_v109_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252) * _mean(closeadj, 126) * _mean(volume, 126) / 1e6
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxzcl_21d_slope_v110_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * _z(closeadj, 63) / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxzcl_63d_slope_v111_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * _z(closeadj, 126) / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaupvol_21d_slope_v112_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaupvol_63d_slope_v113_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emadnvol_21d_slope_v114_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emadnvol_63d_slope_v115_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolxclmean_21d_slope_v116_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 21) * _mean(closeadj, 21) / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolxclmean_63d_slope_v117_signal(closeadj, volume):
    base = _f037_up_vol(closeadj, volume, 63) * _mean(closeadj, 63) / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolxclmean_21d_slope_v118_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 21) * _mean(closeadj, 21) / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolxclmean_63d_slope_v119_signal(closeadj, volume):
    base = _f037_down_vol(closeadj, volume, 63) * _mean(closeadj, 63) / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxclstd_21d_slope_v120_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 21) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udxclstd_63d_slope_v121_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 63) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddifsh_21d_slope_v122_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    total_vol = volume.rolling(21, min_periods=5).sum()
    base = _safe_div(upv - dnv, total_vol) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddifsh_63d_slope_v123_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    total_vol = volume.rolling(63, min_periods=10).sum()
    base = _safe_div(upv - dnv, total_vol) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddifsh_252d_slope_v124_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    dnv = _f037_down_vol(closeadj, volume, 252)
    total_vol = volume.rolling(252, min_periods=21).sum()
    base = _safe_div(upv - dnv, total_vol) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolgap_21_252_slope_v125_signal(closeadj, volume):
    s21 = _f037_up_vol(closeadj, volume, 21) / 21.0
    s252 = _f037_up_vol(closeadj, volume, 252) / 252.0
    base = (s21 - s252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolgap_21_252_slope_v126_signal(closeadj, volume):
    s21 = _f037_down_vol(closeadj, volume, 21) / 21.0
    s252 = _f037_down_vol(closeadj, volume, 252) / 252.0
    base = (s21 - s252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udprod_21d_slope_v127_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    base = (upv * dnv) / 1e6
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udprod_63d_slope_v128_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    base = (upv * dnv) / 1e6
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upfrac_21d_slope_v129_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    total = upv + _f037_down_vol(closeadj, volume, 21)
    base = _safe_div(upv, total) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upfrac_63d_slope_v130_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    total = upv + _f037_down_vol(closeadj, volume, 63)
    base = _safe_div(upv, total) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upfrac_252d_slope_v131_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 252)
    total = upv + _f037_down_vol(closeadj, volume, 252)
    base = _safe_div(upv, total) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxvolz_21d_slope_v132_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 21) - _f037_down_vol(closeadj, volume, 21)) * _z(volume, 21) / 1e3
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_spreadxvolz_63d_slope_v133_signal(closeadj, volume):
    base = (_f037_up_vol(closeadj, volume, 63) - _f037_down_vol(closeadj, volume, 63)) * _z(volume, 63) / 1e3
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udlonggap_21_252_slope_v134_signal(closeadj, volume):
    base = (_f037_ud_ratio(closeadj, volume, 21) - _f037_ud_ratio(closeadj, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udlonggap_63_504_slope_v135_signal(closeadj, volume):
    base = (_f037_ud_ratio(closeadj, volume, 63) - _f037_ud_ratio(closeadj, volume, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_zud_126d_slope_v136_signal(closeadj, volume):
    base = _z(_f037_ud_ratio(closeadj, volume, 126), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_uddev_252d_slope_v137_signal(closeadj, volume):
    base = (_f037_ud_ratio(closeadj, volume, 252) - 1.0).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_logud_252d_slope_v138_signal(closeadj, volume):
    base = np.log(_f037_ud_ratio(closeadj, volume, 252).replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_meanud_126d_slope_v139_signal(closeadj, volume):
    base = _mean(_f037_ud_ratio(closeadj, volume, 126), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_stdud_126d_slope_v140_signal(closeadj, volume):
    base = _std(_f037_ud_ratio(closeadj, volume, 126), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaud_126d_slope_v141_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 126).ewm(span=63, adjust=False, min_periods=21).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_emaud_252d_slope_v142_signal(closeadj, volume):
    base = _f037_ud_ratio(closeadj, volume, 252).ewm(span=126, adjust=False, min_periods=21).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_upvolregime_21_252_slope_v143_signal(closeadj, volume):
    up21 = _f037_up_vol(closeadj, volume, 21) / 21.0
    up252 = _f037_up_vol(closeadj, volume, 252) / 252.0
    base = _safe_div(up21 - up252, up252.abs() + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_dnvolregime_21_252_slope_v144_signal(closeadj, volume):
    dn21 = _f037_down_vol(closeadj, volume, 21) / 21.0
    dn252 = _f037_down_vol(closeadj, volume, 252) / 252.0
    base = _safe_div(dn21 - dn252, dn252.abs() + 1.0) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udprodxcl_21d_slope_v145_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    base = (upv * dnv) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udprodxcl_63d_slope_v146_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    base = (upv * dnv) * closeadj / 1e9
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signspread_5d_slope_v147_signal(closeadj, volume):
    base = np.sign(_f037_up_vol(closeadj, volume, 5) - _f037_down_vol(closeadj, volume, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_signud_10d_slope_v148_signal(closeadj, volume):
    base = np.sign(_f037_ud_ratio(closeadj, volume, 10) - 1.0) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udnormxvolz_21d_slope_v149_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 21)
    dnv = _f037_down_vol(closeadj, volume, 21)
    base = _safe_div(upv - dnv, upv + dnv) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f037udv_f037_up_down_volume_ratio_udnormxvolz_63d_slope_v150_signal(closeadj, volume):
    upv = _f037_up_vol(closeadj, volume, 63)
    dnv = _f037_down_vol(closeadj, volume, 63)
    base = _safe_div(upv - dnv, upv + dnv) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v001_signal,
    f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v002_signal,
    f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v003_signal,
    f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v004_signal,
    f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v005_signal,
    f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v006_signal,
    f037udv_f037_up_down_volume_ratio_upvol_126d_slope_v007_signal,
    f037udv_f037_up_down_volume_ratio_upvol_126d_slope_v008_signal,
    f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v009_signal,
    f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v010_signal,
    f037udv_f037_up_down_volume_ratio_upvol_252d_slope_v011_signal,
    f037udv_f037_up_down_volume_ratio_upvol_504d_slope_v012_signal,
    f037udv_f037_up_down_volume_ratio_upvol_504d_slope_v013_signal,
    f037udv_f037_up_down_volume_ratio_upvol_5d_slope_v014_signal,
    f037udv_f037_up_down_volume_ratio_upvol_10d_slope_v015_signal,
    f037udv_f037_up_down_volume_ratio_upvol_42d_slope_v016_signal,
    f037udv_f037_up_down_volume_ratio_upvol_189d_slope_v017_signal,
    f037udv_f037_up_down_volume_ratio_upvol_378d_slope_v018_signal,
    f037udv_f037_up_down_volume_ratio_upvol_21d_slope_v019_signal,
    f037udv_f037_up_down_volume_ratio_upvol_63d_slope_v020_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v021_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v022_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v023_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v024_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v025_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_126d_slope_v026_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_126d_slope_v027_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v028_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v029_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v030_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_504d_slope_v031_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_504d_slope_v032_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_5d_slope_v033_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_10d_slope_v034_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_42d_slope_v035_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_189d_slope_v036_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_378d_slope_v037_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_21d_slope_v038_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_63d_slope_v039_signal,
    f037udv_f037_up_down_volume_ratio_dnvol_252d_slope_v040_signal,
    f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v041_signal,
    f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v042_signal,
    f037udv_f037_up_down_volume_ratio_udratio_21d_slope_v043_signal,
    f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v044_signal,
    f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v045_signal,
    f037udv_f037_up_down_volume_ratio_udratio_63d_slope_v046_signal,
    f037udv_f037_up_down_volume_ratio_udratio_126d_slope_v047_signal,
    f037udv_f037_up_down_volume_ratio_udratio_126d_slope_v048_signal,
    f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v049_signal,
    f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v050_signal,
    f037udv_f037_up_down_volume_ratio_udratio_252d_slope_v051_signal,
    f037udv_f037_up_down_volume_ratio_udratio_504d_slope_v052_signal,
    f037udv_f037_up_down_volume_ratio_udratio_504d_slope_v053_signal,
    f037udv_f037_up_down_volume_ratio_udratio_5d_slope_v054_signal,
    f037udv_f037_up_down_volume_ratio_udratio_10d_slope_v055_signal,
    f037udv_f037_up_down_volume_ratio_udratio_42d_slope_v056_signal,
    f037udv_f037_up_down_volume_ratio_udratio_189d_slope_v057_signal,
    f037udv_f037_up_down_volume_ratio_udratio_378d_slope_v058_signal,
    f037udv_f037_up_down_volume_ratio_udspread_21d_slope_v059_signal,
    f037udv_f037_up_down_volume_ratio_udspread_63d_slope_v060_signal,
    f037udv_f037_up_down_volume_ratio_udspread_252d_slope_v061_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_21d_slope_v062_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_63d_slope_v063_signal,
    f037udv_f037_up_down_volume_ratio_udspreadnorm_252d_slope_v064_signal,
    f037udv_f037_up_down_volume_ratio_meanud_21d_slope_v065_signal,
    f037udv_f037_up_down_volume_ratio_meanud_63d_slope_v066_signal,
    f037udv_f037_up_down_volume_ratio_meanud_252d_slope_v067_signal,
    f037udv_f037_up_down_volume_ratio_stdud_21d_slope_v068_signal,
    f037udv_f037_up_down_volume_ratio_stdud_63d_slope_v069_signal,
    f037udv_f037_up_down_volume_ratio_zud_21d_slope_v070_signal,
    f037udv_f037_up_down_volume_ratio_zud_63d_slope_v071_signal,
    f037udv_f037_up_down_volume_ratio_emaud_21d_slope_v072_signal,
    f037udv_f037_up_down_volume_ratio_emaud_63d_slope_v073_signal,
    f037udv_f037_up_down_volume_ratio_uddev_21d_slope_v074_signal,
    f037udv_f037_up_down_volume_ratio_uddev_63d_slope_v075_signal,
    f037udv_f037_up_down_volume_ratio_squd_21d_slope_v076_signal,
    f037udv_f037_up_down_volume_ratio_squd_63d_slope_v077_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_21d_slope_v078_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_63d_slope_v079_signal,
    f037udv_f037_up_down_volume_ratio_updaycnt_252d_slope_v080_signal,
    f037udv_f037_up_down_volume_ratio_upbias_21d_slope_v081_signal,
    f037udv_f037_up_down_volume_ratio_upbias_63d_slope_v082_signal,
    f037udv_f037_up_down_volume_ratio_upbias_252d_slope_v083_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_21d_slope_v084_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_63d_slope_v085_signal,
    f037udv_f037_up_down_volume_ratio_upvolxcl_252d_slope_v086_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_21d_slope_v087_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_63d_slope_v088_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxcl_252d_slope_v089_signal,
    f037udv_f037_up_down_volume_ratio_udxvolz_21d_slope_v090_signal,
    f037udv_f037_up_down_volume_ratio_udxvolz_63d_slope_v091_signal,
    f037udv_f037_up_down_volume_ratio_signspread_21d_slope_v092_signal,
    f037udv_f037_up_down_volume_ratio_signspread_63d_slope_v093_signal,
    f037udv_f037_up_down_volume_ratio_signspread_252d_slope_v094_signal,
    f037udv_f037_up_down_volume_ratio_signud_21d_slope_v095_signal,
    f037udv_f037_up_down_volume_ratio_signud_63d_slope_v096_signal,
    f037udv_f037_up_down_volume_ratio_logud_21d_slope_v097_signal,
    f037udv_f037_up_down_volume_ratio_logud_63d_slope_v098_signal,
    f037udv_f037_up_down_volume_ratio_sqrtud_21d_slope_v099_signal,
    f037udv_f037_up_down_volume_ratio_sqrtud_63d_slope_v100_signal,
    f037udv_f037_up_down_volume_ratio_spreadxdv_21d_slope_v101_signal,
    f037udv_f037_up_down_volume_ratio_spreadxdv_63d_slope_v102_signal,
    f037udv_f037_up_down_volume_ratio_udxvolxcl_21d_slope_v103_signal,
    f037udv_f037_up_down_volume_ratio_udxvolxcl_63d_slope_v104_signal,
    f037udv_f037_up_down_volume_ratio_udregime_21_252_slope_v105_signal,
    f037udv_f037_up_down_volume_ratio_udregime_63_504_slope_v106_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_21d_slope_v107_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_63d_slope_v108_signal,
    f037udv_f037_up_down_volume_ratio_udxclxvm_252d_slope_v109_signal,
    f037udv_f037_up_down_volume_ratio_spreadxzcl_21d_slope_v110_signal,
    f037udv_f037_up_down_volume_ratio_spreadxzcl_63d_slope_v111_signal,
    f037udv_f037_up_down_volume_ratio_emaupvol_21d_slope_v112_signal,
    f037udv_f037_up_down_volume_ratio_emaupvol_63d_slope_v113_signal,
    f037udv_f037_up_down_volume_ratio_emadnvol_21d_slope_v114_signal,
    f037udv_f037_up_down_volume_ratio_emadnvol_63d_slope_v115_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclmean_21d_slope_v116_signal,
    f037udv_f037_up_down_volume_ratio_upvolxclmean_63d_slope_v117_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclmean_21d_slope_v118_signal,
    f037udv_f037_up_down_volume_ratio_dnvolxclmean_63d_slope_v119_signal,
    f037udv_f037_up_down_volume_ratio_udxclstd_21d_slope_v120_signal,
    f037udv_f037_up_down_volume_ratio_udxclstd_63d_slope_v121_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_21d_slope_v122_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_63d_slope_v123_signal,
    f037udv_f037_up_down_volume_ratio_uddifsh_252d_slope_v124_signal,
    f037udv_f037_up_down_volume_ratio_upvolgap_21_252_slope_v125_signal,
    f037udv_f037_up_down_volume_ratio_dnvolgap_21_252_slope_v126_signal,
    f037udv_f037_up_down_volume_ratio_udprod_21d_slope_v127_signal,
    f037udv_f037_up_down_volume_ratio_udprod_63d_slope_v128_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_21d_slope_v129_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_63d_slope_v130_signal,
    f037udv_f037_up_down_volume_ratio_upfrac_252d_slope_v131_signal,
    f037udv_f037_up_down_volume_ratio_spreadxvolz_21d_slope_v132_signal,
    f037udv_f037_up_down_volume_ratio_spreadxvolz_63d_slope_v133_signal,
    f037udv_f037_up_down_volume_ratio_udlonggap_21_252_slope_v134_signal,
    f037udv_f037_up_down_volume_ratio_udlonggap_63_504_slope_v135_signal,
    f037udv_f037_up_down_volume_ratio_zud_126d_slope_v136_signal,
    f037udv_f037_up_down_volume_ratio_uddev_252d_slope_v137_signal,
    f037udv_f037_up_down_volume_ratio_logud_252d_slope_v138_signal,
    f037udv_f037_up_down_volume_ratio_meanud_126d_slope_v139_signal,
    f037udv_f037_up_down_volume_ratio_stdud_126d_slope_v140_signal,
    f037udv_f037_up_down_volume_ratio_emaud_126d_slope_v141_signal,
    f037udv_f037_up_down_volume_ratio_emaud_252d_slope_v142_signal,
    f037udv_f037_up_down_volume_ratio_upvolregime_21_252_slope_v143_signal,
    f037udv_f037_up_down_volume_ratio_dnvolregime_21_252_slope_v144_signal,
    f037udv_f037_up_down_volume_ratio_udprodxcl_21d_slope_v145_signal,
    f037udv_f037_up_down_volume_ratio_udprodxcl_63d_slope_v146_signal,
    f037udv_f037_up_down_volume_ratio_signspread_5d_slope_v147_signal,
    f037udv_f037_up_down_volume_ratio_signud_10d_slope_v148_signal,
    f037udv_f037_up_down_volume_ratio_udnormxvolz_21d_slope_v149_signal,
    f037udv_f037_up_down_volume_ratio_udnormxvolz_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F037_UP_DOWN_VOLUME_RATIO_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f037_up_vol", "_f037_down_vol", "_f037_ud_ratio")
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
    print(f"OK f037_up_down_volume_ratio_2nd_derivatives_001_150_claude: {n_features} features pass")
