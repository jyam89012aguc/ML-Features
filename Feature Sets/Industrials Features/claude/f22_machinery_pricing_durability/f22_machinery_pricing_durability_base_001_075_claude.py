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
def _f22_margin_floor(grossmargin, w):
    # rolling min of gross margin -- the floor it never breaks below
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f22_margin_input_resilience(grossmargin, cor, revenue, w):
    # gross margin stability normalized by input cost volatility
    cor_ratio = cor / revenue.replace(0, np.nan).abs()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    cor_std = cor_ratio.rolling(w, min_periods=max(1, w // 2)).std()
    return cor_std / gm_std.replace(0, np.nan).abs()


def _f22_pricing_durability_score(grossmargin, ebitdamargin, w):
    # composite of both margins' mean minus their combined std
    gm_avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em_avg = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    em_std = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm_avg + em_avg) - (gm_std + em_std)


# v001..v015 margin floor
def f22mpd_f22_machinery_pricing_durability_floor_21d_base_v001_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_63d_base_v002_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_126d_base_v003_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_252d_base_v004_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_504d_base_v005_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_5d_base_v006_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_42d_base_v007_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_189d_base_v008_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_378d_base_v009_signal(grossmargin, closeadj):
    result = _f22_margin_floor(grossmargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_252_minus_close_base_v010_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 252)
    result = (grossmargin - floor) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_63_minus_close_base_v011_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 63)
    result = (grossmargin - floor) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_252_dev_base_v012_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 252)
    result = (grossmargin / floor.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_pct_252d_base_v013_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 252)
    result = ((grossmargin - floor) / grossmargin.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_std_252d_base_v014_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 252)
    result = _std(floor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_mean_252d_base_v015_signal(grossmargin, closeadj):
    floor = _f22_margin_floor(grossmargin, 252)
    result = _mean(floor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016..v030 input resilience
def f22mpd_f22_machinery_pricing_durability_resilience_21d_base_v016_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_63d_base_v017_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_126d_base_v018_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_252d_base_v019_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_504d_base_v020_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_42d_base_v021_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_189d_base_v022_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_378d_base_v023_signal(grossmargin, cor, revenue, closeadj):
    result = _f22_margin_input_resilience(grossmargin, cor, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_mean_252d_base_v024_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_z_252d_base_v025_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_z_504d_base_v026_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_std_252d_base_v027_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_sq_252d_base_v028_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_log_252d_base_v029_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resilience_sqrt_252d_base_v030_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031..v045 durability score
def f22mpd_f22_machinery_pricing_durability_score_21d_base_v031_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_63d_base_v032_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_126d_base_v033_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_252d_base_v034_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_504d_base_v035_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_5d_base_v036_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_42d_base_v037_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_189d_base_v038_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_378d_base_v039_signal(grossmargin, ebitdamargin, closeadj):
    result = _f22_pricing_durability_score(grossmargin, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_z_252d_base_v040_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_z_504d_base_v041_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_mean_252d_base_v042_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_std_252d_base_v043_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_ema_252d_base_v044_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_pulse_base_v045_signal(grossmargin, ebitdamargin, closeadj):
    a = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    b = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046..v060 combos
def f22mpd_f22_machinery_pricing_durability_score_x_resil_base_v046_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = s * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_plus_floor_base_v047_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = (s + f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_minus_resil_base_v048_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (s - r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_x_resil_base_v049_signal(grossmargin, cor, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = f * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_combo_base_v050_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = (s + r + f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_w_base_v051_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = (0.5 * s + 0.3 * r + 0.2 * f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_product_base_v052_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = s * r * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_demean_252d_base_v053_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_z_252d_base_v054_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_z_504d_base_v055_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_log_252d_base_v056_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_sqrt_252d_base_v057_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_sq_252d_base_v058_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_med_252d_base_v059_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_med_252d_base_v060_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_med_252d_base_v061_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_ema_63d_base_v062_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_ema_63d_base_v063_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_minus_floor_base_v064_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = (r - f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_div_floor_base_v065_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = _safe_div(r, f.abs() + 1e-6) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_pulse_63d_base_v066_signal(grossmargin, ebitdamargin, closeadj):
    a = _f22_pricing_durability_score(grossmargin, ebitdamargin, 21)
    b = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_pulse_63d_base_v067_signal(grossmargin, closeadj):
    a = _f22_margin_floor(grossmargin, 63)
    b = _f22_margin_floor(grossmargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_pulse_63d_base_v068_signal(grossmargin, cor, revenue, closeadj):
    a = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    b = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_x_close2_base_v069_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_x_close2_base_v070_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_x_close2_base_v071_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_rank_252d_base_v072_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_rank_252d_base_v073_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_rank_252d_base_v074_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_z_252d_base_v075_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = s + r + f
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22mpd_f22_machinery_pricing_durability_floor_21d_base_v001_signal,
    f22mpd_f22_machinery_pricing_durability_floor_63d_base_v002_signal,
    f22mpd_f22_machinery_pricing_durability_floor_126d_base_v003_signal,
    f22mpd_f22_machinery_pricing_durability_floor_252d_base_v004_signal,
    f22mpd_f22_machinery_pricing_durability_floor_504d_base_v005_signal,
    f22mpd_f22_machinery_pricing_durability_floor_5d_base_v006_signal,
    f22mpd_f22_machinery_pricing_durability_floor_42d_base_v007_signal,
    f22mpd_f22_machinery_pricing_durability_floor_189d_base_v008_signal,
    f22mpd_f22_machinery_pricing_durability_floor_378d_base_v009_signal,
    f22mpd_f22_machinery_pricing_durability_floor_252_minus_close_base_v010_signal,
    f22mpd_f22_machinery_pricing_durability_floor_63_minus_close_base_v011_signal,
    f22mpd_f22_machinery_pricing_durability_floor_252_dev_base_v012_signal,
    f22mpd_f22_machinery_pricing_durability_floor_pct_252d_base_v013_signal,
    f22mpd_f22_machinery_pricing_durability_floor_std_252d_base_v014_signal,
    f22mpd_f22_machinery_pricing_durability_floor_mean_252d_base_v015_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_21d_base_v016_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_63d_base_v017_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_126d_base_v018_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_252d_base_v019_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_504d_base_v020_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_42d_base_v021_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_189d_base_v022_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_378d_base_v023_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_mean_252d_base_v024_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_z_252d_base_v025_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_z_504d_base_v026_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_std_252d_base_v027_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_sq_252d_base_v028_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_log_252d_base_v029_signal,
    f22mpd_f22_machinery_pricing_durability_resilience_sqrt_252d_base_v030_signal,
    f22mpd_f22_machinery_pricing_durability_score_21d_base_v031_signal,
    f22mpd_f22_machinery_pricing_durability_score_63d_base_v032_signal,
    f22mpd_f22_machinery_pricing_durability_score_126d_base_v033_signal,
    f22mpd_f22_machinery_pricing_durability_score_252d_base_v034_signal,
    f22mpd_f22_machinery_pricing_durability_score_504d_base_v035_signal,
    f22mpd_f22_machinery_pricing_durability_score_5d_base_v036_signal,
    f22mpd_f22_machinery_pricing_durability_score_42d_base_v037_signal,
    f22mpd_f22_machinery_pricing_durability_score_189d_base_v038_signal,
    f22mpd_f22_machinery_pricing_durability_score_378d_base_v039_signal,
    f22mpd_f22_machinery_pricing_durability_score_z_252d_base_v040_signal,
    f22mpd_f22_machinery_pricing_durability_score_z_504d_base_v041_signal,
    f22mpd_f22_machinery_pricing_durability_score_mean_252d_base_v042_signal,
    f22mpd_f22_machinery_pricing_durability_score_std_252d_base_v043_signal,
    f22mpd_f22_machinery_pricing_durability_score_ema_252d_base_v044_signal,
    f22mpd_f22_machinery_pricing_durability_score_pulse_base_v045_signal,
    f22mpd_f22_machinery_pricing_durability_score_x_resil_base_v046_signal,
    f22mpd_f22_machinery_pricing_durability_score_plus_floor_base_v047_signal,
    f22mpd_f22_machinery_pricing_durability_score_minus_resil_base_v048_signal,
    f22mpd_f22_machinery_pricing_durability_floor_x_resil_base_v049_signal,
    f22mpd_f22_machinery_pricing_durability_triple_combo_base_v050_signal,
    f22mpd_f22_machinery_pricing_durability_triple_w_base_v051_signal,
    f22mpd_f22_machinery_pricing_durability_triple_product_base_v052_signal,
    f22mpd_f22_machinery_pricing_durability_score_demean_252d_base_v053_signal,
    f22mpd_f22_machinery_pricing_durability_floor_z_252d_base_v054_signal,
    f22mpd_f22_machinery_pricing_durability_floor_z_504d_base_v055_signal,
    f22mpd_f22_machinery_pricing_durability_floor_log_252d_base_v056_signal,
    f22mpd_f22_machinery_pricing_durability_floor_sqrt_252d_base_v057_signal,
    f22mpd_f22_machinery_pricing_durability_floor_sq_252d_base_v058_signal,
    f22mpd_f22_machinery_pricing_durability_resil_med_252d_base_v059_signal,
    f22mpd_f22_machinery_pricing_durability_floor_med_252d_base_v060_signal,
    f22mpd_f22_machinery_pricing_durability_score_med_252d_base_v061_signal,
    f22mpd_f22_machinery_pricing_durability_floor_ema_63d_base_v062_signal,
    f22mpd_f22_machinery_pricing_durability_resil_ema_63d_base_v063_signal,
    f22mpd_f22_machinery_pricing_durability_resil_minus_floor_base_v064_signal,
    f22mpd_f22_machinery_pricing_durability_resil_div_floor_base_v065_signal,
    f22mpd_f22_machinery_pricing_durability_score_pulse_63d_base_v066_signal,
    f22mpd_f22_machinery_pricing_durability_floor_pulse_63d_base_v067_signal,
    f22mpd_f22_machinery_pricing_durability_resil_pulse_63d_base_v068_signal,
    f22mpd_f22_machinery_pricing_durability_score_x_close2_base_v069_signal,
    f22mpd_f22_machinery_pricing_durability_floor_x_close2_base_v070_signal,
    f22mpd_f22_machinery_pricing_durability_resil_x_close2_base_v071_signal,
    f22mpd_f22_machinery_pricing_durability_score_rank_252d_base_v072_signal,
    f22mpd_f22_machinery_pricing_durability_floor_rank_252d_base_v073_signal,
    f22mpd_f22_machinery_pricing_durability_resil_rank_252d_base_v074_signal,
    f22mpd_f22_machinery_pricing_durability_triple_z_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_MACHINERY_PRICING_DURABILITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f22_machinery_pricing_durability_base_001_075_claude: {n_features} features pass")
