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


# Floor base, varied slope windows
@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_5d_slope_v001_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_10d_slope_v002_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_21d_slope_v003_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_42d_slope_v004_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_63d_slope_v005_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_126d_slope_v006_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_252d_slope_v007_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_63d_21d_slope_v008_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_126d_21d_slope_v009_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_504d_63d_slope_v010_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Resilience base
@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_5d_slope_v011_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_10d_slope_v012_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_21d_slope_v013_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_42d_slope_v014_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_63d_slope_v015_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_126d_slope_v016_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_252d_slope_v017_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_63d_21d_slope_v018_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_126d_21d_slope_v019_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_504d_63d_slope_v020_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Score base
@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_5d_slope_v021_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_10d_slope_v022_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_21d_slope_v023_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_42d_slope_v024_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_63d_slope_v025_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_126d_slope_v026_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_252d_slope_v027_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_63d_21d_slope_v028_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_126d_21d_slope_v029_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_504d_63d_slope_v030_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Slope_diff_norm variants
@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_dn5_slope_v031_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_dn21_slope_v032_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_dn63_slope_v033_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_252d_dn126_slope_v034_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_dn5_slope_v035_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_dn21_slope_v036_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_dn63_slope_v037_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_252d_dn126_slope_v038_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_dn5_slope_v039_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_dn21_slope_v040_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_dn63_slope_v041_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_252d_dn126_slope_v042_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_504d_21d_slope_v043_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_504d_21d_slope_v044_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_504d_21d_slope_v045_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-smoothed slopes
@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema21_21d_slope_v046_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema21_21d_slope_v047_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema21_21d_slope_v048_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema63_21d_slope_v049_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema63_21d_slope_v050_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema63_21d_slope_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema126_63d_slope_v052_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema126_63d_slope_v053_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema126_63d_slope_v054_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_ema252_63d_slope_v055_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_ema252_63d_slope_v056_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_ema252_63d_slope_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z/std/abs/log transforms then slope
@_add
def f22mpd_f22_machinery_pricing_durability_floor_z252_21d_slope_v058_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_z252_21d_slope_v059_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_z252_21d_slope_v060_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_std63_21d_slope_v061_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_std63_21d_slope_v062_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_std63_21d_slope_v063_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_log_21d_slope_v064_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_log_21d_slope_v065_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_log_21d_slope_v066_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_sqrt_21d_slope_v067_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_sqrt_21d_slope_v068_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_sqrt_21d_slope_v069_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_sq_21d_slope_v070_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_sq_21d_slope_v071_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_sq_21d_slope_v072_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Composites and rank slopes
@_add
def f22mpd_f22_machinery_pricing_durability_comp_sf_21d_slope_v073_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sf_63d_slope_v074_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sr_21d_slope_v075_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s + r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sr_63d_slope_v076_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s + r) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_fr_21d_slope_v077_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f + r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_fr_63d_slope_v078_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f + r) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_21d_slope_v079_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_63d_slope_v080_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_126d_slope_v081_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sxr_21d_slope_v082_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s * r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_sxf_21d_slope_v083_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s * f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_rxf_21d_slope_v084_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f * r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_x_21d_slope_v085_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s * r * f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_sf_21d_slope_v086_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s - f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_sr_21d_slope_v087_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (s - r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_diff_fr_21d_slope_v088_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (f - r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_rank252_21d_slope_v089_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_rank252_21d_slope_v090_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_rank252_21d_slope_v091_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w63_21d_slope_v092_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 63), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w63_21d_slope_v093_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 63), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w63_21d_slope_v094_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 63), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w126_21d_slope_v095_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 126), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w126_21d_slope_v096_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 126), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w126_21d_slope_v097_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 126), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w504_63d_slope_v098_signal(grossmargin, closeadj):
    base = _mean(_f22_margin_floor(grossmargin, 504), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w504_63d_slope_v099_signal(grossmargin, cor, revenue, closeadj):
    base = _mean(_f22_margin_input_resilience(grossmargin, cor, revenue, 504), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w504_63d_slope_v100_signal(grossmargin, ebitdamargin, closeadj):
    base = _mean(_f22_pricing_durability_score(grossmargin, ebitdamargin, 504), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# More mixed: regimes, ranges, cross-window
@_add
def f22mpd_f22_machinery_pricing_durability_floor_regime_21d_slope_v101_signal(grossmargin, closeadj):
    a = _f22_margin_floor(grossmargin, 63)
    b = _f22_margin_floor(grossmargin, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_regime_21d_slope_v102_signal(grossmargin, cor, revenue, closeadj):
    a = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    b = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_regime_21d_slope_v103_signal(grossmargin, ebitdamargin, closeadj):
    a = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    b = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_range_21d_slope_v104_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    rng = (base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_range_63d_slope_v105_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rng = (base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_range_252d_slope_v106_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_max252_63d_slope_v107_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_min252_63d_slope_v108_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_med252_63d_slope_v109_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_med252_21d_slope_v110_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_med252_21d_slope_v111_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_x_revenue_21d_slope_v112_signal(grossmargin, ebitdamargin, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = s * rg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_x_revenue_21d_slope_v113_signal(grossmargin, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = f * rg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_x_revenue_21d_slope_v114_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = r * rg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_demean_21d_slope_v115_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    base = (f - _mean(f, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_demean_21d_slope_v116_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (r - _mean(r, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_demean_21d_slope_v117_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (s - _mean(s, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_inv_21d_slope_v118_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    base = (1.0 / (f.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_inv_21d_slope_v119_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    base = (1.0 / (r.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_inv_21d_slope_v120_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    base = (1.0 / (s.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_w_21d_slope_v121_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (0.5 * s + 0.3 * r + 0.2 * f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_w_63d_slope_v122_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (0.5 * s + 0.3 * r + 0.2 * f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_dn21_slope_v123_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_comp_srf_dn63_slope_v124_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = (s + r + f) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w42_21d_slope_v125_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w42_21d_slope_v126_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w42_21d_slope_v127_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w189_42d_slope_v128_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w189_42d_slope_v129_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w189_42d_slope_v130_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w378_63d_slope_v131_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w378_63d_slope_v132_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w378_63d_slope_v133_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w5_5d_slope_v134_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w5_5d_slope_v135_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w5_5d_slope_v136_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w10_10d_slope_v137_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w10_10d_slope_v138_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w10_10d_slope_v139_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w63_63d_slope_v140_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w63_63d_slope_v141_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w63_63d_slope_v142_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w126_63d_slope_v143_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w126_63d_slope_v144_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w126_63d_slope_v145_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w504_126d_slope_v146_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w504_126d_slope_v147_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_score_w504_126d_slope_v148_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_floor_w42_42d_slope_v149_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f22mpd_f22_machinery_pricing_durability_resil_w42_42d_slope_v150_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_MACHINERY_PRICING_DURABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f22_machinery_pricing_durability_2nd_derivatives_001_150_claude: {n_features} features pass")
