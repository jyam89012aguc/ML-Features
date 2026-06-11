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


# v076..v150 -- 75 more features
def f22mpd_f22_machinery_pricing_durability_floor_range_252d_base_v076_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    rng = (f.rolling(252, min_periods=63).max() - f.rolling(252, min_periods=63).min())
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_range_252d_base_v077_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rng = (s.rolling(252, min_periods=63).max() - s.rolling(252, min_periods=63).min())
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_range_252d_base_v078_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rng = (r.rolling(252, min_periods=63).max() - r.rolling(252, min_periods=63).min())
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_max_252d_base_v079_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = f.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_max_252d_base_v080_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = s.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_max_252d_base_v081_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = r.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_min_252d_base_v082_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = f.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_min_252d_base_v083_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = s.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_cv_252d_base_v084_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    cv = _safe_div(_std(s, 252), _mean(s, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_cv_252d_base_v085_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    cv = _safe_div(_std(f, 252), _mean(f, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_cv_252d_base_v086_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    cv = _safe_div(_std(r, 252), _mean(r, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_diff_21d_base_v087_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (s - s.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_diff_63d_base_v088_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (s - s.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_diff_21d_base_v089_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = (f - f.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_diff_63d_base_v090_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = (f - f.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_diff_21d_base_v091_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_diff_63d_base_v092_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (r - r.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_streak_pos_base_v093_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    pos = (s > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_above_quantile_base_v094_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    qt = f.rolling(252, min_periods=63).quantile(0.5)
    ind = (f > qt).astype(float) * f
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_below_quantile_base_v095_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    qt = r.rolling(252, min_periods=63).quantile(0.5)
    ind = (r < qt).astype(float) * r
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_ema21_base_v096_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = s.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_ema21_base_v097_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = f.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_ema21_base_v098_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = r.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w63_base_v099_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w63_base_v100_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w63_base_v101_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w504_base_v102_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w504_base_v103_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w504_base_v104_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w42_base_v105_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w42_base_v106_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w42_base_v107_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w189_base_v108_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w189_base_v109_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w189_base_v110_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w378_base_v111_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w378_base_v112_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w378_base_v113_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_inv_base_v114_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (1.0 / (s.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_inv_base_v115_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = (1.0 / (f.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_inv_base_v116_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (1.0 / (r.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_x_revenue_base_v117_signal(grossmargin, ebitdamargin, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = s * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_x_revenue_base_v118_signal(grossmargin, revenue, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = f * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_x_revenue_base_v119_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = r * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_cross_21_252_base_v120_signal(grossmargin, ebitdamargin, closeadj):
    a = _f22_pricing_durability_score(grossmargin, ebitdamargin, 21)
    b = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_cross_21_252_base_v121_signal(grossmargin, closeadj):
    a = _f22_margin_floor(grossmargin, 21)
    b = _f22_margin_floor(grossmargin, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_cross_21_252_base_v122_signal(grossmargin, cor, revenue, closeadj):
    a = _f22_margin_input_resilience(grossmargin, cor, revenue, 21)
    b = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_ema_dev_base_v123_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    ema = s.ewm(span=252, min_periods=63).mean()
    result = (s - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_ema_dev_base_v124_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    ema = f.ewm(span=252, min_periods=63).mean()
    result = (f - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_ema_dev_base_v125_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    ema = r.ewm(span=252, min_periods=63).mean()
    result = (r - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w63_z_base_v126_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w63_z_base_v127_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w63_z_base_v128_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_sqrt_base_v129_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs()
    result = np.sqrt(s + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_log_base_v130_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252).abs() + 1.0
    result = np.log(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_sq_base_v131_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    result = s * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_x_cor_base_v132_signal(grossmargin, cor, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = f * cg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_x_cor_base_v133_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = r * cg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_x_cor_base_v134_signal(grossmargin, ebitdamargin, cor, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    cg = cor / (cor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = s * cg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_minus_gm_base_v135_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    result = (grossmargin - f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_above_zero_base_v136_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    ind = (s > 0).astype(float) * s
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_above_zero_base_v137_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 252)
    ind = (f > 0).astype(float) * f
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_above_1_base_v138_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    ind = (r > 1.0).astype(float) * r
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_count_pos_base_v139_signal(grossmargin, ebitdamargin, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 63)
    cnt = (s > 0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_count_pos_base_v140_signal(grossmargin, closeadj):
    f = _f22_margin_floor(grossmargin, 21)
    cnt = (f > 0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_count_low_base_v141_signal(grossmargin, cor, revenue, closeadj):
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 63)
    cnt = (r < 1.0).astype(float).rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_w2_base_v142_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    result = (s + 2 * r - 0.5 * f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_mean_252d_base_v143_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = s + r + f
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_std_252d_base_v144_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = s + r + f
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_triple_rank_252d_base_v145_signal(grossmargin, ebitdamargin, cor, revenue, closeadj):
    s = _f22_pricing_durability_score(grossmargin, ebitdamargin, 252)
    r = _f22_margin_input_resilience(grossmargin, cor, revenue, 252)
    f = _f22_margin_floor(grossmargin, 252)
    base = s + r + f
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w21_base_v146_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_floor_w21_base_v147_signal(grossmargin, closeadj):
    base = _f22_margin_floor(grossmargin, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w21_base_v148_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_score_w10_base_v149_signal(grossmargin, ebitdamargin, closeadj):
    base = _f22_pricing_durability_score(grossmargin, ebitdamargin, 10)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f22mpd_f22_machinery_pricing_durability_resil_w10_base_v150_signal(grossmargin, cor, revenue, closeadj):
    base = _f22_margin_input_resilience(grossmargin, cor, revenue, 10)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22mpd_f22_machinery_pricing_durability_floor_range_252d_base_v076_signal,
    f22mpd_f22_machinery_pricing_durability_score_range_252d_base_v077_signal,
    f22mpd_f22_machinery_pricing_durability_resil_range_252d_base_v078_signal,
    f22mpd_f22_machinery_pricing_durability_floor_max_252d_base_v079_signal,
    f22mpd_f22_machinery_pricing_durability_score_max_252d_base_v080_signal,
    f22mpd_f22_machinery_pricing_durability_resil_max_252d_base_v081_signal,
    f22mpd_f22_machinery_pricing_durability_floor_min_252d_base_v082_signal,
    f22mpd_f22_machinery_pricing_durability_score_min_252d_base_v083_signal,
    f22mpd_f22_machinery_pricing_durability_score_cv_252d_base_v084_signal,
    f22mpd_f22_machinery_pricing_durability_floor_cv_252d_base_v085_signal,
    f22mpd_f22_machinery_pricing_durability_resil_cv_252d_base_v086_signal,
    f22mpd_f22_machinery_pricing_durability_score_diff_21d_base_v087_signal,
    f22mpd_f22_machinery_pricing_durability_score_diff_63d_base_v088_signal,
    f22mpd_f22_machinery_pricing_durability_floor_diff_21d_base_v089_signal,
    f22mpd_f22_machinery_pricing_durability_floor_diff_63d_base_v090_signal,
    f22mpd_f22_machinery_pricing_durability_resil_diff_21d_base_v091_signal,
    f22mpd_f22_machinery_pricing_durability_resil_diff_63d_base_v092_signal,
    f22mpd_f22_machinery_pricing_durability_score_streak_pos_base_v093_signal,
    f22mpd_f22_machinery_pricing_durability_floor_above_quantile_base_v094_signal,
    f22mpd_f22_machinery_pricing_durability_resil_below_quantile_base_v095_signal,
    f22mpd_f22_machinery_pricing_durability_score_ema21_base_v096_signal,
    f22mpd_f22_machinery_pricing_durability_floor_ema21_base_v097_signal,
    f22mpd_f22_machinery_pricing_durability_resil_ema21_base_v098_signal,
    f22mpd_f22_machinery_pricing_durability_score_w63_base_v099_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w63_base_v100_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w63_base_v101_signal,
    f22mpd_f22_machinery_pricing_durability_score_w504_base_v102_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w504_base_v103_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w504_base_v104_signal,
    f22mpd_f22_machinery_pricing_durability_score_w42_base_v105_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w42_base_v106_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w42_base_v107_signal,
    f22mpd_f22_machinery_pricing_durability_score_w189_base_v108_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w189_base_v109_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w189_base_v110_signal,
    f22mpd_f22_machinery_pricing_durability_score_w378_base_v111_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w378_base_v112_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w378_base_v113_signal,
    f22mpd_f22_machinery_pricing_durability_score_inv_base_v114_signal,
    f22mpd_f22_machinery_pricing_durability_floor_inv_base_v115_signal,
    f22mpd_f22_machinery_pricing_durability_resil_inv_base_v116_signal,
    f22mpd_f22_machinery_pricing_durability_score_x_revenue_base_v117_signal,
    f22mpd_f22_machinery_pricing_durability_floor_x_revenue_base_v118_signal,
    f22mpd_f22_machinery_pricing_durability_resil_x_revenue_base_v119_signal,
    f22mpd_f22_machinery_pricing_durability_score_cross_21_252_base_v120_signal,
    f22mpd_f22_machinery_pricing_durability_floor_cross_21_252_base_v121_signal,
    f22mpd_f22_machinery_pricing_durability_resil_cross_21_252_base_v122_signal,
    f22mpd_f22_machinery_pricing_durability_score_ema_dev_base_v123_signal,
    f22mpd_f22_machinery_pricing_durability_floor_ema_dev_base_v124_signal,
    f22mpd_f22_machinery_pricing_durability_resil_ema_dev_base_v125_signal,
    f22mpd_f22_machinery_pricing_durability_score_w63_z_base_v126_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w63_z_base_v127_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w63_z_base_v128_signal,
    f22mpd_f22_machinery_pricing_durability_score_sqrt_base_v129_signal,
    f22mpd_f22_machinery_pricing_durability_score_log_base_v130_signal,
    f22mpd_f22_machinery_pricing_durability_score_sq_base_v131_signal,
    f22mpd_f22_machinery_pricing_durability_floor_x_cor_base_v132_signal,
    f22mpd_f22_machinery_pricing_durability_resil_x_cor_base_v133_signal,
    f22mpd_f22_machinery_pricing_durability_score_x_cor_base_v134_signal,
    f22mpd_f22_machinery_pricing_durability_floor_minus_gm_base_v135_signal,
    f22mpd_f22_machinery_pricing_durability_score_above_zero_base_v136_signal,
    f22mpd_f22_machinery_pricing_durability_floor_above_zero_base_v137_signal,
    f22mpd_f22_machinery_pricing_durability_resil_above_1_base_v138_signal,
    f22mpd_f22_machinery_pricing_durability_score_count_pos_base_v139_signal,
    f22mpd_f22_machinery_pricing_durability_floor_count_pos_base_v140_signal,
    f22mpd_f22_machinery_pricing_durability_resil_count_low_base_v141_signal,
    f22mpd_f22_machinery_pricing_durability_triple_w2_base_v142_signal,
    f22mpd_f22_machinery_pricing_durability_triple_mean_252d_base_v143_signal,
    f22mpd_f22_machinery_pricing_durability_triple_std_252d_base_v144_signal,
    f22mpd_f22_machinery_pricing_durability_triple_rank_252d_base_v145_signal,
    f22mpd_f22_machinery_pricing_durability_score_w21_base_v146_signal,
    f22mpd_f22_machinery_pricing_durability_floor_w21_base_v147_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w21_base_v148_signal,
    f22mpd_f22_machinery_pricing_durability_score_w10_base_v149_signal,
    f22mpd_f22_machinery_pricing_durability_resil_w10_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_MACHINERY_PRICING_DURABILITY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f22_machinery_pricing_durability_base_076_150_claude: {n_features} features pass")
