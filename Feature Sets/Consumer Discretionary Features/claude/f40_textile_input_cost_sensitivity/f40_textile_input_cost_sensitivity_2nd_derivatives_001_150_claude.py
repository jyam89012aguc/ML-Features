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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f40_cor_to_revenue(cor, revenue):
    # Cost of revenue as fraction of revenue (input intensity)
    return cor / revenue.replace(0, np.nan)


def _f40_margin_input_sensitivity(grossmargin, cor, w):
    # Change in margin per change in cor (negative-correlation proxy)
    gm_chg = grossmargin.diff(w)
    cor_chg = cor.pct_change(w)
    return gm_chg / cor_chg.replace(0, np.nan).abs()


def _f40_pass_through_score(grossmargin, cor, revenue, w):
    # Pass-through: positive if revenue rises with cor while margin holds
    rev_g = revenue.pct_change(w)
    cor_g = cor.pct_change(w)
    gm_chg = grossmargin.diff(w)
    return (rev_g - cor_g) + gm_chg


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v001_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v002_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v003_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v004_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v005_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v006_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v007_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v008_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v009_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v010_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v011_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v012_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v013_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v014_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v015_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v016_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v017_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v018_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v019_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v020_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v021_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v022_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v023_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v024_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v025_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v026_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v027_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v028_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v029_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v030_signal(cor, revenue, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v031_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v032_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v033_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v034_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v035_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v036_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v037_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v038_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v039_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v040_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v041_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v042_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v043_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v044_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v045_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v046_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v047_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v048_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v049_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v050_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v051_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v052_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v053_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v054_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v055_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v056_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v057_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v058_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v059_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v060_signal(grossmargin, cor, closeadj):
    base = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v061_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v062_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v063_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v064_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v065_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v066_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v067_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v068_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v069_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v070_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v071_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v072_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v073_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v074_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v075_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v076_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v077_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v078_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v079_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v080_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v081_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v082_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v083_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v084_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v085_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v086_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v087_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v088_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v089_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v090_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v091_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v092_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v093_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v094_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v095_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v096_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 21) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v097_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v098_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v099_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v100_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v101_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v102_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 63) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v103_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v104_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v105_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v106_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v107_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v108_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 126) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v109_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v110_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v111_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v112_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v113_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v114_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 252) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v115_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v116_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v117_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v118_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v119_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v120_signal(cor, revenue, grossmargin, closeadj):
    base = _mean(_f40_cor_to_revenue(cor, revenue), 378) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v121_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v122_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v123_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v124_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v125_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v126_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 21) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v127_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v128_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v129_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v130_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v131_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v132_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 63) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v133_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v134_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v135_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v136_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v137_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v138_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 126) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v139_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v140_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v141_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v142_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v143_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v144_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 252) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v145_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v146_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v147_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v148_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v149_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v150_signal(grossmargin, cor, revenue, closeadj):
    base = _f40_pass_through_score(grossmargin, cor, revenue, 378) * grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v001_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v002_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v003_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v004_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v005_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_slope_v006_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v007_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v008_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v009_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v010_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v011_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_slope_v012_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v013_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v014_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v015_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v016_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v017_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_slope_v018_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v019_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v020_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v021_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v022_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v023_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_slope_v024_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v025_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v026_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v027_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v028_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v029_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_slope_v030_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v031_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v032_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v033_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v034_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v035_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_slope_v036_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v037_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v038_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v039_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v040_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v041_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_slope_v042_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v043_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v044_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v045_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v046_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v047_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_slope_v048_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v049_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v050_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v051_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v052_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v053_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_slope_v054_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v055_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v056_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v057_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v058_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v059_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_slope_v060_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v061_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v062_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v063_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v064_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v065_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_slope_v066_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v067_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v068_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v069_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v070_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v071_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_slope_v072_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v073_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v074_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v075_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v076_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v077_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_slope_v078_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v079_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v080_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v081_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v082_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v083_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_slope_v084_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v085_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v086_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v087_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v088_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v089_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_slope_v090_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v091_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v092_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v093_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v094_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v095_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_slope_v096_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v097_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v098_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v099_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v100_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v101_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_slope_v102_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v103_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v104_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v105_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v106_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v107_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_slope_v108_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v109_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v110_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v111_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v112_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v113_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_slope_v114_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v115_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v116_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v117_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v118_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v119_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_378d_slope_v120_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v121_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v122_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v123_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v124_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v125_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_21d_slope_v126_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v127_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v128_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v129_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v130_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v131_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_63d_slope_v132_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v133_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v134_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v135_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v136_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v137_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_126d_slope_v138_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v139_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v140_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v141_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v142_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v143_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_252d_slope_v144_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v145_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v146_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v147_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v148_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v149_signal,
    f40tic_f40_textile_input_cost_sensitivity_ptxgm_378d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_TEXTILE_INPUT_COST_SENSITIVITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_cor_to_revenue", "_f40_margin_input_sensitivity", "_f40_pass_through_score",)
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
    print(f"OK f40_textile_input_cost_sensitivity_slope_001_150_claude: {n_features} features pass")
