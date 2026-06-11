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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f28_service_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f28_margin_stability(ebitdamargin, w):
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (sd.replace(0, np.nan) + 1e-6)


def _f28_durability_score(ebitdamargin, grossmargin, w):
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (em * gm) / (sd.replace(0, np.nan) + 1e-6)


# 3d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v001_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v002_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v003_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v004_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v005_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v006_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v007_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v008_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v009_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloor base_w=21
def f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v010_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    base = f * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v011_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v012_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v013_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v014_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v015_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v016_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v017_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v018_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v019_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloor base_w=63
def f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v020_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    base = f * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v021_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v022_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v023_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v024_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v025_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v026_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v027_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v028_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v029_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloor base_w=252
def f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v030_signal(ebitdamargin, closeadj):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    base = f * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_3d_jerk_v031_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_5d_jerk_v032_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_10d_jerk_v033_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_21d_jerk_v034_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_42d_jerk_v035_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_63d_jerk_v036_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_84d_jerk_v037_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_126d_jerk_v038_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_168d_jerk_v039_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of mstab base_w=21
def f28cms_f28_cro_margin_stability_mstab_189d_jerk_v040_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 21)
    base = ms * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_3d_jerk_v041_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_5d_jerk_v042_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_10d_jerk_v043_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_21d_jerk_v044_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_42d_jerk_v045_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_63d_jerk_v046_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_84d_jerk_v047_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_126d_jerk_v048_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_168d_jerk_v049_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of mstab base_w=63
def f28cms_f28_cro_margin_stability_mstab_189d_jerk_v050_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 63)
    base = ms * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_3d_jerk_v051_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_5d_jerk_v052_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_10d_jerk_v053_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_21d_jerk_v054_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_42d_jerk_v055_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_63d_jerk_v056_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_84d_jerk_v057_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_126d_jerk_v058_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_168d_jerk_v059_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of mstab base_w=252
def f28cms_f28_cro_margin_stability_mstab_189d_jerk_v060_signal(ebitdamargin, closeadj):
    ms = _f28_margin_stability(ebitdamargin, 252)
    base = ms * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_3d_jerk_v061_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_5d_jerk_v062_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_10d_jerk_v063_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_21d_jerk_v064_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_42d_jerk_v065_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_63d_jerk_v066_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_84d_jerk_v067_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_126d_jerk_v068_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_168d_jerk_v069_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscore base_w=21
def f28cms_f28_cro_margin_stability_durscore_189d_jerk_v070_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 21)
    base = ds * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_3d_jerk_v071_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_5d_jerk_v072_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_10d_jerk_v073_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_21d_jerk_v074_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_42d_jerk_v075_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_63d_jerk_v076_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_84d_jerk_v077_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_126d_jerk_v078_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_168d_jerk_v079_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscore base_w=63
def f28cms_f28_cro_margin_stability_durscore_189d_jerk_v080_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 63)
    base = ds * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_3d_jerk_v081_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_5d_jerk_v082_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_10d_jerk_v083_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_21d_jerk_v084_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_42d_jerk_v085_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_63d_jerk_v086_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_84d_jerk_v087_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_126d_jerk_v088_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_168d_jerk_v089_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscore base_w=252
def f28cms_f28_cro_margin_stability_durscore_189d_jerk_v090_signal(ebitdamargin, grossmargin, closeadj):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 252)
    base = ds * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v091_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v092_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v093_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v094_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v095_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v096_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v097_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v098_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v099_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloorxrev base_w=21
def f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v100_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 21)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = f * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v101_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v102_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v103_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v104_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v105_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v106_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v107_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v108_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v109_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloorxrev base_w=63
def f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v110_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 63)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = f * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v111_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v112_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v113_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v114_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v115_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v116_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v117_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v118_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v119_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of smfloorxrev base_w=252
def f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v120_signal(ebitdamargin, revenue):
    f = _f28_service_margin_floor(ebitdamargin, 252)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = f * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v121_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v122_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v123_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v124_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v125_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v126_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v127_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v128_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v129_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscorexrev base_w=42
