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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f22_margin_floor(grossmargin, w):
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f22_margin_input_resilience(grossmargin, cor, revenue, w):
    cor_ratio = cor / revenue.replace(0, np.nan).abs()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    cor_std = cor_ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return cor_std / gm_std.replace(0, np.nan).abs()


def _f22_pricing_durability_score(grossmargin, ebitdamargin, w):
    gm_avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em_avg = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    em_std = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm_avg + em_avg) - (gm_std + em_std)


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# v001..v030: base jerks on the 3 primitives
@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_5d_jerk_v001_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_10d_jerk_v002_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_21d_jerk_v003_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_42d_jerk_v004_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_63d_jerk_v005_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_126d_jerk_v006_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_63d_21d_jerk_v007_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_126d_21d_jerk_v008_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_504d_63d_jerk_v009_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_504d_21d_jerk_v010_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_5d_jerk_v011_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_10d_jerk_v012_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_21d_jerk_v013_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_42d_jerk_v014_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_63d_jerk_v015_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_126d_jerk_v016_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_63d_21d_jerk_v017_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_126d_21d_jerk_v018_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_504d_63d_jerk_v019_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_504d_21d_jerk_v020_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_5d_jerk_v021_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_10d_jerk_v022_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_21d_jerk_v023_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_42d_jerk_v024_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_63d_jerk_v025_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_126d_jerk_v026_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_63d_21d_jerk_v027_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_126d_21d_jerk_v028_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_504d_63d_jerk_v029_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_504d_21d_jerk_v030_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema21_21d_jerk_v031_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema21_21d_jerk_v032_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema21_21d_jerk_v033_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema63_21d_jerk_v034_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema63_21d_jerk_v035_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema63_21d_jerk_v036_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema126_63d_jerk_v037_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema126_63d_jerk_v038_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema126_63d_jerk_v039_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema252_63d_jerk_v040_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema252_63d_jerk_v041_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema252_63d_jerk_v042_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z, std jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_z252_21d_jerk_v043_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_z252_21d_jerk_v044_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_z252_21d_jerk_v045_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_std63_21d_jerk_v046_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_std63_21d_jerk_v047_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_std63_21d_jerk_v048_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# log/sqrt/sq jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_log_21d_jerk_v049_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_log_21d_jerk_v050_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_log_21d_jerk_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_sqrt_21d_jerk_v052_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_sqrt_21d_jerk_v053_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_sqrt_21d_jerk_v054_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_sq_21d_jerk_v055_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_sq_21d_jerk_v056_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_sq_21d_jerk_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# composites jerks
@_add
def f22mpd_f22_machinery_pricing_durability_comp_sf_21d_jerk_v058_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sf_63d_jerk_v059_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sr_21d_jerk_v060_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s + r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sr_63d_jerk_v061_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s + r) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_fr_21d_jerk_v062_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f + r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_fr_63d_jerk_v063_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f + r) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_21d_jerk_v064_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_63d_jerk_v065_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_126d_jerk_v066_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sxr_21d_jerk_v067_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s * r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sxf_21d_jerk_v068_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s * f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_rxf_21d_jerk_v069_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f * r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_x_21d_jerk_v070_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s * r * f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_sf_21d_jerk_v071_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s - f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_sr_21d_jerk_v072_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s - r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_fr_21d_jerk_v073_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f - r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_rank252_21d_jerk_v074_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_rank252_21d_jerk_v075_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_rank252_21d_jerk_v076_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# More smoothed base jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_w63_21d_jerk_v077_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w63_21d_jerk_v078_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w63_21d_jerk_v079_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w126_21d_jerk_v080_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w126_21d_jerk_v081_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w126_21d_jerk_v082_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w504_63d_jerk_v083_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w504_63d_jerk_v084_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w504_63d_jerk_v085_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Regime jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_regime_21d_jerk_v086_signal(grossmargin, closeadj):
    a = _f22_margin_floor(grossmargin, 63)
    b = _f22_margin_floor(grossmargin, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_regime_21d_jerk_v087_signal(grossmargin, cor, revenue, closeadj):
    a = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    b = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_regime_21d_jerk_v088_signal(grossmargin, ebitdamargin, closeadj):
    a = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    b = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Range jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_range_21d_jerk_v089_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    rng = (base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_range_63d_jerk_v090_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rng = (base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_range_252d_jerk_v091_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_max252_63d_jerk_v092_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_min252_63d_jerk_v093_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_med252_63d_jerk_v094_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_med252_21d_jerk_v095_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_med252_21d_jerk_v096_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue-weighted jerks
@_add
def f22mpd_f22_machinery_pricing_durability_score_x_revenue_21d_jerk_v097_signal(grossmargin, ebitdamargin, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = s * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_x_revenue_21d_jerk_v098_signal(grossmargin, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = f * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_x_revenue_21d_jerk_v099_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = r * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Demean jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_demean_21d_jerk_v100_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    base = (f - _mean(f, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_demean_21d_jerk_v101_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (r - _mean(r, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_demean_21d_jerk_v102_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (s - _mean(s, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Inverse jerks
@_add
def f22mpd_f22_machinery_pricing_durability_floor_inv_21d_jerk_v103_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    base = (1.0 / (f.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_inv_21d_jerk_v104_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (1.0 / (r.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_inv_21d_jerk_v105_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (1.0 / (s.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Weighted composites
@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_w_21d_jerk_v106_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (0.5 * s + 0.3 * r + 0.2 * f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_w_63d_jerk_v107_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (0.5 * s + 0.3 * r + 0.2 * f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Different windows for smoothed-base
@_add
def f22mpd_f22_machinery_pricing_durability_floor_w42_21d_jerk_v108_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w42_21d_jerk_v109_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w42_21d_jerk_v110_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w189_42d_jerk_v111_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w189_42d_jerk_v112_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w189_42d_jerk_v113_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w378_63d_jerk_v114_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w378_63d_jerk_v115_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w378_63d_jerk_v116_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w5_5d_jerk_v117_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w5_5d_jerk_v118_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w5_5d_jerk_v119_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w10_10d_jerk_v120_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w10_10d_jerk_v121_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w10_10d_jerk_v122_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w63_63d_jerk_v123_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w63_63d_jerk_v124_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w63_63d_jerk_v125_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w126_63d_jerk_v126_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w126_63d_jerk_v127_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w126_63d_jerk_v128_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w504_126d_jerk_v129_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w504_126d_jerk_v130_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w504_126d_jerk_v131_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w42_42d_jerk_v132_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w42_42d_jerk_v133_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w42_42d_jerk_v134_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# Slope-of-slope variants
@_add
def f22mpd_f22_machinery_pricing_durability_floor_slope_then_jerk_v135_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_slope_then_jerk_v136_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_slope_then_jerk_v137_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_slope42_then_jerk_v138_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_slope42_then_jerk_v139_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_slope42_then_jerk_v140_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_slope_then_jerk_v141_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_xclose2_jerk_v142_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_xclose2_jerk_v143_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_xclose2_jerk_v144_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_x_cor_jerk_v145_signal(grossmargin, cor, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = f * cg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_x_cor_jerk_v146_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = r * cg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_x_cor_jerk_v147_signal(grossmargin, ebitdamargin, cor, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = s * cg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_z63_21d_jerk_v148_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_z63_21d_jerk_v149_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_z63_21d_jerk_v150_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_MACHINERY_PRICING_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "cor": cor,
            "grossmargin": grossmargin, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f22_margin_floor", "_f22_margin_input_resilience", "_f22_pricing_durability_score")
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
    print(f"OK f22_machinery_pricing_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