def f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v130_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v131_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v132_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v133_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v134_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v135_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v136_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v137_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v138_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v139_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscorexrev base_w=126
def f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v140_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v141_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v142_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v143_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v144_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v145_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v146_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v147_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v148_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v149_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of durscorexrev base_w=504
def f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v150_signal(ebitdamargin, grossmargin, revenue):
    ds = _f28_durability_score(ebitdamargin, grossmargin, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = ds * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v001_signal,
    f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v002_signal,
    f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v003_signal,
    f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v004_signal,
    f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v005_signal,
    f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v006_signal,
    f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v007_signal,
    f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v008_signal,
    f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v009_signal,
    f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v010_signal,
    f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v011_signal,
    f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v012_signal,
    f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v013_signal,
    f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v014_signal,
    f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v015_signal,
    f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v016_signal,
    f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v017_signal,
    f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v018_signal,
    f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v019_signal,
    f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v020_signal,
    f28cms_f28_cro_margin_stability_smfloor_3d_jerk_v021_signal,
    f28cms_f28_cro_margin_stability_smfloor_5d_jerk_v022_signal,
    f28cms_f28_cro_margin_stability_smfloor_10d_jerk_v023_signal,
    f28cms_f28_cro_margin_stability_smfloor_21d_jerk_v024_signal,
    f28cms_f28_cro_margin_stability_smfloor_42d_jerk_v025_signal,
    f28cms_f28_cro_margin_stability_smfloor_63d_jerk_v026_signal,
    f28cms_f28_cro_margin_stability_smfloor_84d_jerk_v027_signal,
    f28cms_f28_cro_margin_stability_smfloor_126d_jerk_v028_signal,
    f28cms_f28_cro_margin_stability_smfloor_168d_jerk_v029_signal,
    f28cms_f28_cro_margin_stability_smfloor_189d_jerk_v030_signal,
    f28cms_f28_cro_margin_stability_mstab_3d_jerk_v031_signal,
    f28cms_f28_cro_margin_stability_mstab_5d_jerk_v032_signal,
    f28cms_f28_cro_margin_stability_mstab_10d_jerk_v033_signal,
    f28cms_f28_cro_margin_stability_mstab_21d_jerk_v034_signal,
    f28cms_f28_cro_margin_stability_mstab_42d_jerk_v035_signal,
    f28cms_f28_cro_margin_stability_mstab_63d_jerk_v036_signal,
    f28cms_f28_cro_margin_stability_mstab_84d_jerk_v037_signal,
    f28cms_f28_cro_margin_stability_mstab_126d_jerk_v038_signal,
    f28cms_f28_cro_margin_stability_mstab_168d_jerk_v039_signal,
    f28cms_f28_cro_margin_stability_mstab_189d_jerk_v040_signal,
    f28cms_f28_cro_margin_stability_mstab_3d_jerk_v041_signal,
    f28cms_f28_cro_margin_stability_mstab_5d_jerk_v042_signal,
    f28cms_f28_cro_margin_stability_mstab_10d_jerk_v043_signal,
    f28cms_f28_cro_margin_stability_mstab_21d_jerk_v044_signal,
    f28cms_f28_cro_margin_stability_mstab_42d_jerk_v045_signal,
    f28cms_f28_cro_margin_stability_mstab_63d_jerk_v046_signal,
    f28cms_f28_cro_margin_stability_mstab_84d_jerk_v047_signal,
    f28cms_f28_cro_margin_stability_mstab_126d_jerk_v048_signal,
    f28cms_f28_cro_margin_stability_mstab_168d_jerk_v049_signal,
    f28cms_f28_cro_margin_stability_mstab_189d_jerk_v050_signal,
    f28cms_f28_cro_margin_stability_mstab_3d_jerk_v051_signal,
    f28cms_f28_cro_margin_stability_mstab_5d_jerk_v052_signal,
    f28cms_f28_cro_margin_stability_mstab_10d_jerk_v053_signal,
    f28cms_f28_cro_margin_stability_mstab_21d_jerk_v054_signal,
    f28cms_f28_cro_margin_stability_mstab_42d_jerk_v055_signal,
    f28cms_f28_cro_margin_stability_mstab_63d_jerk_v056_signal,
    f28cms_f28_cro_margin_stability_mstab_84d_jerk_v057_signal,
    f28cms_f28_cro_margin_stability_mstab_126d_jerk_v058_signal,
    f28cms_f28_cro_margin_stability_mstab_168d_jerk_v059_signal,
    f28cms_f28_cro_margin_stability_mstab_189d_jerk_v060_signal,
    f28cms_f28_cro_margin_stability_durscore_3d_jerk_v061_signal,
    f28cms_f28_cro_margin_stability_durscore_5d_jerk_v062_signal,
    f28cms_f28_cro_margin_stability_durscore_10d_jerk_v063_signal,
    f28cms_f28_cro_margin_stability_durscore_21d_jerk_v064_signal,
    f28cms_f28_cro_margin_stability_durscore_42d_jerk_v065_signal,
    f28cms_f28_cro_margin_stability_durscore_63d_jerk_v066_signal,
    f28cms_f28_cro_margin_stability_durscore_84d_jerk_v067_signal,
    f28cms_f28_cro_margin_stability_durscore_126d_jerk_v068_signal,
    f28cms_f28_cro_margin_stability_durscore_168d_jerk_v069_signal,
    f28cms_f28_cro_margin_stability_durscore_189d_jerk_v070_signal,
    f28cms_f28_cro_margin_stability_durscore_3d_jerk_v071_signal,
    f28cms_f28_cro_margin_stability_durscore_5d_jerk_v072_signal,
    f28cms_f28_cro_margin_stability_durscore_10d_jerk_v073_signal,
    f28cms_f28_cro_margin_stability_durscore_21d_jerk_v074_signal,
    f28cms_f28_cro_margin_stability_durscore_42d_jerk_v075_signal,
    f28cms_f28_cro_margin_stability_durscore_63d_jerk_v076_signal,
    f28cms_f28_cro_margin_stability_durscore_84d_jerk_v077_signal,
    f28cms_f28_cro_margin_stability_durscore_126d_jerk_v078_signal,
    f28cms_f28_cro_margin_stability_durscore_168d_jerk_v079_signal,
    f28cms_f28_cro_margin_stability_durscore_189d_jerk_v080_signal,
    f28cms_f28_cro_margin_stability_durscore_3d_jerk_v081_signal,
    f28cms_f28_cro_margin_stability_durscore_5d_jerk_v082_signal,
    f28cms_f28_cro_margin_stability_durscore_10d_jerk_v083_signal,
    f28cms_f28_cro_margin_stability_durscore_21d_jerk_v084_signal,
    f28cms_f28_cro_margin_stability_durscore_42d_jerk_v085_signal,
    f28cms_f28_cro_margin_stability_durscore_63d_jerk_v086_signal,
    f28cms_f28_cro_margin_stability_durscore_84d_jerk_v087_signal,
    f28cms_f28_cro_margin_stability_durscore_126d_jerk_v088_signal,
    f28cms_f28_cro_margin_stability_durscore_168d_jerk_v089_signal,
    f28cms_f28_cro_margin_stability_durscore_189d_jerk_v090_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v091_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v092_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v093_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v094_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v095_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v096_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v097_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v098_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v099_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v100_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v101_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v102_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v103_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v104_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v105_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v106_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v107_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v108_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v109_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v110_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_3d_jerk_v111_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_5d_jerk_v112_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_10d_jerk_v113_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_21d_jerk_v114_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_42d_jerk_v115_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_63d_jerk_v116_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_84d_jerk_v117_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_126d_jerk_v118_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_168d_jerk_v119_signal,
    f28cms_f28_cro_margin_stability_smfloorxrev_189d_jerk_v120_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v121_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v122_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v123_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v124_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v125_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v126_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v127_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v128_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v129_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v130_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v131_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v132_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v133_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v134_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v135_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v136_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v137_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v138_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v139_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v140_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_3d_jerk_v141_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_5d_jerk_v142_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_10d_jerk_v143_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_21d_jerk_v144_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_42d_jerk_v145_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_63d_jerk_v146_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_84d_jerk_v147_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_126d_jerk_v148_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_168d_jerk_v149_signal,
    f28cms_f28_cro_margin_stability_durscorexrev_189d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CRO_MARGIN_STABILITY_REGISTRY_JERK_001_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_service_margin_floor", "_f28_margin_stability", "_f28_durability_score",)
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
    print(f"OK f28_cro_margin_stability_3rd_derivatives_001_150_claude: {n_features} features pass")
